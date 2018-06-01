fo = open('foo.txt','rw+')
print "name of the file: ",fo.name
line = fo.readline()
print "Read Line %s:",line
fo.seek(0,2)
line = fo.readline()
print "read Line %s",line
fo.close()
