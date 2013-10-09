import sys
#this is printing lines
def readfiles(*filenames):
	for f in filenames:
		for line in open(f):
			 print line
			 #this prints
readfiles(sys.argv[0],'7-1.py')

