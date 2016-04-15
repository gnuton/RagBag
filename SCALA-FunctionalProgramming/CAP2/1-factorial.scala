// scalac 1-factorial.scala
// scala fact

object fact {
  def factorialBAD(i:Int):Int = {
    //@annotation.tailrec
    // stack frames cannot be optimized by compiler
    // tailrec cannot optimize here. recursive call not in tail pos
    def loop(i:Int):Int = {
      if (i>=1)
        i * loop(i-1)
      else
        1
    }
    loop(i)
  }

  // 3    2     1      0
  // 3    3*2   ret
  def factorial(i:Int):Int = {
    @annotation.tailrec
    def loop(i:Int, acc:Int):Int = {
      if (i>1)
        loop(i-1, acc * i)
      else
        acc
    }
    loop(i, 1)
  }

  def main(args: Array[String]):Unit = {
    println(factorial(3))
  }
}
