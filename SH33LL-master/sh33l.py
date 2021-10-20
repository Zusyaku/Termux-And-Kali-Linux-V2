import requests,sys
from multiprocessing.pool import ThreadPool
W = '\033[1;37m' # White bold
N  = '\033[0m'  # white (Normal)
R = '\033[31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
terget=""
num=0
nums=""
def one(args):
	global terget,num,nums
	try:
		r=requests.get(terget+"/"+args).status_code
		if r ==200:
			print(G+"\r(+) "+terget+"/"+args+"                        ")
			open("result.txt","a+").write(terget+"/"+args+"\n")
		else:
			num+=1
			print("\r%s(+)%s scanning %s/%s"%(R,N,num,nums)),;sys.stdout.flush()
	except:pass
		
print W+R+"""
[+]
 |  ___  _   _  ___  ___  __   
 | / __)( )_( )(__ )(__ )(  )  
 | \__ \ ) _ (  (_ \ (_ \ )(__ 
 | (___/(_) (_)(___/(___/(____) v.2"""
print W+R+" |\n[+]"+W+" Tittle   : "+O+"WebShell Scanner\n"+W+R+"[+]"+W+" Coded By : "+O+"Deray"
print W+R+"[+]"+W+" Github   :"+O+" https://github.com/LOoLzeC"
print W+R+"[+]"+W+" Pastebin :"+O+" https://pastebin.com/u/LOoLzeC"
print W+R+"[+]___________________________________________[+]"
print W+"\n[+]=="+R+" Menu :"
print W+B+"\n  1"+R+")"+W+" Default Scan With Ur Random Targets"
print W+B+"  2"+R+")"+W+" Manual With Your Webshell List"
print W+B+"  3"+R+")"+W+" Info"
print W+B+"  4"+R+")"+W+" Exit."
menu=raw_input(W+'\n[+]=='+R+' Menu>>'+W+' ')
if "1" in menu:
	terget=raw_input(R+"[?]"+W+" Target Uri>> ")
	p=ThreadPool(input("[?] ThreadPool: "))
	if requests.get(terget+"/wp-content/").status_code ==200:
		print(G+"(+) Wordpress Detected."+N)
		print(G+"(+) Output: result.txt"+N)
		y=open("wordlist/wplist.txt").read().splitlines()
		nums=len(y)
		p.map(one,y)
	else:
		print(G+"(+) Output: result.txt"+N)
		y=open("wordlist/randomlist.txt").read().splitlines()
		nums=len(y)
		p.map(one,y)
elif "2" in menu:
	terget=raw_input(R+"[?]"+W+" Target Uri>> ")
	y=open(raw_input("[?] webshell list: ")).read().splitlines()
	nums=len(y)
	p=ThreadPool(input("[?] ThreadPool: "))
	p.map(one,y)
elif "3" in menu:
	print("""
	Coded By Deray
	https://facebook.com/achmad.luthfi.hadi.3
	""")
elif "4" in menu:
	exit("[*] Bye")

