#!/bin/bash
#Installing the requirements files
pkg  update -y 
pkg  upgrade -y
pkg install python -y  
apt-get install ruby -y
pip install lolcat
gem install lolcat
apt-get install ncurses-utils -yq --silent
clear

# video tutorial
video_tutorial() {
echo
echo 
echo
echo -en "\e[96m>>\e[92m Do you wish to see a practical video on it (y/n)? \e[m "
read answer
if [ "$answer" != "${answer#[Yy]}" ] ;then
am start -a android.intent.action.VIEW -d https://youtu.be/MLqdeKat5DU > /dev/null 2>&1
else                                                                                  
echo
fi
echo 
clear
}

video_tutorial

sleep 4
echo " "
echo " "
echo "           < ━━━━━━━━━━━━ [★] CREATED BY ASHISH [★] ━━━━━━━━━━━━ > " |lolcat
echo " "
echo "  
                 ▀█▀ █▀▀ █▀█ █▀▄▀█ █ █ ▀▄▀ ▄▄ █▄▀ █▀▀ █▄█ █▀
                  █  ██▄ █▀▄ █ ▀ █ █▄█ █ █    █ █ ██▄  █  ▄█  " |lolcat		  

echo " "
echo " "
echo "           < ━━━━━━━━━━━━━ [★] BHAVIK TUTORIALS [★] ━━━━━━━━━━━━ > " |lolcat

   #Installing Termux-keys
./key
