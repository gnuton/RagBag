                                                       
                                 ,,                           
    `7MM"""Mq.              mm   `7MM                           
      MM   `MM.             MM     MM                           
      MM   ,M9 `7M'   `MF'mmMMmm   MMpMMMb.  ,pW"Wq.`7MMpMMMb.  
      MMmmdM9    VA   ,V    MM     MM    MM 6W'   `Wb MM    MM  
      MM          VA ,V     MM     MM    MM 8M     M8 MM    MM  
      MM           VVV      MM     MM    MM YA.   ,A9 MM    MM  
    .JMML.         ,V       `Mbmo.JMML  JMML.`Ybmd9'.JMML  JMML.
                ,V                                            
             OOb"     Docs                                             

# INTRO #

# Advanced topics #

## Properties ##

````
# Properties


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
