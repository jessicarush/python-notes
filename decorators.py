'''Decorators'''

# functions that take one function as an input and return another function.

# Here is a simplified example:

def my_decorator(some_function):
    def wrapper():
        print('Something happens before some_function() is called.')
        some_function()
        print('Something happens after some_function() is called.')
    return wrapper

@my_decorator
def my_function():
    print("The function runs")

my_function()

# Another example... this decorator will print start when the function is
# called and 'end' when it finishes:

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

# Here's our simple test function:
def add_ints(a, b):
    return a + b

# Note, we could achieve the same result like this:
decorated_add_ints = document_it(add_ints)
print(decorated_add_ints(3,5))

# But decorating like this means less code:
@document_it
def add_ints(a, b):
    return a + b

add_ints(4, 5)

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
