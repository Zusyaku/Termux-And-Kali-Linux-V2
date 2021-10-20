package socks

import (
	"errors"
	"fmt"
	"io"
	//"log"
	"net"
	//"strconv"
	"encoding/binary"
)

/*
socks5 protocol

initial

byte | 0  |   1    | 2 | ...... | n |
     |0x05|num auth|  auth methods  |


reply

byte | 0  |  1  |
     |0x05| auth|


username/password auth request

byte | 0  |  1         |          |     1 byte   |          |
     |0x01|username_len| username | password_len | password |

username/password auth reponse

byte | 0  | 1    |
     |0x01|status|

request

byte | 0  | 1 | 2  |   3    | 4 | .. | n-2 | n-1| n |
     |0x05|cmd|0x00|addrtype|      addr    |  port  |

response
byte |0   |  1   | 2  |   3    | 4 | .. | n-2 | n-1 | n |
     |0x05|status|0x00|addrtype|     addr     |  port   |

*/

// Socks5AuthRequired means socks5 server need auth or not

type socks5Conn struct {
	//addr        string
	clientConn net.Conn
	serverConn net.Conn
	dial       DialFunc
	auth       AuthService
}

func (s5 *socks5Conn) Serve(b []byte, n int) (err error) {
	defer s5.Close()

	if err = s5.handshake(b, n); err != nil {
		//log.Println(err)
		return
	}

	if err = s5.processRequest(); err != nil {
		//log.Println(err)
		return
	}
	return
}

func (s5 *socks5Conn) handshake(buf []byte, n int) (err error) {

	// read auth methods
	if n < 2 {
		n1, err := io.ReadAtLeast(s5.clientConn, buf[1:], 1)
		if err != nil {
			return err
		}
		n += n1
	}

	l := int(buf[1])
	if n != (l + 2) {
		// read remains data
		n1, err := io.ReadFull(s5.clientConn, buf[n:l+2+1])
		if err != nil {
			return err
		}
		n += n1
	}

	if s5.auth == nil {
		// no auth required
		s5.clientConn.Write([]byte{0x05, 0x00})
		return nil
	}

	hasPassAuth := false
	var passAuth byte = 0x02

	// check auth method
	// only password(0x02) supported
	for i := 2; i < n; i++ {
		if buf[i] == passAuth {
			hasPassAuth = true
			break
		}
	}

	if !hasPassAuth {
		s5.clientConn.Write([]byte{0x05, 0xff})
		return errors.New("no supported auth method")
	}

	err = s5.passwordAuth()
	return err
}

func (s5 *socks5Conn) passwordAuth() error {
	buf := make([]byte, 32)

	// username/password required
	s5.clientConn.Write([]byte{0x05, 0x02})
	n, err := io.ReadAtLeast(s5.clientConn, buf, 2)
	if err != nil {
		return err
	}

	//log.Printf("%+v", buf[:n])

	// check auth version
	if buf[0] != 0x01 {
		return errors.New("unsupported auth version")
	}

	usernameLen := int(buf[1])

	p0 := 2
	p1 := p0 + usernameLen

	if n < p1 {
		n1, err := s5.clientConn.Read(buf[n:])
		if err != nil {
			return err
		}
		n += n1
	}

	username := buf[p0:p1]
	passwordLen := int(buf[p1])

	p3 := p1 + 1
	p4 := p3 + passwordLen

	if n < p4 {
		n1, err := s5.clientConn.Read(buf[n:])
		if err != nil {
			return err
		}
		n += n1
	}

	password := buf[p3:p4]

	// log.Printf("get username: %s, password: %s", username, password)

	if s5.auth != nil {
		ret := s5.auth.Authenticate(
			string(username), string(password),
			s5.clientConn.RemoteAddr())
		if ret {
			s5.clientConn.Write([]byte{0x01, 0x00})
			return nil
		}
		s5.clientConn.Write([]byte{0x01, 0x01})

		return errors.New("access denied")
	}

	return errors.New("no auth method")
}

func (s5 *socks5Conn) processRequest() error {
	buf := make([]byte, 258)

	// read header
	n, err := io.ReadAtLeast(s5.clientConn, buf, 10)
	if err != nil {
		return err
	}

	if buf[0] != socks5Version {
		return fmt.Errorf("error version %d", buf[0])
	}

	// command only support connect
	if buf[1] != cmdConnect {
		return fmt.Errorf("unsupported command %d", buf[1])
	}

	hlen := 0   // target address length
	host := ""  // target address
	msglen := 0 // header length

	switch buf[3] {
	case addrTypeIPv4:
		hlen = 4
	case addrTypeDomain:
		hlen = int(buf[4]) + 1
	case addrTypeIPv6:
		hlen = 16
	}

	msglen = 6 + hlen

	if n < msglen {
		// read remains header
		_, err := io.ReadFull(s5.clientConn, buf[n:msglen])
		if err != nil {
			return err
		}
	}

	// get target address
	addr := buf[4 : 4+hlen]
	if buf[3] == addrTypeDomain {
		host = string(addr[1:])
	} else {
		host = net.IP(addr).String()
	}

	// get target port
	port := binary.BigEndian.Uint16(buf[msglen-2 : msglen])

	// target address
	target := net.JoinHostPort(host, fmt.Sprintf("%d", port))

	//log.Printf("connecing to %s\r\n", target)

	// connect to the target
	s5.serverConn, err = s5.dial("tcp", target)
	if err != nil {
		// connection failed
		s5.clientConn.Write([]byte{0x05, 0x01, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x01, 0x01})
		return err
	}

	// connection success
	s5.clientConn.Write([]byte{0x05, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x01, 0x01})

	// enter data exchange
	forward(s5.clientConn, s5.serverConn)

	return nil
}

func (s5 *socks5Conn) Close() {
	if s5.serverConn != nil {
		s5.serverConn.Close()
	}
	if s5.clientConn != nil {
		s5.clientConn.Close()
	}
}
