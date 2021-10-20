<?php

function banner(){
    include 'config.php';
    @system("clear");
    print "$okegreen    ____                  __$yellow    __              \n";
    print "$okegreen   / __ \____ _____  ____/ /$yellow / / /_______  _____\n";
    print "$okegreen  / /_/ / __ `/ __ \/ __  /$yellow / / / ___/ _ \/ ___/\n";
    print "$okegreen / _, _/ /_/ / / / / /_/ /$yellow /_/ (__  )  __/ /    \n";
    print "$okegreen/_/ |_|\__,_/_/ /_/\__,_/$yellow\____/____/\___/_/     \n";
    print "$white    Create Your Random User Information         \n";
    print "\n";
}

function randomuser(){
    include 'config.php';
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_URL,'https://randomuser.me/api/');
    $result=curl_exec($ch);
    $json = json_decode($result, true);
    foreach ($json['results'] as $row){
        $gender = $row['gender'];
        $firstname = $row['name']['first'];
        $lastname = $row['name']['last'];
        $street = $row['location']['street'];
        $city = $row['location']['city'];
        $state = $row['location']['state'];
        $postcode = $row['location']['postcode'];
        $birth = $row['dob']['date'];
        $age = $row['dob']['age'];
        $phone = $row['phone'];
        $cell = $row['cell'];
        print "$cyan [$white Name$cyan ]$red >$white $firstname $lastname\n";
        print "$cyan [$white Gender$cyan ]$red >$white $gender\n";
        print "$cyan [$white Location$cyan ]$red >$white $street, $city, $state\n";
        print "$cyan [$white PostCode$cyan ]$red >$white $postcode\n";
        print "$cyan [$white Age$cyan ]$red >$white $age\n";
        print "\n";
    }
}

function uinames(){
    include 'config.php';
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_URL,'https://uinames.com/api/?ext');
    $result=curl_exec($ch);
    $json = json_decode($result, true);
    $name = $json['name'];
    $surname = $json['surname'];
    $gender = $json['gender'];
    $region = $json['region'];
    $age = $json['age'];
    $phone = $json['phone'];
    $birth = $json['birthday']['dmy'];
    $ccnum = $json['credit_card']['number'];
    $ccexp = $json['credit_card']['expiration'];
    $ccpin = $json['credit_card']['pin'];
    $cccvv = $json['credit_card']['security'];
    $photo = $json['photo'];
    print "$cyan [$white Name$cyan ]$red >$white $name $surname\n";
    print "$cyan [$white Gender$cyan ]$red >$white $gender\n";
    print "$cyan [$white Region$cyan ]$red >$white $region\n";
    print "$cyan [$white Birth$cyan ]$red >$white $birth\n";
    print "$cyan [$white Age$cyan ]$red >$white $age\n";
    print "$cyan [$white Phone$cyan ]$red >$white $phone\n";
    print "$cyan [$white CreditCard$cyan ]$red >$white $ccnum $ccexp $cccvv\n";
    print "\n";
}

banner();
uinames();

?>
