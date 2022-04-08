package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

// GetMaxPrimeFactor require n >= 2
func GetMaxPrimeFactor(n int64) (ans int64) {
	ans = 1
	for i, m := int64(2), int64(math.Floor(math.Sqrt(float64(n)))); i <= m && i <= n; i++ {
		if n%i == 0 {
			ans = i
			for n%i == 0 {
				n /= i
			}
		}
	}
	if ans < n {
		ans = n
	}
	return ans
}

/*
Solution3 求最大质因子
*/
func main() {
	in := bufio.NewReader(os.Stdin)
	var t int
	fmt.Fscan(in, &t)
	for i := 0; i < t; i++ {
		var n int64
		fmt.Fscan(in, &n)
		fmt.Println(GetMaxPrimeFactor(n))
	}
}
