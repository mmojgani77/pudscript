import os
import sys

def main(args):
	appsPath = args[0] + "/../../"
	apps = os.listdir(appsPath)
	print("")
	print("App Scripting Manuals")
	print("---------------------\n")
	print("Commands syntax : app [Script folder name] [Parameters seperated by spaces]\n")
	print("----- List of scripts -----")
	print("---------------------------\n")

	for app in apps:
		if os.path.isdir(appsPath + app):
			print("[*]  " + app)
	print("")


def clrScr():
	os.system("cls")

main(sys.argv)