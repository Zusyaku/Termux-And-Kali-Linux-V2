package nettools

import (
	"net"
	"net/url"

	recover_error "github.com/blackcrw/wafi/pkg/recover"
)

// IsURL :: This function will be used for URL validation
func NetTools_URLValidate(URL string) bool {
	defer recover_error.NetTools_URL()

	uri, err := url.ParseRequestURI(URL)

	if err != nil {
		panic(err)
	}

	switch uri.Scheme {
	case "http":
	case "https":
	default:
		panic("Invalid scheme")
	}

	return true
}

func GetHost(URL string) (string, error) {
	uri, err := url.ParseRequestURI(URL)

	if err != nil {
		return "", err
	}

	_, err = net.LookupHost(uri.Host)

	if err != nil {
		return "", err
	}

	return uri.Host, nil
}
