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




"""
	Generates preprocessed verions of blocksInFile and stackInFile
	and saves the results in bllocksOutFile and stackOutFile respectively
"""
def preProcessAll(blocksInFile, blocksOutFile, stackInFile, stackOutFile):
	print "Generating CSV File from " + blocksInFile
	try:
		if preProcess(blocksInFile,blocksOutFile,processBlocks.process):
			error
		print "Fields Logical Thinking, Flow Control, User Interactivity,"
		print "       Synchronization, Data Representation"
		print "Saved to " + blocksOutFile
	except:
		print "Failure: Resultant File " + blocksOutFile
		print "May Be Missing or Incomplete"

	print ""
	print "Generating CSV File from " + stackInFile
	try:
		if preProcess(stackInFile,stackOutFile,code_stacks.getCodeStackFields):
			error
		print "Fields Abstraction and Parallelism"
		print "Saved to " + stackOutFile
	except:
		print "Failure: Resultant File " +stackOutFile
		print "May Be Missing or Incomplete"



#preProcessAll("RawData/project_blocks/project_blocks.csv","ProcessedData/logical_thinking_flow.csv","RawData/stack.csv","ProcessedData/abstraction_parallelism.csv")
