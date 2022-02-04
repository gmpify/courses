package main

import (
	"fmt"
	"unicode"
)

func main() {
	s1 := []byte("  aa bbbb  cc d      e   fff")
	fmt.Printf("s1 before elim: %s\n", s1)
	elim(&s1)
	fmt.Printf("s1 after elim: %s\n", s1)
}

func elim(s *[]byte) {
	w := 0
	for r := 1; r < len(*s); r++ {
		if !unicode.IsSpace(rune((*s)[r])) || !unicode.IsSpace(rune((*s)[w])) {
			w += 1
		}
		(*s)[w] = (*s)[r]
	}
	*s = (*s)[:w+1]
}
