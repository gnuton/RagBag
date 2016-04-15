/*
Implement the higher-order function that composes two functions.
def compose[A,B,C](f: B => C, g: A => B): A => C
*/

// scala 7-function_composition.scala && scala funccomp

object funccomp {

  def compose[A,B,C](f: B => C, g: A => B): A => C = {
    (a:A) => f(g(a)) 
  }

  def main(args:Array[String]) = {
    val f1 = (x:Int) => x*2
    val g1 = (x:Int) => x*3
    val fg = compose(f1, g1)
    println(fg(1)) // prints 6
  }
}
