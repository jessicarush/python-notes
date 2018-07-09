'''Documenting and Naming'''

# docstrings
# -----------------------------------------------------------------------------
# For obvious reasons, it helps to document your code. Documentation can
# include comments and docstrings, but it can also incorporate informative
# naming of variables, functions, modules, and classes. Don't be obsessive, say
# why you assigned a value. Point out why you called a variable whatever.

def example():
    '''A brief, clear description.

    Extended description - the docstring should describe the function,
    class, or method in a way that is easy to understand.
    '''
    pass

# In larger or more complex projects however, it's often a good idea to give
# more information like, what it does, any exceptions it may raise, what it
# returns, or relevant details about the parameters, arguments, methods,
# variables or attributes. In multiline functions it's best to start with a
# single summary line, a space and then the extended description, followed by
# specific information on args, return etc. There are a number of popular
# documenting styles including reST (reStructuredText ), Numpy style, and
# Google has there own style too.

def example(arg1=0.0, arg2=None):
    '''
    reST style docstring.

    :param arg1: int, description of arg1, default 0.0
    :param arg2: str, description of arg2, default None
    :returns: int - Description of return value
    :raises keyError: raises an exception
    '''
    pass

def example(arg1=0.0, arg2=None):
    '''
    Google style docstring.

    You can find examples of python docstrings by following the links
    here: https://google.github.io/styleguide/.

    Note:
        Do this not that recommendation.

    Args:
        arg1 (int): description of arg1, default 0.0
        arg2 (str): description of arg2, default None

    Returns:
        int: description of return value.

    Raises:
        KeyError: Raises an exception.
    '''
    pass

def example(arg1, arg2=0.0):
    '''
    Numpy style docstring (numpydoc).

    Parameters
    ----------
    arg1 : string
        the 1st param, name `arg1`
    second : float, optional
        the 2nd param, by default 0.0

    Returns
    -------
    string
        a value in a string

    Raises
    ------
    KeyError
        when a key error
    OtherError
        when an other error
    '''
    pass

help(example)  # output all the docstrings (a class could have many)
print(example.__doc__)  # print just the one docstring


# Example
# -----------------------------------------------------------------------------
# if you were writing a Fahrenheit to Celsius converter:

def ftoc(f_temp):
    '''Convert Fahrenheit temperature <f_temp> to Celsius and return it.'''
    f_boil_temp = 212.0
    f_freeze_temp = 32.0
    c_boil_temp = 100.0
    c_freeze_temp = 0.0
    f_range = f_boil_temp - f_freeze_temp
    c_range = c_boil_temp - c_freeze_temp
    f_c_ratio = c_range / f_range
    c_temp = (f_temp - f_freeze_temp) * f_c_ratio + c_freeze_temp
    return c_temp

# And a little test code wouldn't hurt:

if __name__ == '__main__':
    for f_temp in [-40.0, 0.0, 32.0, 100.0, 212.0]:
        c_temp = ftoc(f_temp)
        print('%f F => %f C' % (f_temp, c_temp))


# Constants
# -----------------------------------------------------------------------------
# Python doesn't have constants, but the PEP8 stylesheet recommends using
# capital letters and underscores (e.g., ALL_CAPS) when naming variables that
# should be considered constants.

# Because we precompute values based on constant values, move them to the top
# level of the module. Then, they'll only be calculated once rather than in
# every call to the ftoc() function:

F_BOIL_TEMP = 212.0
F_FREEZE_TEMP = 32.0
C_BOIL_TEMP = 100.0
C_FREEZE_TEMP = 0.0
F_RANGE = F_BOIL_TEMP - F_FREEZE_TEMP
C_RANGE = C_BOIL_TEMP - C_FREEZE_TEMP
F_C_RATIO = C_RANGE / F_RANGE

def ftoc(f_temp):
    "Convert Fahrenheit temperature <f_temp> to Celsius and return it."
    c_temp = (f_temp - F_FREEZE_TEMP) * F_C_RATIO + C_FREEZE_TEMP
    return c_temp


# Private attributes or methods
# -----------------------------------------------------------------------------
# If you're building a module that will be imported, you can identify functions
# that aren't intended to be called on their own by naming them with a leading
# underscore. Python programmers will interpret this as "this is an internal
# variable, think carefully before accessing it directly".

def _guts():
    pass


# Protected attributes or methods (name mangling)
# -----------------------------------------------------------------------------
# This method is for when you want to strongly suggest that outside objects
# don't access an attribute, property or method in a classe. The naming
# convention is a leading double underscore. Python "mangles" the names of
# attributes that start with two underscores to make it more difficult to
# accidentally mess with it. The mangling is this: _Classname__attibutename

class Person():
    def __init__(self, name, alias):
        self.name = name       # public attribute
        self.__alias = alias   # private attribute

x = Person(name='Bob', alias='boktoktok')

print(x.name)
# Bob

# print(x.alias)
# AttributeError: 'Person' object has no attribute 'alias'

# p int(x.__alias)
# AttributeError: 'Person' object has no attribute '__alias'

print(x._Person__alias)
# boktoktok

# However, most Python programmers will not touch a single underscore variable
# without a compelling reason, let alone the double. Therefore, this method is
# overkill. Stick with single leading underscores. If you're going to use
# either method, make a note of it in the docstring.


# Throwaway values
# -----------------------------------------------------------------------------
# in the event that you need to give something a name but you have no intention
# of using it, it's acceptable to use the name '_'. The perfect example of this
# is with tuple unpacking. In the example below, I don't want the age
# information, but I need to give it a name in order to unpack the rest:

person = ('Kali', '50', 'Peru')

name, _, country = person

print(name, country)


# Variable names using Python keywords
# -----------------------------------------------------------------------------
# If you're desperate to name something using one of Pythons keywords, the
# accepted standard is to follow the with an underscore:

from_ = 'example'


# Type hints (variable, function and class annotation)
# -----------------------------------------------------------------------------
# Python 3 introduced a syntax addition called function annotation syntax.
# Python 3.6 introduced a syntax for annotating variables. Python 3.7 introduced
# the dataclasses decorator which requires annotation on class variables.
# Annotations serve as a way of documenting a variable, class or function by
# indicating the type expected and type returned.

# For simple built-in types:
x: int = 1
x: float = 1.0
x: bool = True
x: str = 'test'
x: bytes = b'test'

# In Python 3.5 and earlier you can use a type comment instead
x = 1  # type: int

# Note, you don't need to initialize a variable to annotate it
x: int

# For collections, the types must be imported from the typing module.
# You can specify the types within the colection in brackets.

from typing import List, Set, Dict, Tuple, Optional, Union, Any

x: List[int] = [1]
x: Set[int] = {6, 7}

# For dictionaries, we need the types of both keys and values:
x: Dict[str, float] = {'field': 2.0}

# For tuples, specify the types of all the elements
x: Tuple[int, str, float] = (3, "yes", 7.5)

# Use Optional[] for values that could be None
x: Optional[str] = some_function()

# Use Union when something could be one of a few types
x: List[Union[int, str]] = [3, 5, "test", "fun"]

# Use Any if you don't know the type of or it's too dynamic to pick one:
x: Any = some_function()

# An annotated function would look like this:

import datetime

def to_date(date_string: str) -> datetime:
    return datetime.strptime(date_string, '%Y-%m-%d')

# multiple arguments
def add(num1: int, num2: int) -> int:
    return num1 + num2

# You can split a function annotation over multiple lines
def send_email(address: Union[str, List[str]],
               sender: str,
               cc: Optional[List[str]],
               bcc: Optional[List[str]],
               subject: str = '',
               body: Optional[List[str]] = None) -> bool:
    pass

# There are many more types. See the documentation for more information:

# https://docs.python.org/3.7/library/typing.html#module-typing
# https://www.python.org/dev/peps/pep-0484/
# https://www.python.org/dev/peps/pep-3107/
# https://www.python.org/dev/peps/pep-0526/


# Code Tags
# -----------------------------------------------------------------------------
# https://www.python.org/dev/peps/pep-0350/

# When working on a project, it’s often desirable to create a list of tasks
# for yourself or your team mates. While usually these are described in an
# issue tracker of some sort, some tasks are either too small or too
# code-specific to describe in a formal tracker. In these cases, adding
# code tags in source code makes sense. Some examples are:

# TODO: Create this blah blah
# FIXME: Change this to blah blah
# BUG: Crashes if blah blah
# HACK: Temporary code to force inflexible functionality, or simply a test
# change, or workaround a known problem.
# NOTE: Needs further investigation
# QUESTION: Self explanatory
