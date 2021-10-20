from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.errors import SessionPasswordNeededError
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser

import getpass
import sys
import os
import json
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
        client.sign_in(password=getpass.getpass())


def select_channels(channels):
    
    ch_list=[]
    ch_name=[]
    ch_id=[]
    ch_info=[]
    index=None
    for i,g in enumerate(channels):
        print(str(i+1) + '- ' + g.title)
    while index!=-1:
        print("\n")
        index = int(input("Choose Channel(0 to finish): ").strip())        
        if index==0:
            if len(ch_list)==0:
                print("[+] Error No Channel Choosen")
                continue
            if len(ch_name)!=0:
                print("Groups Chosen: "+(", ".join(ch_name)))
            break
        index-=1
        ch_list.append(index)
        ch_name.append(channels[index].title)
        ch_id.append(channels[index].id)
    return ch_id

def make_config():
    chunk_size = 200
    channels_in=[]
    channels_admin=[]
    result = client(GetDialogsRequest(
                offset_date=None,
                offset_id=0,
                offset_peer=InputPeerEmpty(),
                limit=chunk_size,
                hash = 0
            ))
    
    for chat in result.chats:
        try:
            if chat.broadcast:
                channels_in.append(chat)
        except:
            continue
    channels_admin=channels_in
    print("Choose Channels To Forward Message From: ")
    ch_in_id=select_channels(channels_in)
    
    print("Choose Channels To Send Message To: ")
    ch_own_id=select_channels(channels_admin)
    
    data={"from":ch_in_id,"to":ch_own_id}
    with open("config.json","w") as config_out:
        json.dump(data,config_out)
    
    return data

if __name__=='__main__':
    make_config()