#_* coding:utf-8 *_
# Start : 08-04-2021 15:03 WIB
# Done  : 08-04-2021 16:14 WIB

import sys as snif, os, marshal
from time import sleep as date

'''
!-- Note --!
         Kalo Mau Rikod Sertakan Sumber Peler
         Compile Marshal Only Python3 Not Support Python2
'''

exec(open("etc/.colors").read())

_black_ = lambda: print(f"""\n {yellow}╔═╗╦ ╦╔═╗╔═╗╔╦╗╔═╗╦╦  ╔═╗╦═╗\n {yellow}╠═╝╚╦╝║  ║ ║║║║╠═╝║║  ║╣ ╠╦╝\n {yellow}╩   ╩ ╚═╝╚═╝╩ ╩╩  ╩╩═╝╚═╝╩╚═  {green}Only Py3\n {black}=======================================\n {green}[{white}•{green}] {white}Creator {black}: {white}Kingtebe\n {green}[{white}•{green}] {white}Youtube {black}: {white}FaaL Tv\n {green}[{white}•{green}] {white}Github  {black}: {green}github.com/Kingtebe\n {black}=======================================\n""")

class Compile:

	def __init__(self):
		self._FaaL_ = "#----------------------------------------\n# Compile : Kingtebe\n# Youtube : FaaL TV\n# Github  : https://github.com/Kingtebe\n#----------------------------------------\nimport marshal\nexec(marshal.loads(%s))"
		self._Main_()

	def _Main_(self):
		__import__('os').system('clear')
		try:
			_black_()
			angka = 0
			file = input(f"  {yellow}➣ {white}Input File {black}: {white}")
			count = int(input(f"  {yellow}➣ {white}Count {black}: {white}"))
			if ( count < 400 ):
				out = input(f"  {yellow}➣ {white}Output File {black}: {white}")
				ewe = open(file).read().encode('utf-8')
				xxx = compile(ewe, '<kingtebe>', 'exec')
				asu = repr(marshal.dumps(xxx))
				f = open(out, 'w')
				f.write(self._FaaL_ % asu)
				f.close()
				while ( count >= angka):
					meki = open(out).read().encode('utf-8')
					puki = compile(meki, '<kingtebe>', 'exec')
					peju = repr(marshal.dumps(puki))
					x = open(out, 'w')
					x.write(self._FaaL_ % peju)
					x.close()
					angka += 1
					date(1.2)
				exit(f"\n {green}[{white}•{green}] {white}Succses Saved To »» {green}{out} \n{white}")
		except ValueError:exit(f"\n {black}[ {white}Warning {red}! {white}Harus berupa angka nyet {black}]\n")
		except FileNotFoundError:exit(f"\n {black}[ {white}Warning {red}! {white}File {yellow}{file} {white}Tidak Ditemukan {black}]\n")

if __name__=='__main__':
     Compile()
