import getpass
import sys
import telnetlib

HOST = "https://login.yahoo.com/?.src=fpctx&.intl=in&.lang=en-IN&authMechanism=primary&done=https%3A%2F%2Fin.yahoo.com%2F&eid=100&add=1"
user = raw_input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("login: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("ls\n")
tn.write("exit\n")

print tn.read_all()
