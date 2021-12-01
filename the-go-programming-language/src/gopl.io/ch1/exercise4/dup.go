package main

import (
  "bufio"
  "fmt"
  "os"
)

func main() {
  counts := make(map[string]int)
  filesWithDup := make(map[string][]string)
  files := os.Args[1:]
  if len(files) == 0 {
    countLines(os.Stdin, counts, filesWithDup)
  } else {
    for _, arg := range files {
      f, err := os.Open(arg)
      if err != nil {
        fmt.Fprintf(os.Stderr, "dup2: %v\n", err)
        continue
      }
      countLines(f, counts, filesWithDup)
      f.Close()
    }
  }
  for line, n := range counts {
    if n > 1 {
      fmt.Printf("%d\t%s\t%v\n", n, line, filesWithDup[line])
    }
  }
}
func countLines(f *os.File, counts map[string]int, filesWithDup map[string][]string) {
  input := bufio.NewScanner(f)
  for input.Scan() {
    text := input.Text()
    counts[text]++
    exists := false
    for _, line := range filesWithDup[text] {
      if line == f.Name() {
        exists = true
        break
      }
    }
    if !exists {
      filesWithDup[text] = append(filesWithDup[text], f.Name())
    }
  }
}
