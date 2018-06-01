words = 'The quick brown fox jumps over the lazy dog'.split()
stuff = [[w.upper(),w.lower(),len(w)] for w in words]
for i in stuff:	
	print i
stuff =map(lambda w: [w.upper(),w.lower(),len(w)],words)
for i in stuff:
	print i

