# Kotlin
## Variables
### Val & Vars
```
var x =
val y =
```
##

## Functions
```
```
## Classes
### Enumerations
```
enum class RGB { RED, GREEN, BLUE }
```

## Conditionals
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

## IntelliJ shortcuts
Write the first string and press TAB to expan it to the code on the right side.
```
psvm -> fun main(args: Array<String>) {}
sout -> println()
```
