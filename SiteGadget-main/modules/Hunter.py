from bs4 import BeautifulSoup
import json, requests
from insides.Colors import Colors

def Hunter(site,confHunter,_verbose=None):
	if _verbose != None:
		try:

			dmnlist = ["gmail.com","outlook.com","hotmail.com","yahoo.com","hotmail.co.uk","icloud.com," ,"google.com"]
			if (site in dmnlist):
				print(f"{bcolors.FAIL}Unacceptable domain : {bcolors.ENDC}"+site)
				print("")    
				print("-------------------------------")  
				print("")
			else:
				u = "https://api.hunter.io/v2/domain-search?domain="+site+"&api_key="+confHunter
				response = requests.get(u)
				html = response.content
				lp = json.loads(html)
				for i in range(0,50):
					print(lp['data']['emails'][i]['value'])
		except:
			pass
