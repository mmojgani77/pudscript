import os
import sys

def main(args):
	if (len(args) >= 2) :
		action = args[1].lower()
		appsPath = args[0] + "/../"
		bookmarkdbPath = appsPath + "bookmarkdb.dll";
		database = loadDb(bookmarkdbPath)
		if (action == "set"):
			setBookmark(database, args)
		elif (action == "unset"):
			unsetBookmark(database, args)
		elif (action == "open"):
			openBookmark(database, args)
		elif (action == "show"):
			showBookmark(database, args)
		else:
			print("Invalid action")
		saveDb(database, bookmarkdbPath)
	else:
		print("Invalid command syntax - arguments should be 2\n\
Please execute command \"app man bookmark\"")

def saveDb(databaseMap, databasePath):
	f = open(databasePath,'w+')
	for key in databaseMap:
		f.write(key + "=" + databaseMap[key] + "\n")
	f.close();

def loadDb(databasePath):
	map = {}
	if not os.path.exists(databasePath):
		f = open(databasePath, "w+")
	else:
		f = open(databasePath,'r+')
		data = f.read().replace('\r','')
		if (data.strip() != ""):
			data = data.split('\n')
			for i in range(len(data)):
				if data[i].strip() != "":
					row = data[i].split('=')
					map[row[0]] = row[1]
	f.close()
	return map

def setBookmark(databaseMap, args):
	if (len(args) == 4):
		databaseMap[args[2].lower()] = args[3]
		print("Bookmark setted up")
	else:
		print("Invalid set command syntax")

def unsetBookmark(databaseMap, args):
	if (len(args) == 3):
		if args[2].lower() in databaseMap.keys():
			del(databaseMap[args[2].lower()])
			print("Bookmark unsetted up")
		else:
			print("There is no such bookmark")
	else:
		print("Invalid unsetset command syntax")

def showBookmark(databaseMap, args):
	if (len(args) == 3):
		if args[2].lower() == "--all":
			for key in databaseMap.keys():
				printBookmark(key, databaseMap[key])
		elif args[2].lower() in databaseMap.keys():
			printBookmark(args[2], databaseMap[args[2]])
		else:
			print("There is no such bookmark")
	else:
		print("Invalid show command syntax")

def printBookmark(key, value):
	print("\"" + key.lower() + "\" refers to \"" + value + "\"")

def openBookmark(databaseMap, args):
	if (len(args) == 3):
		if (args[2].lower() != "--all"):
			url = databaseMap[args[2]]
			openInBrowser(url)
		else:
			for key in databaseMap.keys():
				openInBrowser(databaseMap[key])
	else:
		print("Invalid open command syntax")

def openInBrowser(url):
	if not url.startswith("http"):
		url = "http://" + url
	os.system("start " + url)

main(sys.argv)