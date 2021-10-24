import os, requests, getpass

print ("======> LOGIN FB <=======")
id = raw_input("Masukan Email : ")
pw = getpass.getpass(prompt='Masukan Password : ')
print("Please wait...")

url = 'https://mobile.facebook.com/login.php'

headers = {
'User-Agent' : '',
'Accept-Language' : ''
}

data = {
'email' : id,
'pass' : pw
}

requests = requests.post(url, headers=headers, data=data).text

if "xc_message" in requests:
    print("Berhasil Login")
elif "checkpointSubmitButton" in requests:
    print("Kena Checkpoin")
else:
    print("Gagal Login !!!")

