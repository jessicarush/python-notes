# Working with Lists

# There are several ways to make a list.

# Standard way to create a list

weekdays = [
    'Sunday',
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    ]
print(weekdays)

# Use the list() function, then add items with .append()

months = list()
months.append('Jan')
months.append('Feb')
print(months)

# Convert a tuple into a list using the list() function

a_tuple  = ('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul')
a_list = list(a_tuple)
print(a_list)

# Use .split() to break up a string into a list via some separator like space or comma

a_string = "11-7-24-19-74"
a_list = a_string.split('-')
print(a_list)

# Get an item by [position]

print(a_list[2])

# Lists inside lists

dates = [months, weekdays, 'another']
print(dates)
print(dates[0])
print(dates[0][1])

# Change a list item

dates[0] = a_list
print(dates)

# Get a slice or range [

print(weekdays[::2])
print(weekdays[::-2])
print(weekdays[::-1])

# Add a list item

months.append('apr')
print(months)

# Add a list item by position

months.insert(2, 'mar')
print(months)

# Combine lists

list1 = ['one', 'two']
list2 = ['three', 'four']
list1.extend(list2)
print(list1)

# or combine like this:
list2 += list1
print(list2)

# delete an item by position:
del list1[3]
print(list1)

# remove an item by value:
list2.remove('four')
print("List2 : ", list2)

# get an item by position and delete with pop()
list2.pop(0)
print("List2 : ", list2)

# find and items position by value with index()
print(list2.index('three'))

# test for value in list
print('four' in list2)

# count occurences of a value
print(list2.count('one'))
print(list2.count('five'))

# convert to a string with join and split again:
friends = ['Harry', 'Ron', 'Hermione']
separator = ' * '
joined = separator.join(friends)
print(joined)
separated = joined.split(separator)
print(separated)

# reorder items with sort() or sorted()
# sort() sorts the list in place, sorted() returns a copy
sorted_friends = sorted(friends)
print('sorted friends: ', sorted_friends)
print('friends: ', friends)
friends.sort()
print('sort friends: ', friends)

numbers = [1, 2.5, 6, 3.2]
numbers.sort(reverse = True)
print(numbers)

# get length by len()
print(len(friends))

# create a copy with copy(), list() or slice[:]
a = [1, 2, 3]
b = a
c = a.copy()
d = list(a)
e = a[:]

print(a, '\n', b, '\n', c, '\n', d, '\n', e)

a[0] = 'haha'

print(a, '\n', b, '\n', c, '\n', d, '\n', e)
