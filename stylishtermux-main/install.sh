#!/data/data/com.termux/files/usr/bin/bash

black='\033[0;30m'
red='\033[0;31m'
green='\033[0;32m'
yellow='\033[0;33m'
blue='\033[0;34m'
purple='\033[0;35m'
cyan='\033[0;36m'
white='\033[0;37m'

info="${cyan}[${white}+${cyan}] ${yellow}"
ask="${cyan}[${white}?${cyan}] ${purple}"
error="${cyan}[${white}!${cyan}] ${red}"
success="${cyan}[${white}√${cyan}] ${green}"

clear
cat <<- EOF

╔═══╗╔╗────╔╗────╔╗╔════╗
║╔═╗╠╝╚╗───║║────║║║╔╗╔╗║
║╚══╬╗╔╬╗─╔╣║╔╦══╣╚╩╣║║╠╩═╦═╦╗╔╦╗╔╦╗╔╗
╚══╗║║║║║─║║║╠╣══╣╔╗║║║║║═╣╔╣╚╝║║║╠╬╬╝
║╚═╝║║╚╣╚═╝║╚╣╠══║║║║║║║║═╣║║║║║╚╝╠╬╬╗
╚═══╝╚═╩═╗╔╩═╩╩══╩╝╚╝╚╝╚══╩╝╚╩╩╩══╩╝╚╝
───────╔═╝║
───────╚══╝

EOF
chmod 777 *
if ! [[ `command -v git` ]]
then
    echo -e "${info}Installing git...\n $white"
    pkg install git -y
fi
if ! [[ `command -v figlet` ]]
then
    echo -e "${info}Installing figlet...\n $white"
    pkg install figlet -y
fi  
echo -e "${info}Checking Oh-My-Zsh existence....\n $white"
sleep 1
if [ ! -d ~/.oh-my-zsh ]
then
    echo -e "${error}Oh-My-Zsh not Found!\n $white"
    echo -e "${info}Installing Oh-My-Zsh...\n $white"
    sleep 1
    pkg install zsh -y 
    git clone git://github.com/robbyrussell/oh-my-zsh.git "$HOME/.oh-my-zsh" --depth 1
    chsh -s zsh
else
    echo -e "${success}Oh-My-Zsh Found!\n $white"
    sleep 1
    echo -e "${info}Creating backup...\n $white"
    sleep 1
    cp -r ~/.zshrc /data/data/com.termux/files/usr/etc
    cp -r ~/.termux/font.ttf /data/data/com.termux/files/usr/etc
fi    
echo -e "${info}Installing theme....\n $white"
sleep 1
if [ -d ~/.oh-my-zsh/themes/powerlevel10k ]
then
    rm -rf ~/.oh-my-zsh/themes/powerlevel10k
fi    
git clone https://github.com/romkatv/powerlevel10k ~/.oh-my-zsh/themes/powerlevel10k
sleep 2
echo -e "${info}Installing plugin....\n $white"
if [ -d ~/.oh-my-zsh/plugins/zsh-autosuggestions ]
then
    rm -rf ~/.oh-my-zsh/plugins/zsh-autosuggestions
fi    
if [ -d ~/.oh-my-zsh/plugins/zsh-syntax-highlighting ]
then
    rm -rf ~/.oh-my-zsh/plugins/zsh-syntax-highlighting
fi    
git clone https://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting ~/.oh-my-zsh/plugins/zsh-syntax-highlighting
sleep 2
echo -e "${info}Changing font.....\n $white"
sleep 1
termux-reload-settings
cp -r font.ttf ~/.termux
sleep 1
echo -e "${ask}Enter your name to be displayed in home : ${green}" 
read -p "--> " name
if [ "$name" = "" ]
then
    echo -e "${error}No name...\n $white"
else
    echo "figlet $name" >> "/data/data/com.termux/files/usr/etc/zshrc"
fi
echo -e "${info}Finishing installation...\n $white"
sleep 1
cp -r .zshrc ~
cp -r .p10k.zsh ~
rm -rf ~/../usr/etc/motd
cp -r removeall /data/data/com.termux/files/usr/bin
echo -e "${info}Use 'removeall' to remove theme, plugin and restore backup\n $white"
sleep 1
echo -e "${success}Installation complete!\n $white"
sleep 1
echo -e "${info}You can change theme configuration by 'p10k configure'\n $white"
sleep 1
echo -e "${success}Restart Termux to see effects!\n $white"
