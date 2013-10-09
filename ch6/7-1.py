def sum(a,b):
  if b==0:
    return 0
  else:
    return a+sum(a,b-1)

print sum(5,3)
