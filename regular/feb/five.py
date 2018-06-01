f1 = open('one.txt','r')
f2 = open('two.txt','r')
fo = open('output.txt','w')
fa = f1.readlines()
fb = f2.readlines()
for i in fa:
	if i not in fb:
		fo.write(i)
f1.close()
f2.close()
fo.close()
