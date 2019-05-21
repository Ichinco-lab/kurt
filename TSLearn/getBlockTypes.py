import json
import csv

data = {}
#for every unique command in the scratch Program
#add a key to our dictionary with that command as the key
with open('clones.json') as f:
	for line in f:
		try:
			sprite = json.loads(line)
			for word in sprite['stack_squeak'].split():
				if word.strip("()") not in data.keys() and word[0] in '(' and len(word) > 3:
					data.update({word.strip("()"):1})
		except:
			print "Uh-Oh"



#write every command used to a file
with open("getDef.txt","wb") as writer:
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
