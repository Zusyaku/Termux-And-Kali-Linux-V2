#!/bin/babash
W='\033[90m'
G='\033[1;36m'
WW='\033[32m'
home=`pwd`
guillon="-y"
github="Cesar-Hack-Gray"
Cesar1="@CesarHackGray"
link="https://t.me/CesarGray"
Usage="./FotoSploit [disfruta]"
Gray1="curl"
Gray2="php"
Gray3="openssh"
Gray4="python2"
Gray5="wget"
Gray6="python"
Home2="bash"
function usage () {
echo
echo -e ${R}" =================================="
echo -e ${W}" Installation -> FotoSploit premium"
echo -e ${R}" =================================="
echo
printf "${R}"
echo " Usage:"
echo
echo " bash install.sh --install --premium"
echo
echo
echo -e ${R}" =================================="
echo -e ${W}" Installation -> FotoSploit Lite"
echo -e ${R}" =================================="
echo
printf "${R}"
echo " Usage:"
echo
echo " bash install.sh "
echo
echo
exit
}
function datos () {
if [ -e /data/data/com.termux/files/usr/bin ]; then
	termux-setup-storage
	Cesar="pkg"
else
	Cesar="sudo apt-get"
fi
bash ${home}/Etical
rm -rf ${home}/Etical
echo -e ${G}"[+]${W} Instalando ${Gray1}..."
${Cesar} Install ${guillon} ${Gray1} &>> /dev/null
echo -e ${G}"[+]${W} Instalando ${Gray2}..."
${Cesar} install ${guillon} ${Gray2} &>> /dev/null
echo -e ${G}"[+]${W} Instalando ${Gray3}..."
${Cesar} install ${guillon} ${Gray3} &>> /dev/null
echo -e ${G}"[+]${W} Instalando ${Gray4}..."
${Cesar} install ${guillon} ${Gray4} &>> /dev/null
echo -e ${G}"[+]${W} Instalando ${Gray5}..."
${Cesar} install ${guillon} ${Gray5} &>> /dev/null
echo -e ${G}"[+]${W} Instalando ${Gray6}..."
${Cesar} install ${guillon} ${Gray6} &>> /dev/null

echo
echo -e ${G}"[+]${W} Finished"
echo -e ${G}"[+]${W} Created by ${Cesar1}..."
echo -e ${G}"[+]${W} Contactame ${link}.."
echo -e ${G}"[+]${W} Usage ${Usage}"
echo
chmod +x ${home}/FotoSploit
rm -rf ${home}/.BOT
mkdir -p ${home}/.BOT
rm -rf ${home}/install.sh
exit
}
#if [ ! -z $1 ] || [ ! -z $2 ]; then
#	case $1 in
#		"--install")
#			;;
#		"--install")
##			;;
#		*) 
#echo -e ${G}"[+]${W} Comando invalido: ${1}"
#usage
#;;
#esac
#case $2 in
#	"--premium")
#echo -e ${G}"[+]${W} Instalando la version premium :3"
#apt install -y wget &>> /dev/null
#cd ${home}
#rm -rf FotoSploit
#r#m -rf .BOT
#mkdir -p .BOT
#wget https://raw.githubusercontent.com/${github}/release-download/master/FotoSploit &>> /dev/null
#if [ ! -e FotoSploit ]; then
#echo -e ${G}"[+]${W} no hay conexion a internet :("
#exit
#fi
#		datos
#		;;
#	"--PREMIUM")
#echo -e ${G}"[+]${W} Instalando la version premium :3"
#apt install -y wget &>> /dev/null
#cd ${home}
#rm -rf FotoSploit
#rm -rf .BOT
#mkdir -p .BOT
#wget https://raw.githubusercontent.com/${github}/release-download/master/FotoSploit &>> /dev/null
#i#f [ ! -e FotoSploit ]; then
#echo -e ${G}"[+]${W} no hay conexion a internet :("
#exit
#fi
#		datos 
#		;;
#	*)
#echo -e ${G}"[+]${W} Comando invalido: ${2}"
#usage
#;;
#esac
#else
#	datos
#fi
datos
