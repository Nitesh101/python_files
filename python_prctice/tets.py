from string import maketrans
val = "my name is nitesh"
val3 = 'aeiou'
val4 = '14678'
lis = maketrans(val3,val4)
print val.translate(lis)
