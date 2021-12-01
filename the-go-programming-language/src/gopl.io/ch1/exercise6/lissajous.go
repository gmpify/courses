// Lissajous enerates GIF animations of random Lissajous figures.
package main

import (
  "image"
  "image/color"
  "image/gif"
  "io"
  "math"
  "math/rand"
  "os"
)

var palette = []color.Color{
  color.Black,
  color.RGBA{0xff, 0x00, 0x00, 0xff},
  color.RGBA{0x00, 0xff, 0x00, 0xff},
  color.RGBA{0x00, 0x00, 0xff, 0xff},
  color.RGBA{0xff, 0xff, 0xff, 0xff},
}

const (
  blackIndex = 0
  redIndex = 1
  greenIndex = 2
  blueIndex = 3
  whiteIndex = 4
)

func main() {
  lissajous(os.Stdout)
}

func lissajous(out io.Writer) {
  const (
    cycles  = 4
    res     = 0.001
    size    = 100
    nframes = 64
    delay   = 8
  )
  freq := rand.Float64() * 3.0
  anim := gif.GIF{LoopCount: nframes}
  phase := 0.0
  for i := 0; i < nframes; i++ {
    rect := image.Rect(0, 0, 2*size+1, 2*size+1)
    img := image.NewPaletted(rect, palette)
    for t := 0.0; t < cycles*2*math.Pi; t += res {
      x := math.Sin(t)
      y := math.Sin(t*freq + phase)
      index := uint8(t/(2*math.Pi))+1
      img.SetColorIndex(size+int(x*size+0.5), size+int(y*size+0.5), index)
    }
    phase += 0.1
    anim.Delay = append(anim.Delay, delay)
    anim.Image = append(anim.Image, img)
  }
  gif.EncodeAll(out, &anim)
}
