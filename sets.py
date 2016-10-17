# SETS

"""
Sets:
 - a set is like a dictionary but without the values
 - like a dictionary, each key must be unique
 - use a set when you only want to know that somehting exists
 - use a dict when you want to attach information to each key
"""

# create a set with {}:

even_numbers = {1, 2, 4, 6, 8}
print(type(even_numbers))

# convert to a set with set():

from_string = set('letters')
from_list = set(['one', 'two', 'three'])
from_tuple = set(('four', 'five', 'six'))
from_dict = set({'apple' : 'red', 'pear' : 'green', 'banana' : 'yellow'})

# sets can be used in place of values in dictionaries:

drinks = {
    'martini' : {'vodka', 'vermouth'},
    'black russian' : {'vodka', 'kahlua'},
    'white russian' : {'cream', 'kahlua', 'vodka'},
    'manhattan' : {'rye', 'vermouth', 'bitters'},
    'screwdriver' : {'orange juice', 'vodka'},
}

# check for a value with if, in:

def test():
    for key, values in drinks.items():
        if 'vodka' in values:
            print('test 1: ', key)
test()

# the first two words after for are linked to the key and value in the dictionary
# you can use whatever names you want:

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
        if 'vodka' in ingredients and not ('vermouth' in ingredients or 'cream' in ingredients):
            print('test 4: ', name)
test4()

# check for a set of values with & {} ...this is called a set operator:

def test5():
    for name, ingredients in drinks.items():
        if ingredients & {'vermouth', 'orange juice'}:
            print('test 5: ', name)
test5()

# this is same as test 4 but using & {}:
def test6():
    for name, ingredients in drinks.items():
        if 'vodka' in ingredients and not ingredients & {'vermouth', 'cream'}:
            print('test 6: ', name)
test6()

# More set operators:

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

# test if one set is a subset of another(all items in first set are also in second):

print(a <= b)
print(a.issubset(b))

print(bruss <= wruss)
print(bruss.issubset(wruss))

# test if one set is a subset of another(all items in second set are also in first):

print(a >= b)
print(a.issuperset(b))

print(bruss >= wruss)
print(bruss.issuperset(wruss))
