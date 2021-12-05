#Statistik Covid-19 Indonesia
# Official Blog : https://www.blog-gan.org 
##############################
import requests
from time import time as timer  
import time
from re import findall as reg
year = time.strftime('%d/%m/%y')

print('\033[33mStatistik Covid-19 Indonesia' + ' ' + year)

covid = requests.get('https://api.kawalcorona.com/indonesia/')
data = covid.json()
for corona in data:
	print('\033[31mNegara : ' +'\033[0m'+corona['name'])
	print('\033[37mPositif : ' +corona['positif'])
	print('\033[31mMeninggal : ' +corona['meninggal'])
	print('\033[32mSembuh : ' +corona['sembuh'])
	