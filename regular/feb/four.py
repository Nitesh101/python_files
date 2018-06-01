input1 = ['deltas','desalt','lorry','lasted','retainers','salted','aerospace','slated','staled','resmelts']
anagram = {}
for i in input1:
	words = ''.join(sorted(i))
	anagram.setdefault(words,[]).append(i)
anangram_list = [k for k in anagram.values() if len(k) >1 ]
print anangram_list
	
