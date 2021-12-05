import requests
import json

banner = """ 
Translate ID To EN | Python Code

"""
print(banner)

TEXT = raw_input('Text Kamu :' )

header = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Cookie': '1P_JAR=2021-06-17-10; _ga=GA1.3.248365323.1624072747; _gid=GA1.3.1415912091.1624072747; NID=217=WeJhzSMlnDqS-8sPNfYJ7-NlgEIGgzCn03AFl3natmbyumZrolaHA12HW1NibTEBtGYHw7ydMjN3r4VggLbg50ksZk3GsGWB1mYPDYuQxAQegr4ciaKPnjzvus4rPdLaMSg_wq4L2NJ9gMdhryjjEAkAYymnTlWVAoMoRMgrUB4; OTZ=6029481_28_28__28_'}
url = "https://translate.google.com/translate_a/t?client=at&sc=1&v=2.0&sl=id&tl=en&hl=nl&ie=UTF-8&oe=UTF-8&text="+TEXT
req = requests.get(url,headers=header).json()
for gets in req['sentences']:
	print('Hasil : '+gets['trans'])
