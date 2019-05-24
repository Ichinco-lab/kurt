"""
RUN IN PYTHON 3
(DictWriter jumbles dictionaries in python 2)
"""
import csv
import processBlocks
import code_stacks


"""
	stub function used for testing
"""
def processThing(line):
	return {"a":0, "b":1, "c":2}





"""
@param: rawFile
	The unprocessed csv file
@param: outFile
	The csv file to write the processed results of rawFile
@param: process
	The function with which to process the rawFile with
"""
def preProcess(rawFile, outFile, process):
	try: #Opening the file reader and writer
		rawReader = open(rawFile,"r")
		reader = csv.DictReader(rawReader)
		rawWriter = open(outFile, "w")
		writer = None

	except:
		print( "Processor Failed To Open File.")
		print( "Exiting Function With Value of 1.")
		return 1
	writerInit = False

	for line in reader:
		outLine = process(line)
		outLine.update({"project_id":line["project_id"]})
		if writer is None:
			writer = csv.DictWriter(rawWriter, fieldnames=outLine.keys())
			writer.writeheader()
			writerInit = True
		writer.writerow(outLine)







	try: #Closing the file reader and writer
		if writerInit:
			rawWriter.close()
		rawReader.close()
	except:
		print( "Processor Failed To Close File.")
		print( "Exiting Function With Value of 1.")
		return 1
	return 0

#used for testing
#preProcess("project_sprites/sprites.csv","out.csv",processThing)
def preProcessAll():
	print "Generating CSV File for Logical Thinking, Flow Control, and User Interactivity:"
	preProcess("RawData/project_blocks/project_blocks.csv","ProcessedData/logical_thinking_flow.csv",processBlocks.process)
	#print "Generating CSV File for Abstraction and Parallelism"
	#preProcess("RawData/stack.csv","ProcessedData/abstraction_parallelism.csv",code_stacks.getCodeStackFields)
	print "Finished All:"

def preProcessAll(blocksInFile, blocksOutFile, spriteInFile, spriteOutFile):
	print "Generating CSV File from " + blocksInFile
	try:
		if preProcess(blocksInFile,blocksOutFile,processBlocks.process):
			error
		print "Fields Logical Thinking, Flow Control, User Interactivity, Synchronization"
		print "Saved to " + blocksOutFile
	except:
		print "Failure: Resultant File " + blocksOutFile
		print "May Be Missing or Incomplete"

	"""print ""
	print "Generating CSV File from " + spriteInFile
	try:
		if preProcess(spriteInFile,spriteOutFile,code_stacks.getCodeStackFields):
			error
		print "Fields Abstraction and Parallelism"
		print "Saved to " + spriteOutFile
	except:
		print "Failure: Resultant File " +spriteOutFile
		print "May Be Missing or Incomplete" """



preProcessAll("RawData/project_blocks/project_blocks.csv","ProcessedData/logical_thinking_flow.csv","RawData/stack.csv","ProcessedData/abstraction_parallelism.csv")
