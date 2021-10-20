<?php
/*
 * This file is to test the functions of the "functions.php" file
 */
include 'functions.php';

echo "<h2>--Testing debug()</h2>";

// testing debug()
$debug = 1;
// simple string variable
$var = "test string";
debug("var");

// simple one dimensional array
$var = array("this", "is", "an", "array");
debug("var");

// one dimensional array with keys
$var = array(
	"this" => "is",
	"an" => "array"
	);
debug("var");

// two dimensional array
$var = array(
	array("one", "two", "three"),
	array("red", "green", "blue")
	);
debug("var");

echo "<h2>--Testing cdx_conv_date()</h2>";
$testdate = date("Y-m-d H:i:s");
echo "Sending date: $testdate<br/>";
echo cdx_conv_date($testdate, "-");

echo "<h2>--Testing cdx_put_select()</h2>";
$data = array("red", "green", "blue");
echo cdx_put_select("my_select", $data, "2");

echo "<h2>--Testing cdx_date_select()</h2>";
echo cdx_date_select(date("Y-m-d"), "datetest");

?>