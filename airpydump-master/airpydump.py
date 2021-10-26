#!/usr/bin/python

from scapy.all import sniff
from scapy.layers.dot11 import Dot11Beacon, Dot11, Dot11Elt, RadioTap, EAPOL, rdpcap
from scapy.utils import PcapWriter
import curses
import sys
import os
import re
import getopt
import sys
import subprocess
import signal
import time
import random
from threading import Thread
sys.path.append(os.getcwd()+"/utils/")
from tabulater__ import tabulate
from os.path import basename
from Docker import docker


live__ = False
read__ = ""
iface__ = ""
filter__ = "" #Essid to Filter
pathfile__ = "" # File To Write
curses__ = False
helper = docker()

class color:
	WHITE = '\033[0m'
	PURPLE = '\033[95m'
	CYAN = '\033[96m'
	DARKCYAN = '\033[36m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	END = '\033[0m'

	def win_changer(self):
		self.WHITE = ''
		self.PURPLE = ''
		self.CYAN = ''
		self.DARKCYAN = ''
		self.BLUE = ''
		self.GREEN = ''
		self.YELLOW = ''
		self.RED = ''
		self.BOLD = ''
		self.UNDERLINE = ''
		self.END = ''


def maccom(bssid):
	file_ = open(os.getcwd()+'/utils/macers.txt', 'r')
	for line in file_.readlines():
		if line.strip("\n").split(" ~ ")[0].lower() == bssid.lower()[0:9]+"xx:xx:xx":
			file_.close()
			return line.strip("\n").split(' ~ ')[1].split(" ")[0]
	file_.close()
	return "unknown"

def pwrCall(pkt):
	if pkt.haslayer(RadioTap):
		extra = pkt.notdecoded
		dbm_sig = -(256-ord(extra[-6:-5]))
		if dbm_sig < -100 or dbm_sig > -10:
			return '?'
		return dbm_sig

class reader:
	ap_call_ = {}
	ap_call_2 = {}
	headers = [color.BOLD+'BSSID', 'ESSID', 'BEAC', 'DATA', \
			'ENC', 'CIPHER', 'AUTH', 'CH', 'VENDOR'+color.END]
	counter_ = []
	cl_counter = []
	
	def __init__(self, pktfile, filter_essid=""):
		self.pkts = rdpcap(pktfile)
		self.handshake = self.has_handshakes()
		self.filter_bool = "YES" if len(filter_essid) else "NO"
		self.filter_essid = filter_essid
		return

	def has_handshakes(self):
		for pkt in self.pkts:
			if pkt.haslayer(EAPOL):
				return True
		return False

	def check_cipher_48(self, layer, bssid):
		compound = layer.info
		u_cipher = ''
		p_cipher = ''
		comp_sections = compound.split('\x00\x00')[1:]
		u_ciphers = {'\x0f\xac\x00': 'GROUP',
					  '\x0f\xac\x01': 'WEP',
					  '\x0f\xac\x02': 'TKIP',
					  '\x0f\xac\x04': 'CCMP',
					  '\x0f\xac\x05': 'WEP'}
		p_ciphers = {'\x0f\xac\x00': 'GROUP',
					  '\x0f\xac\x01': 'WEP',
					  '\x0f\xac\x02\x00\x0f\xac\x04': 'TKIP/CCMP',
					  '\x0f\xac\x04\x00\x0f\xac\x02': 'CCMP/TKIP',
					  '\x0f\xac\x02': 'TKIP',
					  '\x0f\xac\x04': 'CCMP',
					  '\x0f\xac\x05': 'WEP'}
		auth_suite = {'\x0f\xac\x01': 'MGT',
					'\x0f\xac\x02': 'PSK'}
		for key, value in u_ciphers.items():
			if comp_sections[0].startswith(key):
				u_cipher = value
		for key, value in p_ciphers.items():
			if comp_sections[1].startswith(key):
				p_cipher = value
		for key, value in auth_suite.items():
			if comp_sections[2].startswith(key):
				self.ap_call_[bssid][7] = value
		self.ap_call_[bssid][6] = p_cipher  # Where p_cipher is the pairwise cipher. This will be displayed to the user
		#self.ap_call_[bssid][6] = u_cipher # If else you want to see unicast cipher
	
	def check_cipher_221(self, layer, bssid):
		compound = layer.info
		u_cipher = ''
		p_cipher = ''
		comp_sections = compound.split('\x00\x00')[1:]
		u_ciphers = {'P\xf2\x00': 'GROUP',
					  'P\xf2\x01': 'WEP',
					  'P\xf2\x02': 'TKIP',
					  'P\xf2\x04': 'CCMP',
					  'P\xf2\x05': 'WEP'}
		p_ciphers = {'P\xf2\x00': 'GROUP',
					  'P\xf2\x01': 'WEP',
					  'P\xf2\x02\x00P\xf2\x04': 'TKIP/CCMP',
					  'P\xf2\x04\x00P\xf2\x02': 'CCMP/TKIP',
					  'P\xf2\x02': 'TKIP',
					  'P\xf2\x04': 'CCMP',
					  'P\xf2\x05': 'WEP'}
		auth_suite = {'P\xf2\x01': 'MGT',
					'P\xf2\x02': 'PSK'}
		for key, value in u_ciphers.items():
			if comp_sections[0].startswith(key):
				u_cipher = value
		for key, value in p_ciphers.items():
			if comp_sections[1].startswith(key):
				p_cipher = value
		for key, value in auth_suite.items():
			if comp_sections[2].startswith(key):
				self.ap_call_[bssid][7] = value
		self.ap_call_[bssid][6] = p_cipher  # Where p_cipher is the pairwise cipher. This will be displayed to the user
		#self.ap_call_[bssid][6] = u_cipher # If else you want to see unicast cipher

	def ap_call_ext(self, layers, bssid, crypto, cap):
		for n in range(20):
			try:
				if layers[n].ID == 3 and layers[n].len == 1:
					self.ap_call_[bssid][4] = ord(layers[n].info) #Channel
				elif layers[n].ID == 48:
					self.ap_call_[bssid][3] = "WPA2"
					crypto.add("WPA2")
					self.check_cipher_48(layers[n], bssid)
				elif layers[n].ID == 221 and layers[n].info.startswith("\x00P\xf2\x01\x01\x00"):
					self.ap_call_[bssid][3] = "WPA"
					crypto.add("WPA")
					self.check_cipher_221(layers[n], bssid)	
				else:
					pass
			except IndexError:	
				pass
		if not crypto:
			if 'privacy' in cap:
				self.ap_call_[bssid][3] = "WEP"
				self.ap_call_[bssid][6] = "WEP"	
			else:
				self.ap_call_[bssid][3] = "OPN"
				self.ap_call_[bssid][6] = "OPN"

	def ap_call(self):
		# Main Network Place
		for pkt in self.pkts:
			if pkt.haslayer(Dot11Beacon):
				bssid = pkt.getlayer(Dot11).addr2
				essid = pkt.getlayer(Dot11Elt).info
				essid = re.sub(r'[^\w]', '', essid)
				cap = pkt.sprintf("{Dot11Beacon:%Dot11Beacon.cap%}").split('+')
				elem_layers = pkt.getlayer(Dot11Elt)
				crypto = set()
				if pkt.getlayer(Dot11).addr2 not in self.counter_:
					self.counter_.append(bssid)
					self.ap_call_[str(bssid)] = [essid, 0, 0, '', 0, '', '', ''] # essid[0], beacon[1], data[2], security[3], channel[4], cipher[5], auth[6]
					self.ap_call_[bssid][1] += 1
					self.ap_call_[bssid][5] = maccom(bssid)
				elif pkt[Dot11].addr2 in self.counter_:
					self.ap_call_[bssid][1] += 1
				self.ap_call_ext(elem_layers, bssid, crypto, cap)

	def ap_data_call(self):
		for pkt in self.pkts:
			if pkt.haslayer(Dot11) and pkt.getlayer(Dot11).type == 2L:
				st = pkt.getlayer(Dot11).addr2
				rv = pkt.getlayer(Dot11).addr1
				for dev in self.counter_:
					if dev == st:
						try:
							self.ap_call_[st][2] += 1
						except KeyError:
							pass
					elif dev == rv:
						try:
							self.ap_call_[rv][2] += 1
						except KeyError:
							pass
		return

	def ap_call_print(self):
		tabulator__ = []
		for key, value in self.ap_call_.items():
			#print "BSSID: %s ESSID: %s BEAC: %d DATA: %d ENC: %s CIPHER: %s AUTH: %s CH: %d VENDOR: %s" % (key.upper(), value[0], value[1], value[2], value[3], value[6], value[7], value[4], value[5])
			tab_list_ = [key.upper(),\
						color.BLUE+value[0]+color.END,\
						color.PURPLE+str(value[1])+color.END ,\
						color.GREEN+str(value[2])+color.END if value[2] > 200 else str(value[2]),\
						color.RED+value[3]+color.END if value[3] in ("WEP", "OPN") else color.GREEN+value[3]+color.END,\
						color.GREEN+value[6]+color.END if "CCMP" in value[6] else color.RED+value[3]+color.END,\
						color.RED+value[7]+color.END if "MGT" in value[7] else value[7],\
						color.CYAN+str(value[4])+color.END if value[4] > 12 else str(value[4]),\
						color.GREEN+value[5]+color.END if "unknown" not in value[5] else color.RED+value[5]+color.END]
			tabulator__.append(tab_list_)
			del tab_list_
		#return str(tabulator__)
		return tabulate(tabulator__, headers=self.headers, tablefmt="simple")

	def ap_call_filtered(self, bool_, tgt):
		if bool_ == "YES":
			tabulator__ = []
			for pkt in self.pkts:
				if pkt.haslayer(Dot11Beacon):
					essid = pkt.getlayer(Dot11Elt).info
					obj = re.search(tgt, essid, re.I)
					if obj:
						bssid = pkt.getlayer(Dot11).addr2
						tabulator__.append([bssid.upper(), color.DARKCYAN+essid.upper()+color.END])
			if len(tabulator__) > 0:
				return "\n\n"+tabulate(tabulator__, headers=[color.BOLD+'BSSID','ESSID'+color.END], tablefmt="simple")

	def ap_call_handshake(self):
		eapol_list, tabulator__ = [], []
		for pkt in self.pkts:
			if pkt.haslayer(EAPOL):
				sender = pkt.getlayer(Dot11).addr2
				receiver = pkt.getlayer(Dot11).addr1
				for dev in self.counter_:
					if sender == dev and receiver not in eapol_list:
						handshake = receiver
						ap = sender
						eapol_list.append(handshake)
						tabulator__.append([ap.upper(), color.YELLOW+handshake.upper()+color.END])
					elif receiver == dev and sender not in eapol_list:
						handshake = sender
						ap = receiver
						eapol_list.append(handshake)
						tabulator__.append([ap.upper(), color.YELLOW+handshake.upper()+color.END])
					else:
						pass
		if self.has_handshakes():
			return "\n"+tabulate(tabulator__, headers=['BSSID', 'HANDSHAKE'], tablefmt="simple")+"\n"
		return "\n"

	def ap_call_clients(self):
		for pkt in self.pkts:
			if pkt.haslayer(Dot11) and pkt.getlayer(Dot11).type == 2L and not pkt.haslayer(EAPOL):
				sender = pkt.getlayer(Dot11).addr2
				receiver = pkt.getlayer(Dot11).addr3
				for dev in self.counter_:
					if dev == sender and receiver not in self.cl_counter:
						ap = sender
						cl = receiver
						self.cl_counter.append(cl)
						self.ap_call_2[cl] = [ap, str(pwrCall(pkt)), 1, maccom(cl)]
					elif dev == sender and receiver in self.cl_counter:
						self.ap_call_2[receiver][2] += 1
						self.ap_call_2[receiver][1] = pwrCall(pkt)
					elif dev == receiver and sender not in self.cl_counter:
						ap = receiver
						cl = sender
						self.cl_counter.append(cl)
						self.ap_call_2[cl] = [ap, str(pwrCall(pkt)), 1, maccom(cl)]
					elif dev == receiver and sender in self.cl_counter:
						self.ap_call_2[sender][2] += 1
						self.ap_call_2[sender][1] = pwrCall(pkt)
					else:
						pass

	def ap_call_client_print(self):
		tabulator__ = []
		for key, value in self.ap_call_2.items():
			tabulator__.append([color.BLUE+value[0].upper()+color.END,\
									key.upper(),\
									value[2],\
									color.GREEN+value[3]+color.END if value[3] != 'unknown' else color.RED+value[3]+color.END])
		return "\n"+tabulate(tabulator__, headers=[color.BOLD+'BSSID', 'CLIENT', 'FRAMES', 'VENDOR'+color.END], tablefmt='simple')


	def call(self):
		self.ap_call()
		self.ap_data_call()
		print self.ap_call_print()
		if self.filter_bool == "YES":
			print self.ap_call_filtered(self.filter_bool, self.filter_essid)
		print self.ap_call_handshake()
		self.ap_call_clients()
		print self.ap_call_client_print()
		return


class Display:
	condition = True
	def __init__(self, scanner):
		self.scanner = scanner
		self.screen = curses.initscr()
		curses.noecho()
		curses.cbreak()
		self.screen.keypad(1)
		self.screen.scrollok(True)
		self.x, self.y = self.screen.getmaxyx()
		curses.start_color()
		curses.use_default_colors()
		try:
			self.screen.curs_set(0)
		except:
			try:
				self.screen.curs_set(1)
			except:
				pass

	def turn_true(self):
		self.condition = False

	def term_resize(self, sig, fr):
		curses.endwin()
		curses.initscr()

	def print_handler(self):
		headers = ['BSSID', 'ESSID', 'PWR', 'BEAC', 'DATA', 'ENC', 'CIPHER', 'AUTH', 'CH', 'VENDOR']
		tabulator__ = []
		tabulator__2 = []
		self.screen.clear()
		self.screen.addstr("[CH: %i]\n" % self.scanner.current_ch)
		for key, value in self.scanner.ntwk_call_1.items():
		#print "BSSID: %s ESSID: %s BEAC: %d DATA: %d ENC: %s CIPHER: %s AUTH: %s CH: %d VENDOR: %s" % (key.upper(), value[0], value[1], value[2], value[3], value[6], value[7], value[4], value[5])
			if value[1] > 10:
				tab_list_ = [key.upper(),\
								value[0],\
								value[8] if value[8] < -2 else '?',\
								value[1],\
								value[2],\
								value[3],\
								value[6],\
								value[7],\
								value[4],\
								value[5]]
				tabulator__.append(tab_list_)
				del tab_list_
		self.screen.addstr("\n"+tabulate(tabulator__, headers=headers, tablefmt="simple"))
		if self.scanner.handshakes:
			self.screen.addstr("\n\n"+tabulate(self.scanner.ntwk_call_3, headers=['TARGET', 'HANDSHAKE'], tablefmt="simple"))
		for key, value in self.scanner.ntwk_call_4.items():
			tabulator__2.append([value[0].upper(),\
									key.upper(),\
									value[1],\
									value[2], value[3]])
		self.screen.addstr("\n\n"+tabulate(tabulator__2, headers=['BSSID', 'CLIENT', 'PWR', 'FRAMES', 'VENDOR'], tablefmt='simple'))
		self.screen.refresh()

#################LIVE##################

class live:
	ntwk_call_1 = {}
	ntwk_call_3 = []
	ntwk_call_4 = {}
	counter_ = []
	cl_counter = []
	sec_count = {}
	current_ch = 1

	def __init__(self, iface, save, file__, curses):
		self.iface=iface
		self.save=save
		self.file__ = PcapWriter(file__, append=True, sync=True) if self.save else ''
		self.handshakes = 0
		self.stop_hopper = False
		self.thread = self.chain_thread()
		self.curses = curses
		if self.curses:
			self.display = Display(self)
		signal.signal(signal.SIGINT, self.print_exit)

	def hop_channel(self):
		n = 1
		if subprocess.call(['sudo','iwconfig'], stdout=subprocess.PIPE, stderr=subprocess.PIPE) != 0:
			sys.exit('iwconfig not installed. Required for Channel Hopping')
		while not self.stop_hopper:
			time.sleep(0.40)
			os.system('iwconfig %s channel %d' % (self.iface, n))
			self.current_ch = n
			dig = int(random.random() * 14)
			if dig != 0 and dig != n:
				n = dig

	def chain_thread(self):
		try:
			thread = Thread(target=self.hop_channel)
			thread.daemon = True
			thread.start()
		except:
			pass
		return True

	def check_cipher_48(self, layer, bssid):
		compound = layer.info
		u_cipher = ''
		p_cipher = ''
		comp_sections = compound.split('\x00\x00')[1:]
		u_ciphers = {'\x0f\xac\x00': 'GROUP',
					  '\x0f\xac\x01': 'WEP',
					  '\x0f\xac\x02': 'TKIP',
					  '\x0f\xac\x04': 'CCMP',
					  '\x0f\xac\x05': 'WEP'}
		p_ciphers = {'\x0f\xac\x00': 'GROUP',
					  '\x0f\xac\x01': 'WEP',
					  '\x0f\xac\x02\x00\x0f\xac\x04': 'TKIP/CCMP',
					  '\x0f\xac\x04\x00\x0f\xac\x02': 'CCMP/TKIP',
					  '\x0f\xac\x02': 'TKIP',
					  '\x0f\xac\x04': 'CCMP',
					  '\x0f\xac\x05': 'WEP'}
		auth_suite = {'\x0f\xac\x01': 'MGT',
					'\x0f\xac\x02': 'PSK'}
		for key, value in u_ciphers.items():
			if comp_sections[0].startswith(key):
				u_cipher = value
		for key, value in p_ciphers.items():
			if comp_sections[1].startswith(key):
				p_cipher = value
		for key, value in auth_suite.items():
			if comp_sections[2].startswith(key):
				self.ntwk_call_1[bssid][7] = value
		self.ntwk_call_1[bssid][6] = p_cipher  # Where p_cipher is the pairwise cipher. This will be displayed to the user
		#self.ntwk_call_1[bssid][6] = u_cipher # If else you want to see unicast cipher

	def check_cipher_221(self, layer, bssid):
		# Here is the flteration of WPA 221 Layer.
		compound = layer.info
		u_cipher = ''
		p_cipher = ''
		comp_sections = compound.split('\x00\x00')[1:]
		u_ciphers = {'P\xf2\x00': 'GROUP',
					  'P\xf2\x01': 'WEP',
					  'P\xf2\x02': 'TKIP',
					  'P\xf2\x04': 'CCMP',
					  'P\xf2\x05': 'WEP'}
		p_ciphers = {'P\xf2\x00': 'GROUP',
					  'P\xf2\x01': 'WEP',
					  'P\xf2\x02\x00P\xf2\x04': 'TKIP/CCMP',
					  'P\xf2\x04\x00P\xf2\x02': 'CCMP/TKIP',
					  'P\xf2\x02': 'TKIP',
					  'P\xf2\x04': 'CCMP',
					  'P\xf2\x05': 'WEP'}
		auth_suite = {'P\xf2\x01': 'MGT',
					'P\xf2\x02': 'PSK'}
		for key, value in u_ciphers.items():
			if comp_sections[0].startswith(key):
				u_cipher = value
		for key, value in p_ciphers.items():
			if comp_sections[1].startswith(key):
				p_cipher = value
		for key, value in auth_suite.items():
			if comp_sections[2].startswith(key):
				self.ntwk_call_1[bssid][7] = value
		self.ntwk_call_1[bssid][6] = p_cipher  # Where p_cipher is the pairwise cipher. This will be displayed to the user
		#self.ntwk_call_1[bssid][6] = u_cipher # If else you want to see unicast cipher


	def call1_ext(self, bssid, crypto, layers, cap):
		for n in range(20):
			try:
				if layers[n].ID == 3 and layers[n].len == 1:
					self.ntwk_call_1[bssid][4] = ord(layers[n].info) #Channel
				elif layers[n].ID == 48:
					self.ntwk_call_1[bssid][3] = "WPA2"
					crypto.add("WPA2")
					self.sec_count[bssid] = 0; self.sec_count[bssid]+=1
					self.check_cipher_48(layers[n], bssid)
				elif layers[n].ID == 221 and layers[n].info.startswith("\x00P\xf2\x01\x01\x00"):
					self.ntwk_call_1[bssid][3] = "WPA"
					crypto.add("WPA")
					self.sec_count[bssid] = 0; self.sec_count[bssid]+=1
					self.check_cipher_221(layers[n], bssid)
				else:
					pass
			except IndexError:
				pass
			if not crypto:
				if 'privacy' in cap:
					self.ntwk_call_1[bssid][3], self.ntwk_call_1[bssid][6], self.ntwk_call_1[bssid][7] = "WEP", "WEP", ""		
				else:
					self.ntwk_call_1[bssid][3], self.ntwk_call_1[bssid][6] = "OPN", "OPN"
		return

	def call1(self, pkt):
		if pkt.haslayer(Dot11Beacon):
			bssid = str(pkt.getlayer(Dot11).addr2)
			essid = str(pkt.getlayer(Dot11Elt).info)
			essid = re.sub(r'[^\w]', '', essid)
			cap = pkt.sprintf("{Dot11Beacon:%Dot11Beacon.cap%}").split('+')
			elem_layers = pkt.getlayer(Dot11Elt)
			crypto = set()
			if pkt.getlayer(Dot11).addr2 not in self.counter_:
				self.counter_.append(bssid)
				self.ntwk_call_1[str(bssid)] = [essid, 0, 0, '', 0, '', '', '', pwrCall(pkt)] # essid[0], beacon[1], data[2], security[3], channel[4], cipher[5], auth[6]
				self.ntwk_call_1[bssid][1] += 1
				self.ntwk_call_1[bssid][5] = maccom(bssid)
			elif pkt[Dot11].addr2 in self.counter_:
				self.ntwk_call_1[bssid][8] = pwrCall(pkt)
				self.ntwk_call_1[bssid][1] += 1
			self.call1_ext(bssid, crypto, elem_layers, cap)

	def call2(self, pkt):
		if pkt.haslayer(Dot11) and pkt.getlayer(Dot11).type == 2L:
			st = pkt.getlayer(Dot11).addr2
			rv = pkt.getlayer(Dot11).addr1
			for dev in self.counter_:
				if dev == st:
					try:
						self.ntwk_call_1[st][2] += 1
					except KeyError:
						pass
				elif dev == rv:
					try:
						self.ntwk_call_1[rv][2] += 1
					except KeyError:
						pass

	def call3(self, pkt):
		eapol_list, tabulator__ = [], []
		if pkt.haslayer(EAPOL):
			sender = pkt.getlayer(Dot11).addr2
			receiver = pkt.getlayer(Dot11).addr1
			for dev in self.counter_:
				if sender == dev and receiver not in eapol_list:
					handshake = receiver
					ap = sender
					eapol_list.append(handshake)
					tabulator__.append(ap)
					tabulator__.append(handshake)
					self.handshakes += 1
				elif receiver == dev and sender not in eapol_list:
					handshake = sender
					ap = receiver
					eapol_list.append(handshake)
					tabulator__.append(ap)
					tabulator__.append(handshake)
					self.handshakes += 1
				else:
					pass
		return tabulator__

	def call4(self, pkt):
		tabulator = []
		if pkt.haslayer(Dot11) and pkt.getlayer(Dot11).type == 2L and not pkt.haslayer(EAPOL):
			sender = pkt.getlayer(Dot11).addr2
			receiver = pkt.getlayer(Dot11).addr3
			for dev in self.counter_:
				if dev == sender and receiver not in self.cl_counter:
					ap = sender
					cl = receiver
					self.cl_counter.append(cl)
					self.ntwk_call_4[cl] = [ap, str(pwrCall(pkt)), 1, maccom(cl)]
				elif dev == sender and receiver in self.cl_counter:
					self.ntwk_call_4[receiver][2] += 1
					self.ntwk_call_4[receiver][1] = pwrCall(pkt)
				elif dev == receiver and sender not in self.cl_counter:
					ap = receiver
					cl = sender
					self.cl_counter.append(cl)
					self.ntwk_call_4[cl] = [ap, str(pwrCall(pkt)), 1, maccom(cl)]
				elif dev == receiver and sender in self.cl_counter:
					self.ntwk_call_4[sender][2] += 1
					self.ntwk_call_4[sender][1] = pwrCall(pkt)
				else:
					pass
		return

	def manipulate(self, pkt):
		if self.save:
			self.file__.write(pkt)
		self.call1(pkt)
		self.call2(pkt)
		call3_varbell = self.call3(pkt)
		if bool(call3_varbell):
			self.ntwk_call_3.append(call3_varbell)
		call4_varbell = self.call4(pkt)
		if bool(call4_varbell):
			self.ntwk_call_4.append(call4_varbell)
		if self.curses:
			try:
				self.display.print_handler()
			except:
				curses.nocbreak()
				self.display.screen.keypad(0)
				curses.echo()
				curses.endwin()
		return

	def print_exit(self, signal, frame):
		self.stop_hopper = True
		if self.curses == True:
			curses.nocbreak()
			self.display.screen.keypad(0)
			curses.echo()
			curses.endwin()
		tabulator__ = []
		tabulator__2 = []
		headers = [color.BOLD+'BSSID', 'ESSID', 'PWR', 'BEAC', 'DATA', 'ENC', 'CIPHER', 'AUTH', 'CH', 'VENDOR'+color.END]
		for key, value in self.ntwk_call_1.items():
			#print "BSSID: %s ESSID: %s BEAC: %d DATA: %d ENC: %s CIPHER: %s AUTH: %s CH: %d VENDOR: %s" % (key.upper(), value[0], value[1], value[2], value[3], value[6], value[7], value[4], value[5])
			if value[1] > 10:
				tab_list_ = [key.upper(),\
										color.BLUE+value[0]+color.END,\
										value[8] if value[8] < -2 else color.RED+'?'+color.END,\
										color.PURPLE+str(value[1])+color.END,\
										color.YELLOW+str(value[2])+color.END if value[2] > 150 else value[2],\
										color.RED+value[3]+color.END if value[3] in ('WEP', 'OPN') else color.GREEN+value[3]+color.END,\
										color.GREEN+value[6]+color.END if 'CCMP' in value[6] else color.RED+value[6]+color.END,\
										color.RED+value[7]+color.END if value[7] != "PSK" else value[7],\
										color.DARKCYAN+str(value[4])+color.END if value[4] > 12 else value[4],\
										color.GREEN+value[5]+color.END if value[5] is not 'unknown' else color.RED+value[5]+color.END]
				tabulator__.append(tab_list_)
				del tab_list_
		print "\n"+tabulate(tabulator__, headers=headers, tablefmt="simple")
		if self.handshakes:
			print "\n"+tabulate(self.ntwk_call_3, headers=[color.BOLD+'TARGET', 'HANDSHAKE'+color.END], tablefmt="simple")
		for key, value in self.ntwk_call_4.items():
			tabulator__2.append([color.BLUE+value[0].upper()+color.END,\
									key.upper(),\
									color.GREEN+str(value[1])+color.END if value[1]<-2 else color.RED+'?'+color.END,\
									value[2], value[3]])
		print "\n"+tabulate(tabulator__2, headers=[color.BOLD+'BSSID', 'CLIENT', 'PWR', 'FRAMES', 'VENDOR'+color.END], tablefmt='simple')
		sys.exit("\n"+color.YELLOW+"BYE!"+color.END)


########################################


def check_pcap(file_):
	if os.path.isfile(file_):
		return [True, basename(file_)]
	return [False, '']

def checkinterface(iface):
	ifaces = []
	dev = open('/proc/net/dev', 'r')
	data = dev.read()
	for n in re.findall('[a-zA-Z0-9]+:', data):
		ifaces.append(n.rstrip(":"))
	dev.close()
	if iface in ifaces:
		co = subprocess.Popen(['iwconfig', iface], stdout=subprocess.PIPE)
		data = co.communicate()[0]
		card = re.findall('Mode:[A-Za-z]+', data)[0]	
		if "Monitor" in card:
			return True
		else:
			sys.exit("%s not in monitor mode" % iface)
	else:
		sys.exit("No such interface: %s" % iface)

def main():
	global live__, read__, iface__,filter__, pathfile__, curses__ 
	try:
		opts, noopts = getopt.getopt(sys.argv[1:], "hlr:i:f:w:c", ['help','live', 'read=', 'interface=', 'filter=', 'write=', 'curses'])
	except getopt.GetoptError as err:
		print str(err)+'\n'
		sys.exit("use --help or -h argument for help")
	for o, v in opts:
		if o in ("-l", "--live"):
			live__ = True
		elif o in ("-h", "--help"):
			helper.help()
		elif o in ("-r", "--read"):
			read__ = v
		elif o in ("-i", "--interface"):
			iface__ = v
		elif o in ("-f", "--filter"):
			filter__ = v 
		elif o in ("-w", "--write"):
			if v.endswith('.cap'):
				pathfile__ = v
			else:
				pathfile__ = v+".cap"
		elif o in ("-c", "--curses"):
			curses__ = True
		else:
			pass
	return


if __name__ == "__main__":
	main()
	if os.name != 'posix':
		Color = color()
		Color.win_changer()
		del Color
	if live__:
		if iface__:
			if checkinterface(iface__):
				print "Starting Sniffing... Press CTRL+C anytime to stop see the captured data\n"
				livecap = live(iface__, bool(pathfile__), pathfile__, curses__)
				try:
					sniff(iface=iface__, prn=livecap.manipulate)
				except Exception, e:
					print e
		else:
			helper.no_interface()
	elif len(read__):
		bool_, filename = check_pcap(read__)
		if bool_:
			if filter__:
				filename = reader(read__, filter__)
				filename.call()
			else:
				filename = reader(read__)
				filename.call()
	else:
		helper.help()

		
