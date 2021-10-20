import requests, os, json
from time import sleep as slp





bl = '\033[30m'
lb = '\033[94m'
lc = '\033[96m'
lr = '\033[91m'
lg = '\033[92m'
a  = '\033[93m'
b  = '\033[90m'
x  = '\033[0m'


"""
GW LDR 4 TAHUN, DAN BELOM PERNAH KETEMU.
YANG MAKEK TOOL INI, DOAIN GW YA ?
MOGA CEPET KETEMU :*


"""

try:
      import requests
except ImportError:
      print(lr+"Modul requests belum terinstall.")
      ins= input(lg+"Install sekarang ? (y/n) : ")
      if ins == 'y':
            try:
                  os.system('pip3 install requests')
                  home()
            except:
                  print(lr+"Cek jaringan !"+x)
                  exit()
      else:
            print(lc+"[✓]Successfully Exiting !"+x)
            exit()
try:
      os.system("rm -rf id")
      os.system("mkdir id")

except:
      pass
      
def grup():
      global token 
      print (lc+'\nTUNGGU SEBENTAR EA :*'+x) 
      print (lc+'**********************************'+x)
      try:
            r = requests.get('https://graph.facebook.com/me/groups?access_token='+token)
      except:
            print (lr+'Masalah pada Jaringan/Token !'+x)
            print (a+'Tips: Nyalakan data internet \ndan cek token kembali.\n'+x)
            input(lg+'Press enter to back to menu'+x)
            home()
      result = json.loads(r.text)
      a = open('id/id.txt','w')
      try:
            for grup in result['data']:
                  a.write('Nama : '+grup['name']+'\nID   : '+grup['id']+'\n\n')
                  slp(0.05)
                  print (lc+'Nama = '+x,grup['name'],lc+'\nID   = '+x,grup['id'])
                  print (lc+'**********************************'+x)
      except KeyError:
            print(lr+'Masalah pada token !'+x)
            input(lb+'Press enter to back to menu'+x)
      a.close()
      input(lb+'Press enter to back to menu'+x)
      return token
                        
def home():
      global token
      
      header()
      inn= input(lc+'SHARE'+x+'id/'+lc+'> '+x)
      while inn != '1' and inn != '2' and inn != '3' and inn != '0':
            print (lr+'Input salah !'+x)
            inn= input(lc+'SHAREid/> '+x)
      if inn == '1':
            print (b+"Tips: Gunakan OSIF untuk mendapatkan token."+x)
            token = input(lc+"Masukkan token : "+x+bl)
            while token == "":
                  print(lr+"Token harus di isi !"+x)
                  token = input(lc+"Masukkan token : "+x+bl)
            
            grup()
            home()
      elif inn == '2':
            try:
                  cat = open('id/id.txt').read()
                  print (lg+'\nHasil Dump ID Grup:\n\n'+lc+cat)
                  input(lb+'Press enter to back to menu'+x)
                  home()
            except IOError:
                  print (lr+"\nBelum ada ID tersimpan.\nSilahkan pilih 'Mulai' untuk membuat list ID\n"+x)
                  input(lb+'Press enter to back to menu'+x)
                  home()
      elif inn == '3':
            print (x+"""
Nama      : SHAREid
Versi     : 1.0
Date      : November 5th, 2018 3:17:30 WIB 
Author    : Karjok Pangesy
Code      : KJ4
Grup      : CRABs ID
Lisensi   : Gratis
Thanks to : Allah SWT, My Agustinna Pangesty,
            mas Khanif Ihsanudin,
            dan bully-an all member Termux Indonesia :')
More      : Tool ini sengaja dibuat untuk mempermudah
            para pengguna tool MBF milik bang @pirmansx.
            Yang mana pada tool tersebut
            ada fitur 'Ambil ID dari Grup'
            dan untuk menjalankannya
            perlu ID grup tertentu.
            Dengan tool ini,
            bisa dengan mudah mendapat ID grup.
            Permasalahnannya adalah
            kenewbian Author yang belum
            bisa membuat generator token sendiri,
            sehingha masih
            membutuhkan tool OSIF
            milik @Ciku370 untuk mendapat tokennya.
                        
* Masih banyak error yang terjadi.          
* Silahkan bully saya ke https://t.me/@om_karjok
* Sejelek apapun tool ini, tolong jangan di recode.
            """)
            input(lb+'Press enter to back to menu'+x)
            home()
      else:
            print (lc+'[✓] Exiting Successfully :*'+x)
            exit()
      return token
            
def header():
      os.system('clear')
      print(lc+"              \)/ "+lc+".-. ")      
      print(lc+"              /, "+lc+"("+x+"^,^"+lc+")")   
      print(lc+"             ()   "+lc+"("+lr+"*"+lc+")"+lg+"   'Ini adalah tool")
      print(lc+"       /_ ___  \\, =',",lg+"   yang sama sekali")
      print(lc+"       '-()-()   =/=\\    "+lg+"tidak berfaedah' ")   
      print(lc+"         //\\||  ==== () ")  
      print(lc+"        /`  \\|  ='=  `| "+lr+"-Karjok Pangesty-")
      print(lc+"      =='    `"+lr+"("+x+"KJ4"+lr+")"+lc+"   '--"+x)
      print(lr+"      ==================================="+x)
      print(lc+"        SHARE"+x+"id"+lr+" v1.0"+a+" by: Si Otak Udank")
      print(lr+"      ==================================="+x)
      print(lc+"""
      1. Mulai
      2. Lihat Hasil Sebelumnya
      3. Tentang
      0. Exit\n\n""")


      
      
home()      
