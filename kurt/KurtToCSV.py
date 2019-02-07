""""importing kurt and local files. Ideally I want the more generic path
	but python hasn't been cooperating so I need fix this later"""
import sys
#sys.path.append("/Users/michelle_ichinco/Documents/Research/kurt/tests")
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
		return event



	"""returns the number of movement blocks in a script"""
	def KurtToCSVgetNumMovementBlocks(self, script):
		movement = 0
		for block in script:
			movement += self.KurtToCSVisMovementBlock(block)
		return movement


	"""helper function returns true if a block is a movement block
		returns false otherise"""
	def KurtToCSVisMovementBlock(self,block):
		movements = {'forward:', 'turnRight:', 'turnLeft:', 'heading:', 'pointTowards:', 'gotoX:y:', 'gotoSpriteOrMouse:', 'glideSecs:toX:y:elapsed:from:', 'changeXposBy:', 'xpos:', 'changeYposBy:', 'ypos:', 'bounceOffEdge', 'setRotationStyle'}
		count = 0
		strBlock = block.__repr__()
		for movement in movements:
			count += self.KurtToCSVfindNumInstancesInStr(strBlock,movement)
		return count

	"""returns the number of times a given movement is contained
	within a block"""
	def KurtToCSVfindNumInstancesInStr(self,strBlock,movement):
		words = strBlock.split()
		count = 0
		for word in words:
			if movement in word:
				count += 1
		return count


	"""returns the number of blocks in a script"""
	#must be refactored
	def KurtToCSVgetScriptLength(self,script):
		scriptString = script.__repr__()
		lines = scriptString.splitlines()
		numLines = len(lines)
		for line in lines:
			if "doRepeat" in line:
				numLines -= 1
			if "doIfElse" in line:
				numLines -= 4
			elif "doIf" in line:
				numLines -= 2
			if "doUntil" in line:
				numLines -= 2
		return numLines - 1


	"""returns the maximum level of nesting found in a script"""
	#TO DO
	def KurtToCSVgetScriptNestLevel(self,script):
		#3 potential methods:
		#either use a recursie function to keep track of nesting
		#or find nesting based on indentation (kurt uses 4 spaces)
		#or figure out if kurt has a built in way to determine number of blocks
		return 0



	"""converts the scratch file fromFile to csv format and stores relevant data
		in csv file toFile"""
	def KurtToCSVconvert(self, toFile, fromFile):
		project = kurt.Project.load(fromFile)
		f = open(toFile, 'w')
		f.write("project,object,backgroundOrSprite,script_id,event," + "levelsOfNesting,numberOfMovementBlocks,lengthOfScript,script\n")
		for sprite in project.sprites + [project.stage]:
			scriptCounter = 0
			for script in sprite.scripts:
				line = self.KurtToCSVgetFileName(project) + ","
				line += self.KurtToCSVgetSpriteName(sprite) + ","
				line += self.KurtToCSVSpriteOrBackground(sprite) + ","
				line += str(scriptCounter) + ","
				line += self.KurtToCSVgetEvent(script) + ","
				line += str(self.KurtToCSVgetScriptNestLevel(script)) + ","
				line += str(self.KurtToCSVgetNumMovementBlocks(script)) + ","
				line += str(self.KurtToCSVgetScriptLength(script)) + ',"'
				line += script.__repr__() + '"\n'
				f.write(line)
				scriptCounter += 1
		return


""" TO DO/ BUGS
1. Calculate levels of nesting. This is complicated by the fact that any nested
block segment only counts as 1 block ex.
if x:
	block1
	block2
	...
else:
	block3
	block4
	...

In the example above, the if else statement is stored within the script as a
single block

2. continue refactor the getScriptLength function due to finding the issues
	documented directly above after initially coding said function
	--improved by counting the new lines. Should work much better
	than the previous version although still needs tweaking due to being slightly
	off in control statements. (some use different amounts of newlines when
	they have blocks inside them than if not) To be clear, this could be fixed
	if I tested to see if a line contains a block keyword but this seems
	inefficient and there is most certainly a better way.--
"""
