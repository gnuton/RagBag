/*
  scalac 4-generic_function.scala && scala gen
EXERCISE 2.2

Implement isSorted, which checks whether an Array[A] is sorted according to a

given comparison function:

def isSorted[A](as: Array[A], ordered: (A,A) => Boolean): Boolean*/

object gen {
  def isSorted[A](as: Array[A], ordered: (A,A) => Boolean): Boolean = {
    def loop(i:Int) : Boolean = {
      if (i >= as.length)
        true
      else if (ordered(as(i-1),as(i)))
        false
      else
        loop(i+1)
    }
    loop(1)
  }

  def main(args:Array[String]) = {
    val a = Array(1,2,3,4)
    def compareInt(i:Int, j:Int) : Boolean = i > j
    println(isSorted(a, compareInt))

    val b = Array(1,2,3,4,2)
    println(isSorted(b, compareInt))
  }
}
