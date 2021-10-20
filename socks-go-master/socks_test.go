package socks

import (
	//"bytes"
	//"fmt"
	"errors"
	"net"
	"testing"
)

func TestSocks(t *testing.T) {
	if err := testSocks(t, "u1", "p1", true); err != nil {
		t.Error(err)
	}
	if err := testSocks(t, "", "", false); err != nil {
		t.Error(err)
	}
	if err := testSocks(t, "u3", "p3", true); err != nil {
		t.Error(err)
	}

	if err := testSocks(t, "u3", "p3", false); err != nil {
		t.Log(err)
	} else {
		t.Error("password not active")
	}

	if err := testSocks(t, "u3", "", false); err != nil {
		t.Log(err)
	} else {
		t.Error("password not active")
	}
}

func testSocks(t *testing.T, user, pass string, auth bool) error {
	l, err := net.Listen("tcp", "127.0.0.1:0")
	if err != nil {
		return err
	}
	defer l.Close()

	l1, err := net.Listen("tcp", "127.0.0.1:0")
	if err != nil {
		return err
	}
	defer l1.Close()

	addr := l.Addr().String()

	addr1 := l1.Addr()

	go func() {
		conn, err := l.Accept()
		if err != nil {
			return
		}
		t.Logf("connected from %s", conn.RemoteAddr())
		s := Conn{Conn: conn, Auth: &passwordAuth{user, pass}}
		s.Serve()
	}()

	go func() {
		conn, err := l1.Accept()
		if err != nil {
			return
		}
		t.Logf("server 2 accept connection from %s", conn.RemoteAddr())
		defer conn.Close()
		buf := make([]byte, 512)
		n, err := conn.Read(buf)
		if err != nil {
			return
		}
		conn.Write(buf[:n])
	}()

	c, err := net.Dial("tcp", addr)
	if err != nil {
		return err
	}

	defer c.Close()
	var sc Client
	if auth {
		sc = Client{Conn: c, Username: user, Password: pass}
	} else {
		sc = Client{Conn: c}
	}
	if err = sc.Connect("localhost", uint16(addr1.(*net.TCPAddr).Port)); err != nil {
		return err
	}

	t.Logf("connect success")

	str := "hello1234"
	buf := make([]byte, 512)

	if _, err := sc.Write([]byte(str)); err != nil {
		return err
	}

	n, err := sc.Read(buf)
	if err != nil {
		return err
	}

	if string(buf[:n]) != str {
		return errors.New("socks test failed")
	}
	return nil
}
