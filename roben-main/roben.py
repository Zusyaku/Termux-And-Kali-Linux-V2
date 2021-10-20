#!/usr/bin/env python3

import requests
from sys import argv, exit
from bs4 import BeautifulSoup
import argparse
import validators

script, url = argv

#variables area
__author__ = "@nickvourd"
__version__ = "1.0.2"
__license__ = "GPLv3"
__team__ = "@twelvesec"
__thanks__ = [ '@maldevel', 'servo' ]
bannerL = "========["
bannerR = "]========"
cutter_list = []

ascii_art = '''
___________              .__                _________              
\__    ___/_  _  __ ____ |  |___  __ ____  /   _____/ ____   ____  
  |    |  \ \/ \/ // __ \|  |\  \/ // __ \ \_____  \_/ __ \_/ ___\ 
  |    |   \     /\  ___/|  |_\   /\  ___/ /        \  ___/\  \___ 
  |____|    \/\_/  \___  >____/\_/  \___  >_______  /\___  >\___  >
                       \/               \/        \/     \/     \/ 
Robots Entries v.{} - Robots entries parser & brute forcer tool.
Robots Entries is an open source tool licensed under {}.
Written by: {} of {}.
Special thanks to {} & {}.
https://www.twelvesec.com/
Please visit https://github.com/twelvesec/roben for more..
'''.format(__version__, __license__, __author__, __team__, __thanks__[0], __thanks__[1])


#classes area
class Bcolors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    OKCYAN = '\033[00m'


#check_input function
def check_input(url, bold, fail, endc):
    if not validators.url(url):
        print(bold + fail + "[!] Url validation [FAILED]\n" + endc)
        exit()
    else:
        flag = "TRUE"

    return flag


#check_file function
def check_file(url):
    flag = "FALSE"

    if "robots.txt" in url:
        flag = "TRUE"
        
    return flag


#create_url function
def create_url(flag, url):
    final_url = url 
    if flag == "FALSE":
        url2 = url + " "
        for i in range(len(url2)):
            if url2[i] == ' ':
                if url2[i-1] == "/":
                    final_url = url + "robots.txt"
                else:
                    final_url = url + "/robots.txt" 

    return final_url


#main function
def main():
    
    #call objects of the class
    bcolor = Bcolors()

    print(bcolor.BOLD + bcolor.WARNING + ascii_art + bcolor.ENDC)

    #call check_input function
    flag = check_input(argv[1], bcolor.BOLD, bcolor.FAIL, bcolor.ENDC)

    print(bcolor.BOLD + bcolor.OKBLUE + bannerL + "Url Checks" + bannerR + "\n" + bcolor.ENDC)
    
    if flag == "TRUE":
        print(bcolor.BOLD + bcolor.OKGREEN + "[+] Url validation [OK]" + bcolor.ENDC)

    #call check_file function
    flag2 = check_file(argv[1])
    
    #call create_url function
    url = create_url(flag2, argv[1])

    print(bcolor.BOLD + bcolor.OKGREEN + "[+] String format [OK]" + bcolor.ENDC)

    r = requests.get(url)
    
    if r.status_code == 200:
        print(bcolor.BOLD + bcolor.OKGREEN + "[+] Robots file exists [OK]\n" + bcolor.ENDC)
        print(bcolor.BOLD + bcolor.OKBLUE + bannerL + "Robots File Content" + bannerR + "\n" + bcolor.ENDC)

        list = r.text
        print(list + "\n")

        #save content of robots.txt to a file
        with open('robots.dump.txt', 'w') as f:
             f.write(list)
             f.close

        print(bcolor.BOLD + bcolor.OKGREEN + "[*] Robots.txt file saved to robots.dump.txt" + bcolor.ENDC)

        #copy file output to a list
        with open('robots.dump.txt', 'r') as f:
            for line in f:
                if 'Disallow:' in line:
                    cutter = line.split(":")[1]
                    cutter_list.append(cutter)

        #delete empty lines
        trim_list = " ".join(cutter_list).split()
        
        print(bcolor.BOLD + bcolor.OKBLUE + "\n" + bannerL + "Responses of Robots file entries" + bannerR + "\n" + bcolor.ENDC)
        
        #create a file to save responses outputs
        with open('responses.dump.txt', 'w') as f:
            f.write("\n[+] Robots.txt responses:\n\n")
            f.close
        
        for z in trim_list:
            url = url.replace("/robots.txt","")
            newurl = url + z
            r2 = requests.get(newurl)
            if r2.status_code == 200:
                color = bcolor.OKGREEN
            elif r2.status_code == 301 or r2.status_code == 302:
                color = bcolor.OKCYAN
            else:
                color = bcolor.FAIL

            print(bcolor.BOLD + bcolor.OKBLUE + "[~] " + bcolor.BOLD + bcolor.WARNING + newurl + bcolor.BOLD + bcolor.OKBLUE + " -> " + bcolor.BOLD + color + str(r2.status_code) + bcolor.ENDC)
            
            #append responses to the output file
            with open('responses.dump.txt', 'a') as f:
                f.write("[*] " + newurl + " -> " + str(r2.status_code) + "\n")
                f.close
        
        print(bcolor.BOLD + bcolor.OKGREEN + "\n\n[*] All responses saved to responses.dump.txt\n" + bcolor.ENDC)
        print(bcolor.BOLD + bcolor.OKBLUE + "===================================================" + bcolor.ENDC)
    else:
        print(bcolor.BOLD + bcolor.FAIL + "[!] Robots.txt file doesn't exists [FAILED]\n" + bcolor.ENDC)
        exit()


if __name__ == "__main__":
    main()