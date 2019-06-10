# Spring concepts

## Beans

## Dependency injection

## Spring bean factory
Spring is a containers of bean. 
Any POJO can be hosted by the Spring container as object.
The container manages all the lifecicle of the object. 
The creation of the object is done by Spring.
Factory pattern is used to build objects.
It works in this way Object --> Factory <-- config.
An object A asks to the factory to get an object B.
The factory reads the configuration and instantiate the object B.
The objects are beans, the Factory is the Bean Factory and the config is the Spring XML.

## Application context
