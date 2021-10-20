#!/bin/bash

# WordGen
# By Niirmaal Twaatii

echo "--------- Inputs ---------"
read -p "FirstName: " fn
read -p "LastName: " ln
read -p "Age: " ag
read -p "Birth Year: " by
read -p "Birth Month (eg.January): " bm
read -p "Birth Day: " bd
echo "--------------------------"
echo ""

echo "$fn$ln$ag"
echo "$fn$ag"
echo "$ln$ag"
echo "$fn$ln$by"
echo "$fn$ln$bd"
echo "$fn$ln$by$bd"
echo "$fn$by"
echo "$fn$bd"
echo "$ln$by"
echo "$ln$bd"

echo ""


