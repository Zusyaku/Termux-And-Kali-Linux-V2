#!/bin/python3
from re import findall as reg
import requests

class scrap(object):
    def __init__(self):
        self.header = {'User-Agent':'Mozilla 50/'}
    def req_to(self,key,i,start):
        try:
            req = requests.get("https://www.google.com/search?ei=DnP9X_6ZA8H5rAGrloLgAg&safe=strict&yv=3&tbm=isch&q=" + key + "&vet=10ahUKEwiO58Pk-pTdAhXPdH0KHT60A24QuT0IMSgB.c_uHW87hBc_p9QO-6I7wBg.i&ved=0ahUKEwiO58Pk-pTdAhXPdH0KHT60A24QuT0IMSgB&ijn=" + i + "&start=" + start + "&asearch=ichunk&async=_id:rg_s,_pms:s,_fmt:pc",headers=self.header)
            if '</div>' in req.text:
                ambil = list(dict.fromkeys(self.grab(req.text)))
                for url in ambil:
                    print(url)
                    self.save(url,"result.txt")
            else:
                print("cant get text")
        except KeyboardInterrupt:
            print("Keyboard interrupt, exit")
            exit
        except ConnectionError:
            print("Connection Error")

    def grab(self,key):
        return reg('ou":"(.*?)","ow"', key)
    def save(self,url,filename):
        x = open(filename,"a+")
        x.write(url + "\n")
        x.close()
ll = input("Dork ? : ")
start = 0
for i in range(1,51):
    try:
        test = scrap()
        test.req_to(str(ll),str(i),str(start))
        start = start + 10
    except KeyboardInterrupt:
        print("keyword interrupt, exit")
        exit
