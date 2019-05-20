import json
import csv
data_dict={}
totalSpriteCount= 0
emptySpriteCount= 0 
knownCondition= 0
with open('clones.json') as f:
	
	for line in f:
		totalSpriteCount+= 1
		try:
			data = json.loads(line)
			proj_id=data["project_id"]
			proj_data = {"greenflags":0, "definitions":0, "clones":0,"event":0, "op_on_var":0}
				#####Add entry for proj_id id needed###############
			if proj_id not in data_dict.keys():
				data_dict[proj_id] = proj_data
			stackSqueak = data['stack_squeak'].split()
			if len(stackSqueak) is 0:
				emptySpriteCount+= 1
			startConditionFound = False
			for i in range(len(stackSqueak)):
				
					
					
					
					
				if '(EventHatMorph' in stackSqueak[i]:
				#####When Program Starts###########################
					startConditionFound = True
					if "Scratch-StartClicked" in stackSqueak[i+1]:
						data_dict[proj_id]["greenflags"] += 1
						#print str(proj_id) + ":greenflags:" + str(data_dict[proj_id]["greenflags"])			
				#####When Broadcast Recieved#######################	
					else:
						key = "broadcast"
						j = i #Generate the key
						while '")' not in stackSqueak[j]:
							j+=1
							key += stackSqueak[j].strip('":(\')')
						try: #update based on the key
							data_dict[proj_id][key] += 1
						except:
							data_dict[proj_id].update({key:1})
						#print str(proj_id) + ":" + key + ":" + str(data_dict[proj_id][key])	
				#####When Mouse Clicked############################
				elif '(MouseClickEventHatMorph' in stackSqueak[i]:
					startConditionFound = True
					key = "mouseclicked" + str(data["sprite_id"])
					try:
						data_dict[proj_id][key] += 1
					except:
						data_dict[proj_id].update({key:1})
					#print str(proj_id) + ":" + key + ":" + str(data_dict[proj_id][key])	
				#####When Key Pressed##############################
				elif '(KeyEventHatMorph' in stackSqueak[i]:
					startConditionFound = True
					key = "keypressed" + str(stackSqueak[i+1].strip()[1:-2])
					try:
						data_dict[proj_id][key] += 1
					except:
						data_dict[proj_id].update({key:1})
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
						data_dict[proj_id][key] += 1
					except:
						data_dict[proj_id].update({key:1})
					#print str(proj_id) + ":" + key + ":" + str(data_dict[proj_id][key])
				#	print stackSqueak[i]
				if "(createClone)" in stackSqueak[i] or "(deleteClone)"in stackSqueak[i]:
					data_dict[proj_id]['clones'] += 1
					print str(proj_id)
					
				
					
					
				data_dict[proj_id]["events"] = len(data_dict[proj_id].keys())-4
			#####Debug Text########################################	
			if startConditionFound:
				knownCondition += 1
				startcondtionFound = False
			elif len(stackSqueak) is not 0 and "definition" in stackSqueak:
				print "####DEFINITION_FOUND####"+str(proj_id) + ":" + str(data["sprite_id"])
			elif len(stackSqueak) is not 0:
				print "######ERROR_NO_HAT######"+str(proj_id) + ":" + str(data["sprite_id"])
						
		except:
			print "uh-oh"


			#####Write To CSV FILE#################################	
try:
	rawWriter = open("stack.csv","wb")
	writer    = csv.DictWriter(rawWriter, fieldnames=["project_id","data"])
except:
	print "File Failed To Open For Writing"
writer.writeheader()
for key in data_dict.keys():
	writer.writerow({"project_id":key,"data":data_dict[key]})
rawWriter.close()
			#####Debug Text########################################
print "Total Sprites:   " + str(totalSpriteCount)	
print "Known Condition: " + str(knownCondition)		
print "Empty Sprites:   " + str(emptySpriteCount)
print "No Hat Blocks:   " + str(totalSpriteCount - (knownCondition+emptySpriteCount))
