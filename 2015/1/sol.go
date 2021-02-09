package main

import (
    "os"
    "fmt"
    "io/ioutil"
    "log"
)

func main() {
    // Read file
    content, err := ioutil.ReadFile("input")
    if err != nil {
        log.Fatal(err)
    }
    input := string(content)

    if len(os.Args) > 1 {
        arg := os.Args[1]
        fmt.Println(arg)
        if arg == "1" {
            sol1(input)
        } else if arg == "2" {
            sol2(input)
        }
    } else {
        fmt.Println("Please provide first argument, either 1 or 2")
    }
}

func sol1(input string) {
    floor := 0
    // Iterate over input data chars
    for _, letter := range input {
        if letter == '(' {
            floor++
        } else if letter == ')' {
            floor--
        }
    }

    fmt.Println(floor)
}

func sol2(input string) {
    floor := 0
    // Iterate over input data chars
    for index, letter := range input {
        if letter == '(' {
            floor++
        } else if letter == ')' {
            floor--
        }

        if floor == -1 {
            fmt.Println(index+1)
            return
        }
    }
}
