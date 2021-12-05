#!/bin/bash
clear
echo "
888                     888                     
888                     888                     
888                     888                     
88888b.  8888b.  .d8888b888  888 .d88b. 888d888 
888 "88b    "88bd88P"   888 .88Pd8P  Y8b888P"   
888  888.d888888888     888888K 88888888888     
888  888888  888Y88b.   888 "88bY8b.    888     
888  888"Y888888 "Y8888P888  888 "Y8888 888     
                                 ";
                                 
echo "[✔] Checking directories...";
if [ -d "/usr/share/doc/Owl" ] ;
then
echo "[◉] A directory Owl was found! Do you want to replace it? [Y/n]:" ; 
read mama
if [ $mama == "y" ] ; 
then
 rm -R "/usr/share/doc/Owl"
else
 exit
fi
fi

 echo "[✔] Installing ...";
 echo "";
 git clone https://github.com/TermuxHackz/Owl /usr/share/doc/Owl;
 echo "#!/bin/bash 
 python /usr/share/doc/Owl/Owl.py" '${1+"$@"}' > Owl;
 chmod +x Owl;
 cp Owl /usr/bin/;
 rm Owl;


if [ -d "/usr/share/doc/Owl" ] ;
then
echo "";
echo "[✔]Tool installed with success![✔]";
echo "";
  echo "[✔]====================================================================[✔]";
  echo "[✔] ✔✔✔  All is done!! You can execute tool by typing Owl  !     ✔✔✔ [✔]"; 
  echo "[✔]====================================================================[✔]";
  echo "";
else
  echo "[✘] Installation failed![✘] ";
  exit
fi