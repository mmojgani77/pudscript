import os
import sys

def main(args):
	if (len(args) >= 2) :
		googleIt(args[1:])

def googleIt(query):
	url = "http://www.google.com/search?q=" + "%20".join(query)
	os.system("start  "+ url)

main(sys.argv)