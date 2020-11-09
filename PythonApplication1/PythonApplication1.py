
import getpass
import sys
import telnetlib

host = "10.1.100.113"
user = input ("Enter your user: ")
password = getpass.getpass()

tn = telnetlib.Telnet(host)

tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write("show run\n")
 
print (tn.read_all().decode('ascii'))




