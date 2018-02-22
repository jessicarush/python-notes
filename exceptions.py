'''Exceptions'''


# An exception is a Python object that represents an error.

# There's two types of errors we can get: syntax errors and exceptions.
# Technically a syntax error is a type of exception but let's just say while
# syntax errors are self explanatory, 'Exceptions' are a result of flaws in a
# programs logic or conditions we didn't predict. An example of an exception
# could be dividing by 0 (ZeroDivisionError) or passing an integer to a method
# that only accepts strings (ValueError) or attempting to create a new database
# but there isn't enough space on the drive specified.

# When a Python script "raises an exception", it must "handle" the exception
# immediately or the program terminates (crashes).

# https://docs.python.org/3.4/library/exceptions.html

# In terms of class hierarchy, most exceptions are subclasses of the
# Exception class. Exception itself actually inherits from a class called
# BaseException. SystemExit and KeyboardInterrupt, are the only two special
# exceptions that derive directly from BaseException instead of Exception.
# Generally speaking, this is so that we can, if we want, specify all
# exceptions except these two special ones by explicitly saying 'Exception'.

'''
BaseException <--- Exception <--- All Other Exceptions
                   SystemExit
                   KeyboardInterrupt
'''


# Raise an Exception
# -----------------------------------------------------------------------------
# This example creates a class that adds items to a list only if they are
# 4-digit integers. We're raising two exception objects using built-in classes,
# but we could just as easily write our own. The optional messages help in
# terms of outputting useful error information.

class FourDigitInts(list):
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError('Only integers can be added.')
        if len(str(integer)) != 4:
            raise ValueError('Only 4-digit numbers can be added.')
        super().append(integer)

f = FourDigitInts()
f.append(5678)
# f.append('5678')
# f.append(56)


# Handling Exceptions
# -----------------------------------------------------------------------------
# If you have some code that may raise an exception, you 'handle' the exception
# by placing the code in a try: block. After the try: block, include an
# except: statement, followed by a block of code which handles the problem as
# elegantly as possible.

# Note that when we use the except: clause without specifying any type of
# exception, it will catch all subclasses of BaseException; which is to say,
# it will catch all exceptions, including the two special ones. Since we almost
# always want these to get special treatment, it is unwise to use the except:
# statement without arguments. If you want to catch all exceptions other than
# SystemExit and KeyboardInterrupt, explicitly catch Exception.

fruit = ['apple', 'orange', 'melon', 'pear', 'banana']
index = 5

try:
    fruit[index]
except Exception:
    print('Caught an exception. Need an index between 0 –', len(fruit)-1)

print("Program continues...")


# Choose which type of exceptions you want to handle
# -----------------------------------------------------------------------------
# Generally speaking, you want to be more specific about which kinds of
# exceptions you're dealing with, so you can handle them in different ways.
# Note you can also group exceptions if it makes sense to do so:

import sys

print('\ntry, except example:')

while True:
    try:
        index = input('Enter a number [q to quit]: ')
        if index.lower() == 'q':
            break
        print(fruit[int(index)])
    except IndexError:
        print('I need a number between 0 –', len(fruit)-1)
    except ValueError:
        print('I need an integer')
    except (EOFError, KeyboardInterrupt):  # ctrl + D or C
        print('\nGoodbye')
        sys.exit(1)
    except Exception:
        print('Something else broke')

print("Program continues...")


# Else and finally
# -----------------------------------------------------------------------------
# These are optional clauses that can be added to a try statement.

# The else clause is executed only if the code in the try block completes and
# doesn't raise an exception. It should come after any except clauses.

# The finally clause must come after all other clauses. It will execute
# no matter what happens (even if sys.exit(0) is executed in an except). this
# makes the finally clause an ideal place to perform any necessary clean-up
# like closing any open files, database connections or cursors.

print('\ntry, except, else, finally example:')

while True:
    try:
        index = input('Enter a number [q to quit]: ')
        if index.lower() == 'q':
            break
        print(fruit[int(index)])
    except (IndexError, ValueError):
        print('I need an integer between 0 –', len(fruit)-1)
    except (EOFError, Exception):
        print('\nGoodbye')
        sys.exit(1)
    else:
        print('The else clause executes if no exception was raised.')
    finally:
        print('The finally clause executes no matter what.')


# The finally clause is also very important when we execute a return statement
# from inside a try or else clause. The finally handle will be executed before
# the value is returned. That being said, if the try block contains a
# successful return, continue or break statement, the else clause will NOT run.

def execution_order1():
    try:
        print('Try')
        return 'Return'
    except Exception:
        print('Except')
    else:
        print('Else')
    finally:
        print('Finally')

print('\nExecution order demo 1:')
e = execution_order1()
print(e)
# Execution order demo 1:
# Try
# Finally
# Return

def execution_order2():
    try:
        print('Try')
    except Exception:
        print('Except')
    else:
        print('Else (executes if no exception raised AND no return, '
              'continue or break statement in the try clause.)')
        return 'Return'
    finally:
        print('Finally')

print('\nExecution order demo 2:')
e = execution_order2()
print(e)
# Try
# Else (executes if no exception raised AND no return, continue or break ...)
# Finally
# Return


# Another example with handlers
# -----------------------------------------------------------------------------

print('\nEnter two numbers.')

def get_inputs(arg):
    while True:
        try:
            x = input(f'{arg} number: ')
            return int(x)
        except ValueError:
            print('I need an integer.')
        except (EOFError, KeyboardInterrupt):
            print('\nGoodbye')
            sys.exit(1)

a = get_inputs('first')
b = get_inputs('second')


def divide_inputs(x, y):
    try:
        print(f'{x} \u00F7 {y} = {x / y}')
    except ZeroDivisionError:
        print("You can't divide by zero, moving on...")

divide_inputs(a, b)


# Store the Exception object in a variable with 'as'
# -----------------------------------------------------------------------------
# Sometimes, when we catch an exception, we need a reference to the Exception
# object itself. This most often happens when we define our own exceptions with
# custom arguments, but can also be relevant with standard exceptions. If we
# define our own exception class, we can even call custom methods on it when we
# catch it. Use the as keyword for capturing an exception as a variable:

print('\nStoring Exception object in a variable:')

while True:
    try:
        index = input('Position [q to quit]: ')
        if index.lower() == 'q':
            break
        print(fruit[int(index)])
    except IndexError as ie:
        print(ie, '–', index)
        # list index out of range – 6
        print(f'The exception arguments were: {ie.args}')
        # The exception arguments were: ('list index out of range',)
    except Exception as other:
        print('Something else broke:', other)
        # Something else broke: invalid literal for int() with base 10: 'g'


# Handle, then Raise an Exception
# -----------------------------------------------------------------------------
# In the examples above we've handles the exceptions. Sometimes though, you
# may want to be alerted to a problem but let your code finish first.
# Compare the following:

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
            print('non integer ignored')
            problem = error
    # if problem:
    #     raise problem


testing = [2, 6, 3, 'blerk', 8, 11 ]
sum(testing)
# 2
# 8
# 11
# non integer ignored
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

# Using Raise can also be helpful for testing exception handling. Lets say
# you've written code to handle a MemoryError, ConnectionError or OSError where
# it may be difficult to simulate the problem in order to test it. In this case
# you could manually raise the error as a way of testing the handling.


# Create your own exceptions
# -----------------------------------------------------------------------------
# More often than anything else, raise is used in conjunction with writing
# your own exceptions in an effort to catch potential problems with your code.
# Ideally, when your exception ends up being raised, it's a signal for you to
# modify your code where necessary. The name of the new class is usually
# designed to communicate what went wrong, and we can provide arbitrary
# arguments in the initializer to include additional information.

# An exception is a class: a child of the base class Exception.

class InvalidWithdrawal(Exception):
    def __init__(self, balance, amount):
        super().__init__(f'Account does not have {amount}')
        self.balance = balance
        self.amount = amount

    def short(self):
        return self.amount - self.balance

try:
    raise InvalidWithdrawal(balance=10, amount=50)
except InvalidWithdrawal as e:
    print(f"Sorry, your withdrawal is more than your balance by ${e.short()}")


# Exception vs. if statements
# -----------------------------------------------------------------------------
# Consider the following two examples. In many situations using a try/except
# or a if/else will produce identical results.

def index_with_exception(x, group):
    try:
        print(f'The value at index {x} is: {group[x]}')
    except IndexError:
        print(f'There is no index {x}.')


def index_with_if(x, group):
    if x < len(group):
        print(f'The value at index {x} is: {group[x]}')
    else:
        print(f'There is no index {x}.')

# But we shouldn't do this. There are too many possibilities for us to miss
# checking something in our if statement. For example, lists support negative
# indexing. If we forget to account for that, our program crashes.

index_with_exception(2, fruit)
index_with_exception(6, fruit)
index_with_exception(-2, fruit)
index_with_exception(-6, fruit)

index_with_if(2, fruit)
index_with_if(6, fruit)
index_with_if(-2, fruit)
# index_with_if(-6, fruit)  # crash

# Not only does our exception function do a better job of handling all indexes,
# exception syntax is also effective for flow control. Like an if statement,
# exceptions can be used for decision making, branching, and message passing.

# Imagine an inventory application. When a customer makes a purchase, the item
# can either be available, in which case the item is removed from inventory,
# or it might be out of stock. We can raise OutOfStockException and use the
# try statement to direct program flow control. In addition, if we want to make
# sure we don't sell the same item to two different customers, we can 'lock'
# items to ensure only one person can updates it at a time.

class Inventory:
    def lock(self, item):
        '''Select the item that is going to be manipulated.
        This method will lock the item so nobody else can manipulate the
        inventory until it's returned. This prevents selling the same item
        to two different customers.'''
        pass

    def unlock(self, item):
        '''Release the item so other customers can access it.'''
        pass

    def purchase(self, item):
        '''If the item is not locked, raise an exception.
        If the item does not exist: raise an exception.
        If the item is currently out of stock: raise an exception.
        If the item is available:
        subtract one item and return the number of items left.'''
        pass

item = 'widget'
inv = Inventory()
inv.lock(item)
try:
    num_left = inv.purchase(item)
except InvalidItemType:
    print(f"Sorry, we don't sell {item}")
except OutOfStock:
    print(f"Sorry, that item is out of stock.")
else:
    print(f"Purchase complete. There are {num_left} {item}s left.")
finally:
    inv.unlock(item)

# Pay attention to how all the possible exception handling clauses are used to
# ensure the correct actions happen at the correct time. This code could be
# written with an if...elif...else structure, but it wouldn't be as easy to
# read or maintain. We can also use exceptions to pass messages between
# different methods. For example, the OutOfStock exception could provide a
# method that instructs the inventory object to reorder or backorder an item.

# Using exceptions for flow control can make for some handy program designs.
# The important thing to take from this is that exceptions are not a bad thing
# that we should try to avoid. Having an exception occur does not mean that you
# should have prevented this exceptional circumstance from happening. Rather,
# it is just a powerful way to communicate information between two sections of
# code that may not be directly calling each other.


# Summary
# -----------------------------------------------------------------------------
# Use try/finally when you want exceptions to propagate up but you also want
# to run cleanup code when exceptions occur. For example closing a file,
# rolling back a database or whatever.

fob = open('data/example.txt')
try:
    data = fob.read()
finally:
    fob.close()

# In this example if an exception happens while reading, the finally block is
# guaranteed to run. Note the open line is not inside the try block because if
# there's a problem opening, then we don't need to close().

# Use try/except/else blocks to make it clear which exceptions swill be handled
# by your code and which exceptions will propagate up. The else block can be
# used to perform additional actions after a successful try block but before
# the common cleanup in a finally block.

# There are many reasons for defining our own exceptions. It is often useful
# to add information to the exception or log it in some way. But the utility
# of custom exceptions truly comes to light when creating a framework, library,
# or API that is intended for access by other programmers. In that case, be
# careful to ensure your code is raising exceptions that make sense. Clearly
# describe what went on. The client programmer should easily see how to fix the
# error (if it reflects a bug in their code) or handle the exception (if it's
# a situation they need to be made aware of).
