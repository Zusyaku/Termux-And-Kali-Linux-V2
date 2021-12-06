import requests as req, re, argparse

print("""

  _________  _  ___   _________  ______
 / ___/ __ \/ |/ / | / / __/ _ \/_  __/
/ /__/ /_/ /    /| |/ / _// , _/ / /   
\___/\____/_/|_/ |___/___/_/|_| /_/    
	Coded By:  Latip176                         

""")

parser = argparse.ArgumentParser(description='Tools convert cookies to token.')
parser.add_argument('-cv','--convert',nargs="?",help='Untuk convert cookies ke token (python cv.py -cv "cookies facebook kamu")',type=str, default=max)
args = vars(parser.parse_args())

class Main:
	
	def __init__(self,cookie):
		self.cookie=cookie
	def getToken(self):
		headers = {'Host':'business.facebook.com','cache-control':'max-age=0','upgrade-insecure-requests':'1','user-agent':'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36','accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','content-type' : 'text/html; charset=utf-8','accept-encoding':'gzip, deflate','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cookie': self.cookie}
		try:
			_get=req.get("https://business.facebook.com/creatorstudio/home",headers=headers)
			__token=re.search('{"accessToken":"(EAA\w+)',_get.text).group(1)
			if "EAA" in __token:
				return {"token":__token}
			else:
				return {"token":"error"}
		except AttributeError:
			return {"token":"cookies invalid"}

if __name__=="__main__":
	try:
		__token=Main(args["convert"]).getToken().get("token")
		if "EAA" in __token:
			print("[✓] Convert berhasil\n[=] Token anda:",__token,"\n")
		else:
			print(__token)
	except:
		print("ketik 'python cv.py --help' untuk bantuan\n")