socks-server
============

this is a socks server example.

run it

    go run server.go

test it

    curl --socks4 127.0.0.1:1080 http://www.google.com/
    curl --socks4a 127.0.0.1:1080 http://www.google.com/
    curl --socks5 127.0.0.1:1080 http://www.google.com/
    curl --socks5-hostname 127.0.0.1:1080 http://www.google.com/
