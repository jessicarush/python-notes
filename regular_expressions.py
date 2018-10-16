'''Regular Expressions using the standard module re'''


import re

# https://docs.python.org/3/library/re.html


# match()
# -----------------------------------------------------------------------------
# Define a pattern string, and a source string to compare against.
# match() checks whether the source begins with the pattern. 'You' is the
# pattern 'Young Frankenstein' is the source

r = re.match('You', 'Young Frankenstein')

print(r)          # <_sre.SRE_Match object; span=(0, 3), match='You'>
print(r.group())  # You


# For more complex matches, you can compile your pattern first to speed up the
# match. Then, you can perform your match against the compiled pattern:

pattern = re.compile('You')
r = pattern.match('Young Frankenstein')

print(r)          # <_sre.SRE_Match object; span=(0, 3), match='You'>
print(r.group())  # You

# Obviously the source can be defined in a variable:

pattern = re.compile('blue')
source = 'blue red green yellow blueish blue'
r = re.match(pattern, source)

print(r)          # <_sre.SRE_Match object; span=(0, 4), match='blue'>
print(r.group())  # blue

# In the following, r returns nothing because match only checks out if the
# beginning of the source matches:

r = re.match('green', source)

print(r)           # None
# print(r.group()) # AttributeError: 'NoneType' object has no attribute 'group'


# Wildcards .*
# -----------------------------------------------------------------------------
# . means any character
# * means any number of the preceding character
# .* says there can be any amount of any characters before

r = re.match('.*green', source)

print(r)  # <_sre.SRE_Match object; span=(0, 14), match='blue red green'>
print(r.group())  # blue red green


# search()
# -----------------------------------------------------------------------------
# search() returns the first match, if any.

r = re.search('green', source)

print(r)          # <_sre.SRE_Match object; span=(9, 14), match='green'>
print(r.group())  # green


# findall()
# -----------------------------------------------------------------------------
# findall() returns a list of all non-overlapping matches, if any.

r = re.findall('blue', source)
print('Found', len(r), 'matches')  # Found 3 matches

# this says find 'e' followed by any character:

r = re.findall('e.', source)
print(r)  # ['e ', 'ed', 'ee', 'el', 'ei']

# The above will not return the last e because no character follows it.
# Indicate the character after 'e' is optional with '?':

r = re.findall('e.?', source)
print(r)  # ['e ', 'ed', 'ee', 'el', 'ei', 'e']


# split() and sub()
# -----------------------------------------------------------------------------
# split() splits the source using the pattern as the split point and returns
# a list of the string pieces.

r = re.split(' ', source)
print(r)  # ['blue', 'red', 'green', 'yellow', 'blueish', 'blue']

# sub() takes another replacement argument, and changes all parts of source
# that are matched by pattern to the replacement.

r = re.sub('blue', 'black', source)
print(r)  # black red green yellow blackish black


# Special characters
# -----------------------------------------------------------------------------
# \d a single digit
# \D a single non-digit
# \w an alphanumeric character
# \W an non-alphanumeric character
# \s a whitespace character
# \S a non-whitespace character
# \b a word boundary (the beginning or end of a word)
# \B a non-word boundary (not the beginning or end of a word)


# testing
# -----------------------------------------------------------------------------
sample = """
Intro:
Is this the real Life? Is this just fantasy?
Caught in a landslide, no escape from reality.
Open your eyes, look up to the skies and see.
I'm just a poor boy, I need no sympathy.
Because I'm easy come, easy go, little high, little low.
Any way the wind blows doesn't really matter to me, to me.
For testing: (Verse 1-4, Outro) beau dish, wish, fish, surreal
"""

# which characters are digits:

r = re.findall('\d', sample)
print(r)  # ['1', '4']

# which characters are digits, letters or underscore:

r = re.findall('\w', sample)

# note \d and \w work on whatever Unicode defines as a digit or character
# for example:

test = 'abc-/&\u00ea\u0115'
r = re.findall('\w', test)
print(r)  # ['a', 'b', 'c', 'ê', 'ĕ']

# There are a few cases in which the regular expression pattern rules conflict
# with the Python string rules. The following pattern should match any word
# that begins with b:

r = re.findall('\bb', sample)
print(r)  # []

# In the mini-language of regular expressions \b means the beginning or end of
# a word but in Python strings it means backspace. Avoid the accidental use of
# escape characters by using Python's "raw strings" when you define your
# regular expression string. Always put an r character before your regular
# expression pattern string, and Python escape characters will be disabled:

r = re.findall(r'\bb', sample)
print(r)  # ['b', 'b']

# The above isn't very helpful as we only get the 'b' part of the match.
# This says, find all complete words that start with the letter 'b'

r = re.findall(r'\bb\w*', sample)
print(r)  # ['boy', 'blows']

# breakdown:
# \b    - indicates the beginning of a word
# b     - starts with b
# \w*   - followed by any number of alphanumeric characters

# This says, find all words that start with the letter 'b' or 'B'
r = re.findall(r'\b[bB]\w*', sample)
print(r)  # ['boy', 'Because', 'blows']

# This says, find all 5 letter words that start with 'b' or 'B'
r = re.findall(r'\b[bB]\w\w\w\w\b', sample)
print(r)  # ['blows']

# Same as above:
r = re.findall(r'\b[bB]\w{4}\b', sample)
print(r)  # ['blows']

# Find all words that end in the letter 'r':
r = re.findall(r'\b\w*r\b', sample)
print(r)  # ['your', 'poor', 'matter', 'For']

# Doesn't work well for words ending in 't' on account of apostrophes aren't
# matched by \w. This says match any number of letters or apostrophes: [\w']*

r = re.findall(r"\b[\w']*t\b", sample)
print(r)  # ['just', 'Caught', 'just', "doesn't"]


# Pattern Specifiers
# -----------------------------------------------------------------------------
# abc              literal abc
# (...)            any valid regular expression
# a|b              a or b - these can be expressions too (...)|(...)
# .                any character except \n
# ^                start of source string
# $                end of source string
# *                zero or more of the preceding character, ab* -> a, ab, abbb
# +                one or more of the preceding character, ab+ -> ab, abbb
# ?                means the preceding character is optional (zero or one)
# abc?             c is optional, a(bc)? means bc is optional
# abc*?            zero or more c, as few as possible, will return ab
# abc+             one or more c, as many as possible
# abc+?            one or more c, as few as possible
# a{m}             number of consecutive a, a{3} is aaa
# a{m,n}           m to n consecutive a, as many as possible
# a{m,n}?          m to n consecutive a, as few as possible
# [abc]            a or b or c (same as a|b|c)
# [^abc]           not (a or b or c)
# prev(?= next)    prev if followed by next
# prev(?! next)    prev if not followed by next
# (?<=prev)next    next if preceded by prev
# (?<!prev)next    next if not preceded by prev


# More testing
# -----------------------------------------------------------------------------
# find real anywhere:
r = re.findall('real', sample)
print(r)  # ['real', 'real', 'real', 'real']

# find real where it's at the beginning of a word:
r = re.findall(r'\breal\w*', sample)
print(r)  # ['real', 'reality', 'really']

# find real where it's at the end of a word:
r = re.findall(r'\w*real\b', sample)
print(r)  # ['real', 'surreal']

# find real where it's at the beginning AND end of a word:
r = re.findall(r'\breal\b', sample)
print(r)  # ['real']

# find real where it's at the beginning OR end of a word:
r = re.findall(r'\breal\w*|\w*real\b', sample)
print(r)  # ['real', 'reality', 'really', 'surreal']

# The characters ^ and $ are called anchors. ^ anchors the search to the
# beginning of the string, and $ anchors it to the end.

# find Intro at the beginning:
r = re.findall('^Intro', sample)
print(r)  # []

# find \nIntro at the beginning:
r = re.findall('^\nIntro', sample)
print(r)  # ['\nIntro']

# find surreal at the end:
r = (re.findall('surreal$', sample))
print(r)  # ['surreal']

# find w or f or d followed by ish:
r = re.findall('[wfd]ish', sample)
print(r)  # ['dish', 'wish', 'fish']

# find one or more runs of b or c:
r = re.findall('[bc]+\w*', sample)
print(r)  # ['cape', 'boy', 'cause', 'come', 'blows']

# find me followed by a non-alphanumeric:
r = re.findall('me\W', sample)
print(r)  # ['me,', 'me,', 'me.']

# find poor followed by boy:
r = re.findall('poor (?=boy)', sample)
print(r)  # ['poor ']

# find blows preceded by wind:
r = re.findall('(?<=wind) blows', sample)
print(r)  # [' blows']

# find words that contain 3 vowels in a row:
r = re.findall(r'\b\w*[aeiuo]{3}\w*\b', sample)
print(r)  # ['beau']


# Match Output
# -----------------------------------------------------------------------------
# When using match() or search(), all matches are returned from the result
# object r as r.group(). If you enclose a pattern in parentheses, the match
# will be saved to its own group, and a tuple of them will be available as
# r.groups(), as shown here:

r = re.search(r'(escape).*(reality)', sample)

print(r.group())   # escape from reality
print(r.groups())  # ('escape', 'reality')


# Even More testing
# -----------------------------------------------------------------------------

import re
import sys

pattern = sys.argv[1]
search_string = sys.argv[2]
# To use sys.argv, run the file like this:
# $ python3 re_testing.py 'hello' 'hello world'

match = re.match(pattern, search_string)

if match:
    template = "'{}' matches pattern '{}'"
else:
    template = "'{}' doesn't match pattern '{}'"

print(template.format(search_string, pattern))
