# Decorators

# A decorator is a function that takes one function as an input and returns another function.

"""
the function document_it() defines a decorator that will:
 - print the functions name and values of its arguments
 - run the function with the arguments
 - print the result
 - return the modified function for use
"""

def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function

def add_ints(a, b):
    return a + b

print(add_ints(3, 5))

cooler_add_ints = document_it(add_ints)
print(cooler_add_ints(3,5))

#or do this:

@document_it
def add_ints(a, b):
    return a + b

add_ints(4, 5)

def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function

# you can have more that one decorator for a function
# the decorator thats closest to the actual function (above the def) runs first and then the one above that will run. The results will be the same no matter what order but the intermedate steps are different obv.

@document_it
@square_it
def add_ints(a, b):
    return a + b

print(add_ints(4, 3))


@square_it
@document_it
def add_ints(a, b):
    return a + b

print(add_ints(4, 3))
