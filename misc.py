# Python philosophy:

import this

# About None:

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

# Keyword arguments: **name
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

# Measuring Time:

# A quick way of timing something is to get the current time, do something, get
# the new time, and then subtract the original time from the new time.

from time import time, sleep

t1 = time()

sleep(2.0)

print(time() - t1)

# About range()

# NOTE: when using range() alone, you're actually creating a range object

numbers = range(0, 100)
print(type(numbers)) # class 'range'

print(numbers[0:50:2] == range(0,50,2)) # True
