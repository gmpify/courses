package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	counts := make(map[string][]string)
	files := os.Args[1:]
	if len(files) == 0 {
		fmt.Fprintln(os.Stderr, "please supply files")
		os.Exit(-1)
	}

	for _, arg := range files {
		f, err := os.Open(arg)
		if err != nil {
			fmt.Fprintf(os.Stderr, "dup2: %v\n", err)
			continue
		}
		countLines(f, counts, arg)
		f.Close()
	}

	for line, n := range counts {
		if len(n) > 1 {
			fmt.Printf("%d\t%s\t%v\n", len(n), line, n)
		}
	}
}

func countLines(f *os.File, counts map[string][]string, fileName string) {
	input := bufio.NewScanner(f)
	for input.Scan() {
		line := input.Text()
		counts[line] = append(counts[line], fileName)
	}
}
