package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Println("1", comma("1"))
	fmt.Println("1000", comma("1000"))
	fmt.Println("100000", comma("100000"))
}

func comma(s string) string {
	var buf bytes.Buffer

	buf.WriteString(s[:(len(s) % 3)])

	for i := len(s) % 3; i < len(s); i += 3 {
		if i != 0 {
			buf.WriteString(",")
		}
		buf.WriteString(s[i:i+3])
	}

	return buf.String()
}
