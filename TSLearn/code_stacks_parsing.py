import json

data_dict={}

with open('../project_block_stacks.json') as f:
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
                print data_dict
                if "mouseclicked"+data["sprite_id"] in data_dict[proj_id].keys():
                    data_dict[proj_id]["mouseclicked"+data["sprite_id"]]+=1
                else:
                    data_dict[proj_id]["mouseclicked"+data["sprite_id"]]=1
                    print data_dict
            elif 'KeyEventHatMorph' in data['stack_squeak']:
                #data_dict[proj_id]["keypressed"]+=1
                k= data['stack_squeak'].split('"')[1]
                if "keypressed"+strip(data['stack_squeak'].split('"')[1]) in data_dict[proj_id].keys():
                    data_dict[proj_id]["keypressed"+strip(data['stack_squeak'].split('"')[1])]+=1
                else:
                    data_dict[proj_id]["keypressed"+strip(data['stack_squeak'].split('"')[1])]=1

            elif 'EventHatMorph' in data['stack_squeak']:
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
                        print data_dict
        except:
            pass
            #print line
