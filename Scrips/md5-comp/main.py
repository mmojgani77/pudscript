import hashlib
import sys
import os


def main(args):
	if len(args) == 3:
		text = args[1]
		md5 = args[2]
	else:
		text = input("Enter your text > ")
		md5 = input("Enter your MD5 > ")
	
	text = text.encode("utf-8")
	hasher = hashlib.md5()
	hasher.update(text)
	textMd5 = hasher.hexdigest();
	
	print("\n  --------------------------------")
	if textMd5 == md5:
		print("  Text and MD5 are equal.")
	else:
		print("  Text and MD5 are not equal.")
	print("  --------------------------------")

main(sys.argv)