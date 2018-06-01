str1 = """"The fat cat sat on the mat and it on the way to reach gate,now the fat cat jummped over the gate"""
lst = str1.split()
lst2 = []
count = 0
for i in lst:
	if i.endswith('at'):
		lst2.append(i)
		count += 1
	else:	
		pass
print lst2
print "count of all words",count
