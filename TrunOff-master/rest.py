import os, sys, time

os.system('clear')
try:
	print("\n[1] Restart Hp")
	print("[2] Shutdown Hp")
	ask=input("[!] Masukan Pilihan Anda: ")
	if ask == '1':
		os.system('clear')
		print("[!] Wait 5 second")
		time.sleep(5)
		os.system('/system/bin/reboot')

	elif ask == '2':
		os.system('clear')
		print("[!] Wait 5 second")
		time.sleep(5)
		os.system('/system/bin/reboot -p')
	else:
		print("[!] Anda Salah Memasukan Nomor\n")
except:
	print("[!] Error")
