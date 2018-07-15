import sys
import os
import shutil


def main(args):
	if len(args) >= 1:
		drive = args[1] + "\\";
		path = drive + " " # plus ascii 255
		fileLists = getFilesList(path)
		print("")
		for item in fileLists:
			tempItem = path + "\\" + item
			moveFile(tempItem, drive)
		if len(getFilesList(path)) == 0 :
			shutil.rmtree(path)
			print("\n[-] Ended successfuly")
			print("	   [+] Null directory removed")
		else:
			print("\n[-] Uncomplete operation")
		print("\n---------- End of operations -------")


def moveFile(item,location):
	shutil.move(item,location)
	print(item + " ->  Moved")

def getFilesList(sourceFolder):
	return os.listdir(sourceFolder)
	


main(sys.argv)
