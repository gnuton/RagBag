// scalac 2-fibonacci.scala  && scala fib
// j          0 1 2 3 4 5 6
// fibonacci 0 1 1 2 3 5 8  
object fib {
  def fibonacci(s:Int):Int = {

    @annotation.tailrec
    def loop(i:Int=1, fb1:Int=0, fb2:Int=1):Int = {
      if (i == s) 
        fb2
      else
        loop(i+1,fb2, fb1+fb2)
    }

    s match {
      case 0 => 0
      case 1 => 1
      case _:Int => loop()
    }
  }

  def main(args: Array[String]) ={
    println(fibonacci(6))
  }
}
