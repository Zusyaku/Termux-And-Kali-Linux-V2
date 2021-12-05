#!/bin/bash
echo "# Simple Massive Record Lookup";
echo "# usage: bash lookup.sh A target.txt";

type=$1;
file=$2;
while read bulk;
do
    host -W 3 -t $type "$bulk"
done < "$file"
exit 0
