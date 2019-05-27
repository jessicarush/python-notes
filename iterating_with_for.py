'''Iterating with for'''


# Iterating over lists, tuples and sets returns individual items:
# -----------------------------------------------------------------------------

list1 = ['one', 'two', 'three']
tuple1 = ('four', 'five', 'six')
set1 = {'seven', 'eight', 'nine'}

for item in list1:
    print(item)
# one
# two
# three

for item in tuple1:
    print(item)
# four
# five
# six

for item in set1:
    print(item)
# eight
# nine
# seven

# You cab also iterate over a slice.
for item in list1[2:]:
    print(item)
# three


# Iterating over strings returns characters
# -----------------------------------------------------------------------------

string1 = "ten"

for char in string1:
    print(char)
# t
# e
# n


# Iterating over dictionaries
# -----------------------------------------------------------------------------

dict1 = {'eleven': '11', 'twelve': '12', 'thirteen': '13'}

for item in dict1:  # will choose keys
    print(item)
# eleven
# twelve
# thirteen

for item in dict1.keys():  # works the same as above
    print(item)
# eleven
# twelve
# thirteen

# Therefor, to iterate over a dictionary and get values:
for item in dict1.values():
    print(item)
# 11
# 12
# 13

# To iterate over both keys and values:
for item in dict1.items():
    print(item)
# ('eleven', '11')
# ('twelve', '12')
# ('thirteen', '13')

# Break apart the resulting tuple by doing this:
for key, value in dict1.items():
    print(key, '–', value)
# eleven – 11
# twelve – 12
# thirteen – 13


# Iterating over multiple sequences with zip()
# -----------------------------------------------------------------------------

days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['Apple', 'Banana', 'Pear']
drinks = ['Tea', 'Juice', 'Wine']
desserts = ['Ice cream', 'Cookies', 'Cake', 'Candy']

for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day.upper())
    print('–', fruit)
    print('–', drink)
    print('–', dessert)


# Using range(start, stop, step)
# -----------------------------------------------------------------------------

for x in range(5, -1, -1):
    print(x, end='...')  # 5...4...3...2...1...0..


# using multiple for loops
# -----------------------------------------------------------------------------

for i in range(1, 13):
    for j in range(1, 13):
        print(i, 'x',  j, '=', i * j)
    print('------------------')


# break and continue
# -----------------------------------------------------------------------------
# break is useful when you want to terminate a loop early if some condition
# is met. Continue skips past to the next iteration.

cheeses = ['brie', 'cheddar', 'feta', 'gorgonzola']

for cheese in cheeses:
    if cheese == 'feta':
        break
    print('We have', cheese)

# We have brie
# We have cheddar

for cheese in cheeses:
    if cheese == 'feta':
        continue
    print('We have', cheese)

# We have brie
# We have cheddar
# We have gorgonzola


# Create your own iterator with iter() and next()
# -----------------------------------------------------------------------------
# A for loop actually creates an iterator object that will return each
# item that it's iterating over. When there are no more items, the iterator
# returns an error. The for loop is built to handle the error and terminates.

string = '123'
my_iterator = iter(string)
print(my_iterator)        # <str_iterator object at 0x101ced470>
print(next(my_iterator))  # 1
print(next(my_iterator))  # 2
print(next(my_iterator))  # 3

# To confirm, the following two are the same thing, we don't need to explicitly
# add the iter() as the for loop will do it for us:

for char in string:
    print(char, end='...')  # 1...2...3...

for char in iter(string):
    print(char, end='...')  # 1...2...3...


# Important Note:
# -----------------------------------------------------------------------------
# A for loop is effective for iterating through a list but apparently, "You
# shouldn't modify a list inside a for loop because Python will have trouble
# keeping track of the items in the list. To modify a list as you work through
# it, use a while loop." Using a while loop allows you to better collect,
# store and organize.
