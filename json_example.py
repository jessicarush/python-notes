'''JSON Example'''

# see also structured_file_formats.py

# The JSON (JavaScript Object Notation) module allows you to dump simple python
# data structures into a file and load it back in next time the programs runs.
# You can also use JSON to share data between different python programs or
# other programming languages. It's a useful, portable, easy-to-learn file
# format. The pythons data types it can store are: strings, numbers, booleans,
# lists and dictionaries with string keys.

import json

# The json.dump() function takes two arguments: a piece of data to store and
# the file object to store the data in.

numbers = [4, 5, 7, 9, 11, 13]
username = input("What is your name? ")
filename = 'numbers.json'

with open(filename, 'w') as fob:
    json.dump((numbers, username), fob)

# Read the data back in:

with open(filename) as fob:
    data = json.load(fob)

numbers2, username2 = data
print(type(numbers2))      # <class 'list'>
print(type(username2))     # <class 'str'>
print('Hello', username2)  # Hello Raja
print(numbers2)            # [4, 5, 7, 9, 11, 13]
