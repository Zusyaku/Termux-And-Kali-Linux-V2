from PIL import ImageGrab
import time
def screenshootfunc(name="screen"):
    while True:
        picture = ImageGrab.grab()
        screen_name=name+".jpg"
       # path= "C:\\Windows\\debug\\"
        picture.save(screen_name,'JPEG')
        time.sleep(120)
