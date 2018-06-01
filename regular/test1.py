import re
fa = open('test.txt','r')
fb=fa.readline()
y = re.findall('\S+@\S+',fb)
print y


