'''zip() Built-in Function'''

# -----------------------------------------------------------------------------
# Iterating over multiple sequences
# -----------------------------------------------------------------------------

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
fruits = ['Apple', 'Banana', 'Pear']
drinks = ['Tea', 'Juice', 'Wine']
desserts = ['Ice cream', 'Cookies', 'Cake', 'Candy']

# When using zip in this manner, it will stop iterating when it reaches the end
# of the shortest list.

for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ': eat', fruit, ', drink', drink, ', cheat with', dessert)

# -----------------------------------------------------------------------------
# create a dictionary from two sequences
# -----------------------------------------------------------------------------

english = ['Monday', 'Tuesday', 'Wednesday', 'Thursday']
french = ['Lundi', 'Mardi', 'Mecredi']

e2f = dict(zip(english, french))
f2e = dict(zip(french, english))

print(e2f['Tuesday'])
print(f2e['Mardi'])

# as above, zip will stop creating key/value pairs at the end of the shortest
# list. In the example above, no key will be created for Thursday.

# -----------------------------------------------------------------------------
# Another example
# -----------------------------------------------------------------------------

colours = ['Red', 'Cyan', 'Magenta', 'Orange']
hexadecimal = ['FA200C', '0CD3FA', 'FF0D91', 'FF690D']

colour_values = dict(zip(colours, hexadecimal))

print(colour_values)
