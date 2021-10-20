import requests,sys,os
from bs4 import BeautifulSoup as Bs

class MedDown:
	def __init__(self):
		try:
			os.mkdir('result')
		except:
			pass
		self.req=requests.Session()
		self.req.headers.update({'referer':'http://twittervideodownloader.com','user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'})
		self.u='http://twittervideodownloader.com{}'

	def grap(self,lnk):
		title=[]
		linku=[]
		bs1=Bs(self.req.get(self.u.format('')).text,'html.parser')
		token=bs1.find('input',{'name':'csrfmiddlewaretoken'})
		res=self.req.post(self.u.format('/download'),data={'tweet':lnk,
			'csrfmiddlewaretoken':token['value']})
		bs2=Bs(res.text,'html.parser')
		for a in bs2.find_all('a',{'class':'expanded button small float-right'}):
			linku.append(a['href'])
		for b in bs2.find_all('b'):
			title.append(b.text)
		return (linku,title)

	def dl(self,link,judul):
		print(f"\n[Downloading] {judul}")
		with open('result/('+judul[:20]+'...).mp4',"wb") as f:
			response=requests.get(link, stream=True)
			total_length=response.headers.get('content-length')
			if total_length is None:
				sys.exit("[Err] Failed download videos")
			else:
				dlw=0
				total_length=int(total_length)
				for data in response.iter_content(chunk_size=4096):
					ges=int(100*dlw/total_length)
					dlw+=len(data)
					f.write(data)
					done=int(30*dlw/total_length)
					print(end=f"\r\033[97m[\033[92m{'>'*done}\033[91m{'='*(30-done)}\033[97m] \033[96m{ges+1}% ",flush=True)
		sys.exit(f"\n\033[0m\n[+] Success downloaded '{judul}'\n[!] File saved in folder 'result'")


os.system('clear')
print("""
#########################################
#	[Twitter Video Downloader]	#
#	     [By KANG-NEWBIE]		#
#########################################
""")
tw=MedDown()
linkna=input("[?] Link tweetnya: ")
lk=tw.grap(linkna)
while True:
	try:
		print("""
	[Resolution]
#1. 720p
#2. 480p
#3. 240p
""")
		pilih=int(input("[?] Pilih: "))
		if pilih == 1:
			tw.dl(lk[0][0],lk[1][2])
		elif pilih == 2:
			tw.dl(lk[0][2],lk[1][2])
		elif pilih == 3:
			tw.dl(lk[0][1],lk[1][2])
		else:
			print("[!] Lihat menu dong(o)")
	except KeyboardInterrupt:
		sys.exit("\nGoodbye...")
