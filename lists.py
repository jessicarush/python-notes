'''Lists'''

# List methods ----------------------------------------------------------------

dir(list)
#  [..., 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert',
#  'pop', 'remove', 'reverse', 'sort']

# -----------------------------------------------------------------------------

# Lists are mutable and ordered. They may contain duplicate items and can be
# changed in place. There are several ways to make a list:

weekdays = [
    'Sunday',
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    ]

# Create a blank list, then add items with .append()

months = []
months.append('Jan')
months.append('Feb')

# Convert a tuple, dict, set or ... into a list using the list() function

a_dict = {'a' : 'A', 'b': 'B', 'c': 'C'}
a_tuple  = ('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul')
a_list = list(a_tuple)  # ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul']
a_list = list(a_dict)   # ['a', 'b', 'c']

# as above, you can also use the list function to start with an empty list

a_list = list()
a_list.append('item')

# Use .split() to break up a string into a list using a separator (delimiter)
# like a space or comma:

a_string = "11-7-24-19-74"
a_list = a_string.split('-')  # ['11', '7', '24', '19', '74']

# Accessing list values -------------------------------------------------------

# Get an item by [position]

print(a_list[2])  # 24

# Lists inside lists

dates = [months, weekdays, 'another']
print(dates)
print(dates[0])     # ['Jan', 'Feb']
print(dates[0][1])  # Feb

# Change a list item

dates[0] = a_list

# Get a slice or range [start : end : step]

print(weekdays[::2])   # ['Sunday', 'Tuesday', 'Thursday', 'Saturday']
print(weekdays[::-2])  # ['Saturday', 'Thursday', 'Tuesday', 'Sunday']
print(weekdays[::-1])  # ['Saturday', 'Friday', 'Thursday', 'Wednesday',
                       #  'Tuesday', 'Monday', 'Sunday']

# .append() -------------------------------------------------------------------

# Add a list item with .append()

months.append('apr')

# .insert() -------------------------------------------------------------------

# Add/insert a list item by position with .insert()

months.insert(2, 'mar')

# .extend() -------------------------------------------------------------------

# Combine lists with .extend() - this would be like .update() for dicts

list1 = ['one', 'two']
list2 = ['three', 'four']
list1.extend(list2)
print(list1)  # ['one', 'two', 'three', 'four']

# Or combine like this:

list2 += list1

# To confirm:

list3 = [list1, list2]  # creates a list of two lists

list3 = [list1 + list2] # creates a list of one list

list3 = list1 + list2   # creates one list

# .remove() -------------------------------------------------------------------

# Remove an item by value with .remove(). Note this will only remove the first
# occurrence of the value in the list. Use a loop to delete more than one.

list2.remove('four')

while 'four' in list2:
    list2.remove('four')

# del -------------------------------------------------------------------------

# Delete an item by position with del

del list1[3]

# Delete all items using a slice:

del list1[:]
print(list1)  # []

# .clear() --------------------------------------------------------------------

# In Python 3.3 and higher you can also use clear() to delete all items:

list2.clear()
print(list2)  # []

# .pop() ----------------------------------------------------------------------

# The .pop() method also deletes an item from a list but also lets you work
# with that item after removing it. This is helpful for when you want to move
# an item from place to another.

print("List3: ", list3)         # List3: ['one', 'two', 'three', 'four'...]
popped_item = list3.pop(0)
print("List3: ", list3)         # List3: ['two', 'three', 'four'...]
print('popped: ', popped_item)  # popped item:  one

# see while_loops.py for another example using.pop()

# .index() --------------------------------------------------------------------

# Find the the index position of a value with .index()

print(list3.index('two'))  # 0

# Test for a value in a list

print('four' in list3)  # True

# Test for a value NOT in a list

print('four' not in list3)  # False

# .count() --------------------------------------------------------------------

# Count the occurrences of a value with .count()

print(list3.count('one'))   # 1
print(list3.count('four'))  # 3

# .join() ---------------------------------------------------------------------

# Convert a list to a string with .join()

bands = ['Melvins', 'Ghost', 'Pucifer']
joined_string= ' * '.join(bands)
print(joined_string)  # Melvins * Ghost * Pucifer

# FYI you could also create a string from a list like the following, but this
# is considered not efficient because every time through the for loop, a copy
# of new_string is created and uses up more computer memory:

new_string = ''
for item in bands:
    new_string += item
print(new_string)  # MelvinsGhostPucifer

# .split() --------------------------------------------------------------------

# Convert a string to a list with .split()

split_list = joined_string.split(' * ')
print(split_list)  # ['Melvins', 'Ghost', 'Pucifer']

# sorted() --------------------------------------------------------------------

# Temporarily reorder items with sorted() - this does not change the
# original list, but returns a sorted copy:

print(bands)                 # ['Melvins', 'Ghost', 'Pucifer']
print(sorted(bands))         # ['Ghost', 'Melvins', 'Pucifer']
print(bands)                 # ['Melvins', 'Ghost', 'Pucifer']
sorted_bands = sorted(bands)
print(sorted_bands)          # ['Ghost', 'Melvins', 'Pucifer']

# .sort() ---------------------------------------------------------------------

# Permanently reorder items with .sort() - this sorts the list in place

bands.sort()
print(bands)                 # ['Ghost', 'Melvins', 'Pucifer']

numbers = [1, 2.5, 6, 3.2]
numbers.sort(reverse = True)
print(numbers)  # [6, 3.2, 2.5, 1]

# .reverse() ------------------------------------------------------------------

# Permanently reverse the order of any list with the .reverse method:

numbers.reverse()
print(numbers)  # [1, 2.5, 3.2, 6]

# .len() ----------------------------------------------------------------------

# Get length by len()

print(len(bands))  # 3

# .copy() ---------------------------------------------------------------------

# Create a copy with copy(), list() or slice[:]

a = [1, 2, 3]  # original list
b = a          # not a copy
c = a.copy()
d = list(a)
e = a[:]

a[0] = 'changed'

print(a, '\n', b, '\n', c, '\n', d, '\n', e)
# ['changed', 2, 3]
# ['changed', 2, 3]
# [1, 2, 3]
# [1, 2, 3]
# [1, 2, 3]

# min(), max(), sum() ---------------------------------------------------------

# A few functions are specific to lists of numbers:

print(min(numbers))  # 1
print(max(numbers))  # 6
print(sum(numbers))  # 12.7

# List comprehensions ---------------------------------------------------------

# see comprehensions.py
