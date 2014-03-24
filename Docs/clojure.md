# Clojure #
![logo](http://clojure.org/space/showimage/clojure-icon.gif)

Clojure is a dialect of the Lisp language created by Rich Hickey. It's a general-purpose function language and it runs in the JVM as well as in JS engines (ClojureScript).

## Basic stuff ##

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

### Comments ###
Comment lines start with ';'


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

; range generates finite or infinite sequences 
antonio=> (range 5)
(0 1 2 3 4)

antonio=> (take 3 (range 5))
(0 1 2)

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

; concatenate lists and vectors
user=> (concat [1 2] '(3 4))
(1 2 3 4)

user=> (concat [1 2] [3 4])
(1 2 3 4)

user=> (concat '(1 2) '(3 4))
(1 2 3 4)

; reduce, runs an operation 
user=> (reduce + [1 2 3 4])
10


````

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
````
; define a fuction
user=> (fn [] "Ciao")
#<user$eval27$fn__28 user$eval27$fn__28@49b510b8>

; Call a function
user=> ((fn [] "Ciao"))
"Ciao"

; Assing a function to a variable
user=> (def a (fn [] "ciao"))
#'user/a

user=> (a)
"ciao"

; Written in a shorten form
user=> (defn a [] "ciao") 
#'user/a

; Passing arguments to a function
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
