#!/data/data/com.termux/files/usr/bash
echo "          **************************"
echo
echo "      subscribe   Tech Z India"
echo
echo "          **************************"
echo
echo "You are going to install SEToolkit (Beta Version) in your termux.. :D"
echo
apt update && apt upgrade
apt install python2 figlet python python-dev python2-dev wget tar termux-exec
echo
echo "Dependencies/packages Installed..:D"
echo
echo "Setoolkit is downloading......"
echo "thanks to Hax4us YT channel" 
wget https://hax4us.github.io/setoolkit_7.7.2.gz
echo
echo "Extracting ........"
tar -xf setoolkit_7.7.2.gz
echo
echo "Extracted.... :D"
cd setoolkit
python setup.py install 
echo
figlet Installed
echo
echo " Setoolkit is Installed in Your Termux "
echo " Now Type (setoolkit) to Run Setoolkit In Your Termux "
echo
echo "Note- This is Beta Version of Set" 
echo " This setoolkit is Not Fully Stable "
cd $HOME
rm setoolkit_7.7.2.gz
