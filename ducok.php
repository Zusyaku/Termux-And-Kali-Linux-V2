<?php

error_reporting(0);
#Colors
$ress = "\033[0;32m";
$res = "\033[0;33m";
$red = "\033[0;31m";
$green = "\033[0;37m";
$nau= "\e[38;5;94m";
$white = "\033[0;33m";
$banner = "\r";
$xnhac = "\033[1;96m";
$den = "\033[1;90m";
$do = "\033[1;91m";
$luc = "\033[1;92m";
$vang = "\033[1;93m";
$xduong = "\033[1;94m";
$hong = "\033[1;95m";
$trang = "\033[1;97m";
$y2="\033[0;33m";
$white= "\033[0;37m";
$cyan= "\e[1;36m";
$blue="\e[1;34m";
$ngreen="\033[42m";
$ngreen="\033[42m";
$maul=rand(31,37);
$maui="\033[1;".$maul."m";
$banner="\r
\e[1;31m\     Đức Nobi ♡     I Love You ♡
\033[1;32m\  ▅▅▅▅░░░░▅▅░░ ▅▅░░░▅▅▅
\033[1;33m\  ▅▅░░▅▅░░▅▅░░ ▅▅░░▅▅
\033[1;31m\ ▅▅▅▅░▅▅░░▅▅░░ ▅▅░░▅
\033[1;95m\  ▅▅░░▅▅░░▅▅░░ ▅▅░░▅▅
\033[1;94m   ▅▅▅▅░░░░ ▅▅▅▅░░░░░▅▅▅
\n";
@system('rm TDS.txt');
@system('clear');
echo $banner;
echo"\033[1;37m\033[1;41m \033[1;32m🌺\033[;33m TOOL TDS Đa Luồng Token\033[1;32m 🌺 \033[0m
$vang •╔═════════════════════════☩══♛══☩═════════════════════════╗• 
$blue        ☞ Zalo: 0398951396
$hong        ☞ Tsr: 0398951396
$luc        ☞ Facebook: https://www.facebook.com/ducnobi2004
$vang •╚═════════════════════════☩══✦══☩═════════════════════════╝•\n";
  echo "\e[1;34m┌─[\033[0;41m\e[1;32mNhấn Enter!\e[0m\e[1;34m]
└──╼ \e[1;35m❯\e[1;36m❯\e[1;31m❯ $yellowb ";
$wowksk=trim(fgets(STDIN));
@system('clear');

$banner="\r
\e[1;31m\     Đức Nobi ♡     I Love You ♡
\033[1;32m\  ▅▅▅▅░░░░▅▅░░ ▅▅░░░▅▅▅
\033[1;33m\  ▅▅░░▅▅░░▅▅░░ ▅▅░░▅▅
\033[1;31m\ ▅▅▅▅░▅▅░░▅▅░░ ▅▅░░▅
\033[1;95m\  ▅▅░░▅▅░░▅▅░░ ▅▅░░▅▅
\033[1;94m   ▅▅▅▅░░░░ ▅▅▅▅░░░░░▅▅▅
\n";
@system('rm TDS.txt');
@system('clear');
echo $banner;
echo"\033[1;37m\033[1;41m \033[1;32m🌺\033[;33m TOOL TDS Đa Luồng Token\033[1;32m🌺 \033[0m
$vang •╔═════════════════════════☩══♛══☩═════════════════════════╗• 
$blue        ☞ Zalo: 0398951396
$hong        ☞ Tsr: 0398951396
$luc        ☞ Facebook: https://www.facebook.com/ducnobi2004
$vang •╚═════════════════════════☩══✦══☩═════════════════════════╝•\n";
//login

echo"
                    \033[0;033m•╔═════☩══♛══☩═════╗•
                        \033[0;41m\e[1;32m◆ ĐĂNG NHẬP ◆\e[0m
                    \033[0;033m•╚═════☩══✦══☩═════╝•$end";
echo"\n";


$dem = 0;
  echo "\e[1;34m┌─[\e[1;37m\e[1;42mNhập Token TDS\e[0m\e[1;34m]
└──╼ \e[1;35m❯\e[1;36m❯\e[1;31m❯ $yellowb ";
  $tokenacc = trim(fgets(STDIN));
//Token 
$khoToken = [];
echo "\e[1;34m┌─[\e[1;37m\e[1;42mSố Token FaceBook Cần Làm\e[0m\e[1;34m]
└──╼ \e[1;35m❯\e[1;36m❯\e[1;31m❯ $yellowb ";
$luong=trim(fgets(STDIN));
for($a=1;$a<=$luong;$a++){
echo "\e[1;34m┌─[\e[1;37m\e[1;42mThập Token Fb Thứ $a $do\e[0m\e[1;34m]
└──╼ \e[1;35m❯\e[1;36m❯\e[1;31m❯ $yellowb ";
$nhapck = (string)trim(fgets(STDIN));
if($nhapck == ''){break;}
array_push($khoToken,$nhapck);
    }
//url
$urlinfo = "https://traodoisub.com/api/?fields=profile&access_token=$tokenacc";
$urllike = "https://traodoisub.com/api/?fields=like&access_token=$tokenacc";
$urlsub = "https://traodoisub.com/api/?fields=follow&access_token=$tokenacc";
$urlcmt = "https://traodoisub.com/api/?fields=comment&access_token=$tokenacc";
$urlshare = "https://traodoisub.com/api/?fields=share&access_token=$tokenacc";
//login https://traodoisub.com/api/?fields=share&access_token=TDS0nIxIXZ2V2ciojIyVmdlNnIsISNwAzM0RnxawfIyV2c1Jye
$info = api($urlinfo);
if ($info["error"]) {
    exit ($info["error"]);
}
//$thongtin
$user = strtolower($info["data"]["user"]);
$xuhientai = $info["data"]["xu"];
@system('clear');
 echo $banner;
echo"\033[1;37m\033[1;41m \033[1;32m🌺\033[;33m TOOL TDS Đa Luồng Token\033[1;32m🌺 \033[0m
$vang •╔═════════════════════════☩══♛══☩═════════════════════════╗• 
$blue        ☞ Zalo: 0398951396
$hong        ☞ Tsr: 0398951396
$luc        ☞ Facebook: https://www.facebook.com/ducnobi2004
$vang •╚═════════════════════════☩══✦══☩═════════════════════════╝•\n";
echo $do."[".$luc."●".$do."] ".$trang."=> ".$luc."Tên Tài Khoản Trao Đổi Sub: ".$vang."".$user."\n";
echo $do."[".$luc."●".$do."] ".$trang."=> ".$luc."Số Xu Hiện Tại: ".$vang."".$xuhientai."\n";
echo $do."[".$luc."●".$do."] ".$trang."=> ".$luc."Nhập ".$do."[".$vang."1".$do."]".$luc." Nhiệm Vụ Like\n";
echo $do."[".$luc."●".$do."] ".$trang."=> ".$luc."Nhập ".$do."[".$vang."2".$do."]".$luc." Nhiệm Vụ Follow\n";
echo $do."[".$luc."●".$do."] ".$trang."=> ".$luc."Nhập ".$do."[".$vang."3".$do."]".$luc." Nhiệm Vụ Comment\n"; 
echo $do."[".$luc."●".$do."] ".$trang."=> ".$luc."Nhập ".$do."[".$vang."4".$do."]".$luc." Để Chạy Nhiệm Vụ Share\n";
echo $do."Muốn Chạy Random Thì ghi số rồi thêm dấu cộng => vd :1+2+3\n";                                            
echo "\e[1;34m┌─[\e[1;37m\e[1;42mChọn Chế Độ\e[0m\e[1;34m]
└──╼ \e[1;35m❯\e[1;36m❯\e[1;31m❯ $yellowb ";
$nhiemvu = trim(fgets(STDIN));
//while (true){
echo "\e[1;34m┌─[\e[1;37m\e[1;42mMIN\e[0m\e[1;34m]
└──╼ \e[1;35m❯\e[1;36m❯\e[1;31m❯ $yellowb ";
$delay1 = trim(fgets(STDIN));
echo "\e[1;34m┌─[\e[1;37m\e[1;42mMAX\e[0m\e[1;34m]
└──╼ \e[1;35m❯\e[1;36m❯\e[1;31m❯ $yellowb ";
$delay2 = trim(fgets(STDIN));
//if ( is_numeric($delay1) == '' or numeric($delay2) == '' ) { echo " Lỗi Không Xác Định !!! \n"; continue; }
//else if ( ($delay1) > ($delay2) ) { echo $do." Min Phải Nhỏ Hơn Max Nhé, Vui Lòng Nhập Lại \n"; continue; }
//else { break; }}
echo "\e[1;34m┌─[\e[1;37m\e[1;42mSau Bao Nhiêu Nhiệm Vụ Thì Bật Chống Block\e[0m\e[1;34m]
└──╼ \e[1;35m❯\e[1;36m❯\e[1;31m❯ $yellowb ";
$xxxxx = trim(fgets(STDIN));
echo "\e[1;34m┌─[\e[1;37m\e[1;42mSau ".$vang.$xxxxx.$luc." \e[1;42mNghỉ Ngơi Bao Nhiêu Dây\e[0m\e[1;34m]
└──╼ \e[1;35m❯\e[1;36m❯\e[1;31m❯ $yellowb ";
$delaybl = trim(fgets(STDIN));
echo "\e[1;34m┌─[\e[1;37m\e[1;42mĐổi Cấu Hình Sau\e[0m\e[1;34m]
└──╼ \e[1;35m❯\e[1;36m❯\e[1;31m❯ $yellowb ";
$doinick = trim(fgets(STDIN));
 echo $vang ."===============================================================\n";
while(true){
  if(count($khoToken) == 0){
for($a = 1; $a < 999999;$a++){
echo "\e[1;34m┌─[\e[1;37m\e[1;42mNhập Token Thứ $a $do\e[0m\e[1;34m]
└──╼ \e[1;35m❯\e[1;36m❯\e[1;31m❯ $yellowb ";
$nhapck = (string)trim(fgets(STDIN));
if($nhapck == ''){break;}
array_push($khoToken,$nhapck);
    }
            $js=json_encode($khoToken);
            $demcki=count($khoToken);
            $k = fopen("Token.txt","a+");
fwrite($k, $js);
fclose($k);
echo $do."[".$luc."●".$do."] ".$trang."=> ".$luc."Tìm Thấy ".$vang.$demcki." ".$luc."Token\n";
  }
  for($xz=0;$xz<count($khoToken);$xz++){
    $cookie = $khoToken[$xz];
$access_token = $cookie;
if (strpos($access_token, 'EAAGN') !== 0) {
    echo "Token đúng rùi nè 💖 \n";
}
$tenfb = json_decode(file_get_contents('https://graph.facebook.com/me/?access_token='.$access_token))-> {'name'};
$idfb = json_decode(file_get_contents('https://graph.facebook.com/me/?access_token='.$access_token))-> {'id'};
$urlcauhinh = "https://traodoisub.com/api/?fields=run&id=$idfb&access_token=$tokenacc";
$cauhinh = api($urlcauhinh);
if ($cauhinh["data"]["msg"] == "Cấu hình thành công!") {
    echo $vang."•╔═════════════════════════☩══♛══☩═════════════════════════╗•\n";
       echo $vang."  \033[0;41m\e[1;32m Đang Cấu Hình ID: ".$luc.$idfb." ".$vang."Tên FB: ".$luc.$tenfb."".$res."\n";
    echo $vang."•╚═════════════════════════☩══✦══☩═════════════════════════╝•\n";
} else {
    echo $do."Cấu hình thất bại token có thể bị die thay token tại file ".$trang."Token.txt\n";
    exit;
}
$spam = 0;
while (true) {
    if ($spam == 1) {
        break;
    }
    //listlike
    if (strpos($nhiemvu, '1') !== false) {
        for ($i = 0; $i < 30; $i++) {
            $listlike = api($urllike);
            if (count($listlike) !== 0) {
                break;
            }
        }
    }
    //listfollow
    if (strpos($nhiemvu, '2') !== false) {
        while (true) {
            $listsub = api($urlsub);
            if (count($listsub) !== 0) {
                break;
            }
        }}
    //listcmt
    if (strpos($nhiemvu, '3') !== false) {
        for ($i = 1; $i < 30; $i++) {
            $listcmt = api($urlcmt);
            if (count($listcmt) !== 0) {
                break;
            }}
    }
    //listshare
    if (strpos($nhiemvu, '4') !== false) {
        for ($i = 1; $i < 30; $i++) {
            $listshare = api($urlshare);
            if (count($listshare) > 0) {
                break;
            }}
    }
    for ($lap = 0; $lap < 20; $lap++) {
        // like
        if ($listlike !== NULL) {
            $idlike = $listlike[$lap]["id"];
            if ($idlike !== '') {
                $g = like($access_token, $idlike, $cookie);
                if ($g -> {'error'} -> {'code'} == 190) {
                    echo "Token die !!?!\n";
                    array_splice($khoToken,$xz,1);
                    $spam = 1; break;
                }
                if ($g -> {'error'} -> {'code'} == 368) {
                    echo "\033[1;91m".$g-> {'error'}-> {'message'};
                    echo "\n";
                    $spam = 1;
                    break;
                }
                if ($g -> {'error'} -> {'code'} == 405) {
                    echo "\033[1;91m"."Tài khoản bị checkpoint";
                    $spam = 1;
                    array_splice($khoToken,$xz,1);
                    break;
                }
                $nhanlike = nhantien('LIKE', $idlike, $tokenacc);
                if ($nhanlike["success"] == 200) {
                    $xu = $nhanlike["data"]["xu"];
                    $xujob = $nhanlike["data"]["msg"];
                    $dem++;
                    
                    hoanthanh($dem, ' LIKE ', $idlike, $xujob, $xu);
                    if($dem % $doinick == 0){
                      $spam = 1; break;
                    }
                           if($dem % $xxxxx == 0){
                      delay($delaybl);
                    }
                    
                                  $delay = rand($delay1,$delay2);  
                    delay($delay);
                }
            }}
        //follow
        if ($listsub !== NULL) {
            $idsub = $listsub[$lap]["id"];
            if ($idsub !== '') {
                $g = follow($access_token, $idsub, $cookie);
                if ($g -> {'error'} -> {'code'} == 190) {
                    echo "Token die !!?!\n";
                    array_splice($khoToken,$xz,1);
                    $spam = 1; break;
                }
                if ($g -> {'error'} -> {'code'} == 368) {
                    echo "\033[1;91m".$g-> {'error'}-> {'message'};
                    echo "\n";
                    $spam = 1; break;
                }
                if ($g -> {'error'} -> {'code'} == 405) {
                    echo "\033[1;91m"."Tài khoản bị checkpoint";
                    array_splice($khoToken,$xz,1);
                    $spam = 1; break;
                }
                $nhansub = nhantien('FOLLOW', $idsub, $tokenacc);
                if ($nhansub["success"] == 200) {
                    $xu = $nhansub["data"]["xu"];
                    $xujob = $nhansub["data"]["msg"];
                    $dem++;
                    
                    hoanthanh($dem, 'FOLLOW', $idsub, $xujob, $xu);
                    if($dem % $doinick == 0){
                      $spam = 1; break;
                    }
                            if($dem % $xxxxx == 0){
                      delay($delaybl);
                    }
                    
                                  $delay = rand($delay1,$delay2);  
                    delay($delay);
                }
            }}
            if ($listshare !== NULL) {
                $idshare = $listshare[$lap]["id"];
                if (isset($idshare)) {
                    $r = share($access_token, $idshare);
                    $g = json_decode($r);
                    if ($g -> {'error'} -> {'code'} == 190) {
                        echo "Token die !!?!\n";
                        array_splice($khoToken,$xz,1);
                        $spam = 1; break;
                    }
                    if ($g -> {'error'} -> {'code'} == 368) {
                        echo "\033[1;91m".$g-> {'error'}-> {'message'};
                        echo "\n";
                        array_splice($khoToken,$xz,1);
                        $spam = 1; break;
                    }
                    if ($g -> {'error'} -> {'code'} == 405) {
                        echo "\033[1;91m"."Tài khoản bị checkpoint";
                        array_splice($khoToken,$xz,1);
                        $spam = 1; break;
                    }
                    if (strpos($r, '"id"')){
                        $nhanshare = nhantien('SHARE', $idshare, $tokenacc);
                        if ($nhanshare["success"] == 200) {
                            $xu = $nhanshare["data"]["xu"];
                            $xujob = $nhanshare["data"]["msg"];
                            $dem++;
                            hoanthanh($dem, ' SHARE ', $idshare, $xujob, $xu);
                            if($dem % $doinick == 0){
                              $spam = 1; break;
                            }
                             if($dem % $xxxxx == 0){
                      delay($delaybl);
                    }
                    
                                  $delay = rand($delay1,$delay2);  
                    delay($delay);
                }

                    }else{
                        echo $r;
                    }

                }else{
                    break;
                }
            }
        //cmt
        if ($listcmt !== NULL) {
            $idcmt = $listcmt[$lap]["id"];
            $msg = $listcmt[$lap]["msg"];
            if ($idcmt !== '') {
                cmt($access_token, $idcmt, $cookie, $msg);
                $nhancmt = nhantien('COMMENT', $idcmt, $tokenacc);
                if ($nhancmt["success"] == 200) {
                    $xu = $nhancmt["data"]["xu"];
                    $xujob = $nhancmt["data"]["msg"];
                    $dem++;
                    hoanthanh($dem, ' CMT  ', $idcmt, $xujob, $xu);
                    if($dem % $doinick == 0){
                      $spam = 1; break;
                    }
                              if($dem % $xxxxx == 0){
                      delay($delaybl);
                    }
                    
                                  $delay = rand($delay1,$delay2);  
                    delay($delay);
                }
            }}
        }
}}}
function api($url) {
    $head = array(
        "Host: traodoisub.com",
        "cache-control: max-age=0",
        "upgrade-insecure-requests: 1",
        "user-agent: Mozilla/5.0 (Linux; Android 9; Mi A1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.110 Mobile Safari/537.36",
        "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "sec-fetch-site: none",
        "sec-fetch-mode: navigate",
        "sec-fetch-user: ?1",
        "sec-fetch-dest: document",
        //"accept-encoding: gzip, deflate, br",
        "accept-language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
    );
    $ch = curl_init();
    curl_setopt_array($ch, array(
        CURLOPT_URL => $url,
        CURLOPT_CUSTOMREQUEST => "GET",
        CURLOPT_HTTPHEADER => $head,
        CURLOPT_SSL_VERIFYPEER => FALSE,
        CURLOPT_RETURNTRANSFER => 1
    ));
    $get = curl_exec($ch);
    curl_close($ch);
    return json_decode($get, true);
}
function nhantien($type, $id, $tokenacc) {
    $nhan = file_get_contents("https://traodoisub.com/api/coin/?type=$type&id=$id&access_token=$tokenacc");
    return json_decode($nhan, true);
}
function follow($access_token, $idtest, $cookie) {
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, 'https://graph.facebook.com/'.$idtest.'/subscribers');
    $head[] = "Connection: keep-alive";
    $head[] = "Keep-Alive: 300";
    $head[] = "authority: m.facebook.com";
    $head[] = "ccept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7";
    $head[] = "accept-language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5";
    $head[] = "cache-control: max-age=0";
    $head[] = "upgrade-insecure-requests: 1";
    $head[] = "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9";
    $head[] = "sec-fetch-site: none";
    $head[] = "sec-fetch-mode: navigate";
    $head[] = "sec-fetch-user: ?1";
    $head[] = "sec-fetch-dest: document";
    curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36');
    curl_setopt($ch, CURLOPT_ENCODING, '');
    curl_setopt($ch, CURLOPT_COOKIE, $cookie);
    curl_setopt($ch, CURLOPT_HTTPHEADER, $head);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);
    curl_setopt($ch, CURLOPT_TIMEOUT, 60);
    curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 60);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, TRUE);
    curl_setopt($ch, CURLOPT_HTTPHEADER, array('Expect:'));
    $data = array('access_token' => $access_token);
    curl_setopt($ch, CURLOPT_POST, count($data));
    curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
    $access = curl_exec($ch);
    curl_close($ch);
    return json_decode($access);
}
function like($access_token, $id, $cookie) {
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, 'https://graph.facebook.com/'.$id.'/likes');
    $head[] = "Connection: keep-alive";
    $head[] = "Keep-Alive: 300";
    $head[] = "authority: m.facebook.com";
    $head[] = "ccept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7";
    $head[] = "accept-language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5";
    $head[] = "cache-control: max-age=0";
    $head[] = "upgrade-insecure-requests: 1";
    $head[] = "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9";
    $head[] = "sec-fetch-site: none";
    $head[] = "sec-fetch-mode: navigate";
    $head[] = "sec-fetch-user: ?1";
    $head[] = "sec-fetch-dest: document";
    curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36');
    curl_setopt($ch, CURLOPT_ENCODING, '');
    curl_setopt($ch, CURLOPT_COOKIE, $cookie);
    curl_setopt($ch, CURLOPT_HTTPHEADER, $head);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);
    curl_setopt($ch, CURLOPT_TIMEOUT, 60);
    curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 60);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, TRUE);
    curl_setopt($ch, CURLOPT_HTTPHEADER, array('Expect:'));
    $data = array('access_token' => $access_token);
    curl_setopt($ch, CURLOPT_POST, count($data));
    curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
    $access = curl_exec($ch);
    curl_close($ch);
    return json_decode($access);

}
function share($access_token,$id){
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, 'https://graph.facebook.com/me/feed?method=POST&link=https://www.facebook.com/'.$id.'&privacy={%27value%27:%20%27EVERYONE%27}&access_token='.$access_token);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'GET');
    curl_setopt($ch, CURLOPT_ENCODING, 'gzip, deflate');
    $headers = array();
    $headers[] = 'Authority: graph.facebook.com';
    $headers[] = 'Upgrade-Insecure-Requests: 1';
    $headers[] = 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36';
    $headers[] = 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9';
    $headers[] = 'Sec-Fetch-Site: none';
    $headers[] = 'Sec-Fetch-Mode: navigate';
    $headers[] = 'Sec-Fetch-User: ?1';
    $headers[] = 'Sec-Fetch-Dest: document';
    $headers[] = 'Accept-Language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5';
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

    $result = curl_exec($ch);
    if (curl_errno($ch)) {
        echo 'Error:' . curl_error($ch);
    }
    curl_close($ch);
    return $result;
}
function cmt($access_token, $idcmt, $cookie, $msg) {
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, 'https://graph.facebook.com/'.$idcmt.'/comments');
    $head[] = "Connection: keep-alive";
    $head[] = "Keep-Alive: 300";
    $head[] = "authority: m.facebook.com";
    $head[] = "ccept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7";
    $head[] = "accept-language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5";
    $head[] = "cache-control: max-age=0";
    $head[] = "upgrade-insecure-requests: 1";
    $head[] = "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9";
    $head[] = "sec-fetch-site: none";
    $head[] = "sec-fetch-mode: navigate";
    $head[] = "sec-fetch-user: ?1";
    $head[] = "sec-fetch-dest: document";
    curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36');
    curl_setopt($ch, CURLOPT_ENCODING, '');
    curl_setopt($ch, CURLOPT_COOKIE, $cookie);
    curl_setopt($ch, CURLOPT_HTTPHEADER, $head);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);
    curl_setopt($ch, CURLOPT_TIMEOUT, 60);
    curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 60);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, TRUE);
    curl_setopt($ch, CURLOPT_HTTPHEADER, array('Expect:'));
    $data = array('message' => $msg, 'access_token' => $access_token);
    curl_setopt($ch, CURLOPT_POST, count($data));
    curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
    $access = curl_exec($ch);
    curl_close($ch);
    return json_decode($access);
}
function hoanthanh($dem, $type, $id, $xujob, $xu) {
$time = date('H:i');
$maul=rand(31,37);
$maui="\033[1;".$maul."m";
                            echo "\e[1;34m┌─[";echo"\033[0;41m\e[1;32m Đức nè 😍\e[0m";;echo"\e[1;31m 🛩 ";echo"\e[1;91m Nguyễn Minh Đức 🛩 Đức Nobi\e[1;91m]";echo"\n";
echo"\e[1;95m└──╼\e[1;95m❯\e[1;36m❯\e[1;31m❯ ";echo"\e[1;47;33m";echo"\033[1;36m[\033[1;36m$dem\033[1;36m]\033[1;90m\033[1;32m👉\033[1;91m$time\033[1;91m👉\033[1;32m$maui$type\033[1;32m👉\033[1;91m$id\033[1;90m👉\033[1;32m$xu\033[1;35m\e[0m\n";
    $len = strlen($a);
    for ($x = 0; $x < $len; $x++) {
        echo $a[$x];
        usleep(1000);
    
    }
}
function delay($delay) {
    for ($time = $delay; $time > -1; $time--) {
        echo "\r\033[1;93m   Ｏ(≧▽≦)Ｏ \033[1;91m 🐋       \033[1;92m L      \033[1;91m |\033[1;93m $time\033[1;91m | ";
        usleep(150000);

        echo "\r\033[1;91m   ┗(•°_°•)\033[0;90m   🐋     \033[0;37m LO     \033[0;31m |\033[0;90m $time\033[0;31m | ";
        usleep(150000);
        echo "\r\033[1;92m   ┗(•°_°•)\033[0;90m     🐋   \033[0;37m LOA    \033[0;31m |\033[0;90m $time\033[0;31m | ";
        usleep(150000);
        echo "\r\033[1;94m   ┗(•°_°•)\033[0;90m       🐋 \033[0;37m LOAD   \033[0;31m |\033[0;90m $time\033[0;31m | ";
        usleep(150000);
        echo "\r\033[1;95m   ┗(•°_°•)\033[0;90m        🐋\033[0;37m LOAD.  \033[0;31m |\033[0;90m $time\033[0;31m | ";
        usleep(150000);
        echo "\r\033[1;95m   ┗(•°_°•)\033[0;90m        🐋\033[0;37m LOAD.. \033[0;31m |\033[0;90m $time\033[0;31m | ";
        usleep(150000);
        echo "\r\033[1;95m   ┗(•°_°•)\033[0;90m        🐋\033[0;37m LOAD...\033[0;31m |\033[0;90m $time\033[0;31m | ";
        usleep(100000);
        echo "\r                                          \r";
    
    }}
function laytoken($cookie) {
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, 'https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed');
    $head[] = "Connection: keep-alive";
    $head[] = "Keep-Alive: 300";
    $head[] = "authority: m.facebook.com";
    $head[] = "ccept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7";
    $head[] = "accept-language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5";
    $head[] = "cache-control: max-age=0";
    $head[] = "upgrade-insecure-requests: 1";
    $head[] = "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9";
    $head[] = "sec-fetch-site: none";
    $head[] = "sec-fetch-mode: navigate";
    $head[] = "sec-fetch-user: ?1";
    $head[] = "sec-fetch-dest: document";
    curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36');
    curl_setopt($ch, CURLOPT_ENCODING, '');
    curl_setopt($ch, CURLOPT_COOKIE, $cookie);
    curl_setopt($ch, CURLOPT_HTTPHEADER, $head);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);
    curl_setopt($ch, CURLOPT_TIMEOUT, 60);
    curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 60);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, TRUE);
    curl_setopt($ch, CURLOPT_HTTPHEADER, array('Expect:'));
    $access = curl_exec($ch);
    curl_close($ch);
    if (explode('\",\"useLocalFilePreview', explode('accessToken\":\"', $access)[1])[0]) {
        $access_token = explode('\",\"useLocalFilePreview', explode('accessToken\":\"', $access)[1])[0];
    }
    return $access_token;
}