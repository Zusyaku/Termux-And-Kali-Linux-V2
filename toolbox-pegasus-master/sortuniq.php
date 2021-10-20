<?php
include 'functions.php';
$debug = 0;
$thestring = "";

debug("_POST");
if ($_SERVER["REQUEST_METHOD"] == "POST") {
	$thestring = $_POST["thestring"];
	debug("thestring");
	// Replace alternative line endings all with \n
	$linearray = str_replace("\r\n", "\n", $thestring);
	debug("linearray");
	$lines = explode("\n", $linearray);
	debug("lines");
	$thestring = array_unique($lines, SORT_STRING);
	natsort($thestring);
	$thestring = implode("\n", $thestring);
}
?>
<html>
<head>
	<title>Sort text and remove duplicates</title>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
</head>
<body>
	<p>This script sorts the entered text's lines and removes duplicate lines.</p>
	<p>Enter your text in here:</p>
	<form name="sortuniq" action="<?php echo $_SERVER['PHP_SELF']; ?>" method="post">
		<textarea name="thestring" rows="35" cols="100" wrap="hard"><?php echo $thestring;?></textarea>
		<br />
		<input type="submit" value="Sort and unique" />
	</form>
</body>
</html>
