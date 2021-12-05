#!/data/data/com.termux/files/usr/bin/bash

# MusPlayer
# Version    : 1.0
# Author     : KasRoudra
# Github     : https://github.com/KasRoudra
# Email      : kasroudrakrd@gmail.com
# Contact    : https://m.me/KasRoudra
# Description: Play music in termux.
# Music player termux

white="\033[1;37m"
red="\033[1;31m"
green="\033[1;32m"
yellow="\033[1;33m"
purple="\033[0;35m"
cyan="\033[0;36m"
blue="\033[1;34m"
info="${cyan}[${white}+${cyan}] ${yellow}"
error="${cyan}[${white}!${cyan}] ${red}"
success="${cyan}[${white}√${cyan}] ${green}"
clear
echo -e "${green} __  __           ____  _
${red}|  \/  |_   _ ___|  _ \| | __ _ _   _  ___ _ __
${blue}| |\/| | | | / __| |_) | |/ _' | | | |/ _ \ '__|
${yellow}| |  | | |_| \__ \  __/| | (_| | |_| |  __/ |
${purple}|_|  |_|\__,_|___/_|   |_|\__,_|\__, |\___|_|
${cyan}                                |___/
${red}                               [By KasRoudra]
"
sleep 1
if ! [ `command -v mpv` ]; then
echo -e "\n${info}Installing mpv.....\n"
pkg install mpv -y
if [ `command -v mpv` ]; then
	echo -e "\n${success}Mpv installed!"
else
	echo -e "\n${error}Mpv installation failed!"
	exit
fi
fi
chmod +x *
echo -e "\n${info}Installing files.......\n"
sleep 1
cp -r musplayer.sh $PREFIX/etc
cp -r musplayer $PREFIX/bin
echo -e "${success}MusPlayer successfully installed.\n"
sleep 1
echo -e "${info}Run \"musplayer\" from anywhere and enjoy!\n"