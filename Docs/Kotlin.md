# Kotlin

## Variables
### Val & Vars
```
var x =
val y =
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

## Functions
```
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
