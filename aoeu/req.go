package main

import (
	"fmt"
	"net/http"
)

const url = "https://typing-speed-test.aoeu.eu"

func main() {
	resp, _ := http.Get(url)
	fmt.Println(resp)
}
