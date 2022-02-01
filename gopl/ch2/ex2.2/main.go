package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	for _, n := range os.Args[1:] {
		num, _ := strconv.Atoi(n)
		displayConversions(num)
	}
}

func displayConversions(n int) {
	f := Fahrenheit(n)
	c := Celsius(n)
	fmt.Printf("Temperature\n%s = %s, %s = %s\n\n", f, FToC(f), c, CToF(c))

	fe := Feet(n)
	m := Meter(n)
	fmt.Printf("Lenght\n%s = %s, %s = %s\n\n", fe, FToM(fe), m, MToF(m))
}
