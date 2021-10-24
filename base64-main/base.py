# coding:utf8
import os
import sys
import zlib
import base64
import marshal
import binascii
import time
import py_compile
from time import sleep as waktu
from random import randint

p = '\x1b[0m'
m = '\x1b[31m'
i = '\x1b[32m'
b = '\x1b[34m'
k = '\x1b[33;1m'
cg = '\x1b[36m'
ba = '\x1b[96;1m'
pu = '\x1b[35m'
gr = '\x1b[37m'
pb = '\x1b[47m'
cout = 0
import sys,time
def ketik(teks):
 for i in teks + "\n":
  sys.stdout.write(i)
  sys.stdout.flush()
  time.sleep(0.01)

os.system("clear")
ketik (p +"╔═╗╔╗╔╔═╗ "+ k +" ╔╗ ╔═╗╔═╗╔═╗   "+ m +"     ENC "+ p +"BASE64")
ketik (p +"║╣ ║║║║   "+ k +" ╠╩╗╠═╣╚═╗║╣   "+ i +"+"+ p +" Creator "+ m +":"+ k +" ALDI BACHTIAT RIFAI")
ketik (p +"╚═╝╝╚╝╚═╝ "+ k +" ╚═╝╩ ╩╚═╝╚═╝  "+ i +"+"+ p +" Youtube "+ m +":"+ k +" MR.1557")
print
file = raw_input('%s[%s!%s] %sFile %s>> %s' % (b, k, b, gr, gr, i))
print 
time.sleep (1)
cot = int(raw_input('%s[%s!%s] %sLimit %s(%s50000%s) %s? %s>> %s' % (b, k, b, gr, b, gr, b, k, gr, i)))
print
if cot < 500000:
    out = file.replace('.py', '') + '_base.py'
    oa = open(file).read()
    ni = compile(oa, '<noobe>', 'exec')
    bo = marshal.dumps(ni)
    ab = repr(bo)
    s = open(out, 'w')
    s.write('#Coded By MR.1557\nimport marshal\nexec(marshal.loads(' + str(ab) + '))')
    s.close()
    while True:
        if cot >= cout:
            nz = open(out).read()
            dn = compile(nz, '<noobe>', 'exec')
            bx = marshal.dumps(dn)
            nl = repr(bx)
            ns = open(out, 'w')
            ns.write('#Coded By MR.1557\nimport marshal\nexec(marshal.loads(' + str(nl) + '))')
            ns.close()
            cout += 1
            continue
        break
    mx = open(out).read()
    nl = base64.b32encode(mx)
    xn = open(out, 'w')
    xn.write("#Coded By MR.1557\nimport base64\nexec(base64.b32decode('%s'))\n" % nl)
    xn.close()
    ketik ('%s[%s!%s]%s Please wait%s....' % (b, k, b, gr, m))
    print
    time.sleep (4)
    ketik ('\x1b[34m['+ i +'✓\x1b[34m] \x1b[37mDone Di Simpan \x1b[32m[ \x1b[37m%s \x1b[32m] \x1b[37m!' % out)
