"""
RUN IN PYTHON 3
(DictWriter jumbles dictionaries in python 2)
"""
import csv








"""
@param: userFile
	The raw user projects csv file that is to say, projects.csv
@param: projectFile
	The file which you created in generateProjectFile.py
@param: outFile
	The CSV file to put the new user project information
	This file will have an equal amount of lines to the file
	created in generateProjectFile.py and if a project id appears
	in one then it will also appear in the other.
"""
def generateUserFile(userFile,projectFile,outFile):
	try: #Opening the file reader and writer
		rawReader = open(userFile,"r")
		reader = csv.DictReader(rawReader)
		rawWriter = open(outFile, "w")
		writer = None

	except:
		print( "Processor Failed To Open User File.")
		print( "Exiting Function With Value of 1.")
		return 1
	users = {}
	for line in reader:
		users.update({
			line['project_id']:{
				'project_id':line['project_id'],
				'user_id':line['user_id']
			}
		})
	rawReader.close()

	try: #Opening the file reader and writer
		rawReader = open(projectFile,"r")
		reader = csv.DictReader(rawReader)
	except:
		print( "Processor Failed To Open Project File.")
		print( "Exiting Function With Value of 1.")
		return 1

	writerInit = False
	for line in reader:
		if writer is None:
			writer = csv.DictWriter(rawWriter, fieldnames=users[line['project_id']].keys())
			writer.writeheader()
			writerInit = True
		writer.writerow(users[line['project_id']])
	try: #Closing the file reader and writer
		if writerInit:
			rawWriter.close()
		rawReader.close()
	except:
		print( "Processor Failed To Close File.")
		print( "Exiting Function With Value of 1.")
		return 1
	return 0


#generateUserFile("RawData/projects/projects.csv", "ProcessedData/project_blocks.csv","ProcessedData/projects.csv")
