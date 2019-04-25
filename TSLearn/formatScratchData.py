import csv
import numpy as np

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
"""def formatScratchData(projects_, project_blocks_, min_projects):
	projects = open(projects_, "rb")#initialize the csv readers
	project_blocks = open(project_blocks_, "rb")
	readProjects = csv.DictReader(projects) 
	readBlocks = csv.DictReader(project_blocks) 
	projectTable = []#used to store projects_['user_id'] and projects_['project_id']
	ids = {}	#Stores location in formattedData to insert processed data by user id
	formattedData = []#stores processed data by user id
	counter = np.uint64(0)
	for project in readProjects:
		projectTable.append({'project_id':project['project_id'], 'user_id':project['user_id']})
		if project['user_id'] not in ids:
			ids[project['user_id']] = {'project_count':1, 'index':len(ids)}
			formattedData.append([])
		else:
			ids[project['user_id']]['project_count'] += np.uint64(1)
			
	counter = np.uint64(0)
	for project in readBlocks:
		while int(projectTable[counter]['project_id']) < int(project['project_id']):
			ids[projectTable[counter]['user_id']]['project_count'] -= 1
			counter += np.uint64(1)
		if int(projectTable[counter]['project_id']) == int(project['project_id']):
			
			print projectTable[counter]['project_id'] 
			print project['project_id']
			print
			if ids[projectTable[counter]['user_id']]['project_count'] >= min_projects:
				formattedData[ids[projectTable[counter]['user_id']]['index']].insert(0,process(project))
			counter += np.uint64(1)
		elif int(projectTable[counter]['project_id']) > 1000000:
			print projectTable[counter]['project_id'] 
			print project['project_id']
			print
		
	#for lineNum in range(len(formattedData)):
	#	print str(ids[projectTable[lineNum]['user_id']]['project_count']) + ":" + str(formattedData[lineNum])
"""
def formatScratchData(projects_, project_blocks_, min_projects):
	projects = open(projects_, "rb")#initialize the csv readers
	project_blocks = open(project_blocks_, "rb")
	readProjects = csv.DictReader(projects) 
	readBlocks = csv.DictReader(project_blocks) 
	projectTable = {}
	ids = {}
	formattedData = []
	print "Initializing Project Lists:"
	for project in readProjects:
		projectTable[project['project_id']] = {'user_id':project['user_id'], 'project_id':project['project_id']}
		if project['user_id'] not in ids:
			ids[project['user_id']] = {'project_count':1, 'index':len(ids)}
			formattedData.append([])
		else:
			ids[project['user_id']]['project_count'] += 1

	print "Building Time Series:"
	for line in readBlocks:
		if ids[projectTable[line['project_id']]['user_id']]['project_count'] >= min_projects:
			formattedData[ids[projectTable[line['project_id']]['user_id']]['index']].insert(0,process(line))
			#print projectTable[line['project_id']]['project_id']
			#print line['project_id']
			#print
		
	offset = 0
	"""for user in ids:
		#print ids[user]['project_count']
		ids[user]['index'] -= realignment
		if ids[user]['project_count'] < min_projects:
			formattedData.pop(ids[user]['index'])
			realignment += 1
		else:
			print ids[user]['index']
			print len(formattedData)
			if len(formattedData[ids[user]['index']]) < min_projects:
				formattedData.pop(ids[user]['index'])
				realignment += 1"""
	print "Removing Time Series With Less Than " + str(min_projects) + " Projects:"
	i = 0
	while i < len(formattedData):
		if len(formattedData[i]) < min_projects:
			formattedData.pop(i)
			i -= 1
		i += 1
		
	return formattedData
		
#main
data = formatScratchData("projects/projects.csv", "project_blocks/project_blocks.csv", 4)
for line in data:
	print line
