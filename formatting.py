'''Formatting'''


# Interpolate data values into strings (put values into strings using various
# formats). There are two ways of formatting strings: old style and new style.


# Old Style formatting - deprecated for Python 3
# -----------------------------------------------------------------------------
# Old style with % (string % data) % followed by a letter indicates the type
# of data.

test = 42

print('%s' % test)    # 42 - string
print('%d' % test)    # 42 - decimal integer
print('%f' % test)    # 42.000000 - decimal float
print('%x' % test)    # 2a - hex integer
print('%o' % test)    # 52 - octal integer
print('%e' % test)    # 4.200000e+01 - exponential float
print('%g' % test)    # 42 - decimal or exponential float
print('%d%%' % test)  # 42% - a literal %

# The %s inside a string means to interpolate the string. The number of
# appearances of %s in the string needs to match the number of data items
# after %. If more than one data variable, group like (a, b)

golden_ratio = 1.61803398875
name = 'golden ratio'

print('The %s is %f' % (name, golden_ratio))
# The golden ratio is 1.618034


# New Style formatting - with .format()
# -----------------------------------------------------------------------------

print('The {0} is {1}'.format(name, golden_ratio))
# The golden ratio is 1.61803398875

# You can reference dict values like this:

info = {'name': 'boktoktok', 'address': 'the moon', 'age': 100}
other = 'the end'

print('{0[name]} is {0[age]} years old, lives on {0[address]}. {1}.'
      .format(info, other))
# boktoktok is 100 years old, lives on the moon. the end.

# The number {0} or {1} or whatever, indicates the variable to use
# according to their order in the .format() arguments.

# As a side note, you can also use keyword arguments **name to extract
# the keys and values from the dictionary and feed into a thing:

statement = '{name} who is {age} years old, lives on {address}'

print(statement.format(**info))
# boktoktok who is 100 years old, lives on the moon

# To specify the type of data as with %s, %d or %f in old style,
# use the format {:d} like so:

print('The {0:s} is {1:f}'.format(name, golden_ratio))
# The golden ratio is 1.618034

# Format types
# -------------------------
# s - strings
# d - decimal (base 10)
# f - floats
# x - hexadecimal (base 16)
# b - binary (base 2)
# o - octal (base 8)
# e - exponents
# -------------------------

# Adding a :.int limits the number of characters (precision):

print('The {0:.2s} is {1:.2f}'.format(name, golden_ratio))
# The go is 1.62

print('The {0:.10s} is {1:.10f}'.format(name, golden_ratio))
# The golden rat is 1.6180339887

# Adding a :int (without the dot) says use at least this many spaces (width):

print('The {0:20} is {1:20}'.format(name, golden_ratio))
# The golden ratio         is        1.61803398875

# Alignment can be specified with <>^ (left, right, centered)
# For example, the following :^40 centers within 40 spaces:

print('{0:^40}'.format(name))
#               golden ratio

# Fill empty spaces with characters:

print('{0:~^40}'.format(name))
# ~~~~~~~~~~~~~~golden ratio~~~~~~~~~~~~~~

# Conclusion:

for i in range(1, 13):
    for j in range(1, 13):
        # this:
        print(i, 'x',  j, '=', i * j)
        # will print the same as this:
        print('{} x {} = {}'.format(i, j, i * j))

# Though in some cases, it may make for longer code, the benefit of using
# formatting is that you have access to all the formatting features described
# above as well as the ability to reference the same variables over and over,
# just by including an index number between the {} braces.

def heading(arg):
    print('{0:-^80}'.format(str(arg).title()))

# You can also use variables for any of the formatting conditions like:

def heading(text, width):
    print('{0:->{1}}'.format(str(text).title(), width))

heading('the end', 77)
# ----------------------------------------------------------------------The End


# f-strings (formatted string literals) - Python 3.6
# -----------------------------------------------------------------------------
# As of version 3.6 you can do this. Note the f' prefix follows the same
# pattern as r' for raw strings and b' for byte strings.

f_string = f'The {name} is {golden_ratio}'

print(f_string)
# The golden ratio is 1.61803398875

# As of Python 3.8, you can also add an = sign to self-document expressions.
# This can be really helpful for debugging. For example:

from datetime import date

user = 'eric_idle'

member_since = date(2020, 1, 20)

print(f'{user=} {member_since=}')
# user='eric_idle' member_since=datetime.date(2020, 1, 20)

# By default f-strings use str() on values but you can also use flags:

print(f'repr() flag: {user!r}')
print(f'str() flag: {user!s}')
print(f'ascii() flag: {user!a}')

# These are considered redunant though since you could just use the function:

print(f'repr(): {repr(user)}')
print(f'str(): {str(user)}')
print(f'ascii(): {ascii(user)}')

# Therefore, to output floats hexadecimicals, octals, etc...

print(f'float: {float(golden_ratio)}')
print(f'integer: {int(golden_ratio)}')
print(f'hexadecimal: {hex(member_since.year)}')
print(f'binary: {bin(member_since.year)}')
print(f'octal: {oct(member_since.year)}')
# float: 1.61803398875
# integer: 1
# hexadecimal: 0x7e4
# binary: 0b11111100100
# octal: 0o3744

# Specifying precision in f-strings:
print(f'precision: {golden_ratio:.3}')
# precision: 1.62

# Specifying width in f-strings:
print(f'width: {golden_ratio:17}')
# width:     1.61803398875

# Specifying width & precision:
print(f'width: {golden_ratio:8.3}')
# width:     1.62

# Specifying alignment in f-strings using ^<>:
print(f'alignment: {golden_ratio:^10.3}')
# alignment:    1.62

# Fill the empty spaces with characters:
print(f'alignment: {golden_ratio:~^10.3}')
# alignment: ~~~1.62~~~

# Sepcfiying date formats:
print(f'date formatting: {member_since:%A, %B %d, %Y}')
# Date formatting: Monday, January 20, 2020

# Finally, to compare the last example from the .format() section:

def heading(text, width):
    print(f'{text.title():->{width}}')

heading('the end', 77)
# ----------------------------------------------------------------------The End
