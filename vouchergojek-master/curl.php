<?php

function request($url, $token = null, $data = null, $pin = null){
$header[] = "Host: api.gojekapi.com";
$header[] = "User-Agent: okhttp/3.10.0";
$header[] = "Accept: application/json";
$header[] = "Accept-Language: en-ID";
$header[] = "Content-Type: application/json; charset=UTF-8";
$header[] = "X-AppVersion: 3.30.2";
$header[] = "X-UniqueId: ".time()."57".mt_rand(1000,9999);
$header[] = "Connection: keep-alive";
$header[] = "X-User-Locale: en_ID";
$header[] = "X-Location: -6.246265,106.690718";
$header[] = "X-Location-Accuracy: 3.0";
if ($pin):
$header[] = "pin: $pin";
    endif;
if ($token):
$header[] = "Authorization: Bearer $token";
endif;
$c = curl_init("https://api.gojekapi.com".$url);
    curl_setopt($c, CURLOPT_FOLLOWLOCATION, true);
    curl_setopt($c, CURLOPT_SSL_VERIFYPEER, false);
    if ($data):
    curl_setopt($c, CURLOPT_POSTFIELDS, $data);
    curl_setopt($c, CURLOPT_POST, true);
    endif;
    curl_setopt($c, CURLOPT_SSL_VERIFYHOST, 0);
    curl_setopt($c, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($c, CURLOPT_HEADER, true);
    curl_setopt($c, CURLOPT_HTTPHEADER, $header);
    $response = curl_exec($c);
    $httpcode = curl_getinfo($c);
    if (!$httpcode)
        return false;
    else {
        $header = substr($response, 0, curl_getinfo($c, CURLINFO_HEADER_SIZE));
        $body   = substr($response, curl_getinfo($c, CURLINFO_HEADER_SIZE));
    }
    $json = json_decode($body, true);
    return $json;
}
function save($filename, $content)
{
    $save = fopen($filename, "a");
    fputs($save, "$content\r\n");
    fclose($save);
}

function nama()
    {
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, "http://ninjaname.horseridersupply.com/indonesian_name.php");
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
    curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
    $ex = curl_exec($ch);

    preg_match_all('~(&bull; (.*?)<br/>&bull; )~', $ex, $name);
    return $name[2][mt_rand(0, 14) ];
    }

function register($no)
    {
    $nama = nama();
    $email = str_replace(" ", "", $nama) . mt_rand(100, 999);
    $data = '{"email":"'.$email.'@gmail.com","name":"'.$nama.'","phone":"+'.$no.'","signed_up_country":"ID"}';
    $register = request("/v5/customers", "", $data);
    if ($register['success'] == 1)
        {
        return $register['data']['otp_token'];
        }
      else
        {
      save("error_log.txt", json_encode($register));
        return false;
        }
    }

    function login($no)
    {

    $data = '{"phone":"+'.$no.'"}';
    $register = request("/v4/customers/login_with_phone", "", $data);
   
    if ($register['success'] == 1)
        {
        return $register['data']['login_token'];
        }
      else
        {
      save("error_log.txt", json_encode($register));
        return false;
        }
    }

function veriflogin($otp, $token)
    {
    $data = '{"client_name":"gojek:cons:android","client_secret":"83415d06-ec4e-11e6-a41b-6c40088ab51e","data":{"otp":"'.$otp.'","otp_token":"'.$token.'"},"grant_type":"otp","scopes":"gojek:customer:transaction gojek:customer:readonly"}';
    $verif = request("/v4/customers/login/verify", "", $data);
    if ($verif['success'] == 1)
        {
        return $verif['data']['access_token'];
        }
      else
        {
      save("error_log.txt", json_encode($verif));
        return false;
        }
    }
function change($no)
{
    $data = '{"email":"' .$email . '","name":"'.$nama.'","phone":"+'.$no.'"}';
    $change = request("/v4/customers" ,"", $data);
    if ($change['success'] == 1) {
        return $change;
    }
    else{
        save("error_log.txt", json_encode($change));
        return false;
    }
}
function verifchange($otp,$uid)
{
    $data = '{"id":'.$uid.',"phone":"+'.$no.'","verificationCode":"'.$otp.'"}';
        $verifchange = request("/v4/customer/verificationUpdateProfil" ,"",$data);
        if ($verifchange['success'] == 1) {
            return $verifchange;
        }
        else{
            save("error_log.txt", json_encode($verifchange));
        return false;
        }
}
function verif($otp, $token)
    {
    $data = '{"client_name":"gojek:cons:android","data":{"otp":"' . $otp . '","otp_token":"' . $token . '"},"client_secret":"83415d06-ec4e-11e6-a41b-6c40088ab51e"}';
    $verif = request("/v5/customers/phone/verify", "", $data);
    if ($verif['success'] == 1)
        {
        return $verif['data']['access_token'];
        }
      else
        {
       save("error_log.txt", json_encode($verif));
        return false;
        }
    }
function claim($token)
    {
    $data = '{"promo_code":"GOFOODBOBA07"}';    
    $claim = request("/go-promotions/v1/promotions/enrollments", $token, $data);
    if ($claim['success'] == 1)
        {
        return $claim['data']['message'];
        }
      else
        {
      save("error_log.txt", json_encode($claim));
        return false;
        }
    }
    function claim1($token)
    {
    $data = '{"promo_code":"GOFOODBOBA10"}';    
    $claim = request("/go-promotions/v1/promotions/enrollments", $token, $data);
    if ($claim['success'] == 1)
        {
        return $claim['data']['message'];
        }
      else
        {
      save("error_log.txt", json_encode($claim));
        return false;
        }
    }
    function claim2($token)
    {
    $data = '{"promo_code":"GOFOODBOBA19"}';    
    $claim = request("/go-promotions/v1/promotions/enrollments", $token, $data);
    if ($claim['success'] == 1)
        {
        return $claim['data']['message'];
        }
      else
        {
      save("error_log.txt", json_encode($claim));
        return false;
        }
    }
     function ride($token)
    {
    $data = '{"promo_code":"COBAINGOJEK"}';    
    $claim = request("/go-promotions/v1/promotions/enrollments", $token, $data);
    if ($claim['success'] == 1)
        {
        return $claim['data']['message'];
        }
      else
        {
      save("error_log.txt", json_encode($claim));
          return false;
        }
    }
     function cekvocer($token)
    {
    $data = '{"promo_code":"AYOCOBAGOJEK"}';    
    $claim = request("/go-promotions/v1/promotions/enrollments", $token, $data);
    if ($claim['success'] == 1)
        {
        return $claim['data']['message'];
        }
      else
        {
      save("error_log.txt", json_encode($claim));
        return false;
        }
    }
     function pengen($token)
    {
    $data = '{"promo_code":"JAJANPAKEGOPAY"}';    
    $claim = request("/go-promotions/v1/promotions/enrollments", $token, $data);
    if ($claim['success'] == 1)
        {
        return $claim['data']['message'];
        }
      else
        {
      save("error_log.txt", json_encode($claim));
        return false;
        }
    }
?>
