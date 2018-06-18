'''Generators'''

# A generator is a Python sequence creation object. With it you can iterate
# through huge sequences without creating and storing the entire sequence in
# memory at once. range() is an example of a generator. Every time you iterate
# over a generator, it keeps track of where it was the last time it was called
# and returns the next value. This is different from a normal function, which
# has no memory of previous calls and always starts at its first line in the
# same state. It's important to note that since generators don't store the
# whole range in memory (but generate on the fly), you can only iterate over
# a generator object once (however, the range class resets itself each time,
# so in its case, you can). That being said, you can always call a generator
# function again. Note that yield is used like return... it tells the
# function to return a generator.

# Here's an example of a generator function that would do what range() does:

def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        # the yield statement marks the point where the function will return
        # to generate each item. Each time, it remembers it's previous value
        # when it returns. The generator doesn't actually start generating
        # until you iterate over it with a for loop or next().
        number += step

# The original function is a normal function:
print(type(my_range))
# <class 'function'>

# The result of the functions 'yield' keyword (instead of 'return')
# produces a generator object:
ranger = my_range(1, 5)
print(type(ranger))
# <class 'generator'>

# You can iterate over the generator object:
for x in ranger:
    print(x)
# 1
# 2
# 3
# 4


# Reduced size
# -----------------------------------------------------------------------------
# This example illustrates the size difference between generators and a full
# list equivalent (keep in mind these sizes are using up memory):

import sys

big_range = my_range(1, 10000)

print('big_range is {} bytes'.format(sys.getsizeof(big_range)))
# big_range is 88 bytes

big_list = list(range(1, 10000))

print('big_list is {} bytes'.format(sys.getsizeof(big_list)))
# big_list is 90096 bytes


# Another Generator example
# -----------------------------------------------------------------------------
# This example shows a function that opens and searches a file for text.
# The search words and the filename are entered as arguments. Each time
# We call the generator, it remembers where it left of and continues.

def search(keyword, filename):
    print('generator started')
    with open(filename, 'r') as f:
        for line in f:
            if keyword in line:
                yield line

search_generator = search('Mama', 'data/bohemian_rhapsody_lyrics.txt')

# At this point, nothing is printed because the body code of the search
# function doesn't actually run. The generator function will only return a
# generator object. To make the generator run we need to do something like:

print(next(search_generator))  # generator started, Mama, just killed a man
print(next(search_generator))  # Mama, life had just begun
print(next(search_generator))  # Mama, ooo
print(next(search_generator))  # Mama, ooo (anyway the wind blows)


# Another Generator example
# -----------------------------------------------------------------------------

def fibonacci(n):
    curr = 1
    prev = 0
    counter = 0
    print('ok go')
    while counter < n:
        yield curr
        prev, curr = curr, prev + curr
        counter += 1

test_fibonacci = fibonacci(10)

for i in test_fibonacci:
    print(i)
# ok go
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55


# Multiple Yields
# -----------------------------------------------------------------------------

def odds_generator():
    '''generate infinite odd numbers'''
    number = 1
    while True:
        yield number
        number += 2

def pi_series():
    '''generate π using Leibniz Formula
       https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80
    '''
    odds = odds_generator()
    approximation = 0
    while True:
        approximation += (4 / next(odds))
        yield approximation
        approximation -= (4 / next(odds))
        yield approximation

approx_pi = pi_series()

# The hight the range, the closer it gets to pi. Not really sure why this
# formula is useful because I'm not mathy, but the interesting point here
# is the multiple yields which execute in turn with each loop.

for x in range(100):
    print(next(approx_pi))
