
import stdiomask as sm
import os,sys

# coded by AnonyminHack5

flag = True
endc = '\033[0m'
black = '\033[30m'
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
magneto = '\033[36m'

os.system('figlet -c -k -f slant Termux-Lock|lolcat')
print ( magneto +'\n\t\t[ ★ Termux - Lock ★ ]\n',endc)
print ( green +'\t\tcoded by - AnonyminHack5\n',endc)

def main_menu():
	dash = '-'
	print(blue +'\n'+ dash*15 +'Main-Menu'+ dash*15)
	print(yellow +'''
	1.Register
	2.Login
	3.Remove Lock
	4.Exit\n''',endc)
	print(blue +'\n'+ dash*13 +'Select option'+ dash*13)

def register():
	dash = '-'
	global usr,pw
	print(blue +'\n'+ dash*15 +'Register'+ dash*15)
	usr = input(blue +'\nEnter username : ')
	pw = input(green +'\nEnter password : ')
	rpw = input(green +'\nRetype password : ')
	if pw == rpw:
		os.chdir('/data/data/com.termux/files/usr/share')
		usrpwd = open("usr_nd_pwd.txt",'w')
		usrpwd.writelines(usr+'\n')
		usrpwd.writelines(pw+'\n')
		usrpwd.close()
		print(magneto +'\nRegistered Successfully...')
		os.chdir('/data/data/com.termux/files/home')
	else:
		print(red +"Password doesn't match")
	print(blue +'\n'+ dash*15 +'Complete'+ dash*15)

def check_usr_pass():
	dash = '-'
	global flag,usr,pw
	print(blue +'\n'+ dash*15 +'Login'+ dash*15)
	username = input(yellow + '\n\t[+] Username : ')
	password = sm.getpass(prompt=yellow + '\n\t[*] Password : ',mask='*')
	print(blue +'\n'+ dash*13 +'Completed'+ dash*13)
	usrpwd = open("/data/data/com.termux/files/usr/share/usr_nd_pwd.txt")
	lines = usrpwd.readlines()
	usrpwd.close()
	if(len(lines) >= 2):
		usr = lines[0]
		pwd = lines[1]
		if username+'\n' == usr and password+'\n' == pwd:
			print(green + '\n\t\t[★] Welcome to the termux [★]\n',endc)
			flag = False
		else:
			print(red + '\n\t\t[×] Invalid username or password [×]',endc)
	else:
		print(red +'\n\tYou have removed your lock')
		print(blue +'\tso, First register to login')

def remove():
	dash = '-'
	readFile = open("/data/data/com.termux/files/usr/share/usr_nd_pwd.txt")
	lines = readFile.readlines()
	readFile.close()
	print(blue +'\n'+dash*40)
	if(len(lines) >= 2):
		w = open("/data/data/com.termux/files/home/MyRepo/usr_nd_pwd.txt",'w')
		w.writelines([item for item in lines[:-2]])
		w.close()
		print(magneto +'\n\tTermux-Lock disabled successfully...')
	else:
                print(red +'\n\tYou have already removed your lock')
                print(blue +'\tso, First register to login')
	print(blue +'\n'+dash*40)

def exit():
	global flag
	print(blue +'\n\tThank you for Using my tool...',endc)
	flag = False
	exit

if len(sys.argv) >=2:
        arg = sys.argv[1]
        if arg == '-l':
                check_usr_pass()

while flag == True:
	menu = {1:register,2:check_usr_pass,3:remove,4:exit}
	main_menu()
	choice = int(input(magneto +'\nEnter choice : '))
	menu[choice]()