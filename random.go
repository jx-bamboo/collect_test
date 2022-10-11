package main
import "fmt"
import "os"


func main(){
  fmt.Println("********** 欢迎来到随机的世界 **********")
  args := os.Args
  fmt.Println("长度：",args)

  one := args[1]

  if(one != ""){
    fmt.Println(one)
  } else {
    fmt.Println("false")
  }


}
