# GitHub : https://www.github.com/niirmaaltwaatii/SocketServercClient
# N11rm44L 7w44711

#!/bin/python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 87))
s.listen(8)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} established !");
    clientsocket.send(bytes("Welocme to the server !", "utf-8"))
    clientsocket.close()
