// Copyright © 2016 Alan A. A. Donovan & Brian W. Kernighan.
// License: https://creativecommons.org/licenses/by-nc-sa/4.0/

// See page 13.

// Lissajous generates GIF animations of random Lissajous figures.
package main

import (
	"image"
	"image/color"
	"image/gif"
	"io"
	"log"
	"math"
	"math/rand"
	"net/http"
	"strconv"
)

var palette = []color.Color{color.White, color.Black}

const (
	whiteIndex = 0 // first color in palette
	blackIndex = 1 // next color in palette
)

func main() {
	http.HandleFunc("/lissajous", handler)
	log.Fatal(http.ListenAndServe("localhost:8000", nil))
}

func handler(w http.ResponseWriter, r *http.Request) {
	if err := r.ParseForm(); err != nil {
		log.Print(err)
	}
	params := map[string]int{
		"cycles": 5,
		"size": 100,
		"nframes": 64,
		"delay": 8,
	}
	for k, v := range r.Form {
		var err error
		params[k], err = strconv.Atoi(v[0])
		if err != nil {
			log.Print(err)
		}
	}
	lissajous(w, params)
}

func lissajous(out io.Writer, params map[string]int) {
	const (
		res     = 0.001 // angular resolution
	)
	freq := rand.Float64() * 3.0 // relative frequency of y oscillator
	anim := gif.GIF{LoopCount: params["nframes"]}
	phase := 0.0 // phase difference
	for i := 0; i < params["nframes"]; i++ {
		rect := image.Rect(0, 0, 2*params["size"]+1, 2*params["size"]+1)
		img := image.NewPaletted(rect, palette)
		for t := 0.0; t < float64(params["cycles"])*2*math.Pi; t += res {
			x := math.Sin(t)
			y := math.Sin(t*freq + phase)
			img.SetColorIndex(params["size"]+int(x*float64(params["size"])+0.5), params["size"]+int(y*float64(params["size"])+0.5),
				blackIndex)
		}
		phase += 0.1
		anim.Delay = append(anim.Delay, params["delay"])
		anim.Image = append(anim.Image, img)
	}
	gif.EncodeAll(out, &anim) // NOTE: ignoring encoding errors
}
