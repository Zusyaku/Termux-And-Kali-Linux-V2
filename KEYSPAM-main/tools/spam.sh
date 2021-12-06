#!/bin/bash
#
# spam: (26/01/2021)
#
# [Open Source] - [Código Abierto]
#
# Variables y Colores
#
PWD=$(pwd)
OS=$(uname -o)
USER=$(id -u)
verde='\033[32m'
blanco='\033[37m'
rojo='\033[31m'
azul='\033[34m'
negro='\033[0;30m'
rosa='\033[38;5;207m'
amarillo='\033[33m'
morado='\033[35m'
cian='\033[1;36m'
magenta='\033[1;35m'
q="\033[00m"
h2="\033[40m"
b2="\033[44m"
c2="\033[46m"
i2="\033[42m"
u2="\033[45m"
m2="\033[41m"
p2="\033[47m"
k2="\033[43m"
b='\033[1;34m'
i='\033[1;32m'
c='\033[1;36m'
m='\033[1;31m'
u='\033[1;35m'
k='\033[1;33m'
p='\033[1;37m'
h='\033[1;90m'
#
# Mensaje de Opción Incorrecta
#
function Error {
echo -e "${k}
┌═════════════════════┐
|${m}Maaf Terjadi Erorr !!${k}|
└═════════════════════┘
"${blanco}
sleep 0.5
pip install -r re*
}
#
# Banner SETSMS
#
function SETSMS {
	sleep 1.5
	clear
pip install -r re*
echo -e "${c}
		        [${p}Welcome To KeySpam${c}]${c}
		 [${p}Author : Mr.Risky - SystemX ProX${c}]
${m}   ██╗░░██╗███████╗██╗░░░██╗░██████╗██████╗░░█████╗░███╗░░░███╗
   ██║░██╔╝██╔════╝╚██╗░██╔╝██╔════╝██╔══██╗██╔══██╗████╗░████║
   █████═╝░█████╗░░░╚████╔╝░╚█████╗░██████╔╝███████║██╔████╔██║
   ██╔═██╗░██╔══╝░░░░╚██╔╝░░░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║
   ██║░╚██╗███████╗░░░██║░░░██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║
   ╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝
   [${i}------------------------${p}INFORMATION${i}-----------------------${c}]
   [${p}Gunakan Dengan Bijak Saat Menggunakan Script Ini (KeySpam)${c}]
   [${p}Jika Terjadi Kesalahan Terhadap Script Hubungi Athour !!  ${c}]
   [${p}Whatsapp : 6283143565470				      ${c}]
   [${p}Dana     : 083143565470 				      ${c}]
   [${p}Ovo      : 083143565470 				      ${c}]
   [${p}Gopay    : 083143565470 				      ${c}]
   [${i}------------------------${p}INFORMATION${i}-----------------------${c}]

"${blanco}
}
#
# Declarando Funciones
#
source ${PWD}/tools/list.sh
PHONE='+6283143565470'
NAME='Darkmux'
echo -e "${verde}
┌══════════┐
█ ${blanco}OBJETIVO ${verde}█
└══════════┘
${blanco}
${NAME} ${verde}=>${azul} ${PHONE}"
sleep 1
source /data/data/com.termux/files/home/SETSMS/numbers/Darkmux.sh
PHONE='+6283143565470'
NAME='MR.RISKY'
echo -e "${verde}
┌══════════┐
█ ${blanco}OBJETIVO ${verde}█
└══════════┘
${blanco}
${NAME} ${verde}=>${azul} ${PHONE}"
sleep 1
source /data/data/com.termux/files/home/SETSMS/numbers/EJEMPLO.sh
