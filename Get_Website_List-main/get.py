#!/usr/bin/python
# -*- coding: utf-8 -*
#####################################
import requests, sys, re, os, time, random, json
from colorama import Fore, Back, Style
from re import findall as reg

abang = Fore.RED
ijo = Fore.GREEN
putih = Fore.WHITE
biru = Fore.BLUE
kuning = Fore.YELLOW
mbohopo = Fore.MAGENTA


def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])


def print_logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """
              PRIV GET DOMAIN WITH DATE - Jamet31337
                  Ajibarang - 05 OKTOBER 2K20                   
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)



cls()
print_logo()


try:
    MEMEK = raw_input('Date month Year@ ~#: ')
    ANJING = raw_input('Domain@ ~#: ')
except IndexError:
    print kuning + '-----------------------------------------'
    print abang + '[*]' + kuning + ' Python ' + ijo + 'heker.py ' + putih + 'Name_of_defacer ' + y
    print(Style.RESET_ALL)
    sys.exit()


	
print ijo +   'SCANNING : ' + MEMEK
print ijo +   'SCANNING : ' + MEMEK
for page in range(1,9999):
	Agent1 = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36'}
	url = 'https://domain-status.com/archives/'+MEMEK+'/'+ANJING+'/registered/'+str(page)
	KONTOL = requests.get(url, timeout=10,headers=Agent1).content
	if 'www' in KONTOL:
		domen = reg('<a href="(.*?)">', KONTOL)
		for x in domen:
			print(str(x) + ijo + '[!] LAGI GRAB SLUR . . .')
			for site in x:
				kimak = site.replace("https://domain-status.com/www/","").replace("https://domain-status.com/archives/","").replace("/com/registered/","").replace("/org/registered/","")
				open('ipgoblok.txt', 'a').write('http://'+kimak+'\n')
