# !/bin/bash
# Created by 	: ./LazyBoy - JavaGhost Team
# Contact 		: https://fb.me/n00b.me - httpsL//t.me/noolep

# color(bold)
red='\e[1;31m'
green='\e[1;32m'
yellow='\e[1;33m'
blue='\e[1;34m'
magenta='\e[1;35m'
cyan='\e[1;36m'
white='\e[1;37m'

# create file
array_file=("twilio_cant_get_num" "twilio_can_send" "twilio_cant_send" "twilio_trial")
for file in ${array_file[@]}; do
	touch "${file}-$(date +"%Y-%m-%d").txt" auth_twilio.tmp
done

# to number [ You can change it if u want - ONLY US NUMBER ]
to_number="+19379492383"

# banner
echo '''
		     ┌┬┐┬ ┬┬┬  ┬┌─┐   ┌─┐
		      │ │││││  ││ │───│  
		      ┴ └┴┘┴┴─┘┴└─┘   └─┘
		 - JavaGhost Twilio Checker -
'''

# asking
read -p $'\e[1;37m[ \e[1;32m? \e[1;37m] Type [ \e[1;32m1 \e[1;37m] For Single Check or Type [ \e[1;32m2 \e[1;37m] \e[1;37mFor Mass Check \e[1;34m: \e[1;32m' ask_opt

# option
if [[ $ask_opt == "1" ]]; then
	echo ""
	read -p $'\e[1;37m[ \e[1;32m? \e[1;37m] Input AUTH SID   \e[1;34m: \e[1;32m' ask_auth
	read -p $'\e[1;37m[ \e[1;32m? \e[1;37m] Input AUTH TOKEN \e[1;34m: \e[1;32m' ask_token
	echo "$ask_auth:$ask_token" >> auth_twilio.tmp
elif [[ $ask_opt == "2" ]]; then
	echo ""
	echo -e "${white}[ ${red}INFO ${white}] ${blue}- ${white}Just put list with delimiter like this ${blue}: ${green}AUTH_SID:AUTH_TOKEN${white}"
	read -p $'\e[1;37m[ \e[1;32m? \e[1;37m] Input your list \e[1;34m: \e[1;32m' ask_lst
	if [[ ! -e $ask_lst ]]; then
		echo -e "${white}[ ${red}ERROR ${white}] ${blue}- ${red}File not found in your directory${white}"
		exit
		rm auth_twilio.tmp
	else
		cat $ask_lst | sort -u > auth_twilio.tmp
		echo ""
	fi
else
	echo -e "${white}[ ${red}! ${white}] ${red}you select an option that does not exist!${white}"
	exit
	rm auth_twilio.tmp
fi

# twilio api
function twilio_api(){ curl -s -X "${1}" --url "https://api.twilio.com/2010-04-01/${2}/" -u "${twilio_auth}" ; }

# start checking twilio auth
function check_twilio(){
	twilio_type=$(twilio_api POST Accounts.json | grep -Po '"type": "\K[^"]+')
	twilio_balance=$(twilio_api GET "Accounts/$(echo "${twilio_auth}" | cut -d ":" -f1)/Balance.json" | grep -Po '"balance": "\K[^"]+')
	twilio_phone_number=$(twilio_api GET "Accounts/$(echo "${twilio_auth}" | cut -d ":" -f1)/IncomingPhoneNumbers.json" | grep -Po '"phone_number": "\K[^"]+' | head -n1)

	if [[ $twilio_type == "Full" ]]; then
		if [[ -z $twilio_phone_number ]]; then
			echo -e "\n${white}[ ${red}- ${white}] AUTH\t${blue}: ${white}${twilio_auth}\n${white}[ ${green}? ${white}] ACC TYPE  ${blue}: ${green}FULL\n${white}[ ${green}? ${white}] BALANCE   ${blue}: ${green}${twilio_balance}\n${white}[ ${red}- ${white}] ${red}CANT GET NUMBER${white}"
			echo "${twilio_auth}" >> twilio_cant_get_num.txt
		else
			# for check send
			check_send=$(curl -s -X POST https://api.twilio.com/2010-04-01/Accounts/$(echo $twilio_auth | cut -d ":" -f1)/Messages.json \
								--data-urlencode "Body=JavaGhost - Mass Twilio Checker" \
								--data-urlencode "From=$twilio_phone_number" \
								--data-urlencode "To=${to_number}" \
								-u "${twilio_auth}" | grep -o "queued")

			if [[ $check_send == "queued" ]]; then
				echo -e "\n${white}[ ${green}+ ${white}] AUTH\t${blue}: ${green}${twilio_auth}\n${white}[ ${green}? ${white}] ACC TYPE  ${blue}: ${green}FULL\n${white}[ ${green}? ${white}] BALANCE   ${blue}: ${green}${twilio_balance}\n${white}[ ${green}? ${white}] PHONE\t${blue}: ${green}${twilio_phone_number}\n${white}[ ${green}? ${white}] ${yellow}CAN SEND TO US NUMBER${white}" | tee -a twilio_can_send-$(date +"%Y-%m-%d").txt
			else
				echo -e "\n${white}[ ${red}- ${white}] AUTH\t${blue}: ${green}${twilio_auth}\n${white}[ ${green}? ${white}] ACC TYPE  ${blue}: ${green}FULL\n${white}[ ${green}? ${white}] BALANCE   ${blue}: ${green}${twilio_balance}\n${white}[ ${green}? ${white}] PHONE\t${blue}: ${green}${twilio_phone_number}\n${white}[ ${green}? ${white}] ${red}CANT SEND TO US NUMBER${white}" | tee -a twilio_cant_send-$(date +"%Y-%m-%d").txt
			fi
		fi
	elif [[ $twilio_type == "Trial" ]]; then
		echo -e "${white}[ ${red}- ${white}] AUTH ${blue}: ${red}${twilio_auth} ${blue}- ${white}ACC TYPE ${blue}: ${red}TRIAL ${blue}- ${red}SKIPPED FOR CHECKING${white}"
		echo "${twilio_auth}" >> twilio_trial.txt
	else
		echo -e "${white}[ ${red}! ${white}] AUTH ${blue}: ${red}${twilio_auth} ${blue}- ${red}AUTH INVALID${white}"
	fi
}

# multithreading
limit="10"
for twilio_auth in $(cat auth_twilio.tmp); do
	check_twilio "$twilio_auth" &
	while (( $(jobs | wc -l) >= $limit )); do
		sleep 0.1s
		jobs > /dev/null
	done
done
wait

echo -e "\n${white}[ ${green}+ ${white}] GOOD TWILIO SAVED IN ${blue}: ${green}$(pwd)/twilio_can_send-$(date +"%Y-%m-%d").txt${white}"
rm auth_twilio.tmp
