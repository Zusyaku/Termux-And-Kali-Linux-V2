package socks

import (
	"encoding/binary"
	"fmt"
	"io"
	//"log"
	"net"
)

/*
socks4 protocol

request
byte | 0  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | ...  |
     |0x04|cmd| port  |     ip        |  user\0  |

reply
byte | 0  |  1   | 2 | 3 | 4 | 5 | 6 | 7|
     |0x00|status|       |              |


socks4a protocol

request
byte | 0  | 1 | 2 | 3 |4 | 5 | 6 | 7 | 8 | ... |...     |
     |0x04|cmd| port  |  0.0.0.x     |  user\0 |domain\0|

reply
byte | 0  |  1  | 2 | 3 | 4 | 5 | 6| 7 |
	 |0x00|staus| port  |    ip        |

*/
type socks4Conn struct {
	serverConn net.Conn
	clientConn net.Conn
	dial       DialFunc
}

func (s4 *socks4Conn) Serve(b []byte, n int) (err error) {
	defer s4.Close()

	if err = s4.processRequest(b, n); err != nil {
		//log.Println(err)
		return
	}
	return
}

func (s4 *socks4Conn) Close() {
	if s4.clientConn != nil {
		s4.clientConn.Close()
	}

	if s4.serverConn != nil {
		s4.serverConn.Close()
	}
}

func (s4 *socks4Conn) processRequest(buf []byte, n int) (err error) {
	// process command and target here

	if n < 8 {
		n1, err := io.ReadAtLeast(s4.clientConn, buf[n:], 8-n)
		if err != nil {
			return err
		}
		n += n1
	}

	buf = buf[1:n]

	// command only support connect
	if buf[0] != cmdConnect {
		return fmt.Errorf("error command %d", buf[0])
	}

	// get port
	port := binary.BigEndian.Uint16(buf[1:3])

	// get ip
	ip := net.IP(buf[3:7])

	// NULL-terminated user string
	// jump to NULL character
	var j int
	for j = 7; j < n-1; j++ {
		if buf[j] == 0x00 {
			break
		}
	}

	host := ip.String()

	// socks4a
	// 0.0.0.x
	if ip[0] == 0x00 && ip[1] == 0x00 && ip[2] == 0x00 && ip[3] != 0x00 {
		j++
		var i = j

		// jump to the end of hostname
		for j = i; j < n-1; j++ {
			if buf[j] == 0x00 {
				break
			}
		}
		host = string(buf[i:j])
	}

	target := net.JoinHostPort(host, fmt.Sprintf("%d", port))

	//log.Printf("connecting to %s\r\n", target)

	// connect to the target
	s4.serverConn, err = s4.dial("tcp", target)
	if err != nil {
		// connection failed
		s4.clientConn.Write([]byte{0x00, 0x5b, 0x01, 0x02, 0x00, 0x00, 0x00, 0x00})
		return err
	}

	// connection success
	s4.clientConn.Write([]byte{0x00, 0x5a, 0x01, 0x02, 0x00, 0x00, 0x00, 0x00})

	// enter data exchange
	forward(s4.clientConn, s4.serverConn)

	return nil
}
