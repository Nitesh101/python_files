input1 = ['deltas','desalt','lorry','lasted','retainers','salted','aerospac','slated','staled','resmelts']
new = {}
for key in input1:
	swords = ''.join(sorted(key))
	group = new.setdefault(swords,[]).append(key)
print new
new_list = [k for k in new.values() if len(k) > 1]
print new_list
