clear
green='\e[1;32m'
cyan='\e[1;36m'
red='\e[1;31m'
blue='\e[1;34m'
white='\e[1;35m'
yellow='\e[1;33m'
echo -e $red "__________       _______ _______    ";
echo -e $red "\__   __( (    /(  ____ (  ___  )   ";
echo -e $red "   ) (  |  \  ( | (    \/ (   ) |   ";
echo -e $red "   | |  |   \ | | (__   | |   | |   ";
echo -e $red "   | |  | (\ \) |  __)  | |   | |   ";
echo -e $red "   | |  | | \   | (     | |   | |   ";
echo -e $red "___) (__| )  \  | )     | (___) |   ";
echo -e $red "\_______//    )_)/      (_______)   ";
echo -e $red "                                    ";
echo -e $green " The Script By:$red KiNg-HaCkInG"
echo -e $green "      TELEGREM:$red HACHEER1"
echo
echo
echo -e $red"{$blue 1$red }$green My Ip"
echo
echo -e $red"{$blue 2$red }$green Info Ip and Site"
echo
echo -e $red"{$blue 3$red }$green Host DNS Finder"
echo
echo -e $red"{$blue 4$red }$green Scanner Port"
echo
echo -e $red"{$blue 5$red }$green Host Finder"
echo
echo -e $red"{$blue 6$red }$green info domain"
echo
echo -e $red"{$blue 7$red }$green Extract Links"
echo
echo -e $red"{$blue 0$red }$green EXIT"
echo
echo
read -p "Enter The Number: " ipp
if [ $ipp = 1 ]
then
echo -e $cyan
ip=$(curl -s https://api.ipify.org)
echo "My public IP address is: $ip"
echo
echo -e $blue
read -p "Preas Any Kay To The Back" enter
bash info.sh
fi
if [ $ipp = 2 ]
then
echo
read -p "Enter The Ip or site: " ip
curl http://ip-api.com/$ip
echo
echo -e $blue
read -p "Preas Any Kay To The Back" enter
bash info.sh
fi
if [ $ipp = 3 ]
then
echo
read -p "Enter The Site: " site
curl https://api.hackertarget.com/mtr/?q=$site
echo
echo -e $blue
read -p "Preas Any Kay To The Back" enter
bash info.sh
fi
if [ $ipp = 4 ]
then
echo
read -p "Enter The Ip or Site: " port
curl http://api.hackertarget.com/nmap/?q=$port
echo
echo -e $blue
read -p "Preas Any Kay To The Back" enter
bash info.sh
fi

if [ $ipp = 5 ]
then
echo
read -p "Enter The Site: " s
s=$(curl -s http://api.hackertarget.com/hostsearch/?q=$s)
echo "The host is: $s"
echo
echo -e $blue
read -p "Preas Any Kay To The Back" enter
bash info.sh
fi
if [ $ipp = 6 ]
then
echo
read -p 'Enter The domain: ' mail
curl -H "Accept: application/json" \
https://check-host.net/check-tcp?host=smtp://$mail&max_nodes=1
echo
echo -e $blue
echo
echo
read -p "Preas Any Kay To The Back" enter
bash info.sh
fi
if [ $ipp = 7 ]
then
echo
read -p "Enter The domain: " df
echo -e $red
curl https://api.hackertarget.com/pagelinks/?q=$df
echo
echo -e $blue
read -p "Preas Any Kay To The Back" enter
bash info.sh
fi
if [ $ipp = 0 ]
then
clear
echo
echo
echo
echo
echo
echo -e $green "         TELEGRAM:$red HACKEER1"
echo -e $green "         FACEBOOK:$red KING.HACKING.SY"
echo -e $green "         WHATSAPP:$red 00963937376654"
echo
echo
echo
echo
exit
else
bash info.sh
fi

