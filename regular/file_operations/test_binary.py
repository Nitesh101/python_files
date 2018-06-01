import pickle
output_file = open('myfile.bin','wb')
myint = 333
mystring = 'hello wrodl'
mylist = ['dog','cat','lizard']
mydict = {'name': 'bob','job':'astronaut'}
pickle.dump(myint,output_file)
pickle.dump(mystring,output_file)
pickle.dump(mylist,output_file)
pickle.dump(mydict,output_file)
output_file.close()
