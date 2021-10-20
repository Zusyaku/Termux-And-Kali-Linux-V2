package socks

import (
	"io"
	"log"
	"net"
	"time"
)

const (
	socks4Version  = 0x04
	socks5Version  = 0x05
	cmdConnect     = 0x01
	addrTypeIPv4   = 0x01
	addrTypeDomain = 0x03
	addrTypeIPv6   = 0x04
)

// DialFunc the function dial to remote
type DialFunc func(network, addr string) (net.Conn, error)

// Conn present a socks connection
type Conn struct {
	net.Conn
	// the function to dial to upstream server
	// when nil, use net.Dial
	Dial DialFunc
	// Auth the auth service to authenticate the user for socks5
	Auth AuthService
}

// Serve serve the client
func (s *Conn) Serve() {
	buf := make([]byte, 512)

	// read version
	n, err := io.ReadAtLeast(s.Conn, buf, 1)
	if err != nil {
		log.Println(err)
		return
	}

	dial := s.Dial
	if s.Dial == nil {
		d := net.Dialer{Timeout: 10 * time.Second}
		dial = d.Dial
	}

	switch buf[0] {
	case socks4Version:
		s4 := socks4Conn{clientConn: s.Conn, dial: dial}
		s4.Serve(buf, n)
	case socks5Version:
		s5 := socks5Conn{clientConn: s.Conn, dial: dial, auth: s.Auth}
		s5.Serve(buf, n)
	default:
		log.Printf("unknown socks version 0x%x", buf[0])
		s.Conn.Close()
	}
}

func forward(c1, c2 io.ReadWriter) {

	c := make(chan struct{}, 2)

	go func() {
		io.Copy(c1, c2)
		c <- struct{}{}
	}()

	go func() {
		io.Copy(c2, c1)
		c <- struct{}{}
	}()

	<-c
}
