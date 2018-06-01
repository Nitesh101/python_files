import re
str1 = """a1b2c3ddddd444eeee66gsgg7777sgggjigl9999"""
match = re.findall(r'(\D)',str1)
print match
sep = ''
print (sep.join(match))
