#!usr/bin/python3.7
#Author: KANG-NEWBIE
#contact: t.me/kang_nuubi
#thanks to all member CRABS_ID (t.me/CRABS_ID)

'''
recode? ok, but don't delete the author name
'''
try:
	import requests,mechanize,json,os,sys,time
	from requests import Session as ses
	from http.cookiejar import LWPCookieJar as kuki
	from prompt_toolkit import prompt


	br=mechanize.Browser()
	br.set_handle_robots( False )
	br.set_handle_refresh( mechanize._http.HTTPRefreshProcessor(), max_time = 1 )
	br.addheaders = [ ( 'User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1' ) ]

	def login():
		print("\n[!] checking cookies")
		time.sleep(1)
		s = ses()
		s.cookies = kuki('toket/kue.txt')
		try:
			fil=open('toket/kue.txt')
			fil.close()
		except FileNotFoundError:
			print("[!] cookies not found\n\n[!] please login in your facebook once again")
			email=input('[?] email/username: ')
			pw=prompt('[?] password: ',is_password=True)
			data = {'email':email,'pass':pw}
			url='https://mbasic.facebook.com/login'

			res = s.post(url,data=data).text
			if 'logout.php' in str(res) or 'mbasic_logout_button' in str(res):
				s.cookies.save()
			else:
				exit('[!] fail login into your account')

	def send(id,msg,lop):
		try:
			print()
			cjs = kuki('toket/kue.txt')
			cjs.load()
			br.set_cookiejar(cjs)
			for i in range(int(lop)):
				print("[!] sending messages to "+id)
				br.open('https://mbasic.facebook.com/messages/thread/'+id+'/')
				br.form = list(br.forms())[1]
				control = br.form.find_control("body")
				for control in br.form.controls:
					if control.type == "submit":
						control.disabled = True
				br["body"]=msg
				snd=br.submit().read()
				if 'send_success' in str(snd):
					print('[+] succes')
				else: print('[-] failed')
		except IndexError:
			print("[!] error when sending a message to",id)

	def getid(msg,limit):
		ket=open('toket/token.txt','r').read()
		re=requests.get('https://graph.facebook.com/me/?fields=friends.limit('+limit+')&access_token='+ket).text
		js=json.loads(re)
		for i in js['friends']['data']:
			send(i['id'],msg,1)

	print("""
	[ Facebook chat spammer ]
	   [ By:KANG-NEWBIE ]

1. Target chat spammer
2. Mass chat spammer
""")
	pil = int(input("/kang-newbie_> "))
	if pil == 1:
		login()
		print("\n[Info] type '<n>' for newlines")
		msg=input("[?] message : ").replace('<n>','\n')
		id=input("[?] target id: ")
		lop=input("[?] looping : ")
		send(id,msg,lop)
	elif pil == 2:
		login()
		print("\n[Info] type '<n>' for newlines")
		msg=input("[?] message : ").replace('<n>','\n')
		limit=input("[?] how many: ")
		getid(msg,limit)

except KeyboardInterrupt:
	exit("[Exit] key interrupt")
except Exception as F:
	print("Err: %s"%(F))
