'''Testing Python Code'''

# Run a Python Code Checker ---------------------------------------------------

# These check for code errors and style issues. Examples are:
# pylint - $ pip3 install pylint
# pep8 - $ pip3 install pep8

# Test this file: $ pylint myfile.py or $ pep8 ch12_3.py

A = 1
B = 2
C = 3
print(A)
print(B)
print(C)

# pylint output lines starting with an E: stand for error

# pylint always wants a doctring at the top of the module

# If variables are defined outside of a function or class, it assumes it's a
# constant and as such, wants the name to be all caps and underscores (see
# docmenting_naming.py). The error will read: Invalid constant name "b"
# (invalid-name).

# pep8 always expects 2 blank lines following an import, function def or class

# pep8 expects all imports to be at the top of the file

# Run a Python Code Tester ----------------------------------------------------

# These check for errors in code logic using your own tests. Examples are:
# pytest - https://docs.pytest.org/en/latest/contents.html
# doctest - https://docs.python.org/3.6/library/doctest.html

# content for pytest:

def func1(x):
    return x + 1

def test_answer():
    assert func1(4) == 5

# run pytest: $ pytest myfile.py

# You can simply use the assert statement for asserting test expectations

def func2(text):
    from string import capwords
    return capwords(text)

def test_one_word():
    assert func2('duck') == 'Duck'

def test_mult_words():
    assert func2('a bunch of ducks') == 'A Bunch Of Ducks'

def test_with_apostrophes():
    assert func2("I'm a duck") == "I'm A Duck"

# NOTE: you can write all your tests in one file a simply import the file that
# contains you want to test.

# doctest is written in the docstring itself

# try running the file normally and also verbosely: python3 ch12_3.py -v

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
