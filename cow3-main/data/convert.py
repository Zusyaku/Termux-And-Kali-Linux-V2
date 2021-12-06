import requests as req, re

"""

Copyright © 2021 - 2023 | Latip176
Semua codingan dibuat oleh Latip176.

"""

class Main:
	
	def __init__(self,cookie):
		self.cookie=cookie
	def getToken(self):
		headers = {'Host':'business.facebook.com','cache-control':'max-age=0','upgrade-insecure-requests':'1','user-agent':'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36','accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','content-type' : 'text/html; charset=utf-8','accept-encoding':'gzip, deflate','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cookie': self.cookie}
		try:
			_get=req.get("https://business.facebook.com/creatorstudio/home",headers=headers)
			__token=re.search('\{\"accessToken\"\:\"(EAA\w+)\"',str(_get)).group(1)
			if "EAA" in __token:
				return __token
			else:
				return "Cookies Invalid"
		except AttributeError:
			return "Cookies Invalid"