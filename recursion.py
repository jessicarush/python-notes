'''Recursion'''

# Recursion is a way of programming or coding a problem, in which a function
# calls itself one or more times in its body. Usually, it is returning the
# return value of this function call. Put simply, a recursive function is a
# function that calls itself.


# Factorial
# -----------------------------------------------------------------------------

def factorial_i(n):
    '''calculates n! iteratively'''
    # for example  5! = 5 * 4 * 3 * 2 * 1 = 120
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


# With factorials, you can also say that 6! = 6 * 5!, which is to say you can
# get the factorial of 6 by multiplying 6 * 5's factorial (120).

def factorial_r(n):
    '''calculates n! recursively'''
    # n! can also be defined as n * (n-1)!
    if n <= 1:
        return 1
    else:
        return n * factorial_r(n - 1)

# Termination condition: A recursive function has to terminate to be useable
# in a program. A recursive function terminates, if with every recursive call
# the solution of the problem is downsized and moves towards a base case.
# A base case is, where the problem can be solved without further recursion.
# A recursion can lead to an infinite loop, if the base case is not met. In
# the example above, the base case it met by if n <= 1, return 1

# testing:
for i in range(6):
    print(i, factorial_i(i))
# 0 1
# 1 1
# 2 2
# 3 6
# 4 24
# 5 120

for i in range(6):
    print(i, factorial_r(i))
# 0 1
# 1 1
# 2 2
# 3 6
# 4 24
# 5 120


# Fibonacci
# -----------------------------------------------------------------------------

def fib_i(n):
    '''Calculates fibonacci iteratively'''
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def fib_r(n):
    '''Calculates fibonacci recursively'''
    if n  < 2:
        return n
    else:
        return fib_r(n - 1) + fib_r(n - 2)

def fib_g(n):
    '''Calculates fibonacci with a generator'''
    a, b = 0, 1
    counter = 0
    while counter < n:
        yield b
        a, b = b, a + b
        counter += 1

# testing:
for i in range(10):
    print(fib_i(i))  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

for i in range(10):
    print(fib_r(i))  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

fib_generator = fib_g(10)
for i in fib_generator:
    print(i)        # 1, 1, 2, 3, 5, 8, 13, 21, 34, 55


# Directory Listings
# -----------------------------------------------------------------------------

import os

# os.walk() creates a generator object that yields a 3-item tuple
# (dirpath, dirnames, filenames). dirpath is a string of the path to the
# directory. dirnames is a list of the names of the subdirectories in dirpath
# (excluding '.' and '..'). filenames is a list of the names of the
# non-directory files in dirpath.

# This is a non-recursive example:

listing = os.walk('.')

print(next(listing))

for root, directories, files in listing:
    print('Root: ', root)
    for d in directories:
        print('Directories: ', d)
    for f in files:
        print('Files: ', f)

# here we use os.listdir and os.path to create a recursive example:

def list_directory(s):
    def dir_list(d):
        nonlocal tab_stop
        files = os.listdir(d)
        for f in files:
            current_dir = os.path.join(d, f)
            if os.path.isdir(current_dir):
                print('\t' * tab_stop + 'Directory':  + f)
                tab_stop += 1
                dir_list(current_dir)
                tab_stop -= 1
            else:
                print('\t' * tab_stop + f)

    tab_stop = 0
    if os.path.exists(s):
        print('Directory listing of ' + s)
        dir_list(s)
    else:
        print(s + ' does not exist')


list_directory('./data')


# Tips:
# -----------------------------------------------------------------------------
# When coding/testing a recursive function, it's often helpful to insert print
# statements to see what's going on. When you do this, add a tab before the
# print so you can visually see your levels of recursion.
