import os

def countpy(filepy):
	print filepy
	return [py for py in filepy if '.py' in py]

pyfile=countpy(os.listdir('ch6'))
print pyfile,':',len(pyfile)

