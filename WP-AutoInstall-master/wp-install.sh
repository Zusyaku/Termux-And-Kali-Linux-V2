#!/bin/bash
#### Script Auto Install Wordpress
#### IqbalFAF
##### Warna

cyan='\e[0;36m'
green='\e[0;34m'
okegreen='\033[92m'
lightgreen='\e[1;32m'
white='\e[1;37m'
red='\e[1;31m'
yellow='\e[0;33m'
BlueF='\e[1;34m' #Biru
RESET="\033[00m" #normal
orange='\e[38;5;166m'



#### IPKU
IPKU=$(wget -qO- ipv4.icanhazip.com);

#### Setting Repo
echo 'deb http://packages.dotdeb.org jessie all' >> /etc/apt/sources.list
echo 'deb-src http://packages.dotdeb.org jessie all' >> /etc/apt/sources.list
wget https://www.dotdeb.org/dotdeb.gpg
apt-key add dotdeb.gpg
rm dotdeb.gpg

apt-get update -y 
apt-get install figlet
apt-get install unzip -y

#### Figlet
wp=$(figlet wordpress)

clear
echo -e $okegreen "$wp" 

echo -e $red "        Auto Install Wordpress Debian 8 "
echo -e $yellow "===================== IqbalFAF ===================="
echo -e $BlueF""
echo "Silahkan Isi Data Data Di Bawah "
echo "    WAJIB  "
echo -e $RESET" Rubah kata IqbalGanteng Nya Sesuai Keinginan Kamu"
echo "   Kalau Males Tekan Enter Aja Langsung "
echo -e $BlueF"Password Buat Database Nya:"
read -p "Password baru: " -e -i IqbalGanteng PwdDatabase
echo ""
echo -e $RESET"Rubah Kata Wordpress Nya Sesuai Keinginan Kamu"
echo "   Kalau Males Tekan Enter Aja Langsung "
echo -e $BlueF"Nama Untuk Database Nya"
echo "Jangan Gunakan Karakter Selain _"
read -p "Nama Database: " -e -i wordpress NamaDatabase
echo ""
echo -e $okegreen"Oke, Sekarang Waktunya Instalasi"
read -n1 -r -p "Tekan sembarang tombol untuk melanjutkan..."

#apt-get update
apt-get update -y
apt-get install build-essential -y
apt-get install -y expect
echo -e $red""
read -p "Di Sini Tekan Enter Aja Langsung Jangan Di Isi Biar Nggak Error"
echo -e $okegreen""
apt-get install -y mysql-server

#mysql_secure_installation
so1=$(expect -c "
spawn mysql_secure_installation; sleep 3
expect \"\";  sleep 3; send \"\r\"
expect \"\";  sleep 3; send \"Y\r\"
expect \"\";  sleep 3; send \"$PwdDatabase\r\"
expect \"\";  sleep 3; send \"$PwdDatabase\r\"
expect \"\";  sleep 3; send \"Y\r\"
expect \"\";  sleep 3; send \"Y\r\"
expect \"\";  sleep 3; send \"Y\r\"
expect \"\";  sleep 3; send \"Y\r\"
expect eof; ")
echo "$so1"
#\r
#Y
#pass
#pass
#Y
#Y
#Y
#Y

chown -R mysql:mysql /var/lib/mysql/
chmod -R 755 /var/lib/mysql/

apt-get install -y php7.0 php7.0-fpm php7.0-cli php7.0-mysql php7.0-mcrypt
apt-get install -y php7.0-curl php7.0-gd php7.0-intl php7.0-pear php7.0-imagick php7.0-imap 
apt-get install -y php7.0-memcache  php7.0-pspell php7.0-recode php7.0-sqlite3 php7.0-tidy php7.0-xmlrpc php7.0-xsl php7.0-mbstring php7.0-gettext
apt-get install -y php7.0-apcu
apt-get install -y nginx 
rm /etc/nginx/sites-enabled/default
rm /etc/nginx/sites-available/default
mv /etc/nginx/nginx.conf /etc/nginx/nginx.conf.old
curl https://raw.githubusercontent.com/iqbalfaf/WP-AutoInstall/master/nginx.conf > /etc/nginx/nginx.conf
curl https://raw.githubusercontent.com/iqbalfaf/WP-AutoInstall/master/wordpress.conf > /etc/nginx/conf.d/wordpress.conf
sed -i 's/cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g' /etc/php/7.0/fpm/php.ini
sed -i 's/listen = \/var\/run\/php7.0-fpm.sock/listen = 127.0.0.1:9000/g' /etc/php/7.0/fpm/pool.d/www.conf

useradd -m vps
mkdir -p /home/vps/public_html
chown -R www-data:www-data /home/vps/public_html
chmod -R g+rw /home/vps/public_html
service php7.0-fpm restart
service nginx restart

#### Download Script Wordpress
cd /home/vps/public_html/
wget https://wordpress.org/latest.zip
unzip /home/vps/public_html/latest.zip
mv /home/vps/wordpress/* /home/vps/public_html/
rm -rf /home/vps/public_html/wordpress

#mysql -u root -p
so2=$(expect -c"
spawn mysql -u root -p; sleep 3
expect \"\";  sleep 3; send \"$PwdDatabase\r\"
expect \"\";  sleep 3; send \"CREATE DATABASE IF NOT EXISTS $NamaDatabase;EXIT;\r\"
expect eof; ")
echo "$so2"
#pass
#CREATE DATABASE IF NOT EXISTS OCS_PANEL;EXIT;

clear
echo "Sekarang Buka Browser Akses Server Nya $IPKU Dan Ini Data Buat Database Nya"
echo "Database:"
echo "- Database Host: localhost"
echo "- Database Name: $NamaDatabase"
echo "- Database User: root"
echo "- Database Pass: $PwdDatabase"

sleep 3
echo ""
read -p "Kalau Sudah, silahkan Tekan tombol [Enter] untuk melanjutkan..."
echo ""
cd /root
wget -O webrestart https://raw.githubusercontent.com/iqbalfaf/WP-AutoInstall/master/webrestart.sh
mv webrestart /usr/bin/
chmod +x /usr/bin/webrestart

apt-get -y --force-yes -f install libxml-parser-perl


cd
rm -f /root/.bash_history && history -c
echo "unset HISTFILE" >> /etc/profile
read -p " Instalasi Wordpress Selesai"
echo ""
# info
clear
echo "=======================================================" 
echo "Wordpress Auto Install IqbalFAF" 
echo ""
echo "Untuk Restart Web Server Ketik webrestart" 
echo "Semoga Happy :)"
echo "=======================================================" 
cd ~/

