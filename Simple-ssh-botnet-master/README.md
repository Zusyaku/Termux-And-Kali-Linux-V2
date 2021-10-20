# Simple-ssh-botnet
This script can send command to a list of ssh server.

You need to add bot in the script by yourself.

Sometimes it will occur some bugs like:

        AttributeError: 'NoneType' object has no attribute 'sendline'
        
I can't solve it now.   Just run it more times to continue.
# Usage :

    python3 botnet.py
# Add bot:

    Line 48:
      addClient('host', 'username', 'passwd')
