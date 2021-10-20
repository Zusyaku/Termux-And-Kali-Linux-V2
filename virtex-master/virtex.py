# Author: Rizky
# github: https://github.com/hekelpro

"""
Mau ngapain kontol?
Ganti author? ganti logo?
lemah lu tolol, buat sendiri ngapa
"""

import requests as r
import os

clear = lambda : os.system('clear')

def unduh(link, out):
	print '! Sedang Mengunduh...'
	a = r.get(link)
	with open(out+'.txt', 'wb') as sv:
		sv.write(a.content)
	print '! Selesai..'
	print '* Result : '+out+'.txt'

def main():
	clear()
	print """
VIRTEX WHATSAPP DOWNLOADER
--------------------------
01. Virtex Level 1
02. Virtex Level 2
03. Virtex Level 3
04. Virtex Level 4
05. Virtex Level 5
06. (Segera datang)
--------------------------"""
	kalahari = raw_input('# Pilih: ')
	if kalahari in ('',' '):
		exit('\n! Dahlah Males Kontol')
	elif kalahari in ('1','01'):
		output = raw_input('\n# Output: ')
		url = 'https://sfile.mobi/download/450944/2/ab70c3f5c135b6f7a0cccbdae779a426/virtex4.txt&is=9d02d01904c99c83abfbf7b5db7da899'
		unduh(url, output)
	elif kalahari in ('2','02'):
		output = raw_input('\n# Output: ')
		url = 'https://sfile.mobi/download/450940/2/ab70c3f5c135b6f7a0cccbdae779a426/virtex1.txt&is=56cdd7db6174675bc0d163cd5e1a0c71'
		unduh(url, out)
	elif kalahari in ('3','03'):
		output = raw_input('\n# Output: ')
		url = 'https://sfile.mobi/download/450948/2/ab70c3f5c135b6f7a0cccbdae779a426/virtex5.txt&is=79692ec8b5ae82676eecc56fb729477c'
		unduh(url, output)
	elif kalahari in ('4','04'):
		output = raw_input('\n# Output: ')
		url = 'https://sfile.mobi/download/450943/2/ab70c3f5c135b6f7a0cccbdae779a426/virtex3.txt&is=2c77dac2303347c09bfecf8395bee0ad'
		unduh(url, output)
	elif kalahari in ('5','05'):
		output = raw_input('\n# Output: ')
		url = 'https://sfile.mobi/download/450941/2/ab70c3f5c135b6f7a0cccbdae779a426/virtex2.txt&is=22013b98949be898cfb79228ba1bf735'
		unduh(url, output)
	elif kalahari in ('6','06'):
		exit('\n! Yeee Tolol!')
	else:
		exit('\n! Menu "'+kalahari+'" Mana Ada Kontol')

if __name__=='__main__':
	main()
