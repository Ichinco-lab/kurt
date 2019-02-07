##################################################################################
#KurtToCSV Documentation                                                         #
##################################################################################
"""------------------------------Quick Start-----------------------------------"""
from KurtToCSV import KurtToCSV				#importing the library

scratchFile = "my_scratch_file.sb2"			#the input file
outFile = "my_output_file.csv"				#the output file

converter = KurtToCSV()				   	#initialize KurtToCSV	

converter.KurtToCSVconvert(outFile,scratchFile,'w')	#write 'w', append 'a'
#calling this will automatically generate the csv file


##################################################################################
"""-------------------------------Functions------------------------------------"""



"""converts the scratch file fromFile to csv format and stores relevant data
in csv file toFile."""
	def KurtToCSVconvert(self, toFile, fromFile, mode):

"""Default Constructor"""
	def __init__(self):





"""---------------------------Helper Functions---------------------------------"""


"""Returns the name or 'id' of the project"""
	def KurtToCSVgetFileName(self,project):


"""Returns the name or 'id' of the sprite"""
	def KurtToCSVgetSpriteName(self,sprite):

"""returns if a sprite is the stage (the background) or a regular sprite"""
	def KurtToCSVSpriteOrBackground(self,sprite):

"""returns the string form of the event in a script"""
	def KurtToCSVgetEvent(self,script):

"""returns number of blocks by type in a script"""
	def KurtToCSVgetBlocks(self, script):

"""returns function name if is a def script else returns NULL"""	
	def KurtToCSVgetFunctionName(self, script):

"""returns the number of times a given movement is contained 
	within a block"""
	def KurtToCSVfindNumInstancesInStr(self,strBlock,movement):

"""returns the x position of the script"""
	def KurtToCSVgetXPosition(self,script):

"""returns the y position of the script"""
	def KurtToCSVgetYPosition(self,script):

"""returns the number of blocks in a script"""
	def KurtToCSVgetScriptLength(self,script):

"""returns the maximum level of nesting found in a script"""
	def KurtToCSVgetScriptNestLevel(self,script):

"""function assumes you began at the first single quote and takes every character
after it until the next single quote

for example: given string "stuff='Hello World!'", if you called 
KurtToCSVgetToken(string,6) then the return string would be "Hello World" """
	def KurtToCSVgetToken(self,string,index):

"""returns a formatted string of a script"""
	def KurtToCSVgetScriptString(self, script):

"""returns an array. for each script in the sprite there is an entry
within the array which includes the function name if the script is a
function or NULL otherwise"""
	def KurtToCSVgetFunctions(self, sprite):

"""return an array with the amount of times each function is called within a sprite"""
	def KurtToCSVgetFunctionCounts(self, functions, sprite):
