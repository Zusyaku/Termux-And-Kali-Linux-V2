#!/bin/bash


# Shell Checker
# Author: Arya Narotama (4WSec)
# Team: Anon Cyber Team - anoncyberteam.or.id
# Github: github.com/aryanrtm
# Instagram: instagram.com/aryanrtm_
# 07-2019 - 4WSec

# Date
time=$(date +%d_%m_%y)

# Color
GR='\033[92m'; # Green
YW='\033[93m'; # Yellow
RD='\033[91m'; # Red
NT='\033[97m'; # Netral

# Add Words Here
word1="Shell";
word2="wso";
word3="b374k";
word4="IndoXploit";
word5="backdoor";
word6="cyber";

# User Agent
UserAgent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.89 Safari/537.36";


function banner () {
	printf "
	⚡ \e[1;92mShell Checker by 4WSec ⚡\e[0m\n\n"
}


function shell_checker () {
	local req=$(curl -s -L "${URL}" -I \
	            --user-agent "${UserAgent}" \
	            -w %{http_code} -m 5 | grep "200 OK");

	if [[ $req == 200 ]] || [[ $req =~ '200 OK' ]]; then
		printf " ${GR}[LIVE] ${YW}-> ${NT}${URL}\n"
		echo " [LIVE] $URL" | uniq | sort >> shell_live_$time.txt

	elif [[ $req =~ "${word1}" ]] || [[ $req =~ "${word2}" ]] || [[ $req =~ "${word3}" ]] || [[ $req =~ "${word4}" ]] || [[ $req =~ "${word5}" ]] || [[ $req =~ "${word6}" ]]; then
		printf " ${GR}[LIVE] ${YW}-> ${NT}${URL}\n"
		echo " [LIVE] $URL" | uniq | sort  >> shell_live_$time.txt
	else
		printf " ${RD}[DIE] ${YW}-> ${NT}${URL}\n"
	fi
}


banner
printf " ${NT}[${RD}+${NT}] ${YW}Enter List Shell: ${NT}"; read list;
if [ ! -f $list ]; then
    printf " ${NT}[${RD}!${NT}] ${RD}File Not Found ...\n"
	exit 0
fi

printf " ${NT}[${RD}+${NT}] ${YW}Enter Threads (Default 20): ${NT}"; read threads;
if [[ $threads == "" ]]; then
	threads=20;
fi
printf "\n ---------------------------------------\n\n"

IFS=$'\r\n'
con=1;
for URL in $(cat $list); do
	fast=$(expr $con % $threads);
	if [[ $fast == 0 && $con > 0 ]]; then
		sleep 3
	fi
	shell_checker &
	con=$[$con+1];
done
wait
