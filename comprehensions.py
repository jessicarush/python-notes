'''Comprehensions'''

# -----------------------------------------------------------------------------
# List Comprehensions
# -----------------------------------------------------------------------------
# [expression for item in iterable]
# [expression for item in iterable if condition]

# Let's say we wanted to build a list of squares. Traditionally we could
# create a list, then use an iterator and range() like this:

squares = []
for number in range(1,11):
    squares.append(number ** 2)

print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# or we could do it this way:

squares = list(range(1,11))
for number in squares:
    squares[number-1] = number ** 2

print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# or we could use list comprehensions:
# [expression for item in iterable]

squares = [number ** 2 for number in range(1,11)]

print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# First, define the expression for the values you want to store in the list,
# then write a for loop to generate the numbers you want to feed into the
# expression:

bottles = [(str(number) + ' bottles') for number in range(12,49,12)]

print(bottles)  # ['12 bottles', '24 bottles', '36 bottles', '48 bottles']

# List comprehension with conditionals:
# [expression for item in iterable if condition]

odds = [number for number in range(1,10) if number % 2 == 1]

print(odds)  # [1, 3, 5, 7, 9]

# The above is the same as:

odds = []
for number in range(1,10):
    if number % 2 == 1:
        odds.append(number)

# Because this expression is so simple we could obviously just do this:

odds = list(range(1,10,2))

# But the point here is to illustrate the syntax. The idea is to use an
# actual expression instead of just the number as is.

# Another example with nested loops. Here's the traditional way:

rows = range(1,4)
cols = range(1,3)

cells = []
for row in rows:
    for col in cols:
        cells.append((row, col))

print(cells)  # [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2)]

# or use a comprehension:

rows = range(1,4)
cols = range(1,3)

cells = [(row, col) for row in rows for col in cols]

print(cells)  # [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2)]

# see also: pygal_intro.py

# -----------------------------------------------------------------------------
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
# {key_expression: value_expression for expression in iterable}:

squares = {number: (number * number) for number in range(7)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}

# -----------------------------------------------------------------------------
# Set comprehensions
# -----------------------------------------------------------------------------
# {expression for expression in iterable}

a_set = {number for number in range(1, 10) if number % 3 == 1}
print(a_set)  # {1, 4, 7}
# Review set comprehensions {expression for expression in iterable}:

odds = {number for number in range(10) if number % 2 != 0}
print(odds)  # {1, 3, 5, 7, 9}

# -----------------------------------------------------------------------------
# Generator comprehensions
# -----------------------------------------------------------------------------
# Tuples don't have comprehensions.
# Changing the [] or {} of a comprehension to () is actually
# a generator comprehension and returns a generator object.

number_thing = (number for number in range(1,6))

print(type(number_thing))   # <class 'generator'>
for thing in number_thing:  # you can then iterate over it
    print(thing)

# Review generator comprehensions (expression for expression in iterable):

for thing in (number for number in range(10)):
    print(thing)
