import os
import shutil
source = os.listdir("/home/madisnit/Desktop/python")
destination = "/home/madisnit/Desktop/python/regular"
for files in source:
	if files.endswith(".pptx"):
		shutil.move(files,destination)
