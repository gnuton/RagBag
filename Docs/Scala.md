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

# Functions  & Procedures #
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

// Function can explicitely ask to some arguments type to have some trait
def f(x: Iterable[Int]) = x // useless function that retunrs its Iterable argument

```
and in the end we have special methods
```scala
// some methods allow you to chain calls  like 
// a -= 1 += 3
def -= (elem: A) : ArrayBuffer.this.type

// In a method signature is possible set the upper/lower bound type so that B is constrained to 
// be a supertype/subtype of A
class Stack[+A] {
  def push[B >: A](elem: B): Stack[B] = new Stack[B] { ... }
}

```

# Exceptions #
```scala
// Exception can be thrown as shown
throw new IllegalArgumentException("This is a test")

// Exceptions are not checked at compile time in Scala like they are in Java.
// That means you do not need to add any exception to the function signature
def f(i : Int) = { throw new Exception("test") } // f takes an int and returns a "Nothing" type

// Scala can catch different exception types in a single block
// _ is used to define a variable which is not taked in use
try { throw new IllegalArgumentException("Test") }
catch { 
  case ia: IllegalArgumentException => println( ia.printStackTrace())
  case _: Exception => println("got something else")
}
finally {
  println("it goes all the time here")
}
```

# Data Structures #

## Arrays ##
### Fixed and variable size Array###
#### Array type is fixed type ####
```scala
// new must used to instantiate an array with N null elements
var a = new Array[Int](5)
// new can be omitted if you initialize the array
var a = Array(1,2,3,4,"ciao") // an Array of "Any" object can host integers and strings
// an array can be accessed as follow
a(0) // is 1
a(4) // is "ciao"
a(4) = 4 // replaces "ciao' with 4
a ++= 0 until 5 // appends 0,1,2,3,4 to a
```
You can read more here: http://docs.scala-lang.org/overviews/collections/arrays.html

#### Array Buffers for variable size array ####
They are like the ArrayList available in Java or the Vector in C++.
Adding and removing elements from the beginning or ending happends in efficient (amortized costant time).
Inserting elements in the middle it's not that efficient since it requires shifting elements.
```scala
import collection.mutable.ArrayBuffer
val b = new ArrayBuffer[Int]()
b.append(20)
b.prepend(10)
b.clear()
b += 10
b += (10,20,30)
b.insert(2, 10) // insert 10 to 2nd position
b.toArray() // converts the bufferArray to Array
```
### Traversing Arrays/ArrayBuffers ###
There are basically two ways to traverse an array
```scala
// 1. by element
for (i <- theArray) print i // it will print all the elements in the array

// 2. by index
for (i <- 0 until theArray.size) print i
```
### Algorithms ###
```scala
var a = 0 to 10 toArray
a.reverse
a.sortWith(_ < _)
a.max
a.min

var b = new ArrayBuffer[Int]()
b ++= 0 to 10 toArray
b.reverse // returns a new reversed ArrayBuffer
a.sortWith(_ < _) // returns a new reversed ArrayBuffer
```
### Multi-Dimensional Arrays ###
```scala
val matrix = Array.ofDim[Int](3,2) // creates Array[Array[Int]] = Array(Array(0, 0), Array(0, 0), Array(0, 0))
matrix(2)(1)=112
```

## Maps and Tuples ##
Scala provides mutable and immutable maps. 
Maps in Scala can be sorted (implemented as Tree) or unsorted (implemented as Hash).
```scala
// Immutable maps can be instantiated as 
val map = Map("Antonio" -> 1, "Alessia" -> 2) // creates scala.collection.immutable.Map[java.lang.String,Int]
                                              // the opeartor -> makes a pair. you could use ("antonio", 1) too
// Mutable maps
val map = new collection.mutable.HashMap[String, Int]
map("antonio") = 1 // assign a value to the key "antonio"
map("antonio2") // it doesn't exists and throws java.util.NoSuchElementException
map.contains("antonio")
map.remove("antonio2") // returns None
map.remove("antonio") // remove the element and returns the value of "antonio"
map -= "antonio" // removes the key/value pair associated to "antonio" from the map returns the map
map - "antonio" // returns a NEW map without "antonio" key/value pair
map += ("a" -> 1, "b" -> 2) // adds a set of value to the map

// every map can be traversed with a for
for ((k, v) <- map) println(k + " " + v)

```

# How to use Java in Scala #
## Conversion of collections ##
```scala
import collection.JavaConversions._
TODO
```
http://www.scala-lang.org/api/current/index.html#scala.collection.JavaConversions$

# REPL tricks #
1. :paste enables the paste mode that allow you to paste code blocks 
2. 

# Reference #
- Official docs - http://scala-lang.org/api/current/#package
- Intro to Collections - http://docs.scala-lang.org/overviews/collections/introduction.html
