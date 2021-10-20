import os, sys

print ("\033[1;32mMasukin UserName&Password:)")

print ("\033[1;32mATAU HUBUNGI LANGSUNG MR.K7C8NG WHATSAPP = 082149735460 ")

username = 'MR.K7C8NG'      

password = 'GANTENG1'



def restart():

	ngulang = sys.executable

	os.execl(ngulang, ngulang, *sys.argv)



def main():

	uname = raw_input("username : ")

	if uname == username:

		pwd = raw_input("password : ")



		if pwd == password:

			print "\033[1;32mSAMPAI JUMPA", 

			sys.exit()



		else:

			print "\032[1;32mSorry Passwordmu salah cok !!!\033[00m"

			print "Back Login\n"

			restart()



	else:

		print "\033[1;32mSorry..anda noob !!!\033[00m"

		print "Back Login\n"

		restart()



try:

	main()

except KeyboardInterrupt:

	os.system('clear')

	restart()

