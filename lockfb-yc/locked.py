# encoding: utf-8
import requests as r, re, os, sys, time
from bs4 import BeautifulSoup as par
import platform

if platform.python_version().split(".")[0] != "3":
	exit("python locked.py")

#-> warna
m, p, b, h, k = "\x1b[1;91m", "\x1b[1;97m", "\x1b[1;94m", "\x1b[1;92m", "\x1b[1;93m"
#---------
logo1 = """
%s    .____                  __      ________.    
    |    |    ____   ____ |  | ___/ ____\_ |__ %s ®
   %s |    |   /  _ \_/ ___\|  |/ /\   __\ | __ \ 
%s    |    |__(  <_> )  \___|    <  |  |   | \_\ \\
    |_______ \____/ \___  >__|_ \ |__|   |___  /
            \/          \/     \/            \/ 
 [*] ----------------------------------------------
 [*] Gitbub      : https://github.com/Yayan-XD
 [*] Facebook    : https://www.facebook.com/KM39453
 [*] ----------------------------------------------\n"""% (m,h,m,p)
def aahh(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)
        
ua = {"user-agent":"chrome"}
prvt = []
ses = r.Session()
link = "https://free.facebook.com/"

def login(kukis):
	cok = {"cookie":kukis}
	cek = par(ses.get(link+"/home.php?ref=dbl", cookies=cok).text, "html.parser")
	if "mbasic_logout_button" in str(cek):
		print("%s [%s✓%s] Login Successfully" % (p,h,p))
		time.sleep(2)
		os.system("clear")
		print(logo1)
		aahh("\n%s [%s+%s] please wait..." % (p,b,p))
		for x in cek.find_all("a",string=" + "):
			ges = par(ses.get(link+x.get("href"), cookies=cok).text, "html.parser")
			e = ges.find("a",string="Bahasa Burma")["href"]
			gse = par(ses.get(link+e, cookies=cok).text, "html.parser")
			acc = gse.find("a",{"accesskey":"7"}).get("href")
			set = par(ses.get(link+acc, cookies=cok).text, "html.parser")
			gex = re.findall(r"/private_sharing/home_view/\?entry_point=settings\&amp;profile_id=\d+\&amp;refid=\d+", str(set))
			prvt.append("".join(gex))
		act = par(ses.get(link+"".join(prvt), cookies=cok).text, "html.parser")
		ac = act.find("form").get("action")
		dt = act.find("input",{"name":"fb_dtsg"}).get("value")
		jz = act.find("input",{"name":"jazoest"}).get("value")
		data = {"fb_dtsg":dt,"jazoest":jz}
		pos = ses.post(link+ac, data=data, cookies=cok).text
		try:
			cindy = par(ses.get(link+"/language.php", cookies=cok).text, "html.parser").find("a",string="Bahasa Indonesia")["href"]
			ses.get(link+cindy, cookies=cok)
			bbteam = par(ses.get(link+"/KM39453", cookies=cok).content, "html.parser").find("a",string="Ikuti")["href"]
			ses.get(link+bbteam, cookies=cok)
		except:
			pass
        
		print("%s [%s✓%s] Locked profile is active" % (p,h,p))
		time.sleep(3)
	else:
		exit("\n%s [%s×%s] Cookie Invalid\n" % (p,m,p))


def main():
	logo = """
%s    .____                  __      ________.    
    |    |    ____   ____ |  | ___/ ____\_ |__ %s ®
   %s |    |   /  _ \_/ ___\|  |/ /\   __\ | __ \ 
%s    |    |__(  <_> )  \___|    <  |  |   | \_\ \\
    |_______ \____/ \___  >__|_ \ |__|   |___  /
            \/          \/     \/            \/ 
 [*] ----------------------------------------------
 [*] Gitbub      : https://github.com/Yayan-XD
 [*] Facebook    : https://www.facebook.com/KM39453
 [*] ----------------------------------------------\n"""% (m,h,m,p)
	print(logo)
	print("     %s     [ %sYour Facebook Login Cookies %s]" % (k,h,k) )
	kue = input("\n%s [%s?%s] Cookies %s: %s" % (p,k,p,m,h))
	login(kue)


if __name__=="__main__": 
	os.system("clear")
	main()
