'''Decorators'''


# A decorator is a function that takes one function as an input and returns
# another function. Here is a simplified example:

def my_decorator(func):
    def wrapper(arg):
        print('Before {}() is called.'.format(func.__name__))
        func(arg)
        print('After {}() is called.'.format(func.__name__))
    return wrapper

@my_decorator
def squares(n):
    '''returns the square of a number'''
    print(n ** 2)

squares(6)
# Before squares() is called.
# 36
# After squares() is called.


# @functools.wraps():
# -----------------------------------------------------------------------------
# When you use a decorator, you're replacing one function (squares) with
# another (wrapper). While inside the decorator we can see the original
# function being used but now when when outside, look what happens:

print(squares.__name__)  # wrapper
print(squares.__doc__)   # None

# That's why we have functools.wraps. This takes a function used in a decorator
# and adds the functionality of copying over the functions name, docstring,
# arguments list, etc. See the difference:

from functools import wraps

def my_decorator(func):
    @wraps(func)  # Add this, everything else is the same
    def wrapper(arg):
        print('Before {}() is called.'.format(func.__name__))
        func(arg)
        print('After {}() is called.'.format(func.__name__))
    return wrapper

@my_decorator
def squares(n):
    '''returns the square of a number'''
    print(n ** 2)

print(squares.__name__)  # squares
print(squares.__doc__)   # returns the square of a number


# Returning results
# -----------------------------------------------------------------------------
# The function document_it() below defines a decorator that will:
#  - print the functions name and values of its arguments
#  - run the function with the arguments
#  - print the result
#  - return the modified function for use

def document_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return wrapper

# Here's our simple test function, first we'll do it without a decorator:
def add_mulyiply(a, b, multiplyer=1):
    return (a + b) * multiplyer

decorated_add_ints = document_it(add_mulyiply)
decorated_add_ints(3, 5, multiplyer=100)
# Running function: add_mulyiply
# Positional arguments: (3, 5)
# Keyword arguments: {'multiplyer': 100}
# Result: 800

# Now with a decorator... a little less code:
@document_it
def add_mulyiply(a, b, multiplyer=1):
    return (a + b) * multiplyer

add_mulyiply(4, 5, multiplyer=100)
# Running function: add_mulyiply
# Positional arguments: (4, 5)
# Keyword arguments: {'multiplyer': 100}
# Result: 900


# Multiple decorators
# -----------------------------------------------------------------------------

def square_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return wrapper

# The decorator that's closest to the actual function (above the def) runs
# first and then the one above that will run. The results will be the same no
# matter what order but the intermediate steps are different. Depending on what
# your decorators do, the order may be important.

@document_it
@square_it
def add_ints(a, b):
    return a + b

print(add_ints(4, 3))
# Running function: add_ints
# Positional arguments: (4, 3)
# Keyword arguments: {}
# Result: 49
# 49

@square_it
@document_it
def add_ints(a, b):
    return a + b

print(add_ints(4, 3))
# Running function: add_ints
# Positional arguments: (4, 3)
# Keyword arguments: {}
# Result: 7
# 49


# @property
# -----------------------------------------------------------------------------
# see decorators used as getter and setter methods in classes.py


# decorators with arguments
# -----------------------------------------------------------------------------
# Consider this example. Imagine a number of functions that allow access to
# different things, but you only want to allow access if some criteria is met.
# Instead of repeating code in each function, you can set this up in a
# decorator. The only problem is, for some reason you can't add parameters to
# the decorator that has (func) passed in. So in order to do this, we have to
# create another wrapping decorator :(

def bouncer(flag):
    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if flag:
                func(*args, **kwargs)
            else:
                print('Not running the function')
        return wrapper
    return my_decorator

flag = True

@bouncer(flag)
def my_function():
    print('The function runs...')

my_function()
# The function runs...

flag = False

@bouncer(flag)
def my_function():
    print('The function runs...')

my_function()
# Not running the function


# one last example:
# -----------------------------------------------------------------------------

import time

def timing(func):
    '''Outputs the time a function takes to execute.'''
    @wraps(func)
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()
        return "Time it took to run the function: " + str((t2 - t1))
    return wrapper

@timing
def my_function():
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)

print(my_function())
# Time it took to run the function: 0.0011439323425292969
