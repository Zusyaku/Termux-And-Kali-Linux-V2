#Author:D4Vinci
#Squnity Developers 
import socket
our_log=open("Attackers_Data.txt","w") #Our text file to save attackers data in it

def ssh(msg="",listeners=2):
    welcome="""Welcome to BackBox Linux 4.5 (GNU/Linux 4.2.0-30-generic i686)\n
 * Documentation:  http://www.backbox.org/\n\n
The programs included with the BackBox/Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.\n
BackBox/Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.\n
    """
    s = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 22))#binding for the ssh port
    print "\nSSH Honeypot ready(Waiting For Attackers)..\n"
    s.listen(int(listeners))
    stat=0
    n=0
    rqs=["http","HTTP/1.0","GET","bind","version","OPTIONS"]
    while True:
        n+=1
        c,attacker= s.accept()
        port=attacker[1]
        ip=attacker[0]
        c.send("login as: ")
        login=c.recv(1024)
        c.send(login+"@host's password: ")
        a=c.recv(1024)
        PROMPT = login+"@host:~$"
        c.send(welcome)
        ips.append(ip)
        our_log.write("\n ["+str(n)+"] IP: "+str(ip)+"\tPort: "+str(port)+"\n")
        print "\n ["+str(n)+"] IP: "+str(ip)+"\tPort: "+str(port)+"\n"
        c.send(PROMPT)
        data = c.recv(1024)

        for rq in rqs:
            if rq in data.split(" ") or data.split(" ")=="" or data==" " :
                our_log.write(" ["+str(ip)+"] is Scanning us With nmap looking for service info.!"+"\n")
                print " ["+str(ip)+"] is Scanning us With nmap looking for service info.!"+"\n"
                if ip in ips:c.close()
                stat=1
                break

        if data.split(" ")[0] == "id":
            our_log.write(" ["+str(ip)+"][!]Command: "+str(data)+"\n")
            print " ["+str(ip)+"][!]Command: "+str(data)+"\n"
            c.send("\nuid=0(root) gid=0(root) groups=0(root)")
            our_log.write("  ["+str(ip)+"]>Output: uid=0(root) gid=0(root) groups=0(root)\n")
            print "  ["+str(ip)+"]>Output: uid=0(root) gid=0(root) groups=0(root)\n"
            c.send(str(msg)+'\n')
            stat=1
            c.close()

        elif data.split(" ")[0] == "uname":
            our_log.write(" ["+str(ip)+"]!]Command: "+str(data)+"\n")
            print " ["+str(ip)+"][!]Command: "+str(data)+"\n"
            c.send("\nLinux f001 3.13.3-7-high-octane-fueled #3000-LPG SMPx4 Fri Jun 31 25:24:23 UTC 2200 x86_64 x64_86 x13_37 GNU/Linux")
            our_log.write("  ["+str(ip)+"]>Output: Linux f001 3.13.3-7-high-octane-fueled #3000-LPG SMPx4 Fri Jun 31 25:24:23 UTC 2200 x86_64 x64_86 x13_37 GNU/Linux\n")
            print "  ["+str(ip)+"]>Output: Linux f001 3.13.3-7-high-octane-fueled #3000-LPG SMPx4 Fri Jun 31 25:24:23 UTC 2200 x86_64 x64_86 x13_37 GNU/Linux\n"
            c.send(str(msg)+'\n')
            stat=1
            c.close()

        elif stat==0:
            our_log.write("\t[!]Command: "+str(data)+"\n")
            print " ["+str(ip)+"][!]Command: "+str(data)+"\n"
            c.send("\n"+str(data.split(" ")[0]) + ": command not found")
            our_log.write("   ["+str(ip)+"]>Output: "+ data.split(" ")[0] + ": command not found\n")
            print "   ["+str(ip)+"]>Output: "+ data.split(" ")[0] + ": command not found\n"
            c.send(str(msg)+'\n')
            c.close()
        our_log.write("="*10)
        print "="*10

    our_log.close()

ssh()