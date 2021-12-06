import os,sys,time,re,time
from time import sleep
import requests as req
from urllib.parse import unquote
from colorama import init, Fore, Back
B = Fore.BLUE
W = Fore.WHITE
C = Fore.CYAN
R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW
M = Fore.MAGENTA
BL = Fore.BLACK
def clear():
    os.system("cls" if os.name == "nt" else "clear")
def back():
    input(W+"["+Y+" Press Enter To Back"+W+" ]")
    sleep(1)
    os.system("python run.py")
def failed():
    print(R+"[×]"+W+" No Output"+R+"!!"+W)
    back()
def baner():
    print(f"""
{M}╔╦╗{W}┌─┐┬ ┬┌┐┌┬  ┌─┐┌─┐┌┬┐  {M}╦  ╦{W}┬┌┬┐┬┌─┐  {M}╔═╗{W}┌┐ 
{M} ║║{W}│ ││││││││  │ │├─┤ ││  {M}╚╗╔╝{W}│ ││││ │  {M}╠╣ {W}├┴┐
{M}═╩╝{W}└─┘└┴┘┘└┘┴─┘└─┘┴ ┴─┴┘   {M}╚╝ {W}┴─┴┘┴└─┘  {M}╚  {W}└─┘""")
    print(Back.WHITE+BL+"  Donate : https://saweria.co/donate/FahmiDev \033[00m")


def down(url):
    result=req.get(url).text
    if "video_redirect" in result:
       url=re.search(r'href\=\"\/video\_redirect\/\?src\=(.*?)\"',result)
       url=url.group(1).replace(";","&")
       return unquote(url)
    else:
       failed()
if __name__=="__main__":
     clear()
     baner()
     url=input(W+"["+M+"?"+W+"]Url vidio : "+M)
     url=url.replace("www","mbasic")
     nama=input(W+"["+M+"?"+W+"]Nama vidio : "+M)
     result=down(url)
     result=req.get(result)
     size=round(int(result.headers.get("Content-Length"))/1024)
     print(f"{W}[{M}!{W}]Vidio Size : {M}{size} {W}KB")
     with open(f"/sdcard/Download/{nama}.mp4", "wb") as x:
          for data in result.iter_content(chunk_size=1024):
              x.write(data)
     print(f"{W}[{G}✓{W}]Download Success")
     print(f"{W}[{C}+{W}]Vidio Tersimpan Di /sdcard/Download")
     back()
