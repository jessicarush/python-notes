'''Decorators'''

# A decorator is a function that takes one function as an input and returns
# another function. Here is a simplified example:

def my_decorator(some_func):
    def wrapper(*args):
        print('This happens before {}() is called.'.format(some_func.__name__))
        some_func(*args)
        print('This happens after {}() is called.'.format(some_func.__name__))
    return wrapper

@my_decorator
def squares(n):
    print(n ** 2)

squares(6)
# This happens before squares() is called.
# 36
# This happens after squares() is called.

# A similar example, written a little differently. This decorator will print
# start when the function is called and 'end' when it finishes:

def test(func):
    def new_func(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return new_func

@test
def greeting():
    print('hello')

greeting()
# start
# hello
# end

# The function document_it() below defines a decorator that will:
#  - print the functions name and values of its arguments
#  - run the function with the arguments
#  - print the result
#  - return the modified function for use

def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function

# Here's our simple test function, first we'll do it without a decorator:
def add_ints(a, b):
    return a + b

decorated_add_ints = document_it(add_ints)
print(decorated_add_ints(3,5))
# Running function: add_ints
# Positional arguments: (3, 5)
# Keyword arguments: {}
# Result: 8
# 8

# Now with a decorator -- less code:
@document_it
def add_ints(a, b):
    return a + b

add_ints(4, 5)
# Running function: add_ints
# Positional arguments: (4, 5)
# Keyword arguments: {}
# Result: 9

# You can have more that one decorator applied to a function.

def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function

# The decorator that's closest to the actual function (above the def) runs
# first and then the one above that will run. The results will be the same no
# matter what order but the intermediate steps are different. Depending on what
# your decorators do, the order may be important.

@document_it
@square_it
def add_ints(a, b):
    return a + b

print(add_ints(4, 3))
# Running function: new_function
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

# -----------------------------------------------------------------------------
# @property
# -----------------------------------------------------------------------------
# see decorators used as getter and setter methods in classes.py

# -----------------------------------------------------------------------------
# Decorators example:
# -----------------------------------------------------------------------------

import time

def timing(func):
    '''Outputs the time a function takes to execute.'''

    def new_func():
        t1 = time.time()
        func()
        t2 = time.time()
        return "Time it took to run the function: " + str((t2 - t1))
    return new_func

@timing
def my_function():
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)

print(my_function())
# Time it took to run the function: 0.0011439323425292969
