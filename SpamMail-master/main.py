import os,time,sys,shutil

class Main:

	def __init__(self):
		self.detekos()

	def menu(self):
		print("""
		;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		;     S P A M  E M A I L    ;
		;---------------------------;
		; Author : Kang-newbie      ;
		; Contact : t.me/kang_nuubi ;
		;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

1. Spam BPJS
2. Spam OLX
3. Spam Surveryon
4. Spam PricePrice
5. Spam Mediatek
""")
		pilih=int(input('/Kang-newbie: '))
		if pilih == 1:
			import src.mail
		elif pilih == 2:
			import src.olx
		elif pilih == 3:
			import src.spamemail
		elif pilih == 4:
			import src.price
		elif pilih == 5:
			import src.mediatek
		else: print("[!] lihat menu dong(o)");self.menu()

	def detekos(self):
		#remove cache
		try:
			shutil.rmtree("src/__pycache__")
		except: pass

		if os.name in ['nt','win32']:
			os.system('cls')
		else: os.system('clear')
		self.menu()

try:
	Main()
except KeyboardInterrupt:
	exit('[Exit] Key interrupt')
except Exception as F:
	print('Err: %s'%(F))
