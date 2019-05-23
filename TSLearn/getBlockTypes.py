import json
#import simplejson
import csv

data = {}
#for every unique command in the scratch Program
#add a key to our dictionary with that command as the key
def findCommands(inFile, outFile):
	with open(inFile) as f:
		for line in f:
			try:
				sprite = json.loads(line)#.encode('cp037').strip())
			
				for word in sprite['stack_squeak'].split():
					if  word[0] in '(' and len(word) > 3 and '"' not in word and word.strip("(:)") not in data.keys():
						data.update({word.strip("(:)"):1})
						print word
			except:
				pass
			#except:
			#print line

			#return
	#write every command used to a file
	try:
		writer = open(outFile,'w')
		i = 0
		print "Writing Scratched Commands Used To File"
		print "NOTE: for each command here, the '(' character"
		print "has been stripped from the beginning of the word"
		print "and  additional '(' and ')' chars may have been stripped"
		print "from the command as well;"
		for key in data.keys():
			print str(i) + ": " + str(key)
			writer.write(str(key)+"\n")
			i += 1
	except:
		print "uh-oh"
	writer.close()




findCommands("RawData/project_block_stacks.json","getDef.txt")
#"RawData/project_block_stacks.json"
#"RawData/small_stacks.json"
#"RawData/small_stacks.json"