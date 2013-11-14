     
![logo](http://www.python.org/community/logos/python-logo-master-v3-TM.png)

# INTRO #
Python allows people to write programs very quickly. The aim of this doc is 
let you learn python as quick as possible. Few words, small examples which
allow you to grasp basic concepts that you can develop further with some 
real programming.


# Basic topics #

## static class attributes ##
variables defined in the class definition are defined as static. static means you don't need to instantiate to object to access to the variable.
Python allows you to edit static variables.

````
class foo:
        a=3
        def __init__(self):
                print "INIT"


if __name__ == "__main__":
        foo.sf()

        print foo.a  # prints out 3
        foo.a = 5
        print foo.a  # prints out 5

        bar = foo()
        print bar.a  # prints out 5

````   
## static methods ##
static class methods must be marked by @staticmethod (that's a decorator, see advanced topics for more info)
If you do not define it you will get an error like this: 
"TypeError: unbound method sf() must be called with foo instance as first argument (got nothing instead)"
````
class foo:
        def __init__(self):
                print "INIT"
        
        @staticmethod
        def sf():
                print "STATIC FUNCTION"


if __name__ == "__main__":
        foo.sf()
````


# Intermediate topics #

## Generators ##
TODO

## Properties ##
The following snippets shows how to use properties in Python

````
class foo(object):
        @property
        def x(self):
                try:
                        return self._x
                except AttributeError:
                        return None

        # AttributeError: can't set attribute
        @x.setter
        def x(self, value):
                self._x = value

        def getX(self):
                return self._x

if __name__ == "__main__":
        bar = foo()
        print bar.x
        bar.x = 2
        print bar.x
        print bar.getX()
````

We can define properties without using decorators too, the code in this case would be...
````
class foo(object):

        def get_x(self):
                try:
                        return self._x
                except AttributeError:
                        return None

        def set_x(self, value):
                self._x = value

        x = property(get_x, set_x)

        def getX(self):
                return self._x

if __name__ == "__main__":
        bar = foo()
        print bar.x
        bar.x = 2
        print bar.x
        print bar.getX()
````

## args, * and **: ways of passing args to functions##
Python allows programmers to pass arguments to functions in three ways.
foo functions show all these three options to you

````
def foo1(first, second):
        print first
        print second

def foo2(*args_as_list):
        print args_as_list

def foo3(**args_as_dict):
        print args_as_dict

foo1(1,2)
foo2(1,2)
foo3(first=1, second=2)
````
# Advanced topics #

## Decorators ##
Mostly used by some libraries as Flask or by "properties" as seen in the previous paragraph, decorators are usually blacboxes for most of newbie pythonists
What's a decorator in a nutshell? It's a fuction which returns another function.


````
# This is the fuction which defines my decorator
def my_decorator(old_function):
        # function defined which will be returned by the decorator
        def new_function(*args, **kwrds):
                old_function(*args, **kwrds) # args is __main__.foo object and kwrds is {} in this case
                
        return new_function

class foo(object):

        @my_decorator
        def get_x(self):
                try:
                        return self._x
                except AttributeError:
                        return None
if __name__ == "__main__":
        bar = foo()
        print bar.get_x()
````
