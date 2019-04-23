
"""
Requires:
"""
import csv









"""
@param: project_dictionary
	a dictionary format version of a line from the scratch csv dataset we are using
@return: an array filled with int values. for now this is just a stub function which
	returns an array [0,0,0,0,0]
"""
def process(project_dictionary):
	return [0,0,0,0,0]



"""
@param: projects_
	the projects csv file; what we care about is it having a user_id field and
	a project_id field.
@param: project_blocks_
	the complementary csv file to the projects csv file; must have the project_id
	field and all other scratch datafields. Each line here should correspond to a
	line in the projects csv file directly as the project_id field from each should
	match on each line

"""
def formatScratchData(projects_,project_blocks_):
	projects = open(projects_, "rb")#initialize the csv readers
	project_blocks = open(project_blocks_, "rb")
	readProject = csv.DictReader(projects) 
	readBlocks = csv.DictReader(project_blocks) 
	projectArray = []#used to store projects_['user_id'] and projects_['project_id']
	ids = {}	#Stores location in formattedData to insert processed data by user id
	formattedData = []#stores processed data by user id
	for line in readProject:
		projectArray.append({'user_id': line['user_id'], 'project_id': line['project_id']})
		if str(line['user_id']) not in ids:
			ids[str(line['user_id'])] = len(ids)
			formattedData.append([])
	#print len(projectArray)
	#for every project get its processed form and insert into the correct 
	#spot in formattedData based on the user id. Since newer projects sets
	#appear earlier in the dataset we have to insert at the beginning of a
	#time series rather than append to the end of one.
	#This is also the area we are most likely to run of heap space
	counter = 0
	for line in readBlocks:
		"""line = projectArray[counter] #The Easier to read version of the
		formatLine = ids[str(line['user_id'])] #uncommented loop code
		formattedData[formatLine].insert(0, process(line))
		Keeping the harder to read version because efficiency is priority here"""
		
		formattedData[ids[str(projectArray[counter]['user_id'])]].insert(0, process(line))
		counter += 1
	return formattedData


#main
data = formatScratchData("projects/projects.csv", "project_blocks/project_blocks.csv")
for line in data:
		#if len(line) > 0:
		print line

"""
#fields we care about especially for project_blocks and projects
project_blocks = { 
		"project_id"
	}
projects = {
		project_id	
		user_id		
 """
















