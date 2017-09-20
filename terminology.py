'''Misc Terms''''

# Literal ----------------------------------------------------------------------

# a literal lets you assign values of an object in a single assignment,
# for example:

# assign a string literal to message
message = "some information"

# assign an int literal to x
x = 100

# assign a dictionary literal to plants
plants = {'spider': 'long, slender leaves',
          'succulent': 'like a cactus',
          'fern': 'perfers the forest'}

# None -------------------------------------------------------------------------

# None is not the same as False. Though it may look false when evaluated as a
# boolean, None is technically none as seen here:

thing = None

def is_none(thing):
    if thing is None:
        print("it's none")
    elif thing:
        print("it's True")
    else:
        print("it must be False")

is_none(thing)

# Keyword arguments: **name ----------------------------------------------------

# The keyword argument **h extracts the keys and values from the dictionary
# and supplies them as arguments to the class Element()

class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

h = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}

hydrogen = Element(**h)

print(hydrogen.symbol)


# Function ---------------------------------------------------------------------
# A Function is a bit of reusable code that can de called after being defined.
# Functions can be defined by you in your code or they can be defined in
# libraries that are imported.

# Module -----------------------------------------------------------------------
# Another word for library. Modules are simply python files that can be
# imported and used.

# Package ----------------------------------------------------------------------
# A python module which can contain submodules. Essentially this is just a way
# of organizing many modules (files) into file hierarchies (folders).
# When you create a directory for your modules, you also create an empty file
# in that folder called: __init__.py. This file tells python to use the folder
# name for importing.

# Parameter --------------------------------------------------------------------
# A parameter is a named entity in a functions definition. Parameters can be
# replaced with arguments when the function is called.

# Argument ---------------------------------------------------------------------
# A value passed to a function when calling the function. Arguments are
# assigned to the named local variables (parameters) in the functions body.

# Class ------------------------------------------------------------------------
# A blueprint or template for creating an object.

# Object -----------------------------------------------------------------------
# Everything in Python is an object. The official definition is: any data with
# state (attributes or value) and defined behavior (methods).

# Instance ---------------------------------------------------------------------
# What you get when you create something from a class.

# Attribute --------------------------------------------------------------------
# A value associated with an object which is referenced by name using dot
# notation. As in a class:

class Person():
    def __init__(self, name):
        self.name = name
        self.alive = True

snape = Person('Severus Snape')

# reference the name attribute:
snape.name

# Property ---------------------------------------------------------------------
# property is actually a method that returns a property attribute. It makes a
# method (a function in a class) behave like an attribute.

# self -------------------------------------------------------------------------
# Inside a class definition, self is a variable name used to signify something
# will belong to an instance of a that class. In other words, whenever a new
# instance of a class is created, "self" indicates that it will have its own
# variables that aren't shared with other instances.

# Method -----------------------------------------------------------------------
# A function that is defined inside of a class. It can be called 'on' an
# instance of that class if self was included as its first argument.

class Person():
    def __init__(self, name):
        self.name = name
        self.alive = True

    def deceased(self):
        self.alive = False

snape = Person('Severus Snape')

# call the method (function) like this:
snape.deceased()
# or like this:
Person.deceased(snape)

# Inheritance ------------------------------------------------------------------
# The idea that when one class is created from another, it will inherit that
# classes traits, unless specifically overwritten in its own definition.

# Composition ------------------------------------------------------------------
# A class can be composed of other classes as parts. A lengthier description:
# Composition is a way of aggregating objects together by making some objects
# attributes of other objects.

# Aggregation ------------------------------------------------------------------
# The distinction between aggregation and composition can blur slightly. Unlike
# composition, aggregation uses existing instances of objects to build up
# another object. The composed object does not actually own the objects that
# it's composed of. If it's destroyed, those objects continue to exist.

# is-a -------------------------------------------------------------------------
# A phrase to say something inherits from another.

# has-a ------------------------------------------------------------------------
# A phrase to say something is composed of others.

# Encapsulation ----------------------------------------------------------------
# Encapsulation is the idea that data inside an object should only be accessed
# through a public interface – that is, the object’s methods. Generally speaking
# encapsulation is the mechanism for restricting the access to some of an
# object's components. This means that the internal representation of an object
# can't be seen from outside of the objects definition. Access to this data
# is typically only achieved through methods.

# Delegation -------------------------------------------------------------------
# Delegation is an object oriented technique (also called a design pattern)
# where certain operations on one object are automatically applied to another,
# usually contained, object.

# Polymorphism -----------------------------------------------------------------
# Polymorphism is the idea that even though different types of objects can have
# very different traits (for example int objects can be divided whereas string
# objects can be capitalized), they can also have shared behaviors (for example,
# they are all printable):

int.__str__()
float.__str__()
list.__str__()
tuple.__str__()

# So polymorphism basically means that objects can be more than one thing at the
# same time. Inheritance is one way to implement polymorphism. In the above
# example, every type of object automatically inherits the __str__ method from
# its object base class.

# Another way of implementing polymorphism: one class can behave like another
# class as long as it contains the necessary methods and data attributes.
