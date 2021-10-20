try:
	from multiprocessing.pool import ThreadPool
	import os, requests, sys, json, time
	try:
		os.mkdir('dump')
	except: pass

	id=[]
	def get(ids):
		global token
		token = open('toket/token.txt','r').read()
		a = requests.get("https://graph.facebook.com/"+ids+"/friends?access_token="+token)
		b = json.loads(a.text)
		for i in b['data']:
			id.append(i['id'])

	def main(arg):
		try:
			c=requests.get('https://graph.facebook.com/'+arg+'/?access_token='+token)
			d=json.loads(c.text)
			if '@yahoo' in d['email']:
				fil=open('dump/Ymail.txt','a')
				fil.write(d['email']+'\n')
				fil.close()
				print("[Yahoo] "+d['email'])
			elif '@gmail' in d['email']:
				fIle=open('dump/Gmail.txt','a')
				fIle.write(d['email']+'\n')
				fIle.close()
				print("[Gmail] "+d['email'])
			else:
				fil3=open('dump/other.txt','a')
				fil3.write(d['email']+'\n')
				fil3.close()
				print("[other] "+d['email'])
		except: pass
	
	print("""
	[Facebook Dump Email]
	   [By:KANG-NEWBIE]
	""")
	pil=input("[*] dump with target id? (y/n) ")
	if pil == 'y' or pil == 'Y':
		ids=input("[?] target id: ")
		print("[!] getting id...")
		get(ids)
		print("[!] start\n")
	else:
		print("[!] getting id...")
		get('me')
		print("[!] start\n")

	p=ThreadPool(20)
	p.map(main,id)
	print("""
[FILE SAVED]
Gmail: dump/Gmail.txt
Yahoo: dump/Ymail.txt
Other: dump/other.txt""")

except KeyboardInterrupt: exit("[exit] key interrupt")
except Exception as F:
	print("Err: %s"%(F))