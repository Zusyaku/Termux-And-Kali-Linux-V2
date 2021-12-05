#!/termux/data/data/bin/bash
# script by AnonyminHack5  from [ Termux Android Hackers] WhatsApp group
apt-get update -y
apt-get upgrade -y
pkg install python2 -y
pkg install python -y
pip install lolcat
clear
echo $red 
echo ' 
   ___  __  __  _                  _       _ _   
|  \/  | ___| |_ __ _ ___ _ __ | | ___ (_) |_ 
| |\/| |/ _ \ __/ _  / __|  _ \| |/ _ \| | __|
| |  | |  __/ || (_| \__ \ |_) | | (_) | | |_ 
|_|  |_|\___|\__\__ _|___/ .__/|_|\___/|_|\__|
                         |_|     
                         
/....Kindly TuRn On yOur IntErneT coNnecTion....\' | lolcat
echo " "
echo "### This Script is written by AnonyminHack5  ###" 
echo " "
echo "----------- Fetching.../// ---------️----"
echo " "
pkg install wget -y
pkg install openssh -y
pkg install ruby -y
pkg install unstable-repo -y
pkg install metasploit -y

ls

cd ..

ls

cd usr

ls

cd opt

ls

mv metasploit-framework $HOME

ls

cd /data/data/com.termux/files/home

ls

cd metasploit-framework

ls

wget https://github.com/termux/termux-packages/files/2912002/fix-ruby-bigdecimal.sh.txt

bash fix-ruby-bigdecimal.sh.txt

echo " "
echo "############# Completed ################"                                                                                                                       
echo " "
echo "If You Are connected to the  Internet Then 
you have downloaded metasploit successfully."
echo " "
echo " (x ...BE A WHITE HAT HACKER... x) "
echo " "
echo ' '
echo " "
echo -e "\e[1;34m Type msfconsole to start metasploit..."
echo " "

./msfconsole

exit