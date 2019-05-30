# Java
## 1 Core
## 2 Concurrency
## 3 Collections
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
## 4 Stream API
* do not modify its source
* all operations are lazily applied to the elements of the stream
* parallelStream allows to apply a function in parallel to the stream elements

```java
```
## 5 Java IO
## 6 Unit testing
```java
public class MyClassTest {
  @Test
  public void publicTest() {
    asserEquals(expectedValue, MyClass.theMethodToTest())
  }
}
```
## 7 Advanced
