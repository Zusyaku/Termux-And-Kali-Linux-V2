import os
import urllib.request
import requests
import sys

try:
    def con():
        try:
            print(G+"\nChecking internet connection........\n")
            requests.get("http://google.com")
        except requests.ConnectionError:
            print(Y+"""
<------------------------------>"""+R+"""
Failed to connect to internet!\nCheck your internet connection :( """+Y+"""
<-------------------------------->\n"""+W)
            sys.exit()
	        
    R='\033[91m' #Red
    Y='\033[93m' #Yellow
    G='\033[92m' #Green
    CY='\033[96m' #Cyan
    W='\033[97m' #White
    B='\033[95m' #Blue
    M='\033[1;35m' #mage
    S='\033[1;36m'
    BB='\033[1;34m'

    print(Y+"""
    
    
████████ ███████ ██████  ███    ███ ██    ██ ██   ██       ██████  ██    ██ ██ 
   ██    ██      ██   ██ ████  ████ ██    ██  ██ ██       ██       ██    ██ ██ 
   ██    █████   ██████  ██ ████ ██ ██    ██   ███  █████ ██   ███ ██    ██ ██ 
   ██    ██      ██   ██ ██  ██  ██ ██    ██  ██ ██       ██    ██ ██    ██ ██ 
   ██    ███████ ██   ██ ██      ██  ██████  ██   ██       ██████   ██████  ██ 
                                                                               
                                                                               
"""+CY+"""

 ██████╗ ███╗   ██╗██╗     ██╗███╗   ██╗███████╗               v 2.0
██╔═══██╗████╗  ██║██║     ██║████╗  ██║██╔════╝      
██║   ██║██╔██╗ ██║██║     ██║██╔██╗ ██║█████╗        
██║   ██║██║╚██╗██║██║     ██║██║╚██╗██║██╔══╝          
╚██████╔╝██║ ╚████║███████╗██║██║ ╚████║███████╗      
 ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝  
                                                      
          ██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗ 
          ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝ 
          ███████║███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗
          ██╔══██║██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║
          ██║  ██║██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝
          ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ """+R+"""
                                                      
                                                                                                         
                                                                                                          

<----------------------------------------------->"""+G+"""
              Termux GUI Installer"""+Y+"""
<----------------------------------------------->"""+R+"""
          == """+CY+"""By Online HacKing (SUMAN) """+R+"""==
    
""")
    con()
    print(Y+"\n==>"+CY+" Installing repositories............\n"+W)
    os.system("apt install x11-repo")
    os.system("pkg install xfce4-session")
    os.system("apt install unstable-repo")
    print(Y+"\n==>"+CY+" Installing XFCE Environment...........\n"+W)
    os.system("apt install xfce xfce4-terminal tigervnc -y")
    print(R+"""\n
----------------------------------------------\n"""+R+"""
== """+Y+"""Installation complete! """+R+"""=="""+CY+"""\n
Now follow these steps to run Termux-GUI -->

"""+M+""" Copy Link Peste Browser For How To install And Use


"""+W+"""Website: """+S+""" https://www.onlinehacking.xyz/Graphical-User-Interface-for-Termux

"""+W+"""GitHub: """+BB+""" https://github.com/OnlineHacKing/Termux-GUI



"""+R+"""1)"""+Y+""" Run """+G+"""'vncserver'"""+Y+""" command
"""+R+"""2)"""+Y+""" Add new password for vnc
"""+R+"""3)"""+Y+""" Open VNC and Connect """+G+"""

 """+M+""" @ Any Problem to Open Website Link and Play Video @
 

"""+W+"""Telegram : """+S+""" @OnlineHacking


"""+G+"""
** Important Note - If you want to exit from GUI,type following command before exit -

-> $ vncserver -kill :<session_number> [EX- vncserver -kill :1 ]


"""+W)
except KeyboardInterrupt:
    print("Interrupted ! Good Bye! :) ")

