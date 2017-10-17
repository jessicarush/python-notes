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
a_list = list(a_tuple)
print(a_list)
a_list = list(a_dict)
print(a_list)

# as above, you could start with an empty list, then append:

a_list = list()
a_list.append('item')

# Use .split() to break up a string into a list using a separator (delimiter)
# like a space or comma:

a_string = "11-7-24-19-74"
a_list = a_string.split('-')

# Get an item by [position]

print(a_list[2])

# Lists inside lists

dates = [months, weekdays, 'another']
print(dates)
print(dates[0])
print(dates[0][1])

# Change a list item

dates[0] = a_list

# Get a slice or range [start : end : step]

print(weekdays[::2])
print(weekdays[::-2])
print(weekdays[::-1])

# Add a list item with .append()

months.append('apr')

# Add/insert a list item by position with .insert()

months.insert(2, 'mar')

# Combine lists with .extend() - this would be like .update() for dicts

list1 = ['one', 'two']
list2 = ['three', 'four']
list1.extend(list2)
print(list1)

# Or combine like this:

list2 += list1

# To confirm:

list3 = [list1, list2] # creates a list of two lists

list3 = [list1 + list2] # creates a list of one list

# Remove an item by value with .remove()

list2.remove('four')
print("List2 : ", list2)

# Delete an item by position with del

del list1[3]

# Delete all items using a slice:

del list1[:]
print(list1)

# In Python 3.3 and higher you can also use clear() to delete all items:
list1.clear()
print(list1)

# Get an item by position and delete it from the list with .pop()

pulled_item = list2.pop(0)
print("List2 : ", list2)
print(pulled_item)

# Find and items position by value with .index()

print(list2.index('three'))

# Test for a value in a list

print('four' in list2)

# Test for a value NOT in a list

print('four' not in list2)

# Count the occurrences of a value with .count()

print(list2.count('one'))
print(list2.count('five'))

# Convert a list to a string with .join()

bands = ['Melvins', 'Ghost', 'Pucifer']
joined_string= ' * '.join(bands)
print(joined_string)

# NOTE: you could also create a string from a list like the following, but this
# is considered not efficient because every time through the for loop, a copy
# of new_string is created and uses up more computer memory:

new_string = ''
for item in bands:
    new_string += item
print(new_string)

# Convert a string to a list with .split()

split_list = joined_string.split(' * ')
print(split_list)

# Reorder items with sorted() - this returns a copy of the list

sorted_bands = sorted(bands)
print('sorted bands: ', sorted_bands)

# Reorder items with .sort() - this sorts the list in place

bands.sort()
print('sort bands: ', bands)

numbers = [1, 2.5, 6, 3.2]
numbers.sort(reverse = True)
print(numbers)

# Get length by len()

print(len(bands))

# Create a copy with copy(), list() or slice[:]

a = [1, 2, 3]  # original list
b = a          # not a copy
c = a.copy()
d = list(a)
e = a[:]

a[0] = 'changed'

print(a, '\n', b, '\n', c, '\n', d, '\n', e)
