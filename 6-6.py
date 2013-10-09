import os
import re 
def pyfile(dirt):
	files=os.listdir(dirt)
	pyfile=[f for f in files if '.py' in f]
	print pyfile
	for py in pyfile:
		count=0
		f=open(dirt+'/'+py,'r')
		code=f.readlines()
		for line in code:
			if line!='\n' and line[0]!='#':
				count+=1
		print py,count
pyfile('ch6')

