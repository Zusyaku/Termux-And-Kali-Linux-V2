#!/usr/bin/python
# -*- coding: utf-8 -*-

# -- import Modules --
import os
import sys
import json
import random
import requests
import platform
import threading

py_version = platform.python_version()
if int(py_version[0]) == 2:
   from Queue import Queue
if int(py_version[0]) == 3:
   from queue import Queue

# -- Colors --
if sys.platform in ["linux","linux2"]:
   purple = '\033[95m'
   blue = '\033[94m'
   cyan = '\033[96m'
   green = '\033[92m'
   yellow = '\033[93m'
   red = '\033[91m'
   end = '\033[0m'
   bold = '\033[1m'
   u = '\033[4m'
else:
   purple = ''
   blue = ''
   cyan = ''
   green = ''
   yellow = ''
   red = ''
   end = ''
   bold = ''
   u = ''

# -- Clear --
if sys.platform == 'win32':
   os.system('cls')
else:
   os.system('clear')

# -- Class --
class Reverse_Ip:
   def __init__(self):
      self.url = 'https://reverseip-tools.com/api?q='
      self.banner()
      self.save = 'result.txt'
   def reverse(self, domain):
        try:
            req = requests.get(self.url+domain)
            if req.status_code == 200:
                jumlah = len(req.json()['result'])
                if jumlah > 10  and  jumlah < 100:
                    color = yellow
                elif jumlah < 10:
                    color = red
                else:
                    color = green
                print ("{} >> ({} domains)".format(color+domain, str(jumlah)))
                res = req.json()
                if res['result']:
                    domains = '\n'.join(res['result'])
                    open(self.save, 'a').write(domains+'\n')
        except Exception as v:
            print(v)
   def start(self, q):
     while not q.empty():
       dom = q.get()
       if dom:
          self.reverse(dom)
       q.task_done()
   def banner(self):
      b = '''
     ◢◤ ◢◤ ◢◤ ◢◤ ◢◤ ◢◤ ◢◤ ◢◤ ◢◤ ◢◤
   ◢◤                            ◢◤
  ◢◤  Reverse Ip (Unlimited)    ◢◤
 ◢◤  By Zeerx7 - XpoitSec-ID   ◢◤
◢◤                            ◢◤
 ◢◤ ◢◤ ◢◤ ◢◤ ◢◤ ◢◤ ◢◤ ◢◤ ◢◤ ◢◤
'''   
      co = random.choice([red,purple,blue])
      ct = random.choice([green,cyan,yellow])
      banner = b.replace('◢◤',co+'◢◤').replace('R',ct+'R').replace('B',ct+'B')
      print(banner)
   def input(self, q):
      #input based on python version
      if int(py_version[0]) == 3:
           return input(str(q))
      elif int(py_version[0]) == 2:
           return raw_input(str(q))
   def main(self):
      jobs = Queue()
      thread = 10
      try:
          filename = self.input(yellow+'Domains/Ip List -> '+green)
          list = open(filename, 'r').read().splitlines()
      except IOError:
           exit(red+"File Not Found!\n")
      except FileNotFoundError:
           exit(red+"File Not Found!\n")
      print (red+'\nI suggest using no more than (10) threads \nor the tools will crash!')
      thread = int(self.input(yellow+'Thread -> '+green))
      print(blue+'\nResult will be saved in: result.txt')
      for dom in list:
         if dom:
             jobs.put(dom)

      for x in range(thread):
         worker = threading.Thread(target=self.start, args=(jobs,))
         worker.start()

# -- Main --
if __name__ == '__main__':
     Reverse_Ip().main()
