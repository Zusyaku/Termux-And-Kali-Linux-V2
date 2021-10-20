import os,re

def cat():
	data = []
	for i in ['device_name','manufacturer','model_name','model_number','serial_number','device_type']:
		data.append(re.search(i+'=(.+)',open('/data/misc/wifi/wpa_supplicant.conf','r').read()).group(1))
	print(f'''
+++ \033[92mDevice Informations\033[0m +++

Device Name  : {data[0]}
Manufacturer : {data[1]}
Model Name   : {data[2]}
Model Number : {data[3]}
Serial Number: {data[4]}
Devive Type  : {data[5]}
''')
	print('+++ \033[92mWifi Cache List\033[0m +++\n')
	x  = open('/data/misc/wifi/wpa_supplicant.conf','r').read()
	for i in x.split('network')[1:]:
		ssid = re.search(r'ssid=([\W].+)',i)
		psk  = re.search(r'psk=(.+)',i)
		if psk != None:
			psk = psk.group(1).replace('"','')
		else:
			psk = '-'
		if ssid != None:
			ssid = ssid.group(1).replace('"','')
		else:
			ssid = '-'
		print(f'* \033[90m{ssid} \033[0m:: {psk}')

def privcek():
	if os.geteuid() != 0:
		print("you aren't root user")
	else:
		cat()
if __name__=='__main__':
	os.system('clear')
	print('''
        SHOW WIFI CACHE
        karjok Pangesty
\033[92m,-'"`-._,-'"`-._,-'"`-._,-'\033[0m
''')
	privcek()
	