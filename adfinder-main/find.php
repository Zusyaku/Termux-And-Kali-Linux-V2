<?php

error_reporting(0);
include 'config.php';

function banner(){
	@system("clear");
	include 'config.php';
	print "$cyan      ___       ____________          __         \n";
	print "$cyan     /   | ____/ / ____/  _/___  ____/ /__  _____\n";
	print "$cyan    / /| |/ __  / /_   / // __ \/ __  / _ \/ ___/\n";
	print "$cyan   / ___ / /_/ / __/ _/ // / / / /_/ /  __/ /    \n";
	print "$cyan  /_/  |_\__,_/_/   /___/_/ /_/\__,_/\___/_/     \n";
	print "\n";
	print "$white            Admin Login Panel Finder\n";
}

banner();
print "\n target : ";
$target = trim(fgets(STDIN));
print " panel type (asp,aspx,brf,cfm,cgi,js,php) : ";
$type = trim(fgets(STDIN));

if($type == 'asp'){
    $list = 'list/asp.txt';
} elseif ($type == 'aspx'){
    $list = 'list/aspx.txt';
} elseif ($type == 'brf'){
    $list = 'list/brf.txt';
} elseif ($type == 'cfm'){
    $list = 'list/cfm.txt';
} elseif ($type == 'cgi'){
    $list = 'list/cgi.txt';
} elseif ($type == 'js'){
    $list = 'list/js.txt';
} elseif ($type == 'php'){
    $list = 'list/php.txt';
} else {
    print " list : ";
    $list = trim(fgets(STDIN));
}

$buka = fopen("$list","r");
$ukuran = filesize("$list");
$baca = fread($buka,$ukuran);
$lists = explode("\n",$baca);

banner();
foreach ($lists as $dir){
	request($target, $dir);
}

function request($target, $dir){
	include 'config.php';
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
		print "\n$yellow [?]$white $log$yellow REDIRECTED";
	} else {
		print "\n$red [x]$white $log$red ERROR";
	}
}

?>