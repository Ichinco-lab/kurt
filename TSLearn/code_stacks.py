










def getParallelism(line):
	greenflags = 0
	onclick = 0
	userdefined = 0
	for key in line.keys():
		if line[key > 1]
			if "greenflags" in key:
				greenflags = 1
			elif "mouseclicked" in key or "keypressed" in key:
				onclick = 1
			elif "broadcast" in key or "condition" in key:
				userdefined = 1
	return greenflags + onclick + userdefined
	
	


def getAbstraction(line):
	events = 0
	clones = 0
	definitions = 0
	if line["events"] > 1:
		events = 1
	if line["clones"] >= 1:
		clones = 1
	if line["definitions"] >= 1:
		definitions = 1	
	return events + clones + definitions 
		
	
	
	
	
	
	
	
	#line['events']
