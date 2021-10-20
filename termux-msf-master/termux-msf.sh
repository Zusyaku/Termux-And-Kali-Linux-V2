#!usr/bin/bash
clear
echo "



















































(============================)
     Metasploit Installer
        By: Cr4sH CoD3
 From: Blood Security Hackers
(============================)



"

echo "Updating Your System and Installing Dependencies..."
sleep 3
clear

apt update
echo "
Updated!"
sleep 2
clear

apt upgrade -y
sleep 2
echo "
Upgraded!"
sleep 2
clear

apt install autoconf bison clang coreutils curl findutils git apr apr-util libffi-dev libgmp-dev libpcap-dev postgresql-dev readline-dev libsqlite-dev openssl-dev libtool libxml2-dev libxslt-dev ncurses-dev pkg-config postgresql-contrib wget make ruby-dev libgrpc-dev termux-tools ncurses-utils ncurses
echo "
Depedencies Installed!"
sleep 2
clear
echo "



















"

echo "Cloning Metasploit Framework..."
git clone https://github.com/timwr/metasploit-framework --depth 1
cd metasploit-framework
echo "
cloned!"
sleep 2
clear
echo "



















"

echo "Installing Required Gems..."
gem install bundler
gem install nokogiri -- --use-system-libraries
cd $HOME
gem unpack network_interface
cd network_interface-0.0.1
sed 's|git ls-files|find -type f|' -i network_interface.gemspec
curl -L https://wiki.termux.com/images/6/6b/Netifaces.patch -o netifaces.patch
patch -p1 < netifaces.patch
gem build network_interface.gemspec
gem install network_interface-0.0.1.gem
cd ..
rm -r network_interface-0.0.1
cd metasploit-framework
sed 's|grpc (.*|grpc (1.4.1)|g' -i Gemfile.lock
gem unpack grpc -v 1.4.1
cd grpc-1.4.1
curl -LO https://raw.githubusercontent.com/grpc/grpc/v1.4.1/grpc.gemspec
curl -L https://raw.githubusercontent.com/Hax4us/Hax4us.github.io/master/extconf.patch
patch -p1 < extconf.patch
gem build grpc.gemspec
gem install grpc-1.4.1.gem
cd ..
rm -r grpc-1.4.1
echo "
Gems Installed!"
sleep 2
clear
echo "



















"

echo "Unpacking Bundle..."
bundle -j5
echo "Bundles Successfully Installed!"
sleep 2
clear
echo "



















"

echo "Performing Fix-Shebang..."
$PREFIX/bin/find -type f -executable -exec termux-fix-shebang \{\} \;
echo"
You can now run the metasploit by ./msfconsole"
