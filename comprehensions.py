'''Comprehensions'''


# List Comprehensions
# -----------------------------------------------------------------------------
# [expression for item in iterable]
# [expression for item in iterable if condition]

# Let's say we wanted to build a list of squares. Traditionally we could
# create a list, then use an iterator and range() like this:

squares = []
for number in range(1, 11):
    squares.append(number ** 2)

print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# or we could do it this way:

squares = list(range(1, 11))
for number in squares:
    squares[number-1] = number ** 2

print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# or we could use list comprehensions:
# [expression for item in iterable]

squares = [number ** 2 for number in range(1, 11)]

print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# First, define the expression for the values you want to store in the list,
# then write a for loop to generate the numbers you want to feed into the
# expression:

bottles = [(str(number) + ' bottles') for number in range(12, 49, 12)]

print(bottles)  # ['12 bottles', '24 bottles', '36 bottles', '48 bottles']

# List comprehension with if conditional:
# [expression for item in iterable if condition]

odds = [number for number in range(1, 10) if number % 2 == 1]

print(odds)  # [1, 3, 5, 7, 9]

# The above is the same as:

odds = []
for number in range(1, 10):
    if number % 2 == 1:
        odds.append(number)

# Because this expression is so simple we could obviously just do this:

odds = list(range(1, 10, 2))

# But the point here is to illustrate the syntax.

# List comprehension with if/else conditionals:
# [expression if condition else expression for item in iterable]

# For this example, the values in 'reps' belong to the 'sets' in 'units'.
# I want to fill out the reps list with zero values for the other units so
# that both lista re the same length and could be zipped togtether:

units = ['laps', 'seconds', 'sets', 'twirls', 'sets']
reps = ['10', '6']

# My onstincts would be to add the else at the end, but this is wrong!
# new_reps = [reps.pop() for unit in units if unit == 'sets' else '0']

new_reps = [reps.pop(0) if unit == 'sets' else '0' for unit in units]

print(new_reps)
# ['0', '0', '10', '0', '6']


# List Comprehensions: add a value
# ----------------------------------------------------------------------------
# You can add values at the end of your comprehension using the + operator:

import random

rgba = [random.random() for i in range(3)]
rgba.append(1)

# same as:
rgba = [random.random() for i in range(3)] + [1]

print(rgba)
# [0.2785526331653764, 0.2124238306054994, 0.6514248582355008, 1]


# List Comprehensions: nested loops example
# ----------------------------------------------------------------------------
# Another example using nested loops.
# Here's the traditional way:

rows = range(1, 4)
cols = range(1, 3)

cells = []
for row in rows:
    for col in cols:
        cells.append((row, col))

print(cells)  # [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2)]

# or use a comprehension:

rows = range(1, 4)
cols = range(1, 3)

cells = [(row, col) for row in rows for col in cols]

print(cells)  # [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2)]

# Another example of two expressions in a list comprehension.
# Lets say we wanted to flatten a list of lists into one list:

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]

print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# NOTE: In general, for readability, avoid using more than two expressions
# in a list comprehension whether that be two loops or a loop and a condition.
# If you need to write more, consider normal if and for statements and possibly
# helper functions (see helper_functions.py)


# List Comprehensions: practical example from data plotting
# -----------------------------------------------------------------------------

import pandas

# An example from a pandas, bokeh data plot. What we're trying to do is create
# a new DataFrame column containing a color which will be used for the data
# plot; green if the price went up and red if the price went down.

df = pandas.read_csv('data/NEO_historical.csv')
difference = df.close - df.open
df['color'] = ['green' if x > 0 else 'red' for x in difference]

# Note the 'expression' can be a function, and the iterable can be a zip()
# containing more than one iterable. This essentially does the same as above:

def color_by_value(open_price, close_price):
    if close_price >= open_price:
        color = 'green'
    else:
        color = 'red'
    return color

df['color'] = [color_by_value(open_price, close_price)
               for open_price, close_price in zip(df.open, df.close)]

# see also: pygal_intro.py


# Dictionary Comprehensions
# -----------------------------------------------------------------------------
# {key_expression : value_expression for expression in iterable}:

word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)        # {'l': 1, 'e': 2, 't': 2, 'r': 1, 's': 1}
print(type(letter_counts))  # <class 'dict'>

# Technically we are counting some letters twice.
# By converting the word into a set(), we remove any duplicates for the
# checking part. We still get the same result from the count, but we're only
# asking it to count each letter once.

word = 'letters'
letter_counts = {letter: word.count(letter) for letter in set(word)}

# Review dictionary comprehensions

squares = {number: (number * number) for number in range(7)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}


# Set comprehensions
# -----------------------------------------------------------------------------
# {expression for expression in iterable}

a_set = {number ** 2 for number in range(1, 10)}
print(a_set)  # {64, 1, 4, 36, 9, 16, 49, 81, 25}

# Review set comprehensions:

odds = {number for number in range(10) if number % 2 != 0}
print(odds)  # {1, 3, 5, 7, 9}


# Generator comprehensions (see also generators.py)
# -----------------------------------------------------------------------------
# Tuples don't have comprehensions. Changing the [] or {} to () is actually
# creating a generator comprehension and returns a generator object.

# Generator comprehensions are helpful for when large amounts of data would
# otherwise consume too much memory and possible crash your program. This
# example imagines we wan to read a file and get the length of each line.
# If we use a list comprehensions, each value would have to be held in memory.
# This works fine for small files:

value = [len(line) for line in open('data/example.txt')]

print(value)
# [8, 12, 48, 22, 7]

# Generator expressions don't materialize the whole output sequence when
# they're run. They evaluate to an iterator that yields one item at a time.

gen = (len(line) for line in open('data/example.txt'))

print(type(gen))  # <class 'generator'>
print(next(gen))  # 8

for x in gen:
    print(x)
# 12
# 48
# 22
# 6

# Once a generator has been exhausted, it's done. If we trying getting the
# next value we'll raise a StopIteration exception.

# Another interesting thing about generator expressions, is that they can
# be composed together. See here:

gen = (len(line) for line in open('data/example.txt'))

squares = ((x, x**2) for x in gen)

print(next(squares))  # (8, 64)
print(next(squares))  # (12, 144)
print(next(squares))  # (48, 2304)

# Chaining generators like this executes very quickly in Python. Bottom line
# is list comprehensions can cause problems for very large inputs of data by
# hogging too much memory. Generator expression avoid this by producing
# outputs one at a time as an iterator.
