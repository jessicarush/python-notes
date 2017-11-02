'''Sets'''

# -----------------------------------------------------------------------------
# Set methods
# -----------------------------------------------------------------------------

dir(set)
#  [...,  'add', 'clear', 'copy', 'difference', 'difference_update', 'discard',
#  'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset',
#  'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update',
#  'union', 'update']

# -----------------------------------------------------------------------------
# Sets:
# -----------------------------------------------------------------------------

#  - a set is like a dictionary but without the values
#  - like a dictionary, sets are unordered
#  - like a dictionary, each key must be unique
#  - sets are mutable (except frozen sets - see below)

# create a set with {}:

colours = {'red', 'orange', 'yellow', 'green'}
print(type(colours))

# create an empty set with set() - using {} would make a dictionary:

empty_set = set()

# obviously you can also convert iterable data to a set with set():

from_string = set('letters')
from_list = set(['one', 'two', 'three'])
from_tuple = set(('four', 'five', 'six'))
from_dict = set({'apple' : 'red', 'pear' : 'green', 'banana' : 'yellow'})
from_range = set(range(1, 5))

print(from_string)
print(from_list)
print(from_tuple)
print(from_dict)
print(from_range)

# add to a set with .add():

colours.add('cyan')

# remove from a set with .remove():
# .remove will raise an error if it does not find the item

colours.remove('cyan')

# remove from a set with .discard():
# .discard will NOT raise an error if it does not find the item

colours.discard('cyan')

# use one or the other depending on whether you want to know if the item was
# missing in the first place:

try:
    colours.remove('cyan')
except KeyError:
    print("the item is not there to remove")

# sort a set with sorted():

print(sorted(colours))

# create a copy of a set with .copy():

new_colours = colours.copy()

# sets can be used in place of values in dictionaries:

drinks = {
    'martini' : {'vodka', 'vermouth'},
    'black russian' : {'vodka', 'kahlua'},
    'white russian' : {'cream', 'kahlua', 'vodka'},
    'manhattan' : {'rye', 'vermouth', 'bitters'},
    'screwdriver' : {'orange juice', 'vodka'},
}

# -----------------------------------------------------------------------------
# check for a value with if, in, and, not, or, & {}
# -----------------------------------------------------------------------------

def test1():
    for key, values in drinks.items():
        if 'vodka' in values:
            print('test 1: ', key)
test1()

# the first two words after for are linked to the key and value in the
# dictionary since we're saying 'in drinks.items()':

def test2():
    for name, ingredients in drinks.items():
        if 'kahlua' in ingredients:
            print('test 2: ', name)
test2()

# get more specific with if, in and not

def test3():
    for name, ingredients in drinks.items():
        if 'vodka' in ingredients and not 'vermouth' in ingredients:
            print('test 3: ', name)
test3()

# get even more specific with if, in, and, not, or

def test4():
    for name, ingredients in drinks.items():
        if 'vodka' in ingredients and not (
        'vermouth' in ingredients or 'cream' in ingredients):
            print('test 4: ', name)
test4()

# check for this OR that values with & {} ...this is called a set operator:

def test5():
    for name, ingredients in drinks.items():
        # has vermouth or orange juice
        if ingredients & {'vermouth', 'orange juice'}:
            print('test 5: ', name)
test5()

# this is same as test 4 but using & {}:
def test6():
    for name, ingredients in drinks.items():
        if 'vodka' in ingredients and not ingredients & {'vermouth', 'cream'}:
            print('test 6: ', name)
test6()

# -----------------------------------------------------------------------------
# More set operators
# -----------------------------------------------------------------------------

bruss = drinks['black russian']
wruss = drinks['white russian']
print(type(bruss)) # it's a set

# test for intersection (items common to both sets):

a = {1, 2}
b = {2, 3}

print(a & b)
print(a.intersection(b))

print(bruss & wruss)
print(bruss.intersection(wruss))

# test for union (items in either set):

print(a | b)
print(a.union(b))

print(bruss | wruss)
print(bruss.union(wruss))

# test for difference (items in the first set but not the second):

print(a - b)
print(a.difference(b))

print(bruss - wruss)
print(wruss.difference(bruss))

# test for exclusive items (items in the one set or the other not both:

print(a ^ b)
print(a.symmetric_difference(b))

print(bruss ^ wruss)
print(bruss.symmetric_difference(wruss))

# for all of these (union, intersection, difference, symmetric_difference),
# you can update the set to the result using update() or _update():

a.intersection_update(b)
a.update(b) # union
a.difference_update(b)
a.symmetric_difference_update(b)

# test if one set is a subset of another (all items in first set
# are also in the second):

print(a <= b)
print(a.issubset(b))

print(bruss <= wruss)
print(bruss.issubset(wruss))

# test if one set is a subset of another(all items in second set
# are also in the first):

print(a >= b)
print(a.issuperset(b))

print(bruss >= wruss)
print(bruss.issuperset(wruss))

# -----------------------------------------------------------------------------
# Frozen Sets
# -----------------------------------------------------------------------------
#  - frozen sets are immutable
#  - as a result, can be used as dictionary keys
#  - can be used as items in other sets
#  - frozenset() takes 1 argument so if not using a variable, enclose with ()
#  - while you can't add or remove items from a frozen set, you can still use
#    them to calculate unions, differnces etc.

beer = frozenset(('IPA', 'Pale Ale', 'Stout', 'Pilsner', 'Wheat'))
print(type(beer))
print(beer)
