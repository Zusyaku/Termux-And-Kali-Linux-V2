<?php
class pausiGans{
  var $list;
  var $result;
  var $api = 'https://tools.zone-xsec.com/api/reverse-ip.php?key=pausigans9911&pausi=';
  public function WoW(){
    if(file_exists($this->list)){
       $f = trim(file_get_contents($this->list));
       $pausiGanteng = explode("\n",$f);
       foreach($pausiGanteng as $x){
         self::pausi($x,$this->result,$this->api);
       }
       if(file_exists($this->result)){
         echo "your results are stored in ".$this->result."\n";
       }
    }else{
        echo "\nList Not Found! \n";
    }
  }
  public static function pausi($x,$y,$z){
   //$t = $x; //"seo101.org";
   $ip = $x; //self::curl($t)[1];
   $_ = $z.$ip;
   $__ = self::curl($_)[0]; //file_get_contents($_);
   //$x = str_replace("\n",'~',$__);
   //preg_match_all("`<pre class=\"threecols\">(.+?)</pre>`",$x,$r);
   //print_r($r[1]);
   //$s = explode("~",trim($r[1][0]));
   //echo $__;
   $s = json_decode($__,true);
   if($s['message'] == 'Error url or apikey'){
     echo $s['message']."\n";
     exit;
   }else{
     //print_r($s);
     foreach($s['urls'] as $pausi){
        if(!empty($pausi)){
           echo $pausi ." [Saved✓]\n";
           fwrite(fopen($y,'a+'),$pausi."\n");
           sleep(00.1);
        }
     }
   }
  }
  public static function curl($u){
         if(!preg_match("`http(s)://`",$u)){ $u = 'http://'.$u; }
         $ch = curl_init();
         curl_setopt($ch, CURLOPT_URL, $u);
         curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
         $x = curl_exec($ch);
         $ip = curl_getinfo($ch,CURLINFO_PRIMARY_IP);
         curl_close($ch);
         return [$x,$ip];
  }
}

echo "
* * * * * * * * * * * * * *
~ Reverse IP
~ Coded by Zeerx7(Pausi)
~ XploitSec-ID
~ zone-xsec.com
* * * * * * * * * * * * * *

Input List-> ";
$list = trim(readline());
if(file_exists($list)){
   $pausi = new pausiGans;
   $pausi->list = $list; //'list.txt';
   $pausi->result = 'result.txt';
   $pausi->WoW();
}else{
   echo "List Not Found! \n";
}
