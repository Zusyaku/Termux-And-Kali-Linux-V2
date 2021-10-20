#Python 3.7.X
#Author: KANG-NEWBIE ©2019

import requests,os,sys,time
from bs4 import BeautifulSoup as BS
from multiprocessing.pool import ThreadPool
from src import Genkuki

class DownFotomsg:
	def __init__(self):
		self.link=[]
		self.req=requests.Session()
		self.u='https://mbasic.facebook.com{}'
		self.banner()

	def banner(self):
		print("""
	;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
	; Download all Messages Image ;
	;       By KANG-NEWBIE        ;
	;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;""")
		Genkuki.login(self)
		try:
			pid=int(input('[?] Target id: '))
		except ValueError:
			exit('[!] id must be integer')
		print("[!] Please wait...")
		self.getlnk(self.u.format('/messages/read/?tid='+str(pid)))

	def getlnk(self,lnk):
		bs=BS(self.req.get(lnk).text,'html.parser')
		for img in bs.find_all('img'):
			if 'alt' in str(img) or 'static.xx.fbcdn.net' in img['src']:
				continue
			else:
				self.link.append(img['src'])
		print(f"\r[{len(self.link)}] get photo links...",end="");sys.stdout.flush()
		for a in bs.find_all('a'):
			if 'Lihat Pesan Sebelumnya' in a.text:
				self.getlnk(self.u.format(a['href']))
		self.tes()
	
	def tes(self):
		self.cou=0
		self.fail=0
		try:
			os.mkdir('result')
		except: pass
		try:
			os.mkdir('result/msgphoto')
		except: pass
		self.sfile=input('\n\n[?] file output: ')
		ThreadPool(5).map(self.dlw,self.link)
		exit('\n\n[!] Files save as: result/msgphoto/*.png')

	def dlw(self,l):
		poto=self.req.get(l)
		if poto.status_code == 200:
			with open(f"result/msgphoto/{self.sfile}_{self.cou}.png","wb") as sv:
				sv.write(poto.content)
			self.cou+=1
		else:
			self.fail+=1
		print(f"\r[{self.cou}] Downloading image... failed[{self.fail}]",end="");sys.stdout.flush()

try:
	DownFotomsg()
except Exception as F:
	print(f"Err: {F}")