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
    echo -e ""
    echo -e "$red    フ$yellowァ$greenッ$cyanク$okegreenユ$lightgreenー$white"
    echo -e ""
}

# Menu
main(){
    banner
    echo -e ""
    echo -e "$cyan  01$red :$white Payload Generator"
    echo -e "$cyan  02$red :$white Brute Force Attack"
    echo -e "$cyan  03$red :$white DNS Queries"
    echo -e "$cyan  04$red :$white IP Tools"
    echo -e "$cyan  05$red :$white Web Tools"
    echo -e "$cyan  06$red :$white Nmap Helper"
    echo -e ""
    maincmd
}

payloadmenu(){
    banner
    echo -e ""
    echo -e "$cyan  01$red :$white Windows Payload"
    echo -e "$cyan  02$red :$white Android Payload"
    echo -e "$cyan  03$red :$white Linux Payload"
    echo -e "$cyan  04$red :$white Mac Payload"
    echo -e "$cyan  05$red :$white iOS Payload"
    echo -e ""
    echo -e "$cyan  00$red :$white Back"
    echo -e ""
    payloadcmd
}

brutemenu(){
    banner
    echo -e ""
    echo -e "$cyan  01$red :$white SSH Brute"
    echo -e "$cyan  02$red :$white Facebook Account Brute"
    echo -e ""
    echo -e "$cyan  00$red :$white Back"
    echo -e ""
    brutecmd
}

dnsmenu(){
    banner
    echo -e ""
    echo -e "$cyan  01$red :$white DNS Lookup"
    echo -e "$cyan  02$red :$white Reverse DNS Lookup"
    echo -e "$cyan  03$red :$white DNS Host Records"
    echo -e "$cyan  04$red :$white Shared DNS Servers"
    echo -e "$cyan  05$red :$white DNS Digging"
    echo -e ""
    echo -e "$cyan  00$red :$white Back"
    echo -e ""
    dnscmd

}

ipmenu(){
    banner
    echo -e ""
    echo -e "$cyan  01$red :$white GeoIP Location Lookup"
    echo -e "$cyan  02$red :$white Reverse IP Lookup"
    echo -e "$cyan  03$red :$white Subnet Lookup"
    echo -e "$cyan  04$red :$white Autonomous System Lookup"
    echo -e "$cyan  05$red :$white Banner Grabbing"
    echo -e ""
    echo -e "$cyan  00$red :$white Back"
    echo -e ""
    ipcmd
}

webmenu(){
    banner
    echo -e ""
    echo -e "$cyan  01$red :$white HTTP Header Check"
    echo -e "$cyan  02$red :$white Extract Links From Page"
    echo -e "$cyan  03$red :$white Reverse Google Analytics Lookup"
    echo -e "$cyan  04$red :$white Subdomain Finder"
    echo -e "$cyan  05$red :$white Directory Brute"
    echo -e "$cyan  06$red :$white Admin Login Finder"
    echo -e ""
    echo -e "$cyan  00$red :$white Back"
    echo -e ""
    webcmd
}

# Payload
windowspayload(){
    banner
    echo -e ""
    echo -e "$cyan  01$red :$white Simple Executable File Payload"
    echo -e "$cyan  02$red :$white Installer Payload"
    echo -e ""
    echo -e "$cyan  00$red :$white Back"
    echo -e ""
    read -p " payload/windows # " act;
    if [ $act = 1 ]
    then
        banner
        bash tools/payload/windows/exe
    elif [ $act = 2 ]
    then
        banner
        bash tools/payload/windows/installer
    elif [ $act = 0 ]
    then
        payloadmenu
    else
        windowspayload
    fi
}

androidpayload(){
    banner
    echo -e ""
    echo -e "$cyan  01$red :$white Simple .APK File Payload"
    echo -e ""
    echo -e "$cyan  00$red :$white Back"
    echo -e ""
    read -p " payload/android # " act;
    if [ $act = 1 ]
    then
        banner
        bash tools/payload/android/apk
    elif [ $act = 0 ]
    then
        payloadmenu
    else
        androidpayload
    fi
}

linuxpayload(){
    banner
    echo -e ""
    echo -e "$cyan  01$red :$white Reverse TCP"
    echo -e ""
    echo -e "$cyan  00$red :$white Back"
    echo -e ""
    read -p " payload/linux # " act;
    if [ $act = 1 ]
    then
        banner
        bash tools/payload/linux/reverse_tcp
    elif [ $act = 0 ]
    then
        payloadmenu
    else
        linuxpayload
    fi
}

macpayload(){
    banner
    echo -e ""
    echo -e "$cyan  01$red :$white Reverse TCP"
    echo -e "$cyan  02$red :$white Python Payload"
    echo -e ""
    echo -e "$cyan  00$red :$white Back"
    echo -e ""
    read -p " payload/mac # " act;
    if [ $act = 1 ]
    then
        banner
        bash tools/payload/mac/reverse_tcp
    elif [ $act = 2 ]
    then
        banner
        bash tools/payload/mac/python
    elif [ $act = 0 ]
    then
        payloadmenu
    else
        macpayload
    fi
}

iospayload(){
    banner
    echo -e ""
    echo -e "$cyan  01$red :$white Reverse TCP (execute via ssh)"
    echo -e "$cyan  02$red :$white Embedded iOS Package"
    echo -e ""
    echo -e "$cyan  00$red :$white Back"
    echo -e ""
    read -p " payload/ios # " act;
    if [ $act = 1 ]
    then
        banner
        bash tools/payload/ios/reverse_tcp
    elif [ $act = 2 ]
    then
        banner
        bash tools/payload/ios/arcane
    elif [ $act = 0 ]
    then
        payloadmenu
    else
        iospayload
    fi
}

# List
maincmd(){
    echo -e "$white"
    read -p " ~ # " act;
    if [ $act = 1 ]
    then
        banner
        payloadmenu
    elif [ $act = 2 ]
    then
        banner
        brutemenu
    elif [ $act = 3 ]
    then
        banner
        dnsmenu
    elif [ $act = 4 ]
    then
        banner
        ipmenu
    elif [ $act = 5 ]
    then
        banner
        webmenu
    elif [ $act = 6 ]
    then
        banner
        sudo bash tools/nmap/nmap
    else
        main
    fi
}

brutecmd(){
    echo -e "$white"
    read -p " brute # " act;
    if [ $act = 1 ]
    then
        banner
        python3 tools/brute/ssh
    elif [ $act = 2 ]
    then
        banner
        python3 tools/brute/facebook
    elif [ $act = 0 ]
    then
        banner
        main
    else
        brutemenu
    fi
}

payloadcmd(){
    echo -e "$white"
    read -p " payload # " act;
    if [ $act = 1 ]
    then
        banner
        windowspayload
    elif [ $act = 2 ]
    then
        banner
        androidpayload
    elif [ $act = 3 ]
    then
        banner
        linuxpayload
    elif [ $act = 4 ]
    then
        banner
        macpayload
    elif [ $act = 5 ]
    then
        banner
        iospayload
    elif [ $act = 0 ]
    then
        banner
        main
    else
        payloadmenu
    fi
}

dnscmd(){
    echo -e "$white"
    read -p " dns # " act;
    if [ $act = 1 ]
    then
        bash tools/dns/dnslookup
    elif [ $act = 2 ]
    then
        bash tools/dns/reversednslookup
    elif [ $act = 3 ]
    then
        bash tools/dns/dnshost
    elif [ $act = 4 ]
    then
        bash tools/dns/shareddns
    elif [ $act = 5 ]
    then
        bash tools/dns/dnsdigger
    elif [ $act = 0 ]
    then
        main
    else
        dnsmenu
    fi
}

ipcmd(){
    echo -e "$white"
    read -p " ip # " act;
    if [ $act = 1 ]
    then
        bash tools/ip/geoip
    elif [ $act = 2 ]
    then
        bash tools/ip/reverseiplookup
    elif [ $act = 3 ]
    then
        bash tools/ip/subnetlookup
    elif [ $act = 4 ]
    then
        bash tools/ip/anslookup
    elif [ $act = 5 ]
    then
        bash tools/ip/bannergrabber
    elif [ $act = 0 ]
    then
        main
    else
        ipmenu
    fi
}

webcmd(){
    echo -e "$white"
    read -p " web # " act;
    if [ $act = 1 ]
    then
        bash tools/web/httpcheck
    elif [ $act = 2 ]
    then
        bash tools/web/extractlinks
    elif [ $act = 3 ]
    then
        bash tools/web/analyticslookup
    elif [ $act = 4 ]
    then
        php tools/web/subdoscan
    elif [ $act = 5 ]
    then
        php tools/web/dirbrute
    elif [ $act = 6 ]
    then
        php tools/web/adfinder
    elif [ $act = 0 ]
    then
        main
    else
        webmenu
    fi
}

banner
main
