import sys

def readfiles(*filenames):
	for f in filenames:
		for line in open(f):
			if len(line)>20:	 
				print line

readfiles(sys.argv[0],'6-1.py')

