<?php
error_reporting(0);
function banner(){
	@system("clear");
	echo "
                      (               
      (      )        )\ )       )    
    __)(  ( /(  (    (()/( (    (     
   / (()\ )(_)) )\ )  ((_)))\   )\  ' 
  / / ((_|(_)_ _(_/(  _| |((_)_((_))  
 /_/ | '_/ _` | ' \)) _` / _ \ '  \() 
(_)  |_| \__,_|_||_|\__,_\___/_|_|_|  
---------------------------Tegal1337
-----------Random Generator--------
[+] Usage :
$ --random / random (https://randomuser.me/)
$ --uiname / uiname (https://uinames.com/)
$ --lorsum / lorsum (https://loripsum.net/)
$ --touch / touch (For contact me)

";
}
function randomuser(){
	$ch = curl_init();
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_URL,'https://randomuser.me/api/');
    $result=curl_exec($ch);
    $json = json_decode($result, true);
    foreach ($json['results'] as $data) {
    	$jk = $data['gender'];
    	$npertama = $data['name']['first'];
    	$nkedua = $data['name']['last'];
    	$kota = $data['location']['city'];
    	$provinsi = $data['location']['state'];
    	$negara = $data['location']['country'];
    	$kodepos = $data['location']['postcode'];
    	$ttl = $data['dob']['date'];
    	$umur = $data['dob']['age'];
    	$nohp = $data['phone'];

    	echo "Nama : $npertama $nkedua \n";
    	echo "Jenis kelamin : $jk \n";
    	echo "Asal : $kota, $provinsi, $negara, $kodepos \n";
    	echo "\n";

    }
}

function uinames(){
	$ch = curl_init();
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_URL,'https://uinames.com/api/?ext');
    $result=curl_exec($ch);
    $data = json_decode($result, true);
    $name = $data['name'];
    $surname = $data['surname'];
    $gender = $data['gender'];
    $region = $data['region'];
    $age = $data['age'];
    $phone = $data['phone'];
    $birth = $data['birthday']['dmy'];
    $ccnum = $data['credit_card']['number'];
    $ccexp = $data['credit_card']['expiration'];
    $ccpin = $data['credit_card']['pin'];
    $cccvv = $data['credit_card']['security'];
    $photo = $data['photo'];
    print "Name : $name $surname\n";
    print "Gender : $gender\n";
    print "Region : $region\n";
    print "TTL : $birth\n";
    print "Umur : $age\n";
    print "Nope : $phone\n";
    print "CC : $ccnum $ccexp $cccvv\n";
    print "\n";
}
function lorsum(){
    echo "
    List of command :

(integer) - The number of paragraphs to generate.
short, medium, long, verylong - The average length of a paragraph.
decorate - Add bold, italic and marked text.
link - Add links.
ul - Add unordered lists.
ol - Add numbered lists.
dl - Add description lists.
bq - Add blockquotes.
code - Add code samples.
headers - Add headers.
allcaps - Use ALL CAPS.
prude - Prude version.
plaintext - Return plain text, no HTML.
	
use '/'' to be specific
example : 20/allcaps
    \n";
    $tulis = readline("~Find : ");
	$url = 'https://loripsum.net/api/'.$tulis;
	$result = file_get_contents($url);
	echo $result;
}

function contact(){
	echo "Hello .... My name is dalpan \n";
	echo "Email : contact@dalpan.co\n";
	echo "IG : https://instagram.com/dalpan_ \n";
	echo "Thankss... :D \n";
}
banner();
while (true) {
	echo "[+]-> ";
	$command = trim(fgets(STDIN));
	if(strstr("--random", $command) or strtr("random", $command)){
		randomuser();
	}elseif (strstr("--uiname", $command) or strtr("uiname", $command)) {
		uinames();
	}elseif (strstr("--help", $command) or strtr("help", $command)) {
		banner();
	}elseif (strstr("--touch", $command) or strtr("touch", $command)) {
		contact();
    }elseif (strstr("--lorsum", $command) or strtr("lorsum", $command)){
        lorsum();
    }
    else {
		echo "Nulis opo lurr ?";
	}
}

?>
