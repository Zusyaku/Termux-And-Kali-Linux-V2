#Python 3.7.X
#Author: KANG-NEWBIE ©2019
#Special thanks to LOoLzeC (Deray)

import requests,time,os,click,sys
from bs4 import BeautifulSoup as BS
from getpass import getpass
from multiprocessing.pool import ThreadPool
from src import Genkuki

class Del:
	def __init__(self):
		self.rl=[]
		self.req=requests.Session()
		self.ken=open('toket/token.txt','r').read()
		self.u='https://mbasic.facebook.com{}'
		print("""
	;;;;;;;;;;;;;;;;;;;;;;;
	; Delete all Messages ;
	;    By KANG-NEWBIE   ;
	;;;;;;;;;;;;;;;;;;;;;;;""")
		self.gnam()


	def gnam(self):
		Genkuki.login(self)
		rm=self.req.get(self.u.format('/me')).text
		bs2=BS(rm,'html.parser')
		for x in bs2.find_all('a',string='Log Aktivitas'):
			self.me=x.get('href').replace('/','').replace('allactivity?refid=17','')
		self.gid(self.u.format('/messages'))

	def gid(self,lnk):
		rg=self.req.get(lnk).text
		bs1=BS(rg,'html.parser')
		for ai in bs1.find_all('h3'):
			p=ai.find('a')
			if '/messages/read/?' in str(p):
				try:
					self.rl.append(self.u.format(p['href']))
					print(f'\r[{len(self.rl)}] getting messages. please wait...',end='');sys.stdout.flush()
				except: pass
		for n in bs1.find_all('a',string='Lihat Pesan Sebelumnya'):
			nxt=self.u.format(n.get('href'))
			self.gid(nxt)
		print()
		click.pause()
		self.main()
		exit('[D O N E]')

	def main(self):
		links=[]
		for li in self.rl:
			links.append(li)
		t=ThreadPool(10)
		t.map(self.dell,links)

	def dell(self,l):
		data=[]
		bs=BS(self.req.get(l).text,"html.parser")
		nama=bs.find("title").renderContents().decode("utf-8", "ignore")
		for x in bs("form"):
			if "action_redirect" in x["action"]:
				data.append(x["action"])
				
		for x in bs("input"):
			try:
				if "fb_dtsg" in x["name"]:
					data.append(x["value"])
				if "jazoest" in x["name"]:
					data.append(x["value"])
				if "delete" in x["name"]:
					data.append(x["value"])
					break
			except: pass

		bs3=BS(self.req.post(self.u.format(data[0]),data={"fb_dtsg":data[1],"jazoest":data[2],"delete":data[3]}).text,"html.parser")
		for a in bs3.find_all('a',string='Hapus'):
			rr=self.req.get(self.u.format(a.get('href'))).status_code
			if rr == 200:
				print(f"[success] deleted messages - {nama} ({l.replace('https://mbasic.facebook.com/messages/read/?tid=cid.c.','').replace('https://mbasic.facebook.com/messages/read/?tid=cid.g.','').replace(self.me,'').replace('%3A','').replace('&refid=11#fua','')})")
			else:
				print(f"[failed] deleted messages - {nama} ({l.replace('https://mbasic.facebook.com/messages/read/?tid=cid.c.','').replace('https://mbasic.facebook.com/messages/read/?tid=cid.g.','').replace(self.me,'').replace('%3A','').replace('&refid=11#fua','')})")
try:
	Del()
except Exception as E:
	print(f'Err: {E}')