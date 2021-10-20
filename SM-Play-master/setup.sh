#!/bin/bash
while :
do
clear
echo -e "\e[1;31m"
echo "   _____ __  ___            ____  __           ";
echo "  / ___//  |/  /           / __ \/ /___ ___  __";
echo "  \__ \/ /|_/ /  ______   / /_/ / / __ \`/ / / /";
echo " ___/ / /  / /  /_____/  / ____/ / /_/ / /_/ / ";
echo "/____/_/  /_/           /_/   /_/\__,_/\__, /  ";
echo "                                      /____/   ";
echo -e "\e[1;32m"
echo 'Press 1 to  Install Dependencies'
echo 'Press 2 to  Continue To SM-Play'
echo 'Press 3 to  Add SM-Play To Bin'
echo 'Press 4 to  Update SM-Play  [Online Hacking'
echo 'Press 5 for Help'
echo 'Press 6 to  Exit'
echo
echo -e "\e[1;34m"
read -p 'select_option >' opt
echo -e "\e[1;33m"
if [ $opt -eq 1 ];then
echo 'Make Sure You Have Installed Termux:API From PlayStore ...'
read -p 'Have You Installed Termux:API From Play Store (Y/N) : ' cho
if [ "$cho" = "Y" ] || [ "$cho" = "y" ] ;then
apt update && apt upgrade
apt install figlet git toilet curl python2 -y
pkg install termux-api
termux-setup-storage
if [[ -s $PREFIX/bin/termux-media-player ]] ;then
echo 'All Dependencies installed...'
read -p 'Do you want to add SM-Play To bin (Y/N): ' ch
if [ "$ch" = "Y" ] || [ "$ch" = "y" ] ;then
echo 'cd' $PWD '&& python2 music.py' >$PREFIX/bin/tplay
echo 'exit' >$PREFIX/bin/tplay
chmod +x $PREFIX/bin/tplay
echo 'Added tplay to bin !!'
echo 'Now You Can Launch TPlay just by typing \e[1;31mtplay\e[1;33m anywhere!!!'
read -p 'Press Enter Key To Continue..' k
fi
else
echo 'Please Install Termux:API from PlayStore To Proceed...'
read -p 'Press Enter Key To Continue..' k
fi
else
echo 'Please Install Termux:API from PlayStore To Proceed...'
read -p 'Press Enter Key To Continue..' k
fi
elif [ $opt -eq 2 ];then
termux-setup-storage
python2 music.py
exit
elif [ $opt -eq 3 ];then
echo 'cd' $PWD '&& python2 music.py' >$PREFIX/bin/tplay
echo 'exit' >$PREFIX/bin/tplay
chmod +x $PREFIX/bin/tplay
termux-setup-storage
echo 'Added tplay to bin !!'
echo -e 'Now You Can Launch TPlay just by typing \e[1;31mtplay\e[1;33m anywhere!!!'
read -p 'Press Enter Key To Continue..' k
elif [ $opt -eq 4 ];then
apt install git -y
git clone https://github.com/OnlineHacKing/SM-Play
echo -e "\e[1;34m Downloading Latest Files..."
if [[ -s SM-Play/setup.sh ]];then
cd SM-Play
cp -r -f * .. > temp
cd ..
rm -rf  SM-Play >> temp
rm update.speedx >> temp
rm temp
chmod +x setup.sh
./setup.sh
fi
echo -e "\e[1;32m The Script Will Now Restart Please Choose Install Depedencies (option 1) To Verify the Working Of SM-Play..."
echo -e "\e[1;34m Press Enter To Proceed To Restart..."
read a6
exit
elif [ $opt -eq 5 ];then
echo ' '
echo ' Available Commands are:--- '
echo '         play                  - Plays Paused Music   [OnlineHacKing] '
echo '          play <track_number>   - Plays The Song With That Track Number ( EX- play 3 ) '
echo '          pause                 - Pauses Playing Music    [OnlineHacKing] '
echo '          next                  - Plays Next Song    [OnlineHacKing] '
echo '          prev                  - Plays Previous Song    [OnlineHacKing] '
echo '          random                - Plays Random Song    [OnlineHacKing] '
echo '          quit / exit           - Stops Playing Music And Exits Player    [OnlineHacKing] '
echo '          info                  - Gets Info of Currently Playing Song    [OnlineHacKing] '
echo '          reload                - Rescans The Phone Memory For MP3 files and creates A New List '
echo '          ref                   - Refreshes The Screen    [OnlineHacKing] '
echo '          remove <track_number> - Removes Song With Respective Number From PlayList '
echo '          sort                  - Sort The List According To Path    [OnlineHacKing] '
echo ' '
echo '    ■□■□■□■□■□■□ Social Media □■□■□■□■□■□■ '
echo ' '
echo '   Website :- http://www.onlinehacking-net.cf '
echo '    YouTube Channel :- https://bit.ly/on9youtube '
echo '    Telegram Change :- https://t.me/OnlineHacking '
echo '    Telegram Group :- https://t.me/OnlineHacking0 '
echo '    Github :- https://github.com/OnlineHacKing '
echo '    Facebook :-  https://bit.ly/facebook4page '
echo '    Twitter :- https://bit.ly/twittersuman '
echo '    Instagram :- https://bit.ly/instagram9oh '
read -p 'Press Enter Key To Continue..' k
elif [ $opt -eq 6 ];then
clear
echo -e "\e[1;34m Created By Suman\e[0m"
echo -e "\e[4;32m This Player Was Created By SUMAN \e[0m"
echo -e "\e[1;34m For Any Queries Telegram Message Me\e[0m"
echo -e "\e[1;32m         Telegram: https://t.me/OnlineHacking \e[0m"
echo -e "\e[1;31m          Webside: www.onlinehacking-net.cf \e[0m"
echo -e "\e[1;33m       YouTube Page: https://bit.ly/on9youtube \e[0m"
echo " "
exit 0
else
echo -e "\e[4;32m Invalid Input !!! \e[0m"
echo "Press Enter To Go Home"
read a3
clear
fi
done
