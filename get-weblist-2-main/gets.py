#!/usr/bin/python
# -*- coding: utf-8 -*
#Greetz : Jamet31337 - JametKNTLS - h0d3_g4n - Moslem - Kiddenta
#http://secpriv8.com/crack.php
#https://www.blog-gan.org
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
    PRIV GET DOMAIN  WITH A-Z - KNTL MEGALODON
               Ajibarang - 06 May 2K21                   
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)



cls()
print_logo()


try:
    MEMEK = raw_input('Domain@ ~#: ')
    HANCOK = raw_input('A-Z ~#: ')
except IndexError:
    print kuning + '-----------------------------------------'
    print abang + '[*]' + kuning + ' Python ' + ijo + 'heker.py ' + putih + 'Name_Themes ' + y
    print(Style.RESET_ALL)
    sys.exit()


	
print ijo +   'SCANNING : ' + MEMEK
print ijo +   'SCANNING : ' + HANCOK
try:
	Agent1 = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36'}
	url = 'https://www.pagesinventory.com/tld/'+MEMEK+'/'+HANCOK+'.html'
	KONTOL = requests.get(url, timeout=10,headers=Agent1).content
	if '/tld/' in KONTOL:
		regx = reg('<td><a href="\\/domain\\/(.*?).html">', KONTOL)
		for x in regx:
			print(str(x)+ ijo + '[!] LAGI GRAB SLUR . . .')
			open('lists.txt', 'a').write('http://'+x+'\n')
except:
	pass
