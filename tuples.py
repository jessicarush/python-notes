# TUPLES are immutable: you can't add, change or delete items

colours_tuple = ('green', 'blue', 'red')

# Tuples let you assign multiple variables at once:

a, b, c = colours_tuple
print(a)
print(b)
print(c)

# You can use tuples to swap variable values in one line:

a, c = c, a
print(a)
print(b)

# The tuple() function lets you convert something to a tuple:

colours_list = ['orange', 'yellow', 'purple']
colours_tuple = tuple(colours_list)
print(colours_tuple)

"""
Benefits of using tuples:
- Tuples use less space
- You can't mess with tuple items by mistake
- You can use tuples and dictionary keys
- Named tuples can be a simple alternative to objects
- Function arguments are passed as tuples
"""

# Named Tuples
# A named tuple is a subclass of tuples with which you can access values by name (with .name) 
# as well as position (with [offset])

from collections import namedtuple

Room = namedtuple('Room', 'floor windows')
kitchen = Room('hardwood', '4')

# Testing:

print(kitchen)
print(kitchen.floor)
print(kitchen.windows)
print(kitchen[0])

# You can also make a names tuple from a dict

parts = {'floor': 'linoleum', 'windows': '2'}

bedroom = Room(**parts)

# Testing:

print(bedroom)
print(bedroom.floor)
print(bedroom.windows)
print(bedroom[0])

# Named tuples look and act like an immutable object
# You can access attributes by using dot notation instead of dict style []
# You can use it as a dict key 
