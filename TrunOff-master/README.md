# TrunOff
Tools/scrpt/repostory untuk me-restart/shutdown hp kamu<br>
Tools ini membutuhkan akses root dan sudo
# Installing Sudo
Jika sudah menginstall sudo lewati langkah ini.<br>
$ apt update && apt upgrade<br>
$ pkg install git<br>
$ git clone https://gitlab.com/st42/termux-sudo<br>
$ cd termux-sudo<br>
$ pkg install ncurses-utils<br>
$ cat sudo > /data/data/com.termux/files/usr/bin/sudo<br>
$ chmod 700 /data/data/com.termux/files/usr/bin/sudo
# Installing The Tools
$ apt update && apt upgrade<br>
$ pkg install git<br>
$ pkg install python<br>
$ git clone https://github.com/KANG-NEWBIE/TrunOff<br>
$ cd TrunOff<br>
$ sudo python rest.py
