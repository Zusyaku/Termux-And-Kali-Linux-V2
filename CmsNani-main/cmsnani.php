<?php
error_reporting(0);
set_time_limit(5);
print ini_get('max_execution_time') . "\n";
if (PHP_OS == "Windows") {
  system('cls');
}else {
  system('clear');
}
echo "\033[36m
   _____               _   _             _
  / ____|             | \ | |           (_)
 | |     _ __ ___  ___|  \| | __ _ _ __  _
 | |    | '_ ` _ \/ __| . ` |/ _` | '_ \| |
 | |____| | | | | \__ \ |\  | (_| | | | | |
  \_____|_| |_| |_|___/_| \_|\__,_|_| |_|_|

              LoliC0d3 - Tegal1337

\033[39m";
$file = "ResultCms.txt";
echo " List Target-> ";
$list = trim(fgets(STDIN));
$open = fopen("$list","r");
$size = filesize("$list");
$read = fread($open,$size);
$urls = explode("\n",$read);
foreach($urls as $url){
  $cms = get_meta_tags($url);
  if (!empty($cms['generator'])) {
    $yes = $url ;
    $loli = $url. PHP_EOL;
    $res = $yes ." =>\033[32m " . $cms['generator']. PHP_EOL . "\033[39m";
    echo $res;
    file_put_contents($file ,$loli, FILE_APPEND | LOCK_EX);
  }else {
    echo $url . " => \033[31mUnknown\033[39m" . PHP_EOL;
  }
}
 ?>
