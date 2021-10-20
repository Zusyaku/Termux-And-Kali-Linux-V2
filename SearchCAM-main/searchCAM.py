#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#https://github.com/AngelSecurityTeam/SearchCAM
import requests
from bs4 import BeautifulSoup
import re , colorama 

colorama.init()
def bann():
  print("""
\033[1;31m
   ____                 __   ________   __  ___
  / __/__ ___ _________/ /  / ___/ _ | /  |/  /
 _\ \/ -_) _ `/ __/ __/ _ \/ /__/ __ |/ /|_/ / 
/___/\__/\_,_/_/  \__/_//_/\___/_/ |_/_/  /_/  
                           \033[1;39mAngelSecurityTeam\033[1;31m
  """)

bann()


def http_(keys, number):
    
    listing = []
    for i in range(0, int(number), 1):
        PAGE = i*10
        URL = 'https://www.google.de/search'
        PARAMETERS = {'q': str(keys), 'start': int(PAGE)}
        r = requests.get(URL, params=PARAMETERS)
        soup = BeautifulSoup(r.text, 'html.parser')
        parse_url = soup.findAll('div')
        for _url in parse_url:
            test = re.search(r"url\?q=(.+?)\&", str(_url))
            if test is not None:
                url = test.group(1)
                listing.append(url)
            else:
                pass

    url_list = (set(listing))
    for captura in url_list:
     print(captura)

datos = open('cam.txt', 'r')
for cam in datos:
    http_(cam,5) #5 number page default 
