st = """Name:alice allison Age:23
Occupation:Spy
Name:BobBarkely Age:45
Occupation:Fry cook
Name:Carol Carson Age:44
Occupation:Manager
Name:Prince Age:53
Occupation:World class musician"""

f=st.replace("A", "\nA")

keys = []
values = []
for val in f.split("\n"):
	if val.startswith("Name"):
		keys.append(val.split(":")[1])
	elif val.startswith("Age"):
		values.append(val.split(":")[1])

op = dict(zip(keys, values))
print(op)
		 
