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

String.format("%d %f %s %c",12, 1.2, "anotherString",'c');
"ciao bello".replace(" ",""); // removes spaces

// Transform String to List of chars using streams.
List<Character> chars = s.chars().mapToObj(c -> (char) c).collect(Collectors.toList());

// substring
"123456".substring(1)   // 23456
"123456".substring(1,3) // 23

// regexps 
// match
Pattern p = Pattern.compile("\\w+");
boolean ris = p.matcher("ciao").matches(); // True

// find
Pattern p2 = Pattern.compile("[a-z]+");
Matcher matcher = p2.matcher("123ciao456bello");
while (matcher.find()) {
  System.out.println(String.format("substring:%s found. Start: %d Ends: %d", matcher.group(), matcher.start(), matcher.end()));
}

// the powerfull replace
"ciao bello!".replaceAll("(\\w)(\\w*)", "$2$1ay"); // "iaocay ellobay!"
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
```java
// Package
// to create a package create a folder, and inside the folder create classes with
// package TheNameOfTheFolder
// as first line

import testPackage.*; // Import all Classes in the package
import testPackage.TestClass; // import only TestClass from the package testPackage

abstract class MyAbstractClass {
    final int z = 10;
}
public class MyClass extends  MyAbstractClass { // Inheritance -
    int x = 5; // Attribute or Field -  variable inside the class
    int y;

    // Modifier - define access policy for fields and methods
    // 1 Access Modifers
    // - public (default) - accessible by all classes
    // - protected - accessible by classes in the same package and subclasses
    // - privete - accessible only inside the class itself
    // 2 Non-Access Modifiers
    // For Classes:
    // - final - cannot be inherited by other classes
    // - abstract - must be inherited to crate other classes
    // For attributes and methods
    // - final - attributes cannot be modified and methods cannot be overridden
    // - static - attributes and methods accessible without class instance
    // - abstract - only for methods in abstract classes
    // - transient - attributs and methods are skippped when serializing objects
    // - synchronized - methods that can be accessed only by one method at the time
    // - volatile - attribute always read from the "main memory" and never from the thread cache
    public static void main(String[] args) {
        MyClass myClass = new MyClass();
        // . is used to access methods and fields
        myClass.x = 10;
        final String res = myClass.myMethod();
        final String res2 = MyClass.MyMethod2(); // even static methods are called by .
    }

    public MyClass(){ // Constructor - a special method which is called when new MyClass is called
        y = 10;
    }

    public MyClass(int y){ // Constructor cant take params. A class can have multiple cosntructors
        this.y = y;
    }

    private String myMethod(){ // Method - function inside the class
        return "I'm justa method";
    }
    public static String MyMethod2() {
        return "oh boy I'm a private method";
    }

    // Encapsulation - Hides sensitive data from users
    private int myAttributeToEncapsulate;

    public int getMyAttributeToEncapsulate() {
        return myAttributeToEncapsulate;
    }

    public void setMyAttributeToEncapsulate(int myAttributeToEncapsulate) {
        this.myAttributeToEncapsulate = myAttributeToEncapsulate;
    }
}

// Polymorphism - achieved when two or more classes use extends the same interface or base class
//                and use the same method to perform different tasks
//              - Classes cannot extend multiple abstract classes
abstract class base {
    abstract void myMethod();
    final void methodWhichCannotBeExtended() {}
}
abstract class base2 { }

class derived1 extends base{
    @Override
    void myMethod(){} { }
    // @Override  <-- we cannot use override here bucause it doesn't override anything
    void xxx(){}
}

class derived2 extends  base {
    @Override
    void myMethod() { }
}

// Interface - Along with Abstract classes it's another way to achieve abstraction in java
//           - class can implements multiple interfaces
interface MyInterface1 {
    int x = 0; //Fields are by default static, public and final
    // no costructor allowed
    void myMethod(); // Methods are by default public and abstract
    void myOtherMethod();
}

interface MyInterface2 {
    int y = 4;
}

class MyInterfaceImplementation implements MyInterface1, MyInterface2 {

    @Override
    public void myMethod() { }

    @Override
    public void myOtherMethod() { }
}

// Enumerations
enum MyEnum {
    FIRST,
    SECOND
}

// Usage
// MyEnum myEnum = MyEnum.FIRST;
```
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
// merging streams
Stream<Integer> stream1 = Stream.of(1, 3, 5);
Stream<Integer> stream2 = Stream.of(2, 4, 6);

Stream<Integer> resultingStream = Stream.concat(stream1, stream2);

// Count, filter, map, reduce
Arrays.asList(1,2,3).stream().count(); // 3
Object[] y = Arrays.asList(1, 2, 3).stream().filter((x) -> x <= 2).toArray(); // [1,2]
Object[] y = Arrays.asList(1, 2, 3).stream().filter((x) -> x <= 2).findFirst().orElse(-1); // 1  Returns the first element matching or -1
Object[] z = Arrays.asList(1,2,3).stream().map(x-> x+1).toArray(); // [2,3,4]
int sum = Arrays.asList(1,2,3).stream().reduce(0,(acc, val) -> acc + val); // 6. Reduce an array of T. Outputs a T

// Collectors
// Collectors.toList, Collectors.ToSet, collectors.toCollection
List<Character> toListCollect = Arrays.asList('a', 'b', 'c').stream().collect(Collectors.toList()); // converts stream to list [1,2,3]
Set<Character> toSetCollect = Arrays.asList('a', 'b', 'c', 'b').stream().collect(Collectors.toSet()); // [a, b, c]
List<Character> toListCollector = Arrays.asList('a', 'b').stream().collect(Collectors.toCollection(LinkedList::new)); // [ab,b]
LinkedList<Integer> x = Arrays.stream(A).boxed().collect(Collectors.toCollection(LinkedList::new)); // int[] A  to  LinkedList<Integer>
Map<Integer, List<String>> integerListMap = Arrays.asList("1", "22", "333", "033").stream().collect(Collectors.groupingBy(String::length)); // {1=[1], 2=[22], 3=[333, 033]}
        
// String in streams
// Example 1 - join chars
justAString
    .chars() // generate a IntStream
    .mapToObj(x -> (char) x) // Convert to Stream<Character>
    .map(c-> m.get(c) > 1 ? ')' : '(' ) // Trasformation
    .collect(StringBuilder::new, StringBuilder::appendCodePoint, StringBuilder::append) // Join the chars
    .toString();
    
// Example 2 - joining strings
Stream<String> words = Arrays.stream(str.split(" "));
Function<String, String> transformString = (String x) -> x;
String s = words.map(transformString).collect(Collectors.joining(" "));

// statistics on numbers
String numbers = "8 3 -5 42 -1 0 0 -9 4 7 4 -4";
IntSummaryStatistics stats = Arrays.stream(numbers.split(" ")).mapToInt(Integer::valueOf).summaryStatistics();
System.out.println(String.format("max=%d min=%d", stats.getMax(), stats.getMin()));
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
