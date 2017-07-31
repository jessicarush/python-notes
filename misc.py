# Python philosophy
import this 

# Functions that convert types
float(True)                                 # returns 1.0
int(True)                                   # returns 1
str(True)                                   # returns True
list((1,2,3))                               # returns [1, 2, 3]
dict((('a', 'A'), ('b', 'B'), ('c', 'C')))  # returns {'c':'C', 'a': 'A', 'b': 'B'}
set((('a'), ('b'), ('c')))                  # returns {'b', 'c', 'a'}
tuple((('a'), ('b'), ('c')))                # returns ('a', 'b', 'c')

# Continuing lines with \
long_text = 'A long time ago' + \
    ' in a galaxy far, far away' + \
    ' blah blah bla'

# None
"""
None is not the same as False. Though it may look false when evaluated as a boolean,
None is technically none as seen here:
"""
    
thing = None 

def is_none(thing):
    if thing is None:
        print("it's none")
    elif thing:
        print("it's True")
    else:
        print("it must be False")

is_none(thing)

# The enumerate() function
"""
The enumerate function takes apart a list and feeds each item to the for loop, 
adding a number to each item as a bonus. To compare, test a regular for loop first.
"""

for colour in colours:
    print(colour)

# If a start number isn't specified, the first item is 0
for colour in enumerate(colours):
    print(colour)

# Start at 1 instead:
for number, colour in enumerate(colours, 1):
    print(number, colour)
