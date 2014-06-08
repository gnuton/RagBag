# Javascript #

## Inheritance in objects and classes ##

### Objects inheritance  ###
Every javascript object derives from Object
````
> Object
> function Object() { [native code] }
````

Now we define two objects and we make one inherith the other one.

````
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

````

### Classes inheritance  ###

