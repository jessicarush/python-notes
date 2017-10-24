'''Iterating with for'''

# Iterating over lists, tuples and sets returns items.
list1 = ['one' , 'two', 'three']
tuple1 = ('four', 'five', 'six')
set1 = {'seven', 'eight', 'nine'}

for item in list1:
    print(item)

for item in tuple1:
    print(item)

for item in set1:
    print(item)

# Iterate over a slice.
for item in list1[:1]:
    print(item)

# Iterating over strings returns characters.
string1 = "ten"

for char in string1:
    print(char)

# Iterating over dictionaries returns keys.
dict1 = {'eleven' : '11', 'twelve': '12', 'thirteen': '13'}

for item in dict1: # will choose keys
    print(item)

# same as:
for item in dict1.keys():
    print(item)

# Therefor, to iterate over a dictionary and get values:
for item in dict1.values():
    print(item)

# To iterate over both keys and values:
for item in dict1.items():
    print(item)

# Break apart the resulting tuple by doing this:
for key, value in dict1.items():
    print(key, 'is', value)

# Iterating over multiple sequences with zip() --------------------------------

days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['Apple', 'Banana', 'Pear']
drinks = ['Tea', 'Juice', 'Wine']
desserts = ['Ice cream', 'Cookies', 'Cake', 'Candy']

for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ': eat', fruit, ', drink', drink, ', cheat with', dessert)

# for using range(start, stop, step) ------------------------------------------

for x in range(5, -1, -1):
    print(x, end='...')

evens = list(range(0, 20, 2))
print(evens)

# using multiple for loops ----------------------------------------------------

for i in range(1, 13):
    for j in range(1, 13):
        print(i, 'times',  j, 'is', i*j)
    print('------------------')

# break and continue ----------------------------------------------------------

cheeses = []
for cheese in cheeses:
    print('This shop has', cheese)
    break
else:
    print('no cheese')

# break is useful when you want to terminate a loop early if some condition
# is met, and continue skips past to the next iteration

colours = ['red', 'orange', 'yellow', 'purple', 'white', 'cyan']

for colour in colours:
    if colour == 'white':
        continue
    print('I like ' + colour)

for colour in colours:
    if colour == 'yellow':
        break
    print('I like ' + colour)

# NOTE: a for loop actually creates an iterator object that will return each
# item that it's iterating over. When there are no more items, the iterator
# returns an error and the for loop handles the error and terminates

# Create your own iterator with iter() and next() -----------------------------

string = '12345'
my_iterator = iter(string)
print(my_iterator) # str_iterator object
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

# to confirm, the following two are the same thing, we don't need to explicitly
# add the iter() as the for loop will do it for us:

for char in string:
    print(char)

for char in iter(string):
    print(char)

# Again, the long version:

my_list = [1, 2, 3, 4, 5]
my_iterator = iter(my_list)

for i in range(0, len(my_list)):
    print(next(my_iterator))

# The same as:

for i in my_list:
    print(i)

# Note ------------------------------------------------------------------------

# A for loop is effective for iterating through a list but apparently, "You
# shouldn't modify a list inside a for loop because Python will have trouble
# keeping track of the items in the list. To modify a list as you work through
# it, use a while loop." Using a while loop allows you to better collect,
# store and organize.
