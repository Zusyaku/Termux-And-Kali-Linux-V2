# -*- coding: utf-8 -*-

import requests , os , time , datetime , re
from bs4 import BeautifulSoup

W  = '\033[0m'  # white (default)
R  = '\033[1;31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[1;33m' # orange
B  = '\033[1;34m' # blue
P  = '\033[1;35m' # purple
C  = '\033[1;36m' # cyan
GR = '\033[1;37m' # gray
os.system('clear')

def banner():
    print (R+"██████████████████████████████████████"+C+"═╗")
    print ("╚═══════════════════════════════════"+R+"██"+C+" ║"+R)
    print ("                                    ██"+C+" ║"+W)
    print (W+"    ██╗     ██╗  ██╗██████╗  ██╗    "+R+"██"+C+" ║"+W)
    print (W+"    ██║     ██║ ██╔╝╚════██╗███║    "+R+"██"+C+" ║"+W)
    print (W+"    ██║     █████╔╝  █████╔╝╚██║    "+R+"██"+C+" ║"+W)
    print (W+"    ██║     ██╔═██╗ ██╔═══╝  ██║    "+R+"██"+C+" ║"+W)
    print (W+"    ███████╗██║  ██╗███████╗ ██║    "+R+"██"+C+" ║"+W)
    print (W+"    ╚══════╝╚═╝  ╚═╝╚══════╝ ╚═╝    "+R+"██"+C+" ║"+R)
    print ("                                    ██"+C+" ║"+R)
    print ("██████████████████████████████████████"+C+" ║")
    print ("╚══════════════════════════════════════╝")
    print (W+"")

def banner_dl():
    print (R+"██████████████████████████████████████"+C+"═╗")
    print ("╚═══════════════════════════════════"+R+"██"+C+" ║"+R)
    print ("                                    ██"+C+" ║  ═════════════════════════════")
    print (W+"    ██╗     ██╗  ██╗██████╗  ██╗    "+R+"██"+C+" ║"+W)
    print (W+"    ██║     ██║ ██╔╝╚════██╗███║    "+R+"██"+C+" ║"+W+"   ", time.ctime())
    print (W+"    ██║     █████╔╝  █████╔╝╚██║    "+R+"██"+C+" ║"+W+"   ", judul)
    print (W+"    ██║     ██╔═██╗ ██╔═══╝  ██║    "+R+"██"+C+" ║"+W+"    http://149.56.24.226")
    print (W+"    ███████╗██║  ██╗███████╗ ██║    "+R+"██"+C+" ║"+W)
    print (W+"    ╚══════╝╚═╝  ╚═╝╚══════╝ ╚═╝    "+R+"██"+C+" ║  ═════════════════════════════"+R)
    print ("                                    ██"+C+" ║"+W+"   https://github.com/N1ght420"+R)
    print ("██████████████████████████████████████"+C+" ║")
    print ("╚══════════════════════════════════════╝")
    print (W+"")

banner()
a = input(C+" Judul "+R+"> "+W)
os.system('clear')
payload = {"s":a}
req = requests.get("http://149.56.24.226/", params=payload).text
soup = BeautifulSoup(req, "html.parser")
linknya = soup.find_all('h2')
link = linknya[2]
try:
    judul = re.search(r'<a href="http://149.56.24.226/(.*)/" rel="bookmark"', str(link)).group(1)
except AttributeError:
    judul = re.search(r'<a href="http://149.56.24.226/(.*)/" rel="bookmark"', str(link))
try:
    banner_dl()
    print (C+" ["+W+" JUDUL "+C+"]"+R+" >"+W+" ",str(judul))
    print ("")
    dload = "http://dl.sharemydrive.xyz/get/" + judul
    bpass = "http://dl.sharemydrive.xyz/verifying.php"
    data = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "Accept":"*/*",
            "X-Requested-With":"XMLHttpRequest"}
    payload2 = {"slug":judul}
    req2 = requests.post(bpass, headers=data, params=payload2).text
    soup2 = BeautifulSoup(req2, "html.parser")
    linkdownload = soup2.find_all('a')
    p360 = re.findall(r'btn-360" href="(.*)" rel=', str(linkdownload))
    if len(p360) > 0:
        for laz1 in p360:
            print(C+" ["+W+" 360 P "+C+"]"+R+" >"+W+" ",laz1)
    p480 = re.findall(r'btn-480" href="(.*)" rel=', str(linkdownload))
    if len(p480) > 0:
        for laz2 in p480:
            print(C+" ["+W+" 480 P "+C+"]"+R+" >"+W+" ",laz2)
    p720 = re.findall(r'btn-720" href="(.*)" rel=', str(linkdownload))
    if len(p720) > 0:
        for laz3 in p720:
            print(C+" ["+W+" 720 P "+C+"]"+R+" >"+W+" ",laz3)
    p1080 = re.findall(r'btn-1080" href="(.*)" rel=', str(linkdownload))
    if len(p1080) > 0:
        for laz4 in p1080:
            print(C+" ["+W+" 1080P "+C+"]"+R+" >"+W+" ",laz4)
except:
    print (C+" ["+W+" 404 "+C+"]"+R+" >"+W+" Film tidak ditemukan")
print ("")
