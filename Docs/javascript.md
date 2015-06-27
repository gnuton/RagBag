# Javascript #

![logo](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/JavaScript-logo.png/768px-JavaScript-logo.png)

## Output ##
```js
// 1. to console
console.log("helloWorld"); // <-- each statement in javascript is separated by semicolons
// 2. to window
window.alert("hello world");
// 3. to DOM
document.write("hello world");
```

## Javascript statements ##

```js
// Statements are separated by semicolons
// statements are made by literals, operators, keywords and comments
var a = 3;
// statements can have:
// Literals (numbers, strings, Expressions), those can be changed are called variables.
1
1.0
"hello"
1 + 3 // expression. + is called OPERATOR.
var a = 3; // var is a KEYWORD. Variable names are usually camelCaseInJavascript! 
// this is a comment..
/* This is a multiline
   comment
 */

// do not forget that JAVASCRIPT IS CASE SENSITIVE. Those are two different var definitions
var helloWorld = 1;
var helloWorld = 1;

// Unicode is used by default in JS
```
### Variables and Types ###
```js
// JS has DYNAMIC TYPES: the very same variable can contain many types. 
var a = 1;
a = "ciao";

// TYPES
1.0 // number
1   // number
"this is a string" // string
false // boolean
true // boolean
["ciao", "io"] // array
{name:"antonio, surname: "aloisio"} // objects
null // is an null object so: null == undefined is true. null === undefined is false because they are different types
undefined // undefined type
// we can use typeof to get the type name
typeof("ciao"); // returns "string"
typeof(NaN); // "number" eg: 1 * undefined = NaN
typeof(function a(){}); // returns "function"

// redeclaring a variable doesn't reset the variable itself.
var a; //a still holds the string "ciao"
var b; // when we defined a new variable it's value is undefined. where udefined is a null type.
a=undefined;

// Opeartions
var a = 1 / 3  // split two integers give a float 0.333
var a = "ciao" + 2 + 3 // "ciao23". this 2 and 3 are converted to string and concatenated to ciao. ou
```

### Operators ###
```js
// 1. Arithmetic
1+1 // 2 - addition
1-1 // 0 - subtraction
3*2 // 6 - multiplication
3%2 // 1 - modulus
3/2 // 1.5 - division
// increment & decrement
var a=1;
++a // or a++ increment by 1
--a // or a-- decrement by 1

// 2. Assignement operators
a = 5  // assign 5 to a
a += 5 // increment a by 5
a -= 5 // decrement a by 5
// and so on with other arithmetic operators

// 3. Logical operators
a == b // equal  to
a === b // equal value and equal type
a != b // not equal to
a !=== b // not equal type and not equal value
a > b // greater than
a < b // less than
a >= b // greater or equal to
a <= b // less or equal to

// 4. Boolean operators

```
## Functions ##
In JS we can use functions as declaration (1) or expressions (")
```js
// Function declaration
function myFunc(arg1, arg2) { return arg1 * arg2; }
a = myFunc(1,2) // a holds 2
a = myFunc // a holds myFunc

// Function expression
var myFunc = function (arg1, arg2) { return arg1 * arg2 } // this is called also Anonymous function

//
```
Any function in javascript is an instance of Function Object
```js
// We could instantiate a function using Function costructor (but DO NOT DO THAT! :D)
var myFunc = new Function("arg1", "arg2", "return arg1 * arg2")
myFunc(2, 3); // returns 6
```
Arguments are passed by value and objects by reference
```js
// argument passed by value
var a=3;
function b(x){x=4}
b(a) // a is still 3

// object passed by reference
var a = {b:1} 
function c(d){d.b = 3}
c(a) // the function c modifies b in the object { b: 3 } referenced by a
```
JS doesn't check argument type nor the number of arguments passed to a function.
```js
function f(a1, a2, a3) { console.log( a1 + " " + a2 + " " + a3)}
f(1,2,3) // prints out: 1 2 3
f(1,2) // prints out: 1 2 undefined
f(1,2,3,4,5) // prints out: 1 2 3
```

JS is a crazy language. Even if you don't define any argument for a function, you can still pass N of those
```js
function a(){
  for (i in arguments){
    console.log(arguments[i] + " \n");
   }
}
a(1,2,3,4,5); // yes this works! :D
```
JS doesn't really support default arguments, but we can have them
```js
function f(arg1) {
  if (!arg1) 
    arg1 = -1; 
  console.log(arg1);
}
f(); // -1
f(2); // 2
```
JS supports self invoking function
```js
// syntax: (THE-LAMBDA-FUNCTION)() 
> (function(){console.log("CIAO")})() // prints CIAO
```

### Function closures ###
A closure is an inner function that has access to the outer (enclosing) function's variables—scope chain. 
The closure has three scope chains: it has access to its own scope (variables defined between its curly brackets), it has access to the outer function's variables, and it has access to the global variables.
```js
var add = (function(){ // closure scope
  var counter = 0; // outler enclosed var
  return function(){ return ++counter;} // closure inner function
})()
add() // return3 1
add() // return3 2
add() // returns 3
```

Hoisting is a JS feature that moves the declaration (not initialization) of the variables at the top.
```js
// the followig code is valid.
x = 5
var x; // the declaration of x is moved to the top

// if x is initialized, then it's not moved at the top
console.log(x); // this will fail
var x = 5; // this is not moved at the top
```

We could instantiate a function using Function costructor (but DO NOT DO THAT! :D)
```js
var myFunc = new Function("arg1", "arg2", "return arg1 * arg2")
myFunc(2, 3); // returns 6
```


## objects ##
Objects are variables containing many values
```js
// an object can be created in 3 ways
// 1. from literal
var myObject = { property1: "1", property2: "2", method1: function(){return "ciao"}}
// 2. using keyword new
var myObject = new Object();
myObject.property1 = 1;
// 3. using an object constructor
function myObject (prop1, prop2, method1) {this.property1 = prop1; this.property2 = prop2; this.method1 = method1;}
var a = new myObject(1, 2, function(){return "ciao"})

// they keyword THIS. Yes this is not a variable, since it cannot be modified.
this = 3; // ReferenceError: Invalid left-hand side in assignment
this; // returns the reference to the object parent of the current code
      // In a browser it could be Window {top: Window, location: Location, document: document....
      // In nodejs it prints all the children of the global object
// this in a constructor function doesn't have any value, but it will get the value of the object once created

// Invoking a function as method
// we can use Function.apply if the argument is an array
// we can user Function.call if we hav more argument
function f(a){ console.log(a) } // let's define a simple function
f.apply(global,[2]); // we can invoke the function passing an context object (eg: global) and an array of args
f.call(global,2); // or just the same thing passing the values as separate arguments.

// here is the list of JS built-in constructors
var x1 = new Object();    // A new Object object
var x2 = new String();    // A new String object
var x3 = new Number();    // A new Number object
var x4 = new Boolean()    // A new Boolean object
var x5 = new Array();     // A new Array object
var x6 = new RegExp();    // A new RegExp object
var x7 = new Function();  // A new Function object
var x8 = new Date();      // A new Date object
// but using primitives is better because faster
var x1 = {};            // new object
var x2 = "";            // new primitive string
var x3 = 0;             // new primitive number
var x4 = false;         // new primitive boolean
var x5 = [];            // new array	object
var x6 = /()/           // new regexp object
var x7 = function(){};  // new function object

// access to object methods and members
myObject.property1; // returns the value of property1
myObject["property2"]; // returns the value of property2
myObject.method1(); // execute the method and returns "ciao"
myObject.property1 = 3; // OBJECTS ARE MUTABLE!!

// Add and delete properties
var x = {a:1, b:2}
x.c = 3; // add a property to the object x
delete x.c; // remove the property c from x

// looping properties
var x = {a:1, b:2}
for (i in x) {
  console.log(i); // reading value
  x[i] = 4; // writing value
}

// Copying objects:
var a = {b: 1};
var c = a; // c is NOT a copy of a. It's addressed by reference, not by value
c.b = 3; // the the following will be true: c.b === a.b

// Object properties attribute
// 1. Value - store the value
// 2. Writable - (true/false) - if false, value cannot be changed
// 3. Enumerable - (true/false)- if true for (i in theObject) and Object.keys(theObj) work
// 4. Configurable - (true/false) - if true the object can be deleted
var x = {prop1: 1}
var xAttrs =Object.getOwnPropertyDescriptor(x, "prop1") // returns Object {value: 1, writable: true, enumerable: true, configurable: true}
// we can change property attributes in this way
Object.defineProperty(x, "prop1", {writable: false}); // to make a property not writable
Object.defineProperty(x, "ciao", {enumerable: false}) // Object.keys(x) will now return []

```

### Objects inheritance  ###
Every javascript object derives from Object
```js
> Object
> function Object() { [native code] }
```

Now we define two objects and we make one inherith the other one.

```js
// Create base obj: Object {name: "no name", age: 0}
var person = {name: "no name", age: 0}

// Create a new obj: Object {name: "antonio"}
var antonio = {name: "antonio"}

// Set person base object for "antonio"
// Antonio will look like: Object {name: "no name", age: 0}
// it will inherit other fields defined in the base class
antonio.__proto__ = person

// if we add a new field to person it will be added to the inherited classes too
person.newfield = true;
// antonio now looks like this: Object {name: "antonio", age: 0, newfield: true}

// Deleting an a a field from antonio will reset the value to the one defined in the base object
// antonio.name == "antonio" at beginning. Let's delete it!
delete antonio.name;
// now antonio looks like this Object {name: "no name", age: 0, newfield: true}
// where name="no name" which is the default value set in the base object for the "name" field.

```

### Classes inheritance  ###
Well... there are no classes in Javascript. As we have already seen in the previous chapter in Javascript we have "PROTOTYPES".

Before going forward let's clarify the difference between Object.__proto__ and Object.prototype.
```js
var foo = function(){this.a=1};
var a = new foo; // Instanciate the object { a: 1 }
a.__proto__; // is {}. which is foo.prototype, and it is the actual object that is used in the lookup chain to
             // resolve methods and so on. It's an internal property.
a.prototype; // is undefined for objects. This is the object that is used in order to build __proto__ when you create an object with new
foo.prototype; // {}. prototype is then available only to functions, Infact it's a property of function objects.
               // it's the prototype that the function builds.
foo.__proto__; // [Function: Empty] 
```

Methods and properties live in prototypes:
```js
// Let's create a funciton object or "costructor"
function Cat(name){ this.name = name}

// this creates by default a prototype.
Cat.prototype; // prints out Cat{}

// let s create a new instance
var tom = new Cat("tom")

// if we set a field or method into the Cat.prototype that will be available to tom and other derived objects
Cat.prototype.age= 10

// now tom contains Cat {name: "tom", age: 10}
```

Douglas Crockford makes some analogies between a standard concept of class with its static/private/public methods and Javascript objects.
In Javascript there are no scope modifiers: "private"/"public"/"protected".
JavaScript functions are first-class objects, that means you can treat them just like any object.
```js
// We define a "constructor" function with a private variable and a privileged method
// privileged method are similar to what other languages call "public". They have access to private members
function MyClass() {
  var priv = 1; 
  this.myPrivilegedMethod= function(){console.log("myMethod")}
}

// public methods in JS are added outside the object itself through the prototype
// Properties:
// - "this" keyword refers to MyClass
// - cannot access to MyClass private members. It can access only other "privileged" or "public" members
// - every instance of MyClass (created and future ones) will get this public method.
MyClass.prototype.myPublicMethod = function() {console.log("public metdhod"); }

// static method. are defined as follow and they do not have any relation with the instances we create of our class
MyClass.myStaticMethod = function() { ... } // { [Function: MyClass] myStaticMethod: [Function] }

```

## Coding style ##
```js
// Camel case. Hypen not allowed: it's a reserved char
var helloWorld = 1;

// spaces around operators (= + - / *)
a = 1 + 1;

// As many other languages lines should not be longher than 80 chars
```

## References ##
- Prototypal Inheritance in JavaScript http://javascript.crockford.com/prototypal.html
