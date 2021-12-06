import requests as req, json, time

tampung = []
hitung = 0

class Main(object):
	
	def __init__(self,url,token):
		self.url = url
		self.token = token
	def cek_account(self,id):
		try:
			__cek = json.loads(req.get(f"{self.url}/{id}?access_token={self.token}").text)
			nama = __cek['name']
			return nama
		except KeyError:
			return False

class Dump(Main):
	
	def pertemanan(self,id):
		global hitung
		if self.cek_account(id) == False:
			exit("[!] Ops.. Target tidak ditemukan.")
		else:
			print(f"[=] Nama target: {self.cek_account(id)}")
		try:
			__r=json.loads(req.get(f"{self.url}/{id}/friends?limit=5000&access_token={self.token}").text)
			for __data in __r['data']:
				nama = __data['name'].rsplit(" ")[0]
				id = __data['id']
				tampung.append(nama + "<=>" + id)
		except Exception as e:
			print(f"\n[!] Error: {e}")
		for b in range(len(tampung)):
			hitung+=1
			print(f"\r[!] Mengumpulkan {hitung} ID	",end="")
			time.sleep(0.001)
		print("")
		time.sleep(2)
		print(f"\n[=] Total id -> {len(tampung)}")
		if (len(tampung))==0:
			exit("[!] Ops! Jumlah id hanya terdapat 0.")
		else:
			return tampung
	
	def followers(self,id):
		global hitung
		if self.cek_account(id) == False:
			exit("[!] Ops... Target tidak ditemukan.")
		else:
			print(f"[=] Nama target: {self.cek_account(id)}")
		try:
			__r=json.loads(req.get(f"{self.url}/{id}/subscribers?limit=5000&access_token={self.token}").text)
			for __data in __r['data']:
				nama = __data['name']
				id = __data['id']
				tampung.append(nama + "<=>" + id)
		except Exception as e:
			print(f"\n[!] Error: {e}")
		for b in range(len(tampung)):
			hitung+=1
			print(f"\r[!] Mengumpulkan {hitung} ID	",end="")
			time.sleep(0.001)
		print("")
		time.sleep(2)
		print(f"\n[=] Total id -> {len(tampung)}")
		if (len(tampung))==0:
			exit("[!] Ops! Jumlah id hanya 0.")
		else:
			return tampung
	
