import requests,os,sys,re
import subprocess
from time import sleep
from colorama import Fore
from datetime import datetime
s=requests.Session()

mnb=Fore.BLUE
mxanh=Fore.GREEN
mdo=Fore.RED
mtrang=Fore.WHITE
mvang=Fore.YELLOW
os.system("clear")
os.system("clear")


delay=mxanh+"""        
                      \033[1;31mYTB: \033[1;33mVΔn PhΖ°Ζ‘ng Tricker π
                 \033[1;92mβββββ βββββ βββββ ββββββ ββββββ βββββ  
                 \033[1;92mβββββ βββββ βββββ ββββββ ββββββ βββββ  
                 \033[1;92mβββββ βββββ βββββ ββββββ ββββββ βββββ  """

for c in delay:
  sys.stdout.write(c)
  sys.stdout.flush()
  sleep(0.003)
print('\r')
print('\r')
print(mvang+"                          Tool Buff Like TΓ’y")
print(mtrang+"                           MACHINE-LIKER")
print('\r')                     
print(mtrang+"\033[1;32m[\033[1;31mβ\033[1;32m]\033[1;33mβBαΊ£n quyα»n tool: \033[1;92mVΔn PhΖ°Ζ‘ng Tricker nhΖ°ng code gα»c cα»§a TΓ΄n lΓΉ")
print('\r')             
print(mxanh+f"\033[1;32m[\033[1;31mβ\033[1;32m]NhΓ³m Zalo Hα» Trα»£ ChαΊ‘y {mtrang}Tool + Share{mxanh} All Tool Free")
print('\r')              
print(mdo+f"\033[1;32m[\033[1;31mβ\033[1;32m]{mvang}[{mdo}https://zalo.me/g/ayfulb045{mvang}]")
print('\r')
print(mxanh+f"\033[1;32m[\033[1;31mβ\033[1;32m]Tool FREEE - CαΊ₯m {mtrang}Mua / BΓ‘n {mxanh}DΖ°α»i Mα»i HΓ¬nh Thα»©c")




os.system("clear")
delay=mxanh+"""        

                 \033[1;31mYTB: \033[1;33mVΔn PhΖ°Ζ‘ng Tricker π
                 \033[1;92mβββββ βββββ βββββ ββββββ ββββββ βββββ  
                 \033[1;92mβββββ βββββ βββββ ββββββ ββββββ βββββ  
                 \033[1;92mβββββ βββββ βββββ ββββββ ββββββ βββββ  """

for c in delay:
  sys.stdout.write(c)
  sys.stdout.flush()
  sleep(0)
print('\r')
print('\r')
print(mvang+"                          Tool Buff Like TΓ’y")
print(mtrang+"                           MACHINE-LIKER")
print('\r')                     
print(mtrang+"\033[1;32m[\033[1;31mβ\033[1;32m]\033[1;33mβBαΊ£n quyα»n tool: \033[1;92mVΔn PhΖ°Ζ‘ng Tricker nhΖ°ng code gα»c cα»§a TΓ΄n lΓΉ")
print('\r')             
print(mxanh+f"\033[1;32m[\033[1;31mβ\033[1;32m]NhΓ³m Zalo Hα» Trα»£ ChαΊ‘y {mtrang}Tool + Share{mxanh} All Tool Free")
print('\r')              
print(mdo+f"\033[1;32m[\033[1;31mβ\033[1;32m]{mvang}[{mdo}https://zalo.me/g/ayfulb045{mvang}]")
print('\r')
print(mvang+"=============================================================")
print('\r')

try:
  moa=open("user-agen.txt","r")
  user=moa.read()
  moa.close()
except:
  mo=open("user-agen.txt","a+")
  mo=open("user-agen.txt","r+")
  while True:
    userr=input(mxanh+f"NhαΊ­p {mvang}User-agen {mvang}(LαΊ₯y tαΊ‘i {mdo}http://whatsmyuseragent.org {mvang})"+mtrang)
    if "Mozilla" not in userr:
      os.system("clear")
      print(mdo+"Sai Δα»nh DαΊ‘ng User-Agen")
    else:
      mo.write(userr)
      mo.close()
      mo1=open("user-agen.txt","r")
      user=mo1.read()
      mo1.close()
      break
os.system("clear")
delay=mxanh+"""        

                 \033[1;31mYTB: \033[1;33mVΔn PhΖ°Ζ‘ng Tricker π
                 \033[1;92mβββββ βββββ βββββ ββββββ ββββββ βββββ  
                 \033[1;92mβββββ βββββ βββββ ββββββ ββββββ βββββ  
                 \033[1;92mβββββ βββββ βββββ ββββββ ββββββ βββββ  """

for c in delay:
  sys.stdout.write(c)
  sys.stdout.flush()
  sleep(0)
print('\r')
print('\r')
print(mvang+"                          Tool Buff Like TΓ’y")
print(mtrang+"                           MACHINE-LIKER")
print('\r')                     
print(mtrang+"\033[1;32m[\033[1;31mβ\033[1;32m]\033[1;33mβBαΊ£n quyα»n tool: \033[1;92mVΔn PhΖ°Ζ‘ng Tricker nhΖ°ng code gα»c cα»§a TΓ΄n lΓΉ")
print('\r')             
print(mxanh+f"\033[1;32m[\033[1;31mβ\033[1;32m]NhΓ³m Zalo Hα» Trα»£ ChαΊ‘y {mtrang}Tool + Share{mxanh} All Tool Free")
print('\r')              
print(mdo+f"\033[1;32m[\033[1;31mβ\033[1;32m]{mvang}[{mdo}https://zalo.me/g/ayfulb045{mvang}]")
print('\r')
print(mdo+f"Admin setup time dΖ° 10s trΓ‘nh lα»i nhΓ©! wf")
print('\r')
print(mvang+"=============================================================")
print('\r')

def rundelay(k):
  while (k>0):
    
    print('                                        ', end='\r')
    print(mxanh+'π Phuongsaid '+mvang+'Vui lΓ²ng chα» '  + mtrang+str(k) +mxanh+' giΓ’y', end='\r')
    sleep(1)
    k=k-1
    
    
    
while True:
  ck=input(mxanh+f"\033[1;32m[\033[1;31mβ\033[1;32m]NhαΊ­p Cookie {mvang}Machine liker {mxanh}=>" + mtrang)
  os.system("clear")

  hd={
    "Host":"www.machine-liker.com",
    "x-requested-with":"XMLHttpRequest",
    "user-agent":user,
    "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
    "cookie":ck
  
  }
  check=s.get("https://www.machine-liker.com/dashboard/",headers=hd)
  if "User ID" not in check.text:
    os.system("clear")
    print(mdo+"Cookie Die - Vui LΓ²ng Kiα»m Tra User-Agen hoαΊ·c xoΓ‘ file user-agen.txt cΕ© Δi, sau ΔΓ³ vΓ o lαΊ‘i tool nhαΊ­p lαΊ‘i nhaπΈ")
  else:
    break

delay=mxanh+"""        

                 \033[1;31mYTB: \033[1;33mVΔn PhΖ°Ζ‘ng Tricker π
                 \033[1;92mβββββ βββββ βββββ ββββββ ββββββ βββββ  
                 \033[1;92mβββββ βββββ βββββ ββββββ ββββββ βββββ  
                 \033[1;92mβββββ βββββ βββββ ββββββ ββββββ βββββ  """

for c in delay:
  sys.stdout.write(c)
  sys.stdout.flush()
  sleep(0)
print('\r')
print('\r')
print(mvang+"                          Tool Buff Like TΓ’y")
print(mtrang+"                           MACHINE-LIKER")
print('\r')                     
print(mtrang+"\033[1;32m[\033[1;31mβ\033[1;32m]\033[1;33mβBαΊ£n quyα»n tool: \033[1;92mVΔn PhΖ°Ζ‘ng Tricker nhΖ°ng code gα»c cα»§a TΓ΄n lΓΉ")
print('\r')             
print(mxanh+f"\033[1;32m[\033[1;31mβ\033[1;32m]NhΓ³m Zalo Hα» Trα»£ ChαΊ‘y {mtrang}Tool + Share{mxanh} All Tool Free")
print('\r')              
print(mdo+f"\033[1;32m[\033[1;31mβ\033[1;32m]{mvang}[{mdo}https://zalo.me/g/ayfulb045{mvang}]")
print(mvang+"=============================================================")
linkbv=input(mxanh+f"\033[1;32m[\033[1;31mβ\033[1;32m]NhαΊ­p Link {mvang}CαΊ§n Buff CαΊ£m XΓΊc (lαΊ₯y link trα»±c tiαΊΏp bαΊ±ng app Facebook hoαΊ·c chrome {mxanh}=>"+mtrang)
os.system("clear")
delay=mxanh+"""        

                 \033[1;31mYTB: \033[1;33mVΔn PhΖ°Ζ‘ng Tricker π
                 \033[1;92mβββββ βββββ βββββ ββββββ ββββββ βββββ  
                 \033[1;92mβββββ βββββ βββββ ββββββ ββββββ βββββ  
                 \033[1;92mβββββ βββββ βββββ ββββββ ββββββ βββββ  """

for c in delay:
  sys.stdout.write(c)
  sys.stdout.flush()
  sleep(0)
print('\r')
print('\r')
print(mvang+"                          Tool Buff Like TΓ’y")
print(mtrang+"                           MACHINE-LIKER")
print('\r')                     
print(mtrang+"\033[1;32m[\033[1;31mβ\033[1;32m]\033[1;33mβBαΊ£n quyα»n tool: \033[1;92mVΔn PhΖ°Ζ‘ng Tricker nhΖ°ng code gα»c cα»§a TΓ΄n lΓΉ")
print('\r')             
print(mxanh+f"\033[1;32m[\033[1;31mβ\033[1;32m]NhΓ³m Zalo Hα» Trα»£ ChαΊ‘y {mtrang}Tool + Share{mxanh} All Tool Free")
print('\r')              
print(mdo+f"\033[1;32m[\033[1;31mβ\033[1;32m]{mvang}[{mdo}https://zalo.me/g/ayfulb045{mvang}]")
print(mvang+"=============================================================")
print(mvang+"\033[1;32m[\033[1;31mβ\033[1;32m]Chα»n cαΊ£m xΓΊc cαΊ§n buff");print(mdo+f"VΓ­ Dα»₯ Chα»n {mvang}Like,Wow,Haha {mdo}chα»n {mtrang}1,3,4 nhΓ©!!!!")
print(mvang+"[1].",mxanh+" \033[1;32m[\033[1;31mβ\033[1;32m]Likeπ")
print(mvang+"[2].",mxanh+" \033[1;32m[\033[1;31mβ\033[1;32m]YΓͺu ThΓ­chβ€οΈ")
print(mvang+"[3].",mxanh+" \033[1;32m[\033[1;31mβ\033[1;32m]Wowπ³")
print(mvang+"[4].",mxanh+" \033[1;32m[\033[1;31mβ\033[1;32m]Hahaπ")
print(mvang+"[5].",mxanh+" \033[1;32m[\033[1;31mβ\033[1;32m]Buα»nπ’")
print(mvang+"[6].",mxanh+" \033[1;32m[\033[1;31mβ\033[1;32m]PhαΊ«n Nα»π ")
print(mvang+"[7].",mxanh+" \033[1;32m[\033[1;31mβ\033[1;32m]ThΖ°Ζ‘ng ThΖ°Ζ‘ngπ₯°")
print(mvang+"[all].",mxanh+"\033[1;32m[\033[1;31mβ\033[1;32m]TαΊ₯t CαΊ£π―")
print(mvang+"=============================================================")
cx=input(mxanh+"\033[1;32m[\033[1;31mβ\033[1;32m]NhαΊ­p LoαΊ‘i CαΊ£m XΓΊc \033[1;93m=> "+mvang)
if cx=="all":
  cx="1,2,3,4,5,6,7"
os.system("clear")
delay=mxanh+"""        

                 \033[1;31mYTB: \033[1;33mVΔn PhΖ°Ζ‘ng Tricker π
                 \033[1;92mβββββ βββββ βββββ ββββββ ββββββ βββββ  
                 \033[1;92mβββββ βββββ βββββ ββββββ ββββββ βββββ  
                 \033[1;92mβββββ βββββ βββββ ββββββ ββββββ βββββ  """

for c in delay:
  sys.stdout.write(c)
  sys.stdout.flush()
  sleep(0)
print('\r')
print('\r')
print(mvang+"                          Tool Buff Like TΓ’y")
print(mtrang+"                           MACHINE-LIKER")
print('\r')                     
print(mtrang+"\033[1;32m[\033[1;31mβ\033[1;32m]\033[1;33mβBαΊ£n quyα»n tool: \033[1;92mVΔn PhΖ°Ζ‘ng Tricker nhΖ°ng code gα»c cα»§a TΓ΄n lΓΉ")
print('\r')             
print(mxanh+f"\033[1;32m[\033[1;31mβ\033[1;32m]NhΓ³m Zalo Hα» Trα»£ ChαΊ‘y {mtrang}Tool + Share{mxanh} All Tool Free")
print('\r')              
print(mdo+f"\033[1;32m[\033[1;31mβ\033[1;32m]{mvang}[{mdo}https://zalo.me/g/ayfulb045{mvang}]")
print('\r')
print(mvang+"=============================================================")
print('\r')


hd={
  "Host":"www.machine-liker.com",
  "x-requested-with":"XMLHttpRequest",
  "user-agent":user,
  "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
  "cookie":ck
  
  }
data={

  "url":linkbv
}
stt=0
while True:
  try:
	
    a=s.post("https://www.machine-liker.com/api/get-post-info/",data=data,headers=hd,allow_redirects=False,timeout=30)
  
    if 'The post is either invalid or not public, please check and try again' in a.text:
      os.system("clear")
      print(mdo+"Vui LΓ²ng BαΊ­t CΓ΄ng Khai BΓ i ViαΊΏt")
      waint=input(f"{mvang}CTRT + z {mtrang}Δα» Dα»«ng Tool - BαΊ­t {mdo}CΓ΄ng Khai BΓ i ViαΊΏt {mtrang}VΓ  ChαΊ‘y LαΊ‘i Tool")

    try:
      id=a.json()["post"]["id"]
      story=a.json()["post"]["story"]
    except:
      os.system("clear")
      print(mdo+"Cookie DIE")
      waint=input(f"{mvang}CTRT + z {mtrang}Δα» Dα»«ng Tool - LαΊ₯y LαΊ‘i {mdo}Cookie Machine Liker {mtrang} VΓ  ChαΊ‘y LαΊ‘i Tool")

    link=s.get(f"https://www.machine-liker.com/send-reactions/?post_id={id}&story={story}",headers=hd)


    obj=link.text.split('name="object_id" value="')[1].split('"')[0]

    datab={
      "object_id":obj,

      "reactions":cx,

      "limit":"100"

}
    b=s.post("https://www.machine-liker.com/api/send-reactions/",data=datab,headers=hd)
  
    if "successfully" in b.text:
    
      print('',end="\r")
      so=b.text.split('message": "')[1].split(' reactions')[0]
      stt = stt+1
      tg=datetime.now().strftime('%H:%M')
      print(mvang+"["+str(stt)+"]",mdo+"β’",mtrang+"PhΖ°Ζ‘ngβ’Tool",mdo+"β’",mnb+str(tg ),mdo+"β’",mxanh+f"Cα»ng  {so} Like ",mdo+"β’", +mtrang+" Tα»ng like tα»± ΔαΊΏm nha =))")
      
      print("\r")
    else:
    

      k=600
      rundelay(k)
      
      
  except:
    sleep(10)
