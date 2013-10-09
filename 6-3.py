import os

def findfiles(dirt):
	files=os.listdir(dirt)
	print files
	for f in files:
		#print os.path.abspath(dirt+'/'+f)
		if os.path.isdir(os.path.abspath(dirt+'/'+f)) is True:
			findfiles(dirt+'/'+f)	
		else:
  			print os.path.abspath(dirt+'/'+f)

findfiles('ch6')
