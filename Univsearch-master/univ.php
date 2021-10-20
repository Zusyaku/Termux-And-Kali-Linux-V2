<?php

// Color
$blue="\033[1;34m";
$cyan="\033[1;36m";
$okegreen="\033[92m";
$lightgreen="\033[1;32m";
$white="\033[1;37m";
$purple="\033[1;35m";
$red="\033[1;31m";
$yellow="\033[1;33m";

@system("clear");

print "\n";
print "$red  $yellow   $cyan -=[$white University Search tool v.1.0        $cyan ]\n";
print "$red +$yellow --$cyan -=[$white http://universities.hipolabs.com/   $cyan ]\n";
print "$red +$yellow --$cyan -=[$white Follow My Instagram : @putra.go.id  $cyan ]\n";
print "$red +$yellow --$cyan -=[$white Git : https://github.com/N1ght420   $cyan ]\n";
print "\n";
print "$cyan Univ Name$white (blank for search all country)$red :$white ";
$name = trim(fgets(STDIN));
print "$cyan Country$white (blank for search all country)$red :$white ";
$country = trim(fgets(STDIN));
$ch = curl_init();
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
if ($name == '' AND $country != ''){
    curl_setopt($ch, CURLOPT_URL,'http://universities.hipolabs.com/search?country='.$country);
}
elseif ($name != '' AND $country == ''){
    curl_setopt($ch, CURLOPT_URL,'http://universities.hipolabs.com/search?name='.$name);
}
else{
    curl_setopt($ch, CURLOPT_URL,'http://universities.hipolabs.com/search?name='.$name.'&country='.$country);
}
$result=curl_exec($ch);
$json = json_decode($result, true);

foreach ($json as $row){
    $web = $row['web_pages']['0'];
    $code = $row['alpha_two_code'];
    $state = $row['state-province'];
    $country = $row['country'];
    $domain = $row['domains'];
    $name = $row['name'];
    print "$cyan [$white Name$cyan ]$red >$white $name\n";
    print "$cyan [$white Country$cyan ]$red >$white $country ($code)\n";
    print "$cyan [$white Web$cyan ]$red >$white $web\n\n";
}

?>
