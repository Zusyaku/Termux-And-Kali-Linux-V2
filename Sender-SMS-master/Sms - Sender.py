import requests,time,sys,random

from colorama import *
from colorama import Fore, Back, init
from random import choice

init()

Red = '\033[91m'
Green = '\033[92m'
Grey = '\033[90m'
star = '\033[4m'
White = '\033[00m'



def logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """ 
 
.------..------..------..------..------.     .------..------..------..------.
|A.--. ||M.--. ||J.--. ||A.--. ||D.--. |.-.  |T.--. ||O.--. ||N.--. ||I.--. |
| (\/) || (\/) || :(): || (\/) || :/\: ((5)) | :/\: || :/\: || :(): || (\/) |
| :\/: || :\/: || ()() || :\/: || (__) |'-.-.| (__) || :\/: || ()() || :\/: |
| '--'A|| '--'M|| '--'J|| '--'A|| '--'D| ((1)) '--'T|| '--'O|| '--'N|| '--'I|
`------'`------'`------'`------'`------'  '-'`------'`------'`------'`------'
 +-++-++-+ +-++-++-++-++-++-+
 |S||M||S| |S||E||N||D||E||R|
 +-++-++-+ +-++-++-++-++-++-+
                                                            
      
 
 SMS Send        Coded by "t.me/xanlrbk" Channel : t.me/cityxan                                  


 [+] 1. Run SMS Sender 
 [+] 2. About me 

--- Think before u type ---
"""
    for N, line in enumerate( x.split( "\n" ) ):
        sys.stdout.write( " \x1b[1;%dm%s%s\n " % (random.choice( colors ), line, clear) )
        time.sleep( 0.05 )


logo()

choice=input(' [+] Select : ')
if choice=='1':
 def main():
  x = """\n\033[32mFrom Name = Sender name (ex : Insta)
List of N° = dir number f file almerdi .txt
Subject = message

N.B*: Numbers f txt ktbo haka : +countrycode-number
E.X: +212-649xxxxxx\n"""
  print (x)
  sender=str(input('\n\033[0m[+] From Name >  \033[32m'))
  inputs=open(input('\n\033[0m[+] List of N° (.txt) > \033[32m'),'r').read().splitlines()
  msg=str(input('\n\033[0m[+] Subject > \033[32m'))
  print('\n\033[0m[+] ToTal numbers : '+str(len(inputs)))
  time.sleep(1)
  print("\nlet's Start")
  for i in inputs:
   code=i.split('-')[0]
   num=i.split('-')[1]
   if '+' in str(code):
    code=code.replace('+','')
   bitch=requests.get('http://api.msg91.com/api/sendhttp.php?sender='+sender+'&route=4&mobiles='+num+'&authkey=201074AfPVnOOJCq5a9d4f8e&country='+code+'&message='+msg)
   print('\n[+] Sending To '+str(i)+'\n Statut :\033[92m Succes' )
 try:
  main()
 except FileNotFoundError:
   print('\nFile Not Found :|\n')
   sys.exit(0)
elif choice =='2':
 xx = """\n\033[32mName: Toni 
Current Location : Marruecos 
Telegram : @xanlrbk
                                                          
    _    __  __     _   _    ____    _____ ___  _   _ ___ 
   / \  |  \/  |   | | / \  |  _ \  |_   _/ _ \| \ | |_ _|
  / _ \ | |\/| |_  | |/ _ \ | | | |   | || | | |  \| || | 
 / ___ \| |  | | |_| / ___ \| |_| |   | || |_| | |\  || | 
/_/   \_|_|  |_|\___/_/   \_|____/    |_| \___/|_| \_|___|
                                                          
\n"""
 print(xx)
