'''Built-in Functions'''
# ----------------------------------------------------------------------------
# abs()
#
#
# ----------------------------------------------------------------------------
# all()
#
#
# ----------------------------------------------------------------------------
# any()
#
#
# ----------------------------------------------------------------------------
# ascii()
# return a string containing a printable representation of an object but
# escape the non-ASCII characters. Useful for finding out the unicode:

print(ascii('café'))
print('caf\xe9')

# ----------------------------------------------------------------------------
# bin()
#
#
# ----------------------------------------------------------------------------
# bool()
# see reflection.py
# converts a value to Boolean (True or False)
# ----------------------------------------------------------------------------
# bytearray()
# see binary_data.py
# returns an array of bytes (mutable)
# ----------------------------------------------------------------------------
# bytes()
# see binary_data.py
# returns a bytes object (immmutable)
# ----------------------------------------------------------------------------
# callable()
# see reflection.py
# returns True if the object passed appears callable

def test():
    pass

callable(test)  #True
# ----------------------------------------------------------------------------
# chr()
#
#
# ----------------------------------------------------------------------------
# classmethod()
#
#
# ----------------------------------------------------------------------------
# compile()
# see regular_expressions.py
# returns a Python code object from the source string
# ----------------------------------------------------------------------------
# complex()
#
#
# ----------------------------------------------------------------------------
# delattr()
#
#
# ----------------------------------------------------------------------------
# dict()
# see dictionaries.py
# creates a dictionary object
# ----------------------------------------------------------------------------
# dir()
# tries to return a list of valid attributes of the object

# show the names in the local module namespace:
print(dir())

 # show all the Built-in things:
for m in dir(__builtins__):
    print(m)

# show the names in the random module:
import random
print(dir(random))

# print just the useful ones:
for obj in dir(random.Random):
    if obj[0] != '_':
        print(obj)
# ----------------------------------------------------------------------------
# divmod()
# see operators.py
# takes two numbers and returns a tuple of their quotient and remainder
# ----------------------------------------------------------------------------
# enumerate()
# adds counter to an iterable and returns it. In this example it takes apart a
# list and feeds each item to the for loop, adding a number to each item.

colours = ['red', 'cyan', 'yellow', 'green']

for colour in enumerate(colours):
    print(colour)

for number, colour in enumerate(colours, 1): # starts the numbering at 1
    print(number, colour)
# ----------------------------------------------------------------------------
# eval()
# see files_read_write.py
# runs the python code (which is passed as an argument) within the program
# ----------------------------------------------------------------------------
# exec()
#
#
# ----------------------------------------------------------------------------
# filter()
#
#
# ----------------------------------------------------------------------------
# float()
# see data_types.py
# returns a floating point number from a number or a string
# ----------------------------------------------------------------------------
# format()
# see formatting.py
# returns a formatted representation of the given value
# ----------------------------------------------------------------------------
# frozenset()
# see sets.py
# creates an immutable set
# ----------------------------------------------------------------------------
# getattr()
# see reflection.py
# returns the value of an attribute of an object, given the attribute name,
# but also lets you provide a default value to avoid raising an errors:
# ----------------------------------------------------------------------------
# globals()
# see namespaces.py
# returns a dictionary of the current global symbol table (variable names,
# methods, classes, etc)
# ----------------------------------------------------------------------------
# hasattr()
#
#
# ----------------------------------------------------------------------------
# hash()
#
#
# ----------------------------------------------------------------------------
# help()
# calls the built-in Python help system. If you have documented your code
# properly (docstrings), these can be seen with help() too. You can get help
# on individual functions as well:

help(hash)

import random
help(random.choice)

import documenting_naming
help(documenting_naming)
# ----------------------------------------------------------------------------
# hex()
# see binary_data.py
# convert itegers to hexadecimal (base 16)
# ----------------------------------------------------------------------------
# id()
# see reflection.py
# returns the identity (unique integer) of an object
# ----------------------------------------------------------------------------
# input()
# see while_loops.py
# returns a string uf user input
# ----------------------------------------------------------------------------
# int()
# see data_types.py
# returns and integer object from a number or string
# ----------------------------------------------------------------------------
# isinstance()
# see reflection.py
# checks if the object (first argument) is an instance or subclass of the
# (second argument).
# ----------------------------------------------------------------------------
# issubclass()
#
#
# ----------------------------------------------------------------------------
# iter()
# see iterating_with_for.py
# returns an iterator for the given object
# ----------------------------------------------------------------------------
# len()
# see noSQL_datastores.py
# returns the number of items (length) of an object
# ----------------------------------------------------------------------------
# list()
# see lists.py
# creates a list object
# ----------------------------------------------------------------------------
# locals()
# see namespaces.py
# returns a dictionary of the current local symbol table (variable names,
# methods, classes, etc)
# ----------------------------------------------------------------------------
# map()
#
#
# ----------------------------------------------------------------------------
# max()
#
#
# ----------------------------------------------------------------------------
# memoryview()
#
#
# ----------------------------------------------------------------------------
# min()
#
#
# ----------------------------------------------------------------------------
# next()
# see iterating_with_for.py and generators.py
# returns the next item from the iterator
# ----------------------------------------------------------------------------
# object()
#
#
# ----------------------------------------------------------------------------
# oct()
# see binary_data.py
# convert itegers to octal (base 8)
# ----------------------------------------------------------------------------
# open()
# see files_read_write.py
# opens a file and returns a corresponding file object
# ----------------------------------------------------------------------------
# ord()
#
#
# ----------------------------------------------------------------------------
# pow()
#
#
# ----------------------------------------------------------------------------
# print()
# Remember there are additional args you can provide to print.

# remove the default line break at the end by specifying end=''
for i in range(0, 6):
    print(i, end='')

# add a separator if printing more than one thing
for i in range(0, 6):
    print(i, i, sep='.')

# prints to a file if you've got one open
for i in range(0, 6):
    print(i, file=fileobject)
# ----------------------------------------------------------------------------
# property()
#
#
# ----------------------------------------------------------------------------
# range()
# returns an immutable sequence object of integers - when using range() alone,
# you're creating a range object:

numbers = range(0, 100)
print(type(numbers)) # class 'range'
print(numbers[0:50:2] == range(0,50,2)) # True
# ----------------------------------------------------------------------------
# repr()
# returns a printable representation of the given object:

now = datetime.datetime.utcnow()
print(repr(now))  # datetime.datetime(2017, 9, 5, 18, 23, 30, 607281)
# ----------------------------------------------------------------------------
# reversed()
#
#
# ----------------------------------------------------------------------------
# round()
#
#
# ----------------------------------------------------------------------------
# set()
# see sets.py
# create a set object
# ----------------------------------------------------------------------------
# setattr()
#
#
# ----------------------------------------------------------------------------
# slice()
#
#
# ----------------------------------------------------------------------------
# sorted()
# see dictionaries.py, lists.py, sets.py
# returns a sorted list from the given iterable
# ----------------------------------------------------------------------------
# staticmethod()
#
#
# ----------------------------------------------------------------------------
# str()
# see strings.py
# returns a string object
# ----------------------------------------------------------------------------
# sum()
#
#
# ----------------------------------------------------------------------------
# super()
#
#
# ----------------------------------------------------------------------------
# tuple()
# see tuples.py
# returns a tuple object
# ----------------------------------------------------------------------------
# type()
# see reflection.py
# if a single object is passed, returns type of the given object
# ----------------------------------------------------------------------------
# vars()
#
#
# ----------------------------------------------------------------------------
# zip()
# see zip_function.py
# take iterables (can be zero or more), makes iterator that aggregates
# elements based on the iterables passed, and returns an iterator of tuples
# ----------------------------------------------------------------------------
#__import__()
# see import.py
# This is an advanced function that is called by the import statement.
