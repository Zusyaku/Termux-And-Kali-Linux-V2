import os
import sys

#collor
white = "\033[97m"
Red = "\033[31m"

os.system("clear")
banner = """
=========================
|   \033[31m Dhen Bhocil Tols Mass Add HTTP_-\033[97m
=========================
"""
print(banner)
def good():
	try:
		target=open(raw_input("Masukan list : "),'r').read().splitlines()
		for site in target:
			site.strip()
			print('\033[31m[#] Mass Add\033[97m '+'http://'+site)
			wh=open("succes.txt","a").write('https://'+site+'\n')
	except:
		pass
       
good()