// scalac  5-partialfunction.scala && scala part


object part {
  def partialFunc[A,B,C](a:A, f:(A,B)=>C): B=>C = {
    (b:B) => f(a,b)
  }
  def main(args:Array[String]) = {
    val a=partialFunc(2, (a:Int,b:Int) => a*b)(3)
    println(a)
  }
}
