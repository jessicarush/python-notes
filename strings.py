'''Strings'''

# -----------------------------------------------------------------------------
# String methods
# -----------------------------------------------------------------------------

dir(str)
#  [..., 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith',
#  'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha',
#  'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric',
#  'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower',
#  'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust',
#  'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith',
#  'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']'

# -----------------------------------------------------------------------------
# String Literals
# -----------------------------------------------------------------------------

my_string = 'Some content'
my_string = "Some content"

# Concatenate strings with +, if the lines are long add \:

long_string = 'A long time ago ' + 'in a galaxy far, far away ' + \
    'blah blah bla...'

print(long_string)

# That being said, many feel the use of \ should be minimized. When possible,
# use parenthesis and concatenation instead:

long_string = ('A long time ago '
               'in a galaxy far, far away '
               'blah blah blabity...')

print(long_string)

# You can also use triple quotes for long strings, but I think these are best
# reserved for docstrings (see documenting_naming.py):

long_string = """This string uses
triple quotes because we're pretending
it's very, very long"""
print(long_string)

# Each line in the above will appear on a new line. If you don't want that,
# escape the last invisible line break character with \

long_string = """This string uses \
triple quotes because we're pretending \
it's very, very long"""
print(long_string)

# -----------------------------------------------------------------------------
# str() - to convert to a string
# -----------------------------------------------------------------------------

number = 4.5 * 3.25
print(str(number))

# -----------------------------------------------------------------------------
# Slice with [start : end : step]
# -----------------------------------------------------------------------------

letters = 'abcdefghijk'
print(letters[:-1])
print(letters[2:])
print(letters[2:8])
print(letters[:8])
print(letters[2:8:2])

# -----------------------------------------------------------------------------
# Break a string up into a list with .split()
# -----------------------------------------------------------------------------

test_string = 'Yeti Bigfoot Loch Ness Unicorn...'
test_list = test_string.split()
print(test_list)
print(type(test_list))

# -----------------------------------------------------------------------------
# Join a list into a string with .join()
# -----------------------------------------------------------------------------

test_string = ' '.join(test_list)
print(test_string)
print(type(test_string))

# -----------------------------------------------------------------------------
# Information you can get from strings
# -----------------------------------------------------------------------------

print(len(test_string))
print(test_string.startswith('Yeti'))
print(test_string.endswith('Yeti'))
print('Bigfoot' in test_string)

word = 'Ness'

# Find the offset of the first occurrence of a word

print(test_string.find(word))

# Find the offset of the last occurrence of a word

print(test_string.rfind(word))

# Find the total number of occurrences

print(test_string.count(word))

# Check if all characters are letters or numbers only (T/F)

print(test_string.isalnum())

# -----------------------------------------------------------------------------
# Remove and Replace
# -----------------------------------------------------------------------------
# remove characters from the beginning lstrip(), end rstrip() or both strip():
name = ' .Raja. '
name = name.lstrip()    #--> '.Raja. '
name = name.rstrip()    #--> '.Raja.'
name = name.strip('.')  #--> 'Raja'
print(name)

# Replace characters or words. You can also use a number argument
# to limit the number of replacements like: test_string.replace(' ', '-', 2)

name = 'Yello'
print(name.replace('Y', 'H'))

test_string = test_string.replace(' ', '-')
print(test_string)

test_string = test_string.replace('unicorn', 'red bull')
print(test_string)

# -----------------------------------------------------------------------------
# Change Case
# -----------------------------------------------------------------------------

test_string = test_string.lower()
print(test_string)

test_string = test_string.upper()
print(test_string)

test_string = test_string.capitalize()
print(test_string)

test_string = test_string.title()
print(test_string)

test_string = test_string.swapcase()
print(test_string)

# NOTE: .lower() and .upper() are particularly useful when you're iterating
# over a string looking for something but you don't care about the case or,
# you receive input and you don't want to handle upper and lower variations:

if 'bigfoot' in test_string.lower():
    print("He's there")

# NOTE: title() doesn't handle apostrophes very well. Use capwords() instead:

example = "I'm super fun."
print(example.title())

from string import capwords
print(capwords(example))

# -----------------------------------------------------------------------------
# Alignment
# -----------------------------------------------------------------------------

test_string = test_string.center(20)
print(test_string)

test_string = test_string.ljust(20)
print(test_string)

test_string = test_string.rjust(20)
print(test_string)

# -----------------------------------------------------------------------------
# Raw string type literals
# -----------------------------------------------------------------------------

raw_string = (r"The r at the start of a string before the quotation mark"
r"tells python it's a raw string, so any escape characters like backlash \t"
r"will be ignored... unless it's at the end of the string - then you need to"
r"do a double backlash or a space. This can come into play when creating raw"
r"strings for directory pathnames like C:\ ")

print(raw_string)
