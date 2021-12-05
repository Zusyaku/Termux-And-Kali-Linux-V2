#!/bin/bash
echo "# Simple Zone-H Mass Poster";
echo "# usage: bash mass.sh target.txt";
echo "please change defacer name befure run this script";
defacer=ogatarina
domainlist=$1
while IFS= read domain
do
  curl --silent --output /dev/null --request POST 'http://www.zone-h.org/notify/single' --data "defacer=$defacer&domain1=$domain&hackmode=1&reason=1"
done < $domainlist
echo "Done. Check http://www.zone-h.org/archive/published=0/notifier=$defacer"
exit 0
