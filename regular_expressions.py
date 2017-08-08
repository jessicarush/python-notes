# Regular Expressions using the standard module re

import re

# Define a pattern string, and a source string to compare against.
# match() checks whether the source begins with the pattern.

r = re.match('You', 'Young Frankenstein')

# 'You' is the pattern 'Young Frankenstein' is the source

print(r)

# For more complex matches, you can compile your pattern first to speed up the match later:

pattern = re.compile('You')

# Then, you can perform your match against the compiled pattern:

r = pattern.match('Young Frankenstein')

# Here's another way:

source = 'blue red green yellow blueish blue'
r = re.match('blue', source)
if r:
    print(r.group())

# In the following, m returns nothing because match only checks out if the beginning of 
# the source matches:

r = re.match('green', source)
if r:
    print(r.group())

# search() returns the first match, if any.

r = re.search('green', source)
if r:
    print(r.group())

# . means any character
# * means any number of the preceding character
# .* says there can be any amount of any characters before

r = re.match('.*green', source)
if r:
    print(r.group())

# findall() returns a list of all non-overlapping matches, if any.

r = re.findall('blue', source)
print(r)
print('Found', len(r), 'matches')

# this says find 'e' followed by any character:

r = re.findall('e.', source)
print(r)

# The above will not return the last e because no character follows it. 
# Indicate the charcter after 'e' is optional with '?':

r = re.findall('e.?', source)
print(r)

# split() splits the source at using the pattern as the split point and returns a list of 
# the string pieces.

r = re.split(' ', source)
print(r)

# sub() takes another replacement argument, and changes all parts of source that are matched 
# by pattern to the replacement.

r = re.sub('blue', 'black', source)
print(r)

# Special characters

# \d a single digit
# \D a single non-digit
# \w an alphanumeric character
# \W an non-alphanumeric character
# \s a whitespace character
# \S a non-whitespace character
# \b a word boundary (the beginning or end of a word)
# \B a non-word boundary (not the beginning or end of a word)

# testing:

sample = """
Intro:
Is this the real Life? Is this just fantasy?
Caught in a landslide, no escape from reality.
Open your eyes, look up to the skies and see.
I'm just a poor boy, I need no sympathy.
Because I'm easy come, easy go, little high, little low.
Any way the wind blows doesn't really matter to me, to me.
For testing: (Verse 1-4, Outro) dish, wish, fish, surreal
"""

# which characters are digits:

r = re.findall('\d', sample)
print(r)

# which characters are digits, letters or underscore:

r = re.findall('\w', sample)
print(r)

# note \d and \w work on whatever Unicode defines as a digit or character for example:

test = 'abc' + '-/&' + '\u00ea' +'\u0115'
r = re.findall('\w', test)
print(r)

# There are a few cases in which the regular expression pattern rules conflict with the 
# Python string rules. The following pattern should match any word that begins with b:

r = re.findall('\bb', sample)
print(r)

# In the mini-language of regular expressions \b means the beginning or end of a word but 
# in Python strings it means backspace. Avoid the accidental use of escape characters by 
# using Python’s "raw strings" when you define your regular expression string. Always put 
# an r character before your regular expression pattern string, and Python escape characters 
# will be disabled:

r = re.findall(r'\bb', sample)
print(r)

# The above isn't very helpful as we only get the 'b' part of the match. 
# This says, find all complete words that start with the letter 'b'

r = re.findall(r'\bb\w*', sample)
print(r)

# breakdown:
# \b    - indicates the beginning of a word
# b     - starts with b
# \w*   - followed by any number of alphanumeric characters

# This says, find all words that start with the letter 'b' or 'B'

r = re.findall(r'\b[bB]\w*', sample)
print(r)

# This says, find all 5 letter words that with 'b' or 'B'

r = re.findall(r'\b[bB]\w\w\w\w\b', sample)
print(r)

# Same as above:

r = re.findall(r'\b[bB]\w{4}\b', sample)
print(r)

# Find all words that end in the letter 'r':

r = re.findall(r'\b\w*r\b', sample)
print(r)

# Doesn't work well for words ending in 't' on account of apostrophes aren't matched by \w
# This says match any number of letters or apostrophes: [\w']* 

r = re.findall(r"\b[\w']*t\b", sample)
print(r)

# Pattern Specifiers:

# abc                 literal abc
# (...)               any valid regular expression
# a|b                 a or b
# .                   any character except \n
# *                   any number of the preceding character (0 or more)
# ^                   start of source string
# $                   end of source string
# abc?                c is optional, a(bc)? means bc is optional
# abc*                c (and repetitions of c) is optional, will return ab, abc, abcccc
# abc*?               zero or more c, as few as possible, will return ab
# abc+                one or more c, as many as possible
# abc+?               one or more c, as few as possible
# a{m}                number of consecutive a, a{3} is aaa
# a{m, n}             m to n consecutive a, as many as possible
# a{m, n}?            m to n consecutive a, as few as possible
# [abc]               a or b or c (same as a|b|c)
# [^abc]              not (a or b or c)
# prev(?= next)       prev if followed by next
# prev(?! next)       prev if not followed by next
# (?<=prev)next       next if preceded by prev
# (?<!prev)next       next if not preceded by prev

# More testing:

# find real anywhere:

r = re.findall('real', sample)
print(r)

# find real where it's at the beginning of a word:

r = re.findall(r'\breal\w*', sample)
print(r)

# find real where it's at the end of a word:

r = re.findall(r'\w*real\b', sample)
print(r)

# find real where it's at the beggining and end of a word:

r = re.findall(r'\breal\b', sample)
print(r)

# find real where it's at the beggining OR end of a word:

r = re.findall(r'\breal\w*|\w*real\b', sample)
print(r)

# The characters ^ and $ are called anchors. ^ anchors the search to the beginning of 
# the string, and $ anchors it to the end.

# find Intro at the beginning:

r = re.findall('^Intro', sample)
print(r)

# find \nIntro at the beginning:

r = re.findall('^\nIntro', sample)
print(r)

# find surreal at the end:

r = (re.findall('surreal$', sample))
print(r)

# find w or f or d followed by ish:

r = re.findall('[wfd]ish', sample)
print(r)

# find one or more runs of b or c:

r = re.findall('[bc]+\w*', sample)
print(r)

# find me followed by a non-alphanumeric:

r = re.findall('me\W', sample)
print(r)

# find poor followed by boy:

r = re.findall('poor (?=boy)', sample)
print(r)

# find blows preceded by wind:

r = re.findall('(?<=wind) blows', sample)
print(r)

# find words that contain 3 vowels in a row:

r = re.findall(r'\b\w*[aeiuo]{3}\w*\b', sample)
print(r)

# Match Output

# When using match() or search(), all matches are returned from the result object 
# r as r.group(). If you enclose a pattern in parentheses, the match will be saved 
# to its own group, and a tuple of them will be available as r.groups(), as shown here:

r = re.search(r'(escape).*(reality)', sample)

print(r.group())
print(r.groups())
