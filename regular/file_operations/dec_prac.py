def new_decorator(a_func):
	def wrappedfunction():
		print "I am doing before domr thing"
		a_func()
		print "I am doing after something"
	return wrappedfunction
@new_decorator
def dunction():
	print "new function"
dunction()
