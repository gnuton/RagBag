# Clojure #
![logo](http://clojure.org/space/showimage/clojure-icon.gif)

## Basic stuff ##

### Namespace ###
By default clojure uses "user" as namespace
You can set your own one with:
````
(ns mynamespace)
````

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

antonio=> (seq? '[1 2 3])
false

antonio=> (seq? (range 4))
true


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

