import sys
import os


def main(args):
	blackList = [chr(8204),chr(8207), chr(8235), chr(8205)]
	uncode = "ansi"
	if len(args) > 2 :
		filePath = args[1]
		arg2 = args[2].lower()
		if arg2 == "u":
			uncode = "utf-8"
	elif len(args) == 2 :
		filePath = args[1]
	else:
		filePath = input('Enter file path : ')

	if filePath.lower() == "exit":
		exit()
	if filePath.lower() == "all":
    	# Handle "all" command
		fileList = os.listdir()
		for file in fileList:
			fileName = file.lower()
			if fileName.endswith(".srt") and not ("vlc compatible" in fileName) :
					createSub(file,blackList,uncode)
	else:
		createSub(filePath,blackList,uncode)

def createSub(filePath,blackList,uncode):
	print("With encoding {}".format(uncode))
	filePointer = open(filePath, encoding=uncode)
	exIndex = str(filePath).rindex('.') - 1
	newFilePath = filePath[0:exIndex] + " - vlc compatible.srt"
	newFilePointer = open(newFilePath, "w", encoding='utf-8')
	l = 0
	while True:
		line = filePointer.readline()
		if line == "":
			break
		l += 1
		for c in blackList:
			if c in line:
				line = line.replace(c, " ")
		newFilePointer.write(line)
	print(str(l) + " lines checked out\n")
	filePointer.close()
	newFilePointer.close()


main(sys.argv)
