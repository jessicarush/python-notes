'''Generators'''

# A generator is a Python sequence creation object. With it you can iterate
# through huge sequences without creating and storing the entire sequence in
# memory at once. range() is an example of a generator. Every time you iterate
# over a generator, it keeps track of where it was the last time it was called
# and returns the next value. This is different from a normal function, which
# has no memory of previous calls and always starts at its first line in the
# same state. It's important to note that because generators don't store the
# whole thing in memory but generate on the fly, you can only iterate over them
# once. Note that yield is used like return. It tells the function to return
# a generator.

# Here's an example of a generator function that would do what range() does:

def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        # the yield statement is where the execution leaves the function.
        # the execution then comes back into the function at this point,
        # preserving the state of the function.
        number += step

# The original function is a normal function:
print(type(my_range))

# Because of Yield, what's returned is a generator object:
ranger = my_range(1, 5)
print(type(ranger))

# You can iterate over the generator object"
for x in ranger:
    print(x)

# Another Generator example ----------------------------------------------------

# This example shows a function that opens and searches a file for text.
# The search words and the filename are entered as arguments. Each time
# We call the generator, it remembers where it left of and continues.

def search(keyword, filename):
    print('generator started')
    f = open(filename, 'r')
    for line in f:
        if keyword in line:
            yield line
    f.close()

search_generator = search('Mama', 'bohemian_rhapsody_lyrics.txt')

# At this point, nothing is printed because the body code of the search
# function doesn't actually run. The generator function will only return a
# generator object. To make the generator run we need to do something like:

print(next(search_generator))
print(next(search_generator))
print(next(search_generator))
print(next(search_generator))

# Another Generator example ---------------------------------------------------

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
