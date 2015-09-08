# Scala #
![logo](https://upload.wikimedia.org/wikipedia/en/8/85/Scala_logo.png)

xxx
## Getting started ##
### Create and run your first hello word app  ###
Let's open the scala interpreter and let's run the following code:
```scala
object Hello {
  def main(args: Array[String]) {
    println("Hello word")
  }
}
Hello.main(null)
```
In scala semicolons are optionals. They are only used in case you have multiple instrucitons on the same line.

# Variables #
```scala
// You do not need to define a type when you declare a variable in scala
var a = 1  //Integer

// Types
// Every type in Scala is an object. There are no primitives in Scala
1.to(10) // yields scala.collection.immutable.Range.Inclusive = Range(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
1 to 10 // is the short syntax for the previous 
// Under the hood 1 is converted implicitely to RichInt and than the method is applied.
// Strings are converted to StringOps

// 0. Unit - is the void or null of other languages
var a = ()
// 1. Boolean
// 2. Numeric types (they are 7 as in Java)
//    Byte, Char, Short, Int, Long, Float, Double
// 3. Big numbers - BigInt and BigDecimal are used in order to compute large, but finite number with a lot of //                       digits
      val x = BigInt(1)
```
## lazy variables ##
if a variable is declared lazy, it initiazlization is deferred until it's accessed for the first time
```scala
lazy val words = io.Source.fromFile("/not-existing-file").mkString // this doesn't fail yet
println(words) // here it failes throwing a java.io.FileNotFoundException
```

# Arithmetic operations #
1. Arithmetic operators
```scala
// are + - * / %
1 + 2 // is 1.+(2) where .+() is a method of 1 which is an integer
// there is no ++ o -- operators since Int class is immutable
a
```
2. Bit operators
```scala
// are & | ^ >> <<
```
# Control structures #

## IF/ELSE ##
```scala
if (1 > 0) 1 else -1  // returns 1 and it's like 1 > 0 ? 1 : -1 statement of other programming languages but
                      // you can have expressions for 1 and -1
if (1 > 0) (if (3 < 2) 4) else -1 // returns ()                      
if (1 > 0) "ciao" else -1 // returns "ciao". if there are mixed type expressions, the if returns a super type\
                          // common to both types String and Int which is the type 'Any'

if (n > 0) { val i = 0; i } // returns 45
// in scala it's okay to use the Kernighan & Ritchie brace style
if (n > 0) {
  val i = 0
  i
}
```

## Block Expression ##
They are the same as in C++ or Java, but they return the value of the latest operation
```scala
{ val i = 0; i } // the block contains several expressions sorrounded by braces. it returns the value of i
{ val i = 0 } // returns () because assignements return a Unit value
```
## loops ##
```scala
// WHILE loop
while (n>0) {
  // something
}

// FOR EACH loop. There is no "standard" FOR loop  
for (i <- 1 to 10) { println(i) }
for (i <- "ciao") {println(i)} // prints out all the letters of the string

// scala supports multiple generators in loops
for (i <- 0 to 10;  j <- 10 to 20) println(i +"-" + j) // prints strings: 0-10, 0-11, 0-12, ... ,10-20

// each generator can have a "guard"; a boolean condition which says which may discard the generated value
for (i <- 0 to 3;  j <- 0 to 3 if (i != j)) println(+ i + "-" + j) // 0-1, 0-2, 0-3, 1-0, 1-2, 1-3 ...

// COMPREHENSION it's a loop which yield a series of values
for (i <- 0 to 3;  j <- 0 to 3 ) yield  i + "-" + j // returns Vector(0-0, 0-1, 0-2,..., 3-1, 3-2, 3-3)
```

# Functions  & Procedures#
Everyone knows what a function is, but what about procedure in scala?
Procedures are function that do not return anything. They produce a side-effect.
```scala
// a function
def f(n : Int) = {n} // Takes an Int returns an Int. 
// a procedure the implementation is not proceded by a = sign
def p(n : Int) {n} // Takes an Int in as arg and return Unit
```
and now back to "functions":
```scala
// To define a function in scala you need to define the function name, argument name (n) and type (Int)
// : Int is the return type and it's needed only in case of recursion
// the implementation of the function follows "=" and it must be in a {} block if it uses several lines
// the return keyword is not generally used. The last value is returned in any case
// return can be used to exit before the end
def myFun(n : Int) = n+1

// recursive functions need the returned type defined before "="
def func(n : Int) : Int = if (n != 0) func(n-1) else n

// Function declarations allow default values
def func(s : String, l : String = "[", r : String = "]") = println (l + s + r)
func("ciao", r="Y") // prints "[ciaoY"

// Functions can read in a variable number of arguments
// we can iterate trough args.elements or get the tail from args.tail
def f(args : Int*) = for (i <- args.elements) println(i)
f(1,2,3,4,5) // prints all the argument passed.
f(0 to 10: _*) // since f doesn't teke in sequences but just integers, : _* converts it to ints

```

# Exceptions #
```scala
// Exception can be thrown as shown
throw new IllegalArgumentException("This is a test")

// Exceptions are not checked at compile time in Scala like they are in Java.
// That means you do not need to add any exception to the function signature
def f(i : Int) = { throw new Exception("test") } // f takes an int and returns a "Nothing" type

// Scala can catch different exception types in a single block
try { throw new IllegalArgumentException("Test") }
catch { 
  case ia: IllegalArgumentException => println( ia.printStackTrace())
  case _: Exception => println("got something else")
}
```

# REPL tricks #
1. :paste enables the paste mode that allow you to paste code blocks 
2. 

# Documentation #
http://scala-lang.org/api/current/#package
