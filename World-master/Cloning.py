#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To VivekChandel
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

##### LOGO #####
logo = """
\033[1;96m██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗
\033[1;96m██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝
\033[1;96m██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░
\033[1;96m██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░
\033[1;96m██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗
\033[1;96m╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝

\033[1;96m██╗░░░██╗██╗██╗░░░██╗███████╗██╗░░██╗
\033[1;96m██║░░░██║██║██║░░░██║██╔════╝██║░██╔╝
\033[1;96m╚██╗░██╔╝██║╚██╗░██╔╝█████╗░░█████═╝░
\033[1;96m░╚████╔╝░██║░╚████╔╝░██╔══╝░░██╔═██╗░
\033[1;96m░░╚██╔╝░░██║░░╚██╔╝░░███████╗██║░╚██╗
\033[1;96m░░░╚═╝░░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
\033[1;96m«-----------------\033[1;91mBlackVivek\033[1;96m-----------------»
\033[1;91m  ┈┈┈◢▇◣◢▇◣┈┈◢▇◣◢▇◣┈┈◢▇◣◢▇◣┈┈┈┈  BlackVivek
\033[1;91m  ┈┈┈▇▇▇▇▇▇┈┈▇▇▇▇▇▇┈┈▇▇▇▇▇▇┈┈┈┈  MRVIVEK-CODER
\033[1;91m  ┈┈┈◥▇▇▇▇◤┈┈◥▇▇▇▇◤┈┈◥▇▇▇▇◤┈┈┈┈ 
\033[1;91m  ┈┈┈┈◥▇▇◤┈┈┈┈◥▇▇◤┈┈┈┈◥▇▇◤┈┈┈┈┈   WhatsApp
\033[1;91m  ┈┈-̴̧̬͖͇̟̟̼̱͙̠͉̟̹̘̖̥͈͖͚̯͗͑͌̃̿͗̈̿̿̏͗̑̀̀͘┈┈◥◤┈┈┈-̴̧̬͖͇̟̟̼̱͙̠͉̟̹̘̖̥͈͖͚̯͗͑͌̃̿͗̈̿̿̏͗̑̀̀͘┈┈◥◤┈┈┈-̴̧̬͖͇̟̟̼̱͙̠͉̟̹̘̖̥͈͖͚̯͗͑͌̃̿͗̈̿̿̏͗̑̀̀͘┈┈◥◤┈┈┈-̴̧̬͖͇̟̟̼̱͙̠͉̟̹̘̖̥͈͖͚̯͗͑͌̃̿͗̈̿̿̏͗̑̀̀͘┈┈┈ +1(909)300-8957
\033[1;96m«-----------------\033[1;91mBlackVivek\033[1;96m-----------------»"""   
R = '\033[1;91m'
G = '\033[1;92m'                                
Y = '\033[1;93m'
B = '\033[1;94m'
P = '\033[1;95m'
S = '\033[1;96m'
W = '\033[1;97m'
######Clear######
def clear():
    os.system('clear')

#### time sleep ####
def t():
    time.sleep(1)
def t1():
    time.sleep(0.01)

#### print std #love###
def love(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		t1()

def menu():
    clear()
    os.system('clear')
    print(logo)
    time.sleep(0.05)
    print("\033[1;41m\033[1;37m1   To return to this menu from any Tool   \033[1;0m")
    time.sleep(0.05)
    print("\033[1;41m2\033[1;37m       Stop Process Press CTRL + z        \033[1;0m")
    time.sleep(0.05)
    print("\033[1;41m3\033[1;37m         Type python2 Cloning.py          \033[1;0m")
    time.sleep(0.05)
    print("\033[1;96m[1]  Install With Out Fb Id  Tool      ●")
    time.sleep(0.05)
    print("\033[1;96m[2]  Install Facebook login  Tool      ●")
    time.sleep(0.05)
    print("\033[1;96m[3]  Install After24      Tool      ●")
    time.sleep(0.05)
    print("\033[1;96m[4]  Install Black       Tool      ●")
    time.sleep(0.05)
    print("\033[1;96m[5]  Install fbids        Tool      ●")
    time.sleep(0.05)
    print("\033[1;96m[6]  Install iron      Tool      ●")
    time.sleep(0.05)
    print("\033[1;96m[7]  Install chandel     Tool      ●")
    time.sleep(0.05)
    print("\033[1;96m[8]  Install video           Tool      ●")
    time.sleep(0.05)
    print("\033[1;91m[0]  EXIT")
    time.sleep(0.05)
    mafia()
def mafia():
	black = raw_input("\033[1;91m slect option>>>   ")
	if black =="":
		print ("Select a valid option !")
		mafia()
	elif black =="1":
		clear()
		print(logo)
		os.system("ls")
                os.system("cd World")
		os.system("cd Cloningx")
                love("\033[1;93mTool User Name\033[1;92m Black\033[1;93m Password \033[1;92mVivek")
                time.sleep(6)
                os.system("python2 Cloningx.py")
	elif black =="2":
	        clear()
	        print(logo)
	        os.system("ls")
                os.system("cd World")
		os.system("cd black")
                love("\033[1;93mTool User Name\033[1;92m vivek\033[1;93m Password \033[1;92mvivek")
                time.sleep(6)
                os.system("python2 black.py")
	elif black =="3":
	        clear()
	        print(logo)
	        os.system("rm -rf $HOME/after24")
	        os.system("cd $HOME && git clone https://github.com/MRVIVEK-CODER/after24")
                print (logo)
	        love("\033[1;91mCongratulations after24 Tool Has Been Installed Successfully")
	        love("Now you can open this tool as usual")
                love("\033[1;93mTool User Name vivek Password vivek")
                time.sleep(5)
                os.system("cd $HOME/after24 && python2 after24.py")
        elif black =="4":
		clear()
		print(logo)
		os.system("rm -rf $HOME/black")
		os.system("cd $HOME && git clone https://github.com/MRVIVEK-CODER/black")
                print (logo)
		love("\033[1;96mCongratulations Black Tool Has Been Installed Successfully")
		love("Now you can open this tool as usual")
		love("\033[1;93mTool User Name vivek Password black")
                time.sleep(5)
                os.system("cd $HOME/black && python2 black.py")
	elif black =="5":
	        clear()
		print(logo)
		os.system("rm -rf $HOME/fbids")
		os.system("cd $HOME && git clone https://github.com/MRVIVEK-CODER/fbids")
                print (logo)
		love("\033[1;96mCongratulations fbids Tool Has Been Installed Successfully")
		love("Now you can open this tool as usual")
		love("\033[1;93mTool User Name vivek Password fbids")
                time.sleep(5)
                os.system("cd $HOME/fbids && python2 fbids.py")
	elif black =="6":
	        clear()
	        print(logo)
	        os.system("cd $HOME && git clone https://github.com/MRVIVEK-CODER/iron")
                print (logo)
	        love("\033[1;91mCongratulations iron Tool Has Been Installed Successfully")
	        love("Now you can open this tool as usual")
                love("\033[1;93mTool User Name\033[1;92m vivek\033[1;93m Password \033[1;92miron")
                time.sleep(6)
                os.system("cd $HOME/iron && python2 iron.py")
        elif black =="7":
		clear()
		print(logo)
		os.system("cd $HOME && git clone https://github.com/MRVIVEK-CODER/chandel")
                print (logo)
		love("\033[1;96mCongratulations chandel Tool Has Been Installed Successfully")
		love("Now you can open this tool as usual")
		time.sleep(5)
                os.system("cd $HOME/chandel && python2 old.py")
	elif black =="8":
	        clear()
	        print(logo)
	        os.system("cd $HOME && git clone https://github.com/MRVIVEK-CODER/video")
                print (logo)
	        love("\033[1;93mCongratulations video Tool Has Been Installed Successfully")
	        love("Now you can open this tool as usual")
                love("\033[1;95mTool User Name vivek  Password video")
                time.sleep(5)
                os.system("cd $HOME/video && python2 video.py")
	elif black =="0":
	    os.system("exit")
if __name__ == "__main__":
    menu()
