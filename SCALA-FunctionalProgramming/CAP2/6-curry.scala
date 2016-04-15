/*Let’s look at another example, currying,

into a function of one argument that partially applies f. Here again there’s only one

implementation that compiles. Write this implementation.

def curry[A,B,C](f: (A, B) => C): A => (B => C)

which converts a function f of two arguments*/

// scalac 6-curry.scala && scala curry

object curry {
  def curry[A,B,C](f: (A, B) => C): A => (B => C) = {
    (a:A) => (b:B) => f(a,b)
  }

  def main(args:Array[String]) = {
    val f = (x:Int,y:Int) => x+y
    val x = curry(f) // partial function
    println(x(1)(2)) // returns 3
  }

}
