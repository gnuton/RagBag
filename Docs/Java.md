# Java
## 1 Core
### Comments
```java
// single line comment
/* Multiline comment 
 */
```
### Variables & Constants
All Java variables must be identified with unique names. These unique names are called <b>identifiers</b>
```java
// Variables
int myNum = 5;

// Constants
final int myConstantNum = 5;
```
### Data Types
Java types can be <b>primitive</b> and <b>non-primitive</b>
#### Primitive types
* cannot be defined by the developer
* never null
* primitive types name starts with lower case
* size dependes on the data

|type|size||
|---|---|---|
|byte	|1 byte	|Stores whole numbers from -128 to 127|
|short	|2 bytes	|Stores whole numbers from -32,768 to 32,767|
|int	|4 bytes	|Stores whole numbers from -2,147,483,648 to 2,147,483,647|
|long	|8 bytes	|Stores whole numbers from -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807|
|float	|4 bytes	|Stores fractional numbers from 3.4e−038 to 3.4e+038. Sufficient for storing 6 to 7 decimal digits|
|double	|8 bytes	|Stores fractional numbers from 1.7e−308 to 1.7e+038. Sufficient for storing 15 decimal digits|
|boolean	|1 bit	|Stores true or false values|
|char	|2 bytes	|Stores a single character/letter or ASCII values|

```java
float myFloatNum = 5.99f;
char myLetter = 'D';
boolean myBool = true;
String myText = "Hello";
```
#### Non-primitive types
* can be defined by the developer
* can be null
* non-primitive types never start with lower case
* all have same size
Eg String, Arrays, Classes ...

### Type Casting
* Widening casting - automatically performed
* Narrowing casting - manually performed

```java
// widening -    byte -> short -> char -> int -> long -> float -> double
// narrowing -   double -> float -> long -> int -> char -> short -> byte

int myInt = 9;
double myDouble = myInt; // Automatic casting: int to double
double myDouble = 9.78;
int myInt = (int) myDouble; // Manual casting: double to int
```
### Operators
perform operations on variables and values.

```java

```
### Strings
```java
```
### Math
```java
```
### Booleans
```java
```
### Conditionals
```java
```
### Arrays
```java
```
### Exceptions
```java
```
### 2 Classes

## 3 Concurrency
## 4 Collections
### Java wrapper classes
Needed by Generics. Incapsulate primitive types. 
List of primitive types and its wrapper: 
```java
boolean, byte, short, char, int, long, float, double 
Boolean, Byte, Short, Character, Integer, Long, Float, Double
```
To and from primitive values
```java
Integer x = 1; // bpxing 1 is wrapped
x.intValue(); // returns the primitive value
```

### autoboxing
```java
List<Integer> arrayList = new ArrayList<>();
arrayList.add(1); // autoboxing converts 1 to Integer(1)
```

## Generics
Introduced in Java 5

Why do we need them:
```java
List list = new LinkedList(); // Diamond operator avoid the casting belowList<Integer> list = new LinkedList()
list.add(new Integer(1)); 
Integer i = list.iterator().next(); // This doesn't work. it needs to be casted
```
Generic type argimens must be reference types (so no primitive ones).

TBC
## 5 Stream API
* do not modify its source
* all operations are lazily applied to the elements of the stream
* parallelStream allows to apply a function in parallel to the stream elements

```java
```
## 6 Java IO
## 7 Unit testing
```java
public class MyClassTest {
  @Test
  public void publicTest() {
    asserEquals(expectedValue, MyClass.theMethodToTest())
  }
}
```
## 7 Advanced
