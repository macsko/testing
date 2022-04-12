package main

import "fmt"

func f_bib() (int, error) {
	return 0, nil
}

func main() {
	fmt.Println("Main file")
	fmt.Println("Nice :)")
	a, _ := f_bib()
	fmt.Println(a)
	fmt.Println("New code")
	fmt.Println("other code")
	fmt.Println("New code")
}
