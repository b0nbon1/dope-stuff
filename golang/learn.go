package main

import (
	"fmt"
	"math"
	"strings"
)

func sqrt(x float64) string {
	if x < 0 {
		return sqrt(-x) + "i"
	}
	return fmt.Sprint(math.Sqrt(x))
}

func pow(x, n, lim float64) float64 {
	if v := math.Pow(x, n); v < lim {
		return v
	}
	return lim
}

// type Vertex struct {
// 	X int
// 	Y int
// }

func printSlice(s []int) {
	fmt.Printf("len=%d cap=%d %v\n", len(s), cap(s), s)
}

type Vertex struct {
	Lat, Long float64
}

var m map[string]Vertex

func WordCount(s string) map[string]int {
	m := make(map[string]int)
	fields := strings.Fields(s)
	for _, w := range fields {
		m[w] += 1
	}
	return m
}

func compute(fn func(float64, float64) float64) float64 {
	return fn(3, 4)
}

// closures
func adder() func(int) int {
	sum := 0
	return func(x int) int {
		sum += x
		return sum
	}
}

func main() {
	// sum := 0
	// for i := 0; i < 10; i++ {
	// 	sum += 1
	// }
	// println(sum)

	// sum := 1
	// for ; sum < 1000; {
	// 	sum += sum
	// }
	// println(sum)

	// similar to while loop
	// sum := 1
	// for sum < 1000 {
	// 	sum += sum
	// }
	// fmt.Println(sum)

	// fmt.Println(sqrt(2), sqrt(-4))
	// fmt.Println(
	// 	pow(3, 2, 10),
	// 	pow(3, 3, 20),
	// )

	// defer; Deferred function calls are pushed onto a stack. When a function returns, its deferred calls are executed in last-in-first-out order.
	// fmt.Println("counting")
	// for i := 0; i < 10; i++ {
	// 	defer fmt.Println(i)
	// }

	// fmt.Println("done")

	// pointers pointers !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	// i, j := 42, 2701

	// p := &i         // point to i
	// fmt.Println(*p) // read i through the pointer using referencing
	// *p = 21         // set i through the pointer
	// fmt.Println(i)  // see the new value of i

	// p = &j         // point to j
	// *p = *p / 37   // divide j through the pointer
	// fmt.Println(j) // see the new value of j

	// structs(almost similar to objects)
	// v := Vertex{1, 2}
	// p := &v
	// p.X = 1e9
	// fmt.Println(v)

	// var (
	// 	v1 = Vertex{1, 2}  // has type Vertex
	// 	v2 = Vertex{X: 1}  // Y:0 is implicit
	// 	v3 = Vertex{}      // X:0 and Y:0
	// 	p  = &Vertex{1, 2} // has type *Vertex
	// )
	// fmt.Println(v1, p, v2, v3)

	// arrays
	// var a [2]string
	// a[0] = "Hello"
	// a[1] = "World"
	// fmt.Println(a[0], a[1])
	// fmt.Println(a)

	// primes := [6]int{2, 3, 5, 7, 11, 13}
	// fmt.Println(primes)

	// primes := [6]int{2, 3, 5, 7, 11, 13}

	// // slices are dynamic, arrays are fixed
	// var s []int = primes[1:4]
	// fmt.Println(s)

	// names := [4]string{
	// 	"John",
	// 	"Paul",
	// 	"George",
	// 	"Ringo",
	// }
	// fmt.Println(names)

	// a := names[0:2]
	// b := names[1:3]
	// fmt.Println(a, b)

	// b[0] = "XXX"
	// fmt.Println(a, b)
	// fmt.Println(names)

	// q := []int{2, 3, 5, 7, 11, 13}
	// fmt.Println(q)

	// r := []bool{true, false, true, true, false, true}
	// fmt.Println(r)

	// s := []struct {
	// 	i int
	// 	b bool
	// }{
	// 	{2, true},
	// 	{3, false},
	// 	{5, true},
	// 	{7, true},
	// 	{11, false},
	// 	{13, true},
	// }
	// fmt.Println(s)

	// s := []int{2, 3, 5, 7, 11, 13}
	// fmt.Println(s[:])
	// s = s[1:4]
	// fmt.Println(s)

	// s = s[:2]
	// fmt.Println(s)

	// s = s[1:]
	// fmt.Println(s)

	// s := []int{2, 3, 5, 7, 11, 13}
	// printSlice(s)

	// // Slice the slice to give it zero length.
	// s = s[:0]
	// printSlice(s)

	// // Extend its length.
	// s = s[:4]
	// printSlice(s)

	// // Drop its first two values.
	// s = s[2:]
	// printSlice(s)

	// var s []int
	// fmt.Println(s, len(s), cap(s))
	// if s == nil {
	// 	fmt.Println("nil!")
	// }

	// a := make([]int, 5)
	// printSlice(a)

	// b := make([]int, 0, 5)
	// printSlice( b)

	// c := b[:2]
	// printSlice(c)

	// d := c[2:5]
	// printSlice(d)

	// Create a tic-tac-toe board.
	// board := [][]string{
	// 	[]string{"_", "_", "_"},
	// 	[]string{"_", "_", "_"},
	// 	[]string{"_", "_", "_"},
	// }

	// // The players take turns.
	// board[0][0] = "X"
	// board[2][2] = "O"
	// board[1][2] = "X"
	// board[1][0] = "O"
	// board[0][2] = "X"

	// for i := 0; i < len(board); i++ {
	// 	fmt.Printf("%s\n", strings.Join(board[i], " "))
	// }

	// appending to a slice
	// var s []int
	// printSlice(s)

	// // append works on nil slices.
	// s = append(s, 0)
	// printSlice(s)

	// // The slice grows as needed.
	// s = append(s, 1)
	// printSlice(s)

	// // We can add more than one element at a time.
	// s = append(s, 2, 3, 4)
	// printSlice(s)

	// get indices & values
	// var pow = []int{1, 2, 4, 8, 16, 32, 64, 128}
	// for i, v := range pow {
	// 	fmt.Printf("2**%d = %d\n", i, v)
	// }

	// pow := make([]int, 10)
	// for i := range pow {
	// 	pow[i] = 1 << uint(i) // == 2**i
	// }
	// for _, value := range pow {
	// 	fmt.Printf("%d\n", value)
	// }

	// m = make(map[string]Vertex)
	// m["Bell Labs"] = Vertex{
	// 	40.68433, -74.39967,
	// }
	// fmt.Println(m["Bell Labs"])

	// m := make(map[string]int)

	// m["Answer"] = 42
	// fmt.Println("The value:", m["Answer"])

	// m["Answer"] = 48
	// fmt.Println("The value:", m["Answer"])

	// delete(m, "Answer")
	// fmt.Println("The value:", m["Answer"])

	// v, ok := m["Answer"]
	// fmt.Println("The value:", v, "Present?", ok)

	// hypot := func(x, y float64) float64 {
	// 	return math.Sqrt(x*x + y*y)
	// }
	// fmt.Println(hypot(5, 12))

	// fmt.Println(compute(hypot))
	// fmt.Println(compute(math.Pow))

	// closures
	pos, neg := adder(), adder()
	for i := 0; i < 10; i++ {
		fmt.Println(
			pos(i),
			neg(-2*i),
		)
	}
}