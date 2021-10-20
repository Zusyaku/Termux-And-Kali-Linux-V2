#!/usr/bin/python
########-NGAPAI GAN MAU RECODE YA?-################################
#######-YAUDAH SILAHKAN TAPI INGAT KATA PEPATAH "BANGSAD KAO"-####

import time, sys, threading, os, urllib, httplib, json
from os import system

def menu():
		print "\033[1;91m"
                print """+============================================+
| Created by KANG NEWBIE { t.me/kang_nuubi } |
| note: Jika terjadi error hubungi author    |
+============================================+"""
	       	print "\033[1;93mMenu Pilihan: "
                print "1. Bio data"
                print "2. Tahun Kabisat"
		print "3. Nembak Cewek"
		print "4. Ternak LELE"
		print "5. Menghitung Saldo"
		print "6. Perkiraan Cuaca"
		print "7. Mencari Bilanga Prima"
		print "8. Membuat List Pegawai"
		print "9. Kuis Sosial Media"
		print "10. Install bot Caping"
		print "11. Install bot NewsCat"
		print "12. Install bot Kubik"
		print "13. Install OSIF"
		print "14. Install Spam Sms"
		print "15. Install Hammer"
		print "16. Install Lite ddos"
		print "17. Install Tools Lazymux"
		print "18. Install Metasploit"
		print "19. Install APKDOWNLOADER"
		print "20. Install Spam Email"
		print "21. Install Gps Tracking"
		print "22. Install Tools Cek Gempa Terkini"
		print "23. Install Bot Chastree"
		print "24. Install Tools Weeman/Phising"
		print "25. Install Hunner Framework"
		print "26. Install Sqlmap"
		print "27. Install IpGeoLocation"
		print "28. Install Admin Panel Finder"
		print "29. Install Hakku Framework"
		print "30. Install Red Hawk"
		print "31. Install Mpsyt"
		print "32. Install webdav"
		print "33. Install SYTD"
		print "34. Install Xerxes"
		print "35. Install Torshammer"
		print "36. Install Mail-Generator"
		print "37. Install LiteOTP"
		print "38. Install XAttacker"
		print "39. Install Facebook Video Downloader"
		print "40. Install Tools Th3inspector"
		print "41. Install IP-Tracer"
		print "42. Install KaliNethunter"
		print "43. Install Termux Alpine"
		print "44. Install Smsid"
		print "45. Install Instagram Downloader"
		print "46. Install Spam Call"
		print "47. "
		print "99. Update "
		print "100. About"
		print "0. KELUAR"

def biodata () :
	        print
		print "\033[1;94mSELAMAT DATANG DI PROGRAM BIODATA"
		print "\033[1;92m========================================================"
		print "\033[1;91m*KETIKAN DENGAN HURUF KAPITAL SAJA!"
		print "*tolong isi dengan baik dan benar semua data-data anda!"
		print "*jika anda mengalami kesulitan bertanyalah."
		print
		nama_lengkap = raw_input("\033[93mNama Lengkap: ")
		umur = raw_input("Umur: ")
		jenis_kelamin = raw_input("Jenis Kelamin: ")
		tempat_tanggal_lahir = raw_input("Tempat/tanggal lahir: ")
		alamat = raw_input("Alamat: ")
		agama = raw_input("Agama: ")
		tinggi_badan = raw_input("Tinggi badan: ")
		riwayat_penyakit = raw_input("Riwayat penyakit: ")
		hobi = raw_input("Hobi: ")
		sekolah = raw_input("Sekolah: ")

		teks = "\nNama Lengkap: {}\nUmur: {}\nJenis Kelamin: {}\nTempat/tanggal lahir: {}\nAlamat: {}\nAgama: {}\nTinggi badan: {}\nRiwayat penyakit: {}\nHobi: {}\nSekolah: {}\n-----------------".format(nama_lengkap, umur, jenis_kelamin, tempat_tanggal_lahir, alamat, agama, tinggi_badan, riwayat_penyakit, hobi, sekolah)
		file_bio = open("biodata.txt", "a")
		file_bio.write(teks)
		file_bio.close()
		print "\033[91mNOTE: semua data anda telah dimasukan ke file 'biodata.txt'.\n terima kasih :)"
		print

def tahunkabisat () :
	tahun = input("\033[1;92mInput tahun: ")

	if (tahun % 4) == 0:
	    if (tahun % 100) == 0:
        	if (tahun % 400) == 0:
	            print "-Tahun Tersebut Tahun Kabisat"
		    print
        	else:
	            print "-Tahun Tersebut Bukan Tahun Kabisat"
		    print
	    else:
        	print "-Tahun Tersebut Tahun Kabisat"
		print
	else:
	    print "-Tahun Tersebut Bukan Tahun Kabisat"
	    print

def nembakcewek ():
	def utama():
	    print "\033[1;92mMaukah ente menjadi istriku ?"
	    print "1 = Mau"
	    print "2 = Tidak Mau"
	    dipilih = raw_input("Pilih Nomor ( 1 / 2 ) : ")
	    if dipilih == "1":
	        print '"Aku berjanji akan cinta sampai mati sama kamu :* "'
	    elif dipilih == "2":
	        print '"Yahh jomblo lagi deh"'
	    else :
	        print "Pilihannya Cuma 1 Sama 2 Doang tong -_- "
	    ulangi()
	def ulangi():
	    dicobalagi = raw_input("Coba lagi ? [Y/T] : ")
	    if dicobalagi.lower() == "y":
        	utama()
	    elif dicobalagi.lower() == "t":
        	sys.exit("Dadah :)")
	    else :
        	print "Pilihannya Cuma Y dan T Doang tong -_- "
	        ulangi()
	utama()

def lele():
	print
	nama = raw_input("Siapa nama mu? ")
	jumlah_lele = int(input("Hai " + nama + " Berapa jumlah ikan lele yang kamu punya di kolam? "))
	print "Ikan lele mu di kolam :", jumlah_lele, "ekor"
	kasih_makan = int(input("Berapa kali Anda memberi pakan setiap harinya? "))

# Kondisi
	if kasih_makan == 2:
		print "Jadwal pakan Anda :", kasih_makan, "kali perhari."
		print "Anda mengatur jadwal pakan yang tepat."
		print
	elif kasih_makan < 2:
		print "Jadwal pakan Anda :", kasih_makan, "kali perhari."
		print "Anda mengatur jadwal pakan yang kurang tepat."
		print
	elif kasih_makan > 2:
		print "Jadwal pakan Anda :", kasih_makan, "kali perhari."
		print "Anda memberikan pakan terlalu berlebihan."
		print
	elif kasih_makan == 0:
		print "Jadwal pakan Anda :", kasih_makan, "kali perhari."
		print "Maaf ikan lele Anda mati."
		print

def saldo ():
	print ("")
	print ("\033[1;92m------ PROGRAM PYTHON UNTUK MENGHITUNG SALDO ------")
	print ("")
	print ("by : KANG NEWBIE")
	print ("")

	tabungan = int(input("Masukkan jumlah tabungan :"))
	lama = int(input("Masukkan jumlah lama menabung (bulan) :"))

	if tabungan < 1000000 :
	 sukuBunga = 0.03
	 saldoAkhir = (tabungan * sukuBunga) * lama + tabungan
	 print("")
	 print("Karena tabungan anda dibawah 1.000.000,\nbunga yang anda dapatkan 3%")
	 print("Saldo anda selama " + str (lama) + " bulan, adalah " +str (saldoAkhir))
	 print("")

	elif tabungan > 1000000 :
	 sukuBunga = 0.04
	 saldoAkhir = (tabungan * sukuBunga) * lama + tabungan
	 print("")
	 print("Karena tabungan anda diatas 1.000.000,\nbunga yang anda dapatkan 4%")
	 print("Saldo anda selama " + str (lama) + " bulan, adalah " +str (saldoAkhir))
	 print("")

def cuaca():
	print
	kota= raw_input("\033[1;92mMasukkan Nama Kota : ")
	conn = httplib.HTTPSConnection("api.openweathermap.org")
	conn.request("GET", "/data/2.5/forecast?q="+kota.lower()+",id&mode=json&appid=503186110e24edea8f99643135fd77cc")

	res = conn.getresponse()
	data = json.loads(res.read())
	for a in range (len(data['list'])):
	    print "==============================================="
	    print "Tanggal",data['list'][a]['dt_txt']

	    for b in range(len(data['list'][a]['weather'])):
	        print "Nama kota ", kota
	        print "Cuaca",data['list'][a]['weather'][b]['main']
	        print  "Suhu ",int(data['list'][a]['main']['temp'])-273
	        print "Kecepatan angin ",data['list'][a]['wind']['speed']
	    print "==============================================="

def prima():
	def is_prime(num):
		if num < 2:
			return False
		for prime in range(2, num):
			if num % prime == 0:
				return False
		return True

	def find_primes(max_num):
		primes = []
		for prime in range(0, max_num):
			if is_prime(prime):
				primes.append(prime)

		total_primes = str(len(primes))
		largest_prime = str(primes[-1])
		smallest_prime = str(primes[0])
		print('\n[+] total bilangan prima 1 s/d %s : %s' % (max_num, total_primes))
		print('[+] bilangan prima terbesar : %s' % (largest_prime))
		print('[+] bilangan prima terkecil : %s\n' % (smallest_prime))

		x = 0
		while x < len(primes):
			for value in primes:
				x = x + 1
				print(str(x)+' Yaitu : '+str(value))

	if __name__ == '__main__':
		print("")
		max = int(raw_input('[*] masukan nilai max : '))
		find_primes(max)

def pegawai():
	stop = False
	pegawai = [ ]
	def tambah():

		stop = False
		i = 0

	#Mengisi Array
		while(not stop):
			pegawai_baru = raw_input("Inputkan nama pegawai yang ke-{}: ".format(i+1))
			pegawai.append(pegawai_baru)
		# methode append menambahkan list/item dari belakang 
		# Increment 1
			i += 1

			tanya = raw_input("Mau isi lagi ? (y/t): ")
			if(tanya == "t"):
				kembali()
	def lihat():
	# Cetak Semua Pegawai
		print "\n"
		print "=" * 100
		print "Kamu memiliki {} pegawai" .format(len(pegawai))
		for hb in pegawai:
			print "- {}" .format(hb)
		print "\n"
		pilih = raw_input("mau kembali ke menu ? (y/t): ")
		if(pilih == "y"):
			kembali()
		else:
			lihat()
	#fungsi len digunakan untuk mengambil panjang list

	def kembali():
		print "*" * 100
		print "1. Tambah Data Pegawai \n"
		print "2. Lihat Data Pegawai \n"
		print "3. Hapus Data Pegawai \n"
		print "4. Exit \n"

		pilih = input("Masukkan Pilihan (1/2/3/4)  = ")
		if(pilih == 1):
			tambah()
		elif(pilih == 2) :
			lihat()
		elif(pilih == 3):
			hapus()
		elif(pilih == 4):
			stop = True
		else:
			stop = True
	def hapus():
		a = 0
		print "Kamu memiliki {} pegawai" .format(len(pegawai))
		for hb in pegawai:
			print "- {}" .format(hb)
		print "\n"
		a = input("hapus data pegawai yang ke - ")
		del pegawai[a-1]
		print "Data Pegawai telah dihapus "
		kembali()

	kembali()
	
def kuis_sosmed():
	from random import randint

	count = 0
 

	Soal = ["Social Media buatan Mark zuck...? ",
     			"Social Media yang eksis dengan awake sleep? ",
     			"Microblogging yang gambar burung apa hayo? ",
     			"Social Media yang populer dengan photo?",
     			"Social Media yang logonya hampir sama dengan Path  ",
     			"Social Media buat pekerja itu namanya: ",
     			"Planet Python di Indonesia itu hanya: "]
	Jawab = ["facebook",
    	 			"path",
     				"twitter",
     				"instagram",
     				"pinterest",
     				"linkedin",
     				"planpin"]
     
	link = ["http://www.facebook.com",
            	"http://Path.com",
            	"http://twitter.com",
            	"http://Instagram.com",
            	"http://Pinterest.com",
           	 "http://linkedin.com",
            	"http://planet.python.or.id/"]

	i = randint(0, 7)
	answer = raw_input("Pertanyaan 1 : " + Soal[i])
	if answer.lower() == Jawab[i]: 
    		print "Yeee Benar"
    		count = count + 1
	else: 
    		print "Yaah Salah \nJawaban Benar : " + Jawab[i]
    		print "Pengen Coba? Kunjungi : " + link[i]


	i = randint(0, 7) 
	answer = raw_input("\nPertanyaan 2 : " + Soal[i])
	if answer.lower() == Jawab[i]:
    		print "Yee Benar"
    		count = count + 1
	else:
    		print "Yaah Salah \nJawaban Benar : " + Jawab[i]
    		print "Pengen Coba? Kunjungi : " + link[i]

	i = randint(0, 7)
	answer = raw_input("\nPertanyaan 3 : " + Soal[i])
	if answer.lower() == Jawab[i]:
    		print "Yee Benar"
    		count = count + 1
	else:
    		print "Yahh Salah \nJawaban Benar : " + Jawab[i]
    		print "Pengen Coba? Kunjungi : " + link[i]

	i = randint(0, 7) 
	answer = raw_input("\nPertanyaan 4 : " + Soal[i])
	if answer.lower() == Jawab[i]:
    		print "Yee Benar"
    		count = count + 1
	else:
    		print "Yahh Salah \nJawaban Benar : " + Jawab[i]
    		print "Pengen Coba? Kunjungi : " + link[i]

	i = randint(0, 7)
	answer = raw_input("\nPertanyaan 5 : " + Soal[i])
	if answer.lower() == Jawab[i]:
    		print "Yee Benar"
    		count = count + 1
	else:
    		print "Yahh Salah \nJawaban Benar : " + Jawab[i]
    		print "Pengen Coba? Kunjungi : " + link[i]

	i = randint(0, 7) 
	answer = raw_input("\nPertanyaan 6 : " + Soal[i])
	if answer.lower() == Jawab[i]:
    		print "Yee Benar"
    		count = count + 1
	else:
    		print "Yahh Salah \nJawaban Benar : " + Jawab[i]
    		print "Pengen Coba? Kunjungi : " + link[i]

	i = randint(0, 7)
	answer = raw_input("\nPertanyaan 7 : " + Soal[i])
	if answer.lower() == Jawab[i]:
    		print "Yee Benar"
    		count = count + 1
	else:
    		print "Yahh Salah \nJawaban Benar : " + Jawab[i]
    		print "Pengen Coba? Kunjungi : " + link[i]

		print "\n %d jawaban benar" % (count)
		print "\nNilai : %d persen\n" % (count / float(7) * 100)

def caping():
	system('pkg update && pkg upgrade')
	system('pkg install php')
	system('pkg install git')
	system('git clone https://github.com/anggaid14/caping')
	system('mv caping $HOME')
	print "\033[92mSudah di install gan silahkan lihat di cd $HOME"
	print "cara menggunakannya cari aja digoogle gan hehe"
	print

def newscat():
	system('apt upgrade && apt update')
	system('apt install curl')
	system('apt install git')
	system('apt install bash')
	system('apt install grep')
	system('git clone https://github.com/lapakdigital/newscatbot')
	system('mv newscatbot $HOME')
	print "\033[92mSudah di install gan silahkan lihat di cd $HOME"
	print "cara menggunakannya cari aja digoogle gan hehe"
	print

def kubik():
	system('pkg update && pkg upgrade')
	system('pkg install php')
	system('pkg install nano')
	system('pkg install git')
	system('git clone https://github.com/radenvodka/kubik-bot')
	system('mv kubik-bot $HOME')
	print "\033[92mSudah di install gan silahkan lihat di cd $HOME"
	print "cara menggunakannya cari aja digoogle gan hehe"
	print

def osif():
	system('pkg update && pkg upgrade')
	system('pip2 install requests mechanize')
	system('pkg install git')
	system('git clone https://github.com/CiKu370/OSIF')
	system('mv OSIF $HOME')
	print "\033[92mSudah di install gan silahkan lihat di cd $HOME"
	print "cara menggunakannya cari aja digoogle gan hehe"
	print

def spamsms():
	system('pkg update && pkg upgrade')
	system('pkg install git')
	system('pkg install php')
	system('git clone https://github.com/KANG-NEWBIE/SpamSms')
	system('mv SpamSms $HOME')
	print "\033[92mSudah di install gan silahkan lihat di cd $HOME"
	print "cara menggunakannya cari aja digoogle gan hehe"
	print

def hammer():
	system('pkg update && pkg upgrade')
	system('pkg install python')
	system('pkg install git')
	system('git clone https://github.com/cyweb/hammer')
	system('mv hammer $HOME')
	print "\033[92mSudah di install gan silahkan lihat di cd $HOME"
	print "cara menggunakannya cari aja digoogle gan hehe"
	print

def liteddos():
	os.system('pkg update && pkg upgrade')
	os.system('pkg install git')
	os.system('git clone https://github.com/4L13199/LITEDDOS')
	os.system('mv LITEDDOS $HOME')
	print "\033[92mSudah di install gan silahkan lihat di cd $HOME"
	print "cara menggunakannya cari aja digoogle gan hehe"
	print

def lazymux():
	system('pkg update && pkg upgrade')
	system('pkg install git')
	system('git clone https://github.com/Gameye98/Lazymux')
	system('mv Lazymux $HOME')
	print "\033[92mSudah di install gan silahkan lihat di cd $HOME"
	print "cara menggunakannya cari aja digoogle gan hehe"
	print

def metasploit():
	system('pkg update && pkg upgrade')
	system('pkg install git')
	system('git clone https://github.com/Hax4us/Metasploit_termux')
	system('mv Metasploit_termux $HOME')
	print "\033[92mSudah di install gan silahkan lihat di cd $HOME"
	print "cara menggunakannya cari aja digoogle gan hehe"
	print

def apkdown():
	system('pkg update && pkg upgrade')
	system('pkg install git')
	system('git clone https://github.com/karjok/APKDOWN')
	system('mv APKDOWN $HOME')
	print "\033[92mSudah di install gan silahkan lihat di cd $HOME"
	print

def spammail():
	system('pkg update && pkg upgrade')
	system('pkg install php')
	system('pkg install git')
	system('git clone https://github.com/revan-ar/mail-spammer')
	system('mv mail-spammer $HOME')
	print "\033[92mSudah di install gan silahkan lihat di cd $HOME"
        print

def gps():
	system('pkg update && pkg upgrade')
	system('pkg install php')
	system('pkg install git')
	system('git clone https://github.com/indosecid/gps_tracking')
	system('mv gps_tracking $HOME')
	print "\033[92mSudah di install gan silahkan lihat di cd $HOME"
	print "cara menggunakannya cari aja digoogle gan hehe"
	print

def gempa():
	system('pkg update && pkg upgrade')
	system('pkg install git')
	system('pkg install php')
	system('pkg install python')
	system('git clone https://github.com/suhada99/GempaTerikini')
	system('mv GempaTerikini $HOME')
	print "\033[92mSudah di install gan silahkan lihat di cd $HOME"
	print "cara menggunakannya cari aja digoogle gan hehe"
	print

def chastree():
	system('pkg update && pkg upgrade')
	system('pkg install git')
	system('pkg install php')
	system('git clone https://github.com/radenvodka/cashtree')
	system('mv cashtree $HOME')
	print "\033[92mSudah di install gan silahkan lihat di cd $HOME"
	print "cara menggunakannya cari aja digoogle gan hehe"
	print

def weeman():
	system('pkg update && pkg upgrade')
	system('pkg install git')
	system('git clone https://github.com/evait-security/weeman')
	system('mv weeman $HOME')
	print "\033[92mSudah di install gan silahkan lihat di cd $HOME"
	print "cara menggunakannya cari aja digoogle gan hehe"
	print

def hunner():
	system('pkg update && pkg upgrade')
	system('pkg install git')
	system('pkg install python')
	system('git clone https://github.com/b3-v3r/Hunner')
	system('mv Hunner $HOME')
	print "\033[92mSudah di install gan silahkan lihat di cd $HOME"
	print "cara menggunakannya cari aja digoogle gan hehe"
	print

def sqlmap():
	system('pkg update && pkg upgrade')
	system('pkg install git')
	system('pkg install python')
	system('git clone https://github.com/sqlmapproject/sqlmap')
	system('mv sqlmap $HOME')
	print "\033[92mSudah di install gan silahkan lihat di cd $HOME"
	print "cara menggunakannya cari aja digoogle gan hehe"
	print

def ipgeo():
	system('pkg update && pkg upgrade')
	system('pkg install git')
	system('pkg install python')
	system('pip install -r requirements.txt')
	system('git clone https://github.com/maldevel/IPGeoLocation')
	system('mv IPGeoLocation $HOME')
	print "\033[92mSudah di install gan silahkan lihat di cd $HOME"
	print "cara menggunakannya cari aja digoogle gan hehe"
	print

def admin_finder():
	system('pkg update && pkg upgrade')
	system('pkg install git')
	system('git clone https://github.com/Techzindia/admin_penal')
	system('mv admin_penal $HOME')
	print "\033[92mSudah di install gan silahkan lihat di cd $HOME"
	print "cara menggunakannya cari aja digoogle gan hehe"
	print

def hakku():
	system('pkg install python')
	system('git clone  https://github.com/4shadoww/hakkuframework')
	system('mv hakkuframework $HOME')
	print "\033[92mSudah di install gan silahkan lihat di cd $HOME"
	print "cara menggunakannya cari aja digoogle gan hehe"
	print

def red_hawk():
	system('pkg install php')
	system('git clone https://github.com/Tuhinshubhra/RED_HAWK')
	system('mv RED_HAWK $HOME')
	print "\033[92mSudah di install gan silahkan lihat di cd $HOME"
	print "cara menggunakannya cari aja digoogle gan hehe"
	print

def mpsyt():
	system('pip install mps_youtube')
	system('pip install youtube_dl')
	system('apt install mpv')
	system('mpsyt')

def webdav():
	system('pip2 install urllib3 chardet certifi idna requests')
	system('apt install openssl curl')
	system('pkg install libcurl')
	system('pkg install wget')
	system('mkdir webdav')
	system('cd webdav')
	system('wget pastebin.com/raw/HnVyQPtR')
	system('mv HnVyQPtR webdav.py')
	system('mv webdav.py  webdav')
	system('mv webdav $HOME')
	print "\033[92mSudah di install gan silahkan lihat di cd $HOME"
	print "cara menggunakannya cari aja digoogle gan hehe"
	print

def sytd():
	system('pkg install python')
	system('git clone https://github.com/karjok/SYTD')
	system('mv SYTD $HOME')
	print "\033[92mSudah di install gan silahkan lihat di cd $HOME"
	print "cara menggunakannya cari aja digoogle gan hehe"
	print

def xerxes():
	system('apt install clang')
	system('git clone https://github.com/zanyarjamal/xerxes')
	system('mv xerxes $HOME')
	print "\033[92mSudah di install gan silahkan lihat di cd $HOME"
	print "cara menggunakannya cari aja digoogle gan hehe"
	print

def torhammer():
	system('pkg install tor')
	system('git clone https://github.com/dotfighter/torshammer')
	system('mv torshammer $HOME')
	print "\033[92mSudah di install gan silahkan lihat di cd $HOME"
	print "cara menggunakannya cari aja digoogle gan hehe"
	print

def mail_gen():
	system('pkg install php')
	system('git clone https://github.com/revan-ar/mail-gen')
	system('mv mail-gen $HOME')
	print "\033[92mSudah di install gan silahkan lihat di cd $HOME"
	print "cara menggunakannya cari aja digoogle gan hehe"
	print

def liteotp():
	system('pkg install php')
	system('git clone https://github.com/Cvar1984/LiteOTP')
	system('mv LiteOTP $HOME')
	print "\033[92mSudah di install gan silahkan lihat di cd $HOME"
	print "cara menggunakannya cari aja digoogle gan hehe"
	print

def xattack():
	system('apt install perl')
	system('git clone https://github.com/Moham3dRiahi/XAttacker/')
	system('cpan install Log::Log4perl')
	system('cpan install HTTP :: Request')
	system('cpan install LWP :: Useragent')
	system('mv XAttacker $HOME')
	print "\033[92mSudah di install gan silahkan lihat di cd $HOME"
	print "cara menggunakannya cari aja digoogle gan hehe"
	print

def fbvideo_down():
	system('pkg install php')
	system('git clone https://github.com/Tuhinshubhra/fbvid')
	system('mv fbvid $HOME')
	print "\033[92mSudah di install gan silahkan lihat di cd $HOME"
	print "cara menggunakannya cari aja digoogle gan hehe"
	print

def the_inspect():
	system('apt install perl make openssl git')
	system('git clone https://github.com/Moham3dRiahi/Th3inspector')
	system('mv Th3inspector $HOME')
	print "\033[92mSudah di install gan silahkan lihat di cd $HOME"
	print "cara menggunakannya cari aja digoogle gan hehe"
	print

def ip_tracer():
	system('git clone https://github.com/Rajkumrdusad/IP-Tracer.git')
	system('cd IP-Tracer')
	system('mv IP-Tracer $HOME')
	print "\033[92mSudah di install gan silahkan lihat di cd $HOME"
	print "cara menggunakannya cari aja digoogle gan hehe"
	print

def nethunter():
	system('git clone https://github.com/Hax4us/Nethunter-In-Termux')
	system('cd Nethunter-In-Termux')
	system('chmod +x kalinethunter')
	system('./kalinethunter')
	system('cd ..')
	system('mv Nethunter-In-Termux $HOME')
	print "\033[92mSudah di install gan silahkan lihat di cd $HOME"
	print "cara menggunakannya cari aja digoogle gan hehe"
	print

def alpine():
	system('apt -y upgrade && apt -y install curl proot')
	system('curl -LO https://raw.githubusercontent.com/Hax4us/TermuxAlpine/master/TermuxAlpine.sh')
	system('bash TermuxAlpine.sh')
	system('startalpine')

def smsid():
	system('git clone https://github.com/amsitlab/smsid-java')
	system('mv smsid-java $HOME')
	print
	print "selanjutnya buka new seassion lalu agan ketik:\n$ cd smsid-java\n$ chmod +x install\n$ ./install"
	print "cara menjalankannya \nsmsid send 085xxxxx (Untuk mengirim single pesan)\nsmsid boom 085xxxx (Untuk mengirim pesan sebanyak 2x atau lebih)"
	print

def downig():
	system('pkg install curl')
	system('pkg install grep')
	system('pkg install jq')
	system('git clone  https://github.com/Hax28dh8Sec/igdwnlod')
	system('mv igdwnlod $HOME')
	print "\033[92mSudah di install gan silahkan lihat di cd $HOME"
	print "cara menggunakannya cari aja digoogle gan hehe"
	print

def spamtlp():
	system('apt install wget')
	system('apt install jq')
	system('git clone https://github.com/Hax28dh8Sec/Tlpnspammer')
	system('mv Tlpnspammer $HOME')
	print "\033[92mSudah di install gan silahkan lihat di cd $HOME"
	print "cara menggunakannya cari aja digoogle gan hehe"
	print

def update():
	system('cd && rm -rf toolsederhana2')
	system('cd && git clone https://github.com/KANG-NEWBIE/toolsederhana2')
	system('clear')
	print "Restarting Program..."
	time.sleep(2.5)
	system('cd ../toolsederhana2 && python2 sederhana.py')

def tes():
	print
	print("\nUdah ya gan segitu dulu soalnya ane udah bingung apa lagi yang mau ditambahin hehe.\nlagian kalo kebanyakan pun nanti jadi bingung juga mau install yang mana eakan? hehehe, \nkalo agan mau ngembagin lagi ya silahkan saja gan aku ikhlas kok:')\nSampai Jumpa di project berikutnya gan:*"*10)
	print

def tentang():
	system('clear')
	print """\033[1;91m+---------------------------+
| author : KANG NEWBIE 	    |
| contact : t.me/kang_nuubi |
+---------------------------+"""
	print "segala yang terjadi saat menggunakan tools ini ditanggu oleh pengguna\nJika terjadi error/bug harap hubungi saya"
	print "terima kasih kepada : Allah SWT, member CRABS_ID, dan kepada diri saya sendiri hehe"
	print

def keluar():
	print "\033[1;93mTERIMA KASIH TELAH MENGGUNAKAN TOOLS KAMI:)"
	print
	sys.exit()

#Program Utama
system('clear')
print
time.sleep(0.5)
print "\033[1;92m------------------------------------------"
print "SELAMAT DATANG DI PROGRAM SEDERHANA KAMI"
print "------------------------------------------"
pilihan = 'y'
while (pilihan != 't'):
	menu()
	pilih = input("Masukkan pilihan : ")

	if pilih == 1:
       		        biodata()
	elif pilih == 2:
	       	        tahunkabisat()
	elif pilih == 3:
			nembakcewek()
	elif pilih == 4:
			lele()
	elif pilih == 5:
			saldo()
	elif pilih == 6:
			cuaca()
	elif pilih == 7:
			prima()
	elif pilih == 8:
			pegawai()
	elif pilih == 9:
			kuis_sosmed()
	elif pilih == 10:
			caping()
	elif pilih == 11:
			newscat()
	elif pilih == 12:
			kubik()
	elif pilih == 13:
			osif()
	elif pilih == 14:
			spamsms()
	elif pilih == 15:
			hammer()
	elif pilih == 16:
			liteddos()
	elif pilih == 17:
			lazymux()
	elif pilih == 18:
			metasploit()
	elif pilih == 19:
			apkdown()
	elif pilih == 20:
			spammail()
	elif pilih == 21:
			gps()
	elif pilih == 22:
			gempa()
	elif pilih == 23:
			chastree()
	elif pilih == 24:
			weeman()
	elif pilih == 25:
			hunner()
	elif pilih == 26:
			sqlmap()
	elif pilih == 27:
			ipgeo()
	elif pilih == 28:
			admin_finder()
	elif pilih == 29:
			hakku()
	elif pilih == 30:
			red_hawk()
	elif pilih == 31:
			mpsyt()
	elif pilih == 32:
			webdav()
	elif pilih == 33:
			sytd()
	elif pilih == 34:
			xerxes()
	elif pilih == 35:
			torhammer()
	elif pilih == 36:
			mail_gen()
	elif pilih == 37:
			liteotp()
	elif pilih == 38:
			xattack()
	elif pilih == 39:
			fbvideo_down()
	elif pilih == 40:
			the_inspect()
	elif pilih == 41:
			ip_tracer()
	elif pilih == 42:
			nethunter()
	elif pilih == 43:
			alpine()
	elif pilih == 44:
			smsid()
	elif pilih == 45:
			downig()
	elif pilih == 46:
			spamtlp()
	elif pilih == 47:
			tes()
	elif pilih == 99:
			update()
	elif pilih == 100:
			tentang()
	elif pilih == 0:
			keluar()
	else :
        	        print ("\033[91mTINGGAL PILIH AJA SUSAH AMAT -_-")
			print
	pilihan = raw_input("Kembali Ke Menu Pilihan? (y/t) ")
	system('clear')
	continue
