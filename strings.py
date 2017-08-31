# STRINGS

# valid strings:

my_string = 'Some content'
my_string = "Some content"

# str() - to convert to a string:

number = 4.5 * 3.25
print(str(number))

# String together strings with +, if the lines are long add \:

long_string = 'A long time ago ' + \
    'in a galaxy far, far away ' + \
    'blah blah bla...'

# You can use triple quotes for long strings:

long_string = """This string uses
    triple quotes because we're pretending
    it's very, very long"""

# Each line in the above will appear on a new line. If you don't want that,
# escape the last invisible line break character with \

long_string = """This string uses \
    triple quotes because we're pretending \
    it's very, very long"""

# .replace()

name = 'Yello'
name = name.replace('Y', 'H')
print(name)

# Slice with [start : end : step]

letters = 'abcdefghijk'
print(letters[:-1])
print(letters[2:])
print(letters[2:8])
print(letters[:8])
print(letters[2:8:2])

# Break a string up into a list with .split()

test_string = 'Yeti Bigfoot Loch Ness Unicorn...'
test_list = test_string.split()
print(test_list)
print(type(test_list))

# Join a list into a string with .join()

test_string = ' '.join(test_list)
print(test_string)
print(type(test_string))

# Information you can get from strings

print(len(test_string))
print(test_string.startswith('Yeti'))
print(test_string.endswith('Yeti'))
print('Bigfoot' in test_string)

word = 'Ness'

# Find the offset of the first occurence of a word

print(test_string.find(word))

# Find the offset of the last occurence of a word

print(test_string.rfind(word))

# Find the total number of occurences

print(test_string.count(word))

# Check if all characters are letters or numbers only (T/F)

print(test_string.isalnum())

# remove characters from the beginning and end:

test_string = test_string.strip('.')
print(test_string)

# Replace characters or words. You can also use a number argument
# to limit the number of replacements like: test_string.replace(' ', '-', 2)

test_string = test_string.replace(' ', '-')
print(test_string)

test_string = test_string.replace('unicorn', 'red bull')
print(test_string)

# Change case:

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

# Alignemnt (not sure why you would ever do this):

test_string = test_string.center(20)
print(test_string)

test_string = test_string.ljust(20)
print(test_string)

test_string = test_string.rjust(20)
print(test_string)
