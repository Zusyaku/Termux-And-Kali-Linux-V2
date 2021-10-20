#!/usr/bin/python3
'''

'''
import os, random, time, re, requests, threading

Colors = ['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[39m']
try:
    os.mkdir('Results')
except:
    pass

def Print_Logo():
    Logo = '''

                                                  
                 __          __  _         _ _       
                \ \        / / | |       (_) |      
                 \ \  /\  / /__| |__  ___ _| |_ ___ 
                  \ \/  \/ / _ \ '_ \/ __| | __/ _ \\
                   \  /\  /  __/ |_) \__ \ | ||  __/
                    \/  \/ \___|_.__/|___/_|\__\___|

                        Coded By .::Shayan::.         
                        __      ___                        
                        \ \    / (_)                       
                         \ \  / / _  _____      _____ _ __ 
                          \ \/ / | |/ _ \ \ /\ / / _ \ '__|
                           \  /  | |  __/\ V  V /  __/ |   
                            \/   |_|\___| \_/\_/ \___|_|   
                                                        
                                                        
 

                  '''
    for Line in Logo.split('\n'):
        time.sleep(0.1)
        print(random.choice(Colors)+Line)
def Clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def C():
    return random.choice(Colors)

f_name = ''


def Viewer(Proxy,Url):
    pr = open(Proxy,'r').read().splitlines()
    for prox in pr:            
        headers = {
            'Accept':'*/*',
            'Content-Type':'application/x-www-form-urlencoded',
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'        
        }
        proxies = {
            'http':str(prox),
            'https':str(prox)
        }
        try:
            r = requests.get(Url,proxies=proxies,headers=headers,timeout=1)
            if r.status_code == 200:
                print(C()+prox+C()+' -> '+C()+'Sent'+C()+'!')
                o = open(f_name+'/GoodProxies.txt','a')
                o.write(prox+'\n')
                o.close()
        except:
            print(C()+prox+C()+' -> '+C()+'Bad'+C()+'!')
            o = open(f_name+'/BadProxies.txt','a')
            o.write(prox+'\n')
            o.close()
    time.sleep(3)
    Clear()
    print(C()+'Finished!')
    input(C()+'Press Enter To Continue...')

while True:
    Clear()
    Print_Logo()
    print(C()+' Please Enter The Proxies File Address')
    pr = input(C()+'  > '+C())
    print('\n\n'+C()+' Please Enter The Website Address')
    website = input(C()+'  > '+C())
    Clear()
    f_name = 'Results/'+str(time.strftime("%Y_%m_%d-%H_%M_%S", time.gmtime()))
    if not os.path.isdir(f_name):
        os.mkdir(f_name)
    Viewer(str(pr),str(website))