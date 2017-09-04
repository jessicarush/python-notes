'''Functions, parameters and arguments'''

# Write a function with def() -------------------------------------------------

# Function names can start with letters or _ and contain only letters, numbers
# and _. Pass means do noting but move on. It's a placeholder.
# NOTE: it's good practice to put two spaces after each function definition,
# unless they're nested inside another function or class.

def myfunction(num1, num2): # num1, num2 are parameters
    pass

# Call the function() --------------------------------------------------------

myfunction(1, 2) # 1, 2 are arguments

# Reminder: return vs print --------------------------------------------------

def myfunction1(num1, num2):
    print(num1 * num2) # prints the result but returns None

def myfunction2(num1, num2):
    return num1 * num2 # prints nothing but returns the result

# example:
def heading(arg):
    print('{0:-^80}'.format(str(arg).title()))

heading('Positional Arguments')

# Positional Arguments -------------------------------------------------------

def menu(wine, cheese, dessert):
    return {'wine': wine, 'cheese': cheese, 'dessert': dessert}

print(menu('chardonnay', 'cake', 'swiss'))

# Keyword Arguments ----------------------------------------------------------

print(menu(wine='chardonnay', dessert='cake', cheese='swiss'))

# Default Parameters ---------------------------------------------------------

def menu(wine, cheese, dessert='ice cream'):
    return {'wine': wine, 'cheese': cheese, 'dessert': dessert}

print (menu(wine='chardonnay', dessert='cake', cheese='swiss'))
print (menu(wine='chardonnay', cheese='swiss'))

# Weird Example --------------------------------------------------------------

# In this example the function is expected to run each time with a fresh empty
# result list, add the arg argument to it, and then print a single-item list.
# However, it's only empty the first time it's called. The second time, result
# still has one item from the previous call.

def buggy(arg, result=[]):
    result.append(arg)
    print(result)

buggy('a')
buggy('b')
buggy('new list', ['hello', 'hello'])

# This works better to have an empty list each time:

def works(arg):
    result=[]
    result.append(arg)
    print(result)

works('a')
works('b')

# Or fix the first one by passing in something else to indicate the first call:
# This whole example seems a bit pointless to me but perhaps it will be useful
# later on:

def nonbuggy(arg, result=None):
    if result is None:
        result=[]
    result.append(arg)
    print(result)

nonbuggy('a')
nonbuggy('b')
nonbuggy('new list', ['hello', 'hello'])

# Gather Positional Arguments ------------------------------------------------

def print_args(*args):
    print('Positional argument tuple:', args)

print_args(1, 2, 3, 'hello', 'tuple')

def print_more(required1, required2, *args):
    print('first argument is required:', required1)
    print('second argument is required:', required2)
    print('the rest:', args)

print_more('red', 'green')
print_more('red', 'green', 'one', 'two', 'three')

# Gather Keyword Arguments (makes a Dictionary) ------------------------------

def print_kwargs(**kwargs):
    print('Keyword arguments:', kwargs)
    print(type(kwargs)) # class 'dict'

print_kwargs(wine='merlot', cheese='swiss', fruit='grapes')

# see also terminology.py for another example

# Docstrings -----------------------------------------------------------------

def myfunction1(arg):
    '''this is where you can provide a brief description of the function'''
    print(arg)

def myfunction2(arg):
    '''
    This lets
    you
    do
    a *longer*
    description
    '''
    print(arg)

print(myfunction1.__doc__)
print(myfunction2.__doc__)

# Functions as Arguments -----------------------------------------------------

# Functions are objects, just like numbers, strings, tuples, lists,
# dictionaries, etc. They can be assigned to variables, used as arguments to
# other functions, or returned from other functions.

def answer():
    print(100)

def run_something(func):
    func()

run_something(answer)

# The parameter names arg1 and arg2 don't need to match those in the following
# function, just using those names as examples:

def add_args(arg1, arg2):
    print(arg1 + arg2)

def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)

run_something_with_args(add_args, 5, 10)

# An example with a variable number of arguments:

def sum_args(*args):
    print(sum(args))

def run_with_positional_args(func, *args):
    return func(*args)

run_with_positional_args(sum_args, 2, 3, 1, 4)

# Inner Functions ------------------------------------------------------------

def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)

outer(4, 7)

def nerd(saying):
    def inner(quote):
        print('They said: {}'.format(quote))
    return inner(saying)

nerd("blerk")

# An inner function can act as a closure. In this example the inner2 function
# knows the value of saying that was passed in and remembers it. The line
# return inner2 returns this specialized copy of the inner2 function (but
# doesn't call it). That's a closure... a dynamically created function that
# remembers where it came from.

def nerd2(saying):
    def inner2():
        print('They said: {}'.format(saying))
    return inner2

a = nerd2('bok') # <function nerd2.<locals>.inner2 at 0x1011879d8>
b = nerd2('tok') # <function nerd2.<locals>.inner2 at 0x101187a60>

# lambda() -------------------------------------------------------------------

# The lambda function is an anonymous function expressed as a single statement
# Use it instead of a normal tiny function.

def edit_story(words, func):
    for word in words:
        print(func(word))

sounds = ['thud', 'hiss', 'meow', 'tweet']

def headline(testing):
    return testing.capitalize() + '!'

edit_story(sounds, headline)

# Using lambda, the headline function can be replaced this way:

edit_story(sounds, lambda word: word.capitalize() + '!')
