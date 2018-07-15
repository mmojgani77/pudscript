import hashlib
import sys
import os


def main(args):
	if len(args) == 2:
		text = args[1]
	else:
		text = input("Enter your text to generate MD5 > ")
	
	text = text.encode("utf-8")
	hasher = hashlib.md5()
	hasher.update(text)
	# Print MD5 code
	print("\n  --------------------------------")
	print("  " + hasher.hexdigest())
	print("  --------------------------------")

main(sys.argv)