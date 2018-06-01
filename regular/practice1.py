"""
def print_val(**kwargs):
	print type(kwargs)
	print kwargs
print_val(a=10,b=20)

def print_val(a,b=20):
	print a,b
print_val(10,20)
"""
def print_vals(*args ):

	print("a:", a, "b:",b, "args:", args,"kwargs:", kwargs)

	



print_vals(10, 20,30,40 )
