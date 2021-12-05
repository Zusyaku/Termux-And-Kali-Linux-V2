# -*- coding: utf-8 -*

#!/usr/bin/python

#Filemanager - JametKNTLS -h0d3_g4n -Moslem

#####################################

import requests, re, urllib2, os, sys, codecs, random				from multiprocessing.dummy import Pool					     	

from time import time as timer	

import time

import json				   		

from platform import system	

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

##########################################################################################

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

#####################################

##########################################################################################

def logo():

    clear = "\x1b[0m"

    colors = [36, 32, 34, 35, 31, 37]

    x = """

          \033[31m\   \033[31m/

   \033[34m----- (9\033[31m"-_-\033[34m)9  \033[37mVs  \033[34m6(\033[31mx_x"\033[34m6) -----

   '

   \033[32m>--------------------------------<

   - Jamet Crew - Scanner Filemanager -

   

   \033[41m\033[1;33m[Youtube : Logic Internet\033[0m

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

##########################################################################################

def fileman(url):

	try:

		head = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36'}

		dancok = ['/filemanager','/assets/administrator/filemanager','/assets/admin/js/filemanager','/assets/plugins/filemanager','/assets/filemanager']

		for asu in dancok:

			cuk = requests.post(url+asu+'/dialog.php', timeout=10, headers=head).content

			if 'path_thumb' in cuk:

				print  (ijo+'> Found Filemanager : '+url)

				open('fileman.txt', 'a').write(url+asu+'/dialog.php'+'\n')

			else:

				print(url+ abang + '[!] Not Found . . .')

	except:

		pass

	pass

  

##########################################################################################

def Main():

    try:

        start = timer()

        pp = Pool(int(crownes))

        pr = pp.map(fileman, ooo)

        print('TIME TAKE: ' + str(timer() - start) + ' S')

    except:

        pass

if __name__ == '__main__':

    Main()

    
