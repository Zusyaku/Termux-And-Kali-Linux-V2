#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import requests

print ("""                               
 _____   _ _ _____     _     _     
|   | |_| |_|   __|_ _| |_ _| |___ 
| | | | . | |__   | | | . | . | . |
|_|___|___|_|_____|___|___|___|___|
--------------------------Tegal1337
""")

domain = input("[+] Input domain ndisit : ")
print ("[+] Sabar boss proses ... \n")

def main(domain):
	url = "https://sonar.omnisint.io/subdomains/{}".format(domain)
	data = requests.get(url).json()
	print ("[+] Olihe kie tok : \n")
	for i in data:
		print(i)
		open('Result.txt','a').write(str(i) + '\n')

if __name__ == '__main__':
	main(domain)
