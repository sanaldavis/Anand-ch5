class reverse_iter:
	def __init__(self,n):
		self.i=0
		self.c=len(n)
		self.n=n[::-1]
		print self.n
	def next(self):
		if self.i<self.c:
			print self.n[self.i]
			self.i+=1
		else:
   			raise StopIteration()

a=reverse_iter([1,2,3])
a.next()
a.next()
a.next()
a.next() 
