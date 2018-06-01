class Person():
	def inputname(self,fname,lname):
		self.fname = fname
		self.lname = lname	
	def showfull(self):
		print self.fname+" "+self.lname
p = Person()
p.inputname('veera','Nitesh')
p.showfull()
p.inputname('ajjsa','jahdasd')
p.showfull()
