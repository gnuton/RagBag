# Kotlin
Kotlin is an opensource language (https://github.com/JetBrains/kotlin) developed and maitained by JetBrains.

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

/// way to access a map
val m = mapOf("a" to 1, "b" to 2)
val a = m.getValue("d") // returns null
val b =m["d"]           // throws exception

// getOrElse
mapOf("a" to 1, "b" to 2).getOrElse("f", {4}) //  returns 4 since f is missing in the map

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
```

### Function type
```kotlin
val sum = {x: Int, y:Int -> x+y}
val isEven: (Int) -> Boolean = { x:Int -> x %2  == 0}

// call lambdas
{ println("test") }()
// or
run { println("test")}

// this way we run kotlin lambdas in Java
val runnable = Runnable { println("this is a lambda in Java") }
runnable.run()

// nullability
val f1: () -> Int? = null       // won't compile
val f2: () -> Int? = { null }
val f3: (() -> Int)? = null
val f4: (() -> Int)? = { null } // won't compile
    
f3?.invoke() // allow us to run f3
if (f3 != null) { f3() } // same as the line above
```

store function reference in variables is possible for members and toplevel functions
thanks to function reference "::"
```kotlin
// A. you can store members in variables
class MyClass {
  fun aMember() { println("Hello method")}
}

val x = MyClass::aMember // MyClass:: is a called "Bound reference"
x(MyClass())

// B. you can store functions in variables if you use the function reference ::
fun aFunction() { println("Hello function")}
val y = ::aFunction // :: is an unbound reference
y()
```

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

Abstract classes
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

Data classes - have at least one constructor, hold data, are serializable and comparable by default.
[More info](https://kotlinlang.org/docs/reference/data-classes.html)
```kotlin
data class User(val name: String, val age: Int)
val x = DClass("A", 4)
val y = DClass("A", 4)
x == y // true. It would have been false if it was not a data class
x.toString() // serialize it to (a=A, b=4)

// copying data classes
data class Contact(val name: String, val age: Int)
val a = Contact("Tony", 29)
val b = a.copy(age = 30)
println("$a VS $b")

// Equals (==)VS reference equality (===)
    val c = setOf(1,2,3)
    val d = setOf(1,2,3)
    println(c==d) // true
    println(c===d) // false because the rerefence is different

    // equality with data classes
    data class myClass1(val x:Int)
    val e1 = myClass1(1)
    val f1 = myClass1( 1)
    println(e1==f1) // true
    println(e1===f1) // false
    //
    class myClass(val x:Int)
    val e = myClass(1)
    val f = myClass( 1)
    println(e==f) // false
    println(e===f) // false
```
 
class properties - kotlin exposes getter and setters (accessors) and this make the field (var x) a property.
```kotlin

    class Contact {
        var address: String = ""
            // overwrite the accessor for the property
            set(value) { // Accessor
                println("Field address changed $field")
                field = value
            }
            get() { // here another accessor
                return "xx"
            }
    }

    val c = Contact()
    c.address = "TEST"
    print(c.address)
```
 
 changing accessor visibility
 ```kotlin
 class Person {
        var age: Int = 0
            private set
    }
    val p = Person()
    // p.age=30 THIS FAILS
```    
lazy properties
```kotlin
 // lazy property - runs just once when called
    val l : String by lazy {
        println("Initialized")
        "I'M SO LAZY"
    }
  

    // lazy initialization
    class test {
        // restrictions:
        // - not val -> in java is not final
        // - myVar  is not nullable
        // - cannot be a primitive var
        lateinit var myVar: String
        fun onCreate() {
            myVar = "ok"
            println(myVar)
        }
        // println(myVar) // throws Kotlin expecting member declaration
    }
    val x = test()
    x.onCreate()
```
members can be..
```kotlin
 abstract class MyClass {
       // class members can be
       // public - visible everywhere - default
       // internal -  visible in the same module
       // protected - visible in subclass
       // private - visible in a class
       // but also: final (by default), open, abstract and override
       final fun x() = 3 // final is redundant.. since all functions are final by default
       open fun y() = 4  // open means not final
       abstract fun z() // means that the functions is not implemented
   }

   // more classes can live in the same file. Different than Java
   // package

```
Constructors
```kotlin
    // MyClass has primary contructor
    class MyClass1(val name: String)

    // you can specify the costructor body
    class MyClass2(name: String) {
        val name: String
        init {
            this.name = name
        }
    }

    // second constructor
    class MyClass3(val name: String) {
        public constructor() : this("second constructor") {}
        public constructor(x: Int) : this("third constructor") {}
    }
```
Inheritance
```kotlin
    // interface Base // cannot be local
    open class BaseImpl: Base // open is needed to make Child inherit BaseImpl
    class Child: BaseImpl()

    // Calling constructor of the parent class
    open class Parent(val name: String)
    class child(name: String) : Parent(name)
    // this is the same as
    open class Parent2(val name:String)
    class Child2 : Parent {
        constructor (name: String) : super(name)
    }
```

### Enumerations
```kotlin
enum class RGB { RED, GREEN, BLUE }
enum class Color(val r:Int, val g: Int, val b: Int) {
    BLUE(0,0, 255),
    ORANGE(255, 166, 0); // ; split members and methods
    fun rgb() = (r * 256 + g) * 256 + b
}
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
return can accept labels to force it to return a specific function
```kotlin
fun<T> duplicateNoZeroElements(list: List<T>) : List<T>{
   return list.flatMap thisIsALabel@{
   if (it == 0) {
      return@thisIsALabel listOf<T>() // we exit flatMap here. Same as return@flatMap listOf<T>()
   } else {
       listOf(it, it)
   }
}
duplicateNoZeroElements(listOf(0,1,2,3)) // returns [] if return doesn't have any label because return exits duplicateNoZeroElements function
```

### Common operations on collections
Thsoe operations (filter, map, groupBy, count, any, ..) are defined in the kotlin std lib as extention functions
```kotlin
// Filter - keeps the element satisfing the predicated

// map - applies a function to a collection and returns a new collectin

// any - Returns true if at least one element matches the given predicate.
listOf(1,2,3,4,5).any {it > 1} // true

// all -  Returns true if all elements matche the given predicate.
listOf(1,2,3,4,5).all {it > 1} // false

// none - Returns true if none of the elements matche the given predicate.
listOf(1,2,3,4,5).none {it > 1} // false

 // find/first/firstOrNull - Returns the first element matching the predicate
 listOf(1,2,-3, -4).find {it < 1} // returns -3
 listOf(1,2,3, 4).find {it < 1} // nulll
 listOf(1,2,3, 4).first {it < 1} // java.util.NoSuchElementException
 listOf(1,2,3, 4).firstOrNull {it < 1} // null
 
 // count - returns the n of elements matching the predicate
 listOf(-1,-2,3, 4).count {it < 1} // 2
 
 // partition - returns a pair of lists one matching and the other not the predicate
 val (lessThanOne, moreThanOne) = listOf(-1,-2,3, 4).partition {it < 1} // ([-1, -2], [3, 4])
 
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
 
 // MaxBy - to compare elements when they are not comparable
val heroes = listOf(
Hero("The Captain", 60, MALE),
Hero("Frenchy", 42, MALE), 
Hero("The Kid", 9, null), 
Hero("Lady Lauren", 29, FEMALE), 
Hero("First Mate", 29, MALE), 
Hero("Sir Stephen", 37, MALE))
heroes.maxBy { it.age }?.name // "The Captain" it could return null if heros is empty


```

## IntelliJ templates
IntellJ comes with a few templates for kotlin too.
You can add more templates from File > Settings > Search for "Template" > Live Template > Choose "Kotlin"
```
psvm -> fun main(args: Array<String>) {}
sout -> println()
```
