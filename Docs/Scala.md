# Scala #
![logo](https://upload.wikimedia.org/wikipedia/en/8/85/Scala_logo.png)

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

# Variables & Constatns#
```scala
// Constant values
val c = 3
c = 4 // this will trigger an error

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
// 4. Strings
.... and more.... look at diagram in the next chapter for the full list

Beside those tipes there are some special ones:
// 1. Any - Any variable can contain any kind of variable but null and nothing.
var a:Any = 1
// 2. Null is the type that has only one instance and that's null.
var a = null // Defines a Null object
class MyClass
var c:MyClass = null // it's possible to assign null to a reference (AnyRef derived type)
var c:Int = null // ERROR. It's not possible to assign null to a value (AnyVal derived type)
// 3. Nothing type has not instances. [Read more about that here](http://oldfashionedsoftware.com/2008/08/20/a-post-about-nothing/)
```

## Inheritance hierarchy of Scala types ##
We have three root types. Any, Null and Nothing.
Any type is extended by Anyval and AnyRef; AnyVal is the base type for objects that in Java are primitives and AnyRef is for the rest.
* AnyVal doesn't add any method to Any. It's just a marker.
* AnyRef adds [wait/notify methods and syncronized block ](http://www.programcreek.com/2009/02/notify-and-wait-example/) 
![logo](http://joelabrahamsson.com/PageFiles/148/1310_1644.jpg)

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

## PATTERN MATCHING ##
```scala
var y = x match { 
  case 1 => println("1 is Int")
  case 2 => println("2 is Int")
  //case "uno":String => println("we got a string")
  case _ => println("default")
}

// match supports differnt types too
var x:Any = 1
x match {
  case 1 => println(1);
  case "ciao" => println(2);
  case _ => println("default")
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

# Collections #
Collections are containers of objects. Collections can be: 
* lazy/strict - lazy collections do not consume memory until they are not accessed
* mutable/immutable - immutable when the object referenced by the collection never changes

## 1. Arrays ##
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

## 2. Tuples ##
Are immutable objects containing more than one value. They are usually returned by functions that output many objects. Dislike arrays, the first element in a tuple is 1 and not 0.
```scala
val t = ("antonio",1,3)
t._1 // returns "antonio". 
t._1 = 1 // triggers an error
val (a,b,c) = t // a b and c get the value of the tuple. This is called decomposition.
// tuples can be created with zip methods available in collections.
val a = List(10,20,30)
val b = List(40,50,60)
a.zip(b) // creates List[(Int, Int)] = List((10,40), (20,50), (30,60))
a.zipWithIndex // List[(Int, Int)] = List((10,0), (20,1), (30,2))
```

## 3. Lists ##
Scala's List[T] is a linked list of type T.
List are immutable structures and are implemented as linked list which are used in functional programming.
```scala
// Define List of integers.
val x = List(1,2,3,4)
x(0) = 2 //ERROR it immutable

```
Mutable List can be achieved using ListBuffer. 
Performance differences between Array (which are mutable) and Lists
```
                          Array  List
Access the ith element    O(1)   O(i)
Discard the ith element   O(n)   O(i)
Insert an element at i    O(n)   O(i)
Reverse                   O(n)   O(n)
Concatenate (length m,n)  O(n+m) O(n)
Calculate the length      O(1)   O(n)
Memory differences

                          Array  List
Get the first i elements  O(i)   O(i)
Drop the first i elements O(n-i) O(1)
Insert an element at i    O(n)   O(i)
Reverse                   O(n)   O(n)
Concatenate (length m,n)  O(n+m) O(n)
```
## 4. Sets ##
A set is a collection of pairwise different elements of the same type.
```scala
// Define a set.
var x = Set(1,3,5,7)
```

## 5. Maps ##
A Map is an Iterable consisting of pairs of keys and values 
As other collection types, scala provides mutable and immutable maps. 
Maps in Scala can be sorted (implemented as Tree) or unsorted (implemented as Hash).
```scala
// Immutable unsorted maps can be instantiated as 
val map = Map("Antonio" -> 1, "Alessia" -> 2) // creates scala.collection.immutable.Map[java.lang.String,Int]
                                              // the opeartor -> makes a pair. you could use ("antonio", 1) too
// Immutable sorted maps 
val sortedMap = collection.immutable.SortedMap("antonio" -> 1, "Alessia" -> 2)

// Mutable sorted maps - it has not been implemented yet in Scala, please use java TreeMap
//                     - using TreeMap will allow you to modify the data in constant time insteaf of log(n)
val sortedMap = new java.util.TreeMap[String, Int]()
sortedMap.put("antonio", 1)

// Mutable unsorted maps
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

## 6. Options ##
Option[T] provides a container for zero or one element of a given type.
```scala
// Define an option
val x:Option[Int] = Some(5)
```

# Classes #
Scala files can have more than one class. Every Scala class is child of scala.ScalaObject and it inheriths all the properties from it.

Let's start to have a look at class fields. Those can be public, protected or private. In any cases Scala creates private or public getter and setters method. Class fields must be always initialized
```scala
class MyClass {
  private var x : Int = 0; // as in other langs private fields are accessible only from this class
  var y = 1; // scala creates setter and getters from public fields under the hood.
             // public int y and public void age_$eq(int)
  // in case we would like to redefine the setter method
  private var privateZ:Int= -1
  protected var protectedY = -1 // as in other languages this is accessible only to this and subclasses
  def z_=(newZ:Int) { if (newZ > privateZ) privateZ=newZ }
  def z = privateZ
}

var m = new MyClass
m.y_ = (2) //works too
m.y = 2
m.
```
let's have a look now at the methods
```scala
class MyClass {
  private var x : Int = 0;
  def inc() = { x+=1 }
  def current = x // accessor do not use (). In scala is good practice not to define it as current()
}

var m = new MyClass
m.current() // fails
m current // this works fine! :D
```
As in other languages, even in scala a class instance A can access to private fields of private fields of other instances if they are instance of the same class object.
```scala
class MyClass (private val x:Int){
  def isBigger(y:MyClass) = y.x < x
}

var a = new MyClass(10)
var b = new MyClass(12)
a.isBigger(b)
```

### Class constructors ###
Scala allows you to have a primary and many auxiliary (secondary) constructors as other languages do.
```scala
// Primary constructor
class MyClass(val x:Int){ // val or var can be omitted and x will become a private field
  println(x) // we can access x from the class 
  override def toString = "ciao" /// here in the body or primary constructor we can override some methods
}
def m = new MyClass
m.x // x field can be accessed from outside the class too if not defined as private
```
Auxiliary constructors starts with a call to the main one. For this reason they cannot invoke superclass constructors.
```scala
// Auxiliary constructors are defined as follow
class MyClass{
  private var a:Int = 0
  
  def this(a:Int) { // this is the auxiliary constructor. we can have as much as we want of those
    this()
    this.a = a
  }
}
```
If the constructor make use of some val in the class body some problem may pop up.
Let's have a look at the following example:
```scala
// a standar class with an array. the size of the array is defined by the range value
class a {
  val range = 5
  var array = Array[Int](range)
}
var aa = new a
aa.array // the array has 5 elements

// let's extend the class and let's change the value of range
class b extends a { override val range = 1 } 
var bb = new b
aa.array // the array size is 0. So it didn't worked because we have overriden the value 
         // before running the b constructor which is the one that sets the new value to b.range
```
Solutions for this issue could be:
```scala
//1. To make the field lazy
class a {
  lazy val range = 5
  var array = Array[Int](range)
}
class b extends a { override lazy val range = 1 }  // this will fail!

//2. To set the value as final so that it cannot be overriden
class a {
  final val range = 5 
  var array = Array[Int](range)
}
class b extends a { override val range = 1 }  // this will fail!
```
If you face construction order problems as shown here you could use scalac -Xcheckinit to build your code and that will throw an exception is such issues are found.

### Nested Classes ###
Scala supports nested classes. # sign is called "type projection" and it means "a Member of ANY MyClass".
Type projection is usually used in very few places and 
```scala
class MyClass(){
  def a = new Array[MyClass#NestedClass](5)
  def b = new Array[NestedClass](5)
  def createNestedObj(x:Int) = new NestedClass(x)
  def addNestedObjA0(x:Int) = a(0) = new NestedClass(x)
  def addNestedObjB0(x:Int) = b(0) = new NestedClass(x)
  
  class NestedClass(x:Int) {                               // here is the nested class
    def test(y:Int) = println("TEST")
  }
}
var x = new MyClass
var y = new MyClass
x.a(0) = x.createNestedObj(0)  // works, The array a takes in MyClass#NestedClass
y.a(1) = x.createNestedObj(1)  // works
y.b(0) =  x.createNestedObj(0) // ERROR! the array b doesn't take in MyClass#NestedClass
x.addNestedObjB0(0)            // If we insert the NestedClass into b from inside than it works 
x.addNestedObjA0(0)            // inserting stuff into a will continue to work too

```
under the hood the scala compiler creates two sepearates class MyClass$NestedClass and MyClass.
Despite two separate classes, you cannot instantiate a class defined in another class from the outside.
This looks differents if you use a companion object.
```scala
object MyClass {
  class NestedClass(x:Int) {
    def test(y:Int) = println("TEST")
  }
}

class MyClass(){
  var a = new Array[MyClass.NestedClass](5)
}

m.a(0) = new MyClass.NestedClass(2) // here we are! :D we can create instances of MyClass.
```

## bean properties ##
Java beans are classes that expect to have getter and setter method in the form getX/setX. And Scala as we have seen so far generates different signatures for getter and setter methods.
Annotating a variable with a @BeanProperty tells Scala copiler to generates 2 methods more (public void setX(int) and public int getX())which are needed to make the class java bean compliant.
```scala
import scala.reflect._
class MyClass() {@BeanProperty var x : Int = 0 }
```

## inheritance ##
Classes can be extended unless they are final
```scala
class Person
class Italian extends Person

final class Alien extends Person
class German extends Alien // this fails! Alien is final!
```
Inherited classes must use override keyword to override the behaviour of a method .
```scala
class Person
class Italian extends Person {
  override def toString = "Sono Italiano (it was " + super.toString + ")"
}
def p = new Italian
p.toString  // returns  "Sono Italiano (it was Italian@5323e7b7)"
```

Scala  supports abstract classes which can contain abstract fields and methods.
```scala
abstract class a { 
  val x:Int; // Abstract field  
  val y = 1; // concrete field
  def aMethod // Abstract method
  def getX = x // concrete method
}
```

If a superclass constructors requires some arguments, the derived class must fullfill that request
```scala
class a(x:Int) 
class b(y:Int, x:Int) extends a(x)
```

Scala classes can extend Java ones
```scala
class myFrame(title:String) extends java.awt.Frame(title)
var window = new myFrame("Test")
window.setVisible(true)
```

## Type checks ##
Every scala object inheriths isInstaceOf metdhod.
```scala
1.isInstanceOf[Int] // returns True
1.0.isInstanceOf[Double] // reutnrns True

abstract class a
class b
c = new b
c.isInstanceOf[b] // true
c.isInstanceOf[a] // true
c.isInstanceOf[ScalaObject] // true

().isInstanceOf[Unit]
```
If you wanna check that an object is really an instance of a class and not a sub/super class of it..
```scala
class a 
class b extends a
class c extends b

def bb = new b
def cc = new c

bb.getClass == classOf[b] // true
cc.getClass == classOf[b] // false
```

# Objects #
Objects are abstractions in scala that can extend a class/traits and they may have all the features that a class have, but the costructor must have no arguments as for traits
```scala
object test(a:Int) {} // DOESN'T WORK! 
object test {} // this is OK
```

## Singleton objects ##
Objects are abstractions which are needed in scala whenever you wanna have a singleton instance.
```scala
object counter { 
  private var i = 0; 
  def inc() = {i+=1; i}
}
counter.inc() // returns 1
counter.inc() // returns 2
```

## Companion Objects ##
A companion object is an object which has the same name of a class and it'd defined in the same file.
Companion objects and class can access each other private vars.
Companion objects is what is used in scala in order to define static fields and methods.
```scala
class test {
  def staticFunc() = test.staticFunc() // the staticFunc method points to the object one
  def setX(x:String) = test.x = x // the class have access to the object private vars
}

object test {
  private var x = "ciao" // the class and the object can access this var
  def staticFunc() = println(x)
}

var t = new test
test.staticFunc // prints "ciao"
t.staticFunc // same as test.staticFunc
t.setX("bye")
t.staticFunc
```

## Application object ##
Any application needs an entry point. In scala every app use an Application object as entrypoint
```scala
object HelloWorld extends App { // extending the main traits is one way to create an entry point for an app
  if (args.size > 0)
    println(args(0))
  else
    println("Hello World!")
}
```

## Enumeration object ##
There is no enumeration type in scala, but enumaration can be obtained extending Enumeration helper class.
```scala
object osType extends Enumeration { val linux, win, ios = Value }
import osType._
def myFun(x:osType.Value) = { if (x==linux) println("linux")}
myFun(linux)
```
BTW enumeratum for many people could be a better way to achieve enumerations in scala https://github.com/lloydmeta/enumeratum

## Package object ##
Please have a look at the "Scala packages" chapter

## Case Object ##
* pattern matching support
* default implementations of equals and hashCode
* default implementations of serialization
* a prettier default implementation of toString

```scala
  scala> object A
defined module A

case object B
defined module B

import java.io._
import java.io._

val bos = new ByteArrayOutputStream        
val oos = new ObjectOutputStream(bos)

val bos = new ByteArrayOutputStream  

val oos = new ObjectOutputStream(bos)
oos: java.io.ObjectOutputStream = java.io.ObjectOutputStream@23818a8e
scala> oos.writeObject(B)
scala> oos.writeObject(A) // thrown an exception

```

## Extending a class ##
As said before, objects can extend classes. let's have a look at a simple example
```scala
abstract class MyAbstractClass(x:Int) {
  def myMethod() : Unit
}
object MyObjectWhichExtendTheClass extends MyAbstractClass(10) {
  override def myMethod() {  println("Do something..") }
}
MyObjectWhichExtendTheClass.myMethod
```
# Traits #
Traits are special objects that encapsulates field and method definitions. They are very similar to abstract java clases.
Traits allo classes to inherith properties from one or more traits. Rule of the thumb... put your code in a trait if you wanna make it reusable and if you want make it available in various part of the class hierarchy.

```scala
// trait are just objects that define some methods or fields
trait CanFly { def land(); def takeOff; def isFlying:Boolean }
trait CanSwim { def float; def sink; isSwimming:Boolean }
trait Green { def color = "green"}

// trait can extend other traits
trait anatidae  extends CanSwim with CanFly

// a class can extend multiple traits but only one class
class duck extedns anatidae { ... }

```

# Scala packages #
Scala packages are similar to what java and c++ namespace offer.
We could define our class in org.gnuton.xxx.test scope in two ways:
```scala
// 1. Chained package clause
package org.gnuton.xxx {
  package test {
    class testClass {}
  }
}

// 2. top file notation 
package org.gnuton.xxx.test
class testClass {}
```
We can import testClass and use it in another file as such:
```scala
import org.gnuton.xxx.test._
val t = new testClass
```

Scala packages can host objects only public object. For instance classes and traits, but no functions or variables are allowed due to Java.
Object Packages are objects that are defined in a package and are used to host functions and variables.

```scala
package org.gnuton.xxx
package object test {
  val x = 1
}
package test {
  class testClass {}
}


import org.gnuton.xxx.test
test.x // returns 1
```

# IO #

## Reading from console ##
```scala
val i = readInt // reads Int from STDIN
val str = readLine // reads a string from STDIN
val d = readDouble
val sin = io.Source.stdin
```

## Reading files ##
```scala
// READING FROM PLAIN TEXT FILES
val source = io.Source.fromFile("/usr/share/dict/words")
// once you defined the file source you can
// 1. loop
for (l <- source.getLines) println(l)
// 2. make an array out of it
val lines = source.getLines.toArray
// 3. make a string
val str = source.getLines.mkString

//do not forget to close the file descriptor
source.close

// READING FROM BINARY FILES
// Scala doesn't provide any library for this. We must fall back to java
import java.nio.file._
val path = Paths.get("/usr/bin/mesg")
val bytes = Files.readAllBytes(path) // creates an Array[Byte] object
```

## Reading from URL ##
```scala
var u = io.Source.fromURL("http://www.gnuton.org", "UTF-8")
var html = val str = u.getLines.mkString
```

## Reading from String ##
```scala
var s = io.Source.fromString("12,3124,213,43,45,12,564,234")
val numbers = s.getLines.mkString.split(",").map(_.toInt)
```

## Writing text files ##
Here we are again.. Scala doesn't provide API to write text files, let's use Java for this too.
We could use BufferedWriter (the more efficient) or PrintWriter for achieve this task.
```scala
import java.io.BufferedWriter
import java.io.File
import java.io.FileWriter

val f = new File("/tmp/test")
if (!f.exists()) f.createNewFile
val fw = new FileWriter(f.getAbsoluteFile())
val bw = new BufferedWriter(fw)
bw.write "Hello man"
bw.close
```

## Walk a directory ##

## Object serialization ##
Serialization is usefull to store objects on the disk or send it via network. Scala relies on the java APIs for this.
```scala
@serializable @SerialVersionUID(1L) class a {
  val a = 10
  @transient var b="ciao"
}
var aa = new a
var fileOut = new java.io.FileOutputStream("/tmp/test")
var out = new java.io.ObjectOutputStream(fileOut)
out.writeObject(aa)
out.close()

var fileIn = new java.io.FileInputStream("/tmp/test")
var in = new java.io.ObjectInputStream(fileIn)
var aa2 = in.readObject().asInstanceOf[a]
aa2.b // is null since it's transient and it has not been serialized
```

# Regular Expressions #
```scala
// regular expression patterns are build from strings
val rx = "[0-9]{4}".r
var str = "Copyright 23 Dec 1998-1999"

// get all matches
rx.findAllIn(str).toArray // Array(1998,1999)

// get the first match
rx.findFirstIn(str).toArray

// replace strings
rx.replaceAllIn(str, "XXXX")

// groupping
val rx = "([0-9]{4}) ([a-z]*)".r
val rx(a,b) = "" // throws MatchError exception
val rx(a,b) = "1919 abc" //defines variable a=1919 and b=abc
```

# Concurrency #
## the "old" scala Actors##
[Actors](http://docs.scala-lang.org/overviews/core/actors.html) are concurrent processes that communicate by exchanging async messages. They have been deprecated and Akka actors should be used instead.
Nowadays Actors lib is a separate artifact so you need to add that dependency to SBT config file.
```scala
libraryDependencies ++= Seq(
  "org.scala-lang" % "scala-actors" % "2.10.0-M6"
)
```
## the "new" Akka Actors ##

# How to use Java in Scala #
## Conversion of collections ##
```scala
import collection.JavaConversions._
TODO
```
http://www.scala-lang.org/api/current/index.html#scala.collection.JavaConversions$

# REPL tricks #
1. :paste enables the paste mode that allow you to paste code blocks 
2. pressing several time TAB in the scala REPL triggers auto-completation

# SBT #
SBT is a build tool for Scala and Java projects as Maven or Ant.
An build.sbt file is usually placed in the root of the project and it expects the code to be in src/main/scala/

```scala
name := "MyProject"
version := "1.0"
scalaVersion  := "2.11.7"

scalacOptions ++= Seq( "-unchecked"
  , "-deprecation"
  , "-encoding", "utf8"
)

scalacOptions ++= Seq(
  "-feature",
  "-language", "postfixOps"
)

libraryDependencies ++= Seq(
  "org.scalatest" %% "scalatest" % "2.2.4" % "test",
  //"org.scala-lang" % "scala-actors" % "2.10.0-M6",
  "com.typesafe.akka" %% "akka-actor" % "2.3.14"
)
```

# IDE #
Many scala devs use IntelliJ for developing their own projects.
## Importing a Scala project to IntelliJ #
1. Install scala plugin. Settings -> Plugins -> Scala -> Install
2. Open directory with sbt build: File -> Open Project -> select directory with build.sbt -> configure settings

## Creating a Scala SBT project ##
### Intellij 14 ###
1. File > New > Project > SBT
2. In the wizard dialog change something is needed.. in most of cases just press next and finish in the last page
3. Create a Scala class in src/main/scala 
4. For testing purposes you can enter the following code in the scala file you have just created
```scala
   object Hello extends App{
     println("Hello world")
   }
```
5. Right click on the scala file then click on run from the menu to run the app
# Understanding stuff under the hood #
## Having a look at what the compiler does #
Let's write a simple scala class like this
```scala
class MyClass {
  private var a:Int = 0
  var b:Int = 0
}
```
then we can compile it scalac which generates the bytecode myclass.class
```
scalac myclass.scala
```
At this point we can run javap to analize it
```
gnuton@joseph:/tmp$ javap MyClass
Picked up JAVA_TOOL_OPTIONS: -javaagent:/usr/share/java/jayatanaag.jar 
Compiled from "myclass.scala"
public class MyClass implements scala.ScalaObject {
  public int b();
  public void b_$eq(int);
  public MyClass();
}
```

# Reference #
- Official docs - http://scala-lang.org/api/current/#package
- Intro to Collections - http://docs.scala-lang.org/overviews/collections/introduction.html
