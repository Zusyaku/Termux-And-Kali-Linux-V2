#!/bin/bash
#author: AnonyminHack5
#Team: TermuxHackz Society
clear || cls
echo -e "\e[32m    _____ __             __  ___     __   "
echo -e "   / ___// /____  ____ _/ / / (_)___/ /__ "
echo -e "   \__ \/ __/ _ \/ __ '/ /_/ / / __  / _ \ "
echo -e "  ___/ / /_/  __/ /_/ / __  / / /_/ /  __/ "
echo -e " /____/\__/\___/\__, /_/ /_/_/\__,_/\___/ "
echo -e "               /____/ v1.0 \e[0m     "
menu() {
	printf "\e[1;93mSteghide is a tool that can be used for embedding payload apk into image\e[0m\n"
	printf "\e[1;37mAll you need to do is to follow the instructions from the README.md file and also follow the menu\e[0m\n"
	printf "\n"
	printf "\e[1;93m\tAuthor: AnonyminHack5\e[0m\n"
	printf "\e[1;93m\tTeam: TermuxHackz Society\e[0m\n"
	printf "\e[1;94m\tFacebook: AnonyminHack5\e[0m\n"
	printf "\e[1;94m\tWhatsapp: +2349033677589\e[0m\n"
	
}
echo -e " -\e[90m(https://github.com/TermuxHackz)\e[0m"
# 94 light blue
# 90 gray
menu
printf "\n"
echo -e "\e[31m[\e[0m\e[32m~\e[0m\e[31m]\e[0m \e[32mPlease Choose:\e[0m\e[34m\e[0m"
echo -e " 01. Embed a file in an image (jpeg, au, etc)"
echo -e " 02. Extract an image"
echo -e " 03. View Information of an image"
echo -e " 04. Exit steghide"
echo ""
read -p "Choose your option bro: " zch


if [[ $zch = "1" || $zch = "01" ]]; then
   echo -e "\e[31m[\e[0m\e[32m~\e[0m\e[31m]\e[0m \e[32mEnter an image or file path: \e[0m\e[34m"
   read img
   echo -e "\e[31m[\e[0m\e[32m~\e[0m\e[31m]\e[0m \e[32mEnter file you want to embed:\e[0m\e[34m"
   read file
   echo -e "\e[31m[\e[0m\e[32m~\e[0m\e[31m]\e[0m \e[32mEnter Passkey:\e[0m\e[34m"
   read pass
   echo -e "\e[96m"
   steghide embed -cf $img -ef $file -p "$pass"
   echo -e "\e[0m"

elif [[ $zch = "2" || $zch = "02" ]]; then
   echo -e "\e[31m[\e[0m\e[32m~\e[0m\e[31m]\e[0m \e[32mEnter image or file you want to extract: \e[0m\e[34m"
   read img
   echo -e "\e[31m[\e[0m\e[32m~\e[0m\e[31m]\e[0m \e[32mEnter Passkey:\e[0m\e[34m"
   read pass
   echo -e "\e[96m"
   steghide extract -sf $img -p "$pass"
   echo -e "\e[0m"

elif [[ $zch = "3" || $zch = "03" ]]; then
   echo -e "\e[31m[\e[0m\e[32m~\e[0m\e[31m]\e[0m \e[32mEnter image or file you want to view info:\e[0m\e[34m"
   read img
   echo -e "\e[31m[\e[0m\e[32m~\e[0m\e[31m]\e[0m \e[32mEnter Passkey:\e[0m\e[34m"
   read pass
   echo -e "\e[96m"
   steghide info $img -p "$pass"
   echo -e "\e[0m"
elif [[ $zch = "4" || $zch = "04" ]]; then
exit

else
   printf "\e[91mNot part of the options. Try again bro. 😹😹\e[0m"
   sleep 2
   cls || clear
   bash steghide.sh
fi

