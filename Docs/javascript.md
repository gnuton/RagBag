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

### XXX ###
```js
```

## Inheritance & objects ##


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


// Deleting a field from antonio will reset the value to the one defined in the base object
// antonio.name == "antonio" at beginning. Let's delete it!
delete antonio.name;
// now antonio looks like this Object {name: "no name", age: 0, newfield: true}
// where name="no name" which is the default value set in the base object for the "name" field.

```

### Classes inheritance  ###
Well... there are no classes in Javascript. As we have already seen in the previous chapter in Javascript we have "PROTOTYPES".
Methods live in prototypes:
```js
// Let's create a funciton object or "costructor"
function Cat(name){ this.name = name}

// this creates by default a prototype.
Cat.prototype; // prints out Cat{}

// let create an new instance
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
MyClass.myStaticMethod = function() { ... }


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
