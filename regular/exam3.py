from operator import itemgetter
s = [("Ramu","Python",99),("jahnavi","Django",100),("Kavya","Flask",67),("Bhaskar","Pyramid",87)]
print "first method"
x = sorted(s,key=itemgetter(1),reverse=True)
print x
x = sorted(s,key=itemgetter(2))
print x
print "============================="

print "send method"
x = sorted(s,key=lambda x:x[1],reverse=True)
print  x
x = sorted(s,key=lambda x:x[2])
print x
