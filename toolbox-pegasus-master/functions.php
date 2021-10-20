<?php
/*********************************************************************************
 * functions.php
 *********************************************************************************/

/**
 * debug; Prints a string and a variable value in red (for debugging purposes).
 * @name string containing the name of the variable
 */
function debug($name) {
	global ${$name};
	global $debug;
	$the_style = "color:#f00;font-weight:bold;border:1px solid #f00;margin:1px;";
	// Only show output if debugging is on
	if ($debug == 1) {
		$var = ${$name};
		if (is_array($var)) {
			echo "##<b class=\"bold\">$name</b><br>\n";
			while (list($key, $value) = each($var)){
				print("\n<br>".'<div style="'.$the_style.'">#=>'.$key.' ==> ');
				if (is_array($value)){
					print('<pre>');
					print_r($value);
					print('</pre>');
				} else {
					echo nl2br($value);
				}
				print('</div>'."\n");
			}
		} else {
			print("\n".'<div style="'.$the_style.'">#'.$name.'=>'.$var.'#</div>'."\n");
		}
	}
}

/**
 * cdx_conv_date Receives a date in ISO format and returns a localised date string
 * @date string containing the date in "aaaa-mm-dd hh:mm:ss" ISO format
 * @separator string containing the separator for the output date
 * @return string containing the formatted date
 */
function cdx_conv_date($date, $separator="/") {
	if (@preg_match("/([0-9]{4})-([0-9]{1,2})-([0-9]{1,2}) ([0-9]{2}):([0-9]{2}):([0-9]{2})/", $date, $regs)) {
		return $regs[3].$separator.$regs[2].$separator.$regs[1]." ".$regs[4].":".$regs[5].":".$regs[6];
	} else {
		// If the parameter is not correctly formatted it remains the same
		return "ERROR: Not formatted: &quot;$date&quot;";
	}
}

/**
 * cdx_put_select returns a string with a filled <select> html form item
 * @name the name of the form object
 * @array_values a "key, value" type array with the values for the form item
 * @marked string containing the default delected value
 * @extra string with extra data for the "select" tag, such as javascript events like "onfocus" etc.
 * @return string containing an html <select> tag
 */
function cdx_put_select($name, $array_values, $marked="", $extra="") {
	$string = "";
	// Only create the item if the values are in an array
	if (is_array($array_values)) {
		$string .= '<select name="'.$name.'" class="textbox" '.$extra.'>'."\n";
		$string .= '<option value="--">---</option>'."\n";
		while (list($key, $value) = each($array_values)) {
			$string .= "<option value=\"".$key."\"";
			if ($key == $marked) {
				// The default selected item
				$string .= " selected";
			}
			$string .= ">".$value."</option>\n";
		}
		$string .= "</select>\n";
	} else {
		// Return an error string
		$string .= "cdx_put_select() - Error: input is not an array";
	}
	return $string;
}

/**
 * cdx_date_select Returns a group of <select>s to select a date
 * @default the date selected by default, in yyyy-mm-dd format
 * @prefix the prefix of the field names
 * @order the sort order of the years
 * @extra extra attributes for the <select> tags
 * This functions expects the existence of a global $months array with the names
 * of the months
 */

function cdx_date_select($default, $prefix, $order='asc', $extra="") {
	global $months;
	if (!isset($months)) {
		$months = array(
			"01" => "Enero",
			"02" => "Febrero",
			"03" => "Marzo",
			"04" => "Abril",
			"05" => "Mayo",
			"06" => "Junio",
			"07" => "Julio",
			"08" => "Agosto",
			"09" => "Septiembre",
			"10" => "Octubre",
			"11" => "Noviembre",
			"12" => "Diciembre"
		);
	}
	if ($default == "") {
		// Set default date to zero if there's no default
		$default = date("0000-00-00");
	}
	// Decompose the default date
	list($este_anyo, $este_mes, $este_dia) = explode('-', $default);

	if (checkdate($este_mes, $este_dia, $este_anyo) || $default == "0000-00-00") {
		// If the date is valid, create the <select>s 
		$string = "\n".'<select name="'.$prefix.'_day" class="textbox" '.$extra.'>'."\n\t".'<option value="--"';
		if ($este_dia == "00") {
			$string .= ' selected';
		}
		$string .= '>---</option>'."\n";
		for ($d = 1; $d < 32 ; $d++) {
			$d = str_pad($d, "2", "0", STR_PAD_LEFT);
			$string .= "\t".'<option value="'.$d.'"';
			if ($d == $este_dia) {
				$string .= ' selected';
			}
			$string .= '>'.$d.'</option>'."\n";
		}
		$string .= '</select> -'."\n".'<select name="'.$prefix.'_month" class="textbox">'."\n\t".'<option value="--"';
		if ($este_mes == "00") {
			$string .= ' selected';
		}
		$string .= '>---</option>'."\n";
		for ($m = 1; $m < 13 ; $m++) {
			$m = str_pad($m, "2", "0", STR_PAD_LEFT);
			$string .= "\t".'<option value="'.$m.'"';
			if ($m == $este_mes) {
				$string .= ' selected';
			}
			$string .= '>'.$months[$m].'</option>'."\n";
		}
		$string .= '</select> -'."\n".'<select name="'.$prefix.'_year" class="textbox">'."\n\t".'<option value="--"';
		if ($este_anyo == "0000") {
			$string .= ' selected';
		}
		$string .= '>---</option>'."\n";

		$this_year = date("Y");
		$first_year = $this_year - 5; // 5 year padding for the years
		$last_year = $this_year + 5;
		if ($order == "asc") { 
			for ($y = $first_year; $y < $last_year; $y++) {
				$string .= "\t".'<option value="'.$y.'"';
				if ($y == $este_anyo) {
					$string .= ' selected';
				}
				$string .= '>'.$y.'</option>'."\n";
			}
		} else {
			for ($y = $last_year; $y > $first_year; $y--) {
				$string .= "\t".'<option value="'.$y.'"';
				if ($y == $este_anyo) {
					$string .= ' selected';
				}
				$string .= '>'.$y.'</option>'."\n";
			}
		}
		$string .= '</select>'."\n";
	} else {
		$string = "<b class=\"red\">The date '".$default."' is not correct.</b>";
	}
	return $string;
}

/**
 * cdx_prev_next ; Creates a pager
 * @num_elements the total number of items
 * @init the first item on the current page
 * @limit the numner of items per page
 * @url the URL prefix for the links on the page numbers
 * @returns an html string with the pager elements
 */
function cdx_prev_next($num_elements, $init, $limit, $url) {
	global $config;
	if (!isset($config["margin"])){
		// Set default value for number of pages at each side of the current one
		$margin = 5;
	} else {
		$margin = $config["margin"];
	}
	// Only print the pager if the total numer of items is larger than the limit
	if ($num_elements > $limit) {
		$string = ""; // Initialize the string
		$page_count = 0;
		// See how many pages there are
		$num_pages = floor($num_elements / $limit);
		$resting = $num_elements % $limit;
		// If it's not an integer, round up
		if ($resting > 0) {
			$num_pages++;
		}
		// If it's not the first page, show the backward links
		if ($init > 0) {
			$string .= '<a href="'.$url.'&init=0" class="pager">|&lt;</a>&nbsp;<a href="'.$url.'&init='.($init-$limit).'" class="pager">&lt;&lt;</a>';
		}

		$init_count = 0;
		// Put a number on each page
		// Current one is $init/$limit
		$current = $init/$limit;
		$bottom_margin = ($current-$margin);
		$top_margin = ($current+$margin);
		while ($page_count < $num_pages) {
			// Do nothing while not in the current action radius
			if ($page_count >= $bottom_margin && $page_count <= $top_margin) {
				if ($page_count != $current) {
					$the_class = "pg_no";
				} else {
					$the_class = "pg_yes";
				}
				$string .= '<a href="'.$url.'&init='.$init_count.'" class="'.$the_class.'">'.($page_count+1).'</a>';
			}
			$init_count += $limit;
			$page_count++;
		}

		$last_init = ($num_pages*$limit)-$limit;
		// If it's the las page, and the next one is smaller than the max, don't show more
		$next_init = $init+$limit;
		if ($init < ($num_pages*$limit) && $next_init < ($num_pages*$limit)) {
			$string .= '<a href="'.$url.'&init='.$next_init.'" class="pager">&gt;&gt;</a>';
		}
		// If the current is not the last, show forward links
		if ($init < $last_init) {
			$string .= '&nbsp;<a href="'.$url.'&init='.$last_init.'" class="pager">&gt;|</a>';
		}
		return $string;
	}
}

/**
 * Resamples a jpg image
 */
function resampimagejpg($forcedwidth, $forcedheight, $sourcefile, $destfile) {
	$fw = $forcedwidth;
	$fh = $forcedheight;
	$is = getimagesize($sourcefile);
	$image_width = $is[0];
	$image_height = $is[1];

	if ($image_width >= $image_height) {
		$orientation = 0;
	} else {
		$orientation = 1;
		$fw = $forcedheight;
		$fh = $forcedwidth;
	}
	if ($image_width > $fw || $image_height > $fh) {
		if( ($image_width - $fw) >= ($image_height - $fh)) {
			$iw = $fw;
			$ih = ($fw / $image_width) * $image_height;
		} else {
			$ih = $fh;
			$iw = ($ih / $image_width) * $is[0];
		}
		$t = 1;
	} else {
		// Source image is already of the desired size
		$iw = $image_width;
		$ih = $image_height;
		$t = 2;
	}
	if ($t == 1) {
		$img_src = imagecreatefromjpeg($sourcefile);
		$img_dst = imagecreatetruecolor($iw, $ih);
		imagecopyresampled($img_dst, $img_src, 0, 0, 0, 0, $iw, $ih, $image_width, $image_height);

		// Save image to file
		if(!imagejpeg($img_dst, $destfile, 50)) { // 50 is low quality, 90 is better
			exit();
		}

	} else if ($t == 2) {
		copy($sourcefile, $destfile);
	}
}

/**
 * upload_image Copies an image from POST to the server
*/
function upload_image($image, $dir){
	//debug("_FILES");
	global $config;
	if (!empty($_FILES["image"]["name"])) {
		$img_name = $_FILES['image']['name'];
		// Copy the file to the image folder
		copy($_FILES['image']['tmp_name'], $dir.$img_name);
		// Change permissions to avoid overwriting problems
		chmod($dir.$nombre_foto, 0777);

		// Return the name to insert in db
		return($nombre_foto);
	} else {
		//No image
		return false;
	}
}


/**
 * Return reversed multibyte string
 *
 * @author      Lucas Vieites <lucas@codexion.com>
 * @version     1.0
 * @param       char   $text        The string to revert
 */
function mb_strrev($text) {
	return join('', array_reverse(
		preg_split('~~u', $text, -1, PREG_SPLIT_NO_EMPTY)
	));
}

function get_random_string ($length = 8) {

	// start with a blank password
	$password = "";

	// define possible characters
	$possible = "0123456789bcdfghjkmnpqrstvwxyz";
	 
	// set up a counter
	$i = 0;
	 
	// add random characters to $password until $length is reached
	while ($i < $length) {
		// pick a random character from the possible ones
		$char = substr($possible, mt_rand(0, strlen($possible)-1), 1);
		 
		// we don't want this character if it's already in the password
		if (!strstr($password, $char)) {
			$password .= $char;
			$i++;
		}
	}
	// done!
	return $password;
}


/**
 * Return human readable sizes
 *
 * @author      Aidan Lister <aidan@php.net>
 * @version     1.1.0
 * @link        http://aidanlister.com/repos/v/function.size_readable.php
 * @param       int    $size        Size
 * @param       int    $unit        The maximum unit
 * @param       int    $retstring   The return string format
 * @param       int    $si          Whether to use SI prefixes
 */
function size_readable($size, $unit = null, $retstring = null, $si = true) {
    // Units
    if ($si === true) {
        $sizes = array('B', 'KB', 'MB', 'GB', 'TB', 'PB');
        $mod   = 1000;
    } else {
        $sizes = array('B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB');
        $mod   = 1024;
    }
    $ii = count($sizes) - 1;
 
    // Max unit
    $unit = array_search((string) $unit, $sizes);
    if ($unit === null || $unit === false) {
        $unit = $ii;
    }
 
    // Return string
    if ($retstring === null) {
        $retstring = '%01.2f %s';
    }
 
    // Loop
    $i = 0;
    while ($unit != $i && $size >= 1024 && $i < $ii) {
        $size /= $mod;
        $i++;
    }
 
    return sprintf($retstring, $size, $sizes[$i]);
}

/**
 * Return total size of the path
 */
function getDirectorySize($path) {
	$totalsize = 0;
	$totalcount = 0;
	$dircount = 0;
	if ($handle = opendir ($path)) {
		while (false !== ($file = readdir($handle))) {
			$nextpath = $path . '/' . $file;
			if ($file != '.' && $file != '..' && !is_link ($nextpath)) {
				if (is_dir ($nextpath)) {
					$dircount++;
					$result = getDirectorySize($nextpath);
					$totalsize += $result['size'];
					$totalcount += $result['count'];
					$dircount += $result['dircount'];
				} elseif (is_file ($nextpath)) {
					$totalsize += filesize ($nextpath);
					$totalcount++;
				}
			}
		}
	}
	closedir ($handle);
	$total['size'] = $totalsize;
	$total['count'] = $totalcount;
	$total['dircount'] = $dircount;
	return $total;
}

/*
	Paul's Simple Diff Algorithm v 0.1
	(C) Paul Butler 2007 <http://www.paulbutler.org/>
	May be used and distributed under the zlib/libpng license.
   
	This code is intended for learning purposes; it was written with short
	code taking priority over performance. It could be used in a practical
	application, but there are a few ways it could be optimized.
   
	Given two arrays, the function diff will return an array of the changes.
	I won't describe the format of the array, but it will be obvious
	if you use print_r() on the result of a diff on some test data.
   
	htmlDiff is a wrapper for the diff command, it takes two strings and
	returns the differences in HTML. The tags used are <ins> and <del>,
	which can easily be styled with CSS. 
*/

function diff($old, $new){
	foreach($old as $oindex => $ovalue){
		$nkeys = array_keys($new, $ovalue);
		foreach($nkeys as $nindex){
			$matrix[$oindex][$nindex] = isset($matrix[$oindex - 1][$nindex - 1]) ?
				$matrix[$oindex - 1][$nindex - 1] + 1 : 1;
			if($matrix[$oindex][$nindex] > $maxlen){
				$maxlen = $matrix[$oindex][$nindex];
				$omax = $oindex + 1 - $maxlen;
				$nmax = $nindex + 1 - $maxlen;
			}
		}       
	}
	if($maxlen == 0) return array(array('d'=>$old, 'i'=>$new));
	return array_merge(
		diff(array_slice($old, 0, $omax), array_slice($new, 0, $nmax)),
		array_slice($new, $nmax, $maxlen),
		diff(array_slice($old, $omax + $maxlen), array_slice($new, $nmax + $maxlen)));
}

function htmlDiff($old, $new){
	$diff = diff(explode(' ', $old), explode(' ', $new));
	foreach($diff as $k){
		if(is_array($k))
			$ret .= (!empty($k['d'])?"<del>".implode(' ',$k['d'])."</del> ":'').
				(!empty($k['i'])?"<ins>".implode(' ',$k['i'])."</ins> ":'');
		else $ret .= $k . ' ';
	}
	return $ret;
}

?>
