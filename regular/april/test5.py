str = """Name:allison Age:23 
Occupation:Spy 
Name:BobBarkely Age:45 
Occupation:Fry cook 
Name:Carol Carson Age:44 
Occupation:Manager 
Name:Prince Age:53 
Occupation:World class musician"""
fa = str.replace("A","\nA")
keys = []
values = []
for i in fa.split("\n"):
	if i.startswith("Name"):
		keys.append(i.split(':')[1])
	elif i.startswith("Age"):
		values.append(i.split(':')[1])
op = dict(zip(keys,values))
print op
