# Tools Gak Guna Ini Buat Short Url / Pemendek Url
# Yang Beginian Juga Mau Di Rikod ? Memang Kontol Anda Ini

# Start : 01-04-2021 12:10 WIB
# Done  : 01-04-2021 12:25 WIB
# Create By : Kingtebe
# Only Python3

import requests as connection
import sys as snif, os
from time import sleep as date
try:
	import pyshorteners as cosmic
except ModuleNotFoundError:
	exit("\n [!] Module pyshorteners belum terinstall\n     Ketik : pip install pyshorteners\n")

hemkel_pro_2021 = lambda: print("""\n       ▄▀▄     ▄▀▄        ╭━━━━━━━━━━━━━━━╮\n      ▄█░░▀▀▀▀▀░░█▄       │ URL Shortener │\n  ▄▄  █░░░░░░░░░░░█  ▄▄ / ╰━━━━━━━━━━━━━━━╯\n █▄▄█─█░░▀░░┬░░▀░░█─█▄▄█\n\n  [ Author : Kingtebe ]""")

class Link:

	def __init__(self,link_url):
		self.link_url = link_url
		self._short_()

	def _short_(self):
		try:
			_link_na = cosmic.Shortener()
			_clckru_ = _link_na.clckru.short(self.link_url);hemkel_pro_2021();date(2.8)
			print("\n * Shortener Succses");date(1.8);print(" ✓ Result :",_clckru_,"\n")

		except connection.exceptions.ConnectionError:
			exit("\n [!] Jaringan Internet Lu Buriq Harap Periksa Kembali \n")

if __name__=='__main__':
	try:
		if len(snif.argv) < 2:
			hemkel_pro_2021()
			exit("\n [!] Usage: python short.py <Url>\n")
		else:
			Link(snif.argv[1])

	except IndexError:exit()
