import subprocess
s = subprocess.check_output('ls -l',shell=True)
#print s
s = subprocess.call(['ls -l'],shell=True)
print s
