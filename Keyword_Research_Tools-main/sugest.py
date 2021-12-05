# Keyword Research Tool
# Official Blog : https://www.blog-gan.org
import requests
from time import time as timer  
import time
from re import findall as reg
year = time.strftime("%d/%m/%y")


text = raw_input('\033[31mKeyword Research Tool: ')

test = requests.get('http://suggestqueries.google.com/complete/search?output=toolbar&hl=id&q='+text).content
if '<toplevel>' in test:
	regx = reg('<suggestion data="(.*?)"/>', test)
	for regs in regx:
		print('\033[0mResult :' +' ' + '\033[32m'+regs)
