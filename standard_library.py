# More Functions from the Standard Library

# Functions that convert types

float(True)                                 # returns 1.0
int(True)                                   # returns 1
str(True)                                   # returns True
list((1,2,3))                               # returns [1, 2, 3]
dict((('a', 'A'), ('b', 'B'), ('c', 'C')))  # returns {'c':'C', 'a': 'A', 'b': 'B'}
set((('a'), ('b'), ('c')))                  # returns {'b', 'c', 'a'}
tuple((('a'), ('b'), ('c')))                # returns ('a', 'b', 'c')

# The enumerate() function
# takes apart a list and feeds each item to the for loop, adding a number to each item as a bonus. 
# To compare, test a regular for loop first.

for colour in colours:
    print(colour)

# If a start number isn't specified, the first item is 0

for colour in enumerate(colours):
    print(colour)

# Start at 1 instead:

for number, colour in enumerate(colours, 1):
    print(number, colour)
    
# Counter()
from collections import Counter

jellybeans = ['red', 'red', 'orange', 'red', 'green', 'green']
jb_counter = Counter(jellybeans)
print(jb_counter)

# most_common() 
# returns all elements in descending order (or just the top count if provided)

jb_counter.most_common(1)

# combine, find difference and find intersection of counters using +, -, &

jellybeans1 = ['red', 'red', 'orange', 'red', 'green', 'green']
jellybeans2 = ['black', 'red', 'yellow', 'yellow']

jb_counter1 = Counter(jellybeans1)
jb_counter2 = Counter(jellybeans2)

jb_counter1 + jb_counter2   # returns {'red': 4, 'green': 2, 'yellow': 2, 'black': 1, 'orange': 1}
jb_counter1 - jb_counter2   # returns {'red': 2, 'green': 2, 'orange': 1}
jb_counter2 - jb_counter1   # returns {'yellow': 2, 'black': 1}
jb_counter1 & jb_counter2   # returns {'red': 1}
