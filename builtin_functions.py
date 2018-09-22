'''Built-in Functions'''

for item in dir(__builtins__):
    print(item)


# abs()
# -----------------------------------------------------------------------------
# returns the absolute value of a given number. If the number is a complex
# number, abs() returns its magnitude. It takes one parameter which can be an
# integer, float, or complex number:

integer = -20
print('Absolute value of -20 is:', abs(integer))  # 20

floating = -30.33
print('Absolute value of -30.33 is:', abs(floating))  # 30.33

complex_num = (3 - 4j)
print('Magnitude of 3 - 4j is:', abs(complex_num))  # 5.0


# all()
# -----------------------------------------------------------------------------
# returns True when ALL elements in the given iterable are true. If not, it
# returns False. It takes one parameter, which is an iterable (list, tuple,
# dictionary, etc.)

numbers = [1, 3, 4, 5]          # True
print(all(numbers))

numbers = [1, 3, False, 4, 5]   # False
print(all(numbers))

numbers = [0, 1, 3, 4, 5]       # False
print(all(numbers))

numbers = []                    # True
print(all(numbers))


# any()
# -----------------------------------------------------------------------------
# returns True if ANY element of an iterable is true. If not, it returns False.

numbers = [1, 3, 4, 5]          # True
print(any(numbers))

numbers = [1, 3, False, 4, 5]   # True
print(any(numbers))

numbers = [0, 1, 3, 4, 5]       # True
print(all(numbers))

numbers = []                    # False
print(any(numbers))

# This can be used to see check if anything from one iterable is in another.
# FYI, this example also uses a generator comprehension:

animals = ['fox', 'snake', 'owl', 'cat']
codewords = ['red box', 'cracked buttons', 'white owl', 'giant cactus']

for words in codewords:
    if any(animal in words for animal in animals):
        print('There is an animal in the words')

# The long way without any():
for words in codewords:
    for animal in animals:
        if animal in words:
            print('4. There is an animal in the words')


# ascii()
# -----------------------------------------------------------------------------
# return a string containing a printable representation of an object but
# escape the non-ASCII characters. Useful for finding out the unicode:

print(ascii('café'))  # 'caf\xe9'
print('caf\xe9')      # café


# bin()
# -----------------------------------------------------------------------------
# converts and returns the binary equivalent string of a given integer. It
# takes one parameter, in integer. If not an integer, you can implement the
# __index__() method to return an integer.

number = 5
print('The binary equivalent of 5 is:', bin(number))  # 0b101

class Inventory:
    apple = 1
    orange = 2
    grapes = 2
    def __index__(self):
        return self.apple + self.orange + self.grapes

print('The binary equivalent of Inventory is:', bin(Inventory()))  # 0b101


# bool()
# -----------------------------------------------------------------------------
# see reflection.py
# converts a value to Boolean (True or False)

#
# bytearray()
# -----------------------------------------------------------------------------
# see binary_data.py
# returns an array of bytes (mutable)


# bytes()
# -----------------------------------------------------------------------------
# see binary_data.py
# returns a bytes object (immmutable)


# callable()
# -----------------------------------------------------------------------------
# see reflection.py
# returns True if the object passed appears callable

def test():
    pass

callable(test)  #True


# chr()
# -----------------------------------------------------------------------------
# returns a character (string) from an integer. The integer represents the
# unicode code point of the character. The valid range of the integer is from
# 0 through 1,114,111. The opposite method of chr() is ord()

print(chr(45))     # -
print(chr(454))    # ǆ
print(chr(4540))   # ᆼ
print(chr(45400))  # 녘


# classmethod()
# -----------------------------------------------------------------------------
# see classes.py
# The classmethod function returns a class method for a given function. This
# method is considered un-Pythonic so in newer Python versions, use the
# @classmethod decorator instead.


# compile()
# -----------------------------------------------------------------------------
# see regular_expressions.py
# returns a Python code object from the source string


# complex()
# -----------------------------------------------------------------------------
# returns a complex number when real and imaginary parameters are provided, or
# it converts a string to a complex number. In general, the two parameters:
# real - real part. If real is omitted, it defaults to 0.
# imag - imaginary part. If imag is omitted, it default to 0.
# If the first parameter passed to this method is a string, it will be
# interpreted as a complex number. In this case, second parameter shouldn't
# be passed. The string passed should be in the form real+imagj or real+imagJ

print(complex())        # 0j
print(complex(1))       # (1+0j)
print(complex(2, -3))   # (2-3j)
print(complex('5-9j'))  # (5-9j)


# delattr()
# -----------------------------------------------------------------------------
# deletes an attribute from the object (if the object allows it).
# delattr(object, name).
# object - the object from which name attribute is to be removed
# name -  a string which must be the name of the attribute to be removed

class Coordinate:
    x = 10
    y = -5
    z = 0

point1 = Coordinate()

print(dir(point1)) # [..., 'x', 'y', 'z']

delattr(Coordinate, 'z')

print(dir(point1)) # [..., 'x', 'y']


# dict()
# -----------------------------------------------------------------------------
# see dictionaries.py
# creates a dictionary object


# dir()
# -----------------------------------------------------------------------------
# see also resources.py
# tries to return a list of valid attributes of the object

# show the names in the local module namespace:
print(dir())

# show all the Built-ins:
for m in dir(__builtins__):
    print(m)

# show all the methods available for lists:
print(dir(list))

# show the names in the random module:
import random
print(dir(random))

# print just the useful ones:
for obj in dir(random.Random):
    if obj[0] != '_':
        print(obj)


# divmod()
# -----------------------------------------------------------------------------
# see operators.py
# takes two numbers and returns a tuple of their quotient and remainder


# enumerate()
# -----------------------------------------------------------------------------
# adds counter to an iterable and returns it. In this example it takes apart a
# list and feeds each item to the for loop, adding a number to each item.

colours = ['red', 'cyan', 'yellow', 'green']

for colour in enumerate(colours):
    print(colour)
# (0, 'red')
# (1, 'cyan')
# (2, 'yellow')
# (3, 'green')

# This example uses enumerate to output it's own code with line numbers.
# The second argument passed to enumerate starts the numbering at 1 instead
# of 0. The output below assumes the following snippet is in a file by itself.

import sys
filename = sys.argv[0]

with open(filename) as file:
    for index, line in enumerate(file, 1):
        print("{}: {}".format(index, line), end='')
# 1:  import sys
# 2:  filename = sys.argv[0]
# 3:
# 4:  with open(filename) as file:
# 5:     for index, line in enumerate(file, 1):
# 6:         print("{}:  {}".format(index, line), end='')

# There's a nice example of how enumerate is used with a csv file – to get the
# indexes listed with all the headers so we know which indexes of data we're
# looking for: matplotlib_csv_example.py


# eval()
# -----------------------------------------------------------------------------
# see files_read_write.py
# runs the python code (which is passed as an argument) within the program


# exec()
# -----------------------------------------------------------------------------
# Is used to execute a python statement that is stored in a string or file:

# exec(object, globals, locals)
# – The object is either a string or a code object
# – globals (optional) - a dictionary
# – locals (optional)- a mapping object (dictionary is the standard)

program = 'a = 5\nb=10\nprint("Sum =", a + b)'
exec(program)

program = input('Enter a program:') # for num in range(1, 10): print(num)
exec(program)


# filter()
# -----------------------------------------------------------------------------
# In simple words, the filter() method filters a given iterable with the help
# of a function that tests each element in the iterable to be true or not.
# You can use any function, but it must return either true or false.

# filter(function, iterable)

# The filter() method returns an iterable filter object of the elements that
# passed the function check.

example = [0, 1, '0', 'a', True, False]

filtered_example = filter(None, example)
print(filtered_example)    # <filter object at 0x101a84978>

filtered_example = list(filter(None, example))
print(filtered_example)    # [1, '0', 'a', True]

# In the above example the function is None. In the following, we'll create
# our own function that will return either True or False:

letters = ['a', 'b', 'd', 'e', 'i', 'j', 'k', 's', 'o']

def check_vowels(item):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if item in vowels:
        return True
    return False

filtered_letters = list(filter(check_vowels, letters))
print(filtered_letters)  # ['a', 'e', 'i', 'o']

# Using a lambda function:

data = ['one', 'two', 'n/a', 'three']

filtered_data = list(filter(lambda x: x != 'n/a', data))
print(filtered_data)  # ['one', 'two', 'three']

# Often, filters can be written as list comprehensions instead.

# if the function arg is None it's equivalent to:
# [element for element in iterable if element]

# if a function is defined it's equivalent to:
# [element for element in iterable if function(element)]

# Here's the above three examples written as list comprehensions:

listcomp_example = [x for x in example if x != False]
print(listcomp_example)  # [1, '0', 'a', True]

listcomp_letters = [x for x in letters if check_vowels(x)]
print(listcomp_letters)  # ['a', 'e', 'i', 'o']

listcomp_data = [x for x in data if x != 'n/a']
print(listcomp_data)  # ['one', 'two', 'three']

# The concept of list comprehensions is more popular in Python but doesn't
# exist in many other languages. Those languages will use something more like
# the filter method.


# float()
# -----------------------------------------------------------------------------
# see data_types.py
# returns a floating point number from a number or a string


# format()
# -----------------------------------------------------------------------------
# see formatting.py
# returns a formatted representation of the given value


# frozenset()
# -----------------------------------------------------------------------------
# see sets.py
# creates an immutable set


# getattr()
# -----------------------------------------------------------------------------
# see reflection.py
# returns the value of an attribute of an object, given the attribute name,
# but also lets you provide a default value to avoid raising an errors.


# globals()
# -----------------------------------------------------------------------------
# see namespaces.py
# returns a dictionary of the current global symbol table (variable names,
# methods, classes, etc)


# hasattr()
# -----------------------------------------------------------------------------
# returns true if an object has the given named attribute and false if not.

# hasattr(object, name)

class Person():
    age = 23
    name = 'Raja'

person = Person()

print('Person has age?:', hasattr(person, 'age'))        # True
print('Person has salary?:', hasattr(person, 'salary'))  # False


# hash()
# -----------------------------------------------------------------------------
# The hash(object) method returns the hash value of an object if it has one.
# A hash is a number value created for something based on an algorithm.
# Different systems use different algorithms. Hash values can be used to store
# passwords or to more easily compare large sets of data (below the hash value
# is longer than the given value, but normally the given value would be larger
# than the hash value).

# hash for integer unchanged
print('Hash for 181 is:', hash(181))  # 181

# hash for decimal
print('Hash for 181.23 is:', hash(181.23))  # 530343892119126197

# hash for string
print('Hash for Python is:', hash('Python'))  # 2230730083538390373

# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')
print(hash(vowels))  # -695778075465126279


# help()
# -----------------------------------------------------------------------------
# see resources.py
# calls the built-in Python help system. If you have documented your code
# properly (docstrings), these can be seen with help() too. You can get help
# on individual functions as well:

help(hash)

import random
help(random.choice)

import documenting_naming
help(documenting_naming)


# hex()
# -----------------------------------------------------------------------------
# see binary_data.py
# convert integers to hexadecimal (base 16)


# id()
# -----------------------------------------------------------------------------
# see reflection.py
# returns the identity (unique integer) of an object


# input()
# -----------------------------------------------------------------------------
# see while_loops.py
# returns a string of user input


# int()
# -----------------------------------------------------------------------------
# see data_types.py
# returns and integer object from a number or string


# isinstance()
# -----------------------------------------------------------------------------
# see reflection.py
# checks if the object (first argument) is an instance or subclass of the
# (second argument).


# issubclass()
# -----------------------------------------------------------------------------
# see reflection.py
# checks if the object (first argument) is a subclass of (second argument).


# iter()
# -----------------------------------------------------------------------------
# see iterating_with_for.py
# returns an iterator for the given object


# len()
# -----------------------------------------------------------------------------
# see noSQL_datastores.py
# returns the number of items (length) of an object


# list()
# -----------------------------------------------------------------------------
# see lists.py
# creates a list object


# locals()
# -----------------------------------------------------------------------------
# see namespaces.py
# returns a dictionary of the current local symbol table (variable names,
# methods, classes, etc)


# map()
# -----------------------------------------------------------------------------
# The map() function applies a given function to each item of an iterable and
# returns a list of the results.

def square(n):
    return n * n

numbers = (1, 2, 3, 4)
result = map(square, numbers)

print(result)       # <map object at 0x101185f28>
print(set(result))  # {16, 1, 4, 9}

# That being said, you could also use generator comprehensions for this:
# (expression for item in iterable) - More Pythonic!

numbers = [1, 2, 3, 4]
squares = (x ** 2 for x in numbers)

print(squares)       # <generator object <genexpr> at 0x101553e08>
print(set(squares))  # {16, 1, 4, 9}


# max()
# -----------------------------------------------------------------------------
# The max() method returns the largest element in an iterable or largest of
# two or more parameters.

num1 = [23, 456, 20]
num2 = [6, 66, 899, 790]
num3 = [24, 4, 12, 56, 285]

print(max(num1))  # 456

# You can also use a 'key' function where each argument is passed, and
# comparison is performed based on its return value.

print(max(num1, num2, num3, key=len))  # [24, 4, 12, 56, 285]

# This example will add up the numbers in each list and return the list with
# the max result.

def add(numlist):
    total = 0
    for num in numlist:
        total += num
    return total

print(max(num1, num2, num3, key=add))  # [6, 66, 899, 790]


# memoryview()
# -----------------------------------------------------------------------------
# A buffer protocol provides a way to access the internal data of an object.
# This internal data is a memory array or a buffer. Buffer protocol allows one
# object to expose its internal data (buffers) and another to access those
# buffers without intermediate copying. Memory view is a safe way to expose the
# buffer protocol in Python. It allows you to access the internal buffers of an
# object by creating a memory view object.

# Whenever we perform some action on an object (call a function of an object,
# slice an list), Python needs to create a copy of the object. If we have a
# large data object to work with (eg. binary data of an image), we would
# create copies of huge chunks of data, which serves almost no use.

# Using buffer protocol, we can give another object access to use/modify the
# large data without copying it. This makes the program use less memory and
# increases the execution speed.

# The memory view objects are created using the syntax: memoryview(obj)

# The object passed in must support buffer protocol (eg. bytes, bytearray)

example = bytearray('Hello', 'utf-8')
mv = memoryview(example)

# access memory view's index
print(mv[0])                      # 72

# create byte from memory view
print(bytes(mv[0:3]))             # b'Hel'

# create list from memory view
print(list(mv[0:3]))              # [72, 101, 108]

# update index of mv
print('Before update:', example)  # bytearray(b'Hello')
mv[0] = 90
print('After update:', example)   # bytearray(b'Zello')


# min()
# -----------------------------------------------------------------------------
# The min() method returns the smallest element in an iterable or smallest of
# two or more parameters. Works the same as max() above.


# next()
# -----------------------------------------------------------------------------
# see iterating_with_for.py and generators.py
# returns the next item from the iterator


# object()
# -----------------------------------------------------------------------------
# This returns a featureless object which is a base for all classes.
# The object() method doesn't accept any parameters.

o = object()
print(type(o))  # <class 'object'>


# oct()
# -----------------------------------------------------------------------------
# see binary_data.py
# convert integers to octal (base 8)


# open()
# -----------------------------------------------------------------------------
# see files_read_write.py
# opens a file and returns a corresponding file object


# ord()
# -----------------------------------------------------------------------------
# method returns an integer representing Unicode code point for the given
# Unicode character. The ord() method is the inverse of chr(). It takes a
# single parameter: a string of 1 whose Unicode code point is to be found.

print(ord('-'))    # 45
print(ord('ǆ'))    # 454
print(ord('ᆼ'))    # 4540
print(ord('녘'))    # 45400


# pow()
# -----------------------------------------------------------------------------
# The pow() method returns x to the power of y. If the third argument (z) is
# given, it returns x to the power of y modulus z, i.e. pow(x, y) % z.
# The pow(x, y) is equivalent to: x ** y

print(pow(2, 2))    # 4
print(pow(-2, 2))   # 4
print(pow(2, -2))   # 0.25
print(pow(-2, -2))  # 0.25

x = 7
y = 2
z = 5

print(pow(x, y, z))  # 4


# print()
# -----------------------------------------------------------------------------
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


# property()
# -----------------------------------------------------------------------------
# see classes.py
# returns a property attribute.
# the syntax is:  property(fget=None, fset=None, fdel=None, doc=None)

# The parameters for property() are all optional:
# – fget (Optional) - function for getting the attribute value
# – fset (Optional) - function for setting the attribute value
# – fdel (Optional) - function for deleting the attribute value
# – doc (Optional) - string that contains the docstring for the attribute


# range()
# -----------------------------------------------------------------------------
# returns an immutable sequence object of integers - when using range() alone,
# you're creating a range object:

numbers = range(0, 100)
print(type(numbers)) # class 'range'
print(numbers[0:50:2] == range(0, 50, 2)) # True


# repr()
# -----------------------------------------------------------------------------
# returns a printable representation of the given object:
import datetime

now = datetime.datetime.utcnow()
print(repr(now))  # datetime.datetime(2017, 9, 5, 18, 23, 30, 607281)


# reversed()
# -----------------------------------------------------------------------------
# The reversed() method returns the reversed copy of the given sequence.

seqString = 'Python'
print(list(reversed(seqString)))  # ['n', 'o', 'h', 't', 'y', 'P']

seqTuple = ('P', 'y', 't', 'h', 'o', 'n')
print(list(reversed(seqTuple)))  # ['n', 'o', 'h', 't', 'y', 'P']

seqRange = range(5, 9)
print(list(reversed(seqRange)))  # [8, 7, 6, 5]

seqList = [1, 2, 4, 3, 5]
print(list(reversed(seqList)))  # [5, 3, 4, 2, 1]

class Vowels:
    vowels = ['a', 'e', 'i', 'o', 'u']
    def __reversed__(self):
        return reversed(self.vowels)

v = Vowels()
print(list(reversed(v)))  # ['u', 'o', 'i', 'e', 'a']


# round()
# -----------------------------------------------------------------------------
# returns the floating point number rounded off to the given ndigits digits
# after the decimal point. If no ndigits is provided, it rounds off the number
# to the nearest integer.

# round(number[, ndigits])

print(round(10))        # 10
print(round(10.7))      # 11
print(round(5.5))       # 6
print(round(2.665, 2))  # 2.67

# cannot be represented exactly as float
print(round(2.675, 2))  # 2.67


# set()
# -----------------------------------------------------------------------------
# see sets.py
# create a set object


# setattr()
# -----------------------------------------------------------------------------
# sets the value of given attribute of an object: setattr(object, name, value)
# If the attribute isn't found, it is created. You can use it on an instance
# or the class itself. Though the majority of the time you can just use
# dot notation, there are times when dot notation does't work, for example
# when the name of the attribute you want to set is a variable (see below):

class Person():
    name = 'Adam'

p = Person()

p.name = 'Rick'
print(p.name)  # Rick

setattr(p, 'name', 'Raja')
print(p.name)  # Raja

attributes = {'name': 'Paul', 'age': 50, 'email': 'paul@email.com'}

# doesn't work and I don't know why:
for key, value in attributes.items():
    p.key = value

# but this works:
for key, value in attributes.items():
    setattr(p, key, value)

print(p.name, p.age, p.email)  # Paul 50 paul@email.com


# slice()
# -----------------------------------------------------------------------------
# The slice() constructor creates a slice object representing the set of
# indices specified by range(start, stop, step). If a single parameter is
# passed, it's used for the stop (start and step are set to 0)

# slice(start, stop, step)

a_string = 'Python'
a_list = ['P', 'y', 't', 'h', 'o', 'n']
a_tuple = ('P', 'y', 't', 'h', 'o', 'n')

s_object = slice(3)
print(a_string[s_object])       # Pyt
print(a_list[s_object])         # ['P', 'y', 't']
print(a_tuple[s_object])        # ('P', 'y', 't')

s_object = slice(1, 5, 2)
print(a_string[s_object])       # yh
print(a_list[s_object])         # ['y', 'h']
print(a_tuple[s_object])        # ('y', 'h')

s_object = slice(-1, -4, -1)
print(a_string[s_object])       # noh
print(a_list[s_object])         # ['n', 'o', 'h']
print(a_tuple[s_object])        # ('n', 'o', 'h')

# The slice object can be substituted with the indexing syntax in Python.
# obj[start:stop:step]

print(a_string[1:5:2])          # yh


# sorted()
# -----------------------------------------------------------------------------
# see dictionaries.py, lists.py, sets.py
# returns a sorted list from the given iterable
# There is an optional parameter: reverse=True. You can also supply an optional
# key, which is a function. The sorting will be based on the key functions
# results. For example:

mylist = ['m', 'magic', 'mag', 'magical']
mydict = {'a': 5, 'b': 1, 'c': 3}

print(sorted(mylist, key=len, reverse=True))
# ['magical', 'magic', 'mag', 'm']

print(sorted(mydict.items(), key=lambda x: x[1]))
# [('b', 1), ('c', 3), ('a', 5)]


# staticmethod()
# -----------------------------------------------------------------------------
# see classes.py
# Returns a static method for function – use the @staticmethod decorator


# str()
# -----------------------------------------------------------------------------
# see strings.py
# returns a string object


# sum()
# -----------------------------------------------------------------------------
# The sum() function adds the items of an iterable and returns the sum. Start
# parameter (optional) is a value added to the sum of items in the iterable.
# The default value of start is 0 (if omitted)

# sum(iterable, start)

numbers = [2.5, 3, 4, -5]

total = sum(numbers)      # 4.5
print(total)

total = sum(numbers, 10)  # 14.5
print(total)

# If you need to add floating point numbers with exact precision then use
# math.fsum(iterable) instead.

# If you need to concatenate items of the given iterable (items must be string)
# then use join() method: ''.join(sequence)


# super()
# -----------------------------------------------------------------------------
# see classes.py
# In case of inheritance, it allows us to refer base class by super()


# tuple()
# -----------------------------------------------------------------------------
# see tuples.py
# returns a tuple object


# type()
# -----------------------------------------------------------------------------
# see reflection.py
# if a single object is passed, returns type of the given object


# vars()
# -----------------------------------------------------------------------------
# returns the __dict__ attribute of the given object if the object has a
# __dict__ attribute (eg. a module, class, instance).

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

baker = Person('Mrs. Lovett', 35)

print(vars(baker))
# {'name': 'Mrs. Lovett', 'age': 35}

print(vars())
# will print ALL the variables in the entire doc


# zip()
# -----------------------------------------------------------------------------
# see zip_function.py
# take iterables (can be zero or more), makes iterator that aggregates
# elements based on the iterables passed, and returns an iterator of tuples


#__import__()
# -----------------------------------------------------------------------------
# see import.py
# This is an advanced function that is called by the import statement.
