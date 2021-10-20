<?php

@system("mkdir result");
@system("clear");
$blue="\033[1;34";
$cyan="\033[1;36m";
$green="\033[1;34m";
$okegreen="\033[92m";
$lightgreen="\033[1;32m";
$white="\033[1;37m";
$purple="\033[1;35m";
$red="\033[1;31m";
$yellow="\033[1;33m";

print "$cyan
                                                
  _____ _       _ _    _____ _       _         
 |   __| |_ ___| | |  |   __|_|___ _| |___ ___ 
 |__   |   | -_| | |  |   __| |   | . | -_|  _|
 |_____|_|_|___|_|_|  |__|  |_|_|_|___|___|_|  
                                              

$white ==============================[$yellow Ver.3.0$white ]========

$cyan By$red   :$white N1ght.Hax0r
$cyan List$red :$white 1501 list

$white ==============[$yellow Code Your Freedom$white ]==============

$cyan 01$red :$white Find Shell
$cyan 02$red :$white More Tools
$cyan 03$red :$white Credits
";
echo "
$cyan Menu$red >$white ";
$menu = trim(fgets(STDIN));
if ($menu == '01' OR $menu == '1')
	{
		echo "$cyan Target$red >$white ";
		$target = trim(fgets(STDIN));
		echo "$cyan Use Default List (Y/N)?$red  >$white ";
		$pilihan = trim(fgets(STDIN));

		if ($pilihan == 'Y' OR $pilihan == 'y')
			{
				$list = "list.txt";
			}
		else
			{
				echo "$cyan List$red >$white ";
				$list = trim(fgets(STDIN));
			}
		if(!preg_match("/^http:\/\//",$target) AND !preg_match("/^https:\/\//",$target))
			{
				$targetnya = "http://$target";
			}
		else
			{
				$targetnya = $target;
			}
		echo "$yellow \n [!]==// Opening $list ...";
		$buka = fopen("$list","r");
		$ukuran = filesize("$list");
		$baca = fread($buka,$ukuran);
		$lists = explode("\r\n",$baca);

		echo "$cyan\n [!]==// Please Wait...
		";

		foreach($lists as $shell)
			{
				$log = "$targetnya/$shell";
				$ch = curl_init("$log");
				curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
				curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
				curl_exec($ch);
				$httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
				curl_close($ch);
				if($httpcode == 200){
					$handle = fopen("result/shell-$target.txt", "a+");
					fwrite($handle, "$log\n");
					print "\n$cyan  [".date('H:m:s')."]==//$white $log =>$cyan OK";
				}
				elseif($httpcode == 403){
					print "\n$red  [".date('H:m:s')."]==//$white $log =>$red FORBIDDEN";
				}
				else{
					print "\n$red  [".date('H:m:s')."]==//$white $log =>$red ERROR";
				}
			}
		echo "$lightgreen

[!]==// Result OK reported to $target.txt\n\n $white ";
	}

if ($menu == '02' OR $menu == '2')
	{
		print "$yellow                                                
  _____           _            _____             
 |     |___ _____|_|___ ___   |   __|___ ___ ___ 
 |   --| . |     | |   | . |  |__   | . | . |   |
 |_____|___|_|_|_|_|_|_|_  |  |_____|___|___|_|_|
                       |___|                     

$white";
	}
?>
