#!/bin/sh
clear
echo "   ____          __  _ ___     ___  __ ";
echo "  / __/__  ___  / /_(_) _/_ __/ _ \/ / ";
echo " _\ \/ _ \/ _ \/ __/ / _/ // / // / /__";
echo "/___/ .__/\___/\__/_/_/ \_, /____/____/";
echo "   /_/                 /___/           ";
echo ""
echo "updating repo"
echo ""
apt update >/dev/null 2>&1
echo "Checking Package..."
echo ""
sleep 1
echo "Checking Python..."
echo ""
sleep 1
if which python >/dev/null; then
    echo "python found"
    else
    echo "python not found"
    sleep 1
    echo "installing python"
    apt install python -y > /dev/null 2>&1
fi
sleep 1
echo ""
echo "Checking ffmpeg..."
echo ""
sleep 1
if which ffmpeg >/dev/null; then
    echo "ffmpeg found"
    else 
    echo "ffmpeg not found"
    echo "installing ffmpeg..."
    apt install ffmpeg -y > /dev/null 2>&1
fi
sleep 1
echo ""
echo "Checking git..."
if which git >/dev/null; then
    echo "git found"
    else
    echo "git not found"
    sleep 1
    echo "installing git..."
    apt install git -y > /dev/null 2>&1 
fi
echo ""
sleep 1
echo "Installing script..."
pip install spotdl > /dev/null 2>&1
mv spotifydl.sh spotifydl
mv spotifydl $PREFIX/bin
chmod +x $PREFIX/bin/spotifydl
echo ""
echo "Installl selesai, untuk menjalankan ketik spotifydl"
cd 
rm -rf spotifydl
