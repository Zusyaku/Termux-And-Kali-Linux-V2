#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import optparse
from pexpect import pxssh

print ('''
>-------------------<
This is a simple ssh 
bot control unit
>-------------------<
Coding by Leeon123
>-------------------<''')

class Client:

    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.connect()

    def connect(self):
        try:
            s = pxssh.pxssh()
            s.login(self.host, self.user, self.password)
            return s
        except Exception as e:
            print(e)
            print('[-] Error Connecting')

    def send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before

def botnetCommand(command):
    for client in botNet:
        output = client.send_command(command)
        print('[*] Output from ' + client.host)
        print('[+] ' +str(output, encoding='utf-8')+ '\n')

def addClient(host, user, password):
    client = Client(host, user, password)
    botNet.append(client)

order = input("Command:")
botNet = []
addClient('host', 'username', 'passwd') # Inter your ssh server ip, username and password.
addClient('host','username','passwd')
botnetCommand(order)
