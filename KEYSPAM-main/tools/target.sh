#!/bin/bash
#
# target: (26/01/2021)
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
h='\033[1;90m'#
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
}
#
# Solicitando Número Telefónico
#
function PhoneNumber {
SETSMS
echo -e -n "${verde}
┌════════════════════════════┐
█ ${blanco}INGRESE EL NÚMERO OBJETIVO ${verde}█
└════════════════════════════┘
┃    ┌═════════┐  ┌═══════════════┐
└═>>>█ ${blanco}CONTOH ${verde}█=>█ ${azul}+6283143565479 ${verde}█
┃    └═════════┘  └═══════════════┘
┃    ┌════════════════════════════════════════┐
└═>>>█ ${rojo}MASUKKAN NOMOR TARGET ${verde}█
┃    └════════════════════════════════════════┘
┃
└═>>> "${blanco}
read -r PHONE
sleep 0.5

echo -e "${p}Sebelum Lanjut Gan Jangan Lupa Donasi....!
Jika Tidak Ada Yang Mau Donasi Script Ini Akan Expierd!!
${b}Jika Kalian Mau Donasi DiBawah Ini Gan...
${c}Dana  : ${p}083143565470
${c}Ovo   : ${p}083143565470
${c}Gopay : ${p}083143565470

${p}SILAHKAN TEKAN ENTER UNTUK LANJUT ${m}!!!!"${blanco}
read
}
#
# Llamando a las Herramientas Quack e Impulse
#
function SendSMS {
cd ${RUTA}/quack
python3 quack --tool SMS --target ${PHONE} --threads 60 --timeout 90
python3 quack --tool EMAIL --target ${PHONE} --threads 60 --timeout 90
cd ${RUTA}/Impulse
python3 impulse.py --method SMS --time 90 --threads 60 --target ${PHONE}
python3 impulse.py --method EMAIL --time 90 --threads 60 --target ${PHONE}
cd ${RUTA}
}
function Backup {
SETSMS
echo -e -n "${verde}
┌════════════════════════════════════┐
█ ${blanco}SIMPAN NOMOR DI DAFTAR HITAM?${verde}█
└════════════════════════════════════┘
┃
└═>>> ┃${azul} ${PHONE} ${verde}┃
┃
┃    ┌═══════════════════┐
└═>>>█ [${blanco}01${verde}] ┃ ${blanco}SI GUARDAR ${verde}█
┃    └═══════════════════┘
┃    ┌═══════════════════┐
└═>>>█ [${blanco}02${verde}] ┃ ${blanco}NO GUARDAR ${verde}█
┃    └═══════════════════┘
┃
└═>>> "${blanco}
read -r SCRIPT
sleep 0.5

if [[ ${SCRIPT} == 1 || ${SCRIPT} == 01 ]]; then
echo -e -n "${verde}
┌══════════════════════════════════┐
█ ${blanco}SILAHKAN TULIS DIBAWAH INI${verde}█
└══════════════════════════════════┘
┃    ┌═════════┐  ┌═════════┐
└═>>>█ ${blanco}EJEMPLO ${verde}█=>█ ${azul}Darkmux ${verde}█
┃    └═════════┘  └═════════┘
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
cd ${RUTA}" >> ${RUTA}/numbers/${NAME}.sh
echo -e "${verde}
┌══════════════════════════════┐
█ ${blanco}NOMOR YANG DISIMPAN DALAM SKRIP ${verde}█
└══════════════════════════════┘
┃
└═>>>${blanco} ${RUTA}/numbers/${NAME}.sh"${blanco}
elif [[ ${SCRIPT} == 2 || ${SCRIPT} == 02 ]]; then
exit
else
Error
Backup
fi
}
#
# Regresando al Menu Principal
#
function Restart {
echo -e "${verde}
┌════════════════════════════┐
█ ${blanco}TEKAN MASUK UNTUK MELANJUTKAN${verde}█
└════════════════════════════┘"${blanco}
read
source ${RUTA}/SETSMS.sh
}
#
# Declarando Funciones
#
PhoneNumber
SendSMS
Backup
Restart
