#!/usr/bin/python
#coding=utf-8

import os
import sys
import time
import json
import requests

bacot = ('''\033[1;91m                               \n@@@@@@@   @@@@@@   @@@  @@@  @@@@@@@@  @@@  @@@  \n@@@@@@@  @@@@@@@@  @@@  @@@  @@@@@@@@  @@@@ @@@  \n  @@!    @@!  @@@  @@!  !@@  @@!       @@!@!@@@  \n  !@!    !@!  @!@  !@!  @!!  !@!       !@!!@!@!  \n  @!!    @!@  !@!  @!@@!@!   @!!!:!    @!@ !!@!  \n  !!!    !@!  !!!  !!@!!!    !!!!!:    !@!  !!!  \n  !!:    !!:  !!!  !!: :!!   !!:       !!:  !!!  \n  :!:    :!:  !:!  :!:  !:!  :!:       :!:  !:!  \n   ::    ::::: ::   ::  :::   :: ::::   ::   ::  \n   :      : :  :    :   :::  : :: ::   ::    :\033[1;97m\n\n\033[41;1m ☆ Raka ☆ ™︻®╤───────═◍➤ \033[00;1m\n''')

os.system('clear')
print (bacot)

u = raw_input('\033[1;97m[\033[1;91m×\033[1;97m] Username : ')
p = raw_input('\033[1;97m[\033[1;91m×\033[1;97m] Password : ')
bangsat = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+u+'&locale=en_US&password='+p+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')

lop = bangsat.content
croot = json.loads(lop)
if "session_key" in lop:
                print "\n\033[1;97m[\033[1;91m×\033[1;97m] Your Access Token : \033[1;92m\n"
		print "" + croot["access_token"]
		print "\033[1;97m"
		open("token.txt", 'a').write(croot["access_token"])
		
else:
		print "\n\033[1;97m[\033[1;91m×\033[1;97m] Login Failed !!!"
		print " "
                
                
                
                
