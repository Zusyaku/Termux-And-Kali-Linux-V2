package recover_error

import (
	"fmt"
	"log"
)

func NetTools_URL() {
	if recovered := recover(); recovered != nil { var char = fmt.Sprintf("%s", recovered); log.Fatalln(char) }
}
