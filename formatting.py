'''Formatting'''

# Interpolate data values into strings (put values into strings using various
# formats). There are two ways of formatting strings: old style and new style.

# -----------------------------------------------------------------------------
# Old Style formatting - deprecated for Python 3
# -----------------------------------------------------------------------------
# Old style with % (string % data) % followed by a letter indicates the type
# of data.

test = 42
print('%s' % test)    # 42 - string
print('%d' % test)    # 42 - decimal integer
print('%x' % test)    # 2a - hex integer
print('%o' % test)    # 52 - octal integer
print('%f' % test)    # 42.000000 - decimal float
print('%e' % test)    # 4.200000e+01 - exponential float
print('%g' % test)    # 42 - decimal or exponential float
print('%d%%' % test)  # 42% - a literal %

# The %s inside a string means to interpolate the string. The number of
# appearances of %s in the string needs to match the number of data items
# after %. If more than one data variable, group like (a, b)

value = 1.61803398875
name = 'golden ratio'

print('The %s is %f' % (name, value))
# The golden ratio is 1.618034

# -----------------------------------------------------------------------------
# New Style formatting - with {} and format()
# -----------------------------------------------------------------------------

print('The {0} is {1}'.format(name, value))
# The golden ratio is 1.61803398875

# You can reference dict values like this:

info = {'name': 'boktoktok', 'address': 'the moon', 'age': 100}
other = 'the end'

print('{0[name]} is {0[age]} years old, lives on {0[address]}. {1}.'
      .format(info, other))
# boktoktok is 100 years old, lives on the moon. the end.

# The number {0} or {1} or whatever, indicates the variable to use according to
# their order in the .format() arguments.

# As a side note, you can also use keyword arguments **name to extract
# the keys and values from the dictionary and feed into a thing:

statement = '{name} who is {age} years old, lives on {address}'
print(statement.format(**info))
# boktoktok who is 100 years old, lives on the moon

# to specify the type of data as with %s, %d or %f in old style, use {:d} like:

print('The {0:s} is {1:f}'.format(name, value))
# The golden ratio is 1.618034

# adding .number limits the number of characters:

print('The {0:.2s} is {1:.2f}'.format(name, value))
# The go is 1.62
print('The {0:.10s} is {1:.10f}'.format(name, value))
# The golden rat is 1.6180339887

# adding a number without the dot says use at least this many spaces:

print('The {0:20} is {1:20}'.format(name, value))
# The golden ratio         is        1.61803398875

# Alignment can be specified with <>^ (left, right, centered):

print('{0:^40}'.format(name)) # centres within 40 spaces
#               golden ratio

# Fill empty spaces with characters:

print('{0:-^40}'.format(name))
# --------------golden ratio--------------

# Conclusion:

for i in range(1, 13):
    for j in range(1, 13):
        # this:
        print(i, 'x',  j, '=', i*j)
        # will print the same as this:
        print('{} x {} = {}'.format(i, j, i*j))

# Though in some cases, it may make for longer code, the benefit of using
# formatting is that you have access to all the formatting features described
# above as well as the ability to reference the same variables over and over,
# just by including an index number between the {} braces.

def heading(arg):
    print('{0:-^80}'.format(str(arg).title()))

# You can also use variables for any of the formatting conditions like:

width = 77

def heading(arg):
    print('{0:-^{1}}'.format(str(arg).title(), width))

heading('the end')

# -----------------------------------The End-----------------------------------

# -----------------------------------------------------------------------------
# f-strings (formatted string literals) >= Python 3.6
# -----------------------------------------------------------------------------
# As of version 3.6 you can do this. Note the f' prefix follows the same
# pattern as r' for raw strings and b' for byte strings.

f_string = f'The {name} is {value}'
print(f_string)
# The golden ratio is 1.61803398875
