from colorama import Fore, Back, Style
import os
def clear():
		os.system('clear')
def ban():
		print(Fore.CYAN+"""
	_____ ___ ___ ___  _   __  __ 
       |_   _/ __/ __| _ \/_\ |  \/  |
	 | || (_ \__ \  _/ _ \| |\/| |
	 |_| \___|___/_|/_/ \_\_|  |_|
		 """)
clear()
ban()
print(Fore.CYAN + 'by @lamer112311' + Fore.WHITE + '   Channel: ' + Fore.RED + '@cyber_puffin' + Fore.BLUE)
print(Fore.BLUE + '------SPAM BOT BUILDER-----------------')
print('-------------------------------------------\n')
my_file = open('Tgspam.py', 'w', encoding='utf-8')

a = input(Fore.MAGENTA + "Введите токен бота: ")
my_file.write("""
import telebot
import time
from telebot import *
bot = telebot.TeleBot('""")
my_file.write(a)
my_file.write("""')
print('by @cyber_puffin')
print('БОТ ЗАПУЩЕН!')
s = input("Введите количество спам сообщений: ")
b = input("Введите текст спам сообщения: ")
s = int(s)  # parse string into an integer
print("За одну команду будет отправлено", s, "сообщений")
print("Текст собщения: ", b)
@bot.message_handler(commands=['developer'])
def start_message(message):
	bot.send_message(message.chat.id, "Разработчик бота: @lamer112311")

@bot.message_handler(commands=['""")
b = input(Fore.MAGENTA + "Введите команду, которая будет активировать спам: ")
my_file.write(b)
my_file.write("""'])
def start_message(message):
	for i in range(s):
		try:
			bot.send_message(message.chat.id, b)
			time.sleep(0.05)
			bot.forward_message(message.chat.id, message.chat.id, message.message_id + 1)
			print(i, "Цикл пройден!")
		except Exception as e:
			print("ERROR!")
bot.polling()
""")
my_file.close()
print(Fore.BLUE + "Файл успешно создан и сохранен!")


