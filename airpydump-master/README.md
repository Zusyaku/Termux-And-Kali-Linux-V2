# airpydump
Analyze Wireless Packets on the fly. Currently supporting three working Modes (Reader, Live, Stealth)

## Description

  airpydump is a wireless packet analyzer, providing the interface most likely that of airodump-ng from aircrack suite. It currently provides three working modes which are Reader, Stealth and Live. Reader Mode is used to read a written captured file earlier either with airodump, wireshark or airpydump itself. Stealth mode is used when you are on a run and don't want to see the live traffic but just on the end of your run. So, that you could press CTRL+C at the end of your run and captured packets will be displayed to you. Live mode which is not fully build yet, actually utilize curses library from python which have some problems until now, prints live packets i.e. as soon as they've captured by the wireless adapter. The problem with Live Mode is with resizing the terminal. So, don't try to maximize or restore the screen while live sniffing or else your terminal will be messed up. The only way then you have to get rid of it is forcily shut it down and then spawn a new terminal again. 
  
## MODES
```
READER MODE: python airpydump.py -r [/path/to/.cap/file]
STEALTH MODE: python airpydump.py -i [Monitor Interface] --live
LIVE MODE: python airpydump.py -i [Monitor Interface] --live --curses
```
## USAGE
```
[usage] python airpydump.py [arguments]
```
## ARGUMENTS
```
-h, --help                      prints help manual
-i, --interface=                Monitor Mode Interface to use
-r, --read=                     Read a captured file earlier, e.g. packets.cap
-w, --write=                    Write packets to a file.
-c, --curses                    Utilize curses library to print live packets
-i, --live                      Must be used for stealth and live modes
```
## UPDATE

Terminal Error Resizing while Live sniffing

## Author

admin@shellvoide.com

[https://www.shellvoide.com](https://www.shellvoide.com)
