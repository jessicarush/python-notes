# Functions

"""
Functions are objects, just like numbers, strimgs, tuples, lists, dictionaries, etc. 
They can be assigned to variables, used as arguments to otehr functions, or returned
from other functions.
"""

# A simple example:

def answer():
    print(100)

def run_something(func):
    func()

run_something(answer)


#The paramater names arg1 and arg2 don't need to match those in the following function:

def add_args(arg1, arg2):
    print(arg1 + arg2)
    
def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)

run_something_with_args(add_args, 5, 10)

# Here's an example with a variable number of arguments:

def sum_args(*args):
    print(sum(args))

def run_with_positional_args(func, *args):
    return func(*args)
    
run_with_positional_args(sum_args, 2, 3, 1, 4)

# Inner Functions

def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)

outer(4, 7)

def nerd(saying):
    def inner(quote):
        print("We are the knights who say: '%s'" % quote)
    return inner(saying)

nerd("blerk")

"""
An inner function can act as a closure. In this example the inner2 function knows 
the value of saying that was passed in and remembers it. The line return inner2 returns
this specialized copy of the inner2 function (but doesn't call it). That's a closure...
a dynamically created function that remembers where it came from.
"""

def nerd2(saying):
    def inner2():
        print("We are the knights who say: '%s'" % saying)
    return inner2

a = nerd2('farble')
b = nerd2('gook')
a()
b()

# The lambda function is an anonymous function expressed as a single statement
# Use it instead of a normal tiny function.

def edit_story(words, func):
    for word in words:
        print(func(word))

sounds = ['thud', 'hiss', 'meow', 'tweet']

def headline(testing):
    return testing.capitalize() + '!'

edit_story(sounds, headline)

# The headline function can be replaced this way:

edit_story(sounds, lambda word: word.capitalize() + '!')
