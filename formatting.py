'''Formatting'''

# Interpolate data values into strings (put values into strings using various
# formats). There are two ways of formatting strings: old style and new style.

# Old style with % (string % data) % followed by a letter indicates the type
# of data.

test = 42
print('%s' % test) # string
print('%d' % test) # decimal integer
print('%x' % test) # hex integer
print('%o' % test) # octal integer
print('%f' % test) # decimal float
print('%e' % test) # exponential float
print('%g' % test) # decimal or exponential float
print('%d%%' % test) # a literal %

# The %s inside a string means to interpolate the string. The number of
# appearances of %s in the string needs to match the number of data items
# after %. If more than one data variable, group like (a, b)

goldenratio = 1.61803398875
name = 'golden ratio'

print('The %s is %f' % (name, goldenratio))

# NOTE: Old style formatting has been marked as deprecated for Python 3

# NEW style formatting with {} and format()

print('The {0} is {1}'.format(name, goldenratio))

# You can specify dict values like this:

info = {'name': 'boktoktok', 'address': 'the moon', 'age': 100}
other = 'the end'

print('{0[name]} who is {0[age]} years old, lives at {0[address]}. {1}.'.format(info, other))

# The number {0} or {1} or whatever, indicates the variable to use according to
# their order in the .format() arguments

# As a side note, remember you can also use keyword arguments **name to extract
# the keys and values from the dictionary and feed into a thing:

statement = '{name} who is {age} years old, lives at {address}'
print(statement.format(**info))

# to specify the type of data as with %d or %f in old style, use {0:d} like:

print('The {0:s} is {1:f}'.format(name, goldenratio))

# adding .number limits the number of characters:

print('The {0:.2s} is {1:.2f}'.format(name, goldenratio))
print('The {0:.10s} is {1:.10f}'.format(name, goldenratio))

# adding a number without the dot says use at least this many spaces:

print('The {0:20} is {1:20}'.format(name, goldenratio))

# Alignment can be specified with <>^ (left, right, centered):

print('{0:^40}'.format(name)) # centres within 40 spaces

# Fill spaces with characters:

print('{0:-^40}'.format(name)) # centres within 40 spaces

# Conclusion:

for i in range(1, 13):
    for j in range(1, 13):
        print(i, 'times',  j, 'is', i*j)
        # will print the same as:
        print('{0} times {1} is {2}'.format(i, j, i*j))

# In the above examples where numbers are used, you can always replace these as
# variables. This makes for more wordy code, but if something needs to be
# configurable, this would be the way to go as the variable could be defined
# elsewhere:

def heading(arg):
    print('{0:-^80}'.format(str(arg).title()))

width = 80

def heading(arg):
    print('{0:-^{1}}'.format(str(arg).title(), width))

heading('Fomatting is fun')
