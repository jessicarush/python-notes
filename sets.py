'''Sets'''


# Set methods
# -----------------------------------------------------------------------------

print(dir(set))
# ['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__',
# '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',
# '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__',
# '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__',
# '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__',
# '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__',
# '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference',
# 'difference_update', 'discard', 'intersection', 'intersection_update',
# 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove',
# 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']


# Create a set with set() or {}
# -----------------------------------------------------------------------------
#  - a set is like a dictionary but without the values
#  - like a dictionary, sets are unordered
#  - like a dictionary, each key must be unique
#  - sets are mutable (except frozen sets - see below)

# create a set with {}:

colours = {'red', 'orange', 'yellow', 'green'}
print(type(colours))  # <class 'set'>

# create an empty set with set() - using {} would make a dictionary:

empty_set = set()

# obviously you can also convert iterable data to a set with set():

from_string = set('letters')
from_list = set(['one', 'two', 'three', 'one'])
from_tuple = set(('four', 'five', 'six'))
from_dict = set({'apple' : 'red', 'pear' : 'green', 'banana' : 'yellow'})
from_dict_vals = set({'apple' : 'red', 'pear' : 'green', 'banana' : 'yellow'}.values())
from_range = set(range(1, 5))

print(from_string)     # {'l', 't', 's', 'e', 'r'}
print(from_list)       # {'one', 'three', 'two'}
print(from_tuple)      # {'four', 'five', 'six'}
print(from_dict)       # {'apple', 'banana', 'pear'}
print(from_dict_vals)  # {'red', 'green', 'yellow'}
print(from_range)      # {1, 2, 3, 4}


# unpack a set
# -----------------------------------------------------------------------------
# You can unpack any sequence (including lists) into variables. The only
# requirement is that the number of variables should match the number of items
# in the sequence:

data = {'orange', 'small', (1, 1, 2020), '2.99'}
color, size, (month, day, year), price = data

print(month)  # 1
print(year)   # 2020


# add()
# -----------------------------------------------------------------------------
# add to a set with .add():

colours.add('cyan')


# pop()
# -----------------------------------------------------------------------------

popped = colours.pop()
print(popped)  # will be different every time


# remove(), discard()
# -----------------------------------------------------------------------------
# remove from a set with .remove():
# .remove will raise an error if it does not find the item

colours.add('cyan')
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


# sort a set with sorted()
# -----------------------------------------------------------------------------

print(sorted(colours))
# ['green', 'orange', 'red', 'yellow']


# create a copy of a set with .copy():
# -----------------------------------------------------------------------------

new_colours = colours.copy()


# clear()
# -----------------------------------------------------------------------------
new_colours.clear()
print(new_colours)  # set()


# sets can be used as values in dictionaries:
# -----------------------------------------------------------------------------

drinks = {'martini' : {'vodka', 'vermouth'},
          'black russian' : {'vodka', 'kahlua'},
          'white russian' : {'cream', 'kahlua', 'vodka'},
          'manhattan' : {'rye', 'vermouth', 'bitters'},
          'screwdriver' : {'orange juice', 'vodka'},
          }


# check for values with in, and, not, or, & {}
# -----------------------------------------------------------------------------

def test1():
    for key, values in drinks.items():
        if 'vodka' in values:
            print('test 1: ', key)
test1()
# test 1:  martini
# test 1:  black russian
# test 1:  white russian
# test 1:  screwdriver

# the first two words after for are linked to the key and value in the
# dictionary since we're saying 'in drinks.items()':

def test2():
    for name, ingredients in drinks.items():
        if 'kahlua' in ingredients:
            print('test 2: ', name)
test2()
# test 2:  black russian
# test 2:  white russian

# get more specific with if, in and not

def test3():
    for name, ingredients in drinks.items():
        if 'vodka' in ingredients and not 'vermouth' in ingredients:
            print('test 3: ', name)
test3()
# test 3:  black russian
# test 3:  white russian
# test 3:  screwdriver

# get even more specific with if, in, and, not, or

def test4():
    for name, ingredients in drinks.items():
        if 'vodka' in ingredients and not (
        'vermouth' in ingredients or 'cream' in ingredients):
            print('test 4: ', name)
test4()
# test 4:  black russian
# test 4:  screwdriver

# check for this OR that values with & {} ...this is called a set operator:

def test5():
    for name, ingredients in drinks.items():
        # if has vermouth or orange juice:
        if ingredients & {'vermouth', 'orange juice'}:
            print('test 5: ', name)
test5()
# test 5:  martini
# test 5:  manhattan
# test 5:  screwdriver

# this is same as test 4 but using & {}:
def test6():
    for name, ingredients in drinks.items():
        if 'vodka' in ingredients and not ingredients & {'vermouth', 'cream'}:
            print('test 6: ', name)
test6()
# test 6:  black russian
# test 6:  screwdriver


# Set operators
# -----------------------------------------------------------------------------
# These include union(), intersection(), difference(), symmetric_difference(),
# intersection_update(), difference_update(), symmetric_difference_update(),
# issubset(), issuperset()

bruss = drinks['black russian']
wruss = drinks['white russian']

a = {1, 2}
b = {2, 3}

# test for intersection (items common to both sets):

print(a & b)                              # {2}
print(a.intersection(b))                  # {2}

print(bruss & wruss)                      # {'kahlua', 'vodka'}
print(bruss.intersection(wruss))          # {'kahlua', 'vodka'}

# test for union (items in either set):

print(a | b)                              # {1, 2, 3}
print(a.union(b))                         # {1, 2, 3}

print(bruss | wruss)                      # {'kahlua', 'vodka', 'cream'}
print(bruss.union(wruss))                 # {'kahlua', 'vodka', 'cream'}

# test for difference (items in the first set but not the second):

print(a - b)                              # {1}
print(a.difference(b))                    # {1}

print(wruss - bruss)                      # {cream}
print(wruss.difference(bruss))            # {cream}

# test for exclusive items (items in the one set or the other not both:

print(a ^ b)                              # {1, 3}
print(a.symmetric_difference(b))          # {1, 3}

print(bruss ^ wruss)                      # {cream}
print(bruss.symmetric_difference(wruss))  # {cream}

# for all of these (union, intersection, difference, symmetric_difference),
# you can update the set to the result using update() or _update():

a.update(b)  # union
a.intersection_update(b)
a.difference_update(b)
a.symmetric_difference_update(b)

# test if one set is a subset of another
# (all items in first set are also in the second):

print(a <= b)                             # False
print(a.issubset(b))                      # False

print(bruss <= wruss)                     # True
print(bruss.issubset(wruss))              # True

# test if one set is a subset of another
# (all items in second set are also in the first):

print(a >= b)                             # False
print(a.issuperset(b))                    # False

print(bruss >= wruss)                     # False
print(bruss.issuperset(wruss))            # False


# So the methods on sets clearly suggest that sets are meant to operate on
# other sets, and that they are not just containers. If we have data coming in
# from two different sources and need to quickly combine them in some way, to
# determine where the data overlaps or is different, we can use set operations
# to efficiently compare them. Or if we have data incoming that may contain
# duplicates of data that has already been processed, we can use sets to
# compare the two and process only the new data.

# Finally, it is valuable to know that sets are much more efficient than lists
# when checking for membership using the 'in' keyword. If you use the syntax
# value in container on a set or a list, it will return True if one of the
# elements in container is equal to value and False otherwise. However, in a
# list, it will look at every object in the container until it finds the value,
# whereas in a set, it simply hashes the value and checks for membership. This
# means that a set will find the value in the same amount of time no matter how
# big the container is, but a list will take longer and longer to search for a
# value as the list contains more and more values.


# Frozen Sets
# -----------------------------------------------------------------------------
#  - frozen sets are immutable
#  - as a result, they can be used as dictionary keys
#  - can be used as items in other sets
#  - frozenset() takes 1 argument, so if not using a variable, wrap with ()
#  - frozen sets have fewer methods available to them than regular sets
#  - while you can't add or remove items from a frozen set, you can still use
#    them to calculate unions, differences etc.

print(dir(frozenset))
# ['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__',
# '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',
# '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__',
# '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__',
# '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__',
# '__str__', '__sub__', '__subclasshook__', '__xor__', 'copy', 'difference',
# 'intersection', 'isdisjoint', 'issubset', 'issuperset',
# 'symmetric_difference', 'union']

beer = frozenset(('IPA', 'Ale', 'Stout', 'Pilsner', 'Wheat'))
print(type(beer))  # <class 'frozenset'>
print(beer)        # frozenset({'Ale', 'Wheat', 'IPA', 'Stout', 'Pilsner'})
