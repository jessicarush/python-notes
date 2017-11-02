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
colour_tuple = ('Emerald', 'Pantone 17-5641', 'sRGB 0 148 115')

# Tuples are ordered:

print(colour_tuple[1])

# Tuples let you assign multiple variables at once:

a, b, c = colour_tuple
print(a)
print(b)
print(c)

# This is sometimes called 'tuple unpacking'

text = "spot colour: {0[1]}, name: {0[0]}, screen value: {0[2]}"
print(text.format(colour_tuple))

# You can use tuples to swap variable values in one line:

a, b = 2, 3

print('a is {}, b is {}'.format(a, b))  # a is 2, b is 3

a, b = b, a

print('a is {}, b is {}'.format(a, b))  # a is 3, b is 2


# The tuple() function lets you convert something to a tuple:

colours_list = ['orange', 'yellow', 'purple']
colours_tuple = tuple(colours_list)
print(type(colours_tuple)) # tuple

colours_str = 'orange, yellow, purple'
colours_tuple = tuple(colours_str.split(', '))
print(colours_tuple)  # ('orange, 'yellow', 'purple')

# -----------------------------------------------------------------------------
# Benefits of using tuples
# -----------------------------------------------------------------------------
# - Tuples use less space
# - You can't mess with tuple items by mistake
# - You can use tuples as dictionary keys (you can't use a list because lists
#   are mutable and dictionary keys are not allowed to be mutable)
# - Named tuples can be a simple alternative to objects
# - Function arguments are passed as tuples

# -----------------------------------------------------------------------------
# Named Tuples
# -----------------------------------------------------------------------------
# A named tuple is a subclass of tuples with which you can access values by
# name (with .name) as well as position (with [offset])

from collections import namedtuple

Room = namedtuple('Room', 'floor windows')
kitchen = Room('hardwood', '4')

# Testing:

print(kitchen)
print(kitchen.floor)
print(kitchen.windows)
print(kitchen[0])

# You can also make a named tuple from a dictionary

parts = {'floor': 'linoleum', 'windows': '2'}

bedroom = Room(**parts)

# BTW **parts is a keyword argument. It extracts the keys and values from the
# parts dict and supplies them as arguments to Room()

# Testing:

print(bedroom)
print(bedroom.floor)
print(bedroom.windows)
print(bedroom[0])

# Named tuples look and act like an immutable object.
# You can access attributes by using dot notation instead of dict style['key']
# You can use it as a dict key.

# Though tuples are immutable, tuples can contain mutable items. For example,
# You could have a tuple of lists where the lists themselves cannot be changed
# in the tuple but the list contents can change.
