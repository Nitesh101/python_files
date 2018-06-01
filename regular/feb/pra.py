input1 = ['deltas','desalt','lorry','lasted','retainers','salted','aerospac','slated','staled','resmelts']
anagram = {}
for word in input1:
	swords = ''.join(sorted(word))
	anagram.setdefault(swords,[]).append(word)
anagram_list = [k for k in anagram.values() if len(k) > 1]
print anagram_list	
