<?php

error_reporting(0);
include("config.php");
@system("clear");

$target = $argv[1];
$list = $argv[2];
$buka = fopen("$list","r");
$ukuran = filesize("$list");
$baca = fread($buka,$ukuran);
$lists = explode("\r\n",$baca);

print "\n$okegreen //$white Dircrunch \n\n";

if ($argv[3] == "-s"){
	subdoin($target);
	$sublist = "subdomain/$target.txt";
	$buka = fopen("$sublist","r");
	$ukuran = filesize("$sublist");
	$baca = fread($buka,$ukuran);
	$sublists = explode("\n",$baca);
	foreach ($sublists as $sub){
		foreach ($lists as $dir){
			request($sub, $dir);
		}
	}
} else {
	foreach ($lists as $dir){
		request($target, $dir);
	}
}

function subdoin($target){
	include 'config.php';
	print "$yellow //$white Searching for Subdomains\n";
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_URL,'https://sonar.omnisint.io/subdomains/'.$target);
    $result=curl_exec($ch);
	$json = json_decode($result, true);
	if (!file_exists("subdomain")){
		mkdir("subdomain");
	}
    $file = "subdomain/$target.txt";
    if( is_null($json) ){
        print "\n  Failed\n";
    } else {
        foreach ($json as $row){
            $handle = fopen($file, "a+");
            fwrite($handle, "$row\n");
        }
        $line = count(file($file));
        print "$yellow //$white Grabbed $line Subdomains from $target\n";
    }
}

function request($target, $dir){
	include("config.php");
	$log = "$target/$dir";
	$ch = curl_init("$log");
	curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_exec($ch);
	$httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
	curl_close($ch);
	if (!file_exists("result")){
		mkdir("result");
	}
	if($httpcode == 200){
		$handle = fopen("result/$target.txt", "a+");
		fwrite($handle, "$log\n");
		print "\n$okegreen [+]$white $log$okegreen OK";
	} elseif($httpcode == 403){
		print "\n$yellow [-]$white $log$yellow FORBIDDEN";
	} elseif($httpcode == 302){
		print "\n$yellow [-]$white $log$yellow REDIRECTED";
	} else {
		print "\n$red [x]$white $log$red ERROR";
	}
}

?>
