'''Lists'''


# List methods
# -----------------------------------------------------------------------------

print(dir(list))
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__',
# '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__',
# '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__',
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
# '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__',
# '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend',
# 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


# Lists are mutable and ordered
# -----------------------------------------------------------------------------
# They may contain duplicate items and can be changed in place.
# There are several ways to make a list:

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
a_tuple = ('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul')
a_list = list(a_tuple)  # ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul']
a_list = list(a_dict)   # ['a', 'b', 'c']

# as above, you can also use the list function to start with an empty list

a_list = list()
a_list.append('item')

# Use .split() to break up a string into a list using a separator (delimiter)
# like a space or comma:

a_string = "11-7-24-19-74"
a_list = a_string.split('-')  # ['11', '7', '24', '19', '74']


# Accessing list values by index
# -----------------------------------------------------------------------------
# Get an item by [position]
print(a_list)     # ['11', '7', '24', '19', '74']
print(a_list[2])  # 24

# Lists inside lists

many_lists = [months, weekdays, 'another']
print(many_lists)
print(many_lists[0])     # ['Jan', 'Feb']
print(many_lists[0][1])  # Feb

# Change a list item

many_lists[0] = a_list


# Slice a list [start : end : step]
# -----------------------------------------------------------------------------
# You can access a slice of a list. Note this does not change the list.

print(weekdays[1::2])    # ['Monday', 'Wednesday', 'Friday']
print(weekdays[-1::-6])  # ['Saturday', 'Sunday']

# When assigning to a sliced list, the result is a new list:

weekend = weekdays[-1::-6]
print(weekend)  # ['Saturday', 'Sunday']

# When you reassign a slice, the number of items don't need to match:

test = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
test[1:7] = ['x', 'y']
print(test)  # ['a', 'x', 'y', 'h', 'i']


# .append()
# -----------------------------------------------------------------------------
# Add a list item with .append()

print(months)  # ['Jan', 'Feb']
months.append('Apr')
print(months)  # ['Jan', 'Feb', 'Apr']


# .insert()
# -----------------------------------------------------------------------------
# Add/insert a list item by position with .insert()

months.insert(2, 'Mar')
print(months)  # ['Jan', 'Feb', 'Mar', 'Apr']


# .extend()
# -----------------------------------------------------------------------------
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


# .remove()
# -----------------------------------------------------------------------------
# Remove an item by value with .remove(). Note this will only remove the first
# occurrence of the value in the list. Use a loop to delete more than one.

print(list2)  # ['three', 'four', 'one', 'two', 'three', 'four']
list2.remove('four')
print(list2)  # ['three', 'one', 'two', 'three', 'four']

while 'four' in list2:
    list2.remove('four')

# If you had a list of dictionaries, you could iterate. This works but it
# breaks the rule of "never modify a list in a for loop". I'm not clear as to
# whether this particular example is bad or not:

items = [{'name': 'shoes', 'price': 20.99}, {'name': 'eggs', 'price': 1.99}]

for item in items:
    if item['name'] == 'eggs':
        items.remove(item)


# del
# -----------------------------------------------------------------------------
# Delete an item by position with del

list1 = ['one', 'two', 'three']
del list1[1]
print(list1)  # ['one', 'three']

# Delete all items using a slice:

del list1[:]
print(list1)  # []


# .clear()
# -----------------------------------------------------------------------------
# In Python 3.3 and higher you can also use clear() to delete all items:

list1 = ['one', 'two', 'three']
list1.clear()
print(list1)  # []


# .pop()
# -----------------------------------------------------------------------------
# The .pop() method also deletes an item from a list but also lets you work
# with that item after removing it. This is helpful for when you want to move
# an item from place to another.

list1 = ['one', 'two', 'three', 'four']
popped_first = list1.pop(0)
popped_last = list1.pop(-1)
print(list1)         # ['two', 'three']
print(popped_first)  # one
print(popped_last)   # four

# see while_loops.py for another example using.pop()


# .index()
# -----------------------------------------------------------------------------
# Find the the index position of a value with .index()
# Note that if the value isn't in the list, an exception will be raised.

list1 = ['one', 'two', 'three', 'four']
print(list1.index('two'))  # 1


# Check if a value is in a list
# -----------------------------------------------------------------------------

list1 = ['one', 'two', 'three', 'four']
print('four' in list1)      # True
print('four' not in list1)  # False


# .count()
# -----------------------------------------------------------------------------
# Count the occurrences of a value with .count()

list1 = ['one', 'two', 'three', 'four', 'four', 'four']
print(list3.count('one'))   # 1
print(list3.count('four'))  # 3


# .join()
# -----------------------------------------------------------------------------
# Convert a list to a string with .join()

bands = ['Melvins', 'Ghost', 'Pucifer']
joined_string = ' * '.join(bands)
print(joined_string)  # Melvins * Ghost * Pucifer

# FYI you could also create a string from a list like the following, but this
# is considered not efficient because every time through the for loop, a copy
# of new_string is created and uses up more computer memory:

new_string = ''
for item in bands:
    new_string += item
print(new_string)  # MelvinsGhostPucifer


# .split()
# -----------------------------------------------------------------------------
# Convert a string to a list with .split()

split_list = joined_string.split(' * ')
print(split_list)  # ['Melvins', 'Ghost', 'Pucifer']


# sorted()
# -----------------------------------------------------------------------------
# Temporarily reorder items with sorted() - this does not change the
# original list, but returns a sorted copy:

print(bands)                 # ['Melvins', 'Ghost', 'Pucifer']
print(sorted(bands))         # ['Ghost', 'Melvins', 'Pucifer']
print(bands)                 # ['Melvins', 'Ghost', 'Pucifer']
sorted_bands = sorted(bands)
print(sorted_bands)          # ['Ghost', 'Melvins', 'Pucifer']


# .sort()
# -----------------------------------------------------------------------------
# Permanently reorder items with .sort() - this sorts the list in place

bands.sort()
print(bands)                 # ['Ghost', 'Melvins', 'Pucifer']

numbers = [1, 2.5, 6, 3.2]
numbers.sort(reverse=True)
print(numbers)  # [6, 3.2, 2.5, 1]


# .reverse()
# -----------------------------------------------------------------------------
# Permanently reverse the order of any list with the .reverse method:

numbers.reverse()
print(numbers)  # [1, 2.5, 3.2, 6]


# len()
# -----------------------------------------------------------------------------
# Get length by len()

print(len(bands))  # 3


# .copy()
# -----------------------------------------------------------------------------
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


# min(), max(), sum()
# -----------------------------------------------------------------------------
# A few functions are specific to lists of numbers:

print(min(numbers))  # 1
print(max(numbers))  # 6
print(sum(numbers))  # 12.7


# List comprehensions
# -----------------------------------------------------------------------------
# see comprehensions.py
