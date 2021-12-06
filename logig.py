import os,sys,time,requests,json
from time import sleep
def log_ig(user,pas):
    sleep(2)
    agent="Mozilla/5.0 (Linux; Android 9; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Mobile Safari/537.36"
    csrf=requests.get('https://www.instagram.com',headers={"user-agent":agent}).cookies["csrftoken"]
    sleep(2)
    log = requests.post('https://www.instagram.com/accounts/login/ajax/', headers={
                        'origin': 'https://www.instagram.com',
                        'pragma': 'no-cache',
                        'referer': 'https://www.instagram.com/accounts/login/',
                        'user-agent': agent,
                        'x-csrftoken': csrf,
                        'x-requested-with': 'XMLHttpRequest'
                        }, data={
                        'username': user,
                        'enc_password':f'#PWD_INSTAGRAM_BROWSER:0:{int(time.time())}:{pas}',
                        'queryParams': '{}',
                        'optIntoOneTap':'false',
                        'stopDeletionNonce':'',
                        'trustedDeviceRecords':'{}'
                        }).text
    if '"authenticated":true' in log:
       print({"Message":"Login success","success":True})
    elif "checkpoint_required" in log:
       print({"Message":"Account checkpoint","success":False})
    else:
       print({"Message":"Login failed","success":False})

if __name__=="__main__":
     os.system("clear")
     print("\t\033[1;97mLogin Instagram")
     print("\033[96m\t_______________\033[00m")
     username=input('\t\033[00mUsername : \033[96m')
     password=input('\t\033[00mPassword : \033[96m')
     print("\n")
     log_ig(username,password)
