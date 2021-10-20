<?php

function banner(){
    @system("clear");
    $green="\033[92m";
    $white="\033[1;37m";
    print "$green\n";
    print "  __      __  _______    _        _  \n";
    print "  \ \    / / |__   __|  | |      | | \n";
    print "   \ \  / /_____| | ___ | |_ __ _| | \n";
    print "    \ \/ /______| |/ _ \| __/ _` | | \n";
    print "     \  /       | | (_) | || (_| | | \n";
    print "      \/        |_|\___/ \__\__,_|_| \n";
    print "$white\n";
    print "       Scan Your Whatever From Virus \n";
    print "\n";
    require_once 'Console/Table.php';
    $table = new Console_Table();
    $table->setHeaders(array('1) Check File Report', '4) Rescan from Resource'));
    $table->addRow(array('2) Scan Your File', '5) Check Url Report'));
    $table->addRow(array('3) Create Upload Url', '6) Scan Your Url'));
    $table->setBorderVisibility(
        array(
            'top'    => false,
            'right'  => false,
            'bottom' => false,
            'left'   => false,
            'inner'  => false,
        )
    );
    echo $table->getTable() . "\n\n";
    echo " Choose One : ";
    $menu = trim(fgets(STDIN));
    if ($menu == '1'){
        echo " API Key : ";
        $key = trim(fgets(STDIN));
        echo " Resource Code : ";
        $resource = trim(fgets(STDIN));
        filereport($key, $resource);
    }
    elseif ($menu == '2'){
        echo " API Key : ";
        $key = trim(fgets(STDIN));
        echo " File Path : ";
        $file = trim(fgets(STDIN));
        filescan($key, $file);
    }
    elseif ($menu == '3'){
        echo " API Key : ";
        $key = trim(fgets(STDIN));
        echo " File Path : ";
        $file = trim(fgets(STDIN));
        filescanuploadurl($key, $file);
    }
    elseif ($menu == '4'){
        echo " API Key : ";
        $key = trim(fgets(STDIN));
        echo " Resource Code : ";
        $resource = trim(fgets(STDIN));
        filerescan($key, $resource);
    }
    elseif ($menu == '5'){
        echo " API Key : ";
        $key = trim(fgets(STDIN));
        echo " Resource Code : ";
        $resource = trim(fgets(STDIN));
        urlreport($key, $resource);
    }
    elseif ($menu == '6'){
        echo " API Key : ";
        $key = trim(fgets(STDIN));
        echo " Url to Scan : ";
        $url = trim(fgets(STDIN));
        filescan($key, $url);
    }
}

function filereport($key, $resource){
    $post = array('apikey' => $key,'resource'=>$resource);
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, 'https://www.virustotal.com/vtapi/v2/file/report');
    curl_setopt($ch, CURLOPT_POST,1);
    //curl_setopt($ch, CURLOPT_VERBOSE, 1); // remove this if your not debugging
    curl_setopt($ch, CURLOPT_ENCODING, 'gzip,deflate'); // please compress data
    curl_setopt($ch, CURLOPT_USERAGENT, "gzip, My php curl client");
    curl_setopt($ch, CURLOPT_RETURNTRANSFER ,true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $post);
    $result=curl_exec ($ch);
    $status_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    if ($status_code == 200) { // OK
        $js = json_decode($result, true);
        $messages = $js['verbose_msg'];
        $resource = $js['resource'];
        $scan_id = $js['scan_id'];
        $md5 = $js['md5'];
        $sha1 = $js['sha1'];
        $sha256 = $js['sha256'];
        $scan_date = $js['scan_date'];
        $permalink = $js['permalink'];
        $positives = $js['positives'];
        $total = $js['total'];
        require_once 'Console/Table.php';
        $tbl = new Console_Table();
        $tbl->setHeaders(
            array('Type','Info')
        );
        foreach ($js['scans'] as $row){
            $detected = $row['detected'];
            $version = $row['version'];
            $result = $row['result'];
            $update = $row['update'];
            $tbl->addRow(array('Detect', $detected));
            $tbl->addRow(array('Version', $version));
            $tbl->addRow(array('Result', $result));
            $tbl->addRow(array('Update', $update));
            $tbl->addRow(array(' ', ' '));
            echo $tbl->getTable();
        }
    } else {  // Error occured
        print($result);
    }
    curl_close ($ch);
}

function filescan($key, $file){
    $file_name_with_full_path = realpath($file);
    $api_key = getenv('VT_API_KEY') ? getenv('VT_API_KEY') :$key;
    $cfile = curl_file_create($file_name_with_full_path);
    $post = array('apikey' => $api_key,'file'=> $cfile);
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, 'https://www.virustotal.com/vtapi/v2/file/scan');
    curl_setopt($ch, CURLOPT_POST, True);
    //curl_setopt($ch, CURLOPT_VERBOSE, 1); // remove this if your not debugging
    curl_setopt($ch, CURLOPT_ENCODING, 'gzip,deflate'); // please compress data
    curl_setopt($ch, CURLOPT_USERAGENT, "gzip, My php curl client");
    curl_setopt($ch, CURLOPT_RETURNTRANSFER ,True);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $post);
    $result=curl_exec ($ch);
    $status_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    if ($status_code == 200) { // OK
        $js = json_decode($result, true);
        $permalink = $js['permalink'];
        $resource = $js['resource'];
        $scan_id = $js['scan_id'];
        $messages = $js['verbose_msg'];
        $sha256 = $js['sha256'];
        filereport($key, $resource);
    } else {  // Error occured
        print($result);
    }
    curl_close ($ch);
}

function filescanuploadurl($key, $file){
    $api_key = getenv('VT_API_KEY') ? getenv('VT_API_KEY') :$key;
    $data = array('apikey' => $api_key);
    $ch = curl_init();
    $url = 'https://www.virustotal.com/vtapi/v2/file/scan/upload_url?';
    $url .= http_build_query($data); // append query params
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, True); // API will redirect
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_VERBOSE, 1); // remove this if your not debugging
    curl_setopt($ch, CURLOPT_ENCODING, 'gzip,deflate'); // please compress data
    curl_setopt($ch, CURLOPT_USERAGENT, "gzip, My php curl client");
    curl_setopt($ch, CURLOPT_RETURNTRANSFER ,True);
    $result=curl_exec ($ch);
    $status_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    if ($status_code == 200) { // OK
        $js = json_decode($result, true);
        $upload_url=$js['upload_url'];
    } else {  // Error occured
        print($result);
        return -1;
    }
    echo "upload_url:  $upload_url";
    $file_name_with_full_path = realpath($file);
    $cfile = curl_file_create($file_name_with_full_path);
    $post = array('file'=> $cfile);
    curl_setopt($ch, CURLOPT_URL, $upload_url);
    curl_setopt($ch, CURLOPT_POST, True);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $post); // set file
    $result=curl_exec ($ch);
    $status_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    if ($status_code == 200) { // OK
        $js = json_decode($result, true);
        print_r($js);
    } else {  // Error occured
        print($result);
    }
    curl_close ($ch);
}

function filerescan($key, $resource){
    $api_key = getenv('VT_API_KEY') ? getenv('VT_API_KEY') :$key;
    $post = array('apikey' => $api_key,'resource'=> $resource);
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, 'https://www.virustotal.com/vtapi/v2/file/rescan');
    curl_setopt($ch, CURLOPT_POST, True);
    //curl_setopt($ch, CURLOPT_VERBOSE, 1); // remove this if your not debugging
    curl_setopt($ch, CURLOPT_ENCODING, 'gzip,deflate'); // please compress data
    curl_setopt($ch, CURLOPT_USERAGENT, "gzip, My php curl client");
    curl_setopt($ch, CURLOPT_RETURNTRANSFER ,True);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $post);
    $result=curl_exec ($ch);
    $status_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    if ($status_code == 200) { // OK
        $js = json_decode($result, true);
        $permalink = $js['permalink'];
        $resource = $js['resource'];
        $scan_id = $js['scan_id'];
        $sha256 = $js['sha256'];
        filereport($key, $resource);
    } else {  // Error occured
        print($result);
    }
    curl_close ($ch);
}

function urlreport($key, $resource){
    $post = array('apikey' => $key,'resource'=>$resource);
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, 'https://www.virustotal.com/vtapi/v2/url/report');
    curl_setopt($ch, CURLOPT_POST,1);
    //curl_setopt($ch, CURLOPT_VERBOSE, 1); // remove this if your not debugging
    curl_setopt($ch, CURLOPT_ENCODING, 'gzip,deflate'); // please compress data
    curl_setopt($ch, CURLOPT_USERAGENT, "gzip, My php curl client");
    curl_setopt($ch, CURLOPT_RETURNTRANSFER ,true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $post);
    $result=curl_exec ($ch);
    $status_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    if ($status_code == 200) { // OK
        $js = json_decode($result, true);
        $messages = $js['verbose_msg'];
        $resource = $js['resource'];
        $scan_id = $js['scan_id'];
        $filescan_id = $js['filescan_id'];
        $scan_date = $js['scan_date'];
        $permalink = $js['permalink'];
        $positives = $js['positives'];
        $total = $js['total'];
        require_once 'Console/Table.php';
        $tbl = new Console_Table();
        $tbl->setHeaders(
            array('Type','Info')
        );
        foreach ($js['scans'] as $row){
            $detected = $row['detected'];
            $result = $row['result'];
            $tbl->addRow(array('Detect', $detected));
            $tbl->addRow(array('Result', $result));
            $tbl->addRow(array(' ', ' '));
            echo $tbl->getTable();
        }
    } else {  // Error occured
        print($result);
    }
    curl_close ($ch);
}

function urlscan($key, $url){
    $api_key = getenv('VT_API_KEY') ? getenv('VT_API_KEY') :$key;
    $post = array('apikey' => $api_key,'url'=> $url);
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, 'https://www.virustotal.com/vtapi/v2/url/scan');
    curl_setopt($ch, CURLOPT_POST, True);
    //curl_setopt($ch, CURLOPT_VERBOSE, 1); // remove this if your not debugging
    curl_setopt($ch, CURLOPT_ENCODING, 'gzip,deflate'); // please compress data
    curl_setopt($ch, CURLOPT_USERAGENT, "gzip, My php curl client");
    curl_setopt($ch, CURLOPT_RETURNTRANSFER ,True);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $post);
    $result=curl_exec ($ch);
    $status_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    if ($status_code == 200) { // OK
        $js = json_decode($result, true);
        $permalink = $js['permalink'];
        $resource = $js['resource'];
        $scan_id = $js['scan_id'];
        $messages = $js['verbose_msg'];
        $scan_date = $js['scan_date'];
        urlreport($key, $resource);
    } else {  // Error occured
        print($result);
    }
    curl_close ($ch);
}

banner();

?>