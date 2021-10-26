# -*- coding: utf-8 -*-
#!usr/bin/python
import requests, json
from multiprocessing.dummy import Pool as ThreadPool
from colorama import Fore, init, Style
init(autoreset=True)

def cut(text='',leng=False):
    if leng == False:
        ret = text
    else:
        length_string = len(text)
        if length_string > leng:
            ret = text[0:leng]
        else:
          neko = leng-length_string
          ret = text+' '*neko
    return str(ret)
    
def revip(target):
    try:
        getdom = requests.get("https://sonar.omnisint.io/reverse/" + target)
        if "null" in getdom.text:
            print "[?] "+cut(target, 15)+" | Failed"
        else:
            result = json.loads(getdom.text)
            print "[!] {} | {} Domains".format(cut(str(target) ,15), len(result))
            for domain in result:
                open('resultzz.txt', 'a').write('http://' + domain + "\n")
    except:
        pass
print "{}Reverse IP v1.0 | Tegal1337\n".format(Fore.YELLOW)
target = open(raw_input(Fore.WHITE+'List:~# '),'r').read().replace('http://', '').replace('https://', '').splitlines()
Thread = raw_input(Fore.WHITE+'Thread:~# ')
pool = ThreadPool(int(Thread))
pool.map(revip, target)
pool.close()
pool.join()
