# Functions, parameters and arguments

# Function names can start with letters or _ and contain only letters, numbers and _
# pass means do noting but move on. It's a placeholder.

def myfunction(one, two): # one, two are parameters
    pass
    
# Call the function like this:

myfunction(1, 2) # 1, 2 are arguments

# Positional Arguments

def menu(wine, cheese, dessert):
    return {'wine': wine, 'cheese': cheese, 'dessert': dessert}

print (menu('chardonnay', 'cake', 'swiss'))

# Keyword Arguments

print (menu(wine='chardonnay', dessert='cake', cheese='swiss'))

# Default parameters

def menu(wine, cheese, dessert='ice cream'):
    return {'wine': wine, 'cheese': cheese, 'dessert': dessert}

print (menu(wine='chardonnay', dessert='cake', cheese='swiss'))
print (menu(wine='chardonnay', cheese='swiss'))

"""
In this example the function is expected to run each time with a fresh empty result list, 
add the arg argument to it, and then print a single-item list. However, it's only empty the
first time it's called. The second time, result still has one item from the previus call.
"""

def buggy(arg, result=[]):
    result.append(arg)
    print(result)

buggy('a')
buggy('b') 

# This works better:

def works(arg):
    result=[]
    result.append(arg)
    return result

print(works('a'))
print(works('b'))

# Or fix the first one by passing in something else to indicate the first call:
# Seems a little overly verbose to me, but perhaps this will be useful later

def nonbuggy(arg, result=None):
    if result is None:
        result=[]
    result.append(arg)
    print(result)

nonbuggy('a')
nonbuggy('b')

# Gather positional Arguments

def print_args(*args):
    print('Positional argument tuple:', args)

print_args()
print_args(1,2,3, 'hello', 'tuple')

def print_more(required1, required2, *args):
    print('first argument is required:', required1)
    print('second argument is required:', required2)
    print('the rest:', args)

print_more('red', 'green', 'one', 'two', 'three')

# Gather Keyword Arguments (makes a Dictionary)

def print_kwargs(**kwargs):
    print('Keyword arguments:', kwargs)
    print(type(kwargs))

print_kwargs(wine='merlot', cheese='swiss', fruit='grapes')
print(type(print_kwargs))

# Docstrings

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