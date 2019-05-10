import json

data_dict={}

with open('project_block_stacks_mini.json') as f:
	for line in f:
		try:
			data = json.loads(line)
			proj_id=data["project_id"]
			proj_data = {"greenflags":0, "definitions":0, "clones":0,"event":0, "op_on_var":0}

			if proj_id not in data_dict.keys():
				data_dict[proj_id] = proj_data
			if 'Scratch-StartClicked' in data['stack_squeak']:
				data_dict[proj_id]["greenflags"]+=1
			elif 'Scratch-MouseClickEvent' in data['stack_squeak']:
				for word in data['stack_squeak'].split(): 
					if 'Scratch-MouseClickEvent' in word:			
						if "mouseclicked"+str(data["sprite_id"]) in data_dict[proj_id].keys():
							data_dict[proj_id]["mouseclicked"+str(data["sprite_id"])]+=1
						else:
							data_dict[proj_id]["mouseclicked"+str(data["sprite_id"])]=1





			elif 'KeyEventHatMorph' in data['stack_squeak']:
				#data_dict[proj_id]["keypressed"]+=1
				k= data['stack_squeak'].split('"')[1]
				if "keypressed"+data['stack_squeak'].split('"')[1].strip().strip() in data_dict[proj_id].keys():
					data_dict[proj_id]["keypressed"+data['stack_squeak'].split('"')[1].strip()]+=1
				else:
					data_dict[proj_id]["keypressed"+data['stack_squeak'].split('"')[1].strip()]=1

			elif 'MouseEventHatMorph' in data['stack_squeak']:
				k= data['stack_squeak'].split('"')[1]
				if "mouseevent"+data['stack_squeak'].split('"')[1].strip().strip() in data_dict[proj_id].keys():
					data_dict[proj_id]["mouseevent"+data['stack_squeak'].split('"')[1].strip()]+=1
				else:
					data_dict[proj_id]["mouseevent"+data['stack_squeak'].split('"')[1].strip()]=1
			
			elif 'EventHatMorph' in data['stack_squeak']:
				for word in data['stack_squeak']:
					if 'EventHatMorph' in word and 'KeyEventHatMorph' not in word and 'MouseEventHatMorph' not in word:
						data_dict[proj_id]["event"]+=1
			
			elif 'Hat' in data['stack_squeak']:
				pass
			
			if 'setVar' in data['stack_squeak']:
				for setVarEvent in data['stack_squeak'].split('setVar')[1:]:
					setVarToWhat = setVarEvent.split(")")
				if '+' in setVarToWhat or '-' in setVarToWhat or '*' in setVarToWhat or '/' in setVarToWhat:
						data_dict[proj_id]["op_on_var"] +=1
			
			for key in data_dict.keys():
				for key2 in data_dict[key].keys():
					if 'mouseclicked' in key2:
						#print data_dict
						print str(key) + ":" + str(key2)
		except:
			print "Uh-Oh"
			pass
			#print line
