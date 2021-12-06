#!/usr/bin/perl
# Subdomain Checker tool by N1ght.Hax0r

use HTTP::Request;
use LWP::UserAgent;
use Term::ANSIColor qw(:constants);

system("clear");

print '
'.BOLD CYAN.'  _____     _   _____                         '.RESET.'
'.BOLD CYAN.' |   __|_ _| |_|   __|___ ___ ___ ___ ___ ___ '.RESET.'
'.BOLD CYAN.' |__   | | | . |__   |  _| .\'|   |   | -_|  _|'.RESET.'
'.BOLD CYAN.' |_____|___|___|_____|___|__,|_|_|_|_|___|_|  '.RESET.'

'.BOLD WHITE.' ========================['.BOLD YELLOW.' Ver.2.5 '.BOLD WHITE.']==========='.RESET.'

';

print ''.BOLD GREEN.' Target (Without http://)'.BOLD RED.' > '.BOLD WHITE.'';
$host = <>;
chomp($host);
print ''.BOLD YELLOW.' Listing... '.BOLD WHITE.'';
print "\n\n";
$a = "http://www.ewhois.com/".$host."\/";
$b = LWP::UserAgent->new();
$c = $b->request(HTTP::Request->new(GET=>$a));
$d = $c->content;
if($d =~ m/<span id=\"ip_display\">(.*?)<\/span>/) {
  print " Host IP : $1 \n";
}

$e = LWP::UserAgent->new();
$e->agent('Mozilla/5.0 (Windows; U; Windows NT 5.1; de-LI; rv:1.9.0.16) Gecko/2009120208 Firefox/3.0.16 (.NET CLR 3.5.30729)');
$f = "http://www.pagesinventory.com/search/?s=".$host."";
$g = $e->request(HTTP::Request->new(GET=>$f));
$h = $g->content;

while($h =~ m/<td><a href=\"\/domain\/(.*?).html\">/g ) {
  print " Sub Domain : $1\n";
  open(a, ">>$host.txt");
  print a "http://$1\n";
  close(a);
}

print "\n\n Result reported to $host.txt\n";
