import os
os.system("clear")
## importing socket module
import socket
print("\033[1;34;40m FindMyIp tool made by AnonyminHack5\n")
print("\033[1;36;40m THIS TOOL IS SPECIALLY MADE FOR GETTING IP OF HOST USER IF YOU DONT KNOW YOUR IP\n\n\n\n")
print("""\033[1;35;40m
_____  __ ___  __  ___    _  ___
     | ___ || ||  \ |  || __ \ | ||    \
     | |___ | ||   \|  |||  | \| || |__|
     | ____|| ||  |\   |||__| || || |
     |_|    |_||__| \__||___ / |_||_|
        ======>[Ip Finder Tool made by: AnonyminHack5]=====>
""")
## getting the hostname by socket.gethostname() method
hostname = socket.gethostname()
## getting the IP address using socket.gethostbyname() method
ip_address = socket.gethostbyname(hostname)
## printing the hostname and ip_address
print(f"\033[1;33;40m Your Hostname is: {hostname}")
print(f"\033[1;32;40m Your IP Address: {ip_address}")