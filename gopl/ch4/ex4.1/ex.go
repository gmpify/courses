package main

import (
	"crypto/sha256"
	"fmt"
	"os"
)

func main() {
	if len(os.Args) < 3 {
		fmt.Println("Must provide at least 2 args")
		os.Exit(1)
	}

	s1 := sha256.Sum256([]byte(os.Args[1]))
	s2 := sha256.Sum256([]byte(os.Args[2]))

	fmt.Println("Different bits:", calculateDifferentBits(s1, s2))
}

func calculateDifferentBits(s1, s2 [32]uint8) int {
	var r int

	for i := 0; i < 32; i++ {
		b1 := fmt.Sprintf("%08b", s1[i])
		b2 := fmt.Sprintf("%08b", s2[i])
		for j := 0; j < 8; j++ {
			if b1[j] != b2[j] {
				r += 1
			}
		}
	}

	return r
}
