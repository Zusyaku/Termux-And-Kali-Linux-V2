#!/bin/bash

#color(bold)
red='\e[1;31m'
green='\e[1;32m'
yellow='\e[1;33m'
blue='\e[1;34m'
magenta='\e[1;35m'
cyan='\e[1;36m'
white='\e[1;37m'

#User Agent
user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'

#menu + banner
echo -e '''
               ┌┬┐┬ ┬┌─┐  ┌┬┐┌─┐┬─┐┬┌─┌─┐┬─┐
                │ ├─┤├┤    │││ │├┬┘├┴┐├┤ ├┬┘
                ┴ ┴ ┴└─┘  ─┴┘└─┘┴└─┴ ┴└─┘┴└─    
                 \e[1;37m[ Using : \e[1;37m Yahoo \e[1;31m-\e[1;37m Bing ]        
[ Author : \e[1;34m./Lolz \e[1;31m-\e[1;37m Thanks to : IndoSec \e[1;31m-\e[1;37m \e[1;34mJavaGhost \e[1;31m-\e[1;37m Widhisec ]                                                                              

1]. Get domain \e[1;31m+\e[1;37m path \e[1;31m[ \e[1;37mex : \e[1;32mhttps://localhost:1337/path/../.. \e[1;31m]\e[1;37m
2]. Just get domain name \e[1;31m[ \e[1;37mex : \e[1;32mhttps://localhost:1337 \e[1;31m]
'''

read -p $'\e[1;37m[\e[1;31m?\e[1;37m] What do you want: \e[1;32m' opt
read -p $'\e[1;37m[\e[1;31m?\e[1;37m] Input dork: \e[1;32m' dork
echo -e "${white}[${red}-${white}] Please wait...\n"

touch output.txt

#option1
function option1(){
	echo -e "${white}${yahoo}" | grep -aPo '(?<=<span class=" fz-ms fw-m fc-12th wr-bw lh-17">).*?(?=")' | sed 's,<b>,,g;s,</b>,,g' | cut -d "<" -f1
	echo -e "${white}${bing}" | grep -aPo '(?<=<li class="b_algo"><h2><a href=").*?(?=")'
}

#option2
function option2(){
	echo -e "${white}${yahoo}" | grep -aPo '(?<=<span class=" fz-ms fw-m fc-12th wr-bw lh-17">).*?(?=")' | sed 's,<b>,,g;s,</b>,,g' | cut -d "<" -f1 | cut -d "/" -f1
	echo -e "${white}${bing}" | grep -aPo '(?<=<li class="b_algo"><h2><a href=").*?(?=")' | cut -d "/" -f1,2,3
}

#search_engine
function search_engine(){
	yahoo=$(curl -s "https://search.yahoo.com/search?p=$(echo "$dork" | jq -sRr @uri)&b=${i}&pz=${i}" -H "user-agent: ${user_agent}")
	bing=$(curl -s "https://www.bing.com/search?q=$(echo "$dork" | jq -sRr @uri)&first=${i}" -H "user-agent: ${user_agent}")
	if [[ $yahoo =~ "We did not find results for" ]] || [[ $bing =~ "There are no results for" ]]; then
		echo -e "No matching keywords found for : ${green}${dork}${white}" && exit
	else
		if [[ $opt = "1" ]]; then
			option1 && option1 | sed -s 's,amp;,,g' >> output.txt
		elif [[ $opt = "2" ]]; then
				option2 && option2 >> output.txt
			else
				echo ":/"
		fi
	fi
}


(
	for i in $(seq 50); do
		((thread=thread%20)); ((thread++==0)) && wait
		search_engine "$i" &
	done
	wait
)

echo -e "\n[${red}?${white}] Total results: ${green}"$(< output.txt wc -l)
echo -e "${white}[${red}!${white}] Removing all duplicate results..."$(sort -u output.txt > results.txt)
echo -e "${white}[${red}+${white}] Total fresh results: ${green}"$(< results.txt wc -l)
echo -e "${white}[${red}+${white}] Save in : ${green}results.txt${white}"

rm output.txt
#end
