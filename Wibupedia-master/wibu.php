<?php

function index(){
    include 'config.php';
    @system("clear");
    print "\n";
    print "$red __          ___ _          $white                _ _       \n";
    print "$red \ \        / (_) |         $white               | (_)      \n";
    print "$red  \ \  /\  / / _| |__  _   _$white _ __   ___  __| |_  __ _ \n";
    print "$red   \ \/  \/ / | | '_ \| | | $white| '_ \ / _ \/ _` | |/ _` |\n";
    print "$red    \  /\  /  | | |_) | |_| $white| |_) |  __/ (_| | | (_| |\n";
    print "$red     \/  \/   |_|_.__/ \__,_$white| .__/ \___|\__,_|_|\__,_|\n";
    print "$red                            $white| |                       \n";
    print "$red                            $white|_|                       \n";
    print "\n";
}

function menu(){
    include 'config.php';
    print "\n";
    print "$cyan 01$red :$white Search Anime\n";
    print "$cyan 02$red :$white Search Manga\n";
    print "$cyan 03$red :$white Anime Info\n";
    print "$cyan 04$red :$white Manga Info\n";
    print "$cyan 05$red :$white Anime Schedule\n";
    print "$cyan 06$red :$white Top Anime\n";
    print "$cyan 07$red :$white Top Manga\n";
    print "$cyan 08$red :$white Top Character\n";
    print "$cyan 09$red :$white Search Anime by Genre\n";
    print "$cyan 10$red :$white Search Manga by Genre\n";
    print "\n";
}

function animeinfo(){
    include 'config.php';
    print "\n";
    print "$cyan 01$red :$white Characters\n";
    print "$cyan 02$red :$white Episodes\n";
    print "$cyan 03$red :$white Related News\n";
    print "$cyan 04$red :$white Related Pictures\n";
    print "$cyan 05$red :$white Promotional Videos & Episodes\n";
    print "$cyan 06$red :$white Statistic\n";
    print "$cyan 07$red :$white Forum Topics\n";
    print "$cyan 08$red :$white Reviews\n";
    print "$cyan 09$red :$white Recommendation\n";
    print "$cyan 10$red :$white User Update\n";
    print "$cyan 11$red :$white More Information\n";
    print "\n";
    print "$red >$white ";
    $cmd = trim(fgets(STDIN));
    if ($cmd == '1'){
        charanimeinfo();
    }
    elseif ($cmd == '2'){
        episodeanimeinfo();
    }
    elseif ($cmd == '3'){
        newsanimeinfo();
    }
    elseif ($cmd == '4'){
        pictanimeinfo();
    }
    elseif ($cmd == '5'){
        videoanimeinfo();
    }
    elseif ($cmd == '6'){
        statanimeinfo();
    }
    elseif ($cmd == '7'){
        forumanimeinfo();
    }
    elseif ($cmd == '8'){
        reviewanimeinfo();
    }
    elseif ($cmd == '9'){
        recommendanimeinfo();
    }
    elseif ($cmd == '10'){
        updateanimeinfo();
    }
    elseif ($cmd == '11'){
        moreanimeinfo();
    }
}

function mangainfo(){
    include 'config.php';
    print "\n";
    print "$cyan 01$red :$white Characters\n";
    print "$cyan 02$red :$white Related News\n";
    print "$cyan 03$red :$white Related Pictures\n";
    print "$cyan 04$red :$white Statistic\n";
    print "$cyan 05$red :$white Forum Topics\n";
    print "$cyan 06$red :$white Reviews\n";
    print "$cyan 07$red :$white Recommendation\n";
    print "$cyan 08$red :$white User Update\n";
    print "$cyan 09$red :$white More Information\n";
    print "\n";
    print "$red >$white ";
    $cmd = trim(fgets(STDIN));
    if ($cmd == '1'){
        charmangainfo();
    }
    elseif ($cmd == '2'){
        newsmangainfo();
    }
    elseif ($cmd == '3'){
        pictmangainfo();
    }
    elseif ($cmd == '4'){
        statmangainfo();
    }
    elseif ($cmd == '5'){
        forummangainfo();
    }
    elseif ($cmd == '6'){
        reviewmangainfo();
    }
    elseif ($cmd == '7'){
        recommendmangainfo();
    }
    elseif ($cmd == '8'){
        updatemangainfo();
    }
    elseif ($cmd == '9'){
        moremangainfo();
    }
}

function charanimeinfo(){
    include 'config.php';
    print "$cyan ID$red >$white ";
    $id = trim(fgets(STDIN));
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_URL,'https://api.jikan.moe/v3/anime/'.$id.'/characters_staff');
    $result=curl_exec($ch);
    $json = json_decode($result, true);
    foreach ($json['characters'] as $row){
        $name = $row['name'];
        $id = $row['mal_id'];
        print "$cyan [$white $id$cyan ]$red >$white $name\n";
    }
}

function episodeanimeinfo(){
    include 'config.php';
    print "$cyan ID$red >$white ";
    $id = trim(fgets(STDIN));
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_URL,'https://api.jikan.moe/v3/anime/'.$id.'/episodes');
    $result=curl_exec($ch);
    $json = json_decode($result, true);
    foreach ($json['episodes'] as $row){
        $title = $row['title_romanji'];
        $id = $row['episode_id'];
        print "$cyan [$white $id$cyan ]$red >$white $title\n";
    }
}

function newsanimeinfo(){
    include 'config.php';
    print "$cyan ID$red >$white ";
    $id = trim(fgets(STDIN));
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_URL,'https://api.jikan.moe/v3/anime/'.$id.'/news');
    $result=curl_exec($ch);
    $json = json_decode($result, true);
    foreach ($json['articles'] as $row){
        $title = $row['title'];
        $url = $row['url'];
        print "$cyan [$white $url$cyan ]$red >$white $title\n";
    }
}

function pictanimeinfo(){
    include 'config.php';
    print "$cyan ID$red >$white ";
    $id = trim(fgets(STDIN));
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_URL,'https://api.jikan.moe/v3/anime/'.$id.'/pictures');
    $result=curl_exec($ch);
    $json = json_decode($result, true);
    foreach ($json['pictures'] as $row){
        $pict = $row['large'];
        print "$cyan [$white *$cyan ]$red >$white $pict\n";
    }
}

function videoanimeinfo(){
    include 'config.php';
    print "$cyan ID$red >$white ";
    $id = trim(fgets(STDIN));
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_URL,'https://api.jikan.moe/v3/anime/'.$id.'/videos');
    $result=curl_exec($ch);
    $json = json_decode($result, true);
    foreach ($json['promo'] as $row){
        $title = $row['title'];
        $video = $row['video_url'];
        print "$cyan [$white $video$cyan ]$red >$white $title\n";
    }
}

function statanimeinfo(){
    include 'config.php';
    print "$cyan ID$red >$white ";
    $id = trim(fgets(STDIN));
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_URL,'https://api.jikan.moe/v3/anime/'.$id.'/stats');
    $result=curl_exec($ch);
    $json = json_decode($result, true);
    print "$cyan [$white Watch$cyan ]$red >$white ".$json['watching']."\n";
    print "$cyan [$white Completed$cyan ]$red >$white ".$json['completed']."\n";
    print "$cyan [$white On Hold$cyan ]$red >$white ".$json['on_hold']."\n";
    print "$cyan [$white Dropped$cyan ]$red >$white ".$json['dropped']."\n";
    print "$cyan [$white Plan$cyan ]$red >$white ".$json['plan_to_watch']."\n";
    print "$cyan [$white Total$cyan ]$red >$white ".$json['total']."\n";
}

function forumanimeinfo(){
    include 'config.php';
    print "$cyan ID$red >$white ";
    $id = trim(fgets(STDIN));
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_URL,'https://api.jikan.moe/v3/anime/'.$id.'/forum');
    $result=curl_exec($ch);
    $json = json_decode($result, true);
    foreach ($json['topics'] as $row){
        $title = $row['title'];
        $id = $row['topic_id'];
        print "$cyan [$white $id$cyan ]$red >$white $title\n";
    }
}

function reviewanimeinfo(){
    include 'config.php';
    print "$cyan ID$red >$white ";
    $id = trim(fgets(STDIN));
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_URL,'https://api.jikan.moe/v3/anime/'.$id.'/reviews');
    $result=curl_exec($ch);
    $json = json_decode($result, true);
    foreach ($json['reviews'] as $row){
        $content = $row['content'];
        $id = $row['mal_id'];
        print "$cyan [$white $id$cyan ]$red >$white $content\n\n";
    }
}

function recommendanimeinfo(){
    include 'config.php';
    print "$cyan ID$red >$white ";
    $id = trim(fgets(STDIN));
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_URL,'https://api.jikan.moe/v3/anime/'.$id.'/recommendations');
    $result=curl_exec($ch);
    $json = json_decode($result, true);
    foreach ($json['recommendations'] as $row){
        $title = $row['title'];
        $id = $row['mal_id'];
        print "$cyan [$white $id$cyan ]$red >$white $title\n";
    }
}

function updateanimeinfo(){
    include 'config.php';
    print "$cyan ID$red >$white ";
    $id = trim(fgets(STDIN));
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_URL,'https://api.jikan.moe/v3/anime/'.$id.'/userupdates');
    $result=curl_exec($ch);
    $json = json_decode($result, true);
    foreach ($json['users'] as $row){
        $user = $row['username'];
        $status = $row['status'];
        print "$cyan [$white $status$cyan ]$red >$white $user\n";
    }
}

function moreanimeinfo(){
    include 'config.php';
    print "$cyan ID$red >$white ";
    $id = trim(fgets(STDIN));
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_URL,'https://api.jikan.moe/v3/anime/'.$id.'/moreinfo');
    $result=curl_exec($ch);
    $json = json_decode($result, true);
    print "$cyan [$white Info$cyan ]$red >$white ".$json['moreinfo']."\n";
}

function charmangainfo(){
    include 'config.php';
    print "$cyan ID$red >$white ";
    $id = trim(fgets(STDIN));
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_URL,'https://api.jikan.moe/v3/manga/'.$id.'/characters');
    $result=curl_exec($ch);
    $json = json_decode($result, true);
    foreach ($json['characters'] as $row){
        $name = $row['name'];
        $id = $row['mal_id'];
        print "$cyan [$white $id$cyan ]$red >$white $name\n";
    }
}

function newsmangainfo(){
    include 'config.php';
    print "$cyan ID$red >$white ";
    $id = trim(fgets(STDIN));
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_URL,'https://api.jikan.moe/v3/manga/'.$id.'/news');
    $result=curl_exec($ch);
    $json = json_decode($result, true);
    foreach ($json['articles'] as $row){
        $title = $row['title'];
        $url = $row['url'];
        print "$cyan [$white $url$cyan ]$red >$white $title\n";
    }
}

function pictmangainfo(){
    include 'config.php';
    print "$cyan ID$red >$white ";
    $id = trim(fgets(STDIN));
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_URL,'https://api.jikan.moe/v3/manga/'.$id.'/pictures');
    $result=curl_exec($ch);
    $json = json_decode($result, true);
    foreach ($json['pictures'] as $row){
        $pict = $row['large'];
        print "$cyan [$white *$cyan ]$red >$white $pict\n";
    }
}

function statmangainfo(){
    include 'config.php';
    print "$cyan ID$red >$white ";
    $id = trim(fgets(STDIN));
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_URL,'https://api.jikan.moe/v3/manga/'.$id.'/stats');
    $result=curl_exec($ch);
    $json = json_decode($result, true);
    print "$cyan [$white Read$cyan ]$red >$white ".$json['reading']."\n";
    print "$cyan [$white Completed$cyan ]$red >$white ".$json['completed']."\n";
    print "$cyan [$white On Hold$cyan ]$red >$white ".$json['on_hold']."\n";
    print "$cyan [$white Dropped$cyan ]$red >$white ".$json['dropped']."\n";
    print "$cyan [$white Plan$cyan ]$red >$white ".$json['plan_to_read']."\n";
    print "$cyan [$white Total$cyan ]$red >$white ".$json['total']."\n";
}

function forummangainfo(){
    include 'config.php';
    print "$cyan ID$red >$white ";
    $id = trim(fgets(STDIN));
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_URL,'https://api.jikan.moe/v3/manga/'.$id.'/forum');
    $result=curl_exec($ch);
    $json = json_decode($result, true);
    foreach ($json['topics'] as $row){
        $title = $row['title'];
        $id = $row['topic_id'];
        print "$cyan [$white $id$cyan ]$red >$white $title\n";
    }
}

function reviewmangainfo(){
    include 'config.php';
    print "$cyan ID$red >$white ";
    $id = trim(fgets(STDIN));
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_URL,'https://api.jikan.moe/v3/manga/'.$id.'/reviews');
    $result=curl_exec($ch);
    $json = json_decode($result, true);
    foreach ($json['reviews'] as $row){
        $content = $row['content'];
        $id = $row['mal_id'];
        print "$cyan [$white $id$cyan ]$red >$white $content\n\n";
    }
}

function recommendmangainfo(){
    include 'config.php';
    print "$cyan ID$red >$white ";
    $id = trim(fgets(STDIN));
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_URL,'https://api.jikan.moe/v3/manga/'.$id.'/recommendations');
    $result=curl_exec($ch);
    $json = json_decode($result, true);
    foreach ($json['recommendations'] as $row){
        $title = $row['title'];
        $id = $row['mal_id'];
        print "$cyan [$white $id$cyan ]$red >$white $title\n";
    }
}

function updatemangainfo(){
    include 'config.php';
    print "$cyan ID$red >$white ";
    $id = trim(fgets(STDIN));
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_URL,'https://api.jikan.moe/v3/manga/'.$id.'/userupdates');
    $result=curl_exec($ch);
    $json = json_decode($result, true);
    foreach ($json['users'] as $row){
        $user = $row['username'];
        $status = $row['status'];
        print "$cyan [$white $status$cyan ]$red >$white $user\n";
    }
}

function moremangainfo(){
    include 'config.php';
    print "$cyan ID$red >$white ";
    $id = trim(fgets(STDIN));
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_URL,'https://api.jikan.moe/v3/manga/'.$id.'/moreinfo');
    $result=curl_exec($ch);
    $json = json_decode($result, true);
    print "$cyan [$white Info$cyan ]$red >$white ".$json['moreinfo']."\n";
}

function animeschedule(){
    include 'config.php';
    print "\n";
    print "$cyan 01$red :$white Monday\n";
    print "$cyan 02$red :$white Tuesday\n";
    print "$cyan 03$red :$white Wednesday\n";
    print "$cyan 04$red :$white Thursday\n";
    print "$cyan 05$red :$white Friday\n";
    print "$cyan 06$red :$white Saturday\n";
    print "$cyan 07$red :$white Sunday\n";
    print "$cyan 08$red :$white Other\n";
    print "\n";
    print "$red >$white ";
    $day = trim(fgets(STDIN));
    if ($day == '1'){
        $day = 'monday';
    }
    elseif ($day == '2'){
        $day = 'tuesday';
    }
    elseif ($day == '3'){
        $day = 'wednesday';
    }
    elseif ($day == '4'){
        $day = 'thursday';
    }
    elseif ($day == '5'){
        $day = 'friday';
    }
    elseif ($day == '6'){
        $day = 'saturday';
    }
    elseif ($day == '7'){
        $day = 'sunday';
    }
    elseif ($day == '8'){
        $day = 'other';
    }
    elseif ($day == ''){
        $day = 'unknown';
    }
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_URL,'https://api.jikan.moe/v3/schedule/'.$day);
    $result=curl_exec($ch);
    $json = json_decode($result, true);
    foreach ($json["$day"] as $row){
        $title = $row['title'];
        $id = $row['mal_id'];
        print "$cyan [$white $id$cyan ]$red >$white $title\n";
    }
}

function animetop(){
    include 'config.php';
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_URL,'https://api.jikan.moe/v3/top/anime');
    $result=curl_exec($ch);
    $json = json_decode($result, true);
    foreach ($json['top'] as $row){
        $title = $row['title'];
        $id = $row['mal_id'];
        print "$cyan [$white $id$cyan ]$red >$white $title\n";
    }
}

function mangatop(){
    include 'config.php';
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_URL,'https://api.jikan.moe/v3/top/manga');
    $result=curl_exec($ch);
    $json = json_decode($result, true);
    foreach ($json['top'] as $row){
        $title = $row['title'];
        $id = $row['mal_id'];
        print "$cyan [$white $id$cyan ]$red >$white $title\n";
    }
}

function chartop(){
    include 'config.php';
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_URL,'https://api.jikan.moe/v3/top/characters');
    $result=curl_exec($ch);
    $json = json_decode($result, true);
    foreach ($json['top'] as $row){
        $name = $row['title'];
        $id = $row['mal_id'];
        print "$cyan [$white $id$cyan ]$red >$white $name\n";
    }
}

function animesearch(){
    include 'config.php';
    print "$cyan Judul$red >$white ";
    $title = trim(fgets(STDIN));
    $title = str_replace(" ", "%20", $title);
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_URL,'https://api.jikan.moe/v3/search/anime?q='.$title);
    $result=curl_exec($ch);
    $json = json_decode($result, true);
    foreach ($json['results'] as $row){
        $title = $row['title'];
        $id = $row['mal_id'];
        print "$cyan [$white $id$cyan ]$red >$white $title\n";
    }
}

function mangasearch(){
    include 'config.php';
    print "$cyan Judul$red >$white ";
    $title = trim(fgets(STDIN));
    $title = str_replace(" ", "%20", $title);
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_URL,'https://api.jikan.moe/v3/search/manga?q='.$title);
    $result=curl_exec($ch);
    $json = json_decode($result, true);
    foreach ($json['results'] as $row){
        $title = $row['title'];
        $id = $row['mal_id'];
        print "$cyan [$white $id$cyan ]$red >$white $title\n";
    }
}

function animegenre(){
    include 'config.php';
    print "\n";
    print "$cyan 01$red :$white Action\n";
    print "$cyan 02$red :$white Adventure\n";
    print "$cyan 03$red :$white Cars\n";
    print "$cyan 04$red :$white Comedy\n";
    print "$cyan 05$red :$white Dementia\n";
    print "$cyan 06$red :$white Demons\n";
    print "$cyan 07$red :$white Mystery\n";
    print "$cyan 08$red :$white Drama\n";
    print "$cyan 09$red :$white Ecchi\n";
    print "$cyan 10$red :$white Fantasi\n";
    print "$cyan 11$red :$white Game\n";
    print "$cyan 12$red :$white Hentai\n";
    print "$cyan 13$red :$white Historical\n";
    print "$cyan 14$red :$white Horror\n";
    print "$cyan 15$red :$white Kids\n";
    print "$cyan 16$red :$white Magic\n";
    print "$cyan 17$red :$white Martial Arts\n";
    print "$cyan 18$red :$white Mecha\n";
    print "$cyan 19$red :$white Music\n";
    print "$cyan 20$red :$white Parody\n";
    print "$cyan 21$red :$white Samurai\n";
    print "$cyan 22$red :$white Romance\n";
    print "$cyan 23$red :$white School\n";
    print "$cyan 24$red :$white Sci-fi\n";
    print "$cyan 25$red :$white Shoujo\n";
    print "$cyan 26$red :$white Shoujo Ai\n";
    print "$cyan 27$red :$white Shounen\n";
    print "$cyan 28$red :$white Shounen Ai\n";
    print "$cyan 29$red :$white Space\n";
    print "$cyan 30$red :$white Sport\n";
    print "$cyan 31$red :$white Super Power\n";
    print "$cyan 32$red :$white Vampire\n";
    print "$cyan 33$red :$white Yaoi\n";
    print "$cyan 34$red :$white Yuri\n";
    print "$cyan 35$red :$white Harem\n";
    print "$cyan 36$red :$white Slice Of Life\n";
    print "$cyan 37$red :$white Supranatural\n";
    print "$cyan 38$red :$white Military\n";
    print "$cyan 39$red :$white Police\n";
    print "$cyan 40$red :$white Psychological\n";
    print "$cyan 41$red :$white Thriller\n";
    print "$cyan 42$red :$white Seinen\n";
    print "$cyan 43$red :$white Josei\n";
    print "\n";
    print "$red >$white ";
    $id = trim(fgets(STDIN));
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_URL,'https://api.jikan.moe/v3/genre/anime/'.$id);
    $result=curl_exec($ch);
    $json = json_decode($result, true);
    foreach ($json['anime'] as $row){
        $title = $row['title'];
        $id = $row['mal_id'];
        print "$cyan [$white $id$cyan ]$red >$white $title\n";
    }
}

function mangagenre(){
    include 'config.php';
    print "\n";
    print "$cyan 01$red :$white Action\n";
    print "$cyan 02$red :$white Adventure\n";
    print "$cyan 03$red :$white Cars\n";
    print "$cyan 04$red :$white Comedy\n";
    print "$cyan 05$red :$white Dementia\n";
    print "$cyan 06$red :$white Demons\n";
    print "$cyan 07$red :$white Mystery\n";
    print "$cyan 08$red :$white Drama\n";
    print "$cyan 09$red :$white Ecchi\n";
    print "$cyan 10$red :$white Fantasi\n";
    print "$cyan 11$red :$white Game\n";
    print "$cyan 12$red :$white Hentai\n";
    print "$cyan 13$red :$white Historical\n";
    print "$cyan 14$red :$white Horror\n";
    print "$cyan 15$red :$white Kids\n";
    print "$cyan 16$red :$white Magic\n";
    print "$cyan 17$red :$white Martial Arts\n";
    print "$cyan 18$red :$white Mecha\n";
    print "$cyan 19$red :$white Music\n";
    print "$cyan 20$red :$white Parody\n";
    print "$cyan 21$red :$white Samurai\n";
    print "$cyan 22$red :$white Romance\n";
    print "$cyan 23$red :$white School\n";
    print "$cyan 24$red :$white Sci-fi\n";
    print "$cyan 25$red :$white Shoujo\n";
    print "$cyan 26$red :$white Shoujo Ai\n";
    print "$cyan 27$red :$white Shounen\n";
    print "$cyan 28$red :$white Shounen Ai\n";
    print "$cyan 29$red :$white Space\n";
    print "$cyan 30$red :$white Sport\n";
    print "$cyan 31$red :$white Super Power\n";
    print "$cyan 32$red :$white Vampire\n";
    print "$cyan 33$red :$white Yaoi\n";
    print "$cyan 34$red :$white Yuri\n";
    print "$cyan 35$red :$white Harem\n";
    print "$cyan 36$red :$white Slice Of Life\n";
    print "$cyan 37$red :$white Supranatural\n";
    print "$cyan 38$red :$white Military\n";
    print "$cyan 39$red :$white Police\n";
    print "$cyan 40$red :$white Psychological\n";
    print "$cyan 41$red :$white Seinen\n";
    print "$cyan 42$red :$white Josei\n";
    print "$cyan 43$red :$white Doujinshi\n";
    print "$cyan 44$red :$white Gender Bender\n";
    print "$cyan 45$red :$white Thriller\n";
    print "\n";
    print "$red >$white ";
    $id = trim(fgets(STDIN));
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_URL,'https://api.jikan.moe/v3/genre/manga/'.$id);
    $result=curl_exec($ch);
    $json = json_decode($result, true);
    foreach ($json['manga'] as $row){
        $title = $row['title'];
        $id = $row['mal_id'];
        print "$cyan [$white $id$cyan ]$red >$white $title\n";
    }
}

function cmd(){
    include 'config.php';
    print "$red >$white ";
    $cmd = trim(fgets(STDIN));
    if ($cmd == '1'){
        animesearch();
    }
    elseif ($cmd == '2'){
        mangasearch();
    }
    elseif ($cmd == '3'){
        animeinfo();
    }
    elseif ($cmd == '4'){
        mangainfo();
    }
    elseif ($cmd == '5'){
        animeschedule();
    }
    elseif ($cmd == '6'){
        animetop();
    }
    elseif ($cmd == '7'){
        mangatop();
    }
    elseif ($cmd == '8'){
        chartop();
    }
    elseif ($cmd == '9'){
        animegenre();
    }
    elseif ($cmd == '10'){
        mangagenre();
    }
}

index();
menu();
cmd();

?>
