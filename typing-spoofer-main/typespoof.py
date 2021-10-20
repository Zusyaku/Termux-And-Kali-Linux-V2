import requests
from colorama import Fore, init
import os
init(convert=True)

intro = f"""
                            {Fore.RED}Made by REZIZT. {Fore.CYAN}Zwietracht nacheinander ausnutzen
                                        {Fore.BLUE}https://discord.gg/XgpXMWk2bG
{Fore.RED}                ▄▄▄█████▓▓██   ██▓ ██▓███  ▓█████   ██████  ██▓███   ▒█████   ▒█████    █████▒  
{Fore.RED}                ▓  ██▒ ▓▒ ▒██  ██▒▓██░  ██▒▓█   ▀ ▒██    ▒ ▓██░  ██▒▒██▒  ██▒▒██▒  ██▒▓██   ▒ 
{Fore.RED}                ▒ ▓██░ ▒░  ▒██ ██░▓██░ ██▓▒▒███   ░ ▓██▄   ▓██░ ██▓▒▒██░  ██▒▒██░  ██▒▒████ ░ 
{Fore.RED}                ░ ▓██▓ ░   ░ ▐██▓░▒██▄█▓▒ ▒▒▓█  ▄   ▒   ██▒▒██▄█▓▒ ▒▒██   ██░▒██   ██░░▓█▒  ░ 
{Fore.RED}                  ▒██▒ ░   ░ ██▒▓░▒██▒ ░  ░░▒████▒▒██████▒▒▒██▒ ░  ░░ ████▓▒░░ ████▓▒░░▒█░    
{Fore.RED}                  ▒ ░░      ██▒▒▒ ▒▓▒░ ░  ░░░ ▒░ ░▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒ ░    
{Fore.RED}                    ░     ▓██ ░▒░ ░▒ ░      ░ ░  ░░ ░▒  ░ ░░▒ ░       ░ ▒ ▒░   ░ ▒ ▒░  ░      
{Fore.RED}                  ░       ▒ ▒ ░░  ░░          ░   ░  ░  ░  ░░       ░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░    
{Fore.RED}                          ░ ░                 ░  ░      ░               ░ ░      ░ ░          
{Fore.RED}                          ░ ░                                                                
{Fore.CYAN}                      ███▄,                              ,╓╖╓,
{Fore.CYAN}                     ╙█████░▒▄'                      ▄███▒▓▓╣╣╢╗
{Fore.CYAN}                        ▀▀█████▄,:                  ▐█████████▓▓▓▄
{Fore.CYAN}                            ` █▓░  █╖               ████████▓▄▓▀██
{Fore.CYAN}                              '██▄▄█▓▒╗,             ███████▀▀▀██▀
{Fore.CYAN}                                ▀█████▓▒╢╖            ▀██▄▄░░░░sT
{Fore.CYAN}                                  ██████▓╬╢╖          └███░░░░░─
{Fore.CYAN}                                   ▀█████▓╣╣▒╣         ███▄µ▒░░
{Fore.CYAN}                                     ▀████▓▓▓▓╫┐       ,██▀▀
{Fore.CYAN}                                       ████▓▓█▓▌@▓▒▓▒▄@▓█▓µ▌\  ┌╖
{Fore.CYAN}                                        ▐███████▓▓▓▓▓▒▄▌╢╢╣▀▒ ,░░░▒▒∩,,
{Fore.CYAN}                                         ▀███████▓█▓▓╩▒▀█▄▒▒▒▄▒░░░|░▒░░]▒
{Fore.CYAN}                                            ▀████████▓▓▓▒▀███Ñ▓▒░▒░░░░░▒▒▒
{Fore.CYAN}                                             ░`▀██████▓▓▓@▒███▒▒▒▒▀▒¢g▄╢▒░
{Fore.CYAN}                                                ▐█████▓▓▓▓╣▓▒██▌▒▒▒▒▒▒▐███▄
{Fore.CYAN}                                               ░ ██████▓▓▓▓▌Ñ▓▓▀██▄▒╢¼████æ▄
{Fore.CYAN}                                                 ▀███████▓███▓▓▓▓█░░░░▀▀▀▀██▄
{Fore.CYAN}                                                ╒█████████▓██▓▓▓▓█▒▒▒▒▒▒▒▒▒░░▄
{Fore.CYAN}                                               ,▓█╣▓██▓▓███████▓▓█▒▒▒╢╢▒▒▒▒▒▒░
{Fore.CYAN}                                              ▄▓█▓▄▓███▓█████████████▄▒╢▓╣▓▓╜
{Fore.CYAN}                                             ▐████▓▓██▓▓▓▓▒▒╢╣╣▒▒▒▀█▀█-└▀▀
                                          {Fore.RED}https://exploiting-{Fore.CYAN}discord-for.fun
                                                 {Fore.RED}http://rezizt{Fore.CYAN}.xyz             
                                            
                                                [{Fore.RED}>{Fore.RESET}]{Fore.CYAN}1{Fore.RESET} Typing spoof
                                            
"""

def type():
    print(f'[{Fore.RED}>{Fore.RESET}] Your token', end=''); token = str(input('  :  '))
    print(f'[{Fore.RED}>{Fore.RESET}] Channel id', end=''); channel = str(input('  :  '))
    headers = {'Authorization': token}
    print('started typing...')
    while True:    
        requests.post(f'https://discordapp.com/api/v6/channels/{channel}/typing', headers=headers)




def startMenu():
    print(intro)
    print(f'[{Fore.RED}>{Fore.RESET}] Your choice', end=''); choice = str(input('  :  '))
    if choice == '1':
       os.system('cls')
       type()

if __name__ == '__main__':
    startMenu()
