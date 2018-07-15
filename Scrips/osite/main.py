import os
import sys
import time

def main(args):
	if len(args) >= 2:
		sites = args[1:len(args)]
		for site in sites:
			startWebSite(site)
			time.sleep(0.1)

def clrScr():
	os.system("cls")

def startWebSite(url):
	if not url.startswith("http://") :
		url = "http://" + url
	os.system("start " + url)

main(sys.argv)