'''zip() Built-in Function'''


# Iterating over multiple sequences
# -----------------------------------------------------------------------------
# the zip() function wraps two or more iterators in a lazy generator.
# It yields a tuple containing the next value from each iterator.

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
fruits = ['Apple', 'Banana', 'Pear']
drinks = ['Tea', 'Juice', 'Wine']
desserts = ['Ice cream', 'Cookies', 'Cake', 'Candy']

for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day.upper())
    print(f'– {fruit}, {drink}, {dessert}')

# MONDAY
# – Apple, Tea, Ice cream
# TUESDAY
# – Banana, Juice, Cookies
# WEDNESDAY
# – Pear, Wine, Cake

# When using zip in this manner, it will stop iterating when it reaches the
# end of the shortest list. If you want it to exhaust the longest list, use
# zip_longest() from itertools:

from itertools import zip_longest

for day, fruit, drink, dessert in zip_longest(days, fruits, drinks, desserts):
    print(day.upper())
    print(f'– {fruit}, {drink}, {dessert}')

# MONDAY
# – Apple, Tea, Ice cream
# TUESDAY
# – Banana, Juice, Cookies
# WEDNESDAY
# – Pear, Wine, Cake
# THURSDAY
# – None, None, Candy
# FRIDAY
# – None, None, None


# create a dictionary from two sequences
# -----------------------------------------------------------------------------

english = ['Monday', 'Tuesday', 'Wednesday', 'Thursday']
french = ['Lundi', 'Mardi', 'Mecredi']

e2f = dict(zip(english, french))
f2e = dict(zip(french, english))

print(e2f['Tuesday'])  # Mardi
print(f2e['Mardi'])    # Tuesday

# as above, zip will stop creating key/value pairs at the end of the shortest
# list. In the example above, no key will be created for Thursday.


# Another example
# -----------------------------------------------------------------------------

colours = ['Red', 'Cyan', 'Magenta', 'Orange']
hexadecimal = ['FA200C', '0CD3FA', 'FF0D91', 'FF690D']

colour_values = dict(zip(colours, hexadecimal))

print(colour_values)
# {'Red': 'FA200C', 'Cyan': '0CD3FA', 'Magenta': 'FF0D91', 'Orange': 'FF690D'}

# NOTE that zip() behaves differently in Python 2. In version 2 it is not a
# generator and can therefor use a lot of memory. In Python 2 use itertools
# instead.
