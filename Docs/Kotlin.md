# Kotlin

## Variables & Types
### Val & Vars
```
var x = 0 // variable
val y = 1 // constant

// val may contain mutable objects!! watch out.
val a = arrayOf(1,2,3) 
a[0] =2

// Nulls
var x: Int? = null // the ? let the constant accept nulls

```

### Strings
```kotlin
val multilineStr = """
        this is 
        a test
    """.trimIndent() // there is .trimMargin() too if you wanna get rid of just the margin
println(multilineStr) // prints the multiline string without the identation used in the code
```

### Regexp
```kotlin
// Match
val rx = "[a-z]{3}".toRegex()
rx.matches("abc")
"abc".matches(rx)

```

### Ranges
```kotlin
val x: IntRange = 1..10 //
val y: IntRange = 1 until 10 // 1,2,3, ..., 9
```

### Array
Always mutable.

```kotlin
val x = arrayOf(1,2,3)
x[0] = 2 // we can modify the elements any time
x.getOrNull(10) // tries to get the 10th element otherwise returns null. This is a Kotlin extensino
```

### List
can be mutable or unmutable
```kotlin
// ArrayList is always mutable
val x = arrayListOf(1,2,3) // extends java.util.ArrayList
x[0] = 2

// not mutable list
val x = listOf(1,2,3) // extends java.util.Arrays$ArrayList

// Mutable List
val x = mutableListOf(1,2,3) // extends java.util.ArrayList
x[0] = 2

```

### Set
can be mutable or unmutable
```kotlin
val x = setOf(1,2,3) // immutable extends java.util.LinkedHashSet
val x = hashSetOf(1,2,3) // immutable extends java.util.HashSet
```

### Maps
can be mutable or unmutable
```kotlin
val imap = mapOf( 1 to "a", 2 to "b") // immutable extends java.util.Collections$SingletonMap
val imap = hashMapOf( 1 to "a", 2 to "b") // immutable extends java.util.HashMap

// mutable map
val mmap = mutableMapOf( 1 to "a", 2 to "b") // extends java.util.LinkedHashMap
mmap[1] = "c"

val map1 = mutableMapOf<Int, String>()
val map2 = mutableMapOf<Int, String>()
map1[1] = "c"
map2.put(1,"a")
map2.put(2,"b")
println(map2) // {1=a, 2=b}
println(map1 + map2) // {1=a, 2=b}
println(map2 + map1) // {1=c, 2=b}


// Mapping maps

```
### Nullable type
Nullability is important because we get rid of null pointer exceptions.

```kotlin
val s1: String? = null // question mark allow s1 to accept nulls
// When we havea nullable type we can threat in two ways
// 1. Safe Access (? sign)
val len: Int? = s1?.length // SAFE ACCESS - this is like running if (s1 != null) { return s1.length }
val len: Int  = s1?.length ?: 0 // ?: returns 0 instead of null as default
// 2. Non-null exception (!! sign) - Try to avoid this!
s1!!.length // throws a kotlin.KotlinNullPointerException if s1 is null

// For list
val l: List<Int>? = null           // list can be null
val l2:List<Int?> = listOf(null)   // elements in the list can be null
    
// how they are implemented under the hood?
// they use annotations and no wrappers like Java Optionals
fun foo(): String = "foo" // compiles to @NotNull public static final String foo() { return "foo"; }
fun bar(): String? = "foo" // compiles to @Nullable ...

// Casting
// as  returns ClassCastException if the cast is unsuccesfull
// as? returns null
val x: Any? = 1
val y: Int? =  x as Int //if (x is Int) x else null
// smart cast
val z = "ciao"
val z2 = if (z is String) z.toUpperCase() else "" // Smart cast

## Exceptions
no different between checked and not checked exceptions.
There is no need to use the java @Throws(IOException::class) in Kotlin as we do in Java
```kotlin
// throw is an expression
val n = 200
val e = if (n in 0..100) n else throw IllegalArgumentException("here we go! $n")

// try is an expression too

val t: Int? = try {
  Integer.parseInt("ciao")
} catch(e: NumberFormatException) {
  null
}

```

## Functions
```kotlin
// this is one way to define a fuction
fun myFunction(a: Int, b: Int) : Int = a + b

// Unit is like void. it can be omitted as returned type if we do no return anything
fun myFunction(a:Int) {
  println(a)
}
```
### Template
```kotlin
fun <T> identity(a: T) = a
println(identity(10))
```    

In extensions
```kotlin
class Test {
    fun <A,B> A.to(that: B): Pair<A, B> = Pair(this, that)
}

fun main(args: Array<String>) {
    val t = Test()
    println(t.to(10)) // returns the Pair(t, 10)
}
```

### Infix - allow you not to have to call a method without .
```kotlin
class Test {
    infix fun noDotHere(i: Int) = i
}

fun main(args: Array<String>) {
    val t = Test()
    println(t noDotHere 10)
}
```

## Classes
Constructors
```kotlin
// Primary constructor. constructor visibility modifier can be omitted
class MyClassConstructors public constructor (val first: String, val second: String) {
   constructor(first: String) : this(first, "") // secondary constructor
}
// the above can be re-written as
class MyClassConstructorsCleanedUp  (val first: String, val second: String = "") 

// this class cannot be instantiated
class ThisClassCannotBeInstantiated private constructor() 

val a = MyClassConstructors("test")
val b = MyClassConstructors("test", "test2")
val c = MyClassConstructors(second="test2", first = "test1")
```
Init blocks
```kotlin
class MyClass(name: String) {
   val firstProp = "first $name".also(::println)
   init {
      println("This is printed just when this class is instantiated")
   }

   init {
      println("and again this will be printed after the first init")
   }
}
```

Inheritance
```kotlin
open class BaseClass(num: Int) {
    // Overridable and not functions
    open fun myFun(): Int = 3
    final fun notOverridableFunc() = 5 // actually final is redoundant classes and methods are final by default

    // Overiddable and not properties
    open val x = 3
    
    protected open val protectedY = 4
    private val privateY = 4
}

class DerivedClass(num: Int) : BaseClass(num) {
    override fun myFun(): Int = 5
    fun callBaseMyFun() = super.myFun() // We can call base class methods using super
    override var x = 4 // Note we can override a val with a var. But no viceversa
    
    // overrides private and protected
    private val privateY = 4
    override val protectedY = this.privateY
}

fun main(args: Array<String>) {
    val dc = DerivedClass(1)
    dc.callBaseMyFun()
}
```

Inner classes
```kotlin
class MyClass {
    fun foo() = 4
    inner class InnerClass{
        fun bar() = foo()
    }
    val inn = InnerClass()
    fun bar() = inn.bar()
}

fun main(args: Array<String>) {
    val dc = MyClass()
    println(dc.bar())
}
```

Abrstact classes
```kotlin
open class MyClass {
    fun x() = 3
}
abstract class AbsClass : MyClass()

fun main(args: Array<String>) {
    val dc = MyClass()
    //val abs = AbsClass()  You cannot create instance of an abstract class
}
```

Companion Objects
```kotlin
```

### Enumerations
```kotlin
enum class RGB { RED, GREEN, BLUE }
```

## Control structures
### WHEN
```
enum class RGB { RED, GREEN, BLUE }

fun main(args: Array<String>) {
    fun check(a: Any): String = when (a) {
        RGB.BLUE -> "blue"
        is Int -> "Integer"
        else -> "I dunno"
        }
    println(check(1)) // Integer
}
```
### IF
```kotlin
val x = 9
val y = if (x>=10) "bigger" else "lower" // y == lower
```
### Loops
```kotlin
// looping an array
for (s in arrayOf(1,2,3)) {
       println(s)
}

// looping a map
val map = mapOf( 1 to "a", 2 to "b")
    for ((key, value) in map) {
        println ("$key and $value")
    }

```

### IN
```kotlin

```

## Extension functions
Extensions re Java static functions.
Extend a class. 
Defined outside the class.
Kotlin extension are seen as static functions in java. 
Extension cannot call private members of the extended clas.
Kotlin STD lib is just an extension of the Java's one.

simple example:
```kotlin
infix fun <T> T.eq(other: T) {
  if (this == other) println("ok")
    else println("error")
}
11 eq 10
```

```kotlin
// extendedFunction.kt
package org.gnuton.hellognuton
fun String.lastChar() = this.get(this.length -1)

// main.kt
import org.gnuton.hellognuton.lastChar
fun main(args: Array<String>) {
    println("ciao".lastChar())
}
```
.javaClass member returns the corrispective java function. It's analogous to the Java's set.getClass()
```kotlin
hashSetOf(1,2,3).javaClass // returns java.util.HashSet
```

## Functional Programming
### Lambdas
```kotlin
// lambdas are usually wrapped in {}
val f = {x: Int, y: Int -> x+y } 

// we can avoid to explicitely declrare the type\
listOf(-1,1,2,3).map {i -> i > 0}

// we caan avoid to name the var if we use 'it'
listOf(-1,1,2,3).map {it > 0}

// in a lambda the last value is always returned
listOf(-1,1,2,3).map {print(it); it > 0}

// Decomposing
// we call _ the var which we do not use
mapOf( "one" to 1).map { (_,value) -> "$value" } // [1]

```
### Common operations on collections
Thsoe operations (filter, map, groupBy, count, any, ..) are defined in the kotlin std lib as extention functions
```kotlin
// Filter - keeps the element satisfing the predicated

// map - applies a function to a collection and returns a new collectin

// any - Returns true if at least one element matches the given predicate.
// all -  Returns true if all of one element matches the given predicate.
// none - Returns true if none of one element matches the given predicate.

 // find/first/firstOrNull - Returns the first element matching the predicate
 listOf(1,2,-3, -4).find {it < 1} // returns -3
 listOf(1,2,3, 4).find {it < 1} // nulll
 listOf(1,2,3, 4).first {it < 1} // java.util.NoSuchElementException
 listOf(1,2,3, 4).firstOrNull {it < 1} // null
 
 // count - returns the n of elements matching the predicate
 listOf(-1,-2,3, 4).count {it < 1} // 2
 
 // partition - returns a pair of lists one matching and the other not the predicate
 listOf(-1,-2,3, 4).partition {it < 1} // ([-1, -2], [3, 4])
 
 // groupBy - 
 listOf("Antonio", "Fabio", "Carlo").groupBy { it.length} // {7=[Antonio], 5=[Fabio, Carlo]}
 
 // assiociateBy
class Person(val name: String, val age: Int)

fun main(args: Array<String>) {
    val friends = listOf(
            Person("Alice",31),
            Person("Carl", 31),
            Person("Sam", 22))
    val a = friends.associateBy { it.name } // Map<String, Person>
    val b = friends.associateBy({it.name}, {it.age}) //Map<String, Int?
}

// zip
 val b = listOf("a","b","c","d")
 val c = 1..4
 val ab = c.zip(b) // [(1, a), (2, b), (3, c), (4, d)]
 
 
```

## IntelliJ templates
IntellJ comes with a few templates for kotlin too.
You can add more templates from File > Settings > Search for "Template" > Live Template > Choose "Kotlin"
```
psvm -> fun main(args: Array<String>) {}
sout -> println()
```
