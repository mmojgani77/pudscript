import os
import sys
import time

def main(args):
	fileptr = open("sitedb.txt","r")
	for line in fileptr:
		if (line == None) or (line.strip() == ""):
			continue
		url = line.replace("\n","")
		if not url.startswith('\''):
			startWebSite(url)
			time.sleep(0.1)
	fileptr.close()

def clrScr():
	os.system("cls")

def startWebSite(url):
	os.system("start " + url)

main(sys.argv)