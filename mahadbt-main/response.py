from turtle import update
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import time as t
updater = Updater('1849563775:AAGGX0GCema6OelGZprpu6AdwjzyoWfeULQ')

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def b(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Bye ahmed ,Take care of yourselevs")
    


def chat(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('hello Ahmed , Its mantasha over here')
    t.sleep(10)
    update.message.reply_text("I hope you're doing well without me ")
    t.sleep(10)
    update.message.reply_text(" Yeah the world is really confusing but we should stay with foucsed on our golas ")
    update.message.reply_text(" We should listen to our parent and we should wear nice clothes  ")

def start(update:Update,content: CallbackContext) -> None:
    t.sleep(5)
    update.message.reply_text("this Bot is Currently In development phase ")
    t.sleep(5)
    update.message.reply_text("Soon this Bot will be functional")

