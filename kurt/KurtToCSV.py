""""importing kurt and local files. Ideally I want the more generic path 
	but python hasn't been cooperating so I need fix this later"""
import array as arr
import sys
sys.path.append("/home/aaron/Programs/python/kurt/")
import kurt

class KurtToCSV:


	"""Default Constructor"""
	def __init__(self):
		return
	

	"""Returns the name or 'id' of the project"""
	def KurtToCSVgetFileName(self,project):
		return project.name


	"""Returns the name or 'id' of the sprite"""
	def KurtToCSVgetSpriteName(self,sprite):
		return sprite.name


	"""returns if a sprite is the stage or a regular sprite"""
	def KurtToCSVSpriteOrBackground(self,sprite):
		if self.KurtToCSVgetSpriteName(sprite) == "Stage": 
			return "STAGE"
		return "SPRITE"


	"""returns the string form of the event in a script"""
	def KurtToCSVgetEvent(self,script):
		validEventsList = {'whenGreenFlag' ,'whenKeyPressed', 'whenClicked', 'whenSensorGreaterThan', 'whenSceneStarts', 'whenIReceive'}
		className = script.__class__.__name__
		comment = "'Comment'"
		if className.__repr__() == comment:
			return "NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,"
		#the 1st block always contains the event
		event = script[0].__repr__()	
		#here we strip excess characters from the event
		event = event[2:] #since the event/hat block is never indented this
		#line will always work as intended
		endStrip = 0	#we never need the 1st 2 characters
		#in some cases there is more in the block
		#than just the event so we can't just strip [2:-2]
		#this loop deals with this edge cases
		#while still working for the base case
		for character in event:
			if character == "'":
				break
			endStrip += 1
		event = event[0:endStrip]
		if event not in validEventsList:
			event = 'NULL'
		return event
	
	"""returns number of blocks by type in a script"""
	def KurtToCSVgetBlocks(self, script):
		operators = {"'+'","'-'", "'*'","'/'", 'randomFrom:to:', "'<'", "'='", "'<'", "'&'", "'|'", "'not'", 'concatenate:with', 'letter:of:', 'stringLength:', "'%'", 'rounded', 'competeFunction:of:'}
		events = {'whenGreenFlag', 'whenClicked', 'whenIReceive', 'whenSceneStarts', 'whenKeyPressed', 'whenSensorGreaterThan', 'broacast:', 'doBroadcastAndWait'}
		sensing = {'touching', 'color:sees:', 'distanceTo:', 'timestamp', 'doAsk', 'setVideoState', 'setVideoTransparency', 'timer', 'answer', 'keyPressed:', 'mousePressed', 'soundLevel', 'mouseX', 'mouseY', 'senseVideoMotion', 'getAttribute:of:', 'timeAndDate', 'getUserName'}
		controls = {'whenCloned', 'deleteClone', 'createCloneOf', 'createCloneOf', 'wait:elapsed:from:', 'doRepeat', 'doIf', 'doWaitUntil', 'doUntil', 'stopScripts'}
		dataBlocks = {'setVar:to:', 'changeVar:by:', 'showVariable:', 'hideVariable:', 'append:toList:', 'deleteLine:ofList:', 'insert:at:ofList:', 'setLine:ofList:to:', 'showList:', 'hideList:', 'list:contains:', 'lineCountOfList:', 'getLine:ofList'}
		penBlocks = {'pen', 'Pen', 'stampCostume'}	
		sounds = {'laySound:', 'doPlaySoundAndWait', 'stopAllSounds', 'layDrum', 'rest:elapsed:from:', 'noteOn:duration:elapsed:from:', 'instrument:', 'changeVolumeBy:', 'setVolumeTo:', 'changeTempoBy:', 'setTempoTo:','volume','tempo'}
		looks = {'say:', 'think:', 'show', 'hide', 'lookLike:', 'nextCostume', 'startScene', 'changeGraphicEffect:', 'setGraphicEffect:', 'filterReset', 'changeSizeBy:', 'setSizeTo:', 'comeToFront', 'goBackByLayers:', 'scale', 'sceneName', 'costumeIndex'}	
		movements = {'forward:', 'turnRight:', 'turnLeft:', 'heading:', 'pointTowards:', 'gotoX:y:', 'gotoSpriteOrMouse:', 'glideSecs:toX:y:elapsed:from:', 'changeXposBy:', 'xpos:', 'changeYposBy:', 'ypos:', 'bounceOffEdge', 'setRotationStyle'}	
		blockCounts = {'movements':0, 'looks':0, 'sounds':0, 'pens':0, 'datas':0, 'events':0, 'controls':0, 'sensing':0, 'operators':0}
		className = script.__class__.__name__
		comment = "'Comment'"
		if className.__repr__() == comment:
			return "NULL,"
		for block in script:
			strBlocks = block.__repr__()
			for word in strBlocks.split():
				for command in movements:
					if command in word:
						blockCounts['movements'] += 1
				for command in looks:
					if command in word:
						blockCounts['looks'] += 1
				for command in sounds:
					if command in word:
						blockCounts['sounds'] += 1
				for command in penBlocks:
					if command in word:
						blockCounts['pens'] += 1
				for command in dataBlocks:
					if command in word:
						blockCounts['datas'] += 1
				for command in controls:
					if command in word:
						blockCounts['controls'] += 1
				for command in sensing:
					if command in word:
						blockCounts['sensing'] += 1
				for command in events:
					if command in word:
						blockCounts['events'] += 1
				for command in operators:
					if command in word:
						blockCounts['operators'] += 1
		blockCountStr = ""
		for value in blockCounts:
			blockCountStr += str(blockCounts[value]) + ','
		return blockCountStr
	
	"""returns function name if is a def script else returns NULL"""	
	def KurtToCSVgetFunctionName(self, script):
		defScript = 'NULL'
		className = script.__class__.__name__
		comment = "'Comment'"
		if className.__repr__() == comment:
			return "NULL"
		else:
			headerBlock = script[0].__repr__()
			funcRecString = "'procDef'"
			if funcRecString in headerBlock:
				for i in range(len(headerBlock)):
					#print headerBlock[i:i+9]
					if headerBlock[i:i+9] == funcRecString:
						defScript = self.KurtToCSVgetToken(headerBlock,i+14)
						break
				
		return defScript			
	
		
	"""returns the number of times a given movement is contained 
	within a block"""
	def KurtToCSVfindNumInstancesInStr(self,strBlock,movement):
		words = strBlock.split()
		count = 0
		for word in words:
			if movement in word:
				count += 1
		return count  
	

	"""returns the x position of the script"""
	def KurtToCSVgetXPosition(self,script):
		scriptString = script.__repr__()
		xPos = ''
		strPos = 0
		for i in range(len(scriptString)):
			if scriptString[i:i+4] == "pos=":
				strPos = i + 5
				break
		while scriptString[strPos] != ',':
			xPos += scriptString[strPos]
			strPos += 1
		return xPos


	"""returns the y position of the script"""
	def KurtToCSVgetYPosition(self,script):
		scriptString = script.__repr__()
		yPos = ''
		strPos = 0
		for i in range(len(scriptString)):
			if scriptString[i:i+4] == "pos=":
				strPos = i + 5
				break
		while scriptString[strPos] != ',':
			strPos += 1
		strPos += 1
		while scriptString[strPos] != ')':
			yPos += scriptString[strPos]
			strPos += 1
		return yPos

	"""returns the number of blocks in a script"""
	def KurtToCSVgetScriptLength(self,script):
		scriptString = script.__repr__()
		scriptLength = -2
		for i in range(len(scriptString)):
			if scriptString[i] == '(':
				scriptLength += 1
		return scriptLength
		
		
	"""returns the maximum level of nesting found in a script"""
	def KurtToCSVgetScriptNestLevel(self,script):
		maxNesting = -1
		tempNesting = -1
		strScript = script.__repr__()
		for i in range(len(strScript)):
			if strScript[i] == '[':
				tempNesting += 1
			elif strScript[i] == ']':
				if tempNesting > maxNesting:
					maxNesting = tempNesting
				tempNesting -= 1
		return maxNesting
	"""function assumes you began at the first single quote and takes every character
	after it until the next single quote

	for example:

	given string "stuff='Hello World!'", if you called KurtToCSVgetToken(string,6)
	then the return string would be "Hello World" """
	def KurtToCSVgetToken(self,string,index):
		token = ""		
		endIndex = index+1
		while string[endIndex] != "'":
			token += string[endIndex]
			endIndex += 1
		return token

	"""returns a formatted string of a script"""
	def KurtToCSVgetScriptString(self, script):
		unwantedCharacters = {'[',']','(',')','{','}'}		
		unformattedScript = script.__repr__()
		formattedScript = ""
		for i in range(len(unformattedScript)):
			if unformattedScript[i] == 'u' and unformattedScript[i+1] == "'":
				continue
			elif unformattedScript[i] == ',':
				temp = unformattedScript[i:i+6]
				positionStr = ", pos="	
				isPosStr = True
				for j in range(len(temp)):			
					if temp != positionStr:			
						isPosStr = False
				if isPosStr:
					break
			if unformattedScript[i] == '"':
				formattedScript += "'"
				continue
			if unformattedScript[i] in unwantedCharacters:
				continue
			formattedScript += unformattedScript[i]

		return formattedScript
		
	"""returns an array. for each script in the sprite there is an entry
	within the array which includes the function name if the script is a
	function or NULL otherwise"""
	def KurtToCSVgetFunctions(self, sprite):
		functions = []
		for script in sprite.scripts:
			functions.append(self.KurtToCSVgetFunctionName(script))
			"""tempstr = script[0].__repr__()
			funcDef = "procDef"
			if funcDef in tempstr:
				#todo
				functions.append(self.KurtToCSVgetToken(tempstr,14))
			else:
				functions.append("NULL")"""
		return functions
	"""return an array with the amount of times each function is called within a sprite"""
	def KurtToCSVgetFunctionCounts(self, functions, sprite):
		functionCounts = []
		#init all values of array to -1. This does 2 things
		#1. non functions will remain counted as -1 calls
		#2. actual functions will have a minimum of 0 calls
		for x in range(len(functions)):
			functionCounts.append(-1)
		for script in sprite.scripts:
			scriptString = script.__repr__().split()
			for word in scriptString:
				for i in range(len(functions)):
					if functions[i] != "NULL" and functions[i] in word:
						functionCounts[i] += 1
		return functionCounts
		




	"""converts the scratch file fromFile to csv format and stores relevant data
		in csv file toFile"""
	def KurtToCSVconvert(self, toFile, fromFile, mode):
		project = kurt.Project.load(fromFile)
		f = open(toFile, mode)
		if mode == 'w':
			f.write("project,object,backgroundOrSprite,script_id,event," + "levelsOfNesting,numberOfMovementBlocks,numberOfLookBlocks," + "numberOfSoundBlocks,numberOfPenBlocks,numberOfDataBlocks," + "numberOfEventBlocks,numberOfControlBlocks,numberOfSensingBlocks," + "numberOfOperatorBlocks,lengthOfScript,function,timesCalled,xPos,yPos,script\n")
		for sprite in project.sprites + [project.stage]:
			scriptCounter = 0

			functions = self.KurtToCSVgetFunctions(sprite)
			functionCounts = self.KurtToCSVgetFunctionCounts(functions ,sprite)
			
			for script in sprite.scripts:	
				#fields useful to identify the script specifically
				line = self.KurtToCSVgetFileName(project) + ","
				line += self.KurtToCSVgetSpriteName(sprite) + ","
				line += self.KurtToCSVSpriteOrBackground(sprite) + ","
				line += str(scriptCounter) + ","
				
				#determines the activation condition of a script
				line += self.KurtToCSVgetEvent(script) + ","
				
				#determines how many levels of nesting were used in a script
				line += str(self.KurtToCSVgetScriptNestLevel(script)) + ","
				
				#counts the amount of times a type of block was used
				#does this for all block types
				line += self.KurtToCSVgetBlocks(script)
				
				#determines the total number of blocks in a script
				line += str(self.KurtToCSVgetScriptLength(script)) + ","
				
				#determines the function name of a script if applicable	
				line += functions[scriptCounter] + ","
				#finds out how many times a function is called
				line += str(functionCounts[scriptCounter]) + ","
				
				#returns where a script is physically located in the editor
				line += self.KurtToCSVgetXPosition(script) + ","
				line += self.KurtToCSVgetYPosition(script) + ","
				
				#returns the actual script
				line += '"'+ self.KurtToCSVgetScriptString(script) + '"\n'
				f.write(line)
				scriptCounter += 1
		f.close()
		return
