#!/bin/bash
#///////////////////////////////////////////////////////////////////////////////
#            Jangan lupa subscribe channel HelloBae (Hackbae)                  #
#                 https://www.youtube.com/c/hellobae                           #
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
zlucifer="Jangan lupa subscribe channel HelloBae (Hackbae) https://www.youtube.com/c/hellobae"
#///////////////////////////////////////////////////////////////////////////////
#PERINGATAN : KESALAHAN ATAU KEJAHATAN ADALAH TANGGUNG JAWAB DARI PEMAKAI
#GUNAKAN TOOLS UNTUK KEBAIKAN JANGAN DISALAH GUNAKAN :)
troll(){
    echo "================================================"
    echo "=  _____        _ _ ___          _        _    ="
    echo "= |_   _| _ ___| | | _ \_ _ ___ (_)___ __| |_  ="
    echo "=   | || '_/ _ \ | |  _/ '_/ _ \| / -_) _|  _| ="
    echo "=   |_||_| \___/_|_|_| |_| \___// \___\__|\__| ="
    echo "=                             |__/             ="
    echo "================================================"
    echo "               Troll Project v2.0"
    echo "================================================"
}
server=$(curl -s https://pastebin.com/raw/DhQB56dd)
loading(){
  	load="Loading.... "
  	loading=${#load}
  	i=0
  	while((i<100)); do
    		n=$((i*loading / 100))
    		printf "\e[00;32m\r[%-${loading}s]\e[00m" "${load:0:n}"
    		((i += RANDOM%10))
    		sleep 0.1
  	done
    echo -e "\n"
}
mulai(){
    echo "Gunakan Troll Project Lagi?"
    echo "y/n?"
    echo
    read lagi
    if [ $lagi = "y" ] || [ $lagi = "Y" ] ; then
          spam
    else
          clear
          troll
          echo "Terimakasih sudah menggunakan Troll project"
          close
    fi
}
close(){
    exit
}
#spam
spam(){
    clear
    troll
    loading
    clear
    troll
    echo
    echo "[1] Spam SMS"
    echo "[2] Spam Telp"
    echo "[3] Spam WhatsApp"
    echo "[4] Close Troll Project"
    echo
    echo "1/2/3/4?"
    read pilih
    if [ $pilih = "1" ]; then
        #spam sms
        clear
        troll
        loading
        clear
        troll
        echo "Troll Spam SMS"
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
        if [ $confirm = "y" ]  || [ $confirm = "Y" ] ; then
                clear
                troll
                loading
                clear
                troll
                echo "Melakukan spam sms ke nomor "$target
                echo
                echo "Jangan close aplikasi sebelum spam selesai"
                echo "========================================"
                cek_target=`curl -A "$zlucifer" -s $server/api_sms.php?nomor=$target"&paket="$paket`
                echo -e $cek_target
                echo " Gunakan tools dengan bijak"
                echo
                echo " Love u always "
                echo " -zLucifer"
                echo "========================================"
        else
                echo "Kesalahan"
        fi
        mulai
    elif [ $pilih = "2" ]; then
        #spam call
        clear
        troll
        loading
        clear
        troll
        echo "Troll Spam Telp"
        echo
        echo "Silahkan masukan nomor telp target"
        echo contoh 0812345678
        read target # masukin no telp
        echo
        echo "Gunakan API Jagreward/Nutriclub?"
        echo "[1] Jagreward"
        echo "[2] Nutriclub"
        echo "1/2?"
        read api
        if [ $api = "1" ]; then
            api_spam="jagreward"
        else
            api_spam="nutriclub"
        fi
        echo
        echo "Apakah nomor" $target "dan spam menggunakan" $api_spam "sudah benar?"
        echo y/n?
        read confirm
        echo
        if [ $confirm = "y" ]  || [ $confirm = "Y" ] ; then
                  clear
                  troll
                  loading
                  clear
                  troll
                  echo Melakukan spam call ke nomor $target
                  echo
                  echo "Jangan close aplikasi sebelum spam selesai"
                  echo "========================================"
                  cek_target=`curl -A "$zlucifer" -s $server/api_call.php?nomor=$target"&method="$api_spam`
                  echo -e $cek_target
                  echo " Gunakan tools dengan bijak"
                  echo
                  echo " Love u always "
                  echo " -zLucifer"
                  echo "========================================"
        else
                  echo Kesalahan, silahkan coba lagi
        fi
        mulai
    elif [ $pilih = "3" ]; then
        #spam WhatsApp
        clear
        troll
        loading
        clear
        troll
        echo "Troll Spam WhatsApp"
        echo
        echo "Silahkan masukan nomor telp target"
        echo contoh 0812345678
        read target # masukin no telp
        echo
        echo "Berapa WhatsApp yang mau dikirim?"
        read paket
        echo
        echo Apakah nomor $target "dan WhatsApp dikirim "$paket" sudah benar?"
        echo y/n?
        read confirm
        echo
        if [ $confirm = "y" ]  || [ $confirm = "Y" ] ; then
                clear
                troll
                loading
                clear
                troll
                echo "Melakukan spam WhatsApp ke nomor "$target
                echo
                echo "Jangan close aplikasi sebelum spam selesai"
                echo "========================================"
                cek_target=`curl -A "$zlucifer" -s $server/api_wa.php?nomor=$target"&paket="$paket`
                echo -e $cek_target
                echo " Gunakan tools dengan bijak"
                echo
                echo " Love u always "
                echo " -zLucifer"
                echo "========================================"
        else
                echo "Kesalahan"
        fi
        mulai
    elif [ $pilih = "4" ]; then
        #tutup
        clear
        troll
        echo "Terimakasih sudah menggunakan Troll project"
        close
    else
        clear
        troll
        echo "Kesalahan"
        mulai
  fi
}
#mulai
clear
troll
echo Selamat datang kak, Siapa nick kaka? #tulisan keluar
read nick #membaca yang ditulis
clear
troll
echo Selamat datang $nick ":)"
echo
echo "Mulai Troll Project?"
echo "y/n?"
read confirm
if [ $confirm = "y" ] || [ $confirm = "Y" ] ; then
    spam
else
    echo "Terimakasih sudah menggunakan Troll project"
    close
fi
