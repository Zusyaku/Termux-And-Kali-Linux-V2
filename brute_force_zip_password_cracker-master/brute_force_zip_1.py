import zipfile
from tqdm import tqdm
from time import sleep

wordlist = "PATH TO WORDLIST"
zip_file = "PATH TO PASSWORD-PROTECTED ZIP FILE"

zip_file = zipfile.ZipFile(zip_file)
n_words = len(list(open(wordlist, "rb")))
print("Total passwords to test:", n_words)
with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=n_words, unit="word"):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
            continue
        else:
            print("[+] Password found:", word.decode().strip())
            sleep(8)
            exit(0)
            
print("[!] Password not found")
