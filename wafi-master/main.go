package main

import (
	"runtime"

	"github.com/blackcrw/wafi/cli"
)

func main() {
	runtime.GOMAXPROCS(runtime.NumCPU())

	cli.Execute()
}
