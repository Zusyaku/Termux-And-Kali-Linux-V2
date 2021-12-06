import os,time,requests,re
from time import sleep
id=[]
def search(url):
    global id
    sleep(2)
    req=requests.get(url).text
    usr=re.findall(r'<td class="bz ca"><a href="(.*?)"><div class="cb"><div class="cc">(.*?)</div></div>',req)
    for user in usr:
        username=user[0].replace("/","")
        if 'profile' in username:
            id.append(username.replace("profile.php?id=","")+"|"+user[1])
        else:
            id.append(username+"|"+user[1])
    if "Lihat Hasil Selanjutnya" in req:
        url=re.findall(r'<div class="l m" id="see_more_pager"><a href="(.*?)">',req)[0]
        search(url)
    return id  
if __name__=="__main__":  
    os.system("clear")
    print("\t\033[1;97mGet Username FB From Public")
    print("\t\033[96m___________________________\033[00m")
    nm=input("\t\033[00mQuery Name : \033[96m")
    print("\n")
    username=search("https://mbasic.facebook.com/public/"+nm)
    for user in username:
        user=user.split("|")
        print("\033[00m"+user[0]+"\033[96m|\033[00m"+user[1])

