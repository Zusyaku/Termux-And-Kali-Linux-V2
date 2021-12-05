#!/usr/bin/python
# -*- coding: utf-8 -*
#!/usr/bin/python
#####################################
## Author : Shin_Code 
## Youtube : Logic Internet
## Blog : https://www.blog-gan.org
## Created 24/08/2k20
## Thanks For h0d3_94n
#####################################
import requests, sys, re, os, time, random
from colorama import Fore, Back, Style

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
              Hackersid Grabber - Jamet31337
                  Ajibarang - 24 Agustus                   
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)



cls()
print_logo()

user = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0"}

try:
    __Defacer = raw_input('Nama Heker Disini@ ~#: ')
except IndexError:
    print kuning + '-----------------------------------------'
    print abang + '[*]' + kuning + ' Python ' + ijo + 'heker.py ' + putih + 'Name_of_defacer ' + y
    print(Style.RESET_ALL)
    sys.exit()


	
print ijo +   'Notifier is : ' + __Defacer
for page in range(1, 40):
	url = 'https://hackersid.com/api/hacker/' + __Defacer + '/' + str(page)
	sess = requests.session()
	Open = sess.get(url, timeout=10,headers=user)
	if Open.status_code == 200 and 'http:' in Open.text:
		print mbohopo + '[ Jamet_Code ]' + ' = ' + ijo +'https://hackersid.com/archive/notifier/'+__Defacer+'/',page
		rpp = re.findall('"url":"(.*?)",', Open.text)
		for iii in rpp:
			iii = iii.replace("\\","")
			open('hekersid.txt', 'a').write(iii+'\n')
	else:
		print kuning + 'Jamet_Ganteng' +' ' + 'Ganti Nama Defacer Bro'
		break
