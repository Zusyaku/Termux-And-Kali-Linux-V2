#!/bin/bash

# TelephonyBruteCall for Termux
# By Niirmaal twaatii
#https://www.github.com/niirmaaltwaatii/telephonybrutecall
#niirmaaltwaatii

echo "
 _____ ____   ____
|_   _| __ ) / ___|
  | | |  _ \| |
  | | | |_) | |___         Created by N11rm44L 7w44711
  |_| |____/ \____|
  
  "

sleep 1.0
echo " TooL : TelephonyBruteCall "
echo " Version : 1.0 "
sleep 1.0
echo " By N11rm44L 7w44711 "
echo ""

read -p "Starting Number : " SN
read -p "Ending Number : " EN
read -p "Time Diff : " TD
echo " [√]=⟩ $SN - $EN "
sleep 2.0

while [ $SN -le "$EN" ] ;
do
  echo "Calling $SN ..."
  termux-telephony-call $SN
  SN=$(($SN+1))
  sleep $TD
done