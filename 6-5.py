import os

def py_totalline(dirt):
	files=os.listdir(dirt)
	pyfile=[f for f in files if '.py' in f]
	print pyfile
	for py in pyfile:
		f=open(dirt+'/'+py,'r')
		print py,len(f.readlines())


py_totalline('ch6')
