import os
os.system('clear')
os.system('rm -rf /sdcard/report-tiktok')
os.system('rm -rf /report-tiktok')
os.system('rm -rf /sdcard/REOPRT-TIKTOK.py')
os.system('rm -rf /REOPRT-TIKTOK.py')
os.system('rm -rf /sdcard/download/report-tiktok')
os.system('rm -rf /sdcard/download/REOPRT-TIKTOK.py')

import os
os.system('pip install requests')
os.system('clear')


import os,requests,re,time,datetime
os.system('rm -rf ID-TIKTOK.txt')
os.system('id -u > ID-TIKTOK.txt')
uidd = open('ID-TIKTOK.txt', 'r')
for j in uidd:
    sp = j.split()

def chk(): 
  uuid = str(os.geteuid()) + str(os.getlogin()) 
  id = "|".join(uuid) 
  print("\n\n\x1b[37;1m  YOUR ID : "+id) 
  try: 
    httpCaht = requests.get("https://raw.githubusercontent.com/hamalord4444/report-tiktok/main/ID-TIKTOK.txt").text 
    if id in httpCaht: 
      print("\033[92m  YOUR ID IS ACTIVE. .......\033[97m") 
      msg = str(os.geteuid()) 
      time.sleep(1) 
      pass 
    else: 
      print("\x1b[91m YOUR ID IS NOT ACTIVE SEND MESSAGE TO MY-TELEGRAM @H_4_4_4_4_D\033[97m") 
      time.sleep(1) 
      sys.exit() 
  except: 
    sys.exit() 
    if name == '__main__': 
     print (logo)
     chk() 
    
chk()
os.system('clear')



import os
os.system('pip install requests')
os.system('clear')
os.system('pip install colorama')
os.system('clear')
os.system('pip install user_agent')
os.system('clear')


import os,requests,re,time
from colorama import Fore
import user_agent
import subprocess
import requests, user_agent,os ,sys, time, datetime
import requests
from user_agent import generate_user_agent
from datetime import datetime
from colorama import Fore
import colorama
colorama.init(autoreset=colorama)
green = Fore.LIGHTGREEN_EX
error=0
done=0
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1'
user_agent = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)'
user_agent = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)'
user_agent = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)'
user_agent = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)'
user_agent = 'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)'
user_agent = 'Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)'
user_agent = 'Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51'
user_agent = 'AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)'
user_agent = 'Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1; WOW64; Trident/5.0; FunWebProducts)'
user_agent = 'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
user_agent = 'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.21; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)'
user_agent = 'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
user_agent = 'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)'
user_agent = 'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)'
user_agent = 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3'
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)'
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)'
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)'
user_agent = 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E'
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1'
user_agent = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)'
user_agent = 'Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15'
user_agent = 'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57'
user_agent = 'Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413'
user_agent = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)'
user_agent = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)'
user_agent = 'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0'
user_agent = 'Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g'
user_agent = 'Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)'
user_agent = 'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125'
user_agent = 'Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)'
user_agent = 'Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413'
user_agent = 'Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)'
user_agent = 'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)'
user_agent = 'Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)'
user_agent = 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)'
user_agent = 'Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)'
user_agent = 'Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)'
user_agent = 'Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10'
user_agent = 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4'
user_agent = 'Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0'
user_agent = 'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10'
user_agent = 'Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)'
user_agent = 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)'
user_agent = 'Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)'
user_agent = 'Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)'
user_agent = 'Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16'
user_agent = 'Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1'
user_agent = 'Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)'
user_agent = 'Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51'
user_agent = 'Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)'
user_agent = 'Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)'
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7'
user_agent = 'BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0'
user_agent = 'Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)'
user_agent = 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)'
user_agent = 'Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)'
user_agent = 'Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)'
user_agent = 'Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10'
user_agent = 'Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)'
user_agent = 'Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007'
user_agent = 'BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179'
user_agent = 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3'
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)'
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)'
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)'
user_agent = 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E'
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1'
user_agent = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)'
user_agent = 'Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15'
user_agent = 'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57'
user_agent = 'Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413'
user_agent = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55'
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1'
user_agent = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)'
user_agent = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)'
user_agent = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)'
user_agent = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)'
user_agent = 'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)'
user_agent = 'Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)'
user_agent = 'Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51'
user_agent = 'AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)'
user_agent = 'Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1; WOW64; Trident/5.0; FunWebProducts)'
user_agent = 'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
user_agent = 'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.21; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)'
user_agent = 'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
user_agent = 'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)'
user_agent = 'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)'
user_agent = 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3'
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)'
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)'
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)'
user_agent = 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E'
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1'
user_agent = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)'
user_agent = 'Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15'
user_agent = 'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57'
user_agent = 'Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413'
user_agent = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)'
user_agent = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)'
user_agent = 'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0'
user_agent = 'Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g'
user_agent = 'Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)'
user_agent = 'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125'
user_agent = 'Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)'
user_agent = 'Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413'
user_agent = 'Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)'
user_agent = 'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)'
user_agent = 'Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)'
user_agent = 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)'
user_agent = 'Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)'
user_agent = 'Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)'
user_agent = 'Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10'
user_agent = 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4'
user_agent = 'Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0'
user_agent = 'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10'
user_agent = 'Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)'
user_agent = 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)'
user_agent = 'Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)'
user_agent = 'Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)'
user_agent = 'Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16'
user_agent = 'Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1'
user_agent = 'Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)'
user_agent = 'Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51'
user_agent = 'Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)'
user_agent = 'Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)'
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7'
user_agent = 'BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0'
user_agent = 'Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)'
user_agent = 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)'
user_agent = 'Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)'
user_agent = 'Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)'
user_agent = 'Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10'
user_agent = 'Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)'
user_agent = 'Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007'
user_agent = 'BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179'
user_agent = 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3'
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)'
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)'
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)'
user_agent = 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E'
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1'
user_agent = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)'
user_agent = 'Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15'
user_agent = 'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57'
user_agent = 'Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413'
user_agent = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Vivaldi/4.1'
user_agent = 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36'
os.system('clear')
print("""
\033[92m]

  ████████╗██╗██╗  ██╗████████╗ ██████╗ ██╗  ██╗
  ╚══██╔══╝██║██║ ██╔╝╚══██╔══╝██╔═══██╗██║ ██╔╝
     ██║   ██║█████╔╝    ██║   ██║   ██║█████╔╝ 
     ██║   ██║██╔═██╗    ██║   ██║   ██║██╔═██╗ 
     ██║   ██║██║  ██╗   ██║   ╚██████╔╝██║  ██╗
     ╚═╝   ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                              
██████╗ ███████╗██████╗  ██████╗ ██████╗ ████████╗
██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝
██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝   ██║   
██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║██╔══██╗   ██║   
██║  ██║███████╗██║     ╚██████╔╝██║  ██║   ██║   
╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
                                                  
                ██████╗ ██╗   ██╗
                ██╔══██╗╚██╗ ██╔╝
                ██████╔╝ ╚████╔╝ 
                ██╔══██╗  ╚██╔╝  
                ██████╔╝   ██║   
                ╚═════╝    ╚═╝   
                 
       ██╗      ██████╗ ██████╗ ██████╗ 
       ██║     ██╔═══██╗██╔══██╗██╔══██╗
       ██║     ██║   ██║██████╔╝██║  ██║
       ██║     ██║   ██║██╔══██╗██║  ██║
       ███████╗╚██████╔╝██║  ██║██████╔╝
       ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ 
                                 

      # REPORT TikTok V3
      * Updated by HAMA LORDY EZRAILY
      %100 REPORTED BY LORD
""")
print("""
        \033[91m[1][None] 
    
          \033[91m[2]-[Plagiarism User]         
      
        \033[91m[3]-[Plagiarism Me]
    
          \033[91m[4]-[SEX]         
      
        \033[91m[5]-[Self-Injury]      
       
          \033[91m[6]-[Annoying]
      
        \033[91m[7]-[Violence]      
    
          \033[91m[8]-[Under 13]        
      
        \033[91m[9]-[Cruelty animaly] 
    
          \033[91m[10]-[Cheat&Scam]   
      
        \033[91m[11]-[Terrorism]            
    
          \033[91m[12]-[Hate Speech]
      
        \033[91m[13]-[Child Abuse]  
    
          \033[91m[14]-[Violent Content]   
      
        \033[91m[15]-[Bad prof pic]
    
          \033[91m[16]-[Cotent]
      
        \033[91m[17]-[suicide]    
    
          \033[91m[18]-[Plagiarism Famous user]
       
        \033[91m[19]-[Hate Groups]  
    
          \033[91m[20]-[Promotion Of Criminal Activities]
      
""")
fl=int(input('CHOOSE ONES THIS REPORTS > '))
if fl==1:
    report_id=311
elif fl==2:
    report_id=3143
elif fl==3:
    report_id=3131
elif fl==4:
    report_id=308
elif fl==5:
    report_id=3052
elif fl==6:
    report_id=310
elif fl==7:
    report_id=3072
elif fl==8:
    report_id=317
elif fl==9:
    report_id=304
elif fl==10:
    report_id=3024
elif fl==11:
    report_id=3011
elif fl==12:
    report_id=306
elif fl==13:
    report_id=3093
elif fl==14:
    report_id=303
elif fl==15:
    report_id=3141
elif fl==16:
    report_id=399
elif fl==17:
    report_id=3051
elif fl==18:
    report_id=3073
elif fl==19:
    report_id=3013
elif fl==20:
    report_id=3021
print("---------------------------------------------------------")
print('Updated By HAMA LORDY EZRAILY ')
print("---------------------------------------------------------")
#sessionid
sessionid = input('[?] Enter Sessionid : ')
target = input('[?] Enter Username Target : ')
sleep = int(input('[?] Enter Sleep [1/10] : '))
print("*********************************************************")
url_CHECK_sessionid = 'https://api16-normal-c-alisg.tiktokv.com/passport/login_name/update/?residence=SA&device_id=6904193135771207173&os_version=14.2&app_id=1233&iid=6946987757887047426&app_name=musical_ly&vendor_id=3E86AE5D-1475-4A78-A34E-DCE1C9091FFE&locale=ar&ac=WIFI&sys_region=SA&ssmix=a&version_code=17.7.0&vid=3E86AE5D-1475-4A78-A34E-DCE1C9091FFE&channel=App%20Store&op_region=SA&os_api=18&idfa=D78BAC01-848D-4371-A604-7C3F3D678058&install_id=6946987757887047426&idfv=3E86AE5D-1475-4A78-A34E-DCE1C9091FFE&device_platform=iphone&device_type=iPhone10%2C6&openudid=59e0801cc11a5b89f399df1e1ad749afeed69600&account_region=&tz_name=Asia%2FRiyadh&tz_offset=10800&app_language=ar&carrier_region=SA&current_region=SA&aid=1233&mcc_mnc=42001&screen_width=1125&uoo=0&content_language=&language=ar&cdid=ECAD5F87-4334-4228-94D0-1D9958FC4EBD&build_number=177015&app_version=17.7.0&resolution=1125%2A2436'

headers_CHECK_sessionid = {
    'Host': 'api16-normal-c-alisg.tiktokv.com',
    'Connection': 'close',
    'Content-Length': '31',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-SS-Cookie': f'multi_sids=6778236784885122054%3A41059648ecde93eba0a905c184651adf%7C6946966238849844225%3A953d24738a88f45b4ca12f431525b848%7C6946988349706601473%3A41689832094ae90ae74053275dad09a5; odin_tt=c71c4d9ee4202c651a57ac5b0374a372d9d76f8fca63c3685caf68dac157bccde371c79258427c0ebfef25e27f154f3e2050bae55372e2584203c52780933ddf; sessionid=41689832094ae90ae74053275dad09a5; sessionid_ss=41689832094ae90ae74053275dad09a5; sid_guard=41689832094ae90ae74053275dad09a5%7C1617472026%7C5184000%7CWed%2C+02-Jun-2021+17%3A47%3A06+GMT; sid_tt=41689832094ae90ae74053275dad09a5; store-country-code=sa; store-idc=alisg; uid_tt=9719aa5f7b71b36a7208cec16e785653f095610219b8e792127acff7f77203bf; uid_tt_ss=9719aa5f7b71b36a7208cec16e785653f095610219b8e792127acff7f77203bf; install_id=6946987757887047426; ttreq=1$c6ea408e3f2a28056cb33132cca7c7d29e77992b; cmpl_token=AgQQAPO_F-RPsLBWeltddB04xbEGIBnKf4c0YPjPAA; d_ticket=ab7d42861b134f5a7cefb8addd65d9ceea3a4; passport_csrf_token={sessionid}; passport_csrf_token_default={sessionid}',
    'tt-request-time': '1617472075991',
    'x-tt-passport-csrf-token': sessionid,
    'Accept-Encoding': 'gzip, deflate',
    'X-Khronos': '1617472074',
    'X-Gorgon': '840280396000b30fdab8cc3fa84c05f5a04e008f327ac53688fc',
}

    #cookies_check_sessionid
cookies_CHECK_sessionid = {'sessionid': sessionid}
    #data_check_sessionid
data_CHECK_sessionid = {'login_name': ''}
    #req_check_sessionid
req_CHECK_sessionid = requests.post(url_CHECK_sessionid, data=data_CHECK_sessionid, headers=headers_CHECK_sessionid, cookies=cookies_CHECK_sessionid).text
if ('"description":"معلمات مفقودة"') in req_CHECK_sessionid:
      print(Fore.LIGHTGREEN_EX + '[+] Logged In')
      

url_GET_sessionid = f'https://www.tiktok.com/@{target}?lang=en'
headers_GET_sessionid = {
                'Host': 'www.tiktok.com',
                'Cookie': 'tt_webid_v2=6940688826462406145; tt_webid=6940688826462406145; passport_csrf_token=bb82884d8da300de0ce4f8508694e635; passport_csrf_token_default=bb82884d8da300de0ce4f8508694e635; webapp_tiktok_lang=ar; tta_attr_id=0.1616499265.6942811476331593729; s_v_web_id=verify_kmxb0dd5_U5SMVNWR_g0Au_4r8J_9Qe3_NJxpQO88j1Pw; store-idc=alisg; store-country-code=sa; odin_tt=9e36bc7e668adaca285bdabfdc5522cae25ab7d5a6a56ef8880573ef4c692fdc1f7525f56ac9e3e77660cc380ad65f677e6b00464a9537d5bd8579e837063d3e19601cb7c2bfc2670cffac88be90fe15; ttwid=1%7Cgi8ynNW57o66_fiDbhBjBs9nnuaeZv-1OTK3G5gmasg%7C1620413005%7C394bbe09c3b44c4c9888d610307e0bac9d529e828f5039a5dc2e70b3727ca482; tt_csrf_token=biBAjWPswn1Ia8d_7rsdywQa; MONITOR_WEB_ID=6940688826462406145; R6kq3TV7=AJL0p1x5AQAAgZ7UVUQ6Z_KKbbeh5V5rk1UaC0j4uVifRF8UZNUVrUJz9fFZ|1|0|bde1f506e2e120b4c97406a027a957d96a261126; csrf_session_id=f542d4c150684c8f8b565e56b620bff7; ak_bmsc=22C2B083F339CBE14339EFA65156A32656335E77BE330000BFCA9A6082EF1008~pl9qoJSA+vGmaFbpQTQUctlmE8lshSuY6YHoGK6eAFcwNGgFZsreTcrHNbxxGmpbl2GeyKL5276g5I/XQbSNpcwrr3cLsZ08fYr1T8IsmfB4yVD4pNbOvvocKs0Kwp4oGdquXtKten+dumIsbOYePAhDb4MopA6mBiXQ7IMKkZ66Gs9jhPn/1L7izxuAnlkvBQ2t4Ll3JgjK10tgMrmeooyS384GIBMU/9anOAEvzrh5c=; bm_sz=922FB4C8CA0E7C5EE7AAE96ED45A8D14~YAAQd14zVmmwGkJ5AQAAifunXAu6DUsNarpL0o3/MO2WbnFS6FTTWKwxn2twV02yxkLnXZhK4KuYsQdEvSzvN5Waphqt67i1QrSkqjqjrI+ud2Ipf8kP0aYBPU3F6aZBaTASUC/LPWyw6VSsJBdp2axybcksh9iN4tbe8ckxe0fS9e0HXMtG4zg14NKmCMF2; _abck=494D5CEEE963A444A9BFED1397AE4A1A~-1~YAAQd14zVmqwGkJ5AQAAifunXAXD2Rm1wrf/kCpyHcjNt90XMNyT40T79i2Xiiv/+D7cSh+qO0hCvwfZPOdJLl1TZ/+70kjAkZhxQANKmbR1eG3hCoYziKZOVlLnIM4FvKCjI/8I0Ttyo2MPgy0k0Xd7aFV0JK9JNU0NBZTw4uTAjkpipxbcRFPw0Dzd6fxASkgbhUwGK866PwyfbVVffdeIqZ3USzyrTk6DR8lrU0M6tgsoRbx1/UY+Ue5MFQODr9n56Z6y/6LUuFPHj4WBLa3uxtRaCsS3ffZBU66+rGNterzLBrfZGhzNAYitw3Isd9LMfbDod658wtIzm98l6hqJ+n6aWgxydY/eajbXqFAttTM7k+1LBJdr/HyMCY0EM2MObB4OcU215xtAysmRP0vqjf+lRLvH3A==~-1~-1~-1; bm_sv=5608A62D5E68D2ACA227FA9D6C9729B5~ynyChzuEsfL9Mar+1BiTImNN57zWtpLNnHKGhFxnjMsNaku8SRDMmlYKktjrS+U4SY77kyFEgludaTbRHJVb7W6U/mpXQkWO3M5LkI89zaf3XOSkr/lH7gN3TIjLq2NmfZQcr5ItH2wUXsI/JIXnGpNoOsmTpj3e9ASoOmTXXQQ=',
                'Pragma': 'no-cache',
                'Cache-Control': 'no-cache',
                'Sec-Ch-Ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
                'Sec-Ch-Ua-Mobile': '?0',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-User': '?1',
                'Sec-Fetch-Dest': 'document',
                'Referer': f'https://www.tiktok.com/@{target}',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'en-US,en;q=0.9',}
   #req_get_id
    #data_sessionid
req_GET_sessionid = requests.get(url_GET_sessionid, headers=headers_GET_sessionid)
ID=re.findall('''"user":{"id":"(.*?)"''',req_GET_sessionid.text)[0]

    #check_sessionid
url_SEND_REPORT = 'https://www.tiktok.com/node/report/reasons_put?aid=1988&app_name=tiktok_web&device_platform=web_pc&device_id=6965670367281858049&region=SA&priority_region=SA&os=windows&referer=&root_referer=&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=ar&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows)&browser_online=true&verifyFp=verify_1836fc1bf3f7deccde3944b94542fa17&app_language=ar&timezone_name=Asia%2FRiyadh&is_page_visible=true&focus_state=true&is_fullscreen=false&history_len=4'
headers2 = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-length': '103',
    'content-type': 'application/json',
    'cookie': f'tt_webid_v2=6940688826462406145; tt_webid=6940688826462406145; passport_csrf_token=bb82884d8da300de0ce4f8508694e635; passport_csrf_token_default=bb82884d8da300de0ce4f8508694e635; webapp_tiktok_lang=ar; tta_attr_id=0.1616499265.6942811476331593729; s_v_web_id=verify_kmxb0dd5_U5SMVNWR_g0Au_4r8J_9Qe3_NJxpQO88j1Pw; tt_csrf_token=biBAjWPswn1Ia8d_7rsdywQa; R6kq3TV7=AJL0p1x5AQAAgZ7UVUQ6Z_KKbbeh5V5rk1UaC0j4uVifRF8UZNUVrUJz9fFZ|1|0|bde1f506e2e120b4c97406a027a957d96a261126; csrf_session_id=f542d4c150684c8f8b565e56b620bff7; ak_bmsc=22C2B083F339CBE14339EFA65156A32656335E77BE330000BFCA9A6082EF1008~pl9qoJSA+vGmaFbpQTQUctlmE8lshSuY6YHoGK6eAFcwNGgFZsreTcrHNbxxGmpbl2GeyKL5276g5I/XQbSNpcwrr3cLsZ08fYr1T8IsmfB4yVD4pNbOvvocKs0Kwp4oGdquXtKten+dumIsbOYePAhDb4MopA6mBiXQ7IMKkZ66Gs9jhPn/1L7izxuAnlkvBQ2t4Ll3JgjK10tgMrmeooyS384GIBMU/9anOAEvzrh5c=; bm_sz=922FB4C8CA0E7C5EE7AAE96ED45A8D14~YAAQd14zVmmwGkJ5AQAAifunXAu6DUsNarpL0o3/MO2WbnFS6FTTWKwxn2twV02yxkLnXZhK4KuYsQdEvSzvN5Waphqt67i1QrSkqjqjrI+ud2Ipf8kP0aYBPU3F6aZBaTASUC/LPWyw6VSsJBdp2axybcksh9iN4tbe8ckxe0fS9e0HXMtG4zg14NKmCMF2; _abck=494D5CEEE963A444A9BFED1397AE4A1A~-1~YAAQd14zVmqwGkJ5AQAAifunXAXD2Rm1wrf/kCpyHcjNt90XMNyT40T79i2Xiiv/+D7cSh+qO0hCvwfZPOdJLl1TZ/+70kjAkZhxQANKmbR1eG3hCoYziKZOVlLnIM4FvKCjI/8I0Ttyo2MPgy0k0Xd7aFV0JK9JNU0NBZTw4uTAjkpipxbcRFPw0Dzd6fxASkgbhUwGK866PwyfbVVffdeIqZ3USzyrTk6DR8lrU0M6tgsoRbx1/UY+Ue5MFQODr9n56Z6y/6LUuFPHj4WBLa3uxtRaCsS3ffZBU66+rGNterzLBrfZGhzNAYitw3Isd9LMfbDod658wtIzm98l6hqJ+n6aWgxydY/eajbXqFAttTM7k+1LBJdr/HyMCY0EM2MObB4OcU215xtAysmRP0vqjf+lRLvH3A==~-1~-1~-1; ttwid=1%7CwzXPnMZkgXiSYQk-tkK71Q8KqqRuVhoMRGQW1yNOtOE%7C1620760773%7C24fecb8fa91932b76e6480c16cb8392b7b1bfb21dd687901649d14a6ded3664e; sid_guard={sessionid}%7C1620760969%7C5184000%7CSat%2C+10-Jul-2021+19%3A22%3A49+GMT; uid_tt=7ade13dd61634ac8c0acf0504eb558b59373d907006ed6e825d82f5426c8c9e7; uid_tt_ss=7ade13dd61634ac8c0acf0504eb558b59373d907006ed6e825d82f5426c8c9e7; sid_tt={sessionid}; sessionid={sessionid}; sessionid_ss={sessionid}; store-idc=maliva; store-country-code=pl; cmpl_token=AgQQAPORF-RMpbBGYU5-pd08-jPehXJPv4M0YP-2vw; MONITOR_WEB_ID=6940688826462406145; odin_tt=2d633d2f05bf5413d4279330ba74e7937da365b1ad0d6d01a219b6815756822efd2a5aaf337235a3adc8413c8903a81c158921702571c55cc51e94cd1f87726a33fc6573aa3dbaf3a184c6f346685d21; bm_sv=5608A62D5E68D2ACA227FA9D6C9729B5~ynyChzuEsfL9Mar+1BiTImNN57zWtpLNnHKGhFxnjMsNaku8SRDMmlYKktjrS+U4SY77kyFEgludaTbRHJVb7W6U/mpXQkWO3M5LkI89zafyBPRe7FzV/zaJVNirebe/+vLtXNlOYpEcIbBeY4r/GnE46suCVkZVdiP3+CfbrLw=',
    'origin': 'https://www.tiktok.com',
    'pragma': 'no-cache',
    'referer': f'https://www.tiktok.com/@{target}?lang=ar',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'tt-csrf-token': 'biBAjWPswn1Ia8d_7rsdywQa',
    'user-agent': generate_user_agent(),
    'Tt-Csrf-Token': '9ABBszZbHK-ybQ4EmUNmO88d',
    'X-Secsdk-Csrf-Token': '0001000000014ea713b3201bdb67f32cded9fd338566179a21daa4321f512da8c2c7b50bcdba168c6503d189e850',
    'Te': 'trailers',
    'Connection': 'close'}
# DATA
   #data
data={
    "reason": f'{int(report_id)}',
    "object_id": ID,
    "owner_id": ID,
    "report_type": "user"}
print(str(data))
while True:
    time.sleep(sleep)
    rep = requests.post(url_SEND_REPORT,json=data,headers=headers2).text
    if ('"statusCode":0,"errMsg":"نشكرك على ملاحظاتك"') in rep:
                            #clear text
      os.system("clear")
      print(f'[{Fore.LIGHTMAGENTA_EX}Starting{Fore.RESET}]' + Fore.RESET)
      red = Fore.RED
      print(red + """
 __        ______   _______   _______  
|  \      /      \ |       \ |       \ 
| $$     |  $$$$$$\| $$$$$$$\| $$$$$$$\
| $$     | $$  | $$| $$__| $$| $$  | $$
| $$     | $$  | $$| $$    $$| $$  | $$
| $$     | $$  | $$| $$$$$$$\| $$  | $$
| $$_____| $$__/ $$| $$  | $$| $$__/ $$
| $$     \\$$    $$| $$  | $$| $$    $$
 \$$$$$$$$ \$$$$$$  \$$   \$$ \$$$$$$$ 
      """, Fore.LIGHTGREEN_EX + "\n                  ( @H_4_4_4_4_D )",
      Fore.LIGHTBLUE_EX + "\n   (This tool is programmed by the programmer : HAMA LORDY EZRAILY)              \n",
      Fore.LIGHTYELLOW_EX + "                ( Report TikTok )\n\n" + Fore.RESET)
      done +=1
      print(f'\r[+] REPORTED BY LORD [{done}] | Error Report [{error}]', end='')
      time.sleep(sleep)
    else:
      #clear Text
      os.system("cls")
      print(f'[{Fore.LIGHTMAGENTA_EX}Starting{Fore.RESET}]' + Fore.RESET)
      red = Fore.RED
      print(red + """
 __        ______   _______   _______  
|  \      /      \ |       \ |       \ 
| $$     |  $$$$$$\| $$$$$$$\| $$$$$$$\
| $$     | $$  | $$| $$__| $$| $$  | $$
| $$     | $$  | $$| $$    $$| $$  | $$
| $$     | $$  | $$| $$$$$$$\| $$  | $$
| $$_____| $$__/ $$| $$  | $$| $$__/ $$
| $$     \\$$    $$| $$  | $$| $$    $$
 \$$$$$$$$ \$$$$$$  \$$   \$$ \$$$$$$$ 
      """, Fore.LIGHTGREEN_EX + "\n                  ( @H_4_4_4_4_D )",
      Fore.LIGHTBLUE_EX + "\n   (This tool is programmed by the programmer : HAMA LORDY EZRAILY)              \n",
      Fore.RED + "                ( Report TikTok )\n\n" + Fore.RESET)
      print(f'[{Fore.LIGHTMAGENTA_EX}Starting{Fore.RESET}]' + Fore.RESET)
      print('')
      error +=1
      print(f'\r[+] REPORTED BY LORD [{done}] | Error Report [{error}]', end='')
      time.sleep(sleep)