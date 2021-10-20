import random
import sys
import time
def type(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)
type('Kejarlah kesempurnaan maka kesuksesan akan menghampirimu || Belajar apa yang kau sukai maka kau akan mudah memahami -TUAN B4DUT.')
