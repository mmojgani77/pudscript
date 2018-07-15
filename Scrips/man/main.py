import os
import sys

def main(args):
	appsPath = args[0] + "/../../"
	appName = args[1]
	manualFilePath = appsPath + appName + "/manual.txt"
	print("")
	if os.path.exists(manualFilePath):
		print("  --- Manual.txt of " + appName.capitalize() + " ---\n\n")
		fileptr = open(manualFilePath,"r")
		for line in fileptr:
			print("  " + line,end="",flush=True)
		fileptr.close()
	else:
		print("  -------------------------------------------")
		print("   There is no manual file for this script.")
		print("  -------------------------------------------")
	print("\n")


def clrScr():
	os.system("cls")

main(sys.argv)