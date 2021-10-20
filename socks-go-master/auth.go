package socks

import "net"

// AuthService the service to authenticate the user for socks5
type AuthService interface {
	// Authenticate auth the user
	// return true means ok, false means no access
	Authenticate(username, password string, addr net.Addr) bool
}

// default password auth service
type passwordAuth struct {
	username string
	password string
}

func (pa *passwordAuth) Authenticate(username, password string, addr net.Addr) bool {
	if username == pa.username && password == pa.password {
		return true
	}
	return false
}
