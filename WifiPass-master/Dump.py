#It will save passwords to txt file named "clear.txt"
#Author:D4Vinci
import os, re

#Get all saved wifi networks names
def get_wlans():
    data = os.popen("netsh wlan show profiles").read()
    wifi = re.compile("All User Profile\s*:.(.*)")
    return wifi.findall(data)

#Get a password for a network
def get_pass(network):
    try:
        wlan = os.popen("netsh wlan show profile "+str(network.replace(" ","*"))+" key=clear").read()
        pass_regex = re.compile("Key Content\s*:.(.*)")
        return pass_regex.search(wlan).group(1)
    except:
        return " "

f = open("clear.txt","w")
for wlan in get_wlans():
    f.write("\n-----------\n"+" SSID : "+wlan + "\n Password : " + get_pass(wlan))
f.close()
