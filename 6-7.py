import os
import sys

def split(fname,no,j=0):
	f=open(fname,'r')
	data=f.readlines()
	print data,len(data)	
	i=len(data)/no
	print i
	while i>=0:
		insert(data[j:j+no],i)
		j=j+no
		i=i-1

def insert(line,i):

	pt=open('%d.txt'%i,'a')
	for lines in line:
		pt.write(lines)
	pt.close()	

split(sys.argv[0],int(sys.argv[1]))
