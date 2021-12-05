#!/bin/bash/
#######################################
# Bash script to install apps on a new system (Ubuntu)
# Written by @AnonyminHack5 from http://aamnah.com
#######################################

## Clear Screen ##
clear

## Update packages and Upgrade system
apt-get update -y

## Git ##
echo '###Installing Git..'
apt-get install git -y

## firefox ##
echo '###Installing firefox..'
pkg install firefox

## Requirements ##
echo '###Installing hydra...'
pkg install hydra

##Requirements##
echo -e "\e[1;31m Packages fully satisfied. Tool created by AnonyminHack5"


##Run tool##
echo -e "\e[1;32m Run python2 bughunter.py"