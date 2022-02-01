package main

import "fmt"

type Meter float64
type Feet float64

func (m Meter) String() string { return fmt.Sprintf("%.2fm", m) }
func (f Feet) String() string { return fmt.Sprintf("%.2ff", f) }

func FToM(f Feet) Meter { return Meter(f*0.3048) }
func MToF(m Meter) Feet { return Feet(m/0.3048) }
