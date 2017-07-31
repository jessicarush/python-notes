# LISTS are mutable and ordered. May contain duplicate items and can be changed in place.

# There are several ways to make a list

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

# Convert a tuple into a list using the list() function

a_tuple  = ('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul')
a_list = list(a_tuple)

# Use .split() to break up a string into a list via some separator like space or comma

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

# Add a list item by position with .insert()

months.insert(2, 'mar')

# Combine lists with .extend() - this would be like .update() for dicts

list1 = ['one', 'two']
list2 = ['three', 'four']
list1.extend(list2)
print(list1)

# Or combine like this:

list2 += list1
print(list2)

# Delete an item by position with del

del list1[3]

# Remove an item by value with .remove()

list2.remove('four')
print("List2 : ", list2)

# Get an item by position and delete with .pop()

list2.pop(0)
print("List2 : ", list2)

# Find and items position by value with .index()

print(list2.index('three'))

# Test for a value in a list

print('four' in list2)

# Count the occurrences of a value

print(list2.count('one'))
print(list2.count('five'))

# Convert to a string with .join()

bands = ['Melvins', 'Ghost', 'Pucifer']
separator = ' * '
joined = separator.join(bands)
print(joined)

# And split again with .split()

separated = joined.split(separator)
print(separated)

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
