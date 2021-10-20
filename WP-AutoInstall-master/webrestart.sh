#!/bin/bash
echo " Restarting Webserver "
service nginx restart
service php7.0-fpm restart
echo " Webserver Berhasil Di Restart"
