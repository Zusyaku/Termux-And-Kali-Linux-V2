import requests, random, os, sys

class Croper:
	def __init__(self,key):
		self.head={'X-Api-Key': key}

	def cropbg(self, imgfile, bg_color):
		req=requests.post('https://api.remove.bg/v1.0/removebg',
			files={'image_file': open(imgfile, 'rb')},
			data={'size': 'auto', 'bg_color':bg_color},
			headers=self.head,
			)

		if req.status_code == requests.codes.ok:
			rana=random.randrange(99999)
			with open(str(rana)+'-rmbg.png', 'wb') as out:
				out.write(req.content)
			print(f"\n\033[92msuccess: {rana}-rmbg.png\033[0m")
		else:
			print(f"\n\033[91mError: {req.status_code} {req.text}\033[0m")

	def cropbgurl(self, imgurl, bg_color):
		req=requests.post('https://api.remove.bg/v1.0/removebg',
			data={'image_url':imgurl, 'size': 'auto', 'bg_color':bg_color},
			headers=self.head,
			)

		if req.status_code == requests.codes.ok:
			rana=random.randrange(99999)
			with open(str(rana)+'-rmbg.png', 'wb') as out:
				out.write(req.content)
			print(f"\n\033[92msuccess: {rana}-rmbg.png\033[0m")
		else:
			print(f"\n\033[91mError: {req.status_code} {req.text}\033[0m")

try:
	
	os.system('clear')
	print("""
	# BACKGROUND CROPER #
	 ~ By Kang-Newbie ~
	""")

	imgna=input("Masukan lokasi foto atau url foto: ")
	bgcol=input("\n[info] (ex: red, blue) atau juga bisa menggunakan RGB code (ex: 81d4fa, fff) atau kosongkan untuk bg transparan\nWarna background: ")
	if not bgcol:
		bgcol=None

	crop=Croper('cD5ogD7V12dLAdkSfutJcHgT')
	if 'http://' in imgna or 'https://' in imgna:
		crop.cropbgurl(imgna, bgcol)
	else:
		crop.cropbg(imgna, bgcol)

except KeyboardInterrupt:
	sys.exit("EXIT: KEY INTERRUPT")
except Exception as Err:
	sys.exit(f"\n{Err}")
