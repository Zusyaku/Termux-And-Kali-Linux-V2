#Note : use lowercase when using it 
#gunakan Huruf kecil saat menggunakannya
#Example : blog-gan.org 
#if you run : Blog-gan.org => Error
import requests

print(
	
	"""\033[0m Alexa Rank Checker """
)

Domain = raw_input('Domain ~:# ')

Alexa = requests.get('https://whoisdog.com/tool/domain-alexa-checker/index.php?action=alexa&d='+Domain).text

print(Domain+' : '+ '\033[32m'+Alexa )