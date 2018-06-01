f1 = open('file1.txt', 'r')
val1 = f1.readlines()
f2 = open('file2.txt', 'r')
val2 = f2.readlines()
for line1 in val1:
        if line1 not in val2:
            print line1
f1.close()
f2.close()
