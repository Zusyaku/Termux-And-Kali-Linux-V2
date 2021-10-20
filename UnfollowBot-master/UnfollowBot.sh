#!/bin/bash
# UnfollowBot v1.1
#pembuat :MR.K7C8NG
#GITHUB : https://github.com/pashayogi

trap 'printf "\n";stop;exit 1' 2

############################################################
###################### Bot Config ##########################

## Your Credentials here

default_username_ig=""
default_password_ig=""

## Comments

arr[0]="Profil Anda luar biasa!"
arr[1]="Terlihat bagus"
arr[2]="Umpan Anda bagus"
arr[3]="Gambar Anda sangat bagus!"
arr[4]=":)"
arr[5]="Saya suka tha"
arr[6]="yes!"

############################################################

rand=$[$RANDOM % ${#arr[@]}]
IFS=$'\n'
commt=$(echo ${arr[$rand]})

counter1=0
counter2=0
turn=2
startline_bot=1
endline_bot=1
startline_follow=1
endline_follow=1


csrftoken=$(curl https://www.instagram.com/accounts/login/ajax -L -i -s | grep "csrftoken" | cut -d "=" -f2 | cut -d ";" -f1)

banner() {

printf "\e[1;92m _   _        __       _ _               ____        _  \e[0m\n"
printf "\e[1;92m | | | |_ __  / _| ___ | | | _____      _| __ )  ___ | |_ \e[0m\n"
printf "\e[1;92m | | | | '_ \| |_ / _ \| | |/ _ \ \ /\ / /  _ \ / _ \| __| \e[0m\n"
printf "\e[1;92m | |_| | | | |  _| (_) | | | (_) \ V  V /| |_) | (_) | |_  \e[0m\n"
printf "\e[1;92m  \___/|_| |_|_|  \___/|_|_|\___/ \_/\_/ |____/ \___/ \__|  \e[0m\n"
printf "\n"
printf "\e[1;77m\e[45m Unfollow instagram by MR.K7C8NG       \e[0m\n"
printf "\e[1;28m\e[33m follow ig admin @pranata_pasha bagi yang mau \e[0m\n"
printf "\e[1;35m\e[43m Unfollow bot untuk unfollow pertemanan Instagram kamu   \e[0m\n"
printf "\e[1;37m\e[36m yang sesuai folder txt unfollow.txt \e[0m\n"
printf "\n"                                    

}

dependencies() {


command -v curl > /dev/null 2>&1 || { echo >&2 "I require curl but it's not installed. Run apt-get install curl"; exit 1; }
}

check_unfollow() {
touch unfollow.txt
total_unfollow=$(wc -l unfollow.txt | cut -d " " -f1)

if [ $total_unfollow == "0" ]; then
printf "\e[1;93m[!] Please, put your unfollow on file: \e[0m\e[1;77m unfollow.txt\e[0m\e[1;93m (1 per line, without #)\e[0m\n"
exit 1
fi

}

stop() {
touch likes comments follows unfollows followedtotal.txt
cat follows >> followedtotal.txt
cat unfollows >> unfollowedtotal.txt
session_likes=$(wc -l likes | cut -d " " -f1)
session_comments=$(wc -l comments | cut -d " " -f1)
session_follows=$(wc -l follows | cut -d " " -f1)
session_unfollows=$(wc -l unfollows | cut -d " " -f1)
total_likes=$(wc -l liked.txt | cut -d " " -f1)
total_comments=$(wc -l commented.txt | cut -d " " -f1)
total_follows=$(wc -l followedtotal.txt | cut -d " " -f1)
total_unfollows=$(wc -l unfollowedtotal.txt | cut -d " " -f1)
rm -rf likes comments follows unfollows
printf "\e[1;31m[*] Bot stopped.\e[0m\n"
printf "\n"
printf "\e[1;92m[*] Statistics for this session:\e[0m\n"
printf "\e[1;93m[*] Likes: \e[0m\e[1;77m%s\e[0m\n" $session_likes
printf "\e[1;93m[*] Comments: \e[0m\e[1;77m%s\e[0m\n" $session_comments
printf "\e[1;93m[*] Follows: \e[0m\e[1;77m%s\e[0m\n" $session_follows
printf "\e[1;93m[*] Unfollows: \e[0m\e[1;77m%s\e[0m\n" $session_unfollows
printf "\n"
printf "\e[1;92m[*] Statistics total:\e[0m\n"

printf "\e[1;93m[*] Likes: \e[0m\e[1;77m%s\e[0m\n" $total_likes
printf "\e[1;93m[*] Comments: \e[0m\e[1;77m%s\e[0m\n" $total_comments
printf "\e[1;93m[*] Follows: \e[0m\e[1;77m%s\e[0m\n" $total_follows
printf "\e[1;93m[*] Unfollows: \e[0m\e[1;77m%s\e[0m\n" $total_unfollows
res2=$(date +%s)
secs=$(($res1-$res2))

printf '\e[1;93m[*] Work time:\e[0m\e[1;77m %dd:%dh:%dm:%ds\e[0m\n' $(($secs/86400)) $(($secs%86400/3600)) $(($secs%3600/60)) \
  $(($secs%60))

exit 1

}


login_user() {

if [[ "$default_username" == "" ]]; then
read -p $'\e[1;92m[*] Username: \e[0m' username
else
username="${username:-${default_username}}"
fi

if [[ "$default_password" == "" ]]; then
read -s -p $'\e[1;92m[*] Password: \e[0m' password
else
password="${password:-${default_password}}"
fi

printf "\e[\n1;77m[*] Trying to login as\e[0m\e[1;77m %s\e[0m\n" $username
check_login=$(curl -c cookies.txt 'https://www.instagram.com/accounts/login/ajax/' -H 'Cookie: csrftoken='$csrftoken'' -H 'X-Instagram-AJAX: 1' -H 'Referer: https://www.instagram.com/' -H 'X-CSRFToken:'$csrftoken'' -H 'X-Requested-With: XMLHttpRequest' --data 'username='$username'&password='$password'&intent' -L --compressed -s | grep -o '"authenticated": true')

if [[ "$check_login" == *'"authenticated": true'* ]]; then
printf "\e[1;92m[*] Login Successful!\e[0m\n"
else
printf "\e[1;93m[!] Check your login data or IP! Dont use Tor, VPN, Proxy. It's requires your usual IP.\n\e[0m"
exit 1
fi

}

createlist() {
touch liked.txt commented.txt followed.txt
rm -rf hashtags_id.txt owner_id.txt
IFS=$'\n'
for hashtag in $(cat hashtags.txt);do

printf "\e[1;77m[*] Creating media list for hashtag %s\e[0m\n" $hashtag
{( trap '' SIGINT && curl -s -L https://www.instagram.com/explore/tags/$hashtag/?__a=1 | grep  -o '"node":{"comments_disabled":false,"id":"..................[0-9]'  | cut -d ":" -f4 | tr -d '\"' | head -n 10 >> hashtags_id.txt )} & wait $!;
printf "\e[1;77m[*] Creating follower list for hashtag %s\e[0m\n" $hashtag
{( trap '' SIGINT && curl -L -s https://www.instagram.com/explore/tags/hacking/?__a=1 | grep  -o '"owner":{"id":".........[0-9]"'  | cut -d ":" -f3 | tr -d '\"' | head -n 10 >> owner_id.txt )} & wait $!;

done

}

bot() {

likes=0
comments=0
follows=0
while [ $counter1 -lt $turn ]; do

for media_id in $(sed -n ''$startline_bot','$endline_bot'p' hashtags_id.txt); do 
let count_media++

my_media=$(curl -s https://www.instagram.com/$username/ -L | grep  -o '"GraphImage","id":"..................[0-9]"' | cut -d ":" -f2 | tr -d '\"' | grep -o "$media_id")
if [[ "$my_media" == "" ]]; then
check_media=$(grep -o "$media_id" liked.txt)

if [[ "$check_media" == "" ]]; then
printf "\e[1;77m[*] Trying to like media id %s\e[0m\n" $media_id

#like

{( trap '' SIGINT && like=$(curl -b cookies.txt -H 'Cookie: csrftoken=$csrftoken' -H 'X-Instagram-AJAX: 1' -H 'Referer: https://www.instagram.com/' -H 'X-CSRFToken:$csrftoken' -H 'X-Requested-With: XMLHttpRequest' "https://www.instagram.com/web/likes/$media_id/like" -s -L --request POST | grep -o '"status": "ok"'); if [[ "$like" == *'"status": "ok"'* ]]; then printf "\e[1;92m[*] Media liked\e[0m\n"; printf "%s\n" $media_id >> liked.txt; let likes++ ; echo $likes >> likes ; sleep 60; else printf "\e[1;93m[!] Media not liked\e[0m\n"; sleep 300; fi  )} & wait $!;
 
fi # check_media
fi # my media

#comment

if [[ "$my_media" == "" ]]; then
check_comment=$(grep -o "$media_id" commented.txt)

if [[ "$check_comment" == "" ]]; then
printf "\e[1;77m[*] Trying to comment media id %s\e[0m\n" $media_id
{( trap '' SIGINT && comment=$(curl --data 'comment_text='$commt'' -b cookies.txt -H 'Cookie: csrftoken='$csrftoken'' -H 'Accept: */*' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate, br' -H 'Connection: keep-alive' -H 'Content-Lenght: 0' -H 'X-Instagram-AJAX: 1' -H 'Host: www.instagram.com' -H 'Referer: https://www.instagram.com/' -H 'X-CSRFToken:'$csrftoken'' -H 'X-Requested-With: XMLHttpRequest' -H 'Origin: https://www.instagram.com' -H 'User-Agent: "Instagram 10.26.0 Android (18/4.3; 320dpi; 720x1280; Xiaomi; HM 1SW; armani; qcom; en_US)"'  -H 'Content-Type: application/x-www-form-urlencoded' --user-agent 'User-Agent: "Instagram 10.26.0 Android (18/4.3; 320dpi; 720x1280; Xiaomi; HM 1SW; armani; qcom; en_US)"' -s -L  "https://www.instagram.com/web/comments/$media_id/add/" -w "\n%{http_code}\n" | grep -a "200"); if [[ "$comment" == "200" ]]; then printf "\e[1;92m[*] Media commented\e[0m\n"; let comments++ ; printf "%s\n" $media_id >> commented.txt;  echo $comments >> comments ; sleep 60 ; else printf "\e[1;93m[!] Media not commented\e[0m\n"; sleep 300; fi; )} & wait $!;

fi
fi

let counter1++
let startline_bot++
let endline_bot++
done
done
}

function owner_follow()  {
 
while [ $counter2 -lt $turn ]; do
let count_owner++

for owner_id in  $(sed -n ''$startline_follow','$endline_follow'p' owner_id.txt); do

my_id=$(curl -s "https://www.instagram.com/$username/" -L | grep -o 'profilePage_.*"' | cut -d "," -f1 | cut -d "_" -f2 | tr -d '\"')
check_id=$(grep -o "$my_id" owner_id.txt )

if [[ "$check_id" == "" ]]; then
check_follow=$(grep -o "$owner_id" followed.txt)

if [[ "$check_follow" == "" ]]; then

count_followers=$(curl -s -L "https://i.instagram.com/api/v1/users/$owner_id/info/" | grep -o 'follower_count":.*,' | cut -d "," -f1 | cut -d ":" -f2 | tr -d " ")

if [[ "$count_followers" -gt "1500" ]]; then
printf "\e[1;93m[!] Selebgram or fake account, not following %s\e[0m\n" $owner_id
sleep 10
let counter2++
else

#follow

printf "\e[1;77m[*] Trying to follow user id %s\e[0m\n" $owner_id

{( trap '' SIGINT && follow=$(curl -b cookies.txt -H 'Cookie: csrftoken='$csrftoken'' -H 'X-Instagram-AJAX: 1' -H 'Referer: https://www.instagram.com/' -H 'X-CSRFToken:'$csrftoken'' -H 'X-Requested-With: XMLHttpRequest' "https://www.instagram.com/web/friendships/$owner_id/follow/" -s -L --request POST | grep -o '"status": "ok"'); if [[ "$follow" == *'"status": "ok"'* ]]; then printf "\e[1;92m[*] User followed\e[0m\n"; printf "%s\n" $owner_id >> followed.txt; let follows++ ; echo $follows >> follows ; sleep 60 ; else printf "\e[1;93m[!] User not followed\e[0m\n" ; sleep 300 ; fi   )} & wait $!;


fi

fi #check_id
fi #check follow
let counter2++
let startline_follow++
let endline_follow++
done
done

}


unfollow() {
touch unfollows
unfollows=0
total_unfollow=$(wc -l followed.txt | cut -d " " -f1)
if [[ $total_unfollow -gt 0 ]]; then

for ownerid in $(cat followed.txt);do

printf "\e[1;77m[*] Trying to unfollow user id %s\e[0m\n" $ownerid

{( trap '' SIGINT && unfollow=$(curl -b cookies.txt -H 'Cookie: csrftoken='$csrftoken'' -H 'X-Instagram-AJAX: 1' -H 'Referer: https://www.instagram.com/' -H 'X-CSRFToken:'$csrftoken'' -H 'X-Requested-With: XMLHttpRequest' "https://www.instagram.com/web/friendships/$ownerid/unfollow/" -s -L --request POST | grep -o '"status": "ok"'); if [[ "$unfollow" == *'"status": "ok"'* ]]; then printf "\e[1;92m[*] User unfollowed\e[0m\n" ; awk '!/'$ownerid'/' followed.txt > temp && mv temp followed.txt ; let unfollows++ ; echo $unfollows >> unfollows ; sleep 30 ; else printf "\e[1;93m[!] User not unfollowed\e[0m\n" ; sleep 300 ; fi )} & wait $!;

done
fi # total_follow
remain=$(wc -l followed.txt | cut -d " " -f1)
session_unfollows=$(wc -l unfollows | cut -d " " -f1)
printf "\e[1;92m[*] Total unfollows:\e[0m\e[1;77m %s\e[0m\n" $session_unfollows 
if [[ $total_follow -gt 0 ]]; then
printf "\e[1;92m[*] Remaining:\e[0m\e[1;77m %s\e[0m\n" $remain
fi 

}

res1=$(date +%s)
start_date=$(date +%H:%M:%S)

function control() {

count_media=0
count_owner=0
total_media=$(wc -l unfollowid_id.txt | cut -d " " -f1)
total_owner=$(wc -l owner_id.txt | cut -d " " -f1)

while [ $count_media -lt $total_media ] && [ "$count_owner" -lt "$total_owner" ]; do
bot
owner_follow
let turn+=1
done
unfollow
createlist
let count_media=0
let count_owner=0
let startline_bot=1
let endline_bot=1
let startline_follow=1
let endline_follow=1
control

}
banner
dependencies
check_unfollow
login_user
printf "\e[1;93m[*] Bot started at:\e[0m\e[1;77m %s\e[0m\n" $start_date
createlist
control
