import csv
import numpy as np
from cluster1 import process

"""
@param: project_dictionary
	a dictionary format version of a line from the scratch csv dataset we are using
@return: an array filled with int values. for now this is just a stub function which
	returns an array [0,0,0,0,0,0,0]
"""
#def process(project_dictionary):
#	return [0,0,0,0,0,0,0]



"""
@param: projects_
	the projects csv file; what we care about is it having a user_id field and
	a project_id field.
@param: project_blocks_
	the complementary csv file to the projects csv file; must have the project_id
	field and all other scratch datafields. Each line here should correspond to a
	line in the projects csv file directly as the project_id field from each should
	match on each line
@param: min_projects
	the minimum number of projects for a user for the time series of their programs to
	be included in the returned formatted dataset
@return: an array of length 2
	The 1st index is the user id.
	The 2nd index (result[1]) is a time series dataset where each time series
	has at least min_projects projects. This corresponds with the user id
"""
def formatScratchData(projects_, project_blocks_, min_projects, enableDebugText):
	#########DEBUG STATEMENT: Initialize CSV Readers############################
	if (enableDebugText):
		print "Stage [1/5] Initializing CSV Readers:"
	try:
		projects = open(projects_, "rb")#initialize the csv readers
		project_blocks = open(project_blocks_, "rb")
		readProjects = csv.DictReader(projects)
		readBlocks = csv.DictReader(project_blocks)
	except: #If a file failed to open then print error msg and return empty list
		if (enableDebugText):
			print "ERROR: File Not Found, Returning Empty List"
		return [[],[]]
	projectTable = {} #projectTable[project_id] = {user_id, project_id}
	ids = {}		  #ids[user_id] =             {project_count, index}
	formattedData = [[],[]]    	#formattedData[0] -> user ids
								#formattedData[1] -> processed project data
	#########DEBUG STATEMENT: Intialize Project Lists###########################
	print "testing cluster`"
	for line in readBlocks:
		process(line)

	if (enableDebugText):
		print "Stage [2/5] Initializing Project Lists:"
	for project in readProjects:#add project to projectTable
		projectTable[project['project_id']] = {'user_id':project['user_id'], 'project_id':project['project_id']}
		if project['user_id'] not in ids:#if project's user id not in id list
			ids[project['user_id']] = {'project_count':1, 'index':len(ids)}
			formattedData[0].append(project['user_id'])
			formattedData[1].append([])#add project user id to id list
		else:
			ids[project['user_id']]['project_count'] += 1
	#########DEBUG STATEMENT: Building Time Series##############################
	if (enableDebugText):
		print "Stage [3/5] Building Time Series:"
	for line in readBlocks:
		#for each project if associated user has at least min_projects
		if ids[projectTable[line['project_id']]['user_id']]['project_count'] >= min_projects:
			formattedData[1][ids[projectTable[line['project_id']]['user_id']]['index']].insert(0,cluster1.process(line)) #then process project and insert at beginning
								   #of associated time series
			#we insert at beginning because in the dataset, more recent projetcs
			#get processed before older projects which is the opposite order
			#as we want to create a time series

	#########DEBUG STATEMENT: Removing Time Series That Are Too Small###########
	if (enableDebugText):
		print "Stage [4/5] Removing Time Series With Less Than " + str(min_projects) + " Projects:"
	i = 0
	while i < len(formattedData[0]):
		if len(formattedData[1][i]) < min_projects:
			formattedData[0].pop(i)
			formattedData[1].pop(i)
			i -= 1
		i += 1
	#########DEBUG STATEMENT: Returning Result##################################
	if (enableDebugText):
		print "Stage [5/5] Returning Result:"
	return formattedData

#main
data = formatScratchData("projects.csv", "project_blocks_small.csv", 4, True)
for i in range(len(data[0])):
	print str(data[0][i]) + ":" + str(data[1][i])
