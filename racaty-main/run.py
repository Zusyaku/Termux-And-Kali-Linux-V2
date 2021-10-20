# by Lord Yutix

import requests
from bs4 import BeautifulSoup

def getlink(url):
	unx = url.split('net/')[1]
	hdr = {'user-agent':'Mozilla/5.0 (Linux; Android 10; SM-A115F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.152 Mobile Safari/537.36'}
	dat = {'op':'download2','id':unx,'rand':'','referer':'','method_free':'','method_premium':''}
	raw = requests.post(url,data=dat,headers=hdr).text
	new = BeautifulSoup(raw,'html.parser').find('a',{'id':'uniqueExpirylink'})['href']
	return new

yoo = getlink('https://racaty.net/5teckmixflsp')
print(yoo)
