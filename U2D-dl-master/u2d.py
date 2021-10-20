import requests,os,sys,time,click,random
from bs4 import BeautifulSoup as BS

class U2D:
	def __init__(self):
		self.req=requests.Session()
		self.app=[]
		self.dev=[]
		self.url=[]
		self.banner()

	def banner(self):
		os.system('clear')
		ran=random.randint(0,7)
		print(f"""\033[96m
             ....             
           ..    ..           
 \033[9{ran}mUP2DOWN\033[96m  -        -    \033[9{ran}mKANG-NEWBIE\033[96m
\033[9{ran}mDOWNLOADER\033[96m .`    `.  \033[9{ran}m(t.me/kang_nuubi)\033[96m
             .``.             
   ----      ----      ----   
 --    --  --    --  --    -- 
:   UP   //   TO   //  DOWN  :
 .`    -ohho-    -ohho-    `. 
   .`-ohhhhhho--ohhhhhho-`.   
     :shhhhhhsssshhhhhhs:     
       :shhsshhhysshhs:       
         -ohhhhhhhho-         
           -shhhhs-           
             -ss-             \033[97m""")
		self.grep()

	def grep(self):
		plat=input("\n\tPLATFORM\n1. Android\t2. Windows\n3. Ubuntu\t4. Mac\n\n[?] pilih platform: ")
		if plat == '1':
			p='android'
			self.ex='.apk'
		elif plat == '2':
			p='windows'
			self.ex='.exe'
		elif plat == '3':
			p='ubuntu'
			self.ex='.deb'
		elif plat == '4':
			p='mac'
			self.ex='.dmg'
		else: exit("[!] moonton bercanda?")
		q=input("[?] query: ").replace(' ','%20')
		r=self.req.get('https://id.uptodown.com/'+p+'/search/'+q).text
		bs=BS(r,'html.parser')
		for a in bs.find_all('p'):
			try:
				url=a.find('a')['href']
				app=a.text.strip()
				self.app.append(app)
				self.url.append(url)
			except: pass
		de=bs.find_all('span',{'class':'app_card_system'})
		for d in de:
			self.dev.append(d.text.strip())
		print()
		self.show()

	def show(self):
		c=0
		if len(self.app) == 0:
			exit("[!] Aplikasi yang anda cari tidak tersedia")
		for x in self.app[0:16]:
			try:
				print(f"""NUM [{c+1}]
APP: {x}
DEV: {self.dev[c]}
{'+='*20}""")
				c+=1
			except: continue
#		print(self.app[0:16])
		self.pil=int(input("\n[?] pilih no: "))
		url=self.url[self.pil-1]
		self.dl(url)

	def dl(self,url):
		head={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36 OPR/56.0.3051.52'}
		r=self.req.get(url+'/download').text
		bs2=BS(r,'html.parser')
		rl=bs2.find('a',{'class':'data download'}).get('href')
		size=bs2.find('p',{'class':'size'}).text.strip()
		print(f"[Downloading]: {self.app[self.pil-1]}\nUkuran: {size}")
		with open(self.app[self.pil-1].replace(' ','')+self.ex,'wb') as f:
			response=requests.get(rl,stream=True,headers=head)
			total_length=response.headers.get('content-length')
			if total_length is None:
				try:
					os.remove(self.app[self.pil-1].replace(' ','')+self.ex)
				except: pass
				print("[Err] Failed download app")
				tan=input("[?] anda ingin melanjutkannya ke website uptodown.com (y/n) ")
				if tan.lower() == 'y':
					click.launch(self.url[self.pil-1])
				else:
					exit("okay bye bye:*")
			else:
				dlw=0
				total_length=int(total_length)
				for data in response.iter_content(chunk_size=4096):
					ges=int(100*dlw/total_length)
					dlw+=len(data)
					f.write(data)
					done=int(30*dlw/total_length)
					print(f"\r\033[97m[\033[92m{'>'*done}\033[91m{'='*(30-done)}\033[97m] \033[96m{ges+1}% ",end='')
					sys.stdout.flush()
		print(f"\n\033[97m[DONE] sukses mendownload {self.app[self.pil-1].replace(' ','')}{self.ex}")

try:
	U2D()
	while True:
		plh=input("\033[0m\n[?] coba lagi (y/n) ")
		if plh.lower() == 'y':
			U2D()
		elif plh.lower() == 'n':
			exit('sampai jumpa lagi...')
except KeyboardInterrupt:
	print("\n[!] Key interrupt")
except Exception as EF:
	print(f"Err: {EF}")
