'''Strings'''


# String methods
# -----------------------------------------------------------------------------

print(dir(str))
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__',
# '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
# '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__',
# '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__',
# '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__',
# '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize',
# 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find',
# 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit',
# 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle',
# 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition',
# 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip',
# 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title',
# 'translate', 'upper', 'zfill']


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


# Convert to a string with .str()
# -----------------------------------------------------------------------------

text = 'The number is '
number = 4.5 * 3.25
print(text + str(number))  # The number is 14.625


# Slice with [start : end : step]
# -----------------------------------------------------------------------------

letters = 'abcdefghijk'
print(letters[:3])     # abc
print(letters[-3:])    # ijk
print(letters[:6:2])   # ace
print(letters[1:8:3])  # beh
print(letters[::-1])   # kjihgfedcba


# Break a string up into a list with .split()
# -----------------------------------------------------------------------------

test_string = 'Yeti Bigfoot Loch Ness Unicorn...'
test_list = test_string.split()
print(test_list)        # ['Yeti', 'Bigfoot', 'Loch', 'Ness', 'Unicorn...']
print(type(test_list))  # <class 'list'>


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


# Break a string up into a tuple with .partition()
# -----------------------------------------------------------------------------

filename = 'image.png'
test = filename.partition('.')

print(test)  # ('image', '.', 'png')


# Join a list or tuple into a string with .join()
# -----------------------------------------------------------------------------

test_string = ' '.join(test_list)
print(test_string)        # Yeti Bigfoot Loch Ness Unicorn...
print(type(test_string))  # <class 'str'>


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


# Remove a prefix or suffix with removeprefix(), removesuffix()
# ----------------------------------------------------------------------------
# Python 3.9 added str.removeprefix(prefix) and str.removesuffix(suffix) to
# easily remove an unneeded prefix or a suffix from a string.

og_string = 'test_foo_abc'

print(og_string.removeprefix('test_'))
# foo_abc

print(og_string.removesuffix('_abc'))
# test_foo

# Note that while these look like lstrp() and rstrip(), they are not.
# The main difference is the parameters of removeprefix() and removesuffix()
# are considered substrings while the parameters of lstrip() are considered
# a set of characters. This results in the following:

# 1. lstrip() and rstrip() will remove characters in any order:

og_string = 'ab_python'

print(og_string.lstrip('ba'))
# _python

print(og_string.removeprefix('ba'))
# ab_python

# 2. lstrip() and rstrip() will remove duplicates of the characters:

og_string = 'ababbbaab_python'

print(og_string.lstrip('ba'))
# _python

print(og_string.removeprefix('ba'))
# ababbbaab_python

# 3. If no parameter is passed in, lstrip() and rstrip() will remove spaces.
# Ommitting the parameter in removeprefix() and removesuffix() results in a
# TypeError.

og_string = '   python'

print(og_string.lstrip())
# python


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


# Alignment
# -----------------------------------------------------------------------------

test1 = example.center(20)
test2 = example.ljust(20)
test3 = example.rjust(20)

test_list = [test1, test2, test3]

print(test_list)
# ["   I'm super fun.   ", "I'm super fun.      ", "      I'm super fun."]


# Raw string type literals
# -----------------------------------------------------------------------------

raw_str = (r"The 'r' at the start of a string before the quotation mark "
           r"tells python it's a raw string, so any escape characters like "
           r"backlash \t will be ignored... unless it's at the end of the "
           r"string - then you need to do a double backlash or a space. "
           r"This can come into play when creating raw strings for "
           r"directory pathnames like C:\ ")

print(raw_str)
# The 'r' at the start of a string before the quotation mark tells python it's
# a raw string, so any escape characters like backlash \t will be ignored...
# unless it's at the end of the string - then you need to do a double backlash
# or a space. This can come into play when creating raw strings for directory
# pathnames like C:\


# Note: chaining methods
# -----------------------------------------------------------------------------
# One thing that I'm clear on now but for some reason was never really pointed
# out my early training is the fact that you can 'chain' methods together.
# This is really helpful for shortening code, just make sure it's not at the
# cost of readability. In my early days I remember seeing these long, complex
# chains and it was so hard to understand what was going on.

name = ' Raja.JPEG   '
name = name.strip().lower().replace('jpeg', 'png')
print(name)
# raja.png


# See also: formatting.py
