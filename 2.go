package main

import (
	"bufio"
	"fmt"
	"os"
)

// UpperBound find the first element > x, require non-descending order
func UpperBound(array []int64, want int64) int {
	l := 0
	r := len(array) - 1
	for r-l > 1 {
		m := (l + r) / 2
		if array[m] > want {
			r = m
		} else {
			l = m
		}
	}
	return r
}

/*
Solution2 斐波那契数列
1 1 2 3 5 8 ...
o o e o o e ...
可以得知偶数为每三项出现一次，又因为每个第三项等于前两项的和，所以答案为数列前缀和的一半
如果是正经的OI/ACM题，这里就该进行取模，因为斐波那契是指数增长的，很快就超过10^16
但这里没有取模，所以直接暴力打表即可。
这里还需要实现upper_bound
一定要用这种输入，不然会超时
	in := bufio.NewReader(os.Stdin)
	var t int
	fmt.Fscan(in, &t)
*/
func (Solution) Solution2() {
	// n := []int64{}
	// sum := []int64{}

	// var limit int64 = 4E16
	// var a int64 = 1
	// var b int64 = 1
	// var s int64 = 0
	// for i := 0; ; i++ {
	// 	c := a + b
	// 	if c > limit {
	// 		break
	// 	}
	// 	if (c & int64(1)) == 0 {
	// 		s += c
	// 		fmt.Printf("i=%d, c=%d, sum=%d\n", i, c, s)
	// 		n = append(n, c)
	// 		sum = append(sum, s)
	// 	}
	// 	a = b
	// 	b = c
	// }
	// fmt.Printf("%+#v\n", n)
	// fmt.Printf("%+#v\n", sum)
	in := bufio.NewReader(os.Stdin)
	var t int
	fmt.Fscan(in, &t)
	n := []int64{2, 8, 34, 144, 610, 2584, 10946, 46368, 196418, 832040, 3524578, 14930352, 63245986, 267914296, 1134903170, 4807526976, 20365011074, 86267571272, 365435296162, 1548008755920, 6557470319842, 27777890035288, 117669030460994, 498454011879264, 2111485077978050, 8944394323791464, 37889062373143906}
	s := []int64{2, 10, 44, 188, 798, 3382, 14328, 60696, 257114, 1089154, 4613732, 19544084, 82790070, 350704366, 1485607536, 6293134512, 26658145586, 112925716858, 478361013020, 2026369768940, 8583840088782, 36361730124070, 154030760585064, 652484772464328, 2763969850442378, 11708364174233842, 49597426547377748}
	n = append(n, 5E16)

	for i := 0; i < t; i++ {
		var x int64
		fmt.Fscan(in, &x)
		pos := UpperBound(n, x)
		if n[pos] == x {
			pos++
		}
		fmt.Println(s[pos-1])
	}
}
