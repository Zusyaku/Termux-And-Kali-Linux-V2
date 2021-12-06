#!/bin/sh

# Colors
blue='\e[1;34'
cyan='\e[1;36m'
green='\e[1;34m'
okegreen='\033[92m'
lightgreen='\e[1;32m'
white='\e[1;37m'
red='\e[1;31m'
yellow='\e[1;33m'

# Banner
banner(){
    clear
    echo -e "$cyan"
    echo -e "      _______  _______   ________  ________  ________  _______  "
    echo -e "    ╱╱   ╱   ╲╱       ╲╲╱        ╲╱    ╱   ╲╱  ╱  ╱  ╲╱       ╲╲"
    echo -e "   ╱╱        ╱        ╱╱        _╱         ╱         ╱        ╱╱"
    echo -e "  ╱         ╱         ╱-        ╱╲__     ╱╱╱        ╱         ╱ "
    echo -e "  ╲__╱_____╱╲___╱____╱╲_______╱╱   ╲____╱╱╲╲_______╱╲___╱____╱  "
    echo -e "$white"
    echo -e "           NMAP Automation Script You Want to Adore"
}

if [ $EUID -ne 0 ]
then
    banner
    echo -e "\n$red  !!$white This script must be run as$red root" 
    exit 1
fi

banner
echo -e "$white"
read -p "  target : " target;

function brutense(){
    banner
    echo -e ""
    echo -e "$yellow  [?]$white Brute Script"
    echo -e ""
    echo -e "$cyan  01$red :$white afp-brute"
    echo -e "$cyan  02$red :$white ajp-brute"
    echo -e "$cyan  03$red :$white backorifice-brute"
    echo -e "$cyan  04$red :$white cassandra-brute"
    echo -e "$cyan  05$red :$white cics-user-brute"
    echo -e "$cyan  06$red :$white citrix-brute-xml"
    echo -e "$cyan  07$red :$white cvs-brute-repository"
    echo -e "$cyan  08$red :$white cvs-brute"
    echo -e "$cyan  09$red :$white deluge-rpc-brute"
    echo -e "$cyan  10$red :$white dicom-brute"
    echo -e "$cyan  11$red :$white dns-brute"
    echo -e "$cyan  12$red :$white domcon-brute"
    echo -e "$cyan  13$red :$white dpap-brute"
    echo -e "$cyan  14$red :$white drda-brute"
    echo -e "$cyan  15$red :$white ftp-brute"
    echo -e "$cyan  16$red :$white http-brute"
    echo -e "$cyan  17$red :$white http-form-brute"
    echo -e "$cyan  18$red :$white http-iis-short-name-brute"
    echo -e "$cyan  19$red :$white http-joomla-brute"
    echo -e "$cyan  20$red :$white http-proxy-brute"
    echo -e "$cyan  21$red :$white http-wordpress-brute"
    echo -e "$cyan  22$red :$white iax2-brute"
    echo -e "$cyan  23$red :$white imap-brute"
    echo -e "$cyan  24$red :$white informix-brute."
    echo -e "$cyan  25$red :$white ipmi-brute"
    echo -e "$cyan  26$red :$white irc-brute"
    echo -e "$cyan  27$red :$white irc-sasl-brute"
    echo -e "$cyan  28$red :$white iscsi-brute"
    echo -e "$cyan  29$red :$white ldap-brute"
    echo -e "$cyan  30$red :$white membase-brute"
    echo -e "$cyan  31$red :$white metasploit-msgrpc-brute"
    echo -e "$cyan  32$red :$white metasploit-xmlrpc-brute"
    echo -e "$cyan  33$red :$white mikrotik-routeros-brute"
    echo -e "$cyan  34$red :$white mmouse-brute"
    echo -e "$cyan  35$red :$white mongodb-brute"
    echo -e "$cyan  36$red :$white ms-sql-brute"
    echo -e "$cyan  37$red :$white mysql-brute"
    echo -e "$cyan  38$red :$white nessus-brute"
    echo -e "$cyan  39$red :$white nessus-xmlrpc-brute"
    echo -e "$cyan  40$red :$white netbus-brute"
    echo -e "$cyan  41$red :$white nexpose-brute"
    echo -e "$cyan  42$red :$white nje-node-brute"
    echo -e "$cyan  43$red :$white nje-pass-brute"
    echo -e "$cyan  44$red :$white nping-brute"
    echo -e "$cyan  45$red :$white omp2-brute"
    echo -e "$cyan  46$red :$white openvas-otp-brute"
    echo -e "$cyan  47$red :$white oracle-brute-stealth"
    echo -e "$cyan  48$red :$white oracle-brute"
    echo -e "$cyan  49$red :$white oracle-sid-brute"
    echo -e "$cyan  50$red :$white pcanywhere-brute"
    echo -e "$cyan  51$red :$white pgsql-brute"
    echo -e "$cyan  52$red :$white pop3-brute"
    echo -e "$cyan  53$red :$white redis-brute"
    echo -e "$cyan  54$red :$white rexec-brute"
    echo -e "$cyan  55$red :$white rlogin-brute"
    echo -e "$cyan  56$red :$white rpcap-brute"
    echo -e "$cyan  57$red :$white rsync-brute"
    echo -e "$cyan  58$red :$white rtsp-url-brute"
    echo -e "$cyan  59$red :$white sip-brute"
    echo -e "$cyan  60$red :$white smb-brute"
    echo -e "$cyan  61$red :$white smtp-brute"
    echo -e "$cyan  62$red :$white snmp-brute"
    echo -e "$cyan  63$red :$white socks-brute"
    echo -e "$cyan  64$red :$white ssh-brute"
    echo -e "$cyan  65$red :$white svn-brute"
    echo -e "$cyan  66$red :$white telnet-brute"
    echo -e "$cyan  67$red :$white tso-brute"
    echo -e "$cyan  68$red :$white vmauthd-brute"
    echo -e "$cyan  69$red :$white vnc-brute"
    echo -e "$cyan  70$red :$white xmpp-brute"
    echo -e ""
    echo -e "$cyan  00$red :$white Back"
    echo -e ""
    read -p " Select one : " brute;
    banner
    echo -e ""
    if [ $brute == 1 ]
    then
        read -p " port : " port;
        nmap -p $port --script afp-brute $target
    elif [ $brute == 2 ]
    then
        read -p " port : " port;
        nmap -p 8009 $target --script ajp-brute
    elif [ $brute == 3 ]
    then
        read -p " port : " port;
        nmap -sU --script backorifice-brute $target --script-args backorifice-brute.ports=$port
    elif [ $brute == 4 ]
    then
        read -p " port : " port;
        nmap -p $port $target --script=cassandra-brute
    elif [ $brute == 5 ]
    then
        read -p " port : " port;
        nmap --script=cics-user-brute -p $port $target
    elif [ $brute == 6 ]
    then
        read -p " userdb : " userdb;
        read -p " passdb : " passdb;
        read -p " domain : " domain;
        read -p " port   : " port;
        nmap --script=citrix-brute-xml --script-args=userdb=$userdb,passdb=$passdb,ntdomain=$domain -p $port $target
    elif [ $brute == 7 ]
    then
        read -p " port : " port;
        nmap -p $port --script cvs-brute-repository $target
    elif [ $brute == 8 ]
    then
        read -p " port : " port;
        nmap -p $port --script cvs-brute $target
    elif [ $brute == 9 ]
    then
        read -p " port : " port;
        nmap --script deluge-rpc-brute -p $port $target
    elif [ $brute == 10 ]
    then
        nmap -sV --script dicom-brute $target
    elif [ $brute == 11 ]
    then
        nmap --script dns-brute $target
    elif [ $brute == 12 ]
    then
        read -p " port : " port;
        nmap --script domcon-brute -p $port $target
    elif [ $brute == 13 ]
    then
        read -p " port : " port;
        nmap --script dpap-brute -p $port $target
    elif [ $brute == 14 ]
    then
        read -p " port : " port;
        nmap -p $port --script drda-brute $target
    elif [ $brute == 15 ]
    then
        read -p " port : " port;
        nmap --script ftp-brute -p $port $target
    elif [ $brute == 16 ]
    then
        read -p " port : " port;
        nmap --script http-brute -p $port $target
    elif [ $brute == 17 ]
    then
        read -p " port : " port;
        nmap --script http-form-brute -p $port $target
    elif [ $brute == 18 ]
    then
        read -p " port : " port;
        nmap -p $port --script http-iis-short-name-brute $target
    elif [ $brute == 19 ]
    then
        nmap -sV --script http-joomla-brute $target
    elif [ $brute == 20 ]
    then
        read -p " port : " port;
        nmap --script http-proxy-brute -p $port $target
    elif [ $brute == 21 ]
    then
        nmap -sV --script http-wordpress-brute $target
    elif [ $brute == 22 ]
    then
        read -p " port : " port;
        nmap -sU -p $port $target --script iax2-brute
    elif [ $brute == 23 ]
    then
        read -p " port : " port;
        nmap -p $port --script imap-brute $target
    elif [ $brute == 24 ]
    then
        read -p " port : " port;
        nmap --script informix-brute -p $port $target
    elif [ $brute == 25 ]
    then
        read -p " port : " port;
        nmap -sU --script ipmi-brute -p $port $target
    elif [ $brute == 26 ]
    then
        read -p " port : " port;
        nmap --script irc-brute -p $port $target
    elif [ $brute == 27 ]
    then
        read -p " port : " port;
        nmap --script irc-sasl-brute -p $port $target
    elif [ $brute == 28 ]
    then
        nmap -sV --script=iscsi-brute $target
    elif [ $brute == 29 ]
    then
        read -p " port : " port;
        nmap -p $port --script ldap-brute --script-args ldap.base='"cn=users,dc=cqure,dc=net"' $target
    elif [ $brute == 30 ]
    then
        read -p " port : " port;
        nmap -p $port --script membase-brute $target
    elif [ $brute == 31 ]
    then
        read -p " port : " port;
        nmap --script metasploit-msgrpc-brute -p $port $target
    elif [ $brute == 32 ]
    then
        read -p " port : " port;
        nmap --script metasploit-xmlrpc-brute -p $port $target
    elif [ $brute == 33 ]
    then
        read -p " port : " port;
        nmap -p $port --script mikrotik-routeros-brute $target
    elif [ $brute == 34 ]
    then
        read -p " port : " port;
        nmap --script mmouse-brute -p $port $target
    elif [ $brute == 35 ]
    then
        read -p " port : " port;
        nmap -p $port $target --script mongodb-brute
    elif [ $brute == 36 ]
    then
        read -p " userdb : " userdb;
        read -p " passdb : " passdb;
        read -p " port   : " port;
        nmap -p $port --script ms-sql-brute --script-args mssql.instance-all,userdb=$userdb,passdb=$passdb $target
    elif [ $brute == 37 ]
    then
        nmap --script=mysql-brute $target
    elif [ $brute == 38 ]
    then
        read -p " port : " port;
        nmap --script nessus-brute -p $port $target
    elif [ $brute == 39 ]
    then
        nmap -sV --script=nessus-xmlrpc-brute $target
    elif [ $brute == 40 ]
    then
        read -p " port : " port;
        nmap -p $port --script netbus-brute $target
    elif [ $brute == 41 ]
    then
        read -p " port : " port;
        nmap --script nexpose-brute -p $port $target
    elif [ $brute == 42 ]
    then
        nmap -sV --script=nje-node-brute $target
    elif [ $brute == 43 ]
    then
        read -p " ohost : " ohost;
        read -p " rhost : " rhost;
        nmap -sV --script=nje-pass-brute --script-args=ohost=$ohost,rhost=$rhost $target
    elif [ $brute == 44 ]
    then
        read -p " port : " port;
        nmap -p $port --script nping-brute $target
    elif [ $brute == 45 ]
    then
        read -p " port : " port;
        nmap -p $port --script omp2-brute $target
    elif [ $brute == 46 ]
    then
        nmap -sV --script=openvas-otp-brute $target
    elif [ $brute == 47 ]
    then
        read -p " port : " port;
        nmap --script oracle-brute-stealth -p $port --script-args oracle-brute-stealth.sid=ORCL $target
    elif [ $brute == 48 ]
    then
        read -p " port : " port;
        nmap --script oracle-brute -p $port --script-args oracle-brute.sid=ORCL $target
    elif [ $brute == 49 ]
    then
        read -p " port : " port;
        nmap --script=oracle-sid-brute -p $port $target
    elif [ $brute == 50 ]
    then
        nmap --script=pcanywhere-brute $target
    elif [ $brute == 51 ]
    then
        read -p " port : " port;
        nmap -p $port --script pgsql-brute $target
    elif [ $brute == 52 ]
    then
        nmap -sV --script=pop3-brute $target
    elif [ $brute == 53 ]
    then
        nmap -p $port $target --script redis-brute
    elif [ $brute == 54 ]
    then
        nmap -p $port --script rexec-brute $target
    elif [ $brute == 55 ]
    then
        nmap -p $port --script rlogin-brute $target
    elif [ $brute == 56 ]
    then
        nmap -p $port $target --script rpcap-brute
    elif [ $brute == 57 ]
    then
        nmap -p $port --script rsync-brute --script-args 'rsync-brute.module=www' $target
    elif [ $brute == 58 ]
    then
        read -p " port : " port;
        nmap --script rtsp-url-brute -p $port $target
    elif [ $brute == 59 ]
    then
        read -p " port : " port;
        nmap -sU -p $port $target --script=sip-brute
    elif [ $brute == 60 ]
    then
        read -p " port : " port;
        nmap --script smb-brute.nse -p $port $target
    elif [ $brute == 61 ]
    then
        read -p " port : " port;
        nmap -p $port --script smtp-brute $target
    elif [ $brute == 62 ]
    then
        read -p " wordlist : " wordlist;
        nmap -sU --script snmp-brute $target [--script-args snmp-brute.communitiesdb=$wordlist ]
    elif [ $brute == 63 ]
    then
        read -p " port : " port;
        nmap --script socks-brute -p $port $target
    elif [ $brute == 64 ]
    then
        read -p " userdb : " userdb;
        read -p " passdb : " passdb;
        read -p " port   : " port;
        nmap -p $port --script ssh-brute --script-args userdb=$userdb,passdb=$passdb --script-args ssh-brute.timeout=4s $target
    elif [ $brute == 65 ]
    then
        read -p " port : " port;
        nmap --script svn-brute --script-args svn-brute.repo=/svn/ -p $port $target
    elif [ $brute == 66 ]
    then
        read -p " userdb : " userdb;
        read -p " passdb : " passdb;
        read -p " port   : " port;
        nmap -p $port --script telnet-brute --script-args userdb=$userdb,passdb=$passdb,telnet-brute.timeout=8s $target
    elif [ $brute == 67 ]
    then
        read -p " port : " port;
        nmap -p $port --script tso-brute $target
    elif [ $brute == 68 ]
    then
        read -p " port : " port;
        nmap -p $port $target --script vmauthd-brute
    elif [ $brute == 69 ]
    then
        read -p " port : " port;
        nmap --script vnc-brute -p $port $target
    elif [ $brute == 70 ]
    then
        read -p " port : " port;
        nmap -p $port --script xmpp-brute $target
    elif [ $brute == 0 ]
    then
        scripts
    else
        brutense
    fi
}

function enumnse(){
    banner
    echo -e ""
    echo -e "$yellow  [?]$white Enumeration Script"
    echo -e ""
    echo -e "$cyan  01$red :$white cics-enum"
    echo -e "$cyan  02$red :$white cics-user-enum"
    echo -e "$cyan  03$red :$white citrix-enum-apps-xml"
    echo -e "$cyan  04$red :$white citrix-enum-apps"
    echo -e "$cyan  05$red :$white citrix-enum-servers-xml"
    echo -e "$cyan  06$red :$white citrix-enum-servers"
    echo -e "$cyan  07$red :$white dns-nsec-enum"
    echo -e "$cyan  08$red :$white dns-nsec3-enum"
    echo -e "$cyan  09$red :$white dns-srv-enum"
    echo -e "$cyan  10$red :$white domino-enum-users"
    echo -e "$cyan  11$red :$white eppc-enum-processes"
    echo -e "$cyan  12$red :$white http-domino-enum-passwords"
    echo -e "$cyan  13$red :$white http-drupal-enum-users"
    echo -e "$cyan  14$red :$white http-drupal-enum"
    echo -e "$cyan  15$red :$white http-enum"
    echo -e "$cyan  16$red :$white http-gitweb-projects-enum"
    echo -e "$cyan  17$red :$white http-svn-enum"
    echo -e "$cyan  18$red :$white http-userdir-enum"
    echo -e "$cyan  19$red :$white http-wordpress-enum"
    echo -e "$cyan  20$red :$white krb5-enum-users"
    echo -e "$cyan  21$red :$white lu-enum"
    echo -e "$cyan  22$red :$white msrpc-enum"
    echo -e "$cyan  23$red :$white mysql-enum"
    echo -e "$cyan  24$red :$white ncp-enum-users"
    echo -e "$cyan  25$red :$white nrpe-enum"
    echo -e "$cyan  26$red :$white omp2-enum-targets"
    echo -e "$cyan  27$red :$white oracle-enum-users"
    echo -e "$cyan  28$red :$white rdp-enum-encryption"
    echo -e "$cyan  29$red :$white sip-enum-users"
    echo -e "$cyan  30$red :$white smb-enum-domains"
    echo -e "$cyan  31$red :$white smb-enum-groups"
    echo -e "$cyan  32$red :$white smb-enum-processes"
    echo -e "$cyan  33$red :$white smb-enum-services"
    echo -e "$cyan  34$red :$white smb-enum-sessions"
    echo -e "$cyan  35$red :$white smb-enum-shares"
    echo -e "$cyan  36$red :$white smb-enum-users"
    echo -e "$cyan  37$red :$white smb-mbenum"
    echo -e "$cyan  38$red :$white smtp-enum-users"
    echo -e "$cyan  39$red :$white ssh2-enum-algos"
    echo -e "$cyan  40$red :$white ssl-enum-ciphers"
    echo -e "$cyan  41$red :$white tftp-enum"
    echo -e "$cyan  42$red :$white tso-enum"
    echo -e "$cyan  43$red :$white vtam-enum"
    echo -e ""
    echo -e "$cyan  00$red :$white Back"
    echo -e ""
    read -p " Select one : " enum;
    banner
    echo -e ""
    if [ $enum == 1 ]
    then
        read -p " port : " port;
        nmap --script=cics-enum -p $port $target
    elif [ $enum == 2 ]
    then
        read -p " port : " port;
        nmap --script=cics-user-enum -p $port $target
    elif [ $enum == 3 ]
    then
        read -p " port : " port;
        nmap --script=citrix-enum-apps-xml -p $port $target
    elif [ $enum == 4 ]
    then
        read -p " port : " port;
        nmap -sU --script=citrix-enum-apps -p $port $target
    elif [ $enum == 5 ]
    then
        read -p " port : " port;
        nmap --script=citrix-enum-servers-xml -p $port $target
    elif [ $enum == 6 ]
    then
        read -p " port : " port;
        nmap -sU --script=citrix-enum-servers -p $port $target
    elif [ $enum == 7 ]
    then
        read -p " domain : " domain;
        read -p " port   : " port;
        nmap -sSU -p $port --script dns-nsec-enum --script-args dns-nsec-enum.domains=$domain
    elif [ $enum == 8 ]
    then
        read -p " domain : " domain;
        read -p " port   : " port;
        nmap  -sU -p $port $target --script=dns-nsec3-enum --script-args dns-nsec3-enum.domains=$domain
    elif [ $enum == 9 ]
    then
        nmap --script dns-srv-enum --script-args "dns-srv-enum.domain='$domain'"
    elif [ $enum == 10 ]
    then
        read -p " port : " port;
        nmap --script domino-enum-users -p $port $target
    elif [ $enum == 11 ]
    then
        read -p " port : " port;
        nmap -p $port $target --script eppc-enum-processes
    elif [ $enum == 12 ]
    then
        read -p " username : " username;
        read -p " password : " password;
        read -p " port     : " port;
        nmap --script http-domino-enum-passwords -p $port $target --script-args http-domino-enum-passwords.username=$username,http-domino-enum-passwords.password=$password
    elif [ $enum == 13 ]
    then
        nmap --script=http-drupal-enum-users --script-args http-drupal-enum-users.root="/path/" $target
    elif [ $enum == 14 ]
    then
        read -p " port : " port;
        nmap -p $port --script http-drupal-enum $target
    elif [ $enum == 15 ]
    then
        nmap -sV --script=http-enum $target
    elif [ $enum == 16 ]
    then
        read -p " port : " port;
        nmap -p $port $target --script http-gitweb-projects-enum
    elif [ $enum == 17 ]
    then
        nmap --script http-svn-enum $target
    elif [ $enum == 18 ]
    then
        nmap -sV --script=http-userdir-enum $target
    elif [ $enum == 19 ]
    then
        nmap -sV --script http-wordpress-enum $target
    elif [ $enum == 20 ]
    then
        read -p " port : " port;
        nmap -p $port --script krb5-enum-users --script-args krb5-enum-users.realm='test'
    elif [ $enum == 21 ]
    then
        read -p " port : " port;
        nmap --script lu-enum -p $port $target
    elif [ $enum == 22 ]
    then
        nmap $target --script=msrpc-enum
    elif [ $enum == 23 ]
    then
        nmap --script=mysql-enum $target
    elif [ $enum == 24 ]
    then
        nmap -sV --script=ncp-enum-users $target
    elif [ $enum == 25 ]
    then
        read -p " port : " port;
        nmap --script nrpe-enum -p $port $target
    elif [ $enum == 26 ]
    then
        read -p " port : " port;
        nmap -p $port --script omp2-brute,omp2-enum-targets $target
    elif [ $enum == 27 ]
    then
        read -p " port : " port;
        nmap --script oracle-enum-users --script-args oracle-enum-users.sid=ORCL -p $port $target
    elif [ $enum == 28 ]
    then
        read -p " port : " port;
        nmap -p $port --script rdp-enum-encryption $target
    elif [ $enum == 29 ]
    then
        read -p " port : " port;
        nmap --script=sip-enum-users -sU -p $port $target
    elif [ $enum == 30 ]
    then
        read -p " port : " port;
        nmap --script smb-enum-domains.nse -p $port $target
    elif [ $enum == 31 ]
    then
        read -p " port : " port;
        nmap --script smb-enum-users.nse -p $port $target
    elif [ $enum == 32 ]
    then
        read -p " port : " port;
        nmap --script smb-enum-processes.nse -p $port $target
    elif [ $enum == 33 ]
    then
        read -p " port : " port;
        nmap --script smb-enum-services.nse -p $port $target
    elif [ $enum == 34 ]
    then
        read -p " port : " port;
        nmap --script smb-enum-sessions.nse -p $port $target
    elif [ $enum == 35 ]
    then
        read -p " port : " port;
        nmap --script smb-enum-shares.nse -p $port $target
    elif [ $enum == 36 ]
    then
        read -p " port : " port;
        nmap --script smb-enum-users.nse -p $port $target
    elif [ $enum == 37 ]
    then
        read -p " port : " port;
        nmap -p $port $target --script smb-mbenum
    elif [ $enum == 38 ]
    then
        read -p " port : " port;
        nmap --script smtp-enum-users.nse [--script-args smtp-enum-users.methods=EXPN] -p $port $target
    elif [ $enum == 39 ]
    then
        nmap --script ssh2-enum-algos $target
    elif [ $enum == 40 ]
    then
        nmap -sV --script ssl-enum-ciphers -p $port $target
    elif [ $enum == 41 ]
    then
        read -p " list : " list;
        read -p " port : " port;
        nmap -sU -p $port --script tftp-enum.nse --script-args tftp-enum.filelist=$list $target
    elif [ $enum == 42 ]
    then
        read -p " port : " port;
        nmap --script=tso-enum -p $port $target
    elif [ $enum == 43 ]
    then
        read -p " port : " port;
        nmap --script vtam-enum -p $port $target
    elif [ $enum == 0 ]
    then
        scripts
    else
        enumnse
    fi
}

function authnse(){
    banner
    echo -e ""
    echo -e "$yellow  [?]$white Auth Script"
    echo -e ""
    echo -e "$cyan  01$red :$white ajp-auth"
    echo -e "$cyan  02$red :$white auth-owners"
    echo -e "$cyan  03$red :$white auth-spoof"
    echo -e "$cyan  04$red :$white http-auth-finder"
    echo -e "$cyan  05$red :$white http-auth"
    echo -e "$cyan  06$red :$white netbus-auth-bypass"
    echo -e "$cyan  07$red :$white realvnc-auth-bypass"
    echo -e "$cyan  08$red :$white socks-auth-info"
    echo -e "$cyan  09$red :$white ssh-auth-methods"
    echo -e ""
    echo -e "$cyan  00$red :$white Back"
    echo -e ""
    read -p " Select one : " auth;
    banner
    echo -e ""
    if [ $auth == 1 ]
    then
        read -p " port : " port;
        nmap -p $port $target --script ajp-auth [--script-args ajp-auth.path=/login]
    elif [ $auth == 2 ]
    then
        nmap -sV -sC $target
    elif [ $auth == 3 ]
    then
        nmap -sV --script=auth-spoof $target
    elif [ $auth == 4 ]
    then
        read -p " port : " port;
        nmap -p $port --script http-auth-finder $target
    elif [ $auth == 5 ]
    then
        read -p " port : " port;
        nmap --script http-auth [--script-args http-auth.path=/login] -p $port $target
    elif [ $auth == 6 ]
    then
        read -p " port : " port;
        nmap -p $port --script netbus-auth-bypass $target
    elif [ $auth == 7 ]
    then
        nmap -sV --script=realvnc-auth-bypass $target
    elif [ $auth == 8 ]
    then
        read -p " port : " port;
        nmap -p $port $target --script socks-auth-info
    elif [ $auth == 9 ]
    then
        read -p " username : " username;
        read -p " port     : " port;
        nmap -p $port --script ssh-auth-methods --script-args="ssh.user=$username" $target
    elif [ $auth == 0 ]
    then
        scripts
    else
        authnse
    fi
}

function vulnnse(){
    banner
    echo -e ""
    echo -e "$yellow  [?]$white Vulnerable Script"
    echo -e ""
    echo -e "$cyan  01$red :$white afp-path-vuln"
    echo -e "$cyan  02$red :$white ftp-vuln-cve2010-4221"
    echo -e "$cyan  03$red :$white http-huawei-hg5xx-vuln"
    echo -e "$cyan  04$red :$white http-iis-webdav-vuln"
    echo -e "$cyan  05$red :$white http-vmware-path-vuln"
    echo -e "$cyan  06$red :$white http-vuln-cve2006-3392"
    echo -e "$cyan  07$red :$white http-vuln-cve2009-3960"
    echo -e "$cyan  08$red :$white http-vuln-cve2010-0738"
    echo -e "$cyan  09$red :$white http-vuln-cve2010-2861"
    echo -e "$cyan  10$red :$white http-vuln-cve2011-3192"
    echo -e "$cyan  11$red :$white http-vuln-cve2011-3368"
    echo -e "$cyan  12$red :$white http-vuln-cve2012-1823"
    echo -e "$cyan  13$red :$white http-vuln-cve2013-0156"
    echo -e "$cyan  14$red :$white http-vuln-cve2013-6786"
    echo -e "$cyan  15$red :$white http-vuln-cve2013-7091"
    echo -e "$cyan  16$red :$white http-vuln-cve2014-2126"
    echo -e "$cyan  17$red :$white http-vuln-cve2014-2127"
    echo -e "$cyan  18$red :$white http-vuln-cve2014-2128"
    echo -e "$cyan  19$red :$white http-vuln-cve2014-2129"
    echo -e "$cyan  20$red :$white http-vuln-cve2014-3704"
    echo -e "$cyan  21$red :$white http-vuln-cve2014-8877"
    echo -e "$cyan  22$red :$white http-vuln-cve2015-1427"
    echo -e "$cyan  23$red :$white http-vuln-cve2015-1635"
    echo -e "$cyan  24$red :$white http-vuln-cve2017-5638"
    echo -e "$cyan  25$red :$white http-vuln-cve2017-5689"
    echo -e "$cyan  26$red :$white http-vuln-cve2017-8917"
    echo -e "$cyan  27$red :$white http-vuln-cve2017-1001000"
    echo -e "$cyan  28$red :$white http-vuln-misfortune-cookie"
    echo -e "$cyan  29$red :$white http-vuln-wnr1000-creds"
    echo -e "$cyan  30$red :$white mysql-vuln-cve2012-2122"
    echo -e "$cyan  31$red :$white rdp-vuln-ms12-020"
    echo -e "$cyan  32$red :$white rmi-vuln-classloader"
    echo -e "$cyan  33$red :$white rsa-vuln-roca"
    echo -e "$cyan  34$red :$white samba-vuln-cve-2012-1182"
    echo -e "$cyan  35$red :$white smb-vuln-conficker"
    echo -e "$cyan  36$red :$white smb-vuln-cve-2017-7494"
    echo -e "$cyan  37$red :$white smb-vuln-cve2009-3103"
    echo -e "$cyan  38$red :$white smb-vuln-ms06-025"
    echo -e "$cyan  39$red :$white smb-vuln-ms07-029"
    echo -e "$cyan  40$red :$white smb-vuln-ms08-067"
    echo -e "$cyan  41$red :$white smb-vuln-ms10-054"
    echo -e "$cyan  42$red :$white smb-vuln-ms10-061"
    echo -e "$cyan  43$red :$white smb-vuln-ms17-010"
    echo -e "$cyan  44$red :$white smb-vuln-regsvc-dos"
    echo -e "$cyan  45$red :$white smb-vuln-webexec"
    echo -e "$cyan  46$red :$white smb2-vuln-uptime"
    echo -e "$cyan  47$red :$white smtp-vuln-cve2010-4344"
    echo -e "$cyan  48$red :$white smtp-vuln-cve2011-1720"
    echo -e "$cyan  49$red :$white smtp-vuln-cve2011-1764"
    echo -e "$cyan  50$red :$white vulners"
    echo -e ""
    echo -e "$cyan  00$red :$white Back"
    echo -e ""
    read -p "Select one : " vuln;
    banner
    echo -e ""
    if [ $vuln == 1 ]
    then
        nmap -sV --script=afp-path-vuln $target
    elif [ $vuln == 2 ]
    then
        read -p " port : " port;
        nmap --script ftp-vuln-cve2010-4221 -p $port $target
    elif [ $vuln == 3 ]
    then
        nmap -sV http-huawei-hg5xx-vuln $target
    elif [ $vuln == 4 ]
    then
        read -p " port : " port;
        nmap --script http-iis-webdav-vuln -p $port $target
    elif [ $vuln == 5 ]
    then
        read -p " port : " port;
        nmap --script http-vmware-path-vuln -p $port $target
    elif [ $vuln == 6 ]
    then
        nmap -sV --script http-vuln-cve2006-3392 $target
    elif [ $vuln == 7 ]
    then
        nmap --script=http-vuln-cve2009-3960 --script-args http-http-vuln-cve2009-3960.root="/root/" $target
    elif [ $vuln == 8 ]
    then
        read -p " path : " path;
        nmap --script=http-vuln-cve2010-0738 --script-args "http-vuln-cve2010-0738.paths={$path}" $target
    elif [ $vuln == 9 ]
    then
        nmap --script http-vuln-cve2010-2861 $target
    elif [ $vuln == 10 ]
    then
        read -p " hostname : " hostname;
        read -p " port     : " port;
        nmap --script http-vuln-cve2011-3192.nse [--script-args http-vuln-cve2011-3192.hostname=$hostname] -pT:$port $target
    elif [ $vuln == 11 ]
    then
        nmap --script http-vuln-cve2011-3368 $target
    elif [ $vuln == 12 ]
    then
        nmap -sV --script http-vuln-cve2012-1823 $target
    elif [ $vuln == 13 ]
    then
        nmap -sV --script http-vuln-cve2013-0156 $target
    elif [ $vuln == 14 ]
    then
        nmap -sV http-vuln-cve2013-6786 $target
    elif [ $vuln == 15 ]
    then
        nmap -sV --script http-vuln-cve2013-7091 $target
    elif [ $vuln == 16 ]
    then
        read -p " port : " port;
        nmap -p $port --script http-vuln-cve2014-2126 $target
    elif [ $vuln == 17 ]
    then
        read -p " port : " port;
        nmap -p $port --script http-vuln-cve2014-2127 $target
    elif [ $vuln == 18 ]
    then
        read -p " port : " port;
        nmap -p $port --script http-vuln-cve2014-2128 $target
    elif [ $vuln == 19 ]
    then
        read -p " port : " port;
        nmap -p $port --script http-vuln-cve2014-2129 $target
    elif [ $vuln == 20 ]
    then
        nmap --script http-vuln-cve2014-3704 --script-args http-vuln-cve2014-3704.cmd="uname -a",http-vuln-cve2014-3704.uri="/drupal" $target
    elif [ $vuln == 21 ]
    then
        nmap --script http-vuln-cve2014-8877 $target
    elif [ $vuln == 22 ]
    then
        nmap --script=http-vuln-cve2015-1427 --script-args command='ls' $target
    elif [ $vuln == 23 ]
    then
        nmap -sV --script http-vuln-cve2015-1635 $target
    elif [ $vuln == 24 ]
    then
        read -p " port : " port;
        nmap -p $port --script http-vuln-cve2017-5638 $target
    elif [ $vuln == 25 ]
    then
        read -p " port : " port;
        nmap -p $port --script http-vuln-cve2017-5689 $target
    elif [ $vuln == 26 ]
    then
        read -p " port : " port;
        nmap --script http-vuln-cve2017-8917 -p $port $target
    elif [ $vuln == 27 ]
    then
        nmap --script http-vuln-cve2017-1001000 $target
    elif [ $vuln == 28 ]
    then
        nmap $target -p $port --script=http-vuln-misfortune-cookie
    elif [ $vuln == 29 ]
    then
        read -p " port : " port;
        nmap -sV --script http-vuln-wnr1000-creds $target $port
    elif [ $vuln == 30 ]
    then
        nmap -sV --script mysql-vuln-cve2012-2122 $target
    elif [ $vuln == 31 ]
    then
        read -p " port : " port;
        nmap -sV --script=rdp-vuln-ms12-020 -p $port $target
    elif [ $vuln == 32 ]
    then
        read -p " port : " port;
        nmap --script=rmi-vuln-classloader -p $port $target
    elif [ $vuln == 33 ]
    then
        read -p " port : " port;
        nmap -p $port --script rsa-vuln-roca $target
    elif [ $vuln == 34 ]
    then
        read -p " port : " port;
        nmap --script=samba-vuln-cve-2012-1182 -p $port $target
    elif [ $vuln == 35 ]
    then
        read -p " port : " port;
        nmap --script smb-vuln-conficker -p $port $target
    elif [ $vuln == 36 ]
    then
        read -p " port : " port;
        nmap --script smb-vuln-cve-2017-7494 -p $port $target
    elif [ $vuln == 37 ]
    then
        read -p " port : " port;
        nmap --script smb-vuln-cve2009-3103 -p $port $target
    elif [ $vuln == 38 ]
    then
        read -p " port : " port;
        nmap --script smb-vuln-ms06-025 -p $port $target
    elif [ $vuln == 39 ]
    then
        read -p " port : " port;
        nmap --script smb-vuln-ms07-029 -p $port $target
    elif [ $vuln == 40 ]
    then
        read -p " port : " port;
        nmap --script smb-vuln-ms08-067 -p $port $target
    elif [ $vuln == 41 ]
    then
        read -p " port : " port;
        nmap  -p $port $target --script=smb-vuln-ms10-054 --script-args unsafe
    elif [ $vuln == 42 ]
    then
        read -p " port : " port;
        nmap  -p $port $target --script=smb-vuln-ms10-061
    elif [ $vuln == 43 ]
    then
        read -p " port : " port;
        nmap -p $port --script smb-vuln-ms17-010 $target
    elif [ $vuln == 44 ]
    then
        read -p " port : " port;
        nmap --script smb-vuln-regsvc-dos -p $port $target
    elif [ $vuln == 45 ]
    then
        read -p " username : " username;
        read -p " password : " password;
        read -p " port     : " port;
        nmap --script smb-vuln-webexec --script-args smbusername=$username,smbpass=$passdb -p $port $target
    elif [ $vuln == 46 ]
    then
        nmap -O --script smb2-vuln-uptime $target
    elif [ $vuln == 47 ]
    then
        read -p " port : " port;
        nmap --script=smtp-vuln-cve2010-4344 --script-args="smtp-vuln-cve2010-4344.exploit" -pT:$port $target
    elif [ $vuln == 48 ]
    then
        read -p " domain : " domain;
        read -p " port   : " port;
        nmap --script=smtp-vuln-cve2011-1720 --script-args="smtp.domain=$domain" -pT:$port $target
    elif [ $vuln == 49 ]
    then
        read -p " port   : " port;
        nmap --script=smtp-vuln-cve2011-1764 -pT:$port $target
    elif [ $vuln == 50 ]
    then
        nmap -sV --script vulners [--script-args mincvss=1] $target
    elif [ $vuln == 0 ]
    then
        scripts
    else
        vulnnse
    fi
}

function scripts(){
    banner
    echo -e ""
    echo -e "$yellow  [?]$white Script Category"
    echo -e ""
    echo -e "$cyan  01$red :$white Brute Script"
    echo -e "$cyan  02$red :$white Enumeration Script"
    echo -e "$cyan  03$red :$white Auth Script"
    echo -e "$cyan  04$red :$white Vulnerable Script"
    echo -e ""
    echo -e "$cyan  00$red :$white Back"
    echo -e ""
    read -p "Select one : " script;
    banner
    echo -e ""
    if [ $script == 1 ]
    then
        brutense
    elif [ $script == 2 ]
    then
        enumnse
    elif [ $script == 3 ]
    then
        authnse
    elif [ $script == 4 ]
    then
        vulnnse
    elif [ $script == 0 ]
    then
        menu
    else
        scripts
    fi
}

function menu(){
    banner
    echo -e ""
    echo -e "$yellow  [?]$white Scan type"
    echo -e ""
    echo -e "$cyan  01$red :$white Simple Scan"
    echo -e "$cyan  02$red :$white Fast Scan"
    echo -e "$cyan  03$red :$white Scan OS Version & Traceroute"
    echo -e "$cyan  04$red :$white Check Firewalls"
    echo -e "$cyan  05$red :$white Evading Firewalls"
    echo -e "$cyan  06$red :$white Broadcast Ping"
    echo -e "$cyan  07$red :$white NMAP Script"
    echo -e ""
    read -p " Select one : " menu;
    banner
    echo -e ""
    if [ $menu = 1 ]
    then
        nmap $target
    elif [ $menu = 2 ]
    then
        nmap -F $target
    elif [ $menu = 3 ]
    then
        nmap -sV -T4 -O --version-light 1 $target
    elif [ $menu = 4 ]
    then
        nmap -sA $target
    elif [ $menu = 5 ]
    then
        nmap -sS -P0 --spoof-mac 0 $target
    elif [ $menu = 6 ]
    then
        nmap --script broadcast-ping --script-args broadcast-ping.num_probe=5 $target
    elif [ $menu = 7 ]
    then
        scripts
    else
        menu
    fi
}

menu
