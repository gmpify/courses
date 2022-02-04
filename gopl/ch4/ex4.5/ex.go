package main

import "fmt"

func main() {
	s1 := []string{"a", "b"}
	fmt.Println("s1 before elim: ", s1)
	elim(&s1)
	fmt.Println("s1 after elim: ", s1)

	s2 := []string{"a", "a", "b", "a", "b", "c", "c", "a"}
	fmt.Println("s2 before elim: ", s2)
	elim(&s2)
	fmt.Println("s2 after elim: ", s2)
}

func elim(s *[]string) {
	w := 0
	for r := 0; r < len(*s); r++ {
		if (*s)[r] != (*s)[w] {
			w += 1
		}
		(*s)[w] = (*s)[r]
	}
	fmt.Println(*s)
	*s = (*s)[:w+1]
	fmt.Println(*s)
}
