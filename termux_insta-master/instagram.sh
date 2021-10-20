#!/bin/sh
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
MERAH='\033[0;31m'
N='\033[0;m'
HIJAU='\033[5;49;92m'
#Warna


echo $HIJAU"Selamat datang kak, Siapa nick kaka?" #tulisan keluar

read nick #membaca yang ditulis
echo "$MERAH=================================================$N"
echo "$MERAH== $HIJAU╦ ╦┌─┐┌─┐┬┌─┌─┐┬─┐  ┬┌┐┌┌┬┐┌─┐┌┐┌┌─┐┌─┐┬┌─┐ $MERAH=="
echo "$MERAH== $HIJAU╠═╣├─┤│  ├┴┐├┤ ├┬┘  ││││ │││ ││││├┤ └─┐│├─┤ $MERAH=="
echo "$MERAH== $HIJAU╩ ╩┴ ┴└─┘┴ ┴└─┘┴└─  ┴┘└┘─┴┘└─┘┘└┘└─┘└─┘┴┴ ┴ $MERAH=="
echo "$MERAH=================================================$N"
echo $HIJAU"Selamat datang" $MERAH$nick "$HIJAU""JONES! HAHAHAHA :v$N"
echo
echo $HIJAU"Silahkan masukan username Instagram target"




echo $HIJAU"contoh hack.id_"
read target # masukin user instagram

echo
echo $HUJAU"Apakah username $target sudah benar?"
echo y/n?
read confirm
echo
cek_target=`curl -s http://zpro.000webhostapp.com/api/cek_list_ig.php?cari=$target`
echo $MERAH$cek_target$N
