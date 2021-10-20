<html>
<head>
	<title>UNIX timestamp converter</title>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
</head>
<body>
	<p>This script converts a <a href="http://en.wikipedia.org/wiki/Timestamp" target="_new">UNIX timestamp</a>
	to a more readable format: "day-month-year hours:minutes:seconds"</p>
	<p>Enter a UNIX timestamp:</p>
	<form name="timestamper" action="<?php echo $_SERVER['PHP_SELF']; ?>" method="post">
		<input type="text" name="string" size="35" maxlength="255">
		<input type="submit" value="Process">
	</form>

	<?php
//$dateunix = "1188649800";
if ($_SERVER["REQUEST_METHOD"] == "POST") {
	$string = $_POST["string"];
	if (strlen($string) > 0) {
		if (($newdate = @date("d-m-Y H:i:s", $string)) === false) {
			print('The entered string "'. $string .'" is not a valid <b>timestamp</b>.');
		} else {
			print('The timestamp: "<b>'. $string .' GMT +0</b>"<br />
					is: "<strong>'.$newdate.'</strong>"<br />'."\n");
		}
	}
}

?>
</body>
</html>
