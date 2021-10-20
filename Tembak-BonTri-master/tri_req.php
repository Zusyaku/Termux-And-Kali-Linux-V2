<?php

class tri{
  
  function curls($host,$header,$body,$method)
  	{
  		$ch = curl_init();
  		curl_setopt($ch, CURLOPT_URL, $host);
  		curl_setopt($ch, CURLOPT_HTTPHEADER, $header);	
  		curl_setopt($ch, CURLOPT_HEADER, true);
  		curl_setopt($ch, CURLOPT_CUSTOMREQUEST, $method);
  		curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  		curl_setopt($ch, CURLOPT_ENCODING, 'gzip');
  		curl_setopt($ch, CURLOPT_POSTFIELDS, $body);
  		curl_setopt($ch, CURLOPT_COOKIEJAR, 'cookie.txt');
  		curl_setopt($ch, CURLOPT_COOKIEFILE, 'cookie.txt');
  		curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, true);
  		$req = curl_exec($ch);
  		$req = explode("\r\n\r\n", $req);
  		return $req;
  	}



  function request_otp($msisdn,$imei)
  {
    $body = array("msisdn"=>$msisdn);
    $body = json_encode($body);
    $ctl = strlen($body);
    $header = array("Host:bonstri.tri.co.id" ,
 "Connection:keep-alive" ,
 "Content-Length:" . $ctl ,
 "Accept:application/json, text/plain, */*" ,
 "Origin:http://bonstri.tri.co.id" ,
 "User-Agent:Mozilla/5.0 (Linux; Android 9; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36" ,
 "Content-Type:application/json" ,
 "Referer:http://bonstri.tri.co.id/login?returnUrl=%2Fhome" ,
 "Accept-Encoding:gzip, deflate" ,
 "Accept-Language:id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7");
    $response = $this->curls('http://bonstri.tri.co.id/api/v1/login/request-otp',$header,$body,'POST');
    return $response;
  }
  
  function login($msisdn,$otp)
  {
    $body = "grant_type".'='."password".'&'."username".'=' . $msisdn . '&'."password".'='.$otp;
    $ctl = strlen($body);
    $header = array("Host:bonstri.tri.co.id" ,
 "Connection:keep-alive" ,
 "Content-Length:" . $ctl ,
 "Accept:application/json, text/plain, */*" ,
 "Origin:http://bonstri.tri.co.id" ,
 "Authorization:Basic Ym9uc3RyaTpib25zdHJpc2VjcmV0" ,
 "User-Agent:Mozilla/5.0 (Linux; Android 9; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36" ,
 "Content-Type:application/x-www-form-urlencoded" ,
 "Referer:http://bonstri.tri.co.id/login?returnUrl=%2Fhome" ,
 "Accept-Encoding:gzip, deflate" ,
 "Accept-Language:id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7");
    $response = $this->curls('http://bonstri.tri.co.id/api/v1/login/validate-otp',$header,$body,'POST');
    return $response[1];
  }
  
  function trans($bearer)
  {
    $body = '{}';
    $header = array("Host:bonstri.tri.co.id" ,
 "Connection:keep-alive" ,
 "Content-Length:2" ,
 "Accept:application/json, text/plain, */*" ,
 "Origin:http://bonstri.tri.co.id" ,
 "Authorization:Bearer " . $bearer,
 "User-Agent:Mozilla/5.0 (Linux; Android 9; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36" ,
 "Content-Type:application/json" ,
 "Referer:http://bonstri.tri.co.id/voucherku" ,
 "Accept-Encoding:gzip, deflate" ,
 "Accept-Language:id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7");
   $response = $this->curls("http://bonstri.tri.co.id/api/v1/voucherku/voucher-history",$header,$body,"POST");
   return $response[1];
   
  }
  
  function claim($bearer,$id,$id1)
  {
    $body = array("rewardId"=>$id1,"rewardTransactionId"=>$id);
    $body = json_encode($body);
    $ctl = strlen($body);
    $header = array("Host:bonstri.tri.co.id" ,
 "Connection:keep-alive" ,
 "Content-Length:" . $ctl ,
 "Accept:application/json, text/plain, */*" ,
 "Origin:http://bonstri.tri.co.id" ,
 "Authorization:Bearer " . $bearer ,
 "User-Agent:Mozilla/5.0 (Linux; Android 9; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36" ,
 "Content-Type:application/json" ,
 "Referer:http://bonstri.tri.co.id/voucherku" ,
 "Accept-Encoding:gzip, deflate" ,
 "Accept-Language:id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7");
     $response = $this->curls("http://bonstri.tri.co.id/api/v1/voucherku/get-voucher-code",$header,$body,"POST");
     return $response[1];
  }
  
  
  
}
?>