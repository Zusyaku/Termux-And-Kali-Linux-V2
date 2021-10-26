#!/usr/bin/python

import sys
import os

__doc__ = """
airpydump is wireless (802.11) packet analyzer, currently supporting three operating modes:
1) Reader Mode    (Read a captured File) 
2) Stealth Mode   (Prints the live data on pressing CTRL+C)
3) Live Mode      (Print packets as soon as discovered)

USAGE: python airpydump [arguments]

EXAMPLES: 
	Reader Mode: python airpydump -r [full path to packet captured file]
	Stealth Mode: python airpydump -i [Monitor Interface] --live 
	Live Mode: python airpydump -i [Monior Interface] -c --live

ARGUMENTS: 

-h, --help              This Help MANUAL
-i, --interface         Interface to use for live/stealth sniffing
-c, --curses			Printing Live data on screen
-r, --read              Full Path to captured file
-w, --write             Write packets to a file
-l, --live              Live printing for Stealth/Live Mode

UPDATE:
	Some problems have been detected in airpydump script with Live Mode while resizing the screen. Feel Free to send email on admin@shellvoide.com\
	 in case of any help. So, While using live mode, try not to resize your screen in any way or else your terminal will be messed up 	
"""

class docker:
	__doc__ = __doc__

	def help(self):
		sys.exit(self.__doc__)

	def no_interface(self):
		sys.exit("Live Capture requires an interface")