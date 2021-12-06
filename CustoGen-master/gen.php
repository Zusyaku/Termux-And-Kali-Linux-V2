<?php

// Color
$blue="\033[1;34m";
$cyan="\033[1;36m";
$okegreen="\033[92m";
$lightgreen="\033[1;32m";
$white="\033[1;37m";
$purple="\033[1;35m";
$red="\033[1;31m";
$yellow="\033[1;33m";

echo "$cyan Want to Input Base(y/n)?$red >$white ";
$menu = trim(fgets(STDIN));
if ($menu == 'y' OR $menu == 'Y'){
    echo "$cyan Base$red >$white ";
    $base = trim(fgets(STDIN));
    echo "$cyan Jumlah Digit Kode$red >$white ";
    $total = trim(fgets(STDIN));
    echo "$cyan UPPER/lower (U/l)?$red >$white ";
    $case = trim(fgets(STDIN));
    echo "$cyan Total Kode$red >$white ";
    $jumlah = trim(fgets(STDIN));
    if ($case == 'U' OR $case == 'u'){
        function random($panjang)
        {
            $karakter = '';
            $karakter .= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'; // karakter alfabet
            $karakter .= '1234567890'; // karakter numerik
            $string = '';
            for ($i=0; $i < $panjang; $i++) { 
                $pos = rand(0, strlen($karakter)-1);
                $string .= $karakter{$pos};
            }
            return $string;
        }
        for ($i=0; $i < $jumlah; $i++){
            echo " ".$base.random($total-strlen($base));
            echo "\n";
        }
    }
    elseif ($case == 'l' OR $case == 'L'){
        function random($panjang)
        {
            $karakter = '';
            $karakter .= 'abcdefghijklmnopqrstuvwxyz'; // karakter alfabet
            $karakter .= '1234567890'; // karakter numerik
            $string = '';
            for ($i=0; $i < $panjang; $i++) { 
                $pos = rand(0, strlen($karakter)-1);
                $string .= $karakter{$pos};
            }
            return $string;
        }
        for ($i=0; $i < $jumlah; $i++){
            echo " ".$base.random($total-strlen($base));
            echo "\n";
        }
    }
}
elseif ($menu == 'n' OR $menu == 'N'){
    echo "$cyan Jumlah Digit Kode$red >$white ";
    $total = trim(fgets(STDIN));
    echo "$cyan UPPER/lower (U/l)?$red >$white ";
    $case = trim(fgets(STDIN));
    echo "$cyan Total Kode$red >$white ";
    $jumlah = trim(fgets(STDIN));
    if ($case == 'U' OR $case == 'u'){
        function random($panjang)
        {
            $karakter = '';
            $karakter .= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'; // karakter alfabet
            $karakter .= '1234567890'; // karakter numerik
            $string = '';
            for ($i=0; $i < $panjang; $i++) { 
                $pos = rand(0, strlen($karakter)-1);
                $string .= $karakter{$pos};
            }
            return $string;
        }
        for ($i=0; $i < $jumlah; $i++){
            echo " ".random($total);
            echo "\n";
        }
    }
    elseif ($case == 'l' OR $case == 'L'){
        function random($panjang)
        {
            $karakter = '';
            $karakter .= 'abcdefghijklmnopqrstuvwxyz'; // karakter alfabet
            $karakter .= '1234567890'; // karakter numerik
            $string = '';
            for ($i=0; $i < $panjang; $i++) { 
                $pos = rand(0, strlen($karakter)-1);
                $string .= $karakter{$pos};
            }
            return $string;
        }
        for ($i=0; $i < $jumlah; $i++){
            echo " ".random($total);
            echo "\n";
        }
    }
}

?>
