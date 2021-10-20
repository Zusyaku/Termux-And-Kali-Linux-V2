# Mau Ngapain boss?
# Gw Bingung Buatnya tentunya yg rikod harus bingung juga

import sys, os, io, re, time, hashlib
try:
	import progressbar
except:
	os.system("easy_install progressbar2")
try:
	import requests, bs4
except ModuleNotFoundError:
	os.system("python3 -m pip install -r requirements.txt")

exec(
	open(
		".color"
			).read()
	)

Yurl = []
jin = []
os.system("xdg-open https://m.youtube.com/channel/UCPGGHZ0xutJPK06c5wrEwVw")
os.system(
		"clear"
	)
print(
		"# GET LICENSE: https://semawur.com/hh1ShgV9pD\n"
	)
kukis = input(
		"# License: "
		)
while kukis == "":
	kukis = input(
		"# License: "
		)
pw = hashlib.new(
	"md5"
	)
pw.update(
		kukis.encode(
			"utf-8"
		)
	)
cek = requests.get(
		"https://project-rizky.000webhostapp.com/vid-bok-database/data.php?pass="+pw.hexdigest()
		)
if cek.json()[
		"status"
		] == "Login Gagal":
	exit(
		"# License Tidak Valid\n"
		)
elif cek.json()[
		"status"
		] == "Login Succes":
	print(
		"# Login Sukses ✓"
		)
	time.sleep(
		2
			)
	Yurl.append(
		cek.json()[
				"url"
				]
			)
	jin.append(
		cek.json()[
				"join"
				]
			)

class Main:
	def __init__(
			self
				):
		self.cut = {
				"st":
					"/storage/emulated/0/"
				,
				"sd":
					"/sdcard/"
				}
		self.va1 = []
		self.va2 = []

	def Progres(
			self
		):
		progress = progressbar.ProgressBar(
			redirect_stdout=True,
				redirect_stderr=True,
			widgets=[
				progressbar.Percentage(),
				progressbar.Bar(),
				' (',progressbar.AdaptiveTransferSpeed(),
				' ',
				progressbar.ETA(),
			') '])
		return progress


	def Run(
		self,
			url
				):
		os.system(
				"clear"
			)
		exec(
			open(
				".banner"
			).read()
				)
		ged = bs4.BeautifulSoup(
					requests.get(
						url
					).text,
					"html.parser").find(
						"div", class_="videos-list"
			)
		for judul in ged.find_all(
					"span"
						):
			cek = re.findall(
					"<span>(.*?)</span>",
					str(judul))
			for jud in cek:
				self.va1.append(
					jud
				)

		for link in ged.find_all(
					"a"
					):
			self.va2.append(
						link.get(
					"href"
					)
				)

		for check in range(
					len(
			self.va1
				)
			):
			print(f"{p}[{h}"+str(check+1)+f"{p}] "+self.va1[
				check
				]
					)
		print(
			f"{m}÷"+"="*37+"÷"
			)
		pil = input(
				f"{p}[{h}•{p}] PILIH :{k} "
			)
		while pil in (""," "):
			print(
				f"{p}[{m}×{p}] Pilih Angka Yang Ada..\n"
			)
			pil = input(
				f"{p}[{h}•{p}] PILIH :{k} "
			)
		if (pil in (
				"N",
				"n"
				)
			):
			ce1 = bs4.BeautifulSoup(
				requests.get(
					url
				).text,
					"html.parser"
				).find(
					"a",
					class_="current"
				)
			ce2 = int(
				ce1.text
				) + 1
			if ce2 == 56:
				print(
					f"{p}[{m}~{p}] {p}Page Sudah Habis.."
				)
				input(
					f"\n{m}<!--[ {p}ENTER UNTUK KEHALAMAN AWAL {m}--!>"
				)
				Main().Run(
					''.join(Yurl)
				)
			else:
				Main().Run(
					''.join(Yurl)+"/page/"+str(
				ce2)
					)
		elif (pil in (
				"I",
				"i"
				)
			):
			os.system(
				"clear"
			)
			exec(
				open(
					"info/__init__.py").read()
			)
		elif (pil in (
				"J",
				"j"
				)
			):
			os.system(
				"xdg-open "+''.join(jin)
				)
			Main().Run(
				''.join(Yurl)
			)
		else:
			try: cek = str(
				self.va2[int(pil
					) - 1]
				)
			except IndexError: exit(
					f"{p}[{m}×{p}] Pilih Yang Benar..\n"
				)
			out = input(
					f"{p}[{h}•{p}] OUTPUT: {k}"
				).replace(
					" ",
					"_"
				)
			cek1 = bs4.BeautifulSoup(
					requests.get(
				cek
					).text,
				"html.parser"
				).find(
					"div",
				class_="responsive-player"
					).find(
				"iframe"
					)
			cek2 = bs4.BeautifulSoup(
					requests.get(
				cek1.get("src")
					).text,
				"html.parser"
				).find(
					"source"
					)[
					"src"
					]
			self.Download(
					out,
					cek2
						)

	def Download(
			self,
				out,
					cek2
			):
		print(f"{p}[{k}={p}] Tunggu Sebentar..")
		sv  = io.open(
				"Results/"+out+".mp4",
					"wb"
				)
		get_konten = requests.get(
				cek2,
					stream=True
				)
		total = int(
				get_konten.headers.get(
				'content-length'
			))
		load = self.Progres(
					)
		load.start(
				total
					)
		read = 0
		for num in get_konten.iter_content(
				chunk_size=1024
				):
			if num:
				read += len(
						num
					)
				load.update(
					read
				)
				sv.write(
						num
					)
				sv.flush(
					)
		load.finish(
				)
		print(
			f"{m}÷"+"="*37+"÷"
			)
		print(
			f"{p}[{h}✓{p}] Video Berhasil Di Download.."
			)
		print(
			f"{p}[{h}={p}] Result:{k} Results/"+out+".mp4"
			)
		print(
			f"{m}÷"+"="*37+"÷"
			)
		print(
			f"{p}[{m}?{p}] Mau Dipindahkan Kemana?\n    {m}> {k}ST{p}[{h}/storage/emulated/0/{p}]\n    {m}> {k}SD{p}[{h}/sdcard/{p}]"
			)
		mana = input(
				f"{p}[{h}?{p}] PILIH:{k} "
				)
		os.system("mv -f Results/"+out+".mp4"+" "+self.cut[mana.lower()])
		exit(f"{p}[{h}✓{p}] Tersimpan:{k} "+self.cut[mana.lower()]+out+".mp4")

if __name__=="__main__":
	try:
		os.mkdir(
			"Results"
		)
	except:
		pass
	try:
		Main().Run(
			''.join(
			Yurl
			)
		)
	except Exception as st:
		exit(
			f"{p}[{m}×{p}] ERROR:{m} {str(st)}"
			)
