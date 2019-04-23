
"""
Requires:
"""
import csv










def process(project_dictionary):
	return [0,0,0,0,0]




def formatScratchData(projects_,project_blocks_):






	projects = open(projects_, "rb")
	project_blocks = open(project_blocks_, "rb")
	readProject = csv.DictReader(projects) 
	readBlocks = csv.DictReader(project_blocks) 
	projectArray = []	
	ids = {}
	formattedData = []
	for line in readProject:
		projectArray.append({'user_id': line['user_id'], 'project_id': line['project_id']})
		if str(line['user_id']) not in ids:
			ids[str(line['user_id'])] = len(ids)
			formattedData.append([])
	#print len(projectArray)
	counter = 0
	for line in readBlocks:
		"""line = projectArray[lineNum] #The Easier to read version of the
		formatLine = ids[str(line['user_id'])] #uncommented loop code
		formattedData[formatLine].insert(0, process(blockArray[lineNum]))"""
		formattedData[ids[str(projectArray[counter]['user_id'])]].insert(0, process(line))
		counter += 1
	return formattedData
	
"""print line['project_id']
print line['user_id']
print line['date_created']
break"""




data = formatScratchData("projects/projects.csv", "project_blocks/project_blocks.csv")
for line in data:
		if len(line) > 0:
			print line

"""
	project = { 
		"project_id",
	}
"""




	

"""my_dictionary = {
		project_id	
		user_id	
		date_created	
 }"""
















