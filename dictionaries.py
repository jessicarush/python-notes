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

# get an item by [key]

print(location['street'])
print(location.get('street'))
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
