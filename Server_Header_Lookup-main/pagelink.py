#Server Header Lookup
# Official Blog : https://www.blog-gan.org 
##############################
import requests
from time import time as timer  
import time
from re import findall as reg
year = time.strftime("%d/%m/%y")


text = raw_input('\033[31mServer Header Lookup : ')

test = requests.get('https://api.hackertarget.com/pagelinks/?q='+text).content
if '.' in test:
	print('\033[32m'+test)