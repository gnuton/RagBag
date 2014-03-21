# Clojure #
![logo](http://clojure.org/space/showimage/clojure-icon.gif)

Clojure is a dialect of the Lisp language created by Rich Hickey. It's a general-purpose function language and it runs in the JVM as well as in JS engines (ClojureScript).

## Basic stuff ##

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

; Collections & sequences
; "Collections" are groups of data
; "Sequences"  abstract description of list of data
;              they can define infinite series
;              --> seqs can be lazy, they need to provide an entry item when accessed
;              (something like generators in python!)


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

