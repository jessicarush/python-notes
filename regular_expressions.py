# Regular Expressions using the standard module re

import re

# Define a string pattern, and a source string to compare against.
# match () checks whether the source begins with the pattern.

result = re.match('You', 'Young Frankenstein')

# 'You' is the pattern 'Young Frankenstein' is the source

print(result)

# For more complex matches, you can compile your pattern first to speed up the match later:

pattern = re.compile('You')

# Then, you can perform your match against the compiled pattern:

result = pattern.match('Young Frankenstein')
print(result)

# or vice versa

source = 'blue red green yellow blueish blue'
m = re.match('blue', source)
if m:
    print(m.group())

# m returns nothing because match only checks out if the beginning of the source matches:

m = re.match('green', source)
if m:
    print(m.group())

# search() returns the first match, if any.

m = re.search('green', source)
if m:
    print(m.group())

# .* says there can be any amount of characters before
# . means any character
# * means any number of the preceding character

m = re.match('.*green', source)
if m:
    print(m.group())

# findall() returns a list of all non-overlapping matches, if any.

m = re.findall('blue', source)
print(m)
print('Found', len(m), 'matches')

# this says find 'e' followed by any character:

m = re.findall('e.', source)
print(m)

# the above will not return the last e because no character follows it.
# indicate the character after 'e' is optional with '?':

m = re.findall('e.?', source)
print(m)

# split() splits the source at using the patter as the split point and returns a list of the string pieces.

m = re.split(' ', source)
print(m)

# sub() takes another replacement argument, and changes all parts of source that are matched by pattern 
# to the replacement.

m = re.sub('blue', 'black', source)
print(m)

# Special characters

# \d a single digit
# \D a single non-digit
# \w an alphanumeric character
# \W an non-alphanumeric character
# \s a whitespace character
# \S a non-whitespace character
# \b a word boundary (between a \w and a \W, in either order)
# \B a non-word boundary

# The Python string module has predefined string constants that we can use for testing. 
# Printable contains 100 ASCII characters:

import string
printable = string.printable

# testing:

print(len(printable))
print(printable[0:50])
print(printable[50:])

# which characters are digits:

re.findall('\d', printable)

# which characters are digits, letters or underscore:

re.findall('\w', printable)

# note \d and \w work on whatever Unicode defines as a digit or character for example:

test = 'abc' + '-/&' + '\u00ea' +'\u0115'
re.findall('\w', test)

# Pattern Specifiers:

"""
abc                 literal abc
(expr)              expr (any valid regular expression)
expr1|expr2         expr1 or expr2
.                   any character except \n
^                   start or source string
$                   end of source string
prev?               zero or one prev
prev *              zero or more prev, as many as possible
prev *?             zero or more prev, as few as possible
prev +              one or more prev, as many as possible
prev +?             one or more prev, as few as possible
prev {m}            m consecutive prev
prev {m, n}         m to n consecutive prev, as many as possible
prev {m, n}?        m to n consecutive prev, as few as possible
[abc]               a or b or c (same as a|b|c)
[^abc]              not (a or b or c)
prev (?= next )     prev if followed by next
prev (?! next )     prev if not followed by next
(?<=prev)next       next if preceded by prev
(?<!prev)next       next if not preceded by prev
"""

# testing:

source = '''I wish I may, I wish I might
...Have a dish of fish tonight.'''

# find wish  anywhere:

re.findall('wish', source)

# find wish or fish anywhere:

print(re.findall('wish|fish', source))

# find wish at the beginning:

print(re.findall('^wish', source))

# find I wish at the beginning:

print(re.findall('^I wish', source))

# find fish at the end:

print(re.findall('fish$', source))

# find fish tonight. at the end:

print(re.findall('fish tonight.$', source))

# The characters ^ and $ are called anchors. ^ anchors the search to the beginning of the string, 
# and $ anchors it to the end. .$ matches any character at the end of the line, including a period.

# find w or f followed by ish:

print(re.findall('[wfd]ish', source))

# find one or more runs of w, s, or h:

print(re.findall('[wsh]+', source))

# find ght followed by a non-alphanumeric:

print(re.findall('ght\W', source))

# find I followed by wish:

print(re.findall('I (?=wish)', source))

# find wish preceded by I:

print(re.findall('(?<=I) wish', source))

# There are a few cases in which the regular expression pattern rules conflict with the 
# Python string rules. The following pattern should match any word that begins with fish:

print(re.findall('\bfish', source))

# \b means backspace in strings, but in the mini-language of regular expressions it means 
# the beginning of a word. Avoid the accidental use of escape characters by using Python’s 
# raw strings when you define your regular expression string. Always put an r character 
# before your regular expression pattern string, and Python escape characters will be disabled:

print(re.findall(r'\bfish', source))

# Match Output

# When using match() or search(), all matches are returned from the result object m as m.group(). 
# If you enclose a pattern in parentheses, the match will be saved to its own group, and a tuple 
# of them will be available as m.groups(), as shown here:

m = re.search(r'(. dish\b).*(\bfish)', source)

print(m.group())
print(m.group())
