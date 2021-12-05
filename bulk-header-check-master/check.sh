#!/bin/bash
if [ -z "$1" ]; then
    echo -e "Usage: $0 list.txt\n";
    exit
fi

echo -e "Nakano Nino best waifu!\n";  
for hostlists in $(cat $1);
do
    echo $hostlists | xargs -P 100 curl -s -o /dev/null -I -w "[%{http_code}] - $hostlists\n"
done
