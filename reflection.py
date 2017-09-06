'''Reflection & Introspection'''

# A Python script can find out about the type, class, attributes and methods of
# an object. This is referred to as reflection or introspection. Functions
# include type(), isinstance(), callable(), dir() and getattr().

# type() ---------------------------------------------------------------------

import datetime

now = datetime.datetime.utcnow()

type(now)       # <class 'datetime.datetime'>
type(234)       # <class 'int'>
type('hello')   # <class 'str'>

# bool()----------------------------------------------------------------------

# will tell you whether something is True or False:

x = []
y = ['one']

bool(x)        # False
bool(y)        # True

# isinstance() ---------------------------------------------------------------

# because everything in Python is an object, isinsatnce works everywhere:

isinstance(now, datetime.datetime)  # True
isinstance(234, int)                # True
isinstance('hello', str)            # True

# repr() ---------------------------------------------------------------------

# returns a printable representation of the given object:

print(repr(now))  # datetime.datetime(2017, 9, 5, 18, 23, 30, 607281)

# callable() -----------------------------------------------------------------

# returns True if the object passed appears callable:

def test():
    pass

callable(test)  #True

# dir() ----------------------------------------------------------------------

# tries to return a list of valid attributes of the object.

# show the names in the local module namespace:
print(dir())

 # show all the Built-in things:
for m in dir(__builtins__):
    print(m)

# show the names in the random module:
import random
print(dir(random))

# print just the useful ones:
for obj in dir(random.Random):
    if obj[0] != '_':
        print(obj)

# getattr() ------------------------------------------------------------------

# returns the value of an attribute of an object, given the attribute name
class Person:
    age = 43
    name = "Kali"

person = Person()
print(getattr(person, "age"))  # returns 43
print(person.age)              # same thing
