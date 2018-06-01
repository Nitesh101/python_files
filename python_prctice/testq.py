"""
lis1= [1,2,34,5]
lis = 'nitesh'
print  lis1[::-1]
print ''.join(reversed(lis))
#print ''.join(reversed(lis))

def reverse(s):
  r = ""
  for c in s:
    r = c + r
  return r
s = "String to reverse."
print reverse(s)
"""
import timeit
s = 'abcdefghijklmnopqrstuvwxyz' * 10
timeit.repeat(lambda: reverse_string1(s)) 
