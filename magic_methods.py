'''Special (Magic) Methods'''

# Names of these methods begin and end with __. An example is __init__ which
# initializes a newly created object from its class and any arguments that were
# passed in. Many basic tasks in python can be done with non-object-oriented
# looking syntax (a + b, for example). What's really happening here is a
# kind of "syntactic sugar" that maps to an object-oriented pattern underneath.
# For example, the __contains__ method allows us to use the 'in' keyword (see
# polymorphism.py), __add__ allows us to use the '+' operator and so on.

# Example: override the __add__ method will in turn affect the '+' operator.

class TestInt(int):
    def __add__(self, num):
        return 100

a = TestInt(5)
b = TestInt(3)

print(a + b)  # 100

# Example: create a method that compares two words but is case insensitive.

class Word(str):
    def __eq__(self, word):
        return self.lower() == word.lower()

a = Word('haha')
b = Word('HAHA')

print(a == b)  # True

# In those two examples we inherited from int and str, but we don't have to:

class Word():
    def __init__(self, text):
        self.text = text
    def __eq__(self, word):
        return self.text.lower() == word.text.lower()

a = Word('ha')
b = Word('HA')

print(a == b) # True


# Magic Methods for comparison
# -----------------------------------------------------------------------------

def __eq__(self, other):        # self == other
    pass
def __ne__(self, other):        # self != other
    pass
def __lt__(self, other):        # self < other
    pass
def __gt__(self, other):        # self > other
    pass
def __le__(self, other):        # self <= other
    pass
def __ge__(self, other):        # self >= other
    pass


# Magic Methods for math
# -----------------------------------------------------------------------------

def __add__(self, other):       # self + other
    pass
def __sub__(self, other):       # self - other
    pass
def __mul__(self, other):       # self * other
    pass
def __floordiv__(self, other):  # self // other
    pass
def __truediv__(self, other):   # self / other
    pass
def __mod__(self, other):       # self % other
    pass
def __pow__(self, other):       # self ** other
    pass


# Others...
# -----------------------------------------------------------------------------

# x.__init__()        # initialize an instance
# x.__repr__()        # the official representation as a string
# x.__str__()         # the informal value as a string
# x.__bytes__()       # the informal value as a byte array
# x.__format__()      # the value as a formatted string
# seq.__iter__()      # iterate through a sequence
# seq.__next__()      # get the next value from an iterator
# seq.__reversed__()  # create an iterator in reverse order
# x.__len__()         # number of items
# x.__copy__()        # create a custom object copy

# The list goes on: http://www.diveintopython3.net/special-method-names.html

# You can list all the magic methods related to classes by using dir():

print(dir(list))
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__',
# '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__',
# '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__',
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
# '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__',
# '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend',
# 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


# __str__ and __repr__
# -----------------------------------------------------------------------------

print(a)            # <__main__.Word object at 0x101ca8828>
print(repr(a))      # <__main__.Word object at 0x101ca8828>

class Word():
    def __init__(self, text):
        self.text = text
    def __str__(self):
        return self.text
    def __repr__(self):
        return 'Word("' + self.text + '")'

a = Word('Ha')

print(a)            # Ha
print(repr(a))      # Word("Ha")


# Another __str__ example
# -----------------------------------------------------------------------------

class Player():

    def __init__(self, name):
        self.name = name
        self.lives = 3
        self.level = 1
        self.score = 0

    def __str__(self):
        return ('Name: {0.name}, Lives: {0.lives}, Level: {0.level}, '
                'Score: {0.score}'.format(self))

player1 = Player('Morty')
print(player1)  # Name: Morty, Lives: 3, Level: 1, Score: 0


# __dict__
# -----------------------------------------------------------------------------
# Another magic method is __dict__. It's used to return the dictionary used to
# store an object’s attributes.

print(player1.__dict__)
# {'name': 'Morty', 'lives': 3, 'level': 1, 'score': 0}


# __file__
# -----------------------------------------------------------------------------
# If you want to take a look at the actual file to read the comments and
# docstring there, you can use the __file__ magic method to show you the
# path to where this module lives:

import os
print(os.__file__)
# /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/os.py


# __doc__
# -----------------------------------------------------------------------------
# prints the docstring of a module, function or class:

import random
print(random.__doc__)
print(random.choice.__doc__)


# __len__, __reversed__, __class__, __name__
# -----------------------------------------------------------------------------

normal_sequence = [1, 2, 3, 4, 5]

class CustomSequence():
    def __len__(self):
        return 5

    def __getitem__(self, index):
        return 'x{}'.format(index)

class CustomReversed():
    def __reversed__(self):
        return 'Reversed!'


for seq in normal_sequence, CustomSequence(), CustomReversed():
    print('\n{}: '.format(seq.__class__.__name__), end='')
    for i in reversed(seq):
        print(i, end=", ")
print('')
# list: 5, 4, 3, 2, 1,
# CustomSequence: x4, x3, x2, x1, x0,
# CustomReversed: R, e, v, e, r, s, e, d, !,
