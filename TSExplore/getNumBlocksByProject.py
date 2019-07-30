import json
import csv

#Fails to deal with edge case where "(" ")" within string tokens
#Ignores conditional blocks entirely due to conditional statements use <>
#brackets instead of () parenthesis
def getBlockCountV1(inFile,outFile):
    formatted_data = {}
    with open(inFile, encoding = "ISO-8859-1") as f:
        #'RawData/project_block_stacks.json'
        #'project_block_stacks_mini.json'
        for line in f:
            try:

                data = json.loads(line,strict=False)
            except:
                datastring = str(line)
                for i in range(len(datastring)):
                    if ord(datastring[i]) > 127:
                        datastring = datastring[0:i] + '_' + datastring[i+1:]
                data = json.loads(datastring,strict=False)
            bracketStack = 0
            calls = 0
            #quote   = True
            for word in data['stack_squeak'].strip("\"").split():
                for char in word:
                    if char in "(":
                        bracketStack += 1
                        if len(word) == 1 or word[-1] in ")":
                            calls -= 1
                    if char in ")" and bracketStack > 0:
                        bracketStack -= 1
                        calls += 1
            try:
                formatted_data[str(data['project_id'])] += calls
            except:
                formatted_data.update({str(data['project_id']):calls})

        #for key in formatted_data.keys():
            #print(str(key) + ": " + str(formatted_data[key]))

    with open(outFile, 'w') as f :
        f.write("project_id,block_count\n")
        for key in formatted_data.keys():
            f.write(str(key) + "," + str(formatted_data[key])+"\n")


#Edge case seems to be that only the outer block of nested conditionals are
#counted
def getBlockCountV2(inFile,outFile):
    formatted_data = {}
    #Initialize each line of json file into dictionary form
    with open(inFile, encoding = "ISO-8859-1") as f:
        #'RawData/project_block_stacks.json'
        #'project_block_stacks_mini.json'
        for line in f:
            try:

                data = json.loads(line,strict=False)
            except:
                datastring = str(line)
                for i in range(len(datastring)):
                    if ord(datastring[i]) > 127:
                        datastring = datastring[0:i] + '_' + datastring[i+1:]
                data = json.loads(datastring,strict=False)
            bracketStack = 0
            calls = 0
        #Every time there is a new line character there is a block
        for char in data['stack_squeak']:
            if char in "\n":
                calls += 1
        try:
            formatted_data[str(data['project_id'])] += calls
        except:
            formatted_data.update({str(data['project_id']):calls})

getBlockCountV2("RawData/project_block_stacks.json","RawData/project_blocks/blockCounts.csv")#'RawData/project_block_stacks.json')
