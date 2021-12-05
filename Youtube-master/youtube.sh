#!/bin/bash 
#title           :youtube.sh
#description     :Given a youtube video id, print video url of each format for download.
#author          :AnonyminHack5 
#date            :12122020
#version         :0.1
#usage           :bash youtube.sh video id
#notes           :Install curl to use this script.
#bash_version    :3.2.51(1)-release
video_id=$1
if [[ -z $1 ]]; then
   echo "You must enter the video id"
   echo ""
   echo "Usage: ./youtube.sh eb3suf4REyI"
   exit 1
fi
html=`curl --silent -A "Mozilla" -XGET "http://www.youtube.com/watch?v=$1" `
echo $html > last
title=`echo $html | awk -F 'title>' '{print $2}' | awk -F ' - ' '{print $1}'| sed 's/[^a-zA-Z0-9 ]//g' |sed 's/ /_/g'`

links=`echo $html | awk -F 'url_encoded_fmt_stream_map": "' '{print $2}' | awk -F '",' '{print $1}' | sed 's/sig=/signature=/g' | awk -F, '{ for (i=1; i<=NF; i++) print $i }'`

for link in $links; do

   format=`echo $link | awk -F "type=" '{print $2}' | awk -F "+" '{print $1}' | awk -F "%2F" '{print $2}' | sed -e 's/%3B.*//' -e 's/\\u0026.*//' | sed 's/\\\//g'`
   quality=`echo $link | awk -F "quality=" '{print $2}' | sed 's/\\u0026.*//' | sed 's/\\\//g'`
   temp_link=`echo $link | sed 's/: "//' | sed 's/%3A/:/g' | sed 's/%2F/\//g' | sed 's/%3F/?/g' | sed 's/itag=[^&]*//g' | sed 's/%3D/=/g' | sed 's/%252C/%2C/g' | sed 's/%26/\&/g' | sed 's/sig=/signature=/g' | sed -e 's/\\u0026/\&/g' -e 's/u0026/\&/g' -e 's/\\\//g' | sed 's/type=[^&]*//g' | sed 's/quality=[^&]*//g' | sed 's/fallback_host=[^&]*//g' | sed 's/\\\&//g'`

   empty_link=`echo $temp_link | sed 's/&//g' | sed 's/signature=[^&]*//g'`

   if [[ -z $empty_link ]]; then
      temp_link=`echo $link | sed 's/: "//' | sed 's/%3A/:/g' | sed 's/%2F/\//g' | sed 's/%3F/?/g' | sed 's/%3D/=/g' | sed 's/%252C/%2C/g' | sed 's/%26/\&/g' | sed 's/sig=/signature=/g' | sed -e 's/\\u0026/\&/g' -e 's/u0026/\&/g' -e 's/\\\//g' | sed 's/type=[^&]*//g' | sed 's/quality=[^&]*//g' | sed 's/fallback_host=[^&]*//g' | sed 's/\\\&//g'`
   fi
   temp_signature=`echo $temp_link | sed -n 's/.*signature=\(.*\).*/\1/p' | awk -F\& '{print $1}' | awk -F 'url' '{print $1}' | awk -F 'itag' '{print $1}'`

    if [[ -z $temp_signature ]]; then
      temp_signature=`echo $link | awk -F 'signature=' '{print $NF}'`
   fi
   signature="signature="$temp_signature

   url=`echo $temp_link | sed -n 's/.*url=\(.*\).*/\1/p' | sed 's/signature=[^&]*//g' | sed 's/\&\&/\&/g'`

   echo "## "$quality" ["$format"]"
   echo "$url&$signature&title="$title | sed 's/ //g' | sed 's/\&\&/\&/g'
   echo "---------------------------------------------"
done
