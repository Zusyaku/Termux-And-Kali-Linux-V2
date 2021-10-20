<?php
/*please dont recode*/
/*Coded By Zeerx7*/
/*Rao cyber team*/
//2019©indonesian hacker rulez

//dibikin open source bukan untuk di record ya bangsad...
//record?? izin dulu. wa:0895320325423(no spam/oke)
//record tanpa izin? ga akan berguna ilmu lo asw 
function cekdir(){
$dir = "/data/data/com.termux/files/home";
if( is_dir($dir) === false )
{
    echo "Not Termux Detect\n";
    sleep('1');
    echo "Sepertinya perangkat yang anda gunakan\nBukanlah ANDROID/TERMUX\n";
    sleep('1');
    echo "exit....\n\n";
    sleep('1');
    exit();
}else{
  internet();
  //echo $ambil."\n";
 // echo "perangkat : android/termux\n";
}}
function internet(){
$url="http://zeerx7.my.id/co/de/t-head.php";
//$url="localhost:4444/t.txt";
if(!$sock = @fsockopen('zeerx7.my.id', 80))
{
    //echo 'Not Connected';
}else{
//echo 'Connected';
 $ambil = file_get_contents($url);
 echo "\e[93m".$ambil."\e[36m\n"; }}

function cek($cmd){
$x=shell_exec(sprintf("which %s", escapeshellarg($cmd)));
return !empty($x);
}
function cekpack(){
echo "[+] Checking cowsay/toilet/lolcat Package ...\n";
sleep(1);
if(!cek('cowsay')){
   system("pkg install cowsay -y");
}else{
echo "[+] sudah terinstall ...\n";
sleep(0.6);
}
if(!cek('lolcat')){
   system("pkg install ruby -y");
   system("gem install lolcat");
}else{
echo "[+] sudah terinstall ...\n";
sleep(0.6);
}
if(!cek('figlet')){
   system("pkg install figlet -y");
}else{
echo "[+] sudah terinstall ...\n";
sleep(0.6);
}
if(!cek('toilet')){
   system("pkg install toilet -y");
}else{
echo "[+] sudah terinstall ...\n";
sleep(1);
}}

$banner1="
   @ @ @ @ @ @ @ @ @ @ @ @ @
  @   Welcome To my Tools   @
 @      Coded By Zeerx7    @
  @ @ @ @ @ @ @ @ @ @ @ @ @
";
$banner2="
   $ $ $ $ $ $ $ $ $ $ $ $
  $  Welcome To my Tools  $
 $     Coded by Zeerx7   $
  $ $ $ $ $ $ $ $ $ $ $ $
";
$banner3="
   -,-,-,-,-,-,-,-,-,-,-,-,-
  –,  Welcome To my Tools  ,-
 –,     Cosed by Zeerx7   ,-
  –,-,-,-,-,-,-,-,-,-,-,-,-
";
$bann=array($banner1,$banner2,$banner3);
$bann1=array_rand($bann,2);
$banner=$bann[$bann1[1]];


$set="\e[93mTools ini berfungsi untuk mengubah 
Tampilan header TERMUX anda.
\e[91m
  ( warning!!! )
Ketika anda menekan enter maka tools ini akan
mulai menghapus dan menulis kembali dengan
yang akan di imputkan nanti
\e[92m
ketik exit jika ingin menghentikan tools ini
dan Tekan ENTER untuk memulai program
\e[36m ENTER\e[91m$\e[36m>  ";
//internet();
system("clear");
echo "\e[36m".$banner;
echo $set;
$inputst = trim(fgets(STDIN));
if($inputst == "exit" or $inputst == "EXIT" or $inputst == "Exit"){
  exit();
}else{
  //internet();
  //echo $ambil."\n";
  cekdir();
  cekpack();
  $start = 'go';
  include ".conf.php";
}

/*
dibikin open source bukan buat di record ya bangsad ):<*/
?>
