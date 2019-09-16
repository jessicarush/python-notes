'''Tuples'''


# Tuple methods
# -----------------------------------------------------------------------------

print(dir(tuple))
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__',
# '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
# '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__',
# '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__',
# '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']


# Tuples are ordered (like lists) and immutable (unlike lists)
# -----------------------------------------------------------------------------
# Create a tuple by providing values in brackets separated by commas. If you
# need to create a tuple from one value, you must add a comma at the end,
# otherwise it won't actually be a tuple. TBH, it's actually the commas that
# make groups a tuple:

colour_tuple = ('Emerald')
print(type(colour_tuple))  # <class 'str'>

colour_tuple = ('Emerald',)
print(type(colour_tuple))  # <class 'tuple'>

red = 'Red'
colour_tuple = 'Emerald', red, 'Blue'
print(type(colour_tuple))  # <class 'tuple'>

# REPEAT: It's not the enclosing parenthesis that define a tuple, it the fact
# that we're providing one or more values separated by commas.

# It's the intention that lists contain items of the same type, whereas tuples
# contain related items, not necessarily the same type. Lists contain items
# that could change. Tuples contain items that are not likely to change.
# For example, we would not put three different stock symbols in a tuple, but
# we might create a tuple of stock symbol, its current price, high, and low
# for the day. The primary purpose of a tuple is to aggregate different pieces
# of data together into one container.

# for example:

colour_list = ['green', 'blue', 'red']
colour_tuple = ('green', 'Pantone 17-5641', 'rgb(0, 148, 115)')

# Tuples are ordered:

print(colour_tuple[1])  # Pantone 17-5641

text = 'spot colour: {0[1]} \nname: {0[0]} \nscreen value: {0[2]}'

print(text.format(colour_tuple))
# spot colour: Pantone 17-5641
# name: green
# screen value: rgb(0, 148, 115)


# Tuple unpacking
# -----------------------------------------------------------------------------
# Tuples let you assign multiple variables from a sequence at once:
# This is called 'tuple unpacking'. Note that the sequence can be any iterable
# but the number of variables must match the number of items in the sequnece:

a, b, c = colour_list

print(a)  # green
print(b)  # blue
print(c)  # red

# If you don't care about all the variables, the common method is to use '_':

_, color, _ = colour_list

print(color)  # blue

# If you hava a variable length iterable, you can assign the rest using '*':
color, *etc = colour_list

print(color)  # green
print(etc)    # ['blue', 'red']

# This can be used to select anywhere in the assignemnt. The '*' variable will
# always be a list:

long_color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

c1, c2, *rest, c3 = long_color_list
print(c1)    # red
print(c2)    # orange
print(c3)    # purple
print(rest)  # [yellow, green, blue]

# You can use also tuples to assign or swap variable values in one line:

a, b = 'A', 'B'
print('a is {}, b is {}'.format(a, b))  # a is A, b is B

a, b = b, a
print('a is {}, b is {}'.format(a, b))  # a is B, b is A


# tuple()
# -----------------------------------------------------------------------------
# The tuple() function lets you convert something to a tuple:

colours_list = ['orange', 'yellow', 'purple']
colours_tuple = tuple(colours_list)
print(type(colours_tuple)) # tuple

colours_str = 'orange, yellow, purple'
colours_tuple = tuple(colours_str.split(', '))
print(colours_tuple)  # ('orange, 'yellow', 'purple')


# Named Tuples
# -----------------------------------------------------------------------------
# A named tuple is a subclass of tuples with which you can access values by
# name (with .name) as well as position (with [offset])

from collections import namedtuple

Room = namedtuple('Room', 'name floor windows sqft')
kitchen = Room('kitchen', 'tile', 4, 150)

# Testing:

print(kitchen)          # Room(name='kitchen, floor='tile', windows=4, sqft=150)
print(kitchen.floor)    # tile
print(kitchen.windows)  # 4
print(kitchen.sqft)     # 150

# You can also make a named tuple from a dictionary

parts = {'name': 'bedroom', 'floor': 'wood', 'windows': 2, 'sqft': 250}

bedroom = Room(**parts)

# BTW **parts is a keyword argument. It extracts the keys and values from the
# parts dict and supplies them as arguments to Room(). Note that the dictionary
# keys must match the named tuple keys and there must be the same amount of
# items in both.

# Testing:

print(bedroom)          # Room(name='bedroom', floor='wood', windows=2, sqft=250)
print(bedroom.floor)    # wood
print(bedroom.windows)  # 2
print(bedroom.sqft)     # 250

# Named tuples look and act like an immutable object. You can access attributes
# by using dot notation instead of the dict style['key']. Since tuples are
# immutable, you can use them as a dict key.

apartment = {bedroom : 'stuff...', kitchen: 'things...'}

# You can also 'unpack' a named tuple, just like a regular one:

name, floor, windows, sqft = bedroom

# Though tuples are immutable, tuples can contain mutable items. For example,
# You could have a tuple of lists where the lists themselves cannot be changed
# in the tuple but the list contents can change.

# Named tuples are ideal for storing a fixed group of values that we want to
# access individually by name. Because of their immutability though, if you
# don't know in advance what all the values will be, or the values might
# change, you might be better off using a dictionary.


# Benefits of using tuples
# -----------------------------------------------------------------------------
# - Tuples use less space
# - You can't mess with tuple items by mistake (immutable)
# - You can use tuples as dictionary keys (dictionary keys cannot be mutable)
# - Named tuples can be a simple alternative to class objects (if you don't
#   need any behaviours)
# - Function arguments are passed as tuples
