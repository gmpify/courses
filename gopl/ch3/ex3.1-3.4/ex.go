package main

import (
	"fmt"
	"log"
	"net/http"
	"strconv"
)

func main() {
	http.HandleFunc("/", handler)
	http.HandleFunc("/svg", svgHandler)
	log.Fatal(http.ListenAndServe("0.0.0.0:8000", nil))
}

func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "URL.Path = %q\n", r.URL.Path)
}

func svgHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "image/svg+xml")

	if w := r.URL.Query().Get("width"); w != "" { width, _ = strconv.Atoi(w) }
	if h := r.URL.Query().Get("height"); h != "" { height, _ = strconv.Atoi(h) }

	svg(w)
}
