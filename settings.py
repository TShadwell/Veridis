store ={}
def readsettings(Notify):
	try:
		tasks = open("data/tasks")
		t=tasks.read().rstrip("}").split("\n")
		tasks.close()
		Aliases={}
		def addAlias(fromToList):
			Aliases[fromToList[0]] = fromToList[1]
		t = [dict([[(Aliases[a] if a in Aliases else a) for a in list(value.split(":"))] for value in task.split(";")]) for task in "".join([val for val in [(addAlias(line.split(" ")[1:3]) if not line.find("Alias") else line) for line in t] if not val == None]).split("}")]
		return t
	except IOError as e:
		Notify.Queue.append("Could not load tasks!")