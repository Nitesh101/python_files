s = ['delras','desalt','lorry','lasted','retainers','salted','aerospace','slaled','resmelts']
from collections import Counter
from itertools import combinations
op = []
for val in combinations(s, 2):
	if Counter(val[0])==Counter(val[1]):
		op.extend(val)

print(op)
