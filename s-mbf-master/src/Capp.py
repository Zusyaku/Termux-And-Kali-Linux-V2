import os,time,sys,requests,re
from bs4 import BeautifulSoup as BS

class App:
	def __init__(self,id,pas):
		self.id=id
		self.pas=pas
		self.url='https://mbasic.facebook.com/{}'
		self.req=requests.Session()

	def login(self):
		link=self.url.format('login')
		data={'email':self.id,'pass':self.pas}
		res = self.req.post(link,data=data).text
		if 'logout.php' in str(res) or 'mbasic_logout_button' in str(res):
			self.cekapp()
		else:
			print(f'[!!] {self.id}|{self.pas} FAILED LOGIN')

	def cekapp(self):
		page=self.url.format('settings/apps/tabbed/')
		bs=BS(self.req.get(page).text,features="html.parser")
		for x in bs.find_all("h3"):
			p=x.find("div")
			if "None" in str(p):
				continue
			else:
				print("-",p.text)

try:
	print("""
	;;;;;;;;;;;;;
	; CHECK APP ;
	;;;;;;;;;;;;;""")
	print("\n[INFO] List sparator 'email|pass'")
	inp=input("[+] list account: ")
	file=open(inp,'r').read().splitlines()
	for x in file:
		p=x.split('|')
		id=p[0]
		pas=p[1]
		print("\n[!] Check APP on account [ "+str(id)+"|"+str(pas)+" ]")
		cek=App(id,pas)
		cek.login()
except Exception as F:
	print("Err: %s"%(F))
