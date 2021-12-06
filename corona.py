from urllib import request
import json
import pyfiglet

print('Api corona Provinsi by OmenDev And indonesia-covid-19 :>')

pyfiglet = pyfiglet.figlet_format('OmenLatip')
print(pyfiglet)
print('Youtube  :   Omen Craft')
print('Github   :   https://github.com/Latip176')
print('\nList Corona Provinsi:\n')
print('Tunggu Loading...')

url = "https://indonesia-covid-19.mathdro.id/api/provinsi"
response = request.urlopen(url)

data = json.loads(response.read())

for covid in data['data']:
  print(f"- {covid['provinsi']}")
  print(f" Positif: {covid['kasusPosi']}")
  print(f" Sembuh: {covid['kasusSemb']}")
  print(f" Meninggal: {covid['kasusMeni']}")
print('\nFinisihed Jika Data Indonesia Eror Maklumin\n')