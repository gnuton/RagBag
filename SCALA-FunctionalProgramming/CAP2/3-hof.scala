// HOF High order function
// scalac 3-hof.scala  && scala hof

object hof {
  def sum(i:Int, j:Int): Int = i+j
  def sub(i:Int, j:Int): Int = i-j
  
  def pr(i:Int, j:Int, f:(Int,Int)=>Int) = println("Result " + f(i,j))
  def main(args: Array[String]) = {
    pr(2,1,sum)
    pr(2,1,sub)
  }
}
