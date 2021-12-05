#Google Trends Keyword
# Official Blog : https://www.blog-gan.org 
##############################
import requests
from time import time as timer  
import time
from re import findall as reg
year = time.strftime("%d/%m/%y")

print('\033[31mGoogle Trends Keyword' + ' ' + year)

test = requests.get('https://trends.google.com/trends/hottrends/atom/feed?pn=p19').content
if '<rss xmlns:atom=' in test:
	regx = reg('<title>(.*?)</title>', test)
	for regs in regx:
		trends = regs.replace('Daily Search Trends','')
		print( '\033[32m'+trends)