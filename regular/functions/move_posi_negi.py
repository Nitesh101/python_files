def positive_negitive(mylist):
	op = []
	index = 0
	for val in mylist:
		if val > 0 :
			op.insert(index,val)
			index +=1
		else:
			op.append(val)
	return op
print positive_negitive([1,2,-3,4,-6])
