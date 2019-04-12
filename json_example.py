'''JSON Example'''


# see also structured_file_formats.py

# The JSON (JavaScript Object Notation) module allows you to dump simple python
# data structures into a file and load it back in next time the programs runs.
# You can also use JSON to share data between different python programs or
# other programming languages. It's a useful, portable, easy-to-learn file
# format. The pythons data types it can store are: strings, numbers, booleans,
# lists and dictionaries with string keys.

# There are two sets of functions for working with JSON:

# json.dump() and json.load() – for storing and retrieving JSON from a file
# json.dumps() and json.loads() – for creating and parsing JSON strings


# JSON to file
# -----------------------------------------------------------------------------

import json

# The json.dump() function takes two arguments: a piece of data to store and
# the file object to store the data in.

numbers = [4, 5, 7, 9, 11, 13]
username = input("What is your name? ")
filename = 'data/numbers.json'

with open(filename, 'w') as fob:
    json.dump((numbers, username), fob)

# Read the data back in with json.load():

with open(filename) as fob:
    data = json.load(fob)

print(type(data))          # <class 'list'>

numbers2, username2 = data

print(type(numbers2))      # <class 'list'>
print(type(username2))     # <class 'str'>
print('Hello', username2)  # Hello Raja
print(numbers2)            # [4, 5, 7, 9, 11, 13]


# JSON to strings
# -----------------------------------------------------------------------------
# JSON strings work well for when you want to share data structures between
# programs and languages (e.g. python dictionary to Javscript).

data = {
    'date': '2019-04-10',
    'count': 6,
    'session_id': 102
}

# create a JSON string with json.dumps():

data_json = json.dumps(data)

print(type(data_json), data_json)
# <class 'str'> {"date": "2019-04-10", "count": 6, "session_id": 102}

# parse a JSON string into a python data structure with json.loads():

json_string = '["hello", 100, [2019, 4, 10]]'

data = json.loads(json_string)

print(type(data), data)
# <class 'list'> ['hello', 100, [2019, 4, 10]]


# Encoders and Decoders (json.JSONDecoder, json.JSONEncoder)
# -----------------------------------------------------------------------------
# When you convert from Python to JSON, Python objects are encoded to the
# following JavaScript equivalents:

# Python    JSON
# ------    ------
# dict      Object
# list      Array
# tuple     Array
# str       String
# int       Number
# float     Number
# True      true
# False     false
# None      null


# Extending the JSONEncoder
# -----------------------------------------------------------------------------
# see structured_file_formats.py
