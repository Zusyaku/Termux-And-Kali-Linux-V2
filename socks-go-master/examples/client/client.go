package main

import (
	"bufio"
	"crypto/tls"
	socks "github.com/fangdingjun/socks-go"
	"io"
	"log"
	"net"
	"net/http"
	"os"
)

func main() {
	// connect to socks server
	c, err := net.Dial("tcp", "localhost:1080")
	if err != nil {
		log.Fatal(err)
	}
	defer c.Close()

	sc := &socks.Client{Conn: c}

	// connect to remote server
	if err := sc.Connect("www.google.com", 443); err != nil {
		log.Fatal(err)
	}

	// tls
	conn := tls.Client(sc, &tls.Config{ServerName: "www.google.com"})
	if err := conn.Handshake(); err != nil {
		log.Fatal(err)
	}

	// send http request
	req, err := http.NewRequest("GET", "https://www.google.com/", nil)
	if err != nil {
		log.Fatal(err)
	}
	req.Write(conn)

	bio := bufio.NewReader(conn)

	// read response
	res, err := http.ReadResponse(bio, req)
	if err != nil {
		log.Fatal(err)
	}
	defer res.Body.Close()

	io.Copy(os.Stdout, res.Body)
}
