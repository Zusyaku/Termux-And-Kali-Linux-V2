#!/bin/sh
clear
cowsay Leakix Searcher | lolcat
echo "LoliC0d3 - Tegal1337" | lolcat
read -p "Site:" site 
read -p "Page:" loli
page=0
while [ $page -le $loli ]
do
  curl -sqH'Accept: application/json' 'https://leakix.net/search?page='$page'&q=+'$site'=&scope=leak' | jq | grep ip | sed -nr '$!N;/^(.*)\n\1$/!P;D' | cut -d ':' -f 2 | cut -d '"' -f 2 | cut -d '{' -f 2  | sed 's/[^0-9.]*//g' | awk '{if(NF>0) {print $0}}' | tee -a Result.txt
   ((page++))
done
