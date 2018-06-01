def my_gen(n):
	yield n	
	yield n+1
g = my_gen(6)
print next(g)
