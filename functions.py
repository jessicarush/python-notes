'''Functions'''


from datetime import datetime
from time import sleep


# Write a function with def()
# -----------------------------------------------------------------------------
# Function names can start with letters or _ and contain only letters, numbers
# and _. Pass means do noting but move on. It's a placeholder.
# NOTE: it's good practice to put two spaces after each function definition,
# unless they're nested inside another function or class.

def myfunction(num1, num2): # num1, num2 are parameters
    pass


# Call the function()
# -----------------------------------------------------------------------------
myfunction(1, 2) # 1, 2 are arguments


# Reminder: return vs print
# -----------------------------------------------------------------------------

def myfunction1(num1, num2):
    print(num1 * num2) # prints the result but returns None

def myfunction2(num1, num2):
    return num1 * num2 # prints nothing but returns the result

# example:
def heading(arg):
    return('{0:-^80}'.format(str(arg).title()))

h = heading('Positional Arguments')
print(h)


# Positional Arguments
# -----------------------------------------------------------------------------

def menu(wine, cheese, dessert):
    return {'wine': wine, 'cheese': cheese, 'dessert': dessert}

print(menu('chardonnay', 'cake', 'swiss'))
# {'wine': 'chardonnay', 'cheese': 'cake', 'dessert': 'swiss'}


# Keyword Arguments
# -----------------------------------------------------------------------------

print(menu(wine='chardonnay', dessert='cake', cheese='swiss'))
# {'wine': 'chardonnay', 'cheese': 'swiss', 'dessert': 'cake'}


# Keyword-only arguments
# -----------------------------------------------------------------------------
# In the examples above, we see that it's optional as to whether we use
# keywords when calling the function. If you feel that for the sake of
# clarity, keywords should be mandatory, you can specify this by using '*'.
# The '*' in the argument list indicates the end of positional arguments and
# the beginning of keyword-only arguments. This way there will be no confusion.

def menu(wine, cheese, *, courses=3, guests=1):
    return {'wine': wine, 'cheese': cheese}

# menu('merlot', 'brie', 2, 4)
# TypeError: menu() takes 2 positional arguments but 4 were given

menu('merlot', 'brie', guests=2, courses=4)


# Use None to specify dynamic default values
# -----------------------------------------------------------------------------
# In this example the function is expected to run each time with a fresh empty
# result list, add the argument to it, and then print the single-item list.
# However, it's only empty the first time it's called. The second time, result
# still has one item from the previous call. The reason for this is that
# default argument values are evaluated only once per module load (which
# usually happens when a program starts up). To be precise, the default values
# are generate at the point the function is defined, not when it's called.

def buggy(arg, result=[]):
    result.append(arg)
    print(result)

buggy('a')  # ['a']
buggy('b')  # ['a', 'b']
buggy('c', ['hello', 'hello'])  # ['hello', 'hello', 'c']

# This works better to have an empty list each time, however we no longer
# have the option of passing in a list:

def works(arg):
    result=[]
    result.append(arg)
    print(result)

works('a')  # ['a']
works('b')  # ['b']

# Correct the first one by passing in None to indicate the first call:

def nonbuggy(arg, result=None):
    if result is None:
        result=[]
    result.append(arg)
    print(result)

# or more common method of writing it:

def nonbuggy(arg, result=None):
    result = result if result else []
    result.append(arg)
    print(result)

nonbuggy('a')  # ['a']
nonbuggy('b')  # ['b']
nonbuggy('new list', ['hello', 'hello'])  # ['hello', 'hello', 'new list']

# A more practical example of this situation would be where we want to set
# a default value using a timestamp. In this case, we want to use a function
# that gets the current time. If we put the function as the default value,
# the function will only evaluate once, therefor the time will never update:

def log(message, timestamp=datetime.now()):
    print(f'{timestamp}: {message}')

log('hello')
sleep(1)
log('hello again')
# 2018-02-06 15:46:31.847122: hello
# 2018-02-06 15:46:31.847122: hello again

# Instead use None as the default, also a more compact expression:

def log(message, timestamp=None):
    timestamp = timestamp if timestamp else datetime.now()
    print(f'{timestamp}: {message}')

log('hello')
sleep(1)
log('hello again')
# 2018-02-06 15:46:32.852450: hello
# 2018-02-06 15:46:33.857498: hello again


# Gathering Positional Arguments - *args
# -----------------------------------------------------------------------------
# The * operator used when defining a function means that any extra positional
# arguments passed to the function end up in the variable prefaced with the *.

# In short, args is a tuple and * unpacks the tuple

def print_args(*args):
    print(args, type(args))

print_args(1, 2, 3, 'hello')  # (1, 2, 3, 'hello') <class 'tuple'>
print_args(1)                 # (1,) <class 'tuple'>

# The * operator can also be used when calling functions and here it means the
# analogous thing. A variable prefaced by * when calling a function means that
# the variable contents should be extracted and used as positional arguments.

def add(x, y):
    return x + y

nums = [13, 7]
add(*nums)  # returns 20

# This example uses both methods at the same time:

def add(*args):
    result = 0
    for num in args:
        result += num
    return result

nums = [13, 7, 10, 40, 30]
add(*nums)  # returns 100

# You can have required and optional parameters. The required ones come first:

def print_more(required1, required2, *args):
    print('first argument is required:', required1)
    print('second argument is required:', required2)
    print('the rest:', args)

print_more('red', 'green')
# first argument is required: red
# second argument is required: green
# the rest: ()

print_more('red', 'green', 'one', 'two', 'three')
# first argument is required: red
# second argument is required: green
# the rest: ('one', 'two', 'three')


# Gathering Keyword Arguments - **kwargs
# -----------------------------------------------------------------------------
# ** does for dictionaries & key/value pairs exactly what * does for iterables
# and positional parameters demonstrated above. Here's it being used in the
# function definition:

def print_kwargs(**kwargs):
    print(kwargs, type(kwargs))

print_kwargs(x=1, y=2, z='hi')  # {'x': 1, 'y': 2, 'z': 'hi'} <class 'dict'>

# And here we're using it in the function call:

def add(x, y):
    return x + y

nums = {'x': 13, 'y': 7}
add(**nums)  # returns 20

# And here we're using it in both places"

def print_kwargs(**kwargs):
    for key in kwargs:
        print(key, 'en francais est', kwargs[key])

colours = {'red': 'rouge', 'yellow': 'jaune', 'green': 'vert', 'black': 'noir'}

print_kwargs(**colours)
# red en francais est rouge
# yellow en francais est jaune
# green en francais est vert
# black en francais est noir

# see also terminology.py for another example that feeds dictionary values
# to a class instance.


# Docstrings
# -----------------------------------------------------------------------------

def myfunction1(arg):
    '''This is where you can provide a brief description of the function'''
    print(arg)

def myfunction2(arg):
    '''
    The first line should be a short concise description.

    Followed by a space, and then the extended description.
    See documenting_naming.py or any of the python standard library modules
    for more information and examples.
    '''
    print(arg)

print(myfunction1.__doc__)
print(myfunction2.__doc__)


# Functions as Arguments
# -----------------------------------------------------------------------------
# Functions are objects, just like numbers, strings, tuples, lists,
# dictionaries, etc. They can be assigned to variables, used as arguments to
# other functions, or returned from other functions.

def answer():
    print(100)

def run_something(func):
    func()

run_something(answer)  # 100

# If the function you're passing as an arg requires its own args, just pass
# them following the function name:

def add_numbers(a, b):
    print(a + b)

def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)

run_something_with_args(add_numbers, 5, 10)  # 15

# An example with a variable number of arguments:

def sum_numbers(*args):
    print(sum(args))

def run_with_positional_args(func, *args):
    return func(*args)

run_with_positional_args(sum_numbers, 2, 3, 1, 4)  # 10


# Functions as attributes (& monkey patching)
# -----------------------------------------------------------------------------
# Since functions are objects, they can get set as callable attributes on other
# objects. In addition, you can add or change a function on an instantiated
# object. Consider this:

class A():
    def method(self):
        print("I'm from class A")

def function():
    print("I'm not from class A")

a = A()
a.method()
a.method = function
a.method()
# I'm from class A
# I'm not from class A

# This method of adding or replacing functions is often referred to as
# monkey-patching. Doing this kind of thing can cause situations that are
# difficult to debug. That being said, it does have its uses though. Often, it's
# used in automated testing. For example, if testing a client-server application,
# we may not want to actually connect to the server while testing it; this may
# result in accidental transfers of funds or test e-mails being sent to real
# people. Instead, we can set up our test code to replace some of the key
# methods on the object.

# Monkey-patching can also be used to fix bugs or add features in third-party
# code that we are interacting with, and does not behave quite the way we need
# it to. It should, however, be applied sparingly; it's almost always a
# "messy hack". Sometimes, though, it is the only way to adapt an existing
# library to suit our needs.


# Nested functions
# -----------------------------------------------------------------------------
# This is pretty straight forward. When we call the outer() function, it in
# turn calls the inner function. The inner function used a variable x that's
# defined in the outer functions namespace. The inner function looks for x
# first in its own local namespace, then failing that looks in the surrounding
# namespace. If it didn't find it there, it would check the global namespace
# next (see namespaces.py).

def outer():
    x = 1
    def inner():
        print(x)
    inner()

outer()  # 1


# Closure
# -----------------------------------------------------------------------------
# Consider that the namespace created for our functions are created from
# scratch each time the function is called and then destroyed when the
# function ends. According to this, the following should not work.

def outer():
    x = 1
    def inner():
        print(x)
    return inner

a = outer()
print(outer)  # <function outer at 0x1014a3510>
print(a)      # <function outer.<locals>.inner at 0x100762e18>

# At first glance, since we are returning inner from the outer function and
# assigning it to a new variable, that new variable should no longer have
# access to x because x only exists while the outer function is running.

a()  # 1

# But it does work because of a special feature called closure. An inner
# function knows the value of x that was passed in and remembers it. The line
# return inner returns this specialized copy of the inner function (but
# doesn't call it). That's a closure... a dynamically created function that
# remembers where it came from.

def outer(x):
    def inner():
        print(x)
    return inner

a = outer(2)
b = outer(3)

a()  # 2
b()  # 3

# From this example you can see that closures - the fact that functions
# remember their enclosing scope - can be used to build custom functions that
# have, essentially, a hard coded argument. We aren’t passing the numbers
# to our inner function but are building custom versions of our inner function
# that "remembers" what number it should print.


# lambda()
# -----------------------------------------------------------------------------
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

# Note that the lambda definition does not include a "return" statement –
# it always contains an expression which is returned. Also note that you can
# put a lambda definition anywhere a function is expected, and you don't have
# to assign it to a variable at all.
