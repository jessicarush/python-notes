'''Namespaces'''

# Local and global variables -------------------------------------------------

# You can get the value of a global variable from within a function

animal = 'fruitbat'

def print_global():
    print('inside print_global:', animal)

print_global()

# But if you get the value of a global variable and and try to change it within
# a function, you get an error because as soon as you start assigning to a
# variable, python wants to make it a local variable, and since no local
# variable has been initialized... error:

# def change_and_print_global():
#     print('inside change_and_print_global:', animal)
#     animal = 'wombat'
#     print('after the change:', animal)


# So, if you reassign the variable you are actually making a new local variable
# (also named animal) inside of the function. Use ID to see they're different:

def change_local():
    animal = 'wombat'
    print('local animal:', animal, id(animal))

change_local()
print('global animal:', animal, id(animal))

# To access and change a global variable from within a function you need to be
# explicit by using the global keyword:

def change_and_print_global():
    global animal
    print('inside change_and_print_global:', animal)
    animal = 'wombat'
    print('after the change:', animal)

change_and_print_global()

# nonlocal -------------------------------------------------------------------

# Python 3 introduced the nonlocal keyword that allows you to assign to
# variables in an outer, but non-global, scope.

def testing_nonlocal():
    x = 'lemon'
    def inside():
        nonlocal x
        x = 'lime'
        print(x)
    inside()

testing_nonlocal()

# locals() and globals() -----------------------------------------------------

# Python provides two functions to access the contents of your Namespaces
# locals() and globals():

fruit = 'orange'

def testing_local():
    fruit = 'apple'
    print('locals:', locals())

testing_local()

print('globals:')
g = sorted(globals())
for x in g:
    print(x)

# NOTE: when you reference a variable name, python will start by looking for the variable definition locally, and then move outward until if finds it. The order of scopes is as follows:

# – local
# – enclosing
# – global
# – built-ins

# __name__, __doc__ ----------------------------------------------------------

# The name of a function is in the system variable: function.__name__
# The functions document string in in the variable: function.__doc__

def amazing():
    '''This is the functions description'''
    print('This function is named:', amazing.__name__)
    print('Its docstring says:', amazing.__doc__)
    print('The main program running is assigned a special name:', __name__)

amazing()
