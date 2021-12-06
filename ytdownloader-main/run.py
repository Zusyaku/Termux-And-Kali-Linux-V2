import os,sys,time,requests,json,random,string
from time import sleep
from bs4 import BeautifulSoup as bs
from colorama import init, Fore, Back
B = Fore.BLUE
W = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
BL = Fore.BLACK
url="https://www.yt-download.org/file/"
def clear():
    os.system("cls" if os.name == "nt" else "clear")
def baner():
    print(f"\t\t{R}Youtube \033[00mDownloader")
    print("\t"+Back.WHITE+Fore.BLACK+"https://ainxbot-id.herokuapp.com/\033[00m")
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
      return ''.join(random.choice(chars) for _ in range(size))

def mp3(url):
    req=requests.get(url).text
    res=bs(req,"html.parser").find_all("div", class_="download flex flex-wrap sm:inline-flex text-center items-center justify-center")
    for data in res:
        urls=data.find("a",href=lambda x: x and "mp3" in x)
    return urls["href"]
def mp4(url):
    req=requests.get(url).text
    res=bs(req,"html.parser").find_all("div",class_="download flex flex-wrap sm:inline-flex text-center items-center justify-center")
    for data in res:
        urls=data.find("a",href=lambda x: x and "mp4" in x)
    return urls["href"]
if __name__=="__main__":
    clear()
    baner()
    print()
    url_vidio=input(f"{W}[{G}URL{W}]\033[00m Url vidio: {G}")
    if "www" in url_vidio:
        url_vidio=url_vidio.replace("https://www.youtube.com/","")
    elif "youtube.com" in url_vidio:
        url_vidio=url_vidio.replace("https://youtube.com/","")
    elif "youtu.be" in url_vidio:
        url_vidio=url_vidio.replace("https://youtu.be/","")
    choice=input(f"{W}[{G}CONVERT{W}]\033[00m Download? {W}({G}mp3{W}/{G}mp4{W}) \033[00m or {W}({G}combo{W}): {G}")
    if choice == "mp3":
       ms=mp3(url+"mp3/"+url_vidio)
       req=requests.get(ms)
       with open(f"/sdcard/Download/{id_generator()}.mp3", 'wb') as f:
            for data in req.iter_content(chunk_size=1024):
                f.write(data)
       print(f"{W}[{G}DONE{W}]\033[00m file tersimpan di,\n -> {G}/sdcard/Download/{id_generator()}.mp3")
    elif choice == "mp4":
       vid=mp4(url+"mp4/"+url_vidio)
       req=requests.get(vid)
       with open(f"/sdcard/Download/{id_generator()}.mp4", 'wb') as f:
            for data in req.iter_content(chunk_size=1024):
                f.write(data)
       print(f"{W}[{G}DONE{W}]\033[00m file tersimpan di,\n-> {G}/sdcard/Download/{id_generator()}.mp4")
    elif choice == "combo":
         ms=mp3(url+"mp3/"+url_vidio)
         vid=mp4(url+"mp4/"+url_vidio)
         req1=requests.get(ms)
         req2=requests.get(vid)
         with open(f"/sdcard/Download/{url_vidio}.mp3", 'wb') as f:
            for data in req1.iter_content(chunk_size=1024):
                f.write(data)
         with open(f"/sdcard/Download/{url_vidio}.mp4", 'wb') as f:
            for data in req2.iter_content(chunk_size=1024):
                f.write(data)
         print(f"{W}[{G}DONE{W}]\033[00m file tersimpan di,\n-> {G}/sdcard/Download/{id_generator()}.mp3/{id_generator()}.mp4")
    else:
        sys.exit(f"{W}[{R}INFO{W}]\033[00mInvalid Choice{R}!{W}")
    cblg=input(f"{W}[{G}?{W}]\033[00mCoba Lagi? {W}({G}y{W}/{G}n{W}): {G}")
    if cblg == "y" or cblg == "Y":
        sleep(2)
        os.system("python run.py")
    else:
        sys.exit(f"{W}[{R}EXIT{W}]Dah kontol{R}!!{W}")
