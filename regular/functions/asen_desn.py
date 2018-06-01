def asen(num):
	if num > 0:
		asen(num-1)
		print num,
def decen(num):
	if num > 0:
		print num,
		decen(num-1)
	 
num = input('Enter a number: ')
asen(num)
decen(num)
