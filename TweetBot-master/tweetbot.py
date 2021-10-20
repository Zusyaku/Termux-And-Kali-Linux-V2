import os
import time
from random import *
os.system("chmod +x greet")
os.system("bash greet")
while True:
	print("\nEnter Your username/Phone :")
	user=input().strip()
	print("\nEnter Your Password :")
	pas=input().strip()
	print("\nEnter Tweet List File Path")
	path=input().strip()
	print("\nEnter Additional Things to Put Like #SpeedX or @SpeedX")
	add=input().strip()
	print("\nEnter Delay Between Tweets (in milliseconds) (1000 ms = 1 s)")
	delay=int(input())
	print("Your Twitter Username : \""+user+"\"")
	print("\nYour Twitter Password : \""+pas+"\"")
	print("\nFile Containing Tweets : \""+path+"\"")
	print("\nAdd Text : \""+add+"\" To Each Tweet")
	print("\nDelay Between 2 Tweets : \""+str(delay)+"\"")
	print("\nPress Y To Continue...\nPres N To Edit...")
	ch=input().strip()
	if (ch.find('y') != -1 or ch.find('Y') != -1):
		break
print("\n\n\nLogging in...")
f=open("init","w")
s1="# Command logfile created by Lynx 2.8.9rel.1 SpeedX\n# Arg0 = lynx\n# Arg1 = http://mobile.twitter.com/session/new\n# Arg2 = -cmd_log=init"
s1=s1+"\nkey Down Arrow\nkey Down Arrow"
s2=""
s3=""
for s in user:
	s2=s2+"\nkey "+s
for s in pas:
	s3=s3+"\nkey "
	if s == ' ':
		s3=s3+"<space>"
	else:
		s3=s3+s
s3=s3+"\nkey Down Arrow\nkey Right Arrow"
f.write(s1)
f.write(s2)
f.write("\nkey Down Arrow")
f.write(s3)
f.write("\nkey q\nkey y")
f.close()
os.system("lynx http://mobile.twitter.com/session/new -cmd_script=init")
print("\nLogged in Successfully!!")
print("\nLoading Tweet List...")
f=open(path,"r")
t=f.read()
f.close()
tl=t.split("\n")
print(str(len(tl))+" Tweets Loaded !!!")
print("Starting To Tweet !!!")
n=0
first="\nkey Down Arrow\nkey Down Arrow\nkey Down Arrow\nkey Down Arrow\nkey Down Arrow\nkey Down Arrow\nkey Right Arrow\nkey Down Arrow\nkey Down Arrow"
last="\nkey Down Arrow\nkey Down Arrow\nkey Down Arrow\nkey Down Arrow\nkey Right Arrow\nkey q\nkey y"
for tweet in tl:
	if tweet.strip() == "":
		continue
	n=n+1
	tweet=add+" "+tweet
	f1=open("tweetspeedx"+str(n),"w")
	f1.write("key Right Arrow")
	f1.write(first)
	for st in tweet:
		f1.write("\nkey ")
		if st == ' ':
			f1.write("<space>")
		else:
			f1.write(st)
	f1.write(last)
	f1.close()
	os.system("lynx -cfg=./lynx.cfg http://mobile.twitter.com -cmd_script=tweetspeedx"+str(n))
	print("Tweet Number: "+str(n))
	print("Tweeted: "+tweet)
	os.system("rm tweetspeedx"+str(n))
	tdel=randint(0,delay/2)
	op=randint(0,100)
	if op%2==0:
		tdel=delay-tdel
	else:
		tdel=delay+tdel
	print("Pausing For "+str(tdel/1000.0)+" Seconds!!!")
	time.sleep(tdel/1000.0)
print(str(n)+" Tweets Tweeted!!")
print("Task Completed !!!")
print("I am very Tired...\nPress Enter To Logout!!")
input()
f=open("logout","w")
f.write("# Command logfile created by Lynx 2.8.9rel.1 SpeedX\n# Arg0 = lynx\n# Arg1 = http://mobile.twitter.com/logout\n# Arg2 = -cmd_log=logout")
f.write("\nkey Right Arrow\nkey Right Arrow\nkey q\nkey y")
f.close()
os.system("lynx http://mobile.twitter.com/logout -cmd_script=logout")
os.system("bash greet")
exit()
