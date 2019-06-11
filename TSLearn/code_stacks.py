







def getCodeStackFields(line):
	fields = {
		"parallelism": getParallelism(line),
		"abstraction": getAbstraction(line)
	}
	return fields


def getParallelism(line):
	greenflags = 0
	onclick = 0
	userdefined = 0
	data = line["data"].split()
	for i in range(len(data)-1):
		try:
			if int(data[i+1].strip(",}")) > 1:
				if "greenflags" in data[i]:
					greenflags = 1
				elif "mouseclicked" in data[i] or "keypressed" in data[i]:
					onclick = 1
				elif "broadcast" in data[i] or "condition" in data[i]:
					userdefined = 1
		except:
			pass
	return greenflags + onclick + userdefined




def getAbstraction(line):
	events = 0
	clones = 0
	definitions = 0
	data = line["data"].split()
	for i in range(len(data)-1):
		try:
			value = int(data[i+1].strip(",}"))
		except:
			value = 0
		if value >= 1:
			if "event" in data[i]:
				events = 1
			if "clones" in data[i]:
				clones = 1
			if "definitions" in data[i]:
				definitions = 1
	return  events + clones + definitions








	#line['events']
