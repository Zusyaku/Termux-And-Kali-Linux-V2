#Program : UserAgent
#Coder : Karjok Pangesty
#Tanggal : 9 November 2019 2:09AM
#Team: Cracker Noob Squads [https://t.me/CRABS_ID]
#Mengedit/Menghapus kredit nggak akan membuatmu jadi programmer

from requests import *
from bs4 import BeautifulSoup as bs
import random,os,time



def pr():
	print('Refreshing Proxy\033[0m')
	r = get('https://www.proxy-list.download/api/v1/get?type=https').text
	return r.split()
def crawler():
	n = int(input('UserAgent amounts to collect: '))
	prokk = pr()
	prok = random.choice(prokk)
	print(f'Connecting to proxy: {prok}\033[0m')
	userA = []
	try:
			r = get('https://developers.whatismybrowser.com/useragents/explore/',proxies={'https':'https://'+prok}).text
			print(f'Connected, crawling https://developers.whatismybrowser.com\033[0m')
			b = bs(r,'html.parser')
			
		
			for i in b.find('ul',{'id':'listing-by-field-name'}).find_all('ul'):
				if len(userA) == n:
					break
				else:
					for a in i.find_all('a'):
						if len(userA) == n:
							break
						else:
							url = 'https://developers.whatismybrowser.com'+a.get('href')
							rr = get(url,proxies={'https':'https://'+prok}).text
							bb = bs(rr,'html.parser')
							for ua in bb.find_all('td',{'class','useragent'}):
								if len(userA) == n:
									break
								else:
									userA.append(ua.text)
									print('\rCollecting : ',len(userA),end='',flush=True)
									time.sleep(0.01)
	except KeyboardInterrupt:
		pass
	except exceptions.ProxyError or exceptions.SSLError:
		print('\033[91mProxy error, please restart to refresh with other proxy\033[0m')
	
	if len(userA) != 0:
		f = open('useragents.txt','w')
		for ua in userA:
			f.write(ua+'\n')
		print(f'\n\033[92mFinished. {len(userA)} useragents saved to useragents.txt\033[0m')
	
if __name__=='__main__':
	os.system('clear')
	print('''\033[92m

  __  __            ___                __ 
 / / / /__ ___ ____/ _ |___ ____ ___  / /_ \033[0mKarjok Pangesty\033[92m
/ /_/ (_-</ -_) __/ __ / _ `/ -_) _ \/ __/ \033[0m@CRABS_ID\033[92m
\____/___/\__/_/ /_/ |_\_, /\__/_//_/\__/  \033[0m© 2019\033[92m
                      /___/ \033[93mGenerator\033[0m
---------------------------------------------------------
''')
	crawler()