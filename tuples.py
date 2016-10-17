# TUPLES

# remember tuples are immutable: you can't add, change or delete items
colours_tuple = ('green', 'blue', 'red')

#tuples let you assign multiple variables at once:
a, b, c = colours_tuple
print(a)
print(b)
print(c)

#you can use tuples to swap variable values in one line:
a, c = c, a
print(a)
print(b)

# the tuple() function lets you convert something to a tuple:
colours_list = ['orange', 'yellow', 'purple']
colours_tuple = tuple(colours_list)
print(colours_tuple)

"""
Benefits of using tuples:
- Tuples use less space
- You can't mess with tuple items by mistake
- You can use tuples and dictionary keys
- Named tuples can be a simple alternative to objects
- Function arguments are passed as tuples
"""
