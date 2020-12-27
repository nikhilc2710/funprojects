// Factorial and Fibo.
package main

import "fmt"

func fib(n int) int{
	first:=0
	second:=1
	ans:=0
	for i:=2;i<n;i++{
		ans=first+second
		first=second
		second=ans
	}
	return ans
}

func factorial(n int) int{
	ans:=1
	for i:=1;i<n+1;i++{
		ans*=i
	}
	return ans
}

func main() {
	fmt.Println(fib(10))
	fmt.Println(factorial(5))

	
}