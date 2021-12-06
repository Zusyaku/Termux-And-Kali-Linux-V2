#!/bin/bash
#
# save: (26/01/2021)
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
}
#
# Banner SETSMS
#
function SETSMS {
	sleep 0.5
	clear
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
#
# Solicitando Número Telefónico
#
function PhoneNumber {
SETSMS
echo -e -n "${verde}
┌════════════════════════════┐
█ ${blanco}MASUKKAN NOMOR MAU DISAVE ${verde}█
└════════════════════════════┘
┃    ┌═════════┐  ┌═══════════════┐
└═>>>█ ${blanco}CONTOH ${verde}█=>█ ${azul}+6283143565470${verde}█
┃    └═════════┘  └═══════════════┘
┃    ┌════════════════════════════════════════┐
└═>>>█ ${rojo}INGAT UNTUK MASUKKAN NOMOR SEMUA BERSAMA${verde}█
┃    └════════════════════════════════════════┘
┃
└═>>> "${blanco}
read -r PHONE
sleep 0.5
}
function Backup {
echo -e -n "${verde}
┌══════════════════════════════════┐
█ ${p}Masukkan Nama File Untuk DiSave! ${verde}█
└══════════════════════════════════┘
┃    ┌═════════┐  ┌══════════┐
└═>>>█${p}RIPER-ASW${verde}█=>█${p}PenipuBGST${verde}█
┃    └═════════┘  └══════════┘
┃
└═>>> "${blanco}
read -r NAME
sleep 0.5
echo -e "PHONE='${PHONE}'" >> ${RUTA}/tools/list.sh
echo -e "NAME='${NAME}'" >> ${RUTA}/tools/list.sh
echo -e 'echo -e "${blanco}${NAME} ${verde}=>${azul} ${PHONE}"
sleep 1' >> ${RUTA}/tools/list.sh
echo -e "PHONE='${PHONE}'" >> ${RUTA}/tools/spam.sh
echo -e "NAME='${NAME}'" >> ${RUTA}/tools/spam.sh
echo -e 'echo -e "${verde}
┌══════════┐
█ ${blanco}OBJETIVO ${verde}█
└══════════┘
${blanco}
${NAME} ${verde}=>${azul} ${PHONE}"
sleep 1' >> ${RUTA}/tools/spam.sh
echo -e "source ${RUTA}/numbers/${NAME}.sh" >> ${RUTA}/tools/spam.sh
echo -e "#!/bin/bash
cd ${RUTA}/quack
python3 quack --tool SMS --target ${PHONE} --threads 60 --timeout 90
cd ${RUTA}/Impulse
python3 impulse.py --method SMS --time 90 --threads 60 --target ${PHONE}
python3 impulse.py --method CALL --time 90 --threads 60 --target ${PHONE}
cd ${RUTA}" >> ${RUTA}/numbers/${NAME}.sh
echo -e "${verde}
┌══════════════════════════════┐
█${p}  Membuat List Spam Ngab !!!  ${verde}█
└══════════════════════════════┘
┃
└═>>>${blanco} ${RUTA}/numbers/${NAME}.sh"${blanco}
}
#
# Regresando al Menu Principal
#
function Restart {
echo -e "${verde}
┌════════════════════════════┐
█ ${p}Tekan Enter Untuk Lanjut!! ${verde}█
└════════════════════════════┘"${blanco}
read
source ${RUTA}/SETSMS.sh
}
#
# Declarando Funciones
#
PhoneNumber
Backup
Restart
