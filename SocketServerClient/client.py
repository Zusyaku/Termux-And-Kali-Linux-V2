# GitHub : https://www.github.com/niirmaaltwaatii/SocketServerClient
# N11rm44L 7w44711

#!/bin/python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 87))

fmsg = ''

while True:
    msg = s.recv(8).decode("utf-8")
    if len(msg) <= 0 :
        break
    else :
        fmsg += msg
        continue

print(fmsg)
