clear
bi='\033[34;1m' #biru
i='\033[32;1m' #ijo
pur='\033[35;1m' #purple
cy='\033[36;1m' #cyan
me='\033[31;1m' #merah
pu='\033[37;1m' #putih
ku='\033[33;1m' #kuning
mer='\033[41;97m' #Tepi
st='\033[0m' #Stop

echo -e "\033[31;1m    _    __________  _____________  __    "
echo -e "   | |  / /  _/ __ \/_  __/ ____/ |/ /    "
echo -e "   | | / // // /_/ / / / / __/  |   /     "
echo -e "\033[37;1m   | |/ // // _, _/ / / / /___ /   |      "
echo -e "   |___/___/_/ |_| /_/ /_____//_/|_|      "
echo -e "
╔══════════════════════════════════════╗
║Author  : MR.1557                     ║
║Github  : https://github.com/Aldi4321 ║
║Youtube : MR.1557                     ║
╚══════════════════════════════════════╝
  $bi          [$mer Jenis Virtex$st$bi]
\033[37;1m ╔═════════════════╝
\033[37;1m ╠═\033[32;1m▶\033[31;1m[\033[37;1m1\033[31;1m]\033[37;1mVIRUS 1
\033[37;1m ╠═\033[32;1m▶\033[31;1m[\033[37;1m2\033[31;1m]\033[37;1mVIRUS 2
\033[37;1m ╠═\033[32;1m▶\033[31;1m[\033[37;1m3\033[31;1m]\033[37;1mVIRUS 3
\033[37;1m ╠═\033[32;1m▶\033[31;1m[\033[37;1m4\033[31;1m]\033[37;1mVIRUS 4
\033[37;1m ╠═\033[32;1m▶\033[31;1m[\033[37;1m5\033[31;1m]\033[37;1mVIRUS 5
\033[37;1m ╠═\033[32;1m▶\033[31;1m[\033[37;1m6\033[31;1m]\033[37;1mVIRUS 6
\033[37;1m ╠═\033[32;1m▶\033[31;1m[\033[37;1m7\033[31;1m]\033[37;1mVIRUS 7
\033[37;1m ╠═\033[32;1m▶\033[31;1m[\033[37;1m00\033[31;1m]\033[37;1mExit"
echo -e -n "\033[37;1m ╚═\033[32;1m▶\033[37;1mchoose \033[32;1m> "
read pil
if [ $pil = "1" ]; then
echo -e "\033[37;1m ══\033[32;1m▶\033[37;1m Sedang Membuat virtex"
cp -f virus-1.txt /sdcard
sleep 6
echo -e "\033[37;1m ══\033[32;1m▶\033[37;1m selesai"
echo -e "\033[37;1m ══\033[32;1m▶\033[37;1m Virtex Berada di sdcard/virus-1.txt"
fi
if [ $pil = "2" ]; then
echo -e "\033[37;1m ══\033[32;1m▶\033[37;1m Sedang Membuat virtex"
cp -f virus2.txt /sdcard
sleep 6
echo -e "\033[37;1m ══\033[32;1m▶\033[37;1m selesai"
echo -e "\033[37;1m ══\033[32;1m▶\033[37;1m Virtex Berada di sdcard/virus2.txt"
fi
if [ $pil = "3" ]; then
echo -e "\033[37;1m ══\033[32;1m▶\033[37;1m Sedang Membuat virtex"
cp -f virus3.txt /sdcard
sleep 6
echo -e "\033[37;1m ══\033[32;1m▶\033[37;1m selesai"
echo -e "\033[37;1m ══\033[32;1m▶\033[37;1m Virtex Berada di sdcard/virus3.txt"
fi
if [ $pil = "4" ]; then
echo -e "\033[37;1m ══\033[32;1m▶\033[37;1m Sedang Membuat virtex"
cp -f virus4.txt /sdcard
sleep 6
echo -e "\033[37;1m ══\033[32;1m▶\033[37;1m selesai"
echo -e "\033[37;1m ══\033[32;1m▶\033[37;1m Virtex Berada di sdcard/virus4.txt"
fi
if [ $pil = "5" ]; then
echo -e "\033[37;1m ══\033[32;1m▶\033[37;1m Sedang Membuat virtex"
cp -f virus5.txt /sdcard
sleep 6
echo -e "\033[37;1m ══\033[32;1m▶\033[37;1m selesai"
echo -e "\033[37;1m ══\033[32;1m▶\033[37;1m Virtex Berada di sdcard/virus5.txt"
fi
if [ $pil = "6" ]; then
echo -e "\033[37;1m ══\033[32;1m▶\033[37;1m Sedang Membuat virtex"
cp -f virus6.txt /sdcard
sleep 6
echo -e "\033[37;1m ══\033[32;1m▶\033[37;1m selesai"
echo -e "\033[37;1m ══\033[32;1m▶\033[37;1m Virtex Berada di sdcard/virus6.txt"
fi
if [ $pil = "7" ]; then
echo -e "\033[37;1m ══\033[32;1m▶\033[37;1m Sedang Membuat virtex"
cp -f virus7.txt /sdcard
sleep 6
echo -e "\033[37;1m ══\033[32;1m▶\033[37;1m selesai"
echo -e "\033[37;1m ══\033[32;1m▶\033[37;1m Virtex Berada di sdcard/virus7.txt"
fi
if [ $pil = "0" ] || [ $pil = "00" ]; then
echo -e "\033[37;1m ══\033[32;1m▶\033[37;1m BAY KONTOL"
fi
