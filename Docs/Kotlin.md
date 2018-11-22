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
## Ranges
```kotlin
val x: IntRange = 1..10 //
val y: IntRange = 1 until 10 // 1,2,3, ..., 9
```
## Array
## Maps
```kotlin
// immutable map
val imap = mapOf( 1 to "a", 2 to "b")

// mutable map
val mmap = mutableMapOf( 1 to "a", 2 to "b")
mmap[1] = "c"

val map1 = mutableMapOf<Int, String>()
val map2 = mutableMapOf<Int, String>()
map1[1] = "c"
map2.put(1,"a")
map2.put(2,"b")
println(map2) // {1=a, 2=b}
println(map1 + map2) // {1=a, 2=b}
println(map2 + map1) // {1=c, 2=b}
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
```
## Classes
### Enumerations
```
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

## IntelliJ shortcuts
Write the first string and press TAB to expan it to the code on the right side.
```
psvm -> fun main(args: Array<String>) {}
sout -> println()
```
