import os

def Dos():
	if os.name in ['nt','win32']:
		os.system('cls')
	else: os.system('clear')