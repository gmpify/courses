package main

import (
	"fmt"
)

func main() {
	//!+slice
	s := []int{0, 1, 2, 3, 4, 5}
	// Rotate s left by two positions.
	s = rotate(s, 2)
	fmt.Println(s) // "[2 3 4 5 0 1]"
	//!-slice
}

func rotate(s []int, n int) []int {
	r := s[n:]
	r = append(r, s[:n]...)
	return r
}
