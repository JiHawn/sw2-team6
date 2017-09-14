import pickle

dbfilename = 'test3_4.dat'

def readScoreDB():
	try:
		fH = open(dbfilename, 'rb')
	except FileNotFoundError as e:
		print("New DB: ", dbfilename)
		return []

	scdb = []
	try:
		scdb = pickle.load(fH)
	except:
		print("Empty DB: ", dbfilename)
	else:
		print("Open DB: ", dbfilename)
	fH.close()
	return scdb

# write the data into person db
def writeScoreDB(scdb):
	fH = open(dbfilename, 'wb')
	pickle.dump(scdb, fH)
	fH.close()
def doScoreDB(scdb):
	while (True):
		inputstr = (input("Score DB > "))
		if inputstr == "": continue
		parse = inputstr.split(" ")
		if parse[0].lower() == 'add':
			record = {'Name': parse[1], 'Age': parse[2], 'Score': parse[3]}
			scdb += [record]
		elif parse[0].lower() == 'del':
			for p in scdb:
				if p['Name'].lower() == parse[1].lower():
					scdb.remove(p)
		elif parse[0].lower() == 'show':
			sortKey = 'Name' if len(parse)== 1 else parse[1].lower()
			showScoreDB(scdb, sortKey)
		elif parse[0].lower() == 'quit':
			break
		elif parse[0].lower() == 'find':
			for p in scdb:
				if p['Name'].lower() == parse[1].lower():
					print(p)
		elif parse[0].lower() == 'inc':
			for p in scdb:
				if p['Name'].lower() == parse[1].lower():
					p['Score'] = int(p['Score']) 
					p['Score'] += int(parse[2])
					p['Score'] = str(p['Score'])

		else:
			print("Invalid command: " + parse[0])
def showScoreDB(scdb, keyname):
	for p in sorted(scdb, key=lambda person: person[keyname]):
		for attr in sorted(p):
			print(attr + "=" + p[attr],end=' ')
		print()

scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)


