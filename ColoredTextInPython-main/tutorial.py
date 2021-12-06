import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print(Fore.RED + 'some red text')
print(Back.CYAN + 'cyan')
print(Style.BRIGHT + "BRIGHT")
print(Fore.RED + Back.GREEN + "red text on green back")

'''
Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL
'''