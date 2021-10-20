#!/bin/bash
#update
sudo apt update

#apache
sudo apt install apache2
sudo chown -R pi:www-data /var/www/html/
sudo chmod -R 770 /var/www/html/


#php
sudo apt install php php-mbstring
sudo rm /var/www/html/index.html

#mysql
sudo apt install mysql-server php-mysql
sudo mysql --user=root

#DROP USER 'root'@'localhost';
#CREATE USER 'root'@'localhost' IDENTIFIED BY 'password';
#GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost'

#mysql --user=root --password=yourmysqlpassword

#phpmyadmin
sudo apt install phpmyadmin
sudo phpenmod mysqli
sudo /etc/init.d/apache2 restart
sudo ln -s /usr/share/phpmyadmin /var/www/html/phpmyadmin

#LCD
git clone https://github.com/goodtft/LCD-show.git
chmod -R 755 LCD-show
cd LCD-show/
#sudo ./LCD35-show
#cd LCD-show/
#sudo ./LCD-hdmi
