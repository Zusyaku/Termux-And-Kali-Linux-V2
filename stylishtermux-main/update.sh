black='\033[0;30m'
red='\033[0;31m'
green='\033[0;32m'
yellow='\033[0;33m'
blue='\033[0;34m'
purple='\033[0;35m'
cyan='\033[0;36m'
white='\033[0;37m'

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
echo -e "${cyan}[${white}+${cyan}] ${yellow}Updating theme....."
if [ -d ~/.oh-my-zsh/themes/powerlevel10k ]
then
    rm -rf ~/.oh-my-zsh/themes/powerlevel10k
fi    
git clone https://github.com/romkatv/powerlevel10k ~/.oh-my-zsh/themes/powerlevel10k
sleep 2
echo -e "${cyan}[${white}+${cyan}] ${yellow}Updating plugin....."
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
echo -e "${cyan}[${white}+${cyan}] ${green}Successfully updated!"