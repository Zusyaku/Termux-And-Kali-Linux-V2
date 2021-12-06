<?php

function banner(){
    @system("clear");
    include 'config.php';
    print "$white   ____        _         _       _       \n";
    print "  / ___| _   _| |__   __| | ___ (_)_ __  \n";
    print "  \___ \| | | | '_ \ / _` |/ _ \| | '_ \ \n";
    print "   ___) | |_| | |_) | (_| | (_) | | | | |\n";
    print "  |____/ \__,_|_.__/ \__,_|\___/|_|_| |_|\n";
    print "\n";
    print "$okegreen   Subdomain Grabber\n";
    print "$white   https://github.com/N1ght420/Subdoin\n";
    print "\n";
    menu();
}

function menu(){
    include 'config.php';
    print "$okegreen  [1]$white Single Target$okegreen     [2]$white Multi Target\n";
    print "\n";
    print "$cyan  [?]$white Menu : ";
    $menu = trim(fgets(STDIN));
    if ($menu == '1' OR $menu == '01'){
        single();
    } elseif ($menu == '2' OR $menu == '02'){
        multi();
    }
}

function single(){
    include 'config.php';
    print "$cyan  [?]$white Target : ";
    $target = trim(fgets(STDIN));
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_URL,'https://sonar.omnisint.io/subdomains/'.$target);
    $result=curl_exec($ch);
    $json = json_decode($result, true);
    $file = "$target.txt";
    if( is_null($json) ){
        print "\n  Failed\n";
    } else {
        foreach ($json as $row){
            $handle = fopen($file, "a+");
            fwrite($handle, "$row\n");
            print " -> $row\n";
        }
        $line = count(file($file));
        print "\n  Grabbed $line Subdomains from $target\n";
    }
}

function multi(){
    include 'config.php';
    print "$cyan  [?]$white List : ";
    $list = trim(fgets(STDIN));
    $buka = fopen("$list","r");
    $ukuran = filesize("$list");
    $baca = fread($buka,$ukuran);
    $lists = explode("\n",$baca);
    foreach($lists as $target){
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_URL,'https://sonar.omnisint.io/subdomains/'.$target);
        $result=curl_exec($ch);
        $json = json_decode($result, true);
        $file = "$target.txt";
        if( is_null($json) ){
            print "\n$red  [ERROR]$white $target";
        } else {
            foreach ($json as $row){
                $handle = fopen($file, "a+");
                fwrite($handle, "$row\n");
            }
            $line = count(file($file));
            print "\n$okegreen  [OK]$white $target$okegreen ->$yellow $line$white Subdomains";
        }
    }
    print "\n";
}

banner();

?>