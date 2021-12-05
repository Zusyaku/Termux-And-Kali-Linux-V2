# -*- coding: utf-8 -*
#!/usr/bin/python
#Thanks TO : JametKNTLS -  h0d3_g4n - Moslem And All Coders
#Blog : https://www.blog-gan.org
#YT : PY
################Command#####################
import requests, re, urllib2, os, sys, codecs, random				
from multiprocessing.dummy import Pool					     	
from time import time as timer	
import time
import socket
import json				   		
from platform import system	
from random import sample
from colorama import Fore								
from colorama import Style								
from pprint import pprint								
from colorama import init
from urlparse import urlparse
import warnings
import subprocess
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
reload(sys)  
sys.setdefaultencoding('utf8')
init(autoreset=True)
############Color###############
abang = '\033[31m'
ijo = '\033[32m'
kuning = '\033[33m'
birtu = '\033[34m'
ungu = '\033[35m'
biru = '\033[36m'
abu = '\033[37m'
putih = '\033[0m' 
year = time.strftime("%y")
month = time.strftime("%m")
############Shell Backdoor###############
############Logo###############

def logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """
          \033[31m\   \033[31m/
   \033[34m----- (9\033[31m"-_-\033[34m)9  \033[37mVs  \033[34m6(\033[31mx_x"\033[34m6) -----
   
   \033[32m>--------------------------------<
 Mass Alexa Rank Checker - Pwrd Ajibarang1337
   
   
   \033[41m\033[1;33m[Blog : https://www.blog-gan.org\033[0m
   \033[41m\033[1;33m[ICQ : https://icq.im/Shin403\033[0m
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)


logo()
start_raw = raw_input("\n\033[91mGive,Me List Dear\033[97m:~# \033[97m")
crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
try:
    with open(start_raw, 'r') as f:
        ooo = f.read().splitlines()
except IOError:
    pass
    
try:
    ooo = list(dict.fromkeys(ooo))
except NameError:
    print '\033[31mOpen Your Eyes!'
    sys.exit()
count=0
with open(start_raw,'r')as f:
 for line in f:
    count+=1
print '\x1b[91m[\x1b[92m+\x1b[91m]\x1b[92mTOTAL WEBLIST=',count

############Mulai :v###############

def Alexa(url):
	try:
		head = {'X-NewRelic-ID': 'VgcGVFNVCBABVFRXBAkBUF0B',
		'tracestate': '2115560@nr=0-1-2115560-1055386772-c6e5cb1361e18e6c----1633859372911',
		'traceparent': '00-a6434a140251cf0741d94da217ea2720-c6e5cb1361e18e6c-01',
		'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36',
		'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjIxMTU1NjAiLCJhcCI6IjEwNTUzODY3NzIiLCJpZCI6ImM2ZTVjYjEzNjFlMThlNmMiLCJ0ciI6ImE2NDM0YTE0MDI1MWNmMDc0MWQ5NGRhMjE3ZWEyNzIwIiwidGkiOjE2MzM4NTkzNzI5MTF9fQ==',
		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'Accept': 'application/json, text/javascript, */*; q=0.01',
		'X-Requested-With': 'XMLHttpRequest',
		'Origin': 'https://www.prepostseo.com',
		'Referer': 'https://www.prepostseo.com/bulk-alexa-rank-checker',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'Cookie': '_ga=GA1.2.68648232.1623915513; __gads=ID=a96f05747b680b63-220c9bf182c90048:T=1623915550:RT=1623915550:S=ALNI_MbZbMyhJpGIj1MT7-6gpThfs-oLFQ; ci_session=a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%223dce5eb5701bfc8dc091390c22ecc11b%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A23%3A%222404%3Ac0%3A7140%3A%3A1c0c%3A1bd7%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A120%3A%22Mozilla%2F5.0%20%28Linux%3B%20Android%2011%3B%20Redmi%20Note%209%20Pro%20Build%2FRKQ1.200826.002%3B%20wv%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Versi%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1633859339%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7De5e26fc391f3116451fc5fe725a8f7c3; _gid=GA1.2.1297237295.1633859363; _gat=1; _gat_gtag_UA_67516616_1=1'
		}
		Site = 'https://www.prepostseo.com/ajax/checkAlexaRank'
		data = {'url': url,
		'code':''}
		Alexar = requests.post(Site,data=data,headers=head).text
		domen = json.loads(Alexar)
		print(kuning+'[+]' + url + ijo + ': ' + domen["rank"])
		open('Alexa.txt', 'a').write(url+': ' +domen["rank"]+'\n')
	except:
		pass
	pass

############Penutup :v###############

def Main():
    try:
        start = timer()
        pp = Pool(int(crownes))
        pp = pp.map(Alexa, ooo)
        print('TIME TAKE: ' + str(timer() - start) + ' S')
    except:
        pass


if __name__ == '__main__':
    Main()
