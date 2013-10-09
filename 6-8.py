import itertools

def peep(it):
	b=list(it)
	a=b[0]
	return a,b

it1=iter([1,2,3])
x,it1=peep(it1)
print x,it1
