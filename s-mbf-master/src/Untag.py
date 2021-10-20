#Python 3.7.X
#Author: KANG-NEWBIE ©2019

import sys,requests
from bs4 import BeautifulSoup as BS
from src import Genkuki
from multiprocessing.pool import ThreadPool

class Untag:
	def __init__(self):
		self.link=[]
		self.req=requests.Session()
		self.u='https://mbasic.facebook.com{}'
		self.banner()

	def banner(self):
		print("""
	;;;;;;;;;;;;;;;;;;;
	; Auto UNTAG Post ;
	; By KANG-NEWBIE  ;
	;;;;;;;;;;;;;;;;;;;""")
		Genkuki.login(self)
		self.getlnk(self.u.format('/me'))

	def getlnk(self,lnk):
		bs=BS(self.req.get(lnk).text,'html.parser')
		nama=bs.find("title").renderContents().decode("utf-8", "ignore")
		for a in bs.find_all('a'):
			if 'Lainnya' in a.text:
				self.link.append(a['href'])
			print("\r[!] Please wait...",end='');sys.stdout.flush()
			if 'Lihat Berita Lain' in a.text:
				self.getlnk(self.u.format(a['href']))
		self.thread()

	def thread(self):
		ThreadPool(int(input('\n[?] Threads: '))).map(self.untag,self.link)
		print("[D O N E]")
		exit()

	def untag(self,url):
		tag=[]
		data=[]
		bs2=BS(self.req.get(self.u.format(url)).text,'html.parser')
		for a in bs2.find_all('a'):
			tag.append(a.text)
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
		if len(data) == 3:
			sub=self.req.post(data[0],data={"fb_dtsg":data[1],"jazoest":data[2],"action_key":"UNTAG"}).text
			if 'Selesai' in sub:
				print(f"[!] success UNTAG >> {tag[9]}")

Untag()