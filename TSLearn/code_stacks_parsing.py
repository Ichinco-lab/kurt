"""
Please Run In Python 3
"""
import json
import csv
data_dict={}
totalSpriteCount= 0
emptySpriteCount= 0
knownCondition= 0
numProjects= 2437818
for project_id in range(numProjects):
	data_dict[str(project_id)] = {}
with open('RawData/project_block_stacks.json', encoding = "ISO-8859-1") as f:
	#'RawData/project_block_stacks.json'
	#'project_block_stacks_mini.json'
	for line in f:
		totalSpriteCount+= 1
		try:

			data = json.loads(line,strict=False)
		except:
			datastring = str(line)
			for i in range(len(datastring)):
				if ord(datastring[i]) > 127:
					datastring = datastring[0:i] + '_' + datastring[i+1:]
			data = json.loads(datastring,strict=False)
		try:
			proj_id=str(data["project_id"])
			proj_data = {"greenflags":0, "definitions":0, "clones":0,"event":0, "op_on_var":0}
				#####Add entry for proj_id id needed###############
			if "greenflags" not in data_dict[str(proj_id)].keys():
				data_dict[str(proj_id)].update({"greenflags":0, "definitions":0, "clones":0,"event":0, "op_on_var":0})
			stackSqueak = data['stack_squeak'].split()
			if len(stackSqueak) is 0:
				emptySpriteCount+= 1
			startConditionFound = False

			for i in range(len(stackSqueak)):





				if '(EventHatMorph' in stackSqueak[i]:
				#####When Program Starts###########################
					startConditionFound = True
					if "Scratch-StartClicked" in stackSqueak[i+1]:
						data_dict[str(proj_id)]["greenflags"] += 1
						#print str(proj_id) + ":greenflags:" + str(data_dict[proj_id]["greenflags"])
				#####When Broadcast Recieved#######################
					else:
						key = "broadcast"
						j = i #Generate the key
						while '")' not in stackSqueak[j]:
							j+=1
							key += stackSqueak[j].strip('":(\')')
						try: #update based on the key
							data_dict[str(proj_id)][key] += 1
						except:
							data_dict[str(proj_id)].update({key:1})
						#print str(proj_id) + ":" + key + ":" + str(data_dict[proj_id][key])
				#####When Mouse Clicked############################
				elif '(MouseClickEventHatMorph' in stackSqueak[i]:
					startConditionFound = True
					key = "mouseclicked" + str(data["sprite_id"])
					try:
						data_dict[str(proj_id)][key] += 1
					except:
						data_dict[str(proj_id)].update({key:1})
					#print str(proj_id) + ":" + key + ":" + str(data_dict[proj_id][key])
				#####When Key Pressed##############################
				elif '(KeyEventHatMorph' in stackSqueak[i]:
					startConditionFound = True
					key = "keypressed" + str(stackSqueak[i+1].strip()[1:-2])
					try:
						data_dict[str(proj_id)][key] += 1
					except:
						data_dict[str(proj_id)].update({key:1})
					#print str(proj_id) + ":" + key + ":" + str(data_dict[proj_id][key])
				#####When Case Is true#############################
				elif '(WhenHatBlockMorph' in stackSqueak[i]:
					startConditionFound = True
					key = "condition"
					j = i + 1
					nesting = 1
					while nesting > 0:
						for char in stackSqueak[j]:
							#print char
							if char in "(":
								nesting += 1
							elif char in ")":
								nesting -= 1
							if nesting is 0:
								break
						key += str(stackSqueak[j]).strip('(:\'")')
						j += 1
					try:
						data_dict[str(proj_id)][key] += 1
					except:
						data_dict[str(proj_id)].update({key:1})
					#print str(proj_id) + ":" + key + ":" + str(data_dict[proj_id][key])
				#	print stackSqueak[i]
				#####When Comment Detected#########################
				elif '(scratchComment' in stackSqueak[i]  or '(comment' in stackSqueak[i]:
					startConditionFound = True
			#####Detect Clone Useage###############################
				if "(createClone)" in stackSqueak[i] or "(deleteClone)"in stackSqueak[i]:
					data_dict[str(proj_id)]['clones'] += 1
					print("CLONE FOUND")
					#print str(proj_id)
			#####Detect Variable Useage############################
				if "(readVariable" in stackSqueak[i] or "(changeVariable" in stackSqueak[i]:
					data_dict[str(proj_id)]["op_on_var"] += 1
					#print str(proj_id) + ":" +str(data_dict[proj_id]["op_on_var"])
			#####Get Total Event Count#############################
				data_dict[str(proj_id)]["event"] = len(data_dict[str(proj_id)].keys())-4
			#####Debug Text########################################
			if startConditionFound:
				pass
				knownCondition += 1
				startcondtionFound = False
				#print "Success: " + str(proj_id) + ":" + str(data["sprite_id"])
			#elif len(stackSqueak) is not 0 and "definition" in stackSqueak:
			#	print "####DEFINITION_FOUND####"+str(proj_id) + ":" + #str(data["sprite_id"])
			elif len(stackSqueak) is not 0:
				#print(str(proj_id) + ":" + str(data["sprite_id"])+":"+str(stackSqueak))
				"######ERROR_NO_HAT######"+str(proj_id) + ":" + str(data["sprite_id"])
		except:
			print("FAILURE:"+line)
			#print "Uh-Oh"#line


			#####Write To CSV FILE#################################
try:
	rawWriter = open("RawData/stack.csv","w")
	writer    = csv.DictWriter(rawWriter, fieldnames=["project_id","data"])
except:
	print("File Failed To Open For Writing")
writer.writeheader()
for key in data_dict.keys():
	if len(data_dict[key].keys()) > 1:
		writer.writerow({"project_id":key,"data":data_dict[key]})
rawWriter.close()
			#####Debug Text########################################
print( "Total Sprites:    " + str(totalSpriteCount))
print( "Known Condition:  " + str(knownCondition))
print( "Definiton Blocks: 0 (Not implemented until Scratch 2.0)")
print( "Empty Sprites:    " + str(emptySpriteCount))
print( "No Hat Blocks:    " + str(totalSpriteCount - (knownCondition+emptySpriteCount)))
