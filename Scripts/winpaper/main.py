import sys
import os
from shutil import copyfile


def main(args):
	if len(args) >= 2:
		sourceFolder = os.environ["USERPROFILE"] + "\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets"
		destinationFolder = args[1]
		files = getFilesList(sourceFolder);
		itemIndex = 1
		if os.path.isdir(destinationFolder) :
			for item in files:
				copyImage(sourceFolder + "\\" + item,destinationFolder,itemIndex)
				itemIndex += 1
			print("Finished")
		else:
			print("[+] Error in destination path")


def copyImage(srcImage,desFolder,fileIndex):
	destPath = desFolder + "\\" + str(fileIndex) + ".jpg"
	copyfile(srcImage,destPath)

def getFilesList(sourceFolder):
	return os.listdir(sourceFolder)
	


main(sys.argv)
