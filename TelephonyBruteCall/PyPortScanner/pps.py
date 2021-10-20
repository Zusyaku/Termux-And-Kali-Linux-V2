#!/usr/bin/python3
# N11rm44L 7w44711
# GitHub : https://www.github.com/niirmaaltwaatii/PyPortScanner

import funcs

dl = "-" * 70
banner = f"""
{dl}
    PyTool  : PyPortScanner
    Version : 1.0.0
    Author  : Niirmaal Twaatii
    GitHub  : https://www.github.com/niirmaaltwaatii/PyPortScanner
{dl}
"""

options = f"""
[ShortCommand] [Details] (Command)
    [0] Scan Specific Port (sp)
    [1] FTP scan (ftp)
    [2] SSH Scan (ssh)
    [3] HTTP Scan (http)
    [] Exit (exit)
"""

print(banner)
print(options)

while True :
    inp = input("[PPS]=> ").lower()
    if inp == "0" or inp == "sp" :
        funcs.sscan()
    elif inp == "1" or inp == "ftp" :
        funcs.fscan(21)
    elif inp == "2" or inp == "ssh" :
        funcs.fscan(22)
    elif inp == "3" or inp == "http":
        funcs.fscan(80)
    elif inp == "exit" :
        break
    else :
        print("invalid command !!!")
        continue


