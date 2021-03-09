package main

import (
	"fmt"
	"os"
	"reflect"
)

// Solution ...
type Solution struct{}

func main() {
	if len(os.Args) != 2 {
		panic("want 1 argument")
	}
	s := os.Args[1]
	fmt.Printf("[%s]\n", s)
	method := reflect.ValueOf(Solution{}).MethodByName(s)
	if !method.IsValid() {
		panic("not found")
	}
	res := method.Call([]reflect.Value{})
	if len(res) > 0 {
		fmt.Println("[Result]")
		for i, r := range res {
			fmt.Printf("%d| %+#v\n", i, r)
		}
	} else {
		fmt.Println("[Finished]")
	}
}
