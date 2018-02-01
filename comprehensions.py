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

# Another example of two expressions in a list comprehension.
# Lets say we wanted to flatten a list of lists into one list:

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]

print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# NOTE: In general, for readability, avoid using more than two expressions
# in a list comprehension whether that be two loops or a loop and a condition.
# If you need to write more, consider normal if and for statements and possibly
# helper functions (see helper_functions.py)

# -----------------------------------------------------------------------------
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

df['color'] = [color_by_value(open_price, close_price) \
               for open_price, close_price in zip(df.open, df.close)]

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

num_gen = (number * number for number in range(1,6))

print(type(num_gen))   # <class 'generator'>
for num in num_gen:    # you can then iterate over it
    print(num)

# Lets write another example, that checks if whether any item in one list
# is present in another. Starting simple:

animals = ['fox', 'snake', 'white owl', 'cat']
codewords = ['red box', 'cracked buttons', 'white owl', 'giant cactus']

# (expression for expression in iterable)
if any(animal in codewords for animal in animals):
    print('1. There is an animal in the words')

# examine the long version:
for animal in animals:
    if animal in codewords:
        print('2. There is an animal in the words')

# Let's try again but allow for the animal to be anywhere in the phrase:

animals = ['fox', 'snake', 'owl', 'cat']
codewords = ['red box', 'cracked buttons', 'white owl', 'giant cactus']

# (expression for expression in iterable)
for words in codewords:
    if any(animal in words for animal in animals):
        print('3. There is an animal in the words')

# The long way:
for words in codewords:
    for animal in animals:
        if animal in words:
            print('4. There is an animal in the words')
