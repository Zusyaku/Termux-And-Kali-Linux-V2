#JametKNTLS - h0d3_g4n - Moslem - Kiddenta - Naskleng45
#Created By : Jenderal92@Shin403
banner = """ 
Mass Delete HTTP | Jamet Crew
"""
print banner

def http(url):
	try:
		htt = (url)
		x = htt.replace('http://', '').replace('https://', '')
		open('delhttp.txt','a').write(x+'\n'); print('Deleted http' + ' '+url)
	except: pass


site = raw_input('List Site : ')
ht = open(site, 'r').readlines()
for i in ht:
	try:
		siten = i.strip()
		data=http(siten)
	except: pass