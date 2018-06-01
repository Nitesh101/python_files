class MaxSizeLisr(object):
	lst = []
	def __init__(self,mx):
		self.val =mx
	def push(self,st):
		self.lst.append(st)
	def get_list(self):
		while len(self.lst) != self.val:
			self.lst.pop(0)
		return self.lst
a = MaxSizeLisr(3)
a.push("ji")
a.push('hello')
a.push('there')
a.push('go')
print a.get_list()
