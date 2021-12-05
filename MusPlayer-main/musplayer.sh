#!/data/data/com.termux/files/usr/bin/bash

# MusPlayer
# Version    : 1.0
# Author     : KasRoudra
# Github     : https://github.com/KasRoudra
# Email      : kasroudrakrd@gmail.com
# Contact    : https://m.me/KasRoudra
# Description: Play music in termux.
# Music player termux


white="\033[1;37m"
red="\033[1;31m"
green="\033[1;32m"
yellow="\033[1;33m"
purple="\033[1;35m"
cyan="\033[1;36m"
blue="\033[1;34m"
nc="\033[00m"

info="${cyan}[${white}+${cyan}] ${yellow}"
ask="${cyan}[${white}?${cyan}] ${purple}"
error="${cyan}[${white}!${cyan}] ${red}"
success="${cyan}[${white}√${cyan}] ${green}"

re='^[0-9]+$'

logo="${green} __  __           ____  _
${red}|  \/  |_   _ ___|  _ \| | __ _ _   _  ___ _ __
${blue}| |\/| | | | / __| |_) | |/ _' | | | |/ _ \ '__|
${yellow}| |  | | |_| \__ \  __/| | (_| | |_| |  __/ |
${purple}|_|  |_|\__,_|___/_|   |_|\__,_|\__, |\___|_|
${cyan}                                |___/
${red}                               [By KasRoudra]${nc}
"

helper(){
    if $SHUFFLE; then
    st="On"
    else
    st="Off"
    fi
    if $REPEAT; then
        if [ $REPNUM -eq 0 ]; then
            rt="On ➤ ${cyan}∞ Times"
        else
            rt="On ➤ ${cyan}${REPNUM} Times"
        fi
    else
    rt="Off"
    fi
    echo -e "\n${info}${cyan}List of commands:${yellow}
${purple}> help            ${yellow}Shows this help
${purple}> list            ${yellow}Shows music list
${purple}> chdir${green} <path>    ${yellow}Changes music list directory (current: $blue$DIR$yellow)
${purple}> play${green} <number>   ${yellow}Plays that music
${purple}> play all        ${yellow}Plays all music
${purple}> repeat${green} <number> ${yellow}Repeats the music (current: $blue$rt${yellow})
${purple}> shuffle         ${yellow}Shuffles all music (current: $blue$st$yellow)
${purple}> about           ${yellow}About this program
${purple}> more            ${yellow}More tools from author
${purple}> exit            ${yellow}Exit from this program${nc}"
}

export REPEAT=false
export SHUFFLE=false
export NUMS=0
export RAND=0
export REPNUM=0

if [ `pidof mpv > /dev/null 2>&1` ]; then
    killall mpv
fi
if [ -d "/data/data/com.termux/files/home" ]; then
    if ! [ -d "/sdcard/Music" ]; then
        mkdir /sdcard/Music
    else
        export DIR="/sdcard/Music"
    fi
    export DIR="/sdcard/Music"
else
    if ! [ -d "$HOME/Music" ]; then
        mkdir $HOME/Music
    fi
    export DIR="$HOME/Music"
fi

if ! [ `command -v mpv` ]; then
    echo -e "\n${info}Installing mpv.....\n${nc}"
    pkg install mpv -y
    if [ `command -v mpv` ]; then
	    echo -e "\n${success}Mpv installed!\n${nc}"
    else
	    echo -e "\n${error}Mpv installation failed!\n${nc}"
	    exit
    fi
fi
clear
sleep 0.4
echo -e "$logo"
sleep 0.4
while true; do
	trap '' 2
	sleep 0.2
	printf "\n${yellow}MusPlayer > ${purple}"
	read cmd
	sleep 0.5
	if [ "$cmd" = "help" ]; then
		helper
	elif [ "$cmd" = "list" ]; then
	echo
		getlist=$(ls $DIR | grep mp3)
		replace=${getlist// /%%}
		n=1
		if ! [[ $replace == "" ]]; then
		    for music in $replace; do
		        if (( $n % 2 == 0 )) ; then
		    	    echo -e "${yellow}[$n]${blue} ${music//%%/ }"
		        else
		            echo -e "${green}[$n]${purple} ${music//%%/ }"
		        fi
			((n++))
		    done
		else
		    echo -e "${error}No music here!$blue($DIR)${nc}"
		fi
	elif echo "$cmd" | grep -q "chdir"; then
		path="$(echo "$cmd" | cut -d " " -f 2)"
		if [[ -d "$path" ]]; then
		    export DIR="${path}"
		    echo -e "\n${success}Directory changed!${nc}"
		elif [[ $path == "chdir" ]]; then
		    echo -e "\n${error}Please enter a path!${nc}"
		else
		    echo -e "\n${error}Path do not exist!${nc}"
		fi
	elif echo "$cmd" | grep -q "play"; then
		arg=$(echo "$cmd" | cut -d " " -f 2)
		getlist=$(ls $DIR | grep mp3)
		replace=${getlist// /%%}
		list=()
		for m in $replace; do
			list+=("$m")
		done
		while true; do
		if [[ $arg = "all" || $arg = "play" ]]; then
		    if ! [[ $list == "" ]]; then
		    echo -e "\n${success}Playing all.....${nc}"
		    if $SHUFFLE; then
		    while true; do
		        trap 'break' 2
		        cd $DIR
		        export NUMS=`ls *.mp3 | wc -l`
		        export RAND=`shuf -i 1-${NUMS} -n 1`
		        music=${list[(($RAND))]}
		        echo -e "\n${success}${blue}${music//%%/ }\n${nc}"
		        mpv "$DIR/${music//%%/ }"
		        done
		    break
		    else
			    for ms in $replace; do
			        echo -e "\n${success}${blue}${ms//%%/ }\n${nc}"
				    trap 'break' 2
				    mpv "$DIR/${ms//%%/ }"
			    done
			break
			fi
			else
			   echo -e "\n${error}No music!${nc}"
			   break
			fi
		elif ! [[ $arg =~ $re ]]; then
		    echo -e "\n${error}Not a number!${nc}"
		    break
		else
			music=${list[(($arg-1))]}
			if [[ ${music//%%/ } == "" ]]; then
		        echo -e "\n${error}Music not found!"
		    else
			    echo -e "\n${success}Playing ${music//%%/ }\n${nc}"
			    if $REPEAT; then
			        if [[ "$REPNUM" != "0" ]]; then
			             j=0
			             while [ $j -lt $REPNUM ]; do
			             trap 'break' 2
			             mpv "$DIR/${music//%%/ }"
			             ((j++))
			             done
			        else
			            while true ; do
			            trap 'break' 2
			            mpv "$DIR/${music//%%/ }"
			            done
			        fi
			    else
			        trap 'break' 2
			        mpv "$DIR/${music//%%/ }"
			    fi
			fi
			break
		fi
		done
	elif echo "$cmd" | grep -q "repeat"; then
	arg2=$(echo "$cmd" | cut -d " " -f 2)
	    if [[ $REPEAT = false || $arg2 =~ "$re" ]]; then
	        if [[ $arg2 =~ $re && $arg2 != 0 ]]; then
	            export REPNUM="$arg2"
	        elif [[ "$arg2" == "repeat" || "$arg2" == "∞" ]]; then
	            export REPNUM=0
	        elif [[ "$arg2" == "on" || "$arg2" == "On" || "$arg2" == "ON"   ]]; then
	            printf ""
	        else
	            echo -e "\n${error}Invalid argument for repeat!${nc}"
	        fi
	        export REPEAT=true
	        echo -e "\n${success}Repeat turned on!${nc}"
	    elif [[ $REPEAT = true && $arg2 != "repeat" ]]; then
	        if [[ $arg2 =~ $re && $arg2 != 0 ]]; then
	            export REPNUM="$arg2"
	        elif [[ "$arg2" == "off" || "$arg2" == "Off" || "$arg2" == "OFF"   ]]; then
	            printf ""
	        else
	           echo -e "\n${error}Invalid argument for repeat!${nc}"
	        fi
	    else
	        export REPEAT=false
	        echo -e "\n${success}Repeat turned off!${nc}"
	    fi

	elif echo "$cmd" | grep -q "shuffle"; then
	    if [ $SHUFFLE = false ]; then
	        export SHUFFLE=true
	        echo -e "\n${success}Shuffle turned on!${nc}"
	    else
	        export SHUFFLE=false
	        echo -e "\n${success}Shuffle turned off!${nc}"
	    fi
	elif echo "$cmd" | grep -q "about"; then
	    clear
	    echo -e "$logo"
        echo -e "$red[ToolName]  ${cyan}  :[MusPlayer]
$red[Version]    ${cyan} :[1.0]
$red[Description]${cyan} :[Music player for termux]
$red[Author]     ${cyan} :[KasRoudra]
$red[Github]     ${cyan} :[https://github.com/KasRoudra] 
$red[Messenger]  ${cyan} :[https://m.me/KasRoudra]
$red[Email]      ${cyan} :[kasroudrakrd@gmail.com]"
    read -p ">>> " abot
    clear
    echo -e "$logo"
	elif echo "$cmd" | grep -q "more"; then
	    xdg-open "https://github.com/KasRoudra/KasRoudra#My-Best-Works"
	    clear
		echo -e "$logo"
    elif [ "$cmd" = "clear" ]; then
		clear
		echo -e "$logo"
	elif [ "$cmd" = "exit" ]; then
		echo -e "${nc}"
		exit
	else
		echo -e "\n${error}Sorry, wrong input! Please type 'help'${nc}"
	fi
done
