# DICTIONARIES

# create a dict with = {}

info = {
    'firstname' : 'Mary',
    'lastname' : 'Jane',
    'age' : 70,
    'weight' : 130,
}

# convert to a dict with dict()

list_of_lists = [['a', 'A'], ['b', 'B'], ['c', 'C']]
list_of_tuples = [('d', 'D'), ('e', 'E'), ('f', 'F')]
tuple_of_lists = (['g', 'G'], ['h', 'H'], ['i', 'I'])
list_of_two_char_strings = ['jJ', 'kK', 'lL']
tuple_of_two_char_strings = ('mM', 'nM', 'oO')

dict_from_lol = dict(list_of_lists)
dict_from_lot = dict(list_of_tuples)
dict_from_tol = dict(tuple_of_lists)
dict_from_los = dict(list_of_two_char_strings)
dict_from_tos = dict(tuple_of_two_char_strings)

# Add or change an item:

info['age'] = 40
info['height'] = '5\'5"'

# Combine dicts with .update() - this would be like extend() for lists

location = {
    'street' : 'Main',
    'city' : 'Vancouver',
    'province' : 'BC',
}

info.update(location)

# delete an item by key with del

del info['age']

# delete all items with .clear()

info.clear()

# check for a key with in

print('city' in location)
print('Van' in location)

# get an value by [key]

print(location['street'])

# if the key is not present, you'll get an exception. To avoid this use the get() function.
# provide the key and an optional value. If the exists, you'll get its value. If not, you'll
# get the optional one if you provided one:

print(location.get('country', 'country not specified'))

# get all keys using .keys()

print(location.keys())

#or

list_of_keys = list(location.keys())
print(list_of_keys)

# get all values with .values()

print(location.values())

#or

list_of_values = list(location.values())
print(list_of_values)

# get all key-value pairs with .items()

print(location.items())

#or

list_of_items = list(location.items())
print(list_of_items)

# copy a dict with .copy()

location_copy = location.copy()
location['city'] = 'montreal'

print(location)
print(location_copy)

# setdefault() method is like get() for dictionaries. It looks for the key and if missing, creates it,
# but it does not change the value if the key is already there. 
# If you don't provide a value as with 'Canada' below, the value will be set to None

country = location.setdefault('country', 'Canada')

# defaultdict() specifies a default value for any new key up front when the dictionary is created. 
# In this example, any missing value will be an integer with a value 0

from collections import defaultdict

jellybeans = defaultdict(int)
jellybeans['red']

# The argument to defaultdict() is a function. The function returns the value for the missing key

def missing():
    return 'what?'

jellybeans = defaultdict(missing)
jellybeans['orange']

# you can use int(), list(), or dict() functions to return empty values for those types

jellybeans = defaultdict(int)   # returns 0
jellybeans = defaultdict(list)  # returns an empty list
jellybeans = defaultdict(dict)  # returns an empty dictionary

# you could also use lambda

jellybeans = defaultdict(lambda: 'what?')

# an example of a counter: 

jellybeans = defaultdict(int)

for key in ['red', 'red', 'orange', 'red']:
    jellybeans[key] += 1

