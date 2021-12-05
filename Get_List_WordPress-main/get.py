#Get Wordpress SiteList 
#!/usr/bin/python
# -*- coding: utf-8 -*
#JametKNTLS - h0d3_g4n - Moslem - Jenderal92
# Blog : https://www.blog-gan.org          
#DONATE ME :(
	# BTC = 31mtLHqhaXXyCMnT2EU73U8fwYwigiEEU1
	# PERFECT MONEY  = U22270614
##############################
import sys, os, re, socket, binascii, time, json, random, threading, Queue, pprint, urlparse, smtplib, telnetlib, os.path, hashlib, string, urllib2, glob, sqlite3, urllib, argparse, marshal, base64, colorama, requests
from time import time as timer  
from re import findall as reg
year = time.strftime("%d/%m/%y")

banner =  """
      \033[33mJamet Crew X KNTL Megalodon
       Icq : https://icq.im/Shin403
       Blog : https://www.blog-gan.org          
       Online Tools : http://secpriv8.com
"""
print banner


epp = raw_input('\033[0mTheme Name@ ~#: ')
pagr = raw_input('\033[0mPage@ ~#: ')

print('\033[33mDimulai Dari Angka 2 Bro !!! ')

for page in range(1, int(pagr)):
	state = ['us1', 'us2', 'us3', 'us4', 'us5', 'us6', 'us7', 'us8', 'us9', 'us10', 'us11', 'us12', 'us13', 'us14', 'us15', 'eu1', 'eu2', 'eu3', 'eu4', 'eu5', 'eu6', 'eu7', 'eu8', 'eu9', 'eu10']
	proxy = random.choice(state)
	ua = {'Origin': 'https://' + proxy + '.proxysite.com', 
	'Upgrade-Insecure-Requests': '1',
	'Referer': 'https://' + proxy + '.proxysite.com/process.php?d=d5ww0usE5q1XyjorWQH7sw%3D%3D&b=1&f=norefer',
	'Content-Type': 'application/x-www-form-urlencoded',
	'Content-Type': 'application/x-www-form-urlencoded',
	'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
	'Cookies': '_ga=GA1.2.589987225.1610038351; __gads=ID=bffe8a3c85dbe9de-228786b28fc5007f:T=1610038351:RT=1610038351:S=ALNI_Mbo8XuMGTbG0cfECZhdrpKMLkcBLA; _gid=GA1.2.1432847235.1623704158; c[themetix.com][/][IDE]=AHWqTUl0Im-eLYq4upcs9o_5nQC64Q4uAjr0LgWExpANROqkTn8bXVdImvD2PNcP'
	}
	data = {'allowCookies': 'on',
	'd': 'https://themetix.com/' +epp+'/'+str(page)}
	test = requests.post('https://' + proxy + '.proxysite.com/includes/process.php?action=update', data=data, headers=ua, timeout=10)
	if 'site' in test.content:
		print('\033[0mAuto Rotate Proxy'+ ' ' + proxy) 
		domen = reg('<p style="margin-bottom: 20px">(.*?)</p>', test.content)
		for cc in domen:
			print(str(cc)+'\033[32m[!] LAGI GRAB SLUR . . .')
			open('xx.txt','a').write('http://'+cc+'\n')