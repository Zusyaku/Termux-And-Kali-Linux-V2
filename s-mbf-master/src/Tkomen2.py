#Python 3.7.X
#Author: KANG-NEWBIE ©2019
import requests,os,sys
from src import Genkuki
from bs4 import BeautifulSoup as BS
from multiprocessing.pool import ThreadPool

class Tkomnew:
	def __init__(self):
		self.c=1
		self.link=[]
		self.req=requests.Session()
		self.u='https://mbasic.facebook.com{}'
		self.banner()

	def banner(self):
		print("""
	;;;;;;;;;;;;;;;;;;;;;
	; Comment Target v2 ;
	;  By KANG-NEWBIE   ;
	;;;;;;;;;;;;;;;;;;;;;""")
		Genkuki.login(self)
		self.rl='/'+input('[?] Target id: ')+'?v=timeline'
		self.ig=int(input('[?] How many posts do you want to get: '))
		self.getlnk(self.rl)

	def getlnk(self,lnk):
		bs=BS(self.req.get(self.u.format(lnk)).text,'html.parser')
		for a in bs.find_all('a'):
			if len(self.link) == self.ig:
				break
			if 'Komentar' in a.text:
				self.link.append(a.get('href'))
			print(f'\r[{len(self.link)}] get {self.ig} posts link...',end='');sys.stdout.flush()
			if 'Lihat Berita Lain' in a.text:
				self.getlnk(a.get('href'))
		print()
		self.tgl()
		exit()

	def tgl(self):
		linkt=[]
		self.ct=1
		if len(self.link) != self.ig:
			print(f'[!] Only got {len(self.link)} posting links')
		def tang(lik):
			d=[]
			bs1=BS(self.req.get(self.u.format(lik)).text,'html.parser')
			sts=bs1.find("title").renderContents().decode("utf-8", "ignore")
			for p in bs1.find_all('abbr'):
				d.append(p.text)
			print(f'[\033[93m{self.c}\033[0m] {sts[:30]} \n\033[92m<date>\033[0m ({d[0]})')
			print('=====================================')
			self.c+=1

		print("""
1. coment all post
2. coment target post
""")
		pil=int(input('[?] kang_newbie/> '))
		print()
		if pil == 2:
			for li in self.link:
				tang(li)
			self.pilt=int(input('\n[?] choice: '))
			ms=input('[info] type \'<n>\' for newlines\n[?] comment: ')
			lop=int(input('[?] looping: '))
			self.msg=ms.replace('<n>','\n')
			linkt.append(self.link[self.pilt-1])
			for i in range(lop):
				ThreadPool(10).map(self.komen,linkt)
		elif pil == 1:
			ms=input('[info] type \'<n>\' for newlines\n[?] comment: ')
			self.msg=ms.replace('<n>','\n')
			ThreadPool(10).map(self.komen,self.link)

	def komen(self,url):
		data=[]
		bs2=BS(self.req.get(self.u.format(url)).text,'html.parser')
		for x in bs2('form'):
			data.append(self.u.format(x['action']))
		for xi in bs2('input'):
			try:
				if "fb_dtsg" in xi["name"]:
					data.append(xi["value"])
				if "jazoest" in xi["name"]:
					data.append(xi["value"])
					break
			except: continue
		if len(data) == 4:
			sub=self.req.post(data[0],data={"fb_dtsg":data[2],"jazoest":data[3],"comment_text":self.msg}).status_code
			if sub == 200:
				print(f'[{self.ct}] Success commented')
			else:
				print(f'[{self.ct}] Fail commented')
			self.ct+=1
		else:
			print(f'[{self.ct}] Fail commented')
			self.ct+=1

try:
	Tkomnew()
except Exception as F:
	print(f'Err: {F}')