package main
import "fmt"

func main(){
	// my first 
	fmt.Println("hello, world")
	fmt.Print("hello world")

	var a string = "Run"
	fmt.Print(a)

	var b,c int = 1,2
	fmt.Print(b,c)

	var d int
	fmt.Println(d)

	var e bool
	fmt.Println(e)

	var f *int
	var g []int
	var h map[string] int
	var i chan int
	var j func(string) int
	var k error
	fmt.Println(f,g,h,i,j,k)

	var l int;
	fmt.Println("%v\n",l)

	m := 123
	fmt.Println(m)

	const LENGTH int = 10
	const WIDTH int = 5
	var area int
	const aa,bb,cc = 1, false , "str"

	area = LENGTH * WIDTH
	fmt.Println("房屋面积为： %d", area)
	fmt.Println(aa,bb,cc)

	var aaa int = 4
	var bbb int32 
	var ccc float32
	var ptr *int

	ptr = &aaa
	fmt.Println(aaa,bbb,ccc)
	fmt.Println("%d\n",ptr)

	var ba = [5]float32{12.0,14.0,2.0,5.0,9.0}
	fmt.Println(ba,ba[2])

	var ab int = 20
	var ip *int
	ip = &ab
	fmt.Println(&ab)
	fmt.Println(ip)
	fmt.Println(*ip)

}
