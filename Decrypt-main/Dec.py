# kalo gak tau cara gunain nya gak usah pake ya asw
# kalo ada yang error fix sendiri aja :v
# only marshal or zlib base64 from https://github.com/Dumai-991/

#open scored
import os
import re
import sys
try: import uncompyle6
except: os.system("python -m pip install uncompyle6")
############################################
#SC JANGAN DIPERJUAL BELIKAN :)
#SC PUNYA RISKY
#github : DUMAI-991
#facebook: fb.me/llovexnxx
#yt : Dumai+991
# 6283143565470
############################################
import os, base64, codecs, random
from sys import argv
from os import system
from time import ctime
import os, sys, zlib, base64, marshal, binascii, time, py_compile
from time import sleep as waktu
from random import randint
from os import system, name
from random import choice as pilih
from datetime import datetime
saat_ini = datetime.now()
tgl = saat_ini.strftime('%d')
bln = saat_ini.strftime('%m')
thn = saat_ini.strftime('%Y')
waktu_new = (tgl+"-"+bln+"-"+thn)
xnxx="\033[85m"
q="\033[00m"
h2="\033[40m"
b2="\033[44m"
c2="\033[46m"
i2="\033[42m"
u2="\033[45m"
m2="\033[41m"
p2="\033[47m"
k2="\033[43m"
b='\033[1;34m'
i='\033[1;32m'
c='\033[1;36m'
m='\033[1;31m'
u='\033[1;35m'
k='\033[1;33m'
p='\033[1;37m'
h='\033[1;90m'
k3="\033[43m\033[1;37m"
b3="\033[44m\033[1;37m"
m3="\033[41m\033[1;37m"
wa = ([i, q, b, m, xnxx, u, h,])
w = pilih(wa)
ttl = pilih(["#Jangan DiEdit Ngab Nanti Rusak :)","#Script DiEnclah Goblog Nanti LuRecoder :)","#Anak Kontol Biasanya Anak Reocder","#Kang Recoder Mau Lewat"])
expired = ['20', '07', '2021']
buffer_size = 9999999
logo_exp=('Maaf Gan Script Ini Expired\nHubungi Admin Untuk DiPerbaiki :)\n'+i+'6283143565470')
logo_me = (c+"""________   ____________________  """+i+""">>"""+k+"""Version 2.1.1"""+c+"""
\______ \  \_   _____/\_   ___ \ 
 |    |  \  |    __)_ /    \  \/ 
 |    `   \ |        \\     \____
/_______  //_______  / \______  /
        \/         \/         \/ 
@Enc HAMZAH To Dec
@Gunakan Dengan Bijak :)
@By Mr.Risky
@Jika Terjadi Error Silahkan Banting HP Lu....
@TANGGAL ---> """+k+waktu_new+"""
"""+w+"""
[->FB : https://m.facebook.com/llovexnxx
[->YT : Dumai-991
[->GH : https://github.com/Dumai-991
[->WA : https://wa.me/6283143565470
[->TL : https://t.me/6283143565470\n\n"""+q)
def kontol(ngaceng):
    for peli in ngaceng + '\n':
        sys.stdout.write(peli)
        sys.stdout.flush()
        time.sleep(random.random() * 0.005)

m=[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 39, 109, 97, 114, 115, 104, 97, 108, 39, 41, 46, 108, 111, 97, 100, 115]
z=[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 122, 108, 105, 98, 34, 41, 46, 100, 101, 99, 111, 109, 112, 114, 101, 115, 115]
b64=[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 98, 97, 115, 101, 54, 52, 34, 41, 46, 98, 54, 52, 100, 101, 99, 111, 100, 101]
b32=[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 98, 97, 115, 101, 54, 52, 34, 41, 46, 98, 51, 50, 100, 101, 99, 111, 100, 101]
b16=[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 98, 97, 115, 101, 54, 52, 34, 41, 46, 98, 49, 54, 100, 101, 99, 111, 100, 101]

def kon(tol):
	return "".join([chr(x) for x in tol])

if sys.version[0]!="2":
#	python="3.9" if "3.9" in sys.version[0:3] else "3.8"
	python="3.9" if "3.9" in sys.version[0:3] else "3.9"
else:
	exit(" ! gunakan python3")

def kode(file):
	buka=open(file).read()
	xnxx=re.search("b'(.*?)'",buka)
	if xnxx is not None:
		if str(m) in buka:
			if str(z) in buka:
				if str(b64) in buka:
					return "x={}({}({}(b'{}')))".format(kon(m),kon(z),kon(b64),xnxx.group(1))
				else:
					xnxx=re.search("b'(.+)",buka)
					return "x={}({}(b'{}'))".format(kon(m),kon(z),xnxx.group(1).replace("')))",""))
			else:
				xnxx=re.search("b'(.+)",buka)
				return "x=({}(b'{}".format(kon(m),xnxx.group(1))
		else:
			if str(z) in buka:
				xnxx=re.search("b'(.+)",buka)
				return "x={}(b'{}')".format(kon(z),xnxx.group(1).replace("',compile))",""))
			if str(b64) in buka: return "x={}(b'{}')".format(kon(b64),xnxx.group(1))
			if str(b32) in buka: return "x={}(b'{}')".format(kon(b32),xnxx.group(1))
			if str(b16) in buka: return "x={}(b'{}')".format(kon(b16),xnxx.group(1))
			else: exit()
	else: exit()
			
def decom(code):
	global python
	xode=kode(code)
	if xode is not None:
		if "('marshal').loads" in xode:
			open("cache","w").write("try:\n	{}\n	from uncompyle6.main import decompile\n	from sys import stdout\n	decompile({},x,stdout)\nexcept Exception as err: exit('error '+str(err))".format(xode,python))
			out=code[:-3]+"_.py" if len(code) > 4 else code
			os.system("python3 cache > {}".format(out))
			print(" * file save as {}".format(out))
		else:
			if ").decompress" in xode or ").b64decode" in xode or ").b32decode" in xode or ").b16decode" in xode:
				open("cache","w").write("try:\n	{}\n	print(x)\nexcept Exception as err: exit('error '+str(err))".format(xode))
				out=code[:-3]+"_.py" if len(code) > 4 else code
				os.system("python2 cache > {}".format(out))
				print(" * file save as {}".format(out))
			else: exit()
	else: exit()

if __name__=="__main__":
	tanggal = thn + bln + tgl
	exp = expired[2] + expired[1] + expired[0]
	if tanggal >= exp:
		print (('\n').join(['' + logo_me + logo_exp]))
		sys.exit()
#	else:
#		main()
	os.system("clear")
	kontol(logo_me)
	if len(sys.argv) >= 2:
		if os.path.exists(sys.argv[1]):
			decom(sys.argv[1])
		else:
			exit(" ! file {} tidak ditemukan".format(sys.argv[1]))
	else:
		exit(" ! usage : python3 {} file.py".format(sys.argv[0]))
	
	
