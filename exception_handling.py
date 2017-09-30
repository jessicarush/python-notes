'''Exception Handling'''

# Exceptions -----------------------------------------------------------------

# An exception is a Python object that represents an error.

# There's two types of errors we can get: syntax errors and exceptions.
# Exceptions are a results of flaws in a programs logic or conditions we didn't
# predict. An example of an exception could be dividing by 0 or attempting to
# create a new database but there isn't enough space on the drive specified.

# When a Python script raises an exception, it must either handle the exception
# immediately otherwise the program terminates and quits (crashes).

# https://docs.python.org/3.4/library/exceptions.html
# https://www.tutorialspoint.com/python/python_exceptions.html

# Exception Handling ---------------------------------------------------------

# If you have some code that may raise an exception, you can defend your
# program by placing the code in a try: block. After the try: block, include an
# except: statement, followed by a block of code which handles the problem as
# elegantly as possible.

fruit = ['apple', 'orange', 'melon', 'pear', 'banana']
index = 5

try:
    fruit[index]
except:  # using except alone will catch ALL types of exceptions
    print('I need a number between 0 –', len(fruit)-1)

print("Program continues...")

# Choose which type of exceptions you want to handle -------------------------

# Generally speaking, you want to be more specific about which kinds of
# exceptions you're dealing with, so you can handle them in different ways.

import sys

while True:
    try:
        index = input('Enter a number [q to quit]: ')
        if index == 'q':
            break
        index = int(index)
        print(fruit[index])
    except IndexError:
        print('I need a number between 0 –', len(fruit)-1)
    except ValueError:
        print('I need an integer')
    except EOFError:  # ctrl D will raise this
        print('Goodbye')
        sys.exit(1)
    except Exception:
        print('Something else broke')

print("Program continues...")

# Group exceptions if you want -----------------------------------------------

while True:
    try:
        index = input('Enter a number [q to quit]: ')
        if index == 'q':
            break
        index = int(index)
        print(fruit[index])
    except (IndexError, ValueError):
        print('I need an integer between 0 –', len(fruit)-1)
    except (EOFError, Exception):
        print('Goodbye')
        sys.exit(1)

print("Program continues...")

# Else and finally -----------------------------------------------------------

# these are optional clauses that can be added to a try statement.

# The else clause is executed only if the code in the try block completes and
# doesn't raise an exception. It should come after any except clauses.

# The finally clause must come after all other clauses. It will execute
# no matter what happens (even if sys.exit(0) is executed in an except). this
# makes the finally clause an ideal place to perform any necessary clean-up
# like closing any open files, database connections or cursors.

while True:
    try:
        index = input('Enter a number [q to quit]: ')
        if index == 'q':
            break
        index = int(index)
        print(fruit[index])
    except (IndexError, ValueError):
        print('I need an integer between 0 –', len(fruit)-1)
    except (EOFError, Exception):
        print('Goodbye')
        sys.exit(1)
    else:
        print('Done!')
    finally:
        print('The finally clause executes no matter what.')

# Another example with separate try clauses ----------------------------------

print('Enter two numbers.')

def get_inputs(arg):
    while True:
        try:
            x = input('{} number: '.format(arg))
            x = int(x)
            return x
        except ValueError:
            print('I need an integer please')
        except EOFError:
            print('Goodbye')
            sys.exit(1)
        finally:
            print('The finally clause executes no matter what')

a = get_inputs('first')
b = get_inputs('second')

try:
    print('{} / {} = {}'.format(a, b, a / b))
except ZeroDivisionError:
    print("You can't divide by zero")
else:
    print('Done!')

# Store the Exception in a variable with 'as'---------------------------------

while True:
    try:
        value = input('Position [q to quit]: ')
        if value == 'q':
            break
        position = int(value)
        print(fruit[position])
    except IndexError as error:
        print(error, '–', position)  # list index out of range – 6
    except Exception as other:
        print('Something else broke:', other)  # Something else broke:
                                               # invalid literal for int()
                                               # with base 10: 'g'

# Raise an Exception ---------------------------------------------------------

# The above example simply prints out the stored exception but you can also
# choose to "raise" it when and if you want to. To compare, lets start with
# handling the exception:

def sum(numbers):
    total = 0
    for num in numbers:
        try:
            total += num
            print(total)
        except TypeError:
            print('non integer ignored')

testing = [2, 6, 3, 'blerk', 8, 11 ]
sum(testing)

# The above will return:
# 2
# 8
# 11
# non integer ignored
# 19
# 30

# The following will still handle the exception and complete the iteration
# but when it's done it will raise the exception and terminate the program.

def sum(numbers):
    total = 0
    for num in numbers:
        try:
            total += num
            print(total)
        except TypeError as error:
            print('non integer skipped over')
            problem = error
    if problem:
        raise problem


testing = [2, 6, 3, 'blerk', 8, 11 ]
sum(testing)

# Here's the output:
# 2
# 8
# 11
# non integer skipped over
# 19
# 30
# Traceback (most recent call last):
#   File "test.py", line 29, in <module>
#     sum(testing)
#   File "test.py", line 25, in sum
#     raise problem
#   File "test.py", line 19, in sum
#     total += num
# TypeError: unsupported operand type(s) for +=: 'int' and 'str'

# Using Raise can be helpful for testing exception handling. Lets say you've
# written code to handle a MemoryError, ConnectionError or OSError where it
# may be difficult to simulate the problem in order to test it. In this case
# you could manually raise the error as a way of testing the handling.

# Create your own exceptions to raise ----------------------------------------

# An exception is a class: a child of the base class Exception.

class UppercaseException(Exception):
    pass

words = ['one', 'two', 'THREE', 'four']

for word in words:
    if word.isupper():
        raise UppercaseException(word)

# More in depth example ------------------------------------------------------
