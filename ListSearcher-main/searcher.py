# -*- coding: utf-8 -*-
#!usr/bin/python
import os, re, sys, socket, json
import requests as req 
from multiprocessing.dummy import Pool
from colorama import *

init(autoreset=True)
####################### 
# Coded By Tegal1337  #
#######################
fg = '\033[0;32m'
fr = '\033[0;31m'
fw = '\033[1;37m'
fb = '\033[0;34m'
fy = '\033[1;33m'
fre = '\033[0m'
  
Headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}

def cut(text='',leng=False):
  if leng == False:
    ret = text
  else:
    length_string = len(text)
    if length_string > leng:
      ret = text[0:leng]
    else:
      neko = leng-length_string
      ret = text+' '*neko
  return str(ret)

def dorker(word):
  raw_domain = ['ac', 'ad', 'ae', 'af', 'ag', 'ai', 'al', 'am', 'an', 'ao', 'aq', 'ar', 'as', 'at', 'au', 'aw', 'ax', 'az', 'ba', 'bb', 'bd', 'be', 'bf', 'bg', 'bh', 'bi', 'bj', 'bl', 'bm', 'bn', 'bo', 'br', 'bq', 'bs', 'bt', 'bv', 'bw', 'by', 'bz', 'ca', 'cc', 'cd', 'cf', 'cg', 'ch', 'ci', 'ck', 'cl', 'cm', 'cn', 'co', 'cr', 'cs', 'cu', 'cv', 'cw', 'cx', 'cy', 'cz', 'dd', 'de', 'dj', 'dk', 'dm', 'do', 'dz', 'ec', 'ee', 'eg', 'eh', 'er', 'es', 'et', 'eu', 'fi', 'fj', 'fk', 'fm', 'fo', 'fr', 'ga', 'gb', 'gd', 'ge', 'gf', 'gg', 'gh', 'gi', 'gl', 'gm', 'gn', 'gp', 'gq', 'gr', 'gs', 'gt', 'gu', 'gw', 'gy', 'hk', 'hm', 'hn', 'hr', 'ht', 'hu', 'id', 'ie', 'il', 'im', 'in', 'io', 'iq', 'ir', 'is', 'it', 'je', 'jm', 'jo', 'jp', 'ke', 'kg', 'kh', 'ki', 'km', 'kn', 'kp', 'kr', 'kw', 'ky', 'kz', 'la', 'lb', 'lc', 'li', 'lk', 'lr', 'ls', 'lt', 'lu', 'lv', 'ly', 'ma', 'mc', 'md', 'me', 'mf', 'mg', 'mh', 'mk', 'ml', 'mm', 'mn', 'mo', 'mp', 'mq', 'mr', 'ms', 'mt', 'mu', 'mv', 'mw', 'mx', 'my', 'mz', 'na', 'nc', 'ne', 'nf', 'ng', 'ni', 'nl', 'no', 'np', 'nr', 'nu', 'nz', 'om', 'pa', 'pe', 'pf', 'pg', 'ph', 'pk', 'pl', 'pm', 'pn', 'pr', 'ps', 'pt', 'pw', 'py', 'qa', 're', 'ro', 'rs', 'ru', 'rw', 'sa', 'sb', 'sc', 'sd', 'se', 'sg', 'sh', 'si', 'sj', 'sk', 'sl', 'sm', 'sn', 'so', 'sr', 'ss', 'st', 'su', 'sv', 'sx', 'sy', 'sz', 'tc', 'td', 'tf', 'tg', 'th', 'tj', 'tk', 'tl', 'tm', 'tn', 'to', 'tp', 'tr', 'tt', 'tv', 'tw', 'tz', 'ua', 'ug', 'uk', 'um', 'us', 'uy', 'uz', 'va', 'vc', 've', 'vg', 'vi', 'vn', 'vu', 'wf', 'ws', 'ye', 'yt', 'yu', 'za', 'zm', 'zr', 'zw', 'krd', 'online', 'bussiness', 'pro', 'cat', 'xyz', 'net', 'org', 'site', 'info', 'asia', 'biz', 'edu', 'gov', 'club', 'top', 'tech', 'today', 'space', 'guru', 'icu', 'live', 'mobi']
  try:
    for a in raw_domain:
      getsite = req.get('https://api.domainsdb.info/v1/domains/search?domain='+word+'&zone='+a)
      if "Can't find any domains" in getsite.text:
        print('{}No Result [{}] >> [{}]'.format(fr, word, a))
      else:
        for grabdom in json.loads(getsite.text)['domains']:
          domGrabbed = grabdom['domain']
          if domGrabbed in open('domdb_rez.txt', 'r').read():
            print('{}Duplicate URL >> [{}]'.format(fr, domGrabbed))
          else:
            print('{}Grabbed URL [{}] >> [{}] >> {}'.format(fy, word, a, domGrabbed))
            save = open('domdb_rez.txt', 'a')
            save.write(domGrabbed+'\n')
            save.close()
  except:
    pass
  
def get_plugin(plugin):
  page = 0
  while True:
    page += 1
    b = req.get('http://pluginu.com/'+plugin+'/'+str(page))
    c = re.findall('<p style="margin-bottom: 20px">(.*?)</p></a>', b.text)
    if c == '':
      print('EndPage')
      sys.exit()
    else:
      for domain in c:
        print('[{}] >> [{}]'.format(str(page), domain))
        save = open(plugin+'.txt', 'a')
        save.write('http://'+domain+'\n')
        save.close()
        
#plugins = raw_input('Plugins name : ')
#get_plugin(plugins)

def get_theme(theme):
  page = 0
  while True:
    page += 1
    d = req.get('https://themetix.com/'+theme+'/'+str(page), verify=False)
    e = re.findall('<p style="margin-bottom: 20px">(.*?)</p></a>', d.text)
    if e == '':
      print('EndPage')
      sys.exit()
    else:
      for domain in e:
        print('[{}] >> [{}]'.format(str(page), domain))
        save = open(theme+'.txt', 'a')
        save.write('http://'+domain+'\n')
        save.close()
        
#themes = raw_input('Plugins name : ')
#get_theme(themes)

def zone(dom):
  page = 0
  while True:
    page += 1
    f = req.get('http://pluginu.com/domain-zone/'+dom+'/'+str(page))
    g = re.findall('<button class="btn btn-default pull-left" type="button">\n  (.*?)</button></a>', f.text)
    if g == '':
      print('EndPage')
      sys.exit()
    else:
      for domain in g:
        print('[{}] >> [{}]'.format(str(page), g))
        save = open(dom+'.txt', 'a')
        save.write('http://'+domain+'\n')
        save.close()

#tld = raw_input('enter Tld. Domain : ')
#zone(tld)

def grab(date):
  page = 0
  while True:
    page += 1
    h = req.get('https://www.cubdomain.com/domains-registered-by-date/'+date+'/'+str(page))
    i = re.findall('/site/(.+?)?"', h.text)
    if i == '':
      print('EndPage')
      sys.exit()
    else:
      for domain in i:
        print('[{}] >> [{}]'.format(str(page), domain))
        save = open(date+'.txt', 'a')
        save.write('http://'+domain+'\n')
        save.close()

def domaintoip(domz):
  try:
    j = socket.gethostbyname(domz)
    if j in open('ips_rez.txt', 'r').read():
      pass
    else:
      print('Retrieve IP: {}{}'.format(fy, j))
      open('ips_rez.txt', 'a').write(j+'\n')
  except:
    pass

def ipranger(ipz):
  k = ipz.rstrip()
  l = ipz.split('\n')[0].split('.')
  ip1 = l[0]
  ip2 = l[1]
  ip3 = l[2]
  m = str(ip1) + '.' + str(ip2) + '.'
  n = 0
  while n <= 255:
    n += 1
    o = 0
    while o <= 255:
      o += 1
      print("Ranging ==>" + str(m) + str(o) + '.' + str(n))
      open('range_rez.txt', 'a').write(str(m) + str(o) + '.' + str(n) + '\n')
      
def revip(target):
  try:
    p = req.get('https://sonar.omnisint.io/reverse/' + target)
    if "null" in p.text:
      print("[?] "+cut(target, 18)+" | Failed")
    else:
     q = json.loads(p.text)
     print("[!] {} | {} Domains".format(cut(str(target), 18), len(q)))
     for domain in q:
       open('resultzz.txt', 'a').write('http://' + domain + "\n")
  except:
    pass

def scsubdo(tdomain):
  try:
    r = req.get('https://sonar.omnisint.io/subdomains/'+tdomain)
    if 'null' in r.text:
      print("[?] "+cut(target, 18)+" | Failed")
    else:
      s = json.loads(r.text)
      print("[!] {} | {} SubDomains".format(cut(str(tdomain), 18), len(s)))
      for domain in s:
        open('subdo_rez.txt', 'a').write('http://' + domain + "\n")
  except:
    pass
          
def main():
  banner = """
  {}=============================================
               {}List Searcher v2
               
   {}Coded By: Tegal1337 {}║ {}https://tegalsec.org
  {}=============================================
  """.format(fr, fw, fy, fw, fy, fr)
  print(banner)
  print("{}[{}1{}] {}  Grab Website From Words".format(fr, fg, fr, fw))
  print("{}[{}2{}] {}  WordPress Grabber From Plugins Name".format(fr, fg, fr, fw))
  print("{}[{}3{}] {}  WordPress Grabber From Themes Name".format(fr, fg, fr, fw))
  print("{}[{}4{}] {}  Grab Website From Domain Extensions".format(fr, fg, fr, fw))
  print("{}[{}5{}] {}  Grab Website From Dates".format(fr, fg, fr, fw)) 
  print("{}[{}6{}] {}  Get IP From Domain".format(fr, fg, fr, fw))
  print("{}[{}7{}] {}  IP Ranger (1-255)".format(fr, fg, fr, fw))
  print("{}[{}8{}] {}  Reverse IP Unlimited".format(fr, fg, fr, fw))
  print("{}[{}9{}] {}  Subdomain Scanner".format(fr, fg, fr, fw))
  choice = raw_input('\n{}root@tegalsec.org {}[MENU]:{} '.format(fy, fr, fre))
  if (choice == '1'):
    listword = open(raw_input(fb+'ListWords : '), 'r').read().replace('\n', ' ').strip()
    lis = listword.split(' ')
    pp = Pool(50)
    pp.map(dorker, lis)
  elif (choice == '2'):
    plugins = raw_input('enter plugins name : ')
    get_plugin(plugins)
  elif (choice == '3'):
    themes = raw_input('enter themes name : ')
    get_theme(themes)
  elif (choice == '4'):
    tld = raw_input('enter Tld. Domain : ')
    zone(tld)
  elif (choice == '5'):
    dates = raw_input(fr+'input date (yyyy-mm-dd): ')
    grab(dates)
  elif (choice == '6'):
    domz = open(raw_input(fb+"Give Me list to get IP's : "),'r').read().replace('http://', '').replace('https://', '').splitlines()
    Thread = raw_input('Thread:~# ')
    th = Pool(int(Thread))
    th.map(domaintoip, domz)
  elif (choice == '7'):
    zizi = raw_input(fg+'List Ips:~#')
    with open(zizi) as xy:
      for ipz in xy:
        ipranger(ipz)
  elif (choice == '8'):
    target = open(raw_input(fw+'List:~# '),'r').read().replace('http://', '').replace('https://', '').splitlines()
    Threadz = raw_input(fw+'Thread:~# ')
    xx = Pool(int(Threadz))
    xx.map(revip, target)
  elif (choice == '9'):
    tdomain = open(raw_input(fw+'Input List:~# '),'r').read().replace('http://', '').replace('https://', '').splitlines()
    Threadz = raw_input(fw+'Thread:~# ')
    xz = Pool(int(Threadz))
    xz.map(scsubdo, tdomain)
  else:
    print('Choice Wrong ... Run Again !'.format(fw))
main()
