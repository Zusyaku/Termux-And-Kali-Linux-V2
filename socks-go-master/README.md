socks-go
=======

A socks proxy protocol implemented by golang, support socks 4, 4a and 5.

Only CONNECT command support now.

usage example
=============

server:

    // listen 1080 and act as socks server
    // support socks4, socks4a and socks5

    package main

    import (
        socks "github.com/fangdingjun/socks-go"
        "log"
        "net"
        "time"
    )

    func main() {
        conn, err := net.Listen("tcp", ":1080")
        if err != nil {
            log.Fatal(err)
        }

        for {
            c, err := conn.Accept()
            if err != nil {
                log.Println(err)
                continue
            }

            log.Printf("connected from %s", c.RemoteAddr())

            d := net.Dialer{Timeout: 10 * time.Second}
            s := socks.Conn{Conn: c, Dial: d.Dial}
            go s.Serve()
        }
    }




client:

    // visit https://www.google.com through socks proxy server

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
