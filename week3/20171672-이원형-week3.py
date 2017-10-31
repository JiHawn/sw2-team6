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
	for p in scdb :
		p['Age']=int(p['Age'])
		p['Score']=int(p['Score'])

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
			try :
				record = {'Name': parse[1], 'Age': parse[2], 'Score': parse[3]}
				scdb += [record]
			except :
				print("input : add name age score")
		elif parse[0].lower() == 'del':
			check_del = False
			for p in scdb:
				print(p)
				if p['Name'].lower() == parse[1].lower():
					print("DEL: " + repr(p))
					scdb.remove(p)
					check_del = True
			if not(check_del):
				print("No matching name")
		elif parse[0].lower() == 'show':
			sortKey = 'Name' if len(parse)== 1 else parse[1].lower()
			showScoreDB(scdb, sortKey)
		elif parse[0].lower() == 'quit':
			break
		elif parse[0].lower() == 'find':
			check_find = False
			for p in scdb:
				if p['Name'].lower() == parse[1].lower():
					print(p)
					check_find = True
			if not(check_find):
				print("No matching name")
		elif parse[0].lower() == 'inc':
			check_inc = False
			for p in scdb:
				if p['Name'].lower() == parse[1].lower():
					p['Score'] += int(parse[2])
					check_inc = True
			if not(check_inc):
				print("No matching name")
		else:
			print("Invalid command: " + parse[0])
def showScoreDB(scdb, keyname):
	for p in sorted(scdb, key=lambda person: person[keyname]):
		for attr in sorted(p):
			print(attr + "=" + str(p[attr]),end=' ')
		print()

scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)


