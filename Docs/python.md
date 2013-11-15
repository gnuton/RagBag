     
![logo](http://www.python.org/community/logos/python-logo-master-v3-TM.png)

# INTRO #
Python allows people to write programs very quickly. The aim of this doc is 
let you learn python as quick as possible. Few words, small examples which
allow you to grasp basic concepts that you can develop further with some 
real programming.

# Basic topics #

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
## Unit testing ##
### unittest module ###
Basic usage:
````
import unittest

class foo:
        def sum(self,a,b):
                return a+b


class fooTest(unittest.TestCase):
        def setUp(self):
                # Create an instance of the class
                # setUp runs before each of test* methods here
                self.bar = foo()

        def test_1(self):
                assert self.bar.sum(1,2) == 3

if __name__ == "__main__":
        unittest.main()
````
# FAQ #
1. What's the best IDE for programming in python? Get [PyCharm](http://www.jetbrains.com/pycharm/)
2. Where can I get some help? Try to ask your questions in #python@Freenode IRC channel
3. How do you enforce types in functions? Use @accepts(int, int, int) and @return(float) [decorators](https://wiki.python.org/moin/PythonDecoratorLibrary#Type_Enforcement_.28accepts.2Freturns.29)
