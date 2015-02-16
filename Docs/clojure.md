# Clojure #
![logo](http://clojure.org/space/showimage/clojure-icon.gif)

Clojure is a dialect of the Lisp language created by Rich Hickey. It's a general-purpose function language and it runs in the JVM as well as in JS engines (ClojureScript).

## Getting started ##
### Create and run an app with lein ###
Lein (short for leiningen) is the de-facto building tool for clojure.

````
gnuton@Eva:/tmp$ lein new app clojure-noob      <--- This creates app template
gnuton@Eva:/tmp/clojure-noob$ tree
.
├── doc
│   └── intro.md
├── project.clj        <--- Configuration file
├── README.md
├── src
│   └── clojure_noob   <--- Dir which contains our app code
│       └── core.clj   
└── test
    └── clojure_noob
        └── core_test.clj

5 directories, 5 files

gnuton@Eva:/tmp/clojure-noob$ lein run        <-- runs the app we have just created
Hello, World!

````
### Create jar from clojure code to distribute ###
````
gnuton@Eva:/tmp/clojure-noob$ lein uberjar
Compiling clojure-noob.core
Created /tmp/clojure-noob/target/uberjar+provided/clojure-noob-0.1.0-SNAPSHOT.jar
Including clojure-noob-0.1.0-SNAPSHOT.jar
Including clojure-1.5.1.jar
Created /tmp/clojure-noob/target/clojure-noob-0.1.0-SNAPSHOT-standalone.jar

gnuton@Eva:/tmp/clojure-noob$  java -jar /tmp/clojure-noob/target/clojure-noob-0.1.0-SNAPSHOT-standalone.jar
````
### REPL ###
Or "Read-Eval-Print Loop" is the tool for experimenting with code.
````
gnuton@Eva:/tmp/clojure-noob$ lein repl
clojure-noob.core=> (-main)                     <--- runs the "-main" function in the namespace clojure-noob.core
hello
````

## Clojure syntax ##

### Documentation ###
As python even clojure has a "doc" command which allows you to read the documentation related to a clojure
````
user=> (doc doc)
-------------------------
clojure.core/doc
([name])
Macro
  Prints documentation for a var or special form given its name
nil

user=> (doc map)
-------------------------
clojure.core/map
([f coll] [f c1 c2] [f c1 c2 c3] [f c1 c2 c3 & colls])
  Returns a lazy sequence consisting of the result of applying f to the
  set of first items of each coll, followed by applying f to the set
  of second items in each coll, until any one of the colls is
  exhausted.  Any remaining items in other colls are ignored. Function
  f should accept number-of-colls arguments.
nil

````

### Namespace ###
By default clojure uses "user" as namespace
You can set your own one with:
````
(ns my.namespace)
````
File starts always with a namespace.

A namespace can contain
- (:import (org.something))
- (:require [...])
- (:use [])

#### Importing a namespace ####
Clojure can import clj and classes files in the CLASSPATH dirs.
````
user=> (println (seq (.getURLs (java.lang.ClassLoader/getSystemClassLoader))))
(#<URL file:/usr/share/java/clojure-1.2.1.jar>)

````

A. Require - Accepts namespace symbols and make them available to the namespace for later use
````
; in case we wanna use the plit function in clojure.string, this will fail
user=> (clojure.string/split "1,2,3" #",")
java.lang.ClassNotFoundException: clojure.string (NO_SOURCE_FILE:0)

; we have to import the namespace beforehand
user=> (require 'clojure.string)
nil
user=> (clojure.string/split "1,2,3" #",")
["1" "2" "3"]

; Importing multiple quoted symbols
user=> (require 'clojure.test 'clojure.string)
nil

; Importing a unknown symbol triggers an FileNotFound exception
; Here Clojure cannot find the file unknown_symbol.clj in the clojure dir of your classpath or JAR
user=> (require 'clojure.unknown_symbol)
java.io.FileNotFoundException: Could not locate clojure/unknown_symbol__init.class or clojure/unknown_symbol.clj on classpath:  (NO_SOURCE_FILE:0)

; namespace aliasing
user=> (require '[clojure.string :as string])
nil
; or you can alias it with
user=> (require ['clojure.string :as 'string])
nil

user=> (string/capitalize "foo")
"Foo"

; import libraries with the same prefix
user=> (require '(clojure string test))
nil

; See what happens under the hood when importing a lib
user=> (require 'clojure.string :verbose)
(clojure.core/load "/clojure/string")
nil


````
B. Use
   Use can bue used as "require" for aliases
   ````
   user=> (use '[clojure.string :as str :only [join split]])
   nil
   ````
C. Import
   imports java libs
   ````
   user=> (import 'java.util.Date)
   java.util.Date
   user=> (Date.)
   #<Date Thu Mar 27 13:23:50 EET 2014>
   ````
   
D. Require, Use & Import
   This is the way to import other people code
````
(ns my-great-project.core
   "This namespace is CRAZY!"
   (:use [clojure.string :only [split join]] :reload)
   (:require clojure.stacktrace
             [clojure.test :as test]
             (clojure template walk) :verbose)
  (:import (java.util Date GregorianCalendar)))
````

### Comments ###
Comment lines start with ';'
Comments blocks are defined like this:
````
(comment
  this is the comment block! :DD
)
````

### Vars ###
Clojure provides 4 mechanisms to maintain a persistent reference to a changing value
- Vars - refer to mutable storage location
- Refs
- Agents
- Atoms
````
; DEF creates a static a variable
user=> (def x)
#'user/x

; DEF binds the root to an initial value
user=> (def x 1)
#'user/x

; Dynamic variables - Vars are static by default
; def vs defn, the first are evaulate only once

````

### Private Vars, Functions###
````
(def- private-fun [] ...)
(def ^:private private-var ...)
````

### Types ###
'class' function returns the class name of an object
````
antonio=> (class nil)
nil

antonio=> (class true)
java.lang.Boolean

antonio=> (class 1)
java.lang.Long

antonio=> (class 1.1)
java.lang.Double

antonio=> (class "a")
java.lang.String

antonio=> (class +)
clojure.core$_PLUS_

user=> (class :a)
clojure.lang.Keyword
````

### Collections & Sequences ###
"Collections" are groups of data
"Sequences"  abstract description of list of data
              they can define infinite series
              --> seqs can be lazy, they need to provide an entry item when accessed
             (something like generators in python!)

1. Vectors/List Sequences and Collections - how to create them
  ````
  antonio=> (class ())
  clojure.lang.PersistentList$EmptyList
  
  antonio=> (class '(1 2 3))
  clojure.lang.PersistentList
  
  antonio=> (class [1 2 3])
  clojure.lang.PersistentVector
  
  ; what's a collection?
  antonio=> (coll? [1 2 3])
  true
  
  antonio=> (coll? '(1 2 3))
  true
  
  ; what's a sequence?
  antonio=> (seq? '(1 2 3))
  true
  
  antonio=> (seq? [1 2 3])
  false
  
  antonio=> (seq? (range 4))
  true
  ````

2. "Range" to generate sequences 
  ````
  ; range generates finite or infinite sequences 
  antonio=> (range 5)
  (0 1 2 3 4)
  
  antonio=> (take 3 (range 5))
  (0 1 2)
  ````

3. Adding elements 
  ````
  ; cons - adds item to the beginnig of a list or vector
  ; conj - adds item to collection in the most efficient way
  antonio=> (cons 4 [1 2 3])
  (4 1 2 3)
  antonio=> (cons 4 [1 2 3])
  (4 1 2 3)
  
  user=> (conj [1 2 3] 4)
  [1 2 3 4]
  
  user=> (conj '(1 2 3) 4)
  (4 1 2 3)
  ````

4. Concatenate lists and vectors
  ````
  user=> (concat [1 2] '(3 4))
  (1 2 3 4)
  
  user=> (concat [1 2] [3 4])
  (1 2 3 4)
  
  user=> (concat '(1 2) '(3 4))
  (1 2 3 4)
  ````

5. Reduce and Map operations
  ````
  ; reduce, runs an operation 
  user=> (reduce + [1 2 3 4])
  10
  
  ````

6. Flatten a sequence
  ````
  user=> (flatten [[1,2,3] [4,5,3]])
  (1 2 3 4 5 3)
  ````

#### Useful functions for sequences and collections ####
1. Map -  Returns a lazy sequence consisting of the result of applying f to the
          the set of items
  ````
  ; let's define a function 'a'
  user=> (defn a [i] (* i i))
  #'user/a
  
  ; let's apply 'a' function to the sequence.
  user=> (map a (range 4))
  (0 1 4 9)
  
  ````
2. Into-array/to-array
Create an array from an existing collection.
  ````
  ; let's define a vector
  user=> (def c [1 2 3]) 
  #'user/c
  user=> (class c)
  clojure.lang.PersistentVector
  
  ; to-array creates an array of objects
  user=> (class (to-array c))
  [Ljava.lang.Object;
  
  ; into-array creates an array of objects with the type of the first element
  user=> (class (into-array c))
  [Ljava.lang.Integer;
  
  ````

### Arrays ####
1. Create an array
  ````
  ;;; A - make-array - (multidimensinal) Arrays  
  user=> (pprint (make-array Integer/TYPE 3))
  [0, 0, 0]
  
  user=> (pprint (make-array Integer/TYPE 3 4))
  [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
  
  user=> (pprint (make-array Integer/TYPE 2 3 4))
  [[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
   [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]
  
  ;;; B - into-array - 
  See section 5 (from vector to array)
  ````

2. Get an element from an array
  ````
  user=> (def a (make-array Integer/TYPE 2 3))          
  #'user/a
  
  user=> (pprint a)
  [[0, 0, 0], [0, 0, 0]]
  
  user=> (pprint (aget a 0))
  [0, 0, 0]
  ````

3. Array length
  ````
  user=> (def a (make-array Integer/TYPE 2 3))          
  #'user/a
  
  user=> (pprint a)
  [[0, 0, 0], [0, 0, 0]]
  
  user=> (alength a)
  2
  
  user=> (alength (aget a 0))
  3
  ````

4. Set value at the index
  ````
  user=> (def a (make-array Integer/TYPE 2 3))          
  #'user/a
  
  user=> (pprint a)
  [[0, 0, 0], [0, 0, 0]]
  
  ; aset returns the set value
  user=> (aset a  0 1 11)
  11
  
  user=> (pprint a)
  [[0, 11, 0], [0, 0, 0]]
  ````

5. From vector & To Vector
  ````
  ;;;; Array => vector 
  user=> (def a (make-array Integer/TYPE 2 3))
  #'user/a
  
  user=> (class a)
  [[I
  
  ; here we convert the array to a persistent vector
  user=> (class (into [] a))
  clojure.lang.PersistentVector
  
  ; vector => Array
  user=> (class (into-array [1 2 3]))
  [Ljava.lang.Integer;
  
  ````

6. Flatten a multidimensional array
  Convert the array to vector with (into [] myArray) and use (flatten myVector)

### Maps ###
Types:
- Hash maps (no order, fast lookup)
- Array maps (when big becomes hash maps)
````
; Hash Map
user=> (class (hash-map :a 1 :b 2))
clojure.lang.PersistentHashMap

; Array Map
user=> (class {:a 1 :b 2})
clojure.lang.PersistentArrayMap
````
Key:
  Maps che use any hashable as key, but keywords (check Type chapter for more info) are better.

How to define a map & usage:
````
;;;;; INSTANTIATING A MAP ;;;;;
user=> (def keymap {:a 1 :b 2})
#'user/keymap

user=> keymap
{:a 1, :b 2}

;;;;;;; RETRIEVING VALUES ;;;;;;;;;;;;;;;
; a value can be retrieved in two ways
; - using the map as function
user=> (keymap :a)
1
; - (only for KEYWORDS) using the keyword to retrieve the value
user=> (:a keymap)
1

;;;;;;; ADD/REMOVE KEYS FROM MAPS ;;;;;;;;
; Add - Clojure types are IMMUTABLE.
user=> (def myMap {:a 1 :b 2})
#'user/myMap
user=> (assoc myMap :c 3)
{:c 3, :a 1, :b 2}

; remove
user=> (dissoc myMap :c)
{:a 1, :b 2}


;;;;;; GET ALL THE KEYS AND VALUE ;;;;;
user=> (def a {:a 1 :b 2})
#'user/a

; sequence of keys
user=> (map key a)
(:a :b)

; sequence of values
user=> (map val a)
(1 2)

;;;;;; ITERATING A MAP ;;;;
user=> (defn a [[k v]] (str k "-" v))
#'user/a
user=> (map a {:a 1 :b 2 :c 3})
(":a-1" ":b-2" ":c-3")

;;;;;; NESTED MAPS ;;;;;;
user=> (def c {:b {:a 1}})
clojure-noob.core=> (get c :b)
{:a 1}
clojure-noob.core=> (get-in c [:b :a])    <-- same as (get (get c :b) :a)
1

;;;;;; DEFAULT VALUES ;;;;;;
clojure-noob.core=> c
{:b {:a 1}}
clojure-noob.core=> (:d c)                      <-- :d is not found. returns nil
nil
clojure-noob.core=> (:d c "there is no val")    <- :d is not found. returns a default value
"there is no val"
````

### Sets ###

````
; defining a set
#{1 2 3}

; Set class name
user=> (class #{1 2 3})
clojure.lang.PersistentHashSet

; convert a Vector to set
user=> (set [1 2 3 4])
#{1 2 3 4}

; add member
user=> (def a #{1 2})
#'user/a
user=> (conj a 12)
#{1 2 12}

; remove member a is #{1 2 12}
user=> (disj a 12)
#{1 2}

; test for existence a is #{1 2}
user=> (a 1)
1
user=> (a 3)
nil

;
````

### Strings ###

````
; concatenation
(str "ciao " "bello")
````

### Data evaluation ###
(a b c) is a list, where a,b,c could be function or a var.
(1 2 3) throws a ClassCastException.
a literal list (Clojure won't evaulate it) can be defined as follow:
````
antonio=> '(1 2 3)
(1 2 3)

; eval evaluates literals
antonio=> (eval '(+ 1 2 3))
6

````

### Math ###
````
; allowed operations +, -, *, /
(+ 1 1)

; Equality
(= 1 1)
true

; nesting forms
(+ 1 (- 3 2))


````

### Functions ###
1. Define a function
  ````
  user=> (fn [] "Ciao")
  #<user$eval27$fn__28 user$eval27$fn__28@49b510b8>

  user=> (def a (fn [] "ciao"))
  #'user/a
  
  ; Shortened form
  user=> (defn a [] "ciao") 
  #'user/a
  ````

2. Call a function
  ````
  user=> ((fn [] "Ciao"))
  "Ciao"
  ; or
  user=> (def a (fn [] "ciao"))
  #'user/a
  user=> (a)
  "ciao"
  ````
3 Passing arguments to a function
  ````
  user=> (defn a[b] b)
  #'user/a
  user=> (a "ciao")
  "ciao"
  
  ; # replaces [] and shortens the function definition
  user=> (def myFun #(str "First arg: " %1 " Second one:" %2))                
  #'user/myFun
  user=> (myFun 1 2)
  "First arg: 1 Second one:2"
  
  ; function overloading
  user=> (defn myFun
               ([] "hello world") 
               ([a] (str "hello" a))
         )
  #'user/myFun
  
  user=> (myFun)
  "hello world"
  
  user=> (myFun "antonio")
  "helloantonio"
  
  ; Packing args => use &args
  user=>  (defn myFun[arg1 arg2 & args] (str "arg1:" arg1 " arg2" arg2 "rest:" args))
  
  #'user/myFun
  user=> (myFun 1 2 3)
  "arg1:1 arg22rest:(3)"
  
  ````
4. Anonymous functions
  ````
  ; they start with #
  user=> (map #(* 2 %) (range 4))
  (0 2 4 6)
  
  ````
### Macros ###
Macros are functions that takes some arguments in and return something (actually a list) which "runs" where the macro is called. Clojure uses lists to represents function and macro calls.
Let's have a look at the following function:
````
user=> (def pointless (fn [n] n))
user=> (pointless (+ 3 5))
````
"(def pointless ..." looks like is acting like a macro, but it's NOT. The difference between a macro and a function is that arguments are evaulated before those are passed to the function whereas macros receive arguments as unevaulated data structures.
Then, by attaching a key-value pair ":macro true" as metadata to the var mapped we could make the above function a macro.

The easiest way to define a macro, is the following one:
````
(defmacro name
          "description"
          [expression]
          HERE_THE_BODY)
````

### Special forms ###
Special forms are just Macros

#### IF ####
````
user=> (if (> 2 1) 2 1)
2

user=> (if false "isTrue" "isFalse")
"isFalse"

user=> (if false "isTrue")
nil

````
In clojure when should be used instead of (if .. (do ..))

#### When ####
````
(when pred
  (foo)
  (bar))
````

#### Let ####
(let [bindings* ] exprs*)
binding => binding-form init-expr

Creates temporary bindings
````
user=> (let [a 20 b 10] (> a b))
true
````
Use if-let instead of let + if

#### if-let ####
````
(if-let [results (foo x)]
  (something-with results)
  (something-else))
  
; instead of 
(let [results (foo x)]
  (if result
    (something-with results)
    (
````
#### Do ####
(do exprs*)
Evaluates the expressions in order and returns the value of the last. If no expressions are supplied, returns nil.
````
clojure-noob.core=> (do (def a 1) (def b 2) (+ a b))
3
````


#### Quote ####
Yields the unevaulated form
````
user=> '(a b c)
(a b c)
````

#### Case ####
Acts like almost like a C++/Java Switch statement
````
user=> (case 1          
1 "first"
2 "second")

"first"

````
#### Loop ####


## How to create a Clojure project ##
Lein (http://leiningen.org) it the defacto way to automate all the building phases that a clojure project would need.

- lein new projectname
- add the library you need to your project.clj file with a name you choose
- run lein deps to print out the command to use to add the jar to your local repo
- add the jar
- run lein deps again (you can skip this step if using leiningen2)
- run lein repl
- 
## Introspection in Clojure ##
Prints public vars in a namespace (in this example 'clojure.set')
````
user=> (dir clojure.set)
difference
index
intersection
join
map-invert
project
rename
rename-keys
select
subset?
superset?
union
nil
````

Getting source code of a function
````
user=> (source cascalog.api/union)
(defn union
  "Merge the tuples from the subqueries together into a single
  subquery and ensure uniqueness of tuples."
  [& gens]
  (ops/unique (apply combine gens)))
nil
````

If you feel lost have a look at the help!
````
user=> (help)
    Docs: (doc function-name-here)
          (find-doc "part-of-name-here")
  Source: (source function-name-here)
 Javadoc: (javadoc java-object-or-class-here)
    Exit: Control+D or (exit) or (quit)
 Results: Stored in vars *1, *2, *3, an exception in *e
````


## Clojure style ##
A. Use two spaces per intentation per level
````
(when something
  (something-else))
````

B. Align vertically function arguments.
````
(filter even?
        (range 1 10))
````

C.Align let and map keys

````
(let [thing1 "some stuff"
      thing2 "other stuff"]
  {:thing1 thing1
   :thing2 thing2})
````

Keep reading this on https://github.com/bbatsov/clojure-style-guide

## IDEs for Clojure ##
1. IntelliJ + La Clojure [DEPRECATED](http://blog.tomeklipski.com/2013/04/running-and-debugging-clojure-code-with.html)
2. IntelliJ 12 + Cursive 
   - add this repository to your IntellJ > 13.1 and install cursive http://cursiveclojure.com/plugins.xml 
   - Import a project (https://cursiveclojure.com/userguide/leiningen.html)
   NOTE Cursive didn't work for me with IntellJ 13.

## Clojure Cheat sheet ##
(http://clojure.org/cheatsheet)


## Testing Framework ##
1. Midje (https://github.com/marick/Midje/wiki/A-tutorial-introduction)
   Midje tests can be run from the console in this way
   ````
   lein midje orc.mynamespace.mytestnamespace
   ````


# IDE #
Many people use emacs. Java people may feel more confortable in using a more familiar IDE: IntelliJ Cursive. LaClojure and leiningen plugins have been deprecated!

# Clojure & Hadoop: Cascalog #
In order to get started with Cascalog you may wanna run a single-node hadoop cluster on you machine or run a cloudera VM image on your machine. Some people avoid using hadoop by writing some midje tests to test the output of their cascalog queries, but that may be too advanced if you are a totally noob and it may not give you the understanding of what really happens on hadoop using cascalog.
So once you have hadoop running you can go through the good set of tutorials you can find at http://cascalog.org/articles/guides.html

# References #
0. http://joyofclojure.com/
1. http://pleac.sourceforge.net/pleac_clojure/
2. http://www.braveclojure.com
