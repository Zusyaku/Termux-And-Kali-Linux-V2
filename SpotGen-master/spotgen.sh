#!/bin/bash


# Name: Spotify Account Generator
# Author: Arya Narotama (4WSec)
# Github: github.com/aryanrtm
# Instagram: instagram.com/aryanrtm_
# Give me the credits if you recode this tool. Don't be a SKID!
# 09-2019

# Color
GR=$(tput setaf 2)
RD=$(tput setaf 1)
YW=$(tput setaf 3)
CY=$(tput setaf 6)
NT=$(tput sgr0)
B=$(tput bold)

# List of User Agent
ua[0]="Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
ua[1]="Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"
ua[2]="Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"
ua[3]="Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1"
ua[4]="Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D57"
ua[5]="Mozilla/5.0 (iPhone; CPU iPhone OS 12_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"
ua[6]="Mozilla/5.0 (Linux; Android 9; SM-G960F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36"
ua[7]="Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.83 Mobile Safari/537.36"
ua[8]="Mozilla/5.0 (Linux; Android 9; SM-G950F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36"
ua[9]="Mozilla/5.0 (iPad; CPU OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36"
ua[10]="Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-en) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4"
ua[11]="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.59.10 (KHTML, like Gecko) Version/5.1.9 Safari/534.59.10"
ua[12]="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A"
ua[13]="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0"
ua[14]="Mac OS X/10.6.8 (10K549); ExchangeWebServices/1.3 (61); Mail/4.6 (1085)"
ua[15]="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7"
ua[16]="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15"
ua[17]="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:45.0) Gecko/20100101 Firefox/45.0"
ua[18]="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_8) AppleWebKit/534.50.2 (KHTML, like Gecko) Version/5.0.6 Safari/533.22.3"
ua[19]="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/601.5.17 (KHTML, like Gecko) Version/9.1 Safari/601.5.17"
ua[20]="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/6.2.8 Safari/537.85.17"
ua[21]="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:48.0) Gecko/20100101 Firefox/48.0"
ua[22]="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36"
ua[23]="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
ua[24]="Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1"
ua[25]="Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.0 Mobile/15E148 Safari/604.1"
ua[26]="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36"
ua[27]="Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1"
ua[28]="Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36"
ua[29]="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.2.5 (KHTML, like Gecko) Version/8.0.2 Safari/600.2.5 (Applebot/0.1; +http://www.apple.com/go/applebot)"
ua[30]="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9"

# Random User Agent
rand=$[$RANDOM % ${#ua[@]}]
IFS=$'\r\n'
get_ua=$(echo ${ua[$rand]})

# List of Country
cntry[0]="es_AR/argentina"
cntry[1]="hy_AM/armenia"
cntry[2]="en_AU/australia"
cntry[3]="at_AT/austria"
cntry[4]="de_AT/austria"
cntry[5]="bn_BD/bangladesh"
cntry[6]="fr_BE/belgium"
cntry[7]="nl_BE/belgium"
cntry[8]="pt_BR/brazil"
cntry[9]="bg_BG/bulgaria"
cntry[10]="en_CA/canada"
cntry[11]="fr_CA/canada"
cntry[12]="zh_CN/china"
cntry[13]="hr_HR/croatia"
cntry[14]="cs_CZ/czech-republic"
cntry[15]="da_DK/denmark"
cntry[16]="fi_FI/finland"
cntry[17]="fr_FR/france-french-republic"
cntry[18]="ka_GE/georgia"
cntry[19]="de_DE/germany"
cntry[20]="el_GR/greece"
cntry[21]="hu_HU/hungary"
cntry[22]="is_IS/iceland"
cntry[23]="en_IN/india"
cntry[24]="id_ID/indonesia"
cntry[25]="fa_IR/iran"
cntry[26]="he_IL/israel"
cntry[27]="it_IT/italy"
cntry[28]="ja_JP/japan"
cntry[29]="ar_JO/jordan"
cntry[30]="kk_KZ/kazakhstan"
cntry[31]="ko_KR/korea"
cntry[32]="lv_LV/latvia"
cntry[33]="lt_LT/lithuania"
cntry[34]="ms_MY/malaysia"
cntry[35]="ro_MD/moldova"
cntry[36]="mn_MN/mongolia"
cntry[37]="me_ME/montenegro"
cntry[38]="ne_NP/nepal"
cntry[39]="nl_NL/netherlands-the"
cntry[40]="en_NZ/new-zealand"
cntry[41]="nb_NO/norway"
cntry[42]="es_PE/peru"
cntry[43]="en_PH/philippines"
cntry[44]="pl_PL/poland"
cntry[45]="pt_PT/portugal-portuguese-republic"
cntry[46]="ro_RO/romania"
cntry[47]="ru_RU/russian-federation"
cntry[48]="ar_SA/saudi-arabia"
cntry[49]="sr_RS/serbia"
cntry[50]="sr_Lan_RS/serbia"
cntry[51]="sr_Cyl_RS/serbia"
cntry[52]="en_SG/singapore"
cntry[53]="sk_SK/slovakia"
cntry[54]="sl_SI/slovenia"
cntry[55]="en_ZA/south-africa"
cntry[56]="es_ES/spain"
cntry[57]="sv_SE/sweden"
cntry[58]="it_CH/switzerland-swiss-confederation"
cntry[59]="de_CH/switzerland-swiss-confederation"
cntry[60]="fr_CH/switzerland-swiss-confederation"
cntry[61]="zh_TW/taiwan"
cntry[62]="tr_TR/turkey"
cntry[63]="en_UG/uganda"
cntry[64]="uk_UA/ukraine"
cntry[65]="en_GB/united-kingdom"
cntry[66]="en_US/united-states-of-america"
cntry[67]="es_VE/venezuela"
cntry[68]="vi_VN/vietnam"

# Random Country
rand2=$[$RANDOM % ${#cntry[@]}];
IFS=$'\r\n';
get_cntry=$(echo ${cntry[$rand2]});

# List of Gender
gndr[0]="male";
gndr[1]="female";
gndr[2]="random";

# Random Gender
rand3=$[$RANDOM % ${#gndr[@]}];
IFS=$'\r\n';
get_gndr=$(echo ${gndr[$rand3]});

# Ratio Config
con="1";
threads="5";

# Fake ID Generator (Female)
url_fakeid="https://fakenametool.net/generator/${get_gndr}/${get_cntry}";
# Spotify Register
url_spotify="https://spclient.wg.spotify.com:443/signup/public/v1/account/";
# Spotify Key
key="142b583129b2df829de3656f9eb484e6";

# Random Number (1-2 Digits) for Day
randnumb=$(echo $((1 + RANDOM % 28)));
# Random Number (4 Digits) for Year
randnumb2=$(echo $((1991 + RANDOM % 20)));
# Random Number (1-2 Digits) for Month
randnumb3=$(echo $((1 + RANDOM % 12)));

# Save Results
save="results.txt"

# Function of Banner
function banner () {
	printf "
\t${GR}${B} _____         _   _____         ${RD}${B}Author: ${NT}${B}4WSec
\t${GR}${B}|   __|___ ___| |_|   __|___ ___ 
\t|__   | . | . |  _|  |  | -_|   |
\t|_____|  _|___|_| |_____|___|_|_|
\t      |_|                        

\t   Spotify Account Generator 💔

"
}

# Function of Spotify Register
function spotify_register () {
	local get_email=$(curl -s "${url_fakeid}" | grep -Po '(?<=Email: ).*?(?=")');
	if [[ -z "$get_email" ]]; then
		printf "${NT}[${RD}!${NT}] ${RD}Failed To Get Email ...\n"
		exit
	fi
	local get_password=$(openssl rand -hex 4);
	local regis=$(curl -s "${url_spotify}" \
	              -H 'User-Agent: '$get_ua'' \
	              -H 'Accept: application/json, text/javascript, */*; q=0.01' \
	              -H 'Accept-Language: en-US,en;q=0.5' --compressed \
	              -H 'Referer: https://www.spotify.com/id/signup/' \
	              -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
	              -H 'X-Requested-With: XMLHttpRequest' \
	              -H 'Connection: keep-alive' \
	              -H 'Pragma: no-cache' \
	              -H 'Cache-Control: no-cache' \
	              --data "iagree=true&birth_day=${randnumb}&platform=Android-ARM&creation_point=client_mobile&password=${get_password}&key=${key}&birth_year=${randnumb2}&email=${get_email}&gender=female&app_version=849800892&birth_month=${randnumb3}&password_repeat=${get_password}");
	local response=$(echo $regis | grep -Po '(?<="status":).*?(?=,)');
	# Get country by email
	local country=$(echo $get_cntry | grep -Po '(?<=_).*?(?=/)');

	if [[ $response =~ '1' ]]; then
		printf "${NT}[${GR}REGISTERED${NT}] - [${CY}$country${NT}] - ${NT}[${YW}`date "+%T"`${NT}] - ${NT}$get_email|$get_password\n"
		echo "[REGISTERED] [$country] $get_email|$get_password" >> $save
	elif [[ $response =~ '20' ]]; then
		printf "${NT}[${RD}FAILED${NT}] - [${CY}$country${NT}] - ${NT}[${YW}`date "+%T"`${NT}] - ${NT}$get_email|$get_password\n"
	else
		printf "${NT}[${RD}UNKNOWN${NT}] - ${NT}[${YW}`date "+%T"`${NT}] - ${NT}$get_email|$get_password\n"
	fi
}

# Function of Looping
function go () {
	echo ""
	IFS=$'\r\n'
	for (( i = 0; i < $amount; i++ )); do
		fast=$((con++))
		if [[ $(expr ${i} % ${threads}) == 0 && $i > 0 ]]; then
			sleep 3
		fi
		spotify_register "${get_email}" "${get_password}" "${fast}" &
	done
	wait
}

banner
echo -ne "${NT}[${GR}*${NT}] ${NT}How Many Accounts To Create: ${YW}"; read amount;
go