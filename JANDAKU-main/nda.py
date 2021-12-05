'''    ___  ____ ___  ____ ____    ____ ____ ____ ____ ___  ____ 
       |__] |___ |__] |__| [__     |__/ |___ |    |  | |  \ |___ 
       |__] |___ |__] |  | ___]    |  \ |___ |___ |__| |__/ |___ '''
#!/bin/usr/python
from multiprocessing.pool import ThreadPool
from getpass import getpass
import os, urllib.request, sys, json, time, hashlib, random, shutil, re, threading
from bs4 import BeautifulSoup
try:
    import mechanize
    import requests
except ImportError:
    os.system('pip install mechanize')
    os.system('pip install requests')
if sys.version[0] == '2':
    print(green('[INFO]'),(k),'Ini Menggunakan Python3!')
    sys.exit(1)
sleep = time.sleep
h = '\x1b[32m'
r = '\x1b[1;91m'
k = '\x1b[1;97m'
n = '\033[94m'
W = "\033[0m"
G = '\033[32;1m'
R = '\033[31;1m'
time.sleep(1)
back = 0
lol = []
idd = []
threads = []
berhasil = []
cekpoint = []
gagal = []
idb = []
listgrup = []
id = []
ibb = []
s = ('   Thanks to : Indo'+n+'⟬'+R+'X'+n+'⟭'+k+'ploit'+r+' and '+k+'Python Indonesia')
t = ('                       Token')
m = ('              Multibruteforce Facebook') 



user_agent_list = [
   #Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    #Firefox
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)',
]

proxies_list = [
    'http://10.10.1.10:3128',
    'http://77.232.139.200:8080',
    'http://78.111.125.146:8080',
    'http://77.239.133.146:3128',
    'http://74.116.59.8:53281',
    'http://67.53.121.67:8080',
    'http://67.78.143.182:8080',
    'http://62.64.111.42:53281',
    'http://62.210.251.74:3128',
    'http://62.210.105.103:3128',
    'http://5.189.133.231:80',
    'http://46.101.78.9:8080',
    'http://45.55.86.49:8080',
    'http://40.87.66.157:80',
    'http://45.55.27.246:8080',
    'http://45.55.27.246:80',
    'http://41.164.32.58:8080',
    'http://45.125.119.62:8080',
    'http://37.187.116.199:80',
    'http://43.250.80.226:80',
    'http://43.241.130.242:8080',
    'http://38.64.129.242:8080',
    'http://41.203.183.50:8080',
    'http://36.85.90.8:8080',
    'http://36.75.128.3:80',
    'http://36.81.255.73:8080',
    'http://36.72.127.182:8080',
    'http://36.67.230.209:8080',
    'http://35.198.198.12:8080',
    'http://35.196.159.241:8080',
    'http://35.196.159.241:80',
    'http://27.122.224.183:80',
    'http://223.206.114.195:8080',
    'http://221.120.214.174:8080',
    'http://223.205.121.223:8080',
    'http://222.124.30.138:80',
    'http://222.165.205.204:8080',
    'http://217.61.15.26:80',
    'http://217.29.28.183:8080',
    'http://217.121.243.43:8080',
    'http://213.47.184.186:8080',
    'http://207.148.17.223:8080',
    'http://210.213.226.3:8080',
    'http://202.70.80.233:8080',
]
sleep(0.2)
os.system('clear')
def tik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)
print(k)
def logo():
        os.system('clear')
        print(R,'   ╔═╗                  ╔═╗╔╗')
        print(R,'   ║╔╝                  ║╔╝║║')
        print(R,'  ╔╝╚╗╔══╗╔═╗╔══╗╔══╗  ╔╝╚╗║╚═╗',G,'Author  : As'+R+'_'+G+'Min')
        print(R,'  ╚╗╔╝║╔╗║║╔╝║╔═╝║║═╣  ╚╗╔╝║╔╗║',G,'Github  : asmin19',k)
        print('    ║║ ║╚╝║║║ ║╚═╗║║═╣   ║║ ║╚╝║',G,'Version : 3.0',k)
        print('    ╚╝ ╚══╝╚╝ ╚══╝╚══╝   ╚╝ ╚══╝')
        print(r+'###################################################'+k)
a = ('===================================================')
def about():
    logo()
    print('')
    tik(s)
    print('')
    print(R+'...................[INFORMATION]...................'+k)
    print('')
    print('Creator                Asmin')
    print('About this tools       All about hacking facebook accounts')
    print('Version                3.0')
    print('Special thanks to     '+G+' Khoirul Amsori'+k+' and'+G+' Ez Nhana Hna'+k)
    print('Code name              As'+r+'_'+k+'Min')
    print('Team                   Buton '+R+'Sec'+k+'.')
    print('E-mail                 asmin987asmin@gmail.com')
    print('Github                 asmin19')
    print('Telegram               @asmin19')
    print('WhatsApp               +62 852-6834-5036')
    print('Date                   20:15 13-07-2019')
    print('Region                 Baubau,Sulawesi Tenggara, Indonesia')
    print('Support Password       xxx123, xxx12345, xxx12, xxx, birthday, sayang, minions, number, and many more')
    print('New Features           You can crack with'+R+' Super-Multibruteforce'+k+' from friendlist your friends')
    print(n+'Coming Soon            Checker IG')
    print('')
    tik(G+'* contact author to '+R+'BUY'+G+' the script ')
    print(k)
    input('[+] Press [Enter] to return ')
    menu()
def menu():
    print(k)
    logo()
    print(s)
    print(a)
    print('''  [ 01 ] Create Wordlist
  [ 02 ] Bruteforce
  [ 03 ] Multibruteforce Facebook
  [ 04 ] Friends Information
  [ 05 ] Token
  [ 06 ] About
  [ 00 ] Exit
  ''')
    try:
        asm = input(n+'[#] Asmin'+k+'/' + r+'~' + k + '> ')
        if asm in ['']:
            tik(R+'[!] Please enter your choice ')
            input('[+] Press [Enter] to return ')
            menu()
        elif asm in ['1','01']:
            about()
        elif asm in ['2','02']:
            about()
        elif asm in ['3','03']:
            about()
        elif asm in ['4','04']:
            about()
        elif asm in ['5','05']:
            about()
        elif asm in ['6','06']:
            about()
        elif asm in ['0','00']:
            exit()
        else:
            tik(R+'[!] Wrong input')
            input(n+'[+] Press [Enter] to return ')
            os.system('clear')
            logo()
            print(s)
            print(a)
            menu()
    except EOFError:
        exit()
    except KeyboardInterrupt:
        exit()
menu() 
