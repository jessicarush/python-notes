'''Data Classes'''


# https://docs.python.org/3.7/library/dataclasses.html#module-dataclasses

# Python 3.7 introduced a new module: dataclasses.py. The new dataclass()
# decorator provides a way to declare data classes. When you use it, the
# class constructor (__init__ method) and other magic methods, such as
# __repr__(), __eq__(), and __hash__() are generated automatically.

# When using this decorator, you need to describe the attributes using
# class variable annotations - type hints (introduced in Python 3.6).

# Example:

from dataclasses import dataclass

@dataclass
class Point():
    x: float
    y: float
    z: float = 0.0

p = Point(1.5, 2.5)
print(p)  # Point(x=1.5, y=2.5, z=0.0


# Annotationg varibales
# ------------------------------------------------------------------------------
# Python 3.6 introduced a syntax for annotating variables in PEP 526.
# Here's a quick review. For more see documenting_naming.py

# For simple built-in types:
x: int = 1
x: float = 1.0
x: bool = True
x: str = 'test'
x: bytes = b'test'

from typing import List, Set, Dict, Tuple, Optional

x: List[int] = [1]
x: Set[int] = {6, 7}
x: Dict[str, float] = {'field': 2.0}
x: Tuple[int, str, float] = (3, "yes", 7.5)
# x: Optional[str] = some_function()


# dataclass() parameters
# ------------------------------------------------------------------------------
# The dataclass decorator has some default parameters:

@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)
class Example():
    pass

# init: If true (the default), a __init__() method will be generated. If the
# class already defines __init__(), this parameter is ignored.

# repr: If true (the default), a __repr__() method will be generated. The
# generated string will have the class name and the name and repr of each field,
# in the order they are defined in the class. Fields can be marked to be excluded
# from the repr. If the class defines __repr__(), this parameter is ignored.

# eq: If true (the default), an __eq__() method will be generated. This method
# compares the class as if it were a tuple of its fields, in order. Both
# instances in the comparison must be of the identical type. If the class
# already defines __eq__(), this parameter is ignored.

# order: If true (the default is False), __lt__(), __le__(), __gt__(), and
# __ge__() methods will be generated. Works the same as eq. Note if order is
# true and eq is false, a ValueError is raised.

# unsafe_hash: If False (the default), a __hash__() method is generated
# according to how eq and frozen are set. __hash__() is used by built-in hash(),
# and when objects are added to hashed collections such as dictionaries and sets.
# Having a __hash__() implies that instances of the class are immutable. For an
# in depth explanation see the docs.

# frozen: If true (the default is False), assigning to fields will generate an
# exception. This emulates read-only frozen instances. If __setattr__() or
# __delattr__() is defined in the class, then a TypeError is raised.


# field()
# ------------------------------------------------------------------------------
# This method allows us to add more information to a particular attribute.
# The parameters to field() are:

# default: If provided, this will be the default value for this field. This is
# needed because the field() call itself replaces the normal position where the
# default value would go.

# default_factory: If provided, it must be a zero-argument callable that will
# be called when a default value is needed for this field. Among other purposes,
# this can be used to specify fields with mutable default values.

# init: If true (the default), this field is included as a parameter to the
# generated __init__() method.

# repr: If true (the default), this field is included in the string returned
# by the generated __repr__() method.

# compare: If true (the default), this field is included in the generated
# equality and comparison methods (__eq__(), __gt__(), et al.).

from dataclasses import field

@dataclass
class InventoryItem():
    '''Class representing an item in inventory.'''
    name: str
    price: float
    rating: int = field(repr=False)
    quantity: int = 0
    min: int = field(repr=False, default=10)
    mylist: List[int] = field(default_factory=list)

    def total_value(self):
        return self.price * self.quantity


i = InventoryItem('pencils', 0.5, 5, 100)
i.mylist += [10, 5, 16]
i.mylist += [20, 2]

print(i)
# InventoryItem(name='pencils', price=0.5, quantity=100, mylist=[])
print(i.total_value())
# 50.0
print(i.mylist)
# [10, 5, 16, 20, 2]


# fields(), asdict(), astuple(), is_dataclass()
# ------------------------------------------------------------------------------

from dataclasses import fields, asdict, astuple, is_dataclass
from pprint import pprint

# This method returns a tuple of field objects for a given dataclass.
pprint(fields(i))
#TL;DR

# This method returns a dict of fields for a given dataclass.
pprint(asdict(i))
# {'min': 10,
#  'mylist': [10, 5, 16, 20, 2],
#  'name': 'pencils',
#  'price': 0.5,
#  'quantity': 100,
#  'rating': 5}

# This method returns a tuple of fields for a given dataclass.
pprint(astuple(i))
# ('pencils', 0.5, 5, 100, 10, [10, 5, 16, 20, 2])

# This method returns True if the given arg is a dataclass or instance of one.
pprint(is_dataclass(i))
# True
