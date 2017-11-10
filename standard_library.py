'''More from the Standard Library'''

# https://docs.python.org/3/library/index.html

# -----------------------------------------------------------------------------
# Counter()
# -----------------------------------------------------------------------------

from collections import Counter

jellybeans = ['red', 'red', 'orange', 'red', 'green', 'green']
jb_counter = Counter(jellybeans)
print(jb_counter)

# most_common() returns all elements in descending order
# (or just the top count if provided)

jb_counter.most_common(1)

# combine, find difference and find intersection of counters using +, -, &

jellybeans1 = ['red', 'red', 'orange', 'red', 'green', 'green']
jellybeans2 = ['black', 'red', 'yellow', 'yellow']

jb_counter1 = Counter(jellybeans1)
jb_counter2 = Counter(jellybeans2)

jb_counter1 + jb_counter2   # returns {'red': 4, 'green': 2, 'yellow': 2,
                            # 'black': 1, 'orange': 1}
jb_counter1 - jb_counter2   # returns {'red': 2, 'green': 2, 'orange': 1}
jb_counter2 - jb_counter1   # returns {'yellow': 2, 'black': 1}
jb_counter1 & jb_counter2   # returns {'red': 1}

# -----------------------------------------------------------------------------
# deque()
# -----------------------------------------------------------------------------
# is a double-ended queue which has features of both a stack and a queue.
# It's useful for when you want to add/delete items from either end of a
# sequence.

def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

palindrome('racecar')   # returns True
palindrome('radar')     # returns True
palindrome('maam')      # returns True
palindrome('what')      # returns False

# The example above is just an example. If you wanted to actually check for
# paildromes you could also do:

def palindrome_better(word):
    return word == word[::-1]

palindrome_better('radar')    # returns True

# -----------------------------------------------------------------------------
# itertools
# -----------------------------------------------------------------------------
# itertools are special purpose iterator functions.
# each returns one item at a time when called within a for... in loop and
# rememebers its state between calls

import itertools

# chain()
# runs through its arguments as if they were a single iterable

for item in itertools.chain([1,2], ['a', 'b']):
    print(item)

# cycle()
# is an infinite iterator, cycling through its arguments

# for item in itertools.cycle([1, 2]):
#     print(item)

# accumulate()
# calculates accumulated values. By default it calculates the sum:

for item in itertools.accumulate([1, 2, 3, 4]):
    print(item)

# you can provide a function as a second argument to accumulate().
# this will be used instead of addition. The function should take two arguments
# and return a single result.

def multiply(a, b):
    return a * b

for item in itertools.accumulate([1, 2, 3, 4], multiply):
    print(item)

# -----------------------------------------------------------------------------
# os.walk()
# -----------------------------------------------------------------------------
# os.walk recursively visits each directory from the root, and for each one,
# returns a tuple. The first item in the tuple is a string containing the
# current directory (path). Next is a list of all the directories in the
# current directory (directories). The last item on the tuple is a list
# containing all the file names (files). Note os.walk is a generator. If you
# add an input to pause the loop, you can get a sense of how its drilling down
# and through the root directory.

import os

# Put the directory path here:
root = 'music'

for path, directories, files in os.walk(root, topdown=True):
    print(path)
    print(directories)
    input()
    for f in files:
        print('\t', f)

# Use split and split text to strip out the information you want.

for path, directories, files in os.walk(root, topdown=True):
    if files:
        print(path)                  # <--path is a string
        first_split = os.path.split(path)
        print(first_split)           # <--first_split is a tuple
        print(first_split[1])        # <--contains the album name
        second_split = os.path.split(first_split[0])
        print(second_split)          # <--second_split is a tuple
        print(second_split[1])       # <--contains the artist name
        for f in files:              # <--f is a string, files is a list
            # splitext() will remove any file extension
            f = os.path.splitext(f)  # f is now a tuple
            f = f[0].split(' - ')    # f is now a list
            print(f)
        print('-' * 50)

# Using this you could easily create a database or structures file format,
# pulling out the specific bits of information.

# -----------------------------------------------------------------------------
# difflib.()
# -----------------------------------------------------------------------------
# the difflib module contains tools for comparing and working with differences
# between sequences. It's especially useful for comparing text. This example
# uses the SequenceMatcher class and its .ratio() method:

from difflib import SequenceMatcher

test = SequenceMatcher(None, 'rain', 'rainn')
print(type(test))    # <class 'difflib.SequenceMatcher'>
print(test.ratio())  # 0.8888888888888888

test = SequenceMatcher(None, 'rain', 'Rainn')
print(test.ratio())  # 0.6666666666666666

test = SequenceMatcher(None, ' rain', 'r a i n n ')
print(test.ratio())  # 5333333333333333

# The ratio method returns the similarity between two strings on a scale of 0–1.
# Note, it is case sensitive. Extra characters such as spaces and '\n' also
# count. The None argument is where you can specify which characters should be
# ignored (junk).

from difflib import get_close_matches

# get_close_matches(word, possibilities, n=3, cutoff=0.6)
#    - Use SequenceMatcher to return list of the best "good enough" matches.
#    - word is the sequence your trying to match (typically a string).
#    - possibilities is a list of sequences to match word against
#      (typically a list of strings).
#    - Optional arg n (default 3) is the maximum number of close matches to
#      return. n must be > 0.
#    - Optional arg ration cutoff (default 0.6) is a float in [0, 1].
#      Possibilities that don't score at least that similar to word are ignored

possibilities = ['train', 'car', 'grain', 'arithmetic', 'rain', 'ball']
print(get_close_matches('rainn', possibilities))  # ['rain', 'train', 'grain']
print(get_close_matches('rainn', possibilities, n=1))  # ['rain']
exit()
