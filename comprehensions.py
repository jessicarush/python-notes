# List Comprehensions

# You could build a list of integers like this:

number_list = []
number_list.append(1)
number_list.append(2)
number_list.append(3)
number_list.append(4)
number_list.append(5)

# or use an iterator and range() like this:

number_list = []
for number in range(1,6):
    number_list.append(number)

# or turn the output of range directly into a list:

number_list = list(range(1,6))

# or use list comprehensions: 
# [expression for item in iterable]

number_list = [number for number in range(1,6)]

# The expression starts the list, the item is part of the for loop

number_list = [number+3 for number in range(0,5)]

# List comprehension with conditionals:
# [expression for item in iterable if condition]

number_list = [number for number in range (1,10) if number % 2 == 1]

# The above is the same as:

number_list = []
for number in range(1,10):
    if number % 2 == 1:
        number_list.append(number)
        
# Another example with nested loops. Here's the traditional way:

rows = range(1,4)
cols = range(1,3)

for row in rows:
    for col in cols:
        print (row, col)

# or use a comprehension: Assign it to a variable 'cells' making it a list of (row, col) tuples:

rows = range(1,4)
cols = range(1,3)
cells = [(row, col) for row in rows for col in cols]
for cell in cells:
    print(cell)

# You can also use tuple unpacking to pull the row an col values from each tuple:

for row, col in cells:
    print(row, col)
    
# Review list comprehensions [expression for item in iterable]:

even_numbers = [i for i in range(0, 10, 2)]
print(even_numbers)

# ... or [expression for item in iterable if condition]:

even_numbers = [i for i in range(10) if i % 2 == 0]
print(even_numbers)

# Dictionary Comprehensions
# {key_expression : value_expression for expression in iterable}:

word = 'letters'
letter_counts = {letter : word.count(letter) for letter in word}

# Technically we are counting some letters twice.
# By converting the word into a set(), we remove any duplicates for the checking part.

word = 'letters'
letter_counts = {letter : word.count(letter) for letter in set(word)}

# Review dictionary comprehensions {key_expression: value_expression for expression in iterable}:

squares = { number: number*number for number in range(10)}
print(squares)

# Set comprehensions
# {expression for expression in iterable}

a_set = {number for number in range(1,6) if number % 3 == 1}

# Review set comprehensions {expression for expression in iterable}:

odds = {number for number in range(10) if number % 2 != 0}
print(odds)

# Generator comprehensions
# Tuples don't have comprehensions. 
# Changing the [] or {} of a comprehesion to () is actually a generator comprehesion and returns a generator object.

number_thing = (number for number in range(1,6))

# Review generator comprehensions (expression for expression in iterable):

for thing in (number for number in range(10)):
    print ('Got', thing)
