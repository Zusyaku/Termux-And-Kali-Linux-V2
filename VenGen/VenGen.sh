#!/bin/bash
#VenGen_1.0
#ByNiirmaalTwaatii

echo ""
figlet VenGen
echo ""
echo "~~~~~~~~~~~~~ VenGen 1.0 ~~~~~~~~~~~~~"
echo ""
echo "[]>=>=>=>=> By Niirmaal Twaatii ;"
echo ""

echo "-------------------------------------"
echo ""
echo "[1]=>Android Meterpreter Reverse tcp Payload (apk)"
echo "[2]=>Windows Meterpreter Reverse tcp Payload=>(exe)"
echo "[3]=>Help"
echo "[0]=>Exit"
echo ""
echo "-------------------------------------"
echo ""

read -p "[Input]=> " inp

echo ""

case "$inp" in
[1] ) ./android_reverse_tcp.sh;;
[2] ) ./windows_reverse_tcp.sh;;
[3] ) cat help.txt && sleep 5 && ./VenGen.sh;;
[0] ) exit;;
*   ) echo "Invalid Command " && ./VenGen.sh;;
esac