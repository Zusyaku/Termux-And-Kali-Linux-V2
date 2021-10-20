import colorama
import random, os
from colorama import init, Fore, Back, Style

init(autoreset=True)
# colors foreground text:
fc = Fore.CYAN
fg = Fore.GREEN
fw = Fore.WHITE
fr = Fore.RED
fb = Fore.BLUE
flb = Fore.LIGHTBLUE_EX
fbl = Fore.BLACK
fy = Fore.YELLOW
fm = Fore.MAGENTA

def banner():
    os.system('clear')
    banner = fg + '''
          _______  _______  _______ 
|\     /|(  ____ \(  ____ \(  ____ \

| )   ( || (    \/| (    \/| (    \/
| |   | || |      | (__    | (__    
| | B | || |  A   |  __) B |  __) A 
| |   | || |      | (      | (      
| (___) || (____/\| (____/\| )      
(_______)(_______/(_______/|/       
 \n      UDEMY COURSE ENROLLER FUCKER
──────────────────────────────────────────────────
▸ AUTHOR     : MEHEDI HASAN ARIYAN
▸ FACEBOOK   : FACEBOOK.COM/THEMEHTAN
▸ YOUTUBE    : YOUTUBE.COM/MASTERTRICK1
▸ GITHUB     : GITHUB.COM/BOTOLMEHEDI
──────────────────────────────────────────────────\n\n'''

    bad_colors = ['BLACK', 'WHITE', 'LIGHTBLACK_EX', 'RESET']
    codes = vars(colorama.Fore)
    colors = [codes[color] for color in codes if color not in bad_colors]
    colored_chars = [char for char in banner]

    return ''.join(colored_chars)
