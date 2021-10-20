#!usr/bin/python2

import string

paswd = input("masukan password brute: \n")

def Brute(paswd):
  print("[+]Memulai bruteforce...")
  charset = list(string.ascii_letters + string.digits + string.punctuation)
  result = ""
  x = 0
  while x <= len(paswd)-1:
     for char in charset:
        pchr = paswd[x]
        if char == pchr:
          print("[+] Trying...", char)
          print("[+][+]Matched (",char, ")")
          result += char
          print("[+][+]current:",result)
          x += 1
          break
        else:
          print("[+] Trying...",char)
  print("[+][+] Matching Done - Password Founds:",result)
Brute(paswd)
