#!/bin/bash
echo -e "\e[1;34m Setting up tool environment----//--wait--" | lolcat
sleep 3
echo "Subscribe to my github repository to continue with the tool" | lolcat
sleep 6
xdg-open https://github.com/TermuxHackz
echo -e "\e[0;90m =====[Setup complete]====="
sleep 3
clear
logo()
{                        
    echo ""
    echo -e "\e[91m\e[5m┏━╸┏┓╻┏━╸┏━┓╺┳┓┏━╸┏━┓   \e[25m\e[93m╻ ╻   \e[5m\e[92m╺┳┓┏━╸┏━╸┏━┓╺┳┓┏━╸┏━┓"
    echo -e "\e[91m\e[5m┣╸ ┃┗┫┃  ┃ ┃ ┃┃┣╸ ┣┳┛   \e[25m\e[93m┏╋┛    \e[5m\e[92m┃┃┣╸ ┃  ┃ ┃ ┃┃┣╸ ┣┳┛"
    echo -e "\e[91m\e[5m┗━╸╹ ╹┗━╸┗━┛╺┻┛┗━╸╹┗╸   \e[25m\e[93m╹ ╹   \e[5m\e[92m╺┻┛┗━╸┗━╸┗━┛╺┻┛┗━╸╹┗╸"
    echo -e "\e[25m\e[93m  A BAS64 ENCODER AND DECODER BY ANONYMINHACK5" | lolcat
}

menu()
{
    echo ""
    echo -e "\e[93m[01] Encode BAS64"
    echo -e "\e[93m[02] Decode BAS64"
    echo -e "\e[93m[03] Update Script"
    echo -e "\e[93m[00] Exit "
    echo ""
}
close()
{
    clear
    exit
}

logo
menu
read -p "Choose option: " choose

if [[ $choose == "01" || $choose == "1" ]];
then
clear
logo
echo ""
read -p "Enter text to encode: " text
echo ""
echo $text | base64
elif [[ $choose == "02" || $choose == "2" ]];
then
clear
logo
echo ""
read -p "Enter hash to encode: " hashes
echo ""
echo $hashes | base64 --decode
elif [[ $choose == "03" || $choose == "3" ]];
then
clear
figlet Updating.. 
sleep 2
echo ""
pkg install git
pip install lolcat
pip install figlet
cd $HOME
rm -rf Bas64
git clone https://github.com/TermuxHackz/Bas64
cd Bas64
python install.py
else 
echo -e "\e[1;97m Invalid Command!!! " 
fi