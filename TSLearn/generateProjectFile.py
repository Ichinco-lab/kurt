"""
RUN IN PYTHON 3
(DictWriter jumbles dictionaries in python 2)
"""
import csv


"""
@param: headCSV
	The path to the first csv file to link
@param: nonHeadCSVS
	An array filled with the paths of all other csv files
	you want to link
@param: outFile
	The CSV file in which to place the linked project information
"""
def generateprojectsFile(headCSV, nonHeadCSVS, outFile):
	try: #Opening the file reader and writer
		rawReader = open(headCSV,"r")
		reader = csv.DictReader(rawReader)
		rawWriter = open(outFile, "w")
		writer = None
	except:
		print( "Processor Failed To Open Head File.")
		print( "Exiting Function With Value of 1.")
		return 1

	projects = {}
	maxLength = 0
	lengthAdded = False
	for line in reader:
		if not lengthAdded:
			maxLength += len(line.keys())
			lengthAdded = True
		projects.update({line['project_id']:line})
	rawReader.close()
	for csvFile in nonHeadCSVS:
		lengthAdded = False
		success = True
		try:
			rawReader = open(csvFile, "r")
			reader = csv.DictReader(rawReader)
		except:
			success = False
			print( "Failed to open " + csvFile + " Skipping")
		if success:
			for line in reader:
				project_id = line['project_id']
				del line['project_id']
				try:
					projects[str(project_id)].update(line)
				except:
					continue
			rawReader.close()
			rawReader = open(csvFile, "r")
			reader = csv.DictReader(rawReader)
			for line in reader:
				del line['project_id']
				maxLength += len(line.keys())
				break
	writeInit = False	
	for projectKey in projects.keys():
		if len(projects[projectKey].keys()) is maxLength:
			if writer is None:
				try:
					writer = csv.DictWriter(rawWriter, fieldnames=projects[projectKey].keys())
					writer.writeheader()
					writeInit = True
				except:
					print( "Write Failed")
					print( "Exiting Function With Value of 1.")
					return 1
			writer.writerow(projects[projectKey])
	if writeInit:
		rawWriter.close()
	return 0



generateprojectsFile("out.csv", ["out2.csv"], "out3.csv")

		
