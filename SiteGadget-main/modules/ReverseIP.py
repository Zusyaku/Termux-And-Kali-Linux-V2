import re, requests, os.path
from bs4 import BeautifulSoup
from insides.Colors import Colors

def ReverseIP(site, _verbose=None):
	if _verbose != None:
		try:
			u = ("https://api.hackertarget.com/reverseiplookup/?q="+site)
			response = requests.get(u)
			html = response.content
			soup=BeautifulSoup(html,"html.parser")
			with open("ReverseIPLookup.txt","w") as file :
				file.write(str(soup))
			file.close()
			print("")
			print(f"{Colors.OKGREEN}ReverseIPLookup.txt saved!{Colors.ENDC}")
		except:
			print(f"{Colors.FAIL}Reverse IP Lookup Error!{Colors.ENDC}")