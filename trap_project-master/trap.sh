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
trap(){
      echo "       ) _     _ "
      sleep 0.03
      echo "      ( (^)-~-(^) "
      sleep 0.03
      echo "  _ ,-.\_( 6 6 )__,-.___ "
      sleep 0.03
      echo " | |'M'   \   /   'M'    "
      sleep 0.03
      echo " | |_ _ __ >o< _ _ _   "
      sleep 0.03
      echo " | __| '__/ _  | '_ \  "
      sleep 0.03
      echo " | |_| | | (_| | |_) | "
      sleep 0.03
      echo "  \__|_|  \__,_| .__/  "
      sleep 0.03
      echo "               | |     "
      sleep 0.03
      echo "               |_|    "
      sleep 0.03
      echo " ========================="
      sleep 2
      echo " ==    Trap Project     =="
      sleep 0.7
      echo " ========================="
}
get_url=$(curl -s http://zlucifer.com/api/hackbae.php?request=trap) #cek status
mulai(){
      echo "Gunakan Trap Project lagi?"
      echo "y/n?"
      read lagi
      if [ $lagi = "y" ];then
          clear
          trap
          start_trap_project
      else
          echo "Terimakasih sudah menggunakan Trap Project"
          exit
      fi
}
start_trap_project(){
      echo "[1] Buat File"
      echo "[2] Cek Hasil"
      echo "[3] Close Trap Project"
      echo "1/2/3?"
      read request
      if [ $request = "1" ]; then
            echo "Masukan nama file yang ingin kamu buat"
            read create
            echo "Memproses pembuatan file.."
            load
            clear
            trap
            curl -s $get_url/trap.php?create=$create #create
            mulai
      elif [ $request = "2" ]; then
            echo "Masukan nama file yang sudah kamu buat"
            echo "Untuk melakukan pengecekan hasil"
            read file
            echo
            echo "Melakukan Pengecekan.."
            load
            clear
            trap
            curl -s $get_url/cek.php?input=$file #cek
            mulai
      elif [ $request = "3" ];then
            echo "Terimakasih sudah menggunakan Trap Project"
            exit
      else
            echo "Kesalahan"
            mulai
      fi
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
echo "Loading .."
load
clear
trap
echo Selamat datang kak, Siapa nick kaka? #tulisan keluar
read nick #membaca yang ditulis
clear
trap
echo " Trap Project adalah tools untuk"
echo " mendapatkan IP atau lokasi Target"
echo
echo Selamat datang $nick ":)" Jones! :v
echo
start_trap_project
