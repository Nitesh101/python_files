import os,shutil
val = "/home/madisnit/Desktop/python"
source = os.listdir(val)
val2 = "/home/madisnit/Desktop/python/regular"
for i in source:
	if i.endswith(".py"):
		shutil.move(i,val2)

		
