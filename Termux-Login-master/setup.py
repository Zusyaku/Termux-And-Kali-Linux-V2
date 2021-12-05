import os,sys

os.chdir('/data/data/com.termux/files/usr/etc')

opr = open('bash.bashrc','a')
opr.write("\nalias txl='python /data/data/com.termux/files/home/Termux-Lock/Termux-Lock.py -l'\n")
opr.write('txl\n')
opr.close()

os.system('apt install figlet')
os.system('pip install stdiomask')
os.system('pip install lolcat')