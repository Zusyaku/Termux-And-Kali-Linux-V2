import os,sys,requests,json,time
from time import sleep
def igsearch(nm):
    sleep(2)
    req=requests.get("https://www.instagram.com/web/search/topsearch/?query="+nm,headers={"user-agent":"Mozilla/5.0 (Linux; Android 10; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.186 Mobile Safari/537.36"}).text
    for x in json.loads(req)["users"]:
        username=x['user']['username']
        name=x['user']['full_name']
        print("\033[00m"+username+"\033[96m|\033[00m"+name)

if __name__=="__main__":
     os.system('clear')
     print("\t\033[1;97mGet Username IG From Search")
     print("\t\033[96m___________________________\033[00m")
     nm=input("\tQuery Name : \033[96m")
     print("\n")
     igsearch(nm)
