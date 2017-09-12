'''More from the Standard Library''''

# Counter() ------------------------------------------------------------------

from collections import Counter

jellybeans = ['red', 'red', 'orange', 'red', 'green', 'green']
jb_counter = Counter(jellybeans)
print(jb_counter)

# most_common() returns all elements in descending order
# (or just the top count if provided)

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

# deque() --------------------------------------------------------------------

# is a double-ended queue which has features of both a stack and a queue.
# It's useful for when you want to add/delete items from either end of a
# sequence.

def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

palindrome('racecar')   # returns True
palindrome('radar')     # returns True
palindrome('maam')      # returns True
palindrome('what')      # returns False

# The example above is just an example. If you wanted to actually check for
# paildromes you could also do:

def palindrome_better(word):
    return word == word[::-1]

palindrome_better('radar')    # returns True

# itertools ------------------------------------------------------------------

# itertools are special purpose iterator functions.
# each returns one item at a time when called within a for... in loop and
# rememebers its state between calls

import itertools

# chain()
# runs through its arguments as if they were a single iterable

for item in itertools.chain([1,2], ['a', 'b']):
    print(item)

# cycle()
# is an infinite iterator, cycling through its arguments

for item in itertools.cycle([1, 2]):
    print(item)

# accumulate()
# calculates accumulated values. By default it calculates the sum:

for item in itertools.accumulate([1, 2, 3, 4]):
    print(item)

# you can provide a function as a second argument to accumulate().
# this will be used instead of addition. The function should take two arguments
# and return a single result.

def multiply(a, b):
    return a * b

for item in itertools.accumulate([1, 2, 3, 4], multiply):
    print(item)
