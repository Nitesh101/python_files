fo = open('test.txt','r')
fo.seek(2)
fo.seek(2,1)
print fo.read()
