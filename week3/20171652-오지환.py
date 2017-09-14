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
		scdb =  pickle.load(fH)
	except:
		print("Empty DB: ", dbfilename)
	else:
		print("Open DB: ", dbfilename)
	fH.close()
	for p in scdb:
		p['Age'] = int(p['Age'])
		p['Score'] = int(p['Score'])
	return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()

def doScoreDB(scdb):
	while(True):
		inputstr = (input("Score DB > "))
		if inputstr == "": continue
		parse = inputstr.split(" ")
		if parse[0] == 'add':
			try:
				record = {'Name':parse[1], 'Age':int(parse[2]), 'Score':int(parse[3])}
				scdb += [record]
			except:
				print("input: add Name Age Score")
		elif parse[0] == 'del':
			check_del = False
			try:
				for p in scdb:
					if p['Name'] == parse[1]:
						scdb.remove(p)
						check_del = True
				if not(check_del):
					print("No matching name exists")
			except:
				print("input: del Name")
		elif parse[0] == 'show':
			try:
				sortKey ='Name' if len(parse) == 1 else parse[1]
				showScoreDB(scdb, sortKey)
			except:
				print("input: show (Name or Age or Score)")
		elif parse[0] == 'find':
			check_find = False
			try:
				for p in scdb:
					if p['Name'] == parse[1]:
						for attr in sorted(p):
							print(attr + "=" +str(p[attr]), end=' ')
						print()
						check_find = True
				if not(check_find):
					print("No matching name exists")
			except:
				print("input: find Name")
		elif parse[0] == 'inc':
			try:
				for p in scdb:
					if p['Name'] == parse[1]:
						p['Score'] += int(parse[2])
			except:
				print("input inc Name amount")
		elif parse[0] == 'quit':
			break
		else:
			print("Invalid command: " + parse[0])
			

def showScoreDB(scdb, keyname):
	for p in sorted(scdb, key=lambda person: person[keyname]):
		for attr in sorted(p):
			print(attr + "=" + str(p[attr]), end=' ')
		print()
	


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)

