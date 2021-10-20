import requests
import argparse
import sys
import os
import urllib3
import random

def user_agent():
    
    useragent = [
        "Mozilla/5.0 CK={ } (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:24.0) Gecko/20100101 Firefox/24.0",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a1) Gecko/20070308 Minefield/3.0a1",
        "Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko; googleweblight) Chrome/38.0.1025.166 Mobile Safari/535.19",
        "Mozilla/5.0 (Linux; Android 6.0.1; RedMi Note 5 Build/RB3N5C; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.91 Mobile Safari/537.36",
    ]

    return random.choice(useragent)


def console_clear():
    try:
        if sys.platform == "win32":
            os.system("cls")
        else:
            os.system("clear")
        
        return 0
    except Exception:
        print("could not clear console")
        return 1

console_clear()

def file_writer(filename, data):
    opnr = open(filename, "a+")
    opnr.write(data)
    opnr.close()

parse = argparse.ArgumentParser(description="Send request to a website using proxies to check if it's online How to: python proxyon.py proxies.txt https://www.google.com/")
parse.add_argument("proxy", type=str, help="Enter the list of proxies Example: proxies.txt")
parse.add_argument("web", type=str, help="Enter a website to send http requests using proxies.txt Example: https://www.google.com/")
args = parse.parse_args()


with open(args.proxy, "r") as opnr:
    for x in opnr:
        if x[0].strip().isdigit():
            try:
                req = requests.get(args.web, headers={"User-Agent": user_agent()}, timeout=10 ,proxies={"https": x.strip(), "http": x.strip()})
                if req.status_code == 200:
                    file_writer("onlineProxies.txt", x+"\n")
                    print("\033[1;32;40m[+]Status code: {0} OK Proxy: {1}\033[1;0m".format(req.status_code, x))
                else:
                    print("\033[1;36;40m[-]Status code: {0} Proxy: {1}\033[1;0m".format(req.status_code, x))
            except Exception:
                print("\033[1;36m[-]Error: {0}\033[1;0m".format(x))
                pass
