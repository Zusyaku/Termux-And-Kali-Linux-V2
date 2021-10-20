# Awokawokawokawok Ngentod Mau Apa ? Hm, Boleh Lah
# Start : 26-03-2021 07:22
# Done  : 26-03-2021 13:23
# Only Python3
# Coded : Kingtebe

from telethon.errors import FloodWaitError
from telethon.errors import SessionPasswordNeededError as awokawokawokmengontol
from telethon import TelegramClient, sync, events
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
from bs4 import BeautifulSoup as bs
import os,sys,re,json,time as waktu
from random import choice

red = '\x1b[1;31m'
yellow = '\x1b[1;33m'
green = '\x1b[32m'
blue = '\x1b[1;34m'
purple = '\x1b[1;95m'
cyan = '\x1b[1;36m'
black = '\x1b[1;30m'
white = '\x1b[1;37m'

try:
	import requests
except ModuleNotFoundError:
	exit(f"\n {white}[{purple}!{white}] Module requests not installed\n     {white}Ketik {black}: {yellow}pip install requests{white}\n")

List_User_Agent = [
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.83 Safari/537.1",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
]

ngentod_hemkel = lambda : print(f"\n {cyan}╔╦╗┌─┐┬  ┌─┐┌┐ ┌─┐┌┬┐    {purple}╦ ╔╦╗╔═╗\n {cyan} ║ ├┤ │  ├┤ ├┴┐│ │ │ {white}─── {purple}║  ║ ║\n {cyan} ╩ └─┘┴─┘└─┘└─┘└─┘ ┴     {purple}╩═╝╩ ╚═╝\n{white}====================================\n {white}[{purple}•{white}] Coded By {black}: {white}Kingtebe\n {white}[{purple}•{white}] Youtube  {black}: {white}FaaL TV\n {white}[{purple}•{white}] Github   {black}: {white}github.com/Kingtebe\n")
aing_gans = lambda : os.system('clear')

class tunggu(object):

	def __init__(self,x):
		sys.stdout.write("\r")
		sys.stdout.write("                                                               ")
		for remaining in range(x, 0, -1):
			sys.stdout.write("\r")
			sys.stdout.write("  \x1b[93m•\x1b[92m{:2d} \x1b[97mSeconds Remaining ".format(remaining));sys.stdout.flush();waktu.sleep(1)

class LTC:

	def __init__(self,phone_number):
		self.req = requests.Session()
		self.ua = {"User-Agent":choice(List_User_Agent)}
		self.home = "https://dogeclick.com/reward"
		self.api = 800812
		self.hash = "db55ad67a98df35667ca788b97f771f5"
		self.phone_number = phone_number
		self.Nuyul()

	def Nuyul(self):
		if not os.path.exists("session"):
			os.makedirs("session")
		client = TelegramClient("session/"+ self.phone_number, self.api, self.hash )
		client.connect()
		if not client.is_user_authorized():
			try:
				client.send_code_request(self.phone_number);aing_gans();waktu.sleep(1.2);ngentod_hemkel();print(f"{white}  Note {black}: {yellow}Script Telebot-LTC V.1, Use It Wisely !\n")
				me = client.sign_in(self.phone_number, input(f" {white}[{cyan}+{white}] Code Telegram {black}: {white}"));waktu.sleep(3)
			except awokawokawokmengontol:
				pwd = input(" \x1b[97m[\x1b[95m!\x1b[97m] Input Password \x1b[90m: \x1b[97m")
				me = client.start(self.phone_number, pwd)
		myself = client.get_me()
		print(f" {white}[{cyan}+{white}] Nama User  {black}: {cyan}",myself.first_name);waktu.sleep(3);print(f" {white}[{cyan}+{white}] {white}Phone User {black}: {cyan}"+ self.phone_number );waktu.sleep(2.9)

		print(f"\n {white}[{purple}!{white}] Start Mining {black}...");waktu.sleep(2.9)
		try:
			channel_entity=client.get_entity("@Litecoin_click_bot")
			channel_username="@Litecoin_click_bot"
			while True:
				sys.stdout.write("\r");sys.stdout.write("                                                              ");sys.stdout.write("\r")
				sys.stdout.write(f"  {yellow}• {white}Try Get Url ");sys.stdout.flush()
				client.send_message(entity=channel_entity,message="🖥 Visit sites");waktu.sleep(3)
				posts = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
				if posts.messages[0].message.find("  {cyan}! {white}Sorry, there are no new ads available") != -1:
					print(f"\n {white}[{purple}!{white}] Iklan Sudah Habis Silahkan Coba Lagi Besok\n")
					client.send_message(entity=channel_entity,message="💰 Balance");waktu.sleep(5)
					posts = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
					message = posts.messages[0].message
					print(message)
					exit()
				else:
					try:
						url = posts.messages[0].reply_markup.rows[0].buttons[0].url
						sys.stdout.write("\r")
						sys.stdout.write(f"  {yellow}•{white} Visit {black}: {yellow}"+url);sys.stdout.flush()
						id = posts.messages[0].id
						aing = self.req.get(url, headers=self.ua, timeout=15, allow_redirects=True)
						kntl = bs(aing.content,"html.parser")
						if kntl.find("div",class_="g-recaptcha") is None and kntl.find('div', id="headbar") is None:
							waktu.sleep(2)
							posts = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
							message = posts.messages[0].message
							if posts.messages[0].message.find("You must stay") != -1 or posts.messages[0].message.find("Please stay on") != -1:
								exnx = re.findall( r'([\d.]*\d+)', message)
								tunggu(int(exnx[0]))
								waktu.sleep(1)
								posts = client(GetHistoryRequest(peer=channel_entity,limit=2,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
								messageres = posts.messages[1].message
								waktu.sleep(2)
								sys.stdout.write(f"\r  {cyan}$ {green}"+messageres+"\n")
							else:
							     pass

						elif kntl.find('div', id="headbar") is not None:
							for dat in kntl.find_all('div',class_="container-fluid"):
								code = dat.get('data-code')
								timer = dat.get('data-timer')
								tokena = dat.get('data-token')
								tunggu(int(timer))
								aing = self.req.post(self.home,data={"code":code,"token":tokena}, headers=self.ua, timeout=15, allow_redirects=True)
								meki = json.loads(aing.text)
								sys.stdout.write(f"\r  {cyan}$ {green}You earned "+meki['reward']+" LTC for visiting a site!\n")

						else:
							sys.stdout.write("\r");sys.stdout.write("                                                                ");sys.stdout.write("\r")
							sys.stdout.write(f"  {purple}! {white}Captcha Detected")
							sys.stdout.flush();waktu.sleep(2)
							client(GetBotCallbackAnswerRequest(channel_username,id,data=posts.messages[0].reply_markup.rows[1].buttons[1].data))
							sys.stdout.write(f"\r  {yellow}• {white}Skip Captcha {yellow}!       \n");waktu.sleep(2)
					except:
						waktu.sleep(3)
						posts = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
						message = posts.messages[0].message
						if posts.messages[0].message.find(f"  {purple}• {white}You must stay") != -1 or posts.messages[0].message.find("Please stay on") != -1:
							exnx = re.findall( r'([\d.]*\d+)', message)
							tunggu(int(exnx[0]))
							waktu.sleep(1)
							posts = client(GetHistoryRequest(peer=channel_entity,limit=2,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
							messageres = posts.messages[1].message
							waktu.sleep(2)
							sys.stdout.write(f"\r  {cyan}$ {green}"+messageres+"\n")
						else:
						     pass
		finally:
			client.disconnect()

if __name__=='__main__':
	if len(sys.argv) < 2:
		exit(f"\n {white}[{purple}!{white}] {white}Usage\x1b[93m: {white}python bot.py <Number_Telegram> \n")
	else:
		LTC(sys.argv[1])
