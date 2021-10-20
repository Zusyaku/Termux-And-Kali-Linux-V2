import os

try:
	os.mkdir('../s-mbf_backupdir')
except: pass
try:
	print('[moving] result folder')
	os.system('mv result ../s-mbf_backupdir')
except: pass
try:
	print('[moving] checker folder')
	os.system('mv checker ../s-mbf_backupdir')
except: pass
try:
	print('[moving] toket folder')
	os.system('mv toket ../s-mbf_backupdir')
except: pass