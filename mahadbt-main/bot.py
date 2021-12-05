from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import time as t
import os as s 
from response import *



t.sleep(2)
print("Bot has been started")
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('bye',b))
updater.dispatcher.add_handler(CommandHandler('chatbot',chat))
updater.dispatcher.add_handler(CommandHandler('start',start))
updater.start_polling()
updater.idle()
port = int(os.environ["0.0.0.0"])



