from urllib3.util.retry import Retry
import requests
from requests.adapters import HTTPAdapter
import sys
import random
import requests, threading, os
import os.path
import threading
import json
from multiprocessing.dummy import Pool as ThreadPool
from colorama import Fore, init, Style
init(autoreset=True)
os.system('cls' if os.name == 'nt' else 'clear')
print("""

╭━━━╮╱╱╱╱╭━━┳━━━╮
┃╭━╮┃╱╱╱╱╰┫┣┫╭━╮┃
┃╰━╯┣━━┳╮╭┫┃┃╰━╯┃
┃╭╮╭┫┃━┫╰╯┃┃┃╭━━╯
┃┃┃╰┫┃━╋╮╭┫┣┫┃Coded By Tegal1337
╰╯╰━┻━━╯╰┻━━┻╯
Reverse IP And Subdomain Scanner
1.Reverse
2.Reverse + Subdomain
3.Domain To Ip
""")
select = input("senpai@tegalsec:~# ")


if select == "1":
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
                    print ("[?] "+cut(target, 15)+" {}=> ".format(Fore.WHITE) +"{}Maybe Domains Down".format(Fore.RED))
                else:
                    result = json.loads(getdom.text)
                    print ("[+] {} => {} Domains".format(cut(str(target) ,15), len(result)))
                    for domain in result:
                        open('Resultz.txt', 'a').write('http://' + domain + "\n")
            except:
                pass
        print ("{}Reverse IP".format(Fore.RED))
        print("===============================")
        os.system('dir' if os.name == 'nt' else 'ls')
        target = open(input(Fore.WHITE+'List:~# '),'r').read().replace('http://', '').replace('https://', '').splitlines()
        Thread = input(Fore.WHITE+'Thread:~# ')
        pool = ThreadPool(int(Thread))
        pool.map(revip, target)
        pool.close()
        pool.join()
        print("===============================")
        count_result = len(open("Resultz.txt").readlines())
        print("[ + ] Total Result : "+str(count_result))
elif select == "2":
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
            getdom = requests.get("https://sonar.omnisint.io/reverse/" + target and "https://sonar.omnisint.io/subdomains/" + target)
            if "null" in getdom.text:
                print ("[?] "+cut(target, 15)+" {}=> ".format(Fore.WHITE) +"{}Maybe Domains Down".format(Fore.RED))
            else:
                result = json.loads(getdom.text)
                print ("[+] {} => {} Domains".format(cut(str(target) ,15), len(result)))
                for domain in result:
                    open('Resultz.txt', 'a').write('http://' + domain + "\n")
        except:
            pass
    print ("{}Reverse IP And Subdomain Scanner".format(Fore.RED))
    print("===============================")
    os.system('dir' if os.name == 'nt' else 'ls')
    target = open(input(Fore.WHITE+'List:~# '),'r').read().replace('http://', '').replace('https://', '').splitlines()
    Thread = input(Fore.WHITE+'Thread:~# ')
    pool = ThreadPool(int(Thread))
    pool.map(revip, target)
    pool.close()
    pool.join()
    print("===============================")
    count_result = len(open("Resultz.txt").readlines())
    print("[ + ] Total Result : "+str(count_result))
elif select == "3":


    def ip(site):

    		site = i.strip()
    		try:
    			if 'http://' not in site:
    				IP1 = socket.gethostbyname(site)
    				print (site + " => " +IP1)
    				open('ips.txt', 'a').write(IP1+'\n')
    			elif 'http://' in site:
    				url = site.replace('http://', '').replace('https://', '').replace('/', '')
    				IP2 = socket.gethostbyname(url)
    				print (site +  " => " +IP2)
    				open('ips.txt', 'a').write(IP2+'\n')

    		except:
    			pass
    print ("{}Domain To IP".format(Fore.RED))
    print("===============================")
    os.system('dir' if os.name == 'nt' else 'ls')
    nam=input('List:~# ')
    with open(nam) as f:
        for i in f:
            ip(i)


else:
    print ("Your Brain Error!")
