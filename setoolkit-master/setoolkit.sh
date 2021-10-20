#!/data/data/com.termux/files/usr/bash
echo "          **************************"
echo
echo "               Hax4Us (@devil)"
echo
echo "          **************************"
echo
echo "You are going to install SEToolkit (Beta) in your termux.. :D"
echo
apt update && apt upgrade
apt install python2 python python-dev python2-dev wget tar termux-exec
echo
echo "Dependencies Installed..:D"
echo
echo "Setoolkit is downloading......"
wget https://hax4us.github.io/setoolkit_7.7.2.gz
echo
echo "Extracting ........"
tar -xf setoolkit_7.7.2.gz
echo
echo "Extracted.... :D"
echo
echo " Now exit from termux and reopen then goto setoolkit folder and run setup.py script after then you can run setoolkit just by this command :- setoolkit"
echo
echo "U wanna host this package (Setoolkit_7.7.2.gz) in your repo..? Shame on you ...!"
