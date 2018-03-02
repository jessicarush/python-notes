'''Reflection & Introspection'''

# A Python script can find out about the type, class, attributes and methods
# of an object. This is referred to as reflection or introspection. Functions
# include type(), isinstance(), callable(), dir() and getattr() and more.


# type()
# -----------------------------------------------------------------------------

import datetime

now = datetime.datetime.utcnow()

type(now)       # <class 'datetime.datetime'>
type(234)       # <class 'int'>
type('hello')   # <class 'str'>


# bool()
# -----------------------------------------------------------------------------

# Will tell you whether something is True or False:

x = []
y = ['one']
z = None

bool(x)        # False
bool(y)        # True
bool(z)        # False


# isinstance()
# -----------------------------------------------------------------------------
# because everything in Python is an object, isinstance works everywhere:

isinstance(now, datetime.datetime)  # True
isinstance('hello', str)            # True
isinstance(234, int)                # True
isinstance(234, float)              # False


# issubclass()
# -----------------------------------------------------------------------------
# The issubclass() function checks if the object (first argument) is a subclass
# of a class (second argument). You can also provide a tuple as the second
# argument. issubclass() will return True if at least one of the items in the
# tuple is True:

class Polygon():
    def __init__(self, polygon_type):
        print('This polygon is a', polygon_type)

class Triangle(Polygon):
    def __init__(self):
        super().__init__('triangle')

t = Triangle()                                # This polygon is a triangle
print(issubclass(Triangle, Polygon))          # True
print(issubclass(Triangle, list))             # False
print(issubclass(Triangle, (list, Polygon)))  # True


# repr()
# -----------------------------------------------------------------------------
# returns a printable representation of the given object:

print(now)        # 2017-11-17 18:44:35.002758
print(repr(now))  # datetime.datetime(2017, 9, 5, 18, 23, 30, 607281)

# As a side note, you can customize what repr() outputs in a class by using
# its magic method. See magic_methods.py


# callable()
# -----------------------------------------------------------------------------
# returns True if the object passed appears callable:

def test():
    pass

callable(test)  # True


# dir()
# -----------------------------------------------------------------------------
# tries to return a list of valid attributes of the object.

# show the names in the local module namespace:
print(dir())
# ['Polygon', 'Triangle', '__annotations__', '__builtins__', '__cached__',
# '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__',
# 'datetime', 'now', 't', 'test', 'x', 'y', 'z']

# show all the Built-in things:
for m in dir(__builtins__):
    print(m, end=', ')

# show the names in the datetime module:

print(dir(datetime))
# ['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__',
# '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime',
# 'datetime_CAPI', 'time', 'timedelta', 'timezone', 'tzinfo']

# Print just the useful ones:

for m in dir(datetime.datetime):
    if m[0] != '_':
        print(m, end=', ')
# astimezone, combine, ctime, date, day, dst, fold, fromordinal, fromtimestamp,
# hour, isocalendar, isoformat, isoweekday, max, microsecond, min, minute,
# month, now, replace, resolution, second, strftime, strptime, time, timestamp,
# timetuple, timetz, today, toordinal, tzinfo, tzname, utcfromtimestamp,
# utcnow, utcoffset, utctimetuple, weekday, year


# getattr()
# -----------------------------------------------------------------------------
# returns the value of an attribute of an object, given the attribute name,
# but also lets you provide a default value to avoid raising an exception:

class Person:
    age = 43
#   name = 'Ghost'

p = Person()
print(getattr(p, "age"))  # 43
print(p.age)              # 43

# These two return - AttributeError: 'Person' object has no attribute 'name'
# print(getattr(p, 'name'))
# print(p.name)

# This will return the default value if name doesn't exist
print(getattr(p, 'name', 'No Name'))  # No Name


# hasattr()
# -----------------------------------------------------------------------------
# returns true if an object has the given named attribute and false if not.

# hasattr(object, name)

class Person:
    age = 23
    name = 'Raja'

p = Person()

print('Person has age?:', hasattr(p, 'age'))        # True
print('Person has salary?:', hasattr(p, 'salary'))  # False


# id()
# -----------------------------------------------------------------------------
# returns the identity (unique integer) of an object

animal = 'cat'

def example1():
    animal = 'dog'
    print('local animal:', animal, id(animal))

def example2():
    print('global animal:', animal, id(animal))

example1()
example2()

# local animal: dog 4316822976
# global animal: cat 4316589728
