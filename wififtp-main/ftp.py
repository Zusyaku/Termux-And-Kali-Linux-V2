import os,sys,socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(10)
try:
	s.connect(("8.8.8.8", 80))
	ip=s.getsockname()[0]
	if ((ip.find("192") != -1) | (ip.find("172") != -1)):
	    pass
	else:
	    print("You are not using any local network!\nPlease connect to a hotspot or router/Wi-Fi!")
	    exit()
except socket.error:
    print("No internet")
    exit()
s.close()
portno=input("Enter the port no:(Press enter to keep default 8000)\n")

if (portno==""):
    print("Port supported!")
else:
    try:
        portno=int(portno)
        if (portno>1023 & portno<65536):
            print("Port supported")
        else:
            print("Port not allowed!Range 1024-65535")
            exit()
    except:
        print("Port must be a number!")
        exit()
path=input("Enter the path:(Press enter to keep default current path)\n")
if (os.path.exists(path) | (path=="")):
    print("Path supported!")
else:
    print("Path error!")
    exit()
    
alltext='''from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("user", "12345","/sdcard", perm="elradfmw")
authorizer.add_anonymous("/sdcard", perm="elradfmw")

handler = FTPHandler
handler.authorizer = authorizer

try:
	server = FTPServer(("0.0.0.0", 8000), handler)
	server.serve_forever()
except:
	print("Error! Change port or restart terminal!")'''

def replacer(alltext,portno, path):
    portno=str(portno)
    alltext1=alltext.replace("8000", portno)
    alltext2=alltext1.replace("/sdcard", path, 2)
    os.system("rm -rf .ftptemp")
    opr=open(".ftptemp", 'a')
    opr.write(alltext2)
    opr.close()
    os.system("clear")
    os.system("figlet WiFi-FTP")
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(10)
    s.connect(("8.8.8.8", 80))
    ip=s.getsockname()[0]
    print("Your FTP link is:\nftp://"+ip+":"+portno)
    os.system("python3 .ftptemp")
    
while True:
    if ((portno=="") & (path=="")):
        portno="8000"
        path=os.getcwd()
        replacer(alltext,portno,path)
        break
    if ((portno!="") & (path=="")):
        path=os.getcwd()
        replacer(alltext,portno,path)
        break
    if ((portno=="") & (path!="")):
        portno="8000"
        replacer(alltext,portno,path)
        break
    if ((portno!="") & (path!="")):
        replacer(alltext,portno,path)
