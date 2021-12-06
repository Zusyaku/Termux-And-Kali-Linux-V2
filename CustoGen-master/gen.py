# -*- coding: utf-8 -*-
# Python 3
import string , random

W  = '\033[0m'  # white (default)
R  = '\033[1;31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[1;33m' # orange
B  = '\033[1;34m' # blue
P  = '\033[1;35m' # purple
C  = '\033[1;36m' # cyan
GR = '\033[1;37m' # gray

pil = str(input(C+' Want to Input Base(y/n)? '+R+'> '+W))
if pil == 'n' or pil == 'N' :
    size = int(input(C+' Jumlah digit Kode '+R+'> '+W))
    case = str(input(C+' UPPER/lower (U/l)? '+W))
    total = int(input(C+' Total Kode '+R+'> '+W))
    if case == 'u' or case == 'U' :
        def rand(chars=string.ascii_uppercase + string.digits):
            return ''.join(random.choice(chars) for _ in range(size))
        for i in range(total):
            print (' '+rand())
    elif case == 'l' or case == 'L' :
        def rand(chars=string.ascii_lowercase + string.digits):
            return ''.join(random.choice(chars) for _ in range(size))
        for i in range(total):
            print (' '+rand())
elif pil == 'y' or pil == 'Y' :
    base = str(input(C+' Input Base '+R+'> '+W))
    size = int(input(C+' Jumlah digit Kode '+R+'> '+W))
    case = str(input(C+' UPPER/lower (U/l)? '+W))
    total = int(input(C+' Total Kode '+R+'> '+W))
    if case == 'u' or case == 'U' :
        def rand(chars=string.ascii_uppercase + string.digits):
            return ''.join(random.choice(chars) for _ in range(size-len(base)))
        for i in range(total):
            print (' '+base+rand())
    elif case == 'l' or case == 'L' :
        def rand(chars=string.ascii_lowercase + string.digits):
            return ''.join(random.choice(chars) for _ in range(size-len(base)))
        for i in range(total):
            print (' '+base+rand())
else :
    exit()
