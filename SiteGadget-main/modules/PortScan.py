import requests
from bs4 import BeautifulSoup
from insides.Colors import Colors

def PortScan(getip, _verbose=None):
	if _verbose != None:
		try:
			u = ("https://api.hackertarget.com/nmap/?q="+getip)
			response = requests.get(u)
			report = response.content
			soup = BeautifulSoup(report, 'html.parser')
			print(str(soup))
		except:
			print(f"{Colors.FAIL}Port Scan Error!{Colors.ENDC}")