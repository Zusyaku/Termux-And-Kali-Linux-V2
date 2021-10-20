<?php


class Url {
	/*
	Script : Shorteners Url
	Creator : Kingtebe
	Date    : 17-06-2021
	*/
	public function __construct(){
		$this->Tinyurl();}
		var $menu = "\n=====================\n ╔╦╗╦╔╗╔╦ ╦╦ ╦╦═╗╦\n  ║ ║║║║╚╦╝║ ║╠╦╝║\n  ╩ ╩╝╚╝ ╩ ╚═╝╩╚═╩═╝\n=====================\n 1) Short Url\n 2) About Tools\n 3) More Tools\n 0) Exit\n=====================\n";

	public function Tinyurl(){
		try {
			system("clear");
			echo $this->menu;
			echo " > Choose : ";
			$link = trim(fgets(STDIN));
			if (is_numeric($link)) {
				if ($link == "1" or $link == "01") {
					echo " > Link/Url : "; $short = trim(fgets(STDIN));
					$user = "Chrome/83.0.4103.106";
					$api = "https://tinyurl.com/api-create.php?url=$short";
					$headers = array("upgrade-insecure-requests: 1",
						"accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
						"sec-fetch-site: none",
						"sec-fetch-mode: navigate",
						"sec-fetch-user: ?1",
						"sec-fetch-dest: document");
					$ch = curl_init();
					curl_setopt($ch, CURLOPT_URL, $api);
					curl_setopt($ch, CURLOPT_POST, 1);
					curl_setopt($ch, CURLOPT_USERAGENT, $user);
					curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
					curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
					$response = curl_exec($ch);
					curl_close($ch); echo "=====================\n > Success : ".$response."\n\n";

				} else if ($link == "2" or $link == "02") {
					$options = ["\n •) Script Name : Shorteners Url\n",
						" •) Author : Kingtebe\n",
						" •) Date : 17-06-2021\n",
						" •) Youtube : FaaL TV\n",
						" •) Github : https://github.com/Kingtebe\n\n"];

					foreach($options as $list) {
						echo $list;}

				} else if ($link == "3" or $link == "03") {
					system("xdg-open https://github.com/Kingtebe");}

			} else {
				exit("\n !) Yang Bener Dong Guoblokkk !!! \n\n");}

		} catch(Exception $e) {
			print $e.getMessage();}}}

new Url;

?>
