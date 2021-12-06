#!/bin/bash
#
# SETSMS: (26/01/2021)
#
# [Open Source] - [Código Abierto]
#
# Variables y Colores
#
####################################
#Ayo Mau Apa... Hahahahah
####################################
#123 Tutuo Botok Muka Lu Kaya Kntl
####################################

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
# Dependencias del Script
#
function Dependencies {
if [ "${OS}" == "Android" ]; then
	if [ -x ${PREFIX}/bin/python ]; then
		RUTA=$(pwd)
	else
		RUTA=$(pwd)
		pkg update && pkg upgrade -y
		pkg install python -y
		pip install --upgrade pip
	fi
	if [ -x ${PWD}/quack ]; then
		RUTA=$(pwd)
	else
		RUTA=$(pwd)
		unzip quack.zip
		rm quack.zip
		cd ${RUTA}/quack
		python3 -m pip install -r requirements.txt
		cd ${RUTA}
	fi
	if [ -x ${PWD}/Impulse ]; then
		RUTA=$(pwd)
	else
		RUTA=$(pwd)
		unzip Impulse.zip
		rm Impulse.zip
		cd ${RUTA}/Impulse
		python3 -m pip install -r requirements.txt
		cd ${RUTA}
	fi
else
	if [ -x /bin/python3 ]; then
		RUTA=$(pwd)
	else
		RUTA=$(pwd)
		apt-get update && apt-get upgrade -y
		apt-get install python3 -y
	fi
	if [ -x ${PWD}/quack ]; then
		RUTA=$(pwd)
	else
		RUTA=$(pwd)
		unzip quack.zip
		rm quack.zip
		cd ${RUTA}/quack
		python3 -m pip install -r requirements.txt
		cd ${RUTA}
	fi
	if [ -x ${PWD}/Impulse ]; then
		RUTA=$(pwd)
	else
		RUTA=$(pwd)
		unzip Impulse.zip
		rm Impulse.zip
		cd ${RUTA}/Impulse
		python3 -m pip install -r requirements.txt
		cd ${RUTA}
	fi
fi
}
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
# Menu Principal
#
function Choose {
SETSMS
echo -e -n "${k}
┌═══════════════════════┐
█${p}Silahkan Pilih Menunya ${k}█
└═══════════════════════┘
┃    ┌═══════════════════════════════════════════┐
└═>>>█${c}[${p}01${c}]${p}Spam Satu Nomor !! ${c}|${p} Semua Nomor Negara${k}█
┃    └═══════════════════════════════════════════┘
┃    ┌═══════════════════════════════════════════┐
└═>>>█${c}[${p}02${c}]${p}Save List Nomor !! ${c}|${p} Untuk Menu No 03 ${k} █
┃    └═══════════════════════════════════════════┘
┃    ┌═══════════════════════════════════════════┐
└═>>>█${c}[${p}03${c}]${p}Mulai Spam Yang TerSimpan !! ${c}|${p}Mr.Risky${k} █
┃    └═══════════════════════════════════════════┘
┃    ┌═══════════════════════════════════════════┐
└═>>>█${c}[${p}04${c}]${p}Check List Spam !! ${c}|${p} Untuk Menu No 03 ${k} █
┃    └═══════════════════════════════════════════┘
┃    ${i}┌══════════════┐
└═>>>${i}█ [${blanco}00${verde}] ┃ ${rojo}Exit ${verde}█
┃    └══════════════┘
┃
└═>>> "${blanco}
read -r OPTION
sleep 1.2

if [[ ${OPTION} == 0 || ${OPTION} == 00 ]]; then
exit
elif [[ ${OPTION} == 1 || ${OPTION} == 01 ]]; then
source ${RUTA}/tools/target.sh
elif [[ ${OPTION} == 2 || ${OPTION} == 02 ]]; then
source ${RUTA}/tools/save.sh
elif [[ ${OPTION} == 3 || ${OPTION} == 03 ]]; then
source ${RUTA}/tools/spam.sh
elif [[ ${OPTION} == 4 || ${OPTION} == 04 ]]; then
source ${RUTA}/tools/list.sh
else
Error
Choose
fi
}
#
# Declarando Funciones
#
Dependencies
Choose
