     
![](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/110px-Python-logo-notext.svg.png)

# INTRO #

# Basic topics #
````
# You have numbers
3 #=> 3

# Math is what you would expect
1 + 1 #=> 2
8 - 1 #=> 7
10 * 2 #=> 20
35 / 5 #=> 7

# Division is a bit tricky. It is integer division and floors the results
# automatically.
5 / 2 #=> 2

# To fix division we need to learn about floats.
2.0     # This is a float
11.0 / 4.0 #=> 2.75 ahhh...much better

# Enforce precedence with parentheses
(1 + 3) * 2 #=> 8

# Boolean values are primitives
True
False

# negate with not
not True #=> False
not False #=> True

# Equality is ==
1 == 1 #=> True
2 == 1 #=> False

# Inequality is !=
1 != 1 #=> False
2 != 1 #=> True

# More comparisons
1 < 10 #=> True
1 > 10 #=> False
2 <= 2 #=> True
2 >= 2 #=> True

# Comparisons can be chained!
1 < 2 < 3 #=> True
2 < 3 < 2 #=> False

# Strings are created with " or '
"This is a string."
'This is also a string.'

# Strings can be added too!
"Hello " + "world!" #=> "Hello world!"

# A string can be treated like a list of characters
"This is a string"[0] #=> 'T'

# % can be used to format strings, like this:
"%s can be %s" % ("strings", "interpolated")

# A newer way to format strings is the format method.
# This method is the preferred way
"{0} can be {1}".format("strings", "formatted")
# You can use keywords if you don't want to count.
"{name} wants to eat {food}".format(name="Bob", food="lasagna")

# None is an object
None #=> None

# Don't use the equality "==" symbol to compare objects to None
# Use "is" instead
"etc" is None #=> False
None is None  #=> True

# The 'is' operator tests for object identity. This isn't
# very useful when dealing with primitive values, but is
# very useful when dealing with objects.

# None, 0, and empty strings/lists all evaluate to False.
# All other values are True
bool(0)  #=> False
bool("") #=> False
````
## Classes ##

## Private methods ##
By default python class methods are public. To make a method private the class
name has to start with "__".

Even if private is still possible to access to a private method in the following way:
````
class foo(object):
        def __init__(self):
                print "INIT FOO"

        def __hidden(self):
                print "HIDDEN FOO"
f = foo()
f._foo__hidden()
````

## Exceptions ##
[Built-in exceptions](http://docs.python.org/2/library/exceptions.html)

## new-style classes ##
Before Python 2.2 there was no consistent way to discover what attributes and methods were supported by an object.
Subclassing object class gives to your class a consistance interface among other python classes which allow developers
to get, set and delete attribute values, to check the size of the object in memory (__sizeof__()), to get a string which
represent the object (__repr__ or __str__) and so on.
```` 
# Defines old-style class
class a:
   pass

# Defines new-style class
class b(object):
   pass
 
dir(a)
# a supports the following methods
# ['__doc__', '__module__']

dir(b)
# b supports the following methods
# ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
```` 

## static class attributes ##
variables defined in the class declaration are defined as static. static means you don't need to instantiate to object to access to the variable.
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
## overriding methods ##

````
class stack(list):
  def push(self, x):
    print "PUSH"
    self.append(x)

  def pop(self):
    print "POP"
    super(stack, self).pop()

s = stack() # instantiate a stack object
s.push(2) # appends 2 to the list
s.pop() # calls list.pop()
print len(s) # len works on stack since it's a child of list

````

# Intermediate topics #

## Unicode and Strings ##
unicode and str are two differnt types.

````
# to detect if a string is unicode. this returns FALSE
s="ciao"
isinstance(s, unicode)
>>> False

# u before the string declaration says to python that we wanna use a unicode type
s=u"ciao"
isinstance(s, unicode)
>>> True

# binary strings
s=b'c\xc3\xa5i\xc3\xb6'
print s
>>> cåiö

# convert binary string to unicode
a=s.decode("utf8)
>> u'c\xe5i\xf6'
isinstance(a, unicode)
>>> True

````

## Generators ##
The concept of generators is something that every pythonist should be aware about.
In a nutshell, they are iterable objects (like lists), but when next() is called, the returned item is generated on the fly.

### YIELD ####
Generators can be obtained using 'yield' in a function.
Or in with a less pythonic way using the generator pattern achieved with a iterable shown in the patterns paragraph.
````
def firstn(n):
        num = 0
        while num < n:
                yield num
                num = num+1

sum_of_first_n = sum(firstn(1000000))
print sum_of_first_n

````

### Generator expressions ###
Generator expressions provide an additional shortcut to build generators out of expressions similar to that of list comprehensions.

````
doubles = (2 * n for n in range(50))
# doubles is a generator object 
doubles.next()
# next() method let the generator generates the next item
````



[Reference manual](https://wiki.python.org/moin/Generators)

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


## Descriptors ##
[Documentation](http://docs.python.org/2/howto/descriptor.html)

## Design patterns ##

### Decorators ###
Mostly used by some libraries as Flask or by "properties" as seen in the previous paragraph, decorators are usually blacboxes for most of newbie pythonists
What's a decorator in a nutshell? It's a fuction which returns another function.
You can find a lot of very useful decorators in the [Python decorator library](https://wiki.python.org/moin/PythonDecoratorLibrary)

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

### Singleton class ###
A singleton class is a class which has only one instance in the application scope
Here is a decorator which you can use to make your class singleton
````
class Singleton:
    """
    A non-thread-safe helper class to ease implementing singletons.
    This should be used as a decorator -- not a metaclass -- to the
    class that should be a singleton.

    The decorated class can define one `__init__` function that
    takes only the `self` argument. Other than that, there are
    no restrictions that apply to the decorated class.

    To get the singleton instance, use the `Instance` method. Trying
    to use `__call__` will result in a `TypeError` being raised.

    Limitations: The decorated class cannot be inherited from.

    """

    def __init__(self, decorated):
        self._decorated = decorated

    def Instance(self):
        """
        Returns the singleton instance. Upon its first call, it creates a
        new instance of the decorated class and calls its `__init__` method.
        On all subsequent calls, the already created instance is returned.

        """
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)

@Singleton
class Foo:
    def __init__(self):
        print 'Foo created'

class SingletonTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_errors(self):
        passed = False
        try:
          f = Foo()
        except TypeError:
          passed = True
        assert passed

    def test_instance(self):
        f = Foo.Instance()
        g = Foo.Instance()
        assert f == g

if __name__ == "__main__":
    unittest.main()
````

### Builder pattern ###
Python is not Java. Python allows you to have default value for function arguments
So you may want to write your code in this way:
````
class foo:
     defaultVar1 = "a"
     defaultVar2 = "b"
     def __init__(self, **args):
          self.var1 = args.get("var1", self.defaultVar1)
          self.var2 = args.get("var2", self.defaultVar2)
          print "INIT var1=%s var2=%s" % (self.var1, self.var2)

if __name__ == "__main__":
     bar = foo(var1="c")                # INIT var1=c var2=b
     bar = foo(var2="d")                # INIT var1=a var2=d
     bar = foo(var2="d", var1="c")      # INIT var1=c var2=d
     bar = foo()                        # INIT var1=a var2=b

````

### Generator pattern as Iterable ###
Not really smart to use as we have 'yeld'. See generators paragraph instead of this one.

````
class firstn(object):
        def __init__(self, n):
                self.n = n
                self.num, self.nums = 0, []

        def __iter__(self):
                return self

        def next(self):
                if self.num < self.n:
                        cur, self.num = self.num, self.num+1
                        return cur
                else:
                        raise StopIteration()

sum_of_first_n = sum(firstn(1000000))
print sum_of_first_n
````

##  Concurrency programming ##

### Multiprocessing module ###
If you want to run in paralled a function on a list of data, this may be the code you are looking for.
Please note that Python actually spawn new processes and doesn't not really use threads here.
The number of processes that the operating system can run is limited. Usually it's 1024. 
On linux, you can run: "ulimit -n" to know how many open files can your system handle per user. 
````
def  runFunctionsInParallel(listOf_FuncAndArgLists):
    """
    Take a list of lists like [function, arg1, arg2, ...]. Run those functions in parallel, wait for them all to finish, and return the list of their return values, in order.
    (This still needs error handling ie to ensure everything returned okay.)
    """
    from multiprocessing import Process, Queue

    def storeOutputFFF(fff,theArgs,que): #add a argument to function for assigning a queue
        print 'MULTIPROCESSING: Launching %s in parallel '%fff.func_name
        que.put(fff(*theArgs)) #we're putting return value into queue

    queues=[Queue() for fff in listOf_FuncAndArgLists] #create a queue object for each function
    jobs = [Process(target=storeOutputFFF,args=[funcArgs[0],funcArgs[1:],queues[iii]]) for iii,funcArgs in enumerate(listOf_FuncAndArgLists)]
    for job in jobs: job.start() # Launch them all
    for job in jobs: job.join() # Wait for them all to finish
    # And now, collect all the outputs:
    return([queue.get() for queue in queues])

def concat(x):
    return "CIAO" + str(x)

#NOTE: OS limits the num of parallel process.
# OSError: [Errno 24] Too many open files is returned for high values in range
if __name__ == "__main__":
   # Create a list of jobs called lfaa. A job is tuple containing function name and argument
   lfaa = list()
   args = range(100)
   for arg in args:
       lfaa.append((concat, arg))

   # This is a blocking function
   results = runFunctionsInParallel(lfaa)
   
   # results is a list containing the values returned by "concat" in this case
   # please note that this list is not sorted.
   print "Results %d" % len(results)
````

### Subprocess: the way to launch external application###
The code below shows you how to use subprocess in order to run N jobs being sure that only M of them run in parallel
````
import subprocess
import os
import time

files = [1,2,3,4,5,6]
command = "/bin/sleep"
max_processes =2
processes = set()

for name in files:
    name = str(name)
    # Run the first command
    print "Running %s %s" % (command, name)
    p = subprocess.Popen([command, name])
    processes.add(p)

    # once we started our M processes, the script waits for a job to finish
    # When a job is completed, it remove it from the list and the "for" loop loops again.
    if len(processes) >= max_processes:
        loop = True
        print "Waiting for a job to finish"
        while loop:
            for process in processes:
                xxx = process.poll()
                if xxx != None:
                    loop = False
        print "Job completed. Proceeding..."

        # remove completed processes from the list
        complete_procs = set([p for p in processes if p.poll() is not None])
        processes -= complete_procs
````

## Unit testing ##
### unittest module ###
Basic usage:
````
import unittest

class foo:
        def sum(self,a,b):
                return a+b

        def throwException(self):
                raise Exception("ciao")

class fooTest(unittest.TestCase):
        def setUp(self):
                # Create an instance of the class
                # setUp runs before each of test* methods here
                self.bar = foo()

        def test_1(self):
                assert self.bar.sum(1,2) == 3

        def test_2(self):
                with self.assertRaisesRegexp(Exception, "ciao"):
                        self.bar.throwException()

if __name__ == "__main__":
        unittest.main()
````
## Packaging ##
You can package your python in 3 simple steps

a. Your project has to look as follow
````
TowelStuff/
    LICENSE.txt
    README.txt
    setup.py
    towelstuff/
        __init__.py
````
b. Add a setup.py file which look like this one:
````
from distutils.core import setup

setup(
    name='TowelStuff',
    version='0.1dev',
    packages=['towelstuff',],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.txt').read(),
)
````

c. Create the first release with:
```` 
python setup.py sdist

````
This will generate a tag.gz in the dist/ directory.


## Cool libraries ##
### Networking ###
#### GEvent ####
gevent is a Python networking library that uses greenlet to provide a synchronous API on top of libevent event loop.
[Read more](http://www.gevent.org/intro.html)

### WSGI ####
The Web Server Gateway Interface is a simple and universal interface between web servers and web applications or frameworks for the Python programming language.

[List of python WSGI frameworks] (http://en.wikipedia.org/wiki/Web_Server_Gateway_Interface#WSGI-compatible_applications_and_frameworks)
#### Flask ####
[TODO]

## Coding style ##
Every programmer should follow the PEP-8 [guidelines](http://legacy.python.org/dev/peps/pep-0008/).
Coding style by pylint, if you do not use any IDE.

## Misc ##
### Closures ###
Or "Function closure" is a function object that has access to vars in "terminated" enclosing scopes.
````
# myVar lives in the foo enclosing scope
def foo(myVar):
     # bar is a closure since it has access to myVar
     def bar():
          print myVar
     return bar

# f holds a reference to the function bar(), at this point foo has been executed and is not in memory anymore
f = foo("ciao")
f()
````


# FAQ #
1. What's the best IDE for programming in python? Get [PyCharm](http://www.jetbrains.com/pycharm/)
2. Where can I get some help? Try to ask your questions in #python@Freenode IRC channel
3. How do you enforce types in functions? Use @accepts(int, int, int) and @return(float) [decorators](https://wiki.python.org/moin/PythonDecoratorLibrary#Type_Enforcement_.28accepts.2Freturns.29)
