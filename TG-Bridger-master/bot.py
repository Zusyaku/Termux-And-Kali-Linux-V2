from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError
from telethon.errors.rpcerrorlist import PeerFloodError
import json
import os
import re
import sys
import asyncio
from dotenv import load_dotenv

load_dotenv()

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
phone =  os.getenv("PHONE")
client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)    
    try:
        client.sign_in(phone,code=input('Enter code: '))
    except SessionPasswordNeededError:
        print("Enter Cloud Password: ",end='')
        client.sign_in(password=getpass.getpass())

bridge_from=[]
bridge_to=[]
try:
    data = json.load(open("config.json"))
except Exception as err:
    print("Error: "+str(err))
    print("Make Sure To Build Config First.")
    sys.exit()
bridge_from=data['from']
bridge_to=data['to']

def filter(text):
    if re.search(r"[0-9]{10}",text):
        return text

@client.on(events.NewMessage(chats=bridge_from))
async def handler(event):
    try:
        datestamp=datetime.now().strftime('%Y_%m_%d')
        timestamp=datetime.now().strftime('%Y_%m_%d-%H_%M_%S')
        print("Received Message ", event.raw_text)
        message=filter(event.raw_text)
        if not message:
            return
        with open("logs_{}.txt".format(datestamp) ,'a', encoding='utf8') as f:
            f.write('[{}] : '.format(timestamp)+message+"\n")
        for tid in bridge_to:
            await client.send_message(tid, message,link_preview=False)
    except PeerFloodError:
        print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")

print(
"""
            Made With ❤️ By
███████╗██████╗ ███████╗███████╗██████╗ ██╗  ██╗
██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗╚██╗██╔╝
███████╗██████╔╝█████╗  █████╗  ██║  ██║ ╚███╔╝ 
╚════██║██╔═══╝ ██╔══╝  ██╔══╝  ██║  ██║ ██╔██╗ 
███████║██║     ███████╗███████╗██████╔╝██╔╝ ██╗
╚══════╝╚═╝     ╚══════╝╚══════╝╚═════╝ ╚═╝  ╚═╝
""")


with client:
    client.run_until_disconnected()
