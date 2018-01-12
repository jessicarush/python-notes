'''Dictionaries'''

# -----------------------------------------------------------------------------
# Dictionary methods
# -----------------------------------------------------------------------------

dir(dict)
#  [..., 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem',
#  'setdefault', 'update', 'values']

# -----------------------------------------------------------------------------
# Creating a dictionary
# -----------------------------------------------------------------------------
# create a dict with = {}

person = {
    'first' : 'Mary',
    'last' : 'Jane',
    'age' : 70,
    'height' : 165,
    }

# Add or change an item

person['age'] = 40
person['weight'] = 140

# -----------------------------------------------------------------------------
# Convert to a dict with .dict()
# -----------------------------------------------------------------------------

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

# -----------------------------------------------------------------------------
# Combine dicts with .update()
# -----------------------------------------------------------------------------
# this would be like extend() for lists

location = {
    'apt' : '2',
    'number' : '1234',
    'street' : 'Main',
    'city' : 'Vancouver',
    'province' : 'BC',
    }

person.update(location)

# -----------------------------------------------------------------------------
# Delete an item by key with del
# -----------------------------------------------------------------------------
del person['age']

# -----------------------------------------------------------------------------
# Delete all items with .clear()
# -----------------------------------------------------------------------------
person.clear()

# -----------------------------------------------------------------------------
# Remove an item and use it with .pop() or .popitem()
# -----------------------------------------------------------------------------
# The .pop() and .popitem() methods are like .pop() for list. They remove the
# item from the dict but make it available for you to use. The differences
# between the two are:
#   1. pop() returns just the value, popitem() returns both key and value.
#   2. pop() lets you choose the key, whearas .popitem() takes no arguments;
#      it removes an arbitrary item from the dict.

person = {'first' : 'Mary', 'last' : 'Jane', 'age' : 70, 'height' : 165,}

popped = person.popitem()
print(person)                # {'first': 'Mary', 'last': 'Jane', 'age': 70}
print(popped, type(popped))  # ('height', 165) <class 'tuple'>

popped = person.pop('age')
print(person)                # {'first': 'Mary', 'last': 'Jane'}
print(popped, type(popped))  # 70 <class 'int'>

# Note with .pop():
# If key is found - the item is removed/popped from the dictionary
# If key is not found - the value specified as the second argument is returned
# If key is not found and a second argument is not specified - a KeyError
# exception is raised.

popped = person.pop('satus', 'nope')
print(popped, type(popped))  # nope <class 'str'>

# -----------------------------------------------------------------------------
# get a value by [key] and .get()
# -----------------------------------------------------------------------------
print(location['street'])

# if the key is not present, you'll get an exception. To avoid this use the
# get() function. Provide the key and an optional value. If the exists, you'll
# get its value. If not, you'll get None or the optional value:

print(location.get('country')) # returns None
print(location.get('country', 'country not specified')) # country not specified

# Or use 'in' to test when looking for a key:

while True:
    key = input('Enter a key (q to quit): ')
    if key == 'q':
        break
    elif key in location:
        print(location[key])
    else:
        print('There is no ' + key)

# Again, using .get() to avoid an exception:

while True:
    key = input('Enter a key (q to quit): ')
    if key == 'q':
        break
    value = location.get(key, 'There is no ' + key)
    print(value)

# -----------------------------------------------------------------------------
# .keys() .values() .items()
# -----------------------------------------------------------------------------
# When iterating over keys, values or both,
# keep in mind that keys are the default:

for i in location.keys():
    print(i)
# apt
# number
# street
# city
# province

# is the same as:
for i in location:
    print(i)
# apt
# number
# street
# city
# province

# but the other two methods (values and items) are still required:
for i in location.values():
    print(i)
# 2
# 1234
# Main
# Vancouver
# BC

for k, v in location.items():
    print(k, '–', v)
# apt – 2
# number – 1234
# street – Main
# city – Vancouver
# province – BC

# -----------------------------------------------------------------------------
# Convert to a string with join()
# -----------------------------------------------------------------------------

key_string = ', '.join(location.keys())
print(key_string)  # apt, number, street, city, province

value_string = ', '.join(location.values())
print(value_string)  # 2, 1234, Main, Vancouver, BC

# -----------------------------------------------------------------------------
# Sort by dict keys
# -----------------------------------------------------------------------------

ordered_keys = list(location.keys())

ordered_keys.sort()
for key in ordered_keys:
    print(key, '–', location[key])

# location.keys() behaves like a sequence and can therefor be passed to sorted:

for key in sorted(location.keys()):
    print(key, '–', location[key])

# -----------------------------------------------------------------------------
# Sort by dict values
# -----------------------------------------------------------------------------
# this trick returns a list of tuples from a dict, sorted by value:

ordered_vals = sorted(location.items(), key=lambda x: x[1])
print(ordered_vals)

# -----------------------------------------------------------------------------
# Copy a dict with .copy()
# -----------------------------------------------------------------------------

location_copy = location.copy()
location['city'] = 'montreal'

print(location)
print(location_copy)

# -----------------------------------------------------------------------------
# Create a new dict from a sequence with .fromkeys()
# -----------------------------------------------------------------------------
# The fromkeys() method creates a new dictionary with keys from a sequence and
# also takes an optional single value parameter (if no value is specified,
# the values will all be set to None).

person = {'first' : 'Mary', 'last' : 'Jane', 'age' : 70, 'height' : 165,}
things = ['thing1', 'thing2', 'thing3', 'thing4']

new_dict = dict.fromkeys(things, 0.0)

for k, v, in new_dict.items():
    print(k, '-', v)
# thing1 - 0.0
# thing2 - 0.0
# thing3 - 0.0
# thing4 - 0.0

new_dict = dict.fromkeys(person)

for k, v, in new_dict.items():
    print(k, '-', v)
# first - None
# last - None
# age - None
# height - None

# NOTE: If you don't want the new dictionary values to all be the same thing,
# but instead another sequence, use the .zip() function: see zip_function.py

# -----------------------------------------------------------------------------
# setdefault()
# -----------------------------------------------------------------------------
# setdefault() method is like get() for dictionaries. It looks for the key and
# if missing, creates it, but it does not change the value if the key is
# already there. If you don't provide a value as with 'Canada' below, the
# value will be set to None

country = location.setdefault('country', 'Canada')

# -----------------------------------------------------------------------------
# defaultdict()
# -----------------------------------------------------------------------------
# defaultdict() specifies a default value for any new key up front when the
# dictionary is created. In this example, any missing value will be an integer
# with a value 0

from collections import defaultdict

jellybeans = defaultdict(int)
jellybeans['red']

# The argument to defaultdict() is a function. The function returns the value
# for the missing key.

def missing():
    print('A value was not entered for a new key')
    print('It has been given a default value of 0.0')
    return 0.0

jellybeans = defaultdict(missing)
jellybeans['orange']
print(jellybeans['orange'])

# you can use int(), list(), or dict() functions to return empty values for
# those types:

jellybeans = defaultdict(int)   # returns 0
jellybeans = defaultdict(list)  # returns an empty list
jellybeans = defaultdict(dict)  # returns an empty dictionary

# if you wanted to add items to the the key's value list as with
# jellybeans = defaultdict(list):

jellybeans = defaultdict(list)
jellybeans['archived'].append('gray')
jellybeans['archived'].append('beige')
print(jellybeans['archived'])  # ['gray', 'beige']

# you could also use lambda

jellybeans = defaultdict(lambda: None)
jellybeans['red']
print(jellybeans['red'])  # None

# an example of a counter:

jellybeans = defaultdict(int)

for key in ['red', 'red', 'orange', 'red']:
    jellybeans[key] += 1

print(jellybeans)  # defaultdict(<class 'int'>, {'red': 3, 'orange': 1})

# -----------------------------------------------------------------------------
# OrderedDict()
# -----------------------------------------------------------------------------
# OrderedDict() remembers the order of key addition and returns them in that
# same order (remember, dictionaries are NOT usually ordered like lists)

from collections import OrderedDict

numbers = OrderedDict([
    ('one', 'uno'),
    ('two', 'dos'),
    ('three', 'tres'),
    ('four', 'quatro')
    ])

numbers['five'] = 'cinqo'
print(numbers)
# OrderedDict([('one', 'uno'), ('two', 'dos'), ('three', 'tres'), ...])
