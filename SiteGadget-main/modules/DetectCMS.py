import re ,requests, json
from bs4 import BeautifulSoup
from prettytable import PrettyTable
from insides.Colors import Colors

def DetectCMS(confCMS,site, _verbose=None):
	if _verbose != None:
		CMSapi_Status = ("https://whatcms.org/API/Status?key="+confCMS)
		CMSapi = ("https://whatcms.org/API/CMS?key="+confCMS+"&url="+site)
		try:
			response = requests.get(CMSapi_Status)
			js = response.content
			data = json.loads(js)
			print(f"{Colors.BOLD}API Credits = {Colors.ENDC}" +str(data['result']['period_remaining']))
			print("")
		except:
			print(f"{Colors.FAIL}API Error !{Colors.ENDC}")
			print("")
		try:
			response = requests.get(CMSapi)
			js = response.content
			data = json.loads(js)
			table = PrettyTable([("CMS : "+data['result']['name']),("Version : "+data['result']['version'])])
			table.add_row([('Confidence : '+data['result']['confidence']),('CMS URL : '+data['result']['cms_url'])])
			print(table)
		except:
			print(f"{Colors.FAIL}No Found CMS{Colors.ENDC}")