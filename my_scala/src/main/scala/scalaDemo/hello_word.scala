package scalaDemo

object hello_word {
  def main(args: Array[String]): Unit = {
    println("Fuck World")

    for (a <- 1 to 10) {  // 1 to 10 包含10 ,前后都是闭区间
      println("a is : " + a )
    }
    println("==" * 20)
    for (b <- 1 until 10) {  // until 不包含结束值,前闭后开
      println("b is : " + b)
    }
    println("==" * 20)
    //在 for 循环 中你可以使用分号 (;) 来设置多个区间，它将迭代给定区间所有的可能值
    var m, n = 0;
    for (m <- 1 to 4; n <- 2 to 6) {
      println(m+" * "+n+" = "+m*n)
    }
    // for 循环集合
    var numList = List(1,4,5,7,8)
    for (num <- numList) {
      println(num)
    }
    println("==" * 20)
    // for循环过滤
    for (a <- 1 to 10 if a != 3; if a < 8) {
      println("a is :" + a)
    }
    println("==" * 20)
    // 使用 yield 关键字
    println(addNum(6,7))
    println("==" * 20)
    printString("Hello", "Fuck", "World")
    println("==" * 20)
    for (i <- 1 to 10) {
      println(i + " 的阶乘为: = " + factorial(i) )
    }
  }

  def addNum(a:Int, b:Int):Int = {
    var sum = 0
    sum = a + b
    return sum
  }

  def printString(args:String*) = { //函数可变参数
    var i = 0 ;
    for (arg <- args) {
      println("Arg value[" + i + "] = " + arg)
      i += 1;
    }
  }

  def factorial(x:BigInt):BigInt = { //递归函数  阶乘
    if (x <= 1) {
      1
    }
    else {
      x * factorial(x-1)
    }
  }
}
