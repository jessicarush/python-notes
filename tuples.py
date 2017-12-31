'''Tuples'''

# -----------------------------------------------------------------------------
# Tuple methods
# -----------------------------------------------------------------------------

dir(tuple)
#  [..., 'count', 'index']

# -----------------------------------------------------------------------------
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

# It's the intention that lists contain items of the same type,
# whereas tuples contain related items, not necessarily the same type.
# Lists contain items that could change.
# Tuples contain items that are not likely to change.

# for example:

colour_list = ['green', 'blue', 'red']
colour_tuple = ('Emerald', 'Pantone 17-5641', 'rgb(0, 148, 115)')

# Tuples are ordered:

print(colour_tuple[1])  # Pantone 17-5641

text = "spot colour: {0[1]} \nname: {0[0]} \nscreen value: {0[2]}"
print(text.format(colour_tuple))
# spot colour: Pantone 17-5641
# name: Emerald
# screen value: rgb(0, 148, 115)

# Tuples let you assign multiple variables at once:
# This is called 'tuple unpacking'

a, b, c = colour_tuple
print(a)  # Emerald
print(b)  # Pantone 17-5641
print(c)  # rgb(0, 148, 115)

# You can use tuples to assign or swap variable values in one line:

a, b = 'A', 'B'
print('a is {}, b is {}'.format(a, b))  # a is A, b is B

a, b = b, a
print('a is {}, b is {}'.format(a, b))  # a is B, b is A

# The tuple() function lets you convert something to a tuple:

colours_list = ['orange', 'yellow', 'purple']
colours_tuple = tuple(colours_list)
print(type(colours_tuple)) # tuple

colours_str = 'orange, yellow, purple'
colours_tuple = tuple(colours_str.split(', '))
print(colours_tuple)  # ('orange, 'yellow', 'purple')

# -----------------------------------------------------------------------------
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
print(kitchen[3])       # 150

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
print(bedroom[3])       # 250

# Named tuples look and act like an immutable object. You can access attributes
# by using dot notation instead of the dict style['key']. Because tuples are
# immutable, you can use then as a dict key.

apartment = {bedroom : 'stuff...', kitchen: 'things...'}

# Though tuples are immutable, tuples can contain mutable items. For example,
# You could have a tuple of lists where the lists themselves cannot be changed
# in the tuple but the list contents can change.

# -----------------------------------------------------------------------------
# Benefits of using tuples
# -----------------------------------------------------------------------------
# - Tuples use less space
# - You can't mess with tuple items by mistake
# - You can use tuples as dictionary keys (you can't use a list because lists
#   are mutable and dictionary keys are not allowed to be mutable)
# - Named tuples can be a simple alternative to objects
# - Function arguments are passed as tuples
