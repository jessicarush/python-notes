# Iterating over multiple sequences with zip()

days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['Apple', 'Banana', 'Pear']
drinks = ['Tea', 'Juice', 'Wine']
desserts = ['Ice cream', 'Cookies', 'Cake', 'Candy']

for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ': eat', fruit, ', drink', drink, ', cheat with', dessert)

# Use zip() to create a dictionary from two sequences

english = ['Monday', 'Tuesday', 'Wednesday']
french = ['Lundi', 'Mardi', 'Mecredi']

e2f = dict(zip(english, french))
f2e = dict(zip(french, english))

print(e2f['Tuesday'])
print(f2e['Mardi'])

# Another example

colours = ['Red', 'Cyan', 'Magenta', 'Orange']
hexadecimal = ['FA200C', '0CD3FA', 'FF0D91', 'FF690D']

colour_values = dict(zip(colours, hexadecimal))

print(colour_values)
