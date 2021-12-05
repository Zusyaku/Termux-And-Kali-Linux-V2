#!bin/bash
#author: AnonyminHack5
termux_ngrok() {
cls || clear
pkg update 
pkg upgrade
pkg install unzip wget -y
pkg install curl
printf "\e[1;97mNgrok in termux will Start to Download Now!!....\e[0m\n"
sleep 1
cd $HOME
curl -LO https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip > /dev/null 2>&1
if [[ -e ngrok-stable-linux-arm.zip ]]; then
unzip ngrok-stable-linux-arm.zip > /dev/null 2>&1
rm -rf ngrok-stable-linux-arm.zip
chmod +x ngrok
printf "\e[1;34m[!] Download Complete!! [!] \e[0m\n"
sleep 1
cls || clear
printf "\e[1;37m=>Now press Enter to visit ngrok website and copy your authtoken<=\e[0m\n"
read a1
termux-open https://ngrok.com
sleep 1
cls || clear
echo -e "\e[0;34m Go to home directory by typing\e[0m\e[1;95m cd $HOME\e[0m\n"
echo ""
cd $HOME
sleep 0.5
printf "\e[0;34m Now paste your authtoken in this format [Ex\e[0m\e[1;97m./ngrok authtoken jhakiwnasskaihaJsv\e[0m\n"
sleep 0.5
printf "\e[1;95mAfter you have pasted your authtoken, then Ngrok has been Successfully Installed in Termux!!\e[0m\n"
sleep 1
cls || clear
echo -e "\e[1;33m Now run\e[0m\e[1;34m ./ngrok http 3333 \e[0m\e[1;33m to Start Ngrok Server\e[0m\n"
sleep 0.5
printf "\e[97mCreated By AnonyminHack5\e[0m\n"
printf "\n"
else
printf "\e[1;31m[\e[0m\e[1;77m!\e[0m\e[1;31m]\e[0m \e[1;76mError\e[0m \e[1;97mCheck your network or internet connection!!\e[1;31m[\e[0m\e[1;77m!\e[0m\e[1;31m]\e[0m\n"
exit 1
fi
}

termux_uninstall() {
printf "\e[1;31mNgrok will be uninstalled into Termux Shortly\e[0m\n"
sleep 0.5
cd $HOME
rm -rf ngrok
sleep 0.5
cls || clear
printf "\e[1;34mNgrok has been successfully removed from Termux\e[0m\n"
printf "\n"
sleep 0.5
cls || clear
menu
}

termux_update() {
clear || cls
printf "\e[1;42mNgrok-toolkit will Start to update now..\e[0m\e[1;44m/\e[0m\n"
sleep 0.5
cd $HOME
rm -rf ngrok-toolkit
git clone https://github.com/TermuxHackz/ngrok-toolkit
cd ngrok-toolkit
cls || clear
printf "\e[1;94m\t[!]UPDATE COMPLETE[!]\e[0m\n"
printf "\e[1;95m\tNow type\e[0m\e[1;96m bash ngrok-toolkit.sh\e[0m\n"
sleep 0.5
exit 1
}

ngrok_windows() {
cls || clear
printf "\e[1;94mNgrok for windows will start to download...\e[0m\n"
sleep 0.5
curl -LO https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-windows-amd64.zip > /dev/null 2>&1
if [[ -e ngrok-stable-windows-amd64.zip ]]; then
unzip ngrok-stable-windows-amd64.zip > /dev/null 2>&1
rm -rf ngrok-stable-windows-amd64.zip
chmod +x ngrok
printf "\e[1;34m[!] Download Complete!! [!] \e[0m\n"
sleep 1
cls || clear
printf "\e[1;37m=>Now press Enter to visit ngrok website and copy your authtoken<=\e[0m\n"
read a1
termux-open https://ngrok.com
sleep 1
cls || clear
echo -e "\e[1;35m Now to go your home directory by typing\e[0m \e[1;77m cd \e[0m"
printf "\e[1;43m Now paste your authtoken in this format [Ex\e[0m\e[1;97m ngrok authtoken jhakiwnasskaihaJsv\e[0m\e[1;43m]\e[0m\n"
cd $HOME
sleep 1
printf "\e[1;95mAfter you have pasted your authtoken, then Ngrok has been Successfully Installed in Termux!!\e[0m\n"
sleep 0.5
echo -e "\e[1;33m Now run\e[0m\e[1;34m ngrok http 3333 \e[0m\e[1;33m to Start Ngrok Server\e[0m\n"
sleep 0.5
printf "\e[97mCreated By AnonyminHack5\e[0m\n"
printf "\n"
cd $HOME
else
printf "\e[1;31m[\e[0m\e[1;77m!\e[0m\e[1;31m]\e[0m \e[1;76mError\e[0m \e[1;97mCheck your network or internet connection!!\e[1;31m[\e[0m\e[1;77m!\e[0m\e[1;31m]\e[0m\n"
exit 1
fi
}

close() {
printf "\e[1;98mYou have now exited from ngrok-toolkit..\e[0m\n"
sleep 0.5
exit 1
}

termux_linux() {
cls || clear
apt-get update
apt-get install curl
apt-get install unzip
curl -LO https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-386.zip > /dev/null 2>&1
if [[ -e ngrok-stable-linux-386.zip ]]; then
unzip ngrok-stable-linux-386.zip > /dev/null 2>&1
rm -rf ngrok-stable-linux-386.zip
chmod +x ngrok
printf "\e[1;34m[!] Download Complete!! [!] \e[0m\n"
sleep 1
cls || clear
printf "\e[1;37m=>Now press Enter to visit ngrok website and copy your authtoken<=\e[0m\n"
read a1
termux-open https://ngrok.com
sleep 1
cls || clear
echo -e "\e[0;34m Go to home directory by typing\e[0m\e[1;95m cd $HOME\e[0m\n"
echo ""
cd $HOME
sleep 0.5
printf "\e[0;34m Now paste your authtoken in this format [Ex\e[0m\e[1;97m./ngrok authtoken jhakiwnasskaihaJsv\e[0m\n"
sleep 0.5
printf "\e[1;95mAfter you have pasted your authtoken, then Ngrok has been Successfully Installed in Termux!!\e[0m\n"
sleep 1
cls || clear
echo -e "\e[1;33m Now run\e[0m\e[1;34m ./ngrok http 3333 \e[0m\e[1;33m to Start Ngrok Server\e[0m\n"
sleep 0.5
printf "\e[97mCreated By AnonyminHack5\e[0m\n"
printf "\n"
else
printf "\e[1;31m[\e[0m\e[1;77m!\e[0m\e[1;31m]\e[0m \e[1;76mError\e[0m \e[1;97mCheck your network or internet connection!!\e[1;31m[\e[0m\e[1;77m!\e[0m\e[1;31m]\e[0m\n"
exit 1
fi
}



	
menu() {
printf "\e[1;33m    _   __                 __       ______            ____   _ __  \e[0m\n"
printf "\e[1;33m   / | / /___ __________  / /__    /_  __/___  ____  / / /__(_) /_ \e[0m\n"
printf "\e[1;33m  /  |/ / __  / ___/ __ \/ //_/_____/ / / __ \/ __ \/ / //_/ / __/ \e[0m\n"
printf "\e[1;36m / /|  / /_/ / /  / /_/ / ,< /_____/ / / /_/ / /_/ / / ,< / / /_   \e[0m\n"
printf "\e[1;36m/_/ |_/\__, /_/   \____/_/|_|     /_/  \____/\____/_/_/|_/_/\__/   \e[0m\n"
printf "\e[1;36m      /____/                                                       \e[0m\n"
printf "\n"
printf "\e[1;28m\tAuthor: \e[0m\e[0;36mAnonyminHack5\e[0m\n"
printf "\e[1;28m\tGithub: \e[0m\e[0;34mTermuxHackz\e[0m\n"
printf "\e[1;28m\tTelegram: \e[0m\e[0;35mAnonyminHack5\e[0m\n"
printf "\n"
printf "\e[104m This tool is meant for the installation of ngrok into Termux and Windows PC\e[0m\n"
printf "\n"
printf "\n"
printf "\e[1;31m\t[\e[0m\e[1;32m01\e[0m\e[1;31m]\e[0m\e[1;34mInstall Ngrok in Termux \e[0m\n"
printf "\e[1;31m\t[\e[0m\e[1;32m02\e[0m\e[1;31m]\e[0m\e[1;34mInstall Ngrok in Windows \e[0m\n"
printf "\e[1;31m\t[\e[0m\e[1;32m03\e[0m\e[1;31m]\e[0m\e[1;34mInstall Ngrok in Linux \e[0m\n"
printf "\e[1;31m\t[\e[0m\e[1;32m04\e[0m\e[1;31m]\e[0m\e[1;34mUninstall Ngrok from Termux \e[0m\n"
printf "\e[1;31m\t[\e[0m\e[1;32m05\e[0m\e[1;31m]\e[0m\e[1;34mUpdate Script \e[0m\n"
printf "\e[1;31m\t[\e[0m\e[1;32m06\e[0m\e[1;31m]\e[0m\e[1;34mExit Ngrok-toolkit\e[0m\n"
printf "\n"
read -p "Chooose your option: " choose

if [[ $choose == 01 || $choose == 1 ]]; then
termux_ngrok
elif [[ $choose == 02 || $choose == 2 ]]; then
ngrok_windows
elif [[ $choose == 03 || $choose == 3 ]]; then
termux_linux
elif [[ $choose == 04 || $choose == 4 ]]; then
termux_uninstall
elif [[ $choose == 05 || $choose == 5 ]]; then
termux_update
elif [[ $choose == 06 || $choose == 6 ]]; then
close

else
printf "\e[1;96mInvalid Option!!!\e[0m"
sleep 1
clear
menu
fi
}
cls || clear
menu




















