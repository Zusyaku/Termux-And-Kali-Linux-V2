import os,sys,time,requests,json
from bs4 import BeautifulSoup as bs
from time import sleep
from concurrent.futures import ThreadPoolExecutor
b="\033[94m"
c="\033[96m"
g="\033[92m"
r="\033[91m"
p="\033[1;97m"
d="\033[00m"
dn=f"{d}[{g}√{d}]{p}"
er=f"{d}[{r}!{d}]{p}"
pr=f"{d}[{c}*{d}]{p}"
url="https://mangaid.click/"
ses=requests.Session()
ses.headers["User-Agent"] = "Mozilla/5.0 (Linux; Android 10; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.50 Mobile Safari/537.36"
result=[]
ch_result=[]
last_result=[]
def clear():
    os.system("cls" if os.name == "nt" else "clear")
def baner():
    print(f'''
\t     {d}Manga {r}ID {d}Downloader
\033[90m----------------------------------------------
{d}Donate   : {g}https://saweria.co/FahmiDevs
{d}Message  : {g}https://wa.me/62881024612817
{d}Restapi  : {g}https://ainxbot-id.herokuapp.com
{d}Youtube  : {g}https://youtube.com/KuhakuTermux
{d}Github   : {g}https://github.com/Ainx-BOT
{d}Facebook : {g}https://facebook.com/kang.ngeue.313
\033[90m----------------------------------------------{d}''')
def process():
    for i in list("\|/-•"):
        print(f"\r{pr}Process\033[90m...{d}({r}{i}{d})",end="")
        sleep(0.2)
def cblg():
    lg=input(f"{pr}Coba lagi? ({d}{c}y{d}/{c}n{p}) : {c}")
    if lg == "y" or lg == "Y":
        os.system("python run.py")
    elif lg == "n" or lg == "N":
        sys.exit(er+"Bye Bro")
        sleep(1)
        clear()
    else:
         print(er+"Wrong Input")
         sleep(1)
         cblg()
def search(judul):
    temp=[]
    req=ses.get(url+"search?query="+judul).text
    js=json.loads(req)
    for x in js["suggestions"]:
        jud=x["value"]
        dat=x["data"]
        temp.append((jud,dat))
    return temp
def manga(title):
    temp=[]
    req=ses.get(url+"manga/"+title).text
    res=bs(req,"html.parser").find_all("h5", class_="chapter-title-rtl")
    for data in res:
        manga=data.find("a",href=lambda x: x and "manga" in x)
        name=manga["title"]
        ur=manga["href"]
        total=manga["href"].split("/")[5]
        temp.append((name,ur,total))
    return temp

def lihat(param):
     temp=[]
     req=ses.get(param).text
     res=bs(req,"html.parser").find_all("div", {"id":"all","style":""})
     for data in res:
         img=data.find_all('img')
         for x in img:
             temp.append((x["alt"],x["data-src"]))
     return temp
def download(path,url):
    req=requests.get(url)
    with open(f"{path}.jpg","wb") as x:
         x.write(req.content)
if __name__=="__main__":
     clear()
     baner()
     print()
     que=input(f"{pr}Judul komik? : {c}")
     id=search(que)
     if len(id) <= 0:
        print(f"{pr}Komik yang kamu cari tidak ada")
        sleep(2)
        os.system("python run.py")
     for i,x in enumerate(id):
         print(f"{c}{i+1}\033[90m. {p}{x[0]}")
         result.append(x[1])
     print("\033[90m----------------------------------------------\033[00m")
     try:
         anim=input(f"{pr}Select : {c}")
         anim=int(anim)
     except ValueError:
         print(f"{er}Pilih yang bener")
         sleep(2)
         os.system("python run.py")
     dir1=result[anim-1]
     data=manga(result[anim-1])
     for i in reversed(data):
         ch_result.append((i[1],i[0]))
     for i,x in enumerate(ch_result):
         print(f"{c}{i+1}\033[90m. {p}{x[1]}")
     print("\033[90m----------------------------------------------\033[00m")
     try:
        pilih=input(f"{pr}Select Chapter? : {c}")
        if ":" in pilih:
           lst=pilih.split(":")
           pil1=int(lst[0])
           pil2=int(lst[1])
           pilih=ch_result[pil1-1:pil2]
           for x in pilih:
               last_result.append(x[0])
        else:
           pilih=int(pilih)
           pilih=ch_result[pilih-1][0]
           last_result.append(pilih)
     except ValueError:
        print(f"{er}Pilih yang bener")
        sleep(2)
        os.system("python run.py")
     for x in last_result:
         dir2="Chapter "+x.replace("https://mangaid.click/manga/"+dir1+"/","")
         img=lihat(x)
         try:
             f=open("/sdcard/maid/plugins.txt","w")
             f.write("biar ga error!")
         except FileNotFoundError:
             os.mkdir(os.path.join("/sdcard","maid"))
         try:
             f=open("/sdcard/maid/"+dir1+"/plugins.txt","w")
             f.write("biar ga error!")
         except FileNotFoundError:
             os.mkdir(os.path.join("/sdcard/maid",dir1))
         try:
             f=open("/sdcard/maid/"+dir1+"/"+dir2+"/plugins.txt","w")
             f.write("biar ga error!")
         except FileNotFoundError:
             os.mkdir(os.path.join("/sdcard/maid/"+dir1,dir2))
         with ThreadPoolExecutor(max_workers=10) as ex:
             path=f"/sdcard/maid/{str(dir1)}/{dir2}/"
             for images in img:
                 process()
                 name=images[0]
                 url=images[1]
                 if not "https:" in url:
                    url="https:"+url
                 ex.submit(download,(path+name),(url))
     print()
     print("\033[90m----------------------------------------------\033[00m")
     print(f"{dn}Done.")
     print(f"{pr}Komik tersimpan di internal\n {c}-> {p}/sdcard/maid/{dir1}")
     cblg()
