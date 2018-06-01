def count_len(input1):
	global count
	count = 0
	dict = {}
	for i in input1:
		keys = dict.keys()
		if i in keys:
			dict[i] +=1
			count += 1
		else:
			dict[i] = 1
			count +=1
	return dict
print count_len('ggole.com')
print count
