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
    'firstname' : 'Mary',
    'lastname' : 'Jane',
    'age' : 70,
    'weight' : 130,
}

# Add or change an item

person['age'] = 40
person['height'] = '5\'5"'

# convert to a dict with dict() ----------------------------------------------

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
# delete an item by key with del
# -----------------------------------------------------------------------------
del person['age']

# -----------------------------------------------------------------------------
# delete all items with .clear()
# -----------------------------------------------------------------------------
person.clear()

# -----------------------------------------------------------------------------
# get an value by [key] and get()
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

# Again, using get() to avoid an exception:

while True:
    key = input('Enter a key (q to quit): ')
    if key == 'q':
        break
    value = location.get(key, 'There is no ' + key)
    print(value)

# -----------------------------------------------------------------------------
# .keys() .values() .items()
# -----------------------------------------------------------------------------

# get all keys using .keys()

print(location.keys())

key_list = list(location.keys())
print(key_list)

# get all values with .values()

print(location.values())

value_list = list(location.values())
print(value_list)

# get all key-value pairs with .items()

print(location.items())

items_list = list(location.items())
print(items_list)

# When iterating over keys, values or both... keep in mind that keys are the
# default so:

for i in location.keys():
    print(i)

# is the same as:

for i in location:
    print(i)

# but the other two methods (values and items) are still required:

for i in location.values():
    print(i)

for k, v in location.items():
    print(k, '–', v)

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
# copy a dict with .copy()
# -----------------------------------------------------------------------------

location_copy = location.copy()
location['city'] = 'montreal'

print(location)
print(location_copy)

# -----------------------------------------------------------------------------
# Convert to a string with join()
# -----------------------------------------------------------------------------

key_string = ', '.join(location.keys())
print(key_string)

value_string = ', '.join(location.values())
print(value_string)

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
    print('It has been given a default value of 0')
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
