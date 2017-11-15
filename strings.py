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

# Concatenate strings with '+'. If the lines are long you can add '\':

long_string1 = 'A long time ago, ' + 'in a galaxy far, far away... ' + \
              'blah blah bla...'

# That being said, many feel the use of \ should be minimized. When possible,
# use parenthesis instead. When strings fall on new lines, you don't need '+':

long_string2 = ('A long time ago, ' + 'in a galaxy far, far away... '
              'blah blah bla...')

long_string3 = ('A long time ago, '
               'in a galaxy far, far away... '
               'blah blah bla...')

print(long_string1)
print(long_string2)
print(long_string3)
# A long time ago, in a galaxy far, far away... blah blah bla...
# A long time ago, in a galaxy far, far away... blah blah bla...
# A long time ago, in a galaxy far, far away... blah blah bla...

# You can also use triple quotes for long strings, but I think these are
# best reserved for docstrings (see documenting_naming.py). When using triple
# quotes, all invisible line breaks and spaces are included in the output.

long_string = """A long time ago,
in a galaxy far, far away...
It is a period of civil war."""

print(long_string)
# A long time ago,
# in a galaxy far, far away...
# It is a period of civil war.

# -----------------------------------------------------------------------------
# Convert to a string with .str()
# -----------------------------------------------------------------------------

text = 'The number is '
number = 4.5 * 3.25
print(text + str(number))  # The number is 14.625

# -----------------------------------------------------------------------------
# Slice with [start : end : step]
# -----------------------------------------------------------------------------

letters = 'abcdefghijk'
print(letters[:3])     # abc
print(letters[-3:])    # ijk
print(letters[:6:2])   # ace
print(letters[1:8:3])  # beh
print(letters[::-1])   # kjihgfedcba

# -----------------------------------------------------------------------------
# Break a string up into a list with .split()
# -----------------------------------------------------------------------------

test_string = 'Yeti Bigfoot Loch Ness Unicorn...'
test_list = test_string.split()
print(test_list)        # ['Yeti', 'Bigfoot', 'Loch', 'Ness', 'Unicorn...']
print(type(test_list))  # <class 'list'>

# -----------------------------------------------------------------------------
# Break a large string up into a list of lines with .splitlines()
# -----------------------------------------------------------------------------

long_string = '''
A long time ago, in a galaxy far, far away...
It is a period of civil war. Rebel
spaceships, striking from a hidden
base, have won their first victory
against the evil Galactic Empire. '''

splitline_list = long_string.splitlines()
print(splitline_list[3])     # spaceships, striking from a hidden
print(type(splitline_list))  # <class 'list'>

# -----------------------------------------------------------------------------
# Join a list into a string with .join()
# -----------------------------------------------------------------------------

test_string = ' '.join(test_list)
print(test_string)        # Yeti Bigfoot Loch Ness Unicorn...
print(type(test_string))  # <class 'str'>

# -----------------------------------------------------------------------------
# .len(), .startswith(), .endswith(), .find(), .rfind(), .count(), .isalnum()
# -----------------------------------------------------------------------------

print(len(test_string))                # 33
print(test_string.startswith('Yeti'))  # True
print(test_string.endswith('Yeti'))    # False
print('Bigfoot' in test_string)        # True

# Find the offset of the first occurrence of a word

word = 'Ness'

print(test_string.find(word))  # 18

# Find the offset of the last occurrence of a word

print(test_string.rfind(word))  # 18

# Find the total number of occurrences

print(test_string.count(word))  # 1

# Check if all characters are letters or numbers only (T/F)

print(test_string.isalnum())  # False

# -----------------------------------------------------------------------------
# Remove and replace: .lstrip(), .rstrip(), .strip(), .replace()
# -----------------------------------------------------------------------------
# remove characters from the beginning with .lstrip(), the end with .rstrip()
# or both with .strip():

name = '- Raja -'
name = name.lstrip('-')  # ' Raja -'
name = name.rstrip('-')  # ' Raja '
name = name.strip(' ')   # 'Raja'

# Replace characters or words. You can also use a number argument
# to limit the number of replacements like: test_string.replace(' ', '-', 2)

name = 'Yello'
print(name.replace('Y', 'H'))  # Hello

test_string = test_string.replace(' ', ', ')
print(test_string)  # Yeti, Bigfoot, Loch, Ness, Unicorn...

test_string = test_string.replace('Unicorn', 'Dragon')
print(test_string)  # Yeti, Bigfoot, Loch, Ness, Dragon...

# -----------------------------------------------------------------------------
# Change Case
# -----------------------------------------------------------------------------

test_string = test_string.lower()
print(test_string)  # yeti, bigfoot, loch, ness, dragon...

test_string = test_string.upper()
print(test_string)  # YETI, BIGFOOT, LOCH, NESS, DRAGON...

test_string = test_string.capitalize()
print(test_string)  # Yeti, bigfoot, loch, ness, dragon...

test_string = test_string.title()
print(test_string)  # Yeti, Bigfoot, Loch, Ness, Dragon...

test_string = test_string.swapcase()
print(test_string)  # yETI, bIGFOOT, lOCH, nESS, dRAGON...

# NOTE: .lower() and .upper() are particularly useful when you're iterating
# over a string looking for something but you don't care about the case or,
# you receive input and you don't want to handle upper and lower variations:

if 'bigfoot' in test_string.lower():
    print("He's there")  # He's there

# NOTE: title() doesn't handle apostrophes very well. Use capwords() instead:

from string import capwords

example = "I'm super fun."

print(example.title())    # I'M Super Fun.
print(capwords(example))  # I'm Super Fun.

# -----------------------------------------------------------------------------
# Alignment
# -----------------------------------------------------------------------------

test1 = example.center(20)
test2 = example.ljust(20)
test3 = example.rjust(20)

test_list = [test1, test2, test3]

print(test_list)
# ["   I'm super fun.   ", "I'm super fun.      ", "      I'm super fun."]

# -----------------------------------------------------------------------------
# Raw string type literals
# -----------------------------------------------------------------------------

raw_string = (r"The r at the start of a string before the quotation mark"
r"tells python it's a raw string, so any escape characters like backlash \t"
r"will be ignored... unless it's at the end of the string - then you need to"
r"do a double backlash or a space. This can come into play when creating raw"
r"strings for directory pathnames like C:\ ")

print(raw_string)
