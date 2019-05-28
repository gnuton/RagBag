# Java
## The good old Java

## Java wrapper classes
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

## Java 8
### Stream API
```java
```

## Unit testing
