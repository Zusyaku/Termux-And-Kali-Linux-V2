<html>
<head>
	<title>Url encoder - decoder</title>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
</head>
<body>
	<p>This script encodes and decodes a string via de <i>urlencode()</i> and <i>urldecode()</i> functions.</p>
	<p>Please enter a string:</p>
	<form name="urlencode" action="<?php echo $_SERVER['PHP_SELF']; ?>" method="post">
		<input type="text" name="urlstring" size="50" maxlength="255">
		<input type="submit" value="Process">
	</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
	$string = $_POST["urlstring"];
	if (strlen($string) > 0) {
		print('<div>Original string:<br/>
				&nbsp;&nbsp;&nbsp;&nbsp;<strong>'. $string .'</strong></div>
				encoded: <br/>
				&nbsp;&nbsp;&nbsp;&nbsp;<strong>'.urlencode($string).'</strong><br/>
				decoded:<br/> 
				&nbsp;&nbsp;&nbsp;&nbsp;<strong>'.urldecode($string).'</strong><br/>'."\n");
	}
}

?>
</body>
</html>
