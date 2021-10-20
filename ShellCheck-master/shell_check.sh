# !/bin/bash
# author : ./Lolz ( JavaGhost Team )
# error ? contact me buddy
# note : iam sorry if my code absurd :(

# useragent
useragent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"

# var_shell
name_shell[0]="option&path="
name_shell[1]="&path="
name_shell[2]="WebShellOrb"
name_shell[3]="<center><form method=post>Password:"
name_shell[4]="<pre align=center><form method=post>Password<br>"
name_shell[5]="<pre align=center><form method=post>Password"
name_shell[6]="login_shell"
name_shell[7]="Uploader"
name_shell[8]="uploader"
#name_shell[9]="<form method=post enctype=multipart/form-data>"
name_shell[11]="?dir="

# color(bold)
red='\e[1;31m'
green='\e[1;32m'
yellow='\e[1;33m'
blue='\e[1;34m'
magenta='\e[1;35m'
cyan='\e[1;36m'
white='\e[1;37m'

# banner
echo -e '''
                   \e[1;31m-\e[1;37m JavaGhost Shell Checker \e[1;31m-\e[1;37m

1\e[1;31m). \e[1;37mCheck shell with show information shell \e[1;34m[\e[1;32m system \e[1;34m\e[1;31m+\e[1;32m name \e[1;34m] \e[1;31m-\e[1;34m [ \e[1;32minfo \e[1;34m:\e[1;32m not fast \e[1;34m]\e[1;37m
2\e[1;31m). \e[1;37mCheck shell without show information \e[1;34m[\e[1;32m very fast \e[1;34m]\e[1;37m
'''

# asking
read -p $'\e[1;37m[\e[1;31m?\e[1;37m]\e[1;37m Choose one \e[1;31m:\e[1;32m ' a_menu
read -p $'\e[1;37m[\e[1;31m?\e[1;37m]\e[1;37m Input your list shell \e[1;31m:\e[1;32m ' a_list
echo ""

# run
case $a_menu in
	1 )
		l_thread=2
		function checkingShell_showInfo(){
			c_shell=$(curl -sk --connect-timeout 35 --max-time 35 --user-agent "${useragent}" -XGET "${l_shell}" -L)
			if [[ $c_shell =~ "${name_shell[0]}" || $c_shell =~ "${name_shell[1]}" || $c_shell =~ "${name_shell[2]}" || $c_shell =~ "${name_shell[11]}" ]]; then
				local n_shell=$(curl -sk --connect-timeout 35 --max-time 35 --user-agent "${useragent}" --url "${l_shell}" | grep -o "<title>.*" | cut -d ">" -f2 | cut -d "<" -f1)
				echo -ne " ${white}[${green}LIVE${white}] ${blue}-${white} ${l_shell} ${blue}:${green} [ ${white}Name shell ${blue}:${green} ${n_shell} ${blue}- "
				echo $l_shell >> ShellLive.txt
				local cs_shell=$(curl -sk --connect-timeout 35 --max-time 35 --user-agent "${useragent}" --url "${l_shell}")
				if [[ $cs_shell == "System" || $cs_shell == "system" ]]; then
					local s_shell=$(curl -sk --connect-timeout 35 --max-time 35 --user-agent "${useragent}" --url "${l_shell}" | grep -o "Linux.*\|Ubuntu.*\|Windows.*\|CentOS.*" | cut -d "<" -f1)
					echo -e "${white}Sys ${blue}:${green} ${s_shell} ${white}]"
				elif [[ $cs_shell =~ "${name_shell[2]}" ]]; then
					#statements
					local wso_uname=$(curl -sk --connect-timeout 35 --max-time 35 --user-agent "${useragent}" --url "${l_shell}" |  grep -o "Cwd:.*" | cut -d ">" -f5 | cut -d "<" -f1)
					echo -e "${white}Sys ${blue}:${green} ${wso_uname} ${white}]"
				elif [[ $cs_shell == "Con7ext" ]]; then
					echo -e " ${white}Sys ${blue}:${cyan} Not showing, maybe this mini shell ${green}]${white}"
				else
					echo -e " ${white}Sys ${blue}:${cyan} Not showing, maybe this mini shell ${green}]${white}"
				fi
			elif [[ $c_shell =~ "${name_shell[3]}" || $c_shell =~ "${name_shell[4]}" || $c_shell =~ "${name_shell[5]}" || $c_shell =~ "${name_shell[6]}" ]]; then
				echo -e " ${white}[${green}LIVE${white}] ${blue}-${white} ${l_shell} ${blue}:${green} [ ${white}Shell with password ${blue}:${red} can't show information ${green}]${white}"
				echo $l_shell >> ShellLive.txt
			elif [[ $c_shell =~ "${name_shell[7]}" || $c_shell =~ "${name_shell[8]}" ]]; then
				echo -e " ${white}[${green}LIVE${white}] ${blue}-${white} ${l_shell} ${blue}:${green} [ ${yellow}This is uploader${green} ]${white}"
				echo $l_shell >> ShellLive.txt
			else
				echo -e " ${white}[${red}DEAD${white}] ${blue}-${white} ${l_shell}"
				echo $l_shell >> ShellDead.txt
			fi
		}		

		(
			for l_shell in $(cat $a_list); do
				((theread=theread%$l_thread)); ((theread++==0)) && wait
				checkingShell_showInfo "$l_shell" &
			done
			wait
		)
		;;
	2 )
		l_thread=50
		function just_checkingShell(){
			c_shell=$(curl -sk --connect-timeout 20 --max-time 20 --user-agent "${useragent}" -XGET "${l_shell}" -L)
			if [[ $c_shell =~ "${name_shell[0]}" || $c_shell =~ "${name_shell[1]}" || $c_shell =~ "${name_shell[2]}" || $c_shell =~ "${name_shell[3]}" || $c_shell =~ "${name_shell[4]}" || $c_shell =~ "${name_shell[5]}" || $c_shell =~ "${name_shell[6]}" || $c_shell =~ "${name_shell[7]}" || $c_shell =~ "${name_shell[8]}" || $c_shell =~ "${name_shell[11]}" ]]; then
				echo -e " ${white}[${green}LIVE${white}] ${blue}-${white} ${l_shell}"
				echo $l_shell >> ShellLive.txt
			else
				echo -e " ${white}[${red}DEAD${white}] ${blue}-${white} ${l_shell}"
			fi
		}

		(
			for l_shell in $(cat $a_list); do
				((theread=theread%$l_thread)); ((theread++==0)) && wait
				just_checkingShell "$l_shell" &
			done
			wait
		)
		;;
	* )
		echo -e "${red}ERROR${white}"
esac

echo -e "\n${white}[${green}+${white}] Total shell live ${blue}:${green} $(< ShellLive.txt wc -l) ${blue}-${white} Saved in ${blue}:${green} $(pwd)${white}"
# end
