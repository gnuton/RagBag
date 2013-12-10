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
antonio=> (class ())
clojure.lang.PersistentList$EmptyList

antonio=> (class '(1 2 3))
clojure.lang.PersistentList

````
### Data evaluation ###
(a b c) is a list, where a,b,c could be functions or vars.
(1 2 3) throws a ClassCastException.
a literal list (Clojure won't evaulate it) can be defined as follow:
````
antonio=> '(1 2 3)
(1 2 3)
````

### String ###

````
; concatenation
(str "ciao " "bello")
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

