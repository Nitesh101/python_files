"""
def smalest_lis(lis):
	min=lis[0]	
	for i in lis:
		if i < min:
			min = i
	return min
print smalest_lis([3,2,1,4,56,-1])
"""
def match_words(words):
	ctr = 0
	for i in words:
		if len(i) > 1 and i[0]==i[-1]:
			ctr+=1
	return ctr
print(match_words(['aba','niteshn','aygfyuaf']))
