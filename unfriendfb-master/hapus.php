<?php set_time_limit(0);

class Console {
 
    static $foreground_colors = array(
        'bold'         => '1',    'dim'          => '2',
        'black'        => '0;30', 'dark_gray'    => '1;30',
        'blue'         => '0;34', 'light_blue'   => '1;34',
        'green'        => '0;32', 'light_green'  => '1;32',
        'cyan'         => '0;36', 'light_cyan'   => '1;36',
        'red'          => '0;31', 'light_red'    => '1;31',
        'purple'       => '0;35', 'light_purple' => '1;35',
        'brown'        => '0;33', 'yellow'       => '1;33',
        'light_gray'   => '0;37', 'white'        => '1;37',
        'normal'       => '0;39',
    );
    
    static $background_colors = array(
        'black'        => '40',   'red'          => '41',
        'green'        => '42',   'yellow'       => '43',
        'blue'         => '44',   'magenta'      => '45',
        'cyan'         => '46',   'light_gray'   => '47',
    );
 
    static $options = array(
        'underline'    => '4',    'blink'         => '5', 
        'reverse'      => '7',    'hidden'        => '8',
    );
    static $EOF = "\n";

public static function log($str = '', $color = 'normal', $newline = true, $background_color = null)
    {
        if( is_bool($color) )
        {
            $newline = $color;
            $color   = 'normal';
        }
        elseif( is_string($color) && is_string($newline) )
        {
            $background_color = $newline;
            $newline          = true;
        }
        $str = $newline ? $str . self::$EOF : $str;
        echo self::$color($str, $background_color);
    }


public static function __callStatic($foreground_color, $args)
    {
        $string         = $args[0];
        $colored_string = "";
 
        // Check if given foreground color found
        if( isset(self::$foreground_colors[$foreground_color]) ) {
            $colored_string .= "\033[" . self::$foreground_colors[$foreground_color] . "m";
        }
        else{
            die( $foreground_color . ' not a valid color');
        }
        
        array_shift($args);
        foreach( $args as $option ){
            // Check if given background color found
            if(isset(self::$background_colors[$option])) {
                $colored_string .= "\033[" . self::$background_colors[$option] . "m";
            }
            elseif(isset(self::$options[$option])) {
                $colored_string .= "\033[" . self::$options[$option] . "m";
            }
        }
        
        // Add string and end coloring
        $colored_string .= $string . "\033[0m";
        
        return $colored_string;
        
    }
 

public static function bell($count = 1) {
        echo str_repeat("\007", $count);
    }
 
}


function friendlist($token){
	$a = json_decode(file_get_contents('https://graph.facebook.com/me/friends?access_token='.$token), true);
	return $a['data'];
}
function last_active($id, $tok){
	$a = json_decode(file_get_contents('https://graph.facebook.com/'.$id.'/feed?access_token='.$tok.'&limit=1'), true);
	$date = $a['data'][0]['created_time'];
	$aa = strtotime($date);
	return date('Y', $aa);
}
function unfriend($id, $token){
	$url = 'https://graph.facebook.com/me/friends?uid='.$id.'&access_token='.$token;
	$ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "DELETE");
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    $result = curl_exec($ch);
    curl_close($ch);
	if($result == true){
		$unf = ('[BATAL BERTEMAN]');
	} else {
		$unf = ('[GAGAL BATAL BERTEMAN]');
	}
	return $unf;
}
echo console :: blue("[===========================================]\n");
echo console :: green("[         FACEBOOK All UNFRIEND        ]\n");
echo console :: cyan("[ Author  : Kumpulan Remaja                   ]\n");
echo console :: red("[ Website : https://kumpulanremaja.com       ]\n");
echo console :: yellow("[ Github  : https://github.com/kumpulanremaja ]\n");
echo console :: light_purple("[ <?php set_time_limit(0);

class Console {
 
    static $foreground_colors = array(
        'bold'         => '1',    'dim'          => '2',
        'black'        => '0;30', 'dark_gray'    => '1;30',
        'blue'         => '0;34', 'light_blue'   => '1;34',
        'green'        => '0;32', 'light_green'  => '1;32',
        'cyan'         => '0;36', 'light_cyan'   => '1;36',
        'red'          => '0;31', 'light_red'    => '1;31',
        'purple'       => '0;35', 'light_purple' => '1;35',
        'brown'        => '0;33', 'yellow'       => '1;33',
        'light_gray'   => '0;37', 'white'        => '1;37',
        'normal'       => '0;39',
    );
    
    static $background_colors = array(
        'black'        => '40',   'red'          => '41',
        'green'        => '42',   'yellow'       => '43',
        'blue'         => '44',   'magenta'      => '45',
        'cyan'         => '46',   'light_gray'   => '47',
    );
 
    static $options = array(
        'underline'    => '4',    'blink'         => '5', 
        'reverse'      => '7',    'hidden'        => '8',
    );
    static $EOF = "\n";

public static function log($str = '', $color = 'normal', $newline = true, $background_color = null)
    {
        if( is_bool($color) )
        {
            $newline = $color;
            $color   = 'normal';
        }
        elseif( is_string($color) && is_string($newline) )
        {
            $background_color = $newline;
            $newline          = true;
        }
        $str = $newline ? $str . self::$EOF : $str;
        echo self::$color($str, $background_color);
    }


public static function __callStatic($foreground_color, $args)
    {
        $string         = $args[0];
        $colored_string = "";
 
        // Check if given foreground color found
        if( isset(self::$foreground_colors[$foreground_color]) ) {
            $colored_string .= "\033[" . self::$foreground_colors[$foreground_color] . "m";
        }
        else{
            die( $foreground_color . ' not a valid color');
        }
        
        array_shift($args);
        foreach( $args as $option ){
            // Check if given background color found
            if(isset(self::$background_colors[$option])) {
                $colored_string .= "\033[" . self::$background_colors[$option] . "m";
            }
            elseif(isset(self::$options[$option])) {
                $colored_string .= "\033[" . self::$options[$option] . "m";
            }
        }
        
        // Add string and end coloring
        $colored_string .= $string . "\033[0m";
        
        return $colored_string;
        
    }
 

public static function bell($count = 1) {
        echo str_repeat("\007", $count);
    }
 
}


function friendlist($token){
	$a = json_decode(file_get_contents('https://graph.facebook.com/me/friends?access_token='.$token), true);
	return $a['data'];
}
function last_active($id, $tok){
	$a = json_decode(file_get_contents('https://graph.facebook.com/'.$id.'/feed?access_token='.$tok.'&limit=1'), true);
	$date = $a['data'][0]['created_time'];
	$aa = strtotime($date);
	return date('Y', $aa);
}
function unfriend($id, $token){
	$url = 'https://graph.facebook.com/me/friends?uid='.$id.'&access_token='.$token;
	$ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "DELETE");
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    $result = curl_exec($ch);
    curl_close($ch);
	if($result == true){
		$unf = ('[BATAL BERTEMAN]');
	} else {
		$unf = ('[GAGAL BATAL BERTEMAN]');
	}
	return $unf;
}
echo console :: blue("[===========================================]\n");
echo console :: green("[         ~FACEBOOK UNFRIEND       ]\n");
echo console :: cyan("[ Author  : Kumpulan Remaja                   ]\n");
echo console :: red("[ Team    : KumpulanRemaja        ]\n");
echo console :: yellow("[ Github  : https://github.com/kumpulanremaja ]\n");
echo console :: light_purple("[ Website : https://kumpulanremaja.com ]\n");
echo console :: green("[         ~FACEBOOK : https://www.facebook.com/4kumpulanremaja    ]\n");
echo console :: blue("[===========================================]\n\n");

echo console :: cyan("Masukan Token Akun Facebook anda : ");
$fbtoken = trim(fgets(STDIN));
echo "\n[?]Masukan Tahun Terakhir Aktif, Yang Mau Di Hapus teman nya\n";
echo console :: cyan("Masukan Tahun : ");
$year = trim(fgets(STDIN));
echo "\n";
$FL = friendlist($fbtoken);
foreach($FL as $list){
	$name = $list['name'];
	$id = $list['id'];
	$date = last_active($id, $fbtoken);
	if($date < $year){
		echo console :: red('[TIDAK AKTIF]').' '.$name.' ~ '.$date.' '.unfriend($id, $fbtoken);
		echo "\r\n";
	}else{
		echo console :: green('[AKTIF]').' '.$name.' ~ '.$date;
		echo "\r\n";
	}
} ?>]\n");
echo console :: blue("[===========================================]\n\n");

echo console :: cyan("Masukan Token Akun Fb Kalian : ");
$fbtoken = trim(fgets(STDIN));
echo "\n[?]Masukan Tahun Terakhir Aktif Yang Mau Di Hapus\n";
echo console :: cyan("Masukan Tahun : ");
$year = trim(fgets(STDIN));
echo "\n";
$FL = friendlist($fbtoken);
foreach($FL as $list){
	$name = $list['name'];
	$id = $list['id'];
	$date = last_active($id, $fbtoken);
	if($date < $year){
		echo console :: red('[TIDAK AKTIF]').' '.$name.' ~ '.$date.' '.unfriend($id, $fbtoken);
		echo "\r\n";
	}else{
		echo console :: green('[AKTIF]').' '.$name.' ~ '.$date;
		echo "\r\n";
	}
} ?>
