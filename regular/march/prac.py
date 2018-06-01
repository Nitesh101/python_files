class MaxSize(object):
	ls =[]	
	def __init__(self,mx):
		self.val=mx
	def push(self,sr):
		self.ls.append(sr)
	def get_lst(self):
		while len(self.ls) != self.val:
			self.ls.pop()
		return self.ls
a =MaxSize(3)
a.push('ij')
a.push('bdhahfv')
a.push('data')
a.push('nitehs')
print a.get_lst()
