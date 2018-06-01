import telnetlib

tn = telnetlib.Telnet('http://w3schools.com')
tn.read_until(' ')
print tn
