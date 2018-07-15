import os
import sys
import time

def main(args):
	mainFlag = (len(args) == 2) and (args[1].lower() == "main")
	fileptr = open("sitedb.txt","r")
	for line in fileptr:
		if (line == None) or (line.strip() == ""):
			continue
		url = line.replace("\n","")
		if not url.startswith('\''):
			startWebSite(url, mainFlag)
			time.sleep(0.1)
	fileptr.close()

def clrScr():
	os.system("cls")

def startWebSite(url,mainFlag):
	isMainUrl = url.startswith("*")
	cleanUrl = url
	hasToRun = False
	if isMainUrl :
		cleanUrl = cleanUrl[1:len(cleanUrl)]

	if mainFlag :
		if isMainUrl:
			hasToRun = True
	else:
		hasToRun = True

	if hasToRun:
		os.system("start " + cleanUrl)



main(sys.argv)