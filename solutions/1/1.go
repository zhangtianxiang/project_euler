package main

import (
	"fmt"
)

// Solution1 容斥：3的倍数的和+5的倍数的和-15的倍数的和
func main() {
	var t int
	fmt.Scanf("%d", &t)
	for i := 0; i < t; i++ {
		var n int64
		fmt.Scanf("%d", &n)
		k3 := (n - 1) / 3
		k5 := (n - 1) / 5
		k15 := (n - 1) / 15
		sum3 := (1 + k3) * k3 * 3 / 2
		sum5 := (1 + k5) * k5 * 5 / 2
		sum15 := (1 + k15) * k15 * 15 / 2
		res := sum3 + sum5 - sum15
		fmt.Println(res)
	}
}
