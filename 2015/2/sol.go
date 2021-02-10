package main

import (
    "os"
    "fmt"
    "log"
    "strings"
    "bufio"
    "strconv"
    "math"
    "sort"
)

func main() {
    // Read file
    input, err := read_input()
    if err != nil {
        log.Fatal(err)
    }

    if len(os.Args) > 1 {
        arg := os.Args[1]
        if arg == "1" {
            sol1(input)
        } else if arg == "2" {
            sol2(input)
        }
    } else {
        fmt.Println("Please provide first argument, either 1 or 2")
    }
}

func read_input() ([]string, error) {
    file, err := os.Open("input")
    if err != nil {
        return nil, err
    }
    defer file.Close()

    var lines []string
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        lines = append(lines, scanner.Text())
    }
    return lines, scanner.Err()
}

func sol1(input []string) {
    var counted float64 = 0
    for _, line := range input {
        m := strings.Split(line, "x")
        x, _ := strconv.ParseFloat(m[0], 64)
        y, _ := strconv.ParseFloat(m[1], 64)
        z, _ := strconv.ParseFloat(m[2], 64)
        side_xy := x*y
        side_yz := y*z
        side_zx := z*x
        counted += 2*(side_xy + side_yz + side_zx) +
            math.Min(side_xy, math.Min(side_yz, side_zx))
    }
    fmt.Println(int(counted))
}

func sol2(input []string) {
    counted := 0
    for _, line := range input {
        m := strings.Split(line, "x")
        x, _ := strconv.Atoi(m[0])
        y, _ := strconv.Atoi(m[1])
        z, _ := strconv.Atoi(m[2])
        sides := []int{x,y,z}
        sort.Ints(sides)
        counted += 2*(sides[0] + sides[1]) + x*y*z
    }
    fmt.Println(counted)
}
