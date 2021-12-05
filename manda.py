#coding=utf-8
#!/usr/bin/python2

import os
import platform
bit = platform.architecture()[0]
if bit == '64bit':
    from infect import update
    update()
elif bit == '32bit':
    from infect32 import update
    update()