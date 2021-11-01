'''Testing Python Code'''


# Code checkers: pylint, pycodestyle or pyflakes
# -----------------------------------------------------------------------------
# These check for code errors and style issues:
# https://pylint.readthedocs.io/en/latest/
# https://pypi.python.org/pypi/pycodestyle/2.2.0
# https://pypi.org/project/pyflakes/

# Install:
# pylint       $ pip install pylint
# pycodestyle  $ pip install pycodestyle
# pyflakes     $ pip install pyflakes

# Test a file via the command line:
# $ pylint myfile.py
# $ pycodestyle myfile.py
# $ pyflakes myfile.py

A = 1
B = 2
C = 3
print(A)
print(B)
print(C)

# pylint message types can be:
#     - [R]efactor for a "good practice" metric violation
#     - [C]onvention for coding standard violation
#     - [W]arning for stylistic problems, or minor programming issues
#     - [E]rror for important programming issues (i.e. probably bug)
#     - [F]atal for errors which prevented further processing

# pylint always wants a docstring at the top of the module

# If variables are defined outside of a function or class, it assumes it's a
# constant and as such, wants the name to be all caps and underscores (see
# documenting_naming.py). The error will read: Invalid constant name

# pycodestyle always expects 2 blank lines following an import, function def
# or class. It also expects all imports to be at the top of the file.

# Some developers that actually code for python say that they hate pylint,
# because it's way too opinionated. For example, they get 40% marks on average
# and they are ideal python developers. These people say they prefer pyflakes
# and I tend to agree.


# NOTE: Atom linter-pylint package
# -----------------------------------------------------------------------------
# After a while, the C0103 pylint warning for invalid constant names gets
# really irritating. If you want to turn it off permanently in Atom do this:

# Create an rc file:
# $ pylint --generate-rcfile > ~/.pylintrc

# In this file, find the variable 'disable=...'. It will be located in the
# [MESSAGES CONTROL] category. At the end of the disable assignment, add a
# comma followd by the code C0103 (this is the code is found in the warning).


# Testing code with assert
# -----------------------------------------------------------------------------
# To assert is to ensure something is True

def words(text):
    return text.title()
    # from string import capwords
    # return capwords(text)


def test_one_word():
    assert words('duck') == 'Duck', 'Single word failed!'


def test_many_words():
    assert words('flock of ducks') == 'Flock Of Ducks', 'Multiple words fail!'


def test_with_apostrophes():
    assert words("I'm a duck") == "I'm A Duck", 'Apostrophe fail!'


test_one_word()
test_many_words()
test_with_apostrophes()
# Traceback (most recent call last):
#   File "testing.py", line 73, in <module>
#     test_with_apostrophes()
#   File "testing.py", line 69, in test_with_apostrophes
#     assert words("I'm a duck") == "I'm A Duck", 'Apostrophe fail!'
# AssertionError: Apostrophe fail!


# Code tester: pytest
# -----------------------------------------------------------------------------
# Code testers still use assert but include many more features. The modules
# pytest and unittest seem to be the most common. The unnitest module is part
# of the standard library but the pytest module seems to be much more popular
# and recommended by most people on reddit and slant. The main reason seems to
# be that pytest introduced the concept that Python tests should be plain
# functions instead of forcing developers to include their tests inside large
# test classes (unnitest).

# pytest - https://docs.pytest.org/en/latest/contents.html
# Code testers check for errors in code logic using your own tests.

# content for myfile.py:

def func1(x):
    return x + 1


def test_answer():
    assert func1(4) == 5

# run pytest: $ pytest myfile.py

# NOTE: you can write all your tests in one file and import the module and
# functions that you want to test.


# Code tester: unittest
# -----------------------------------------------------------------------------
# The Python standard library also provides a module to automate the testing of
# a functions output: unittest. A unit test verifies that one specific aspect
# of a functions behaviour is correct. A test case is a collection of unit
# tests that together prove that a function behaves as it's supposed to, within
# the full range of situations you expect it to handle. A good test case
# considers all the possible kinds of input a function could receive.

# Example function to test:

def format_name(first, last, middle=' '):
    '''Generate neatly formatted name'''
    if middle != ' ':
        middle = ' ' + middle + ' '
    full_name = first + middle + last
    return full_name.title()

# Example test file test_functions.py:

import unittest
# import the function(s) to be tested


class NamesTestCase(unittest.TestCase):
    '''Tests for format_name()'''

    def test_first_last(self):
        '''Do names like Janis Joplin work?'''
        formatted = format_name('janis', 'joplin')
        self.assertEqual(formatted, 'Janis Joplin')

    def test_first_middle_last(self):
        '''Do names like Martin Luther King work?'''
        formatted = format_name('martin', 'king', 'luther')
        self.assertEqual(formatted, 'Martin Luther King')


unittest.main()

# You can call your test class anything you want but it must inherit from
# unittest.TestCase. Methods that start with 'test_' will will be run
# automatically when we run the test file. The unittest.TestCase class allows
# you to use a number of special assert methods. These can only be used in a
# class that inherits from unittest.TestCase (these are just a few of them):

# assertEqual(a, b)         – verify that a == b
# asertNotEqual(a, b)       – verify that a != b
# assertTrue(x)             – verify that x is True
# assertFalse(x)            – verify that x is False
# assertIn(item, list)      – verify that item is in list
# assertNotIn(item, list)   – verify that item is not in list

# testing a class is similar to testing a function – much of the work involves
# testing the methods in the class, but there are a few differences.

# Example class to test:


class AnonymousSurvey():
    '''Collect anonymous answers to a survey question'''

    def __init__(self, question):
        '''Stores question and prepares to store responses'''
        self.question = question
        self.responses = []

    def show_question(self):
        '''Show the survey question'''
        print(self.question)

    def store_response(self, new_response):
        '''Store a single response to the survey'''
        self.responses.append(new_response)

    def show_results(self):
        '''Show all the responses to the survey'''
        print('Survey Results:')
        for response in self.responses:
            print('– ' + response)


# Example code that uses the class:

question = 'What is your favourite language?'
my_survey = AnonymousSurvey(question)
my_survey.show_question()

while True:
    response = input('Language (q to quit): ')
    if response == 'q':
        break
    my_survey.store_response(response)

my_survey.show_results()

# Example test file test_classes.py:

# This test will verify that a single response to the survey question is stored
# properly. Once the test is written, we can safely extend the class and its
# modules to include more functionality.

import unittest
# import the class(es) to be tested


class TestAnonymousSurvey(unittest.TestCase):
    '''Tests for the class AnonymousSurvey'''

    def setUp(self):
        '''Create a survey and set of responses for test methods to use'''
        question = 'What is your favourite language?'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['Python', 'Ruby', 'Javascript']

    def test_single_response(self):
        '''Test that a single response is stored properly'''
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_multi_response(self):
        '''Test that a multiple responses are stored properly'''
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


unittest.main()

# unittest.TestCase has a setUp() method that allows you to create objects once
# and use them in each of your test methods. When you include a setUp() method,
# Python runs it before running each method that starts with 'test_'.


# Code tester: doctest
# -----------------------------------------------------------------------------
# doctest - https://docs.python.org/3.6/library/doctest.html
# Doctests are written in the docstring. Try running the file normally and
# also verbosely: python3 testing.py -v

def func3(x):
    """
    >>> func3(4)
    5
    """
    return x + 1


def func2(text):
    """
    >>> func2('duck')
    'Duck'
    >>> func2('a bunch of ducks')
    'A Bunch Of Ducks'
    >>> func2("I'm a duck")
    "I'm A Duck"
    """
    from string import capwords
    return capwords(text)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
