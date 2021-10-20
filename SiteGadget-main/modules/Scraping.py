import re ,requests
from bs4 import BeautifulSoup
from insides.Colors import Colors

def Scraping(site, _verbose=None):
	if _verbose != None:
		try:
			u = ("https://"+site)
			response = requests.get(u)
			html = response.content
			soup=BeautifulSoup(html,"html.parser")
			rgx = str(soup)
			urls = re.findall('(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})', rgx)
			
			with open("ScrapingTheLinks.txt","w") as file :
				file.write(str(urls))
			file.close()
			print("")
			print(f"{Colors.OKGREEN}ScrapingTheLinks.txt saved!{Colors.ENDC}")
		except:
			print("")
			print(f"{Colors.FAIL}Scraping Data Error!{Colors.ENDC}")