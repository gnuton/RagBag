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
* Arithmetic operators (+ - * / % ++ --)
* Assignment operators (= += -= *= /= %= |= ^=  >>= <<=)
* Comparison operators (== != < > >= <=)
* Logical operators (&& || !)
* Bitwise operators
```java

```
### Strings
```java
        String a = "ciao";
        a.length(); // size
        a.toCharArray();
        a.toLowerCase();
        a.indexOf('c'); // returns the position of the char 'c' or -1
        a.indexOf("c"); // returns the position of the string "c" or -1
        String b = "a" + "b"; //concatenation
        String c = "a" + 20; //"a20"
```
### Math
Basic math functions are in the Math package: https://docs.oracle.com/javase/8/docs/api/java/lang/Math.html

### Conditionals
```java
// if else
if (condition1) {
  // block of code to be executed if condition1 is true
} else if (condition2) {
  // block of code to be executed if the condition1 is false and condition2 is true
} else {
  // block of code to be executed if the condition1 is false and condition2 is false
}

// switch
switch(expression) {
  case x:
    // code block
    break;
  case y:
    // code block
    break;
  default:
    // code block
}

// while
while (condition) {
  // code block to be executed
}

// for 
for (int i = 0; i < N; i++) {
  // code block to be executed
}

// break and continue
loops can be stopped or steps can  be skipped 
```
### Data structures

#### Array
* fixed size
```java
        String[] stringArray = {"ciao"};
        Integer[][] multidimensinoalArray = {{1,2},{3,4}, {5}, {}};
        stringArray[0] = "test";
        int stringArrayLength = stringArray.length;
        for (int i=0; i < stringArrayLength; i++) {
            // do stuff with stringArray[i]
        }
        for (String s : stringArray) {
            // do stuff with s
        }
        // to print the values in an array we use Arrays.string
        System.out.println(Arrays.toString(my_array))
```
#### Collections
Most of  data structures in java belongs since Java 2.0 to the collection framework.
Please have look at the collection chapter for more info.

### Exceptions
```java
try {
  //  Block of code to try
}
catch(Exception e) {
  //  Block of code to handle errors
}
```
## 2 Classes

## 3 Concurrency
## 4 Collections
Introduced in Java 2.
Collection framework is made of:
* Interfaces - Abstract data types
* Classes - Implementation of the interfaces
* Algorithms - methods performin useful computations

### 4.1 Interfaces
1. The root - public interface Collection<E> extends Iterable<E> has method(add,remove,addAll,removeAll,clan...)
2. List Interface 
3. Set Interface
  * Sorted Set - extends Set
4. Map
  * SortedMap
5. Enumeration (obsolete)

### 4.2 Classes
It's a set of classes which full or (Abstract) partially implement the collection interfaces.
AbstractCollection, AbstractSet, AbstractList, AbstractSequentialList and AbstractMap provide skeletal implemetnation to the core collection interfaces.
The fully implemented classes are:
1. LinkedList/ArrayList
2. HashSet/TreeSet
3. HashMap/TreeMap/WeakHashMap/LinkedHashMap/IdentityHashMap
```java
        // LinkedList
        Integer[] array = {1,2,3};
        List linkedList = Arrays.asList(array); // asList returns an ArrayList as List
        List linkedList2 = new LinkedList<Integer>(linkedList); // can take another collection in the constructor.
        linkedList2.add(1); // append. Same as addLast
        linkedList2.add(1,0); //prepend - same as addFirst
        List linkedList2ShallowCopy = (List) ((LinkedList) linkedList2).clone();
        linkedList2.get(0); // get element 0
        linkedList2.indexOf(1); // search element 1 in the list and returns the position index
        linkedList.size();
        linkedList2.remove(1); // remove the element at position 1
        linkedList2.remove((Integer)1); // search and remove element 1
        linkedList.toArray();
        linkedList2.clear();
        linkedList2.add(1);
        linkedList2.add(31);
        linkedList2.removeIf((x)-> (int)x > 30); // just like filter in streeams but not lazy
        linkedList2.contains(1);
        Stream s = linkedList2.stream(); // return a stream
        Stream ps = linkedList2.parallelStream(); // returns a parallel stream

        // ArrayList
        List arrayList = new ArrayList(8); // set to 8 the initial capacity
        arrayList.add(2);
        arrayList.add(0,1);
        ((ArrayList) arrayList).trimToSize();
        // the rest of methods are pretty much the same as LinkedList above
        System.out.printf("the array list %s", arrayList);
        
        // HashSet/TreeSet
        Set hashSet= new HashSet<Integer>(); // unsorted. items are hashed and stored. The hash is used as index.
        Set treeSet = new TreeSet<String>(); // sorted. items stored in a tree.

        // HashMap/TreeMap/WeakHashMap/LinkedHashMap/IdentityHashMap
        Map hashMap = new HashMap();
        hashMap.put("key1", "value1");
        hashMap.containsKey("TheKey");
        hashMap.containsValue("TheValue");
        Set set = hashMap.entrySet(); // return mapping contained
```
#### Comparator
Comparator is the toCompare method which you should implement when you extend a abstract subclass.

#### Iterator

### 4.3 Algorithms
It's a set of algorithms usefull to extend the abstract classes.

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
* do not modify the input
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
