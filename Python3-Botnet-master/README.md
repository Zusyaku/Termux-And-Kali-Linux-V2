# Python3-Botnet ![](https://img.shields.io/badge/Version-2.1-brightgreen.svg)  ![](https://img.shields.io/badge/license-GPL3.0-blue.svg)

**Project moved to [here](https://github.com/Leeon123/Aoyama)**

**Use Python3 to build a botnet (include bot and c&amp;c)**

**Xor encode traffic**

**Qbot style Login.**

Build up a easy P2P botnet with python3.

***Youtube Video: https://youtu.be/3_JnAXVtFNs (outdated)***

I will upload xor version and new tut video as fast as i can :)

## C&C Features

Using login.txt to check account.

**TCP Keep-Alive Connection**

**Simple CNC** with **Xor encode traffic**
## Bot Features
**Xor encode traffic**

**Three attack mode**

- [x] Http-flood 
- [x] TCP Connection FLood 
- [x] UDP Flood

**Keep-Alive connection**
## Requirement
***Only need python3 :)***

## Usage:
***Edit*** the cnc server ip and port into the bot.py **at first**.

Then, edit the password of cnc.py and run the cnc.py:

    python3 cnc.py <port>
    
At Last, run the bot.py in any python3 environment(IDE, codeanywhere,etc.) then the **Bot** is online.

***To login cnc***, using **putty raw-mode** or telnet(**in linux**) to connect it then

input worlds "Login" will show the login parameters

        Username:
At this moment, u should create a text called login.txt and input the username and password in it

Like this:

        Leeon123 test

After that, Just input ur username and password.
        
                    
            Username:Leeon123
            Password:test
            
**Welcome to Python3 C&C Server.**
