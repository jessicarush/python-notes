'''Context managers: with expression as variable'''

# Context managers allow the execution of initialization and finalization
# code around another block of code. In simpler terms, its helpful for when you
# have two related operations you'd like to execute as a pair, with a block of
# code in between.

print('set things up') # initialization code
try:
    print('do something') # another block of code
finally:
    print('tear things down') # finalization code

# Here, “set things up” could be opening a file, or acquiring some external
# resource, and “tear things down” would then be closing the file, or releasing
# or removing the resource. The try-finally construct guarantees that the
# “tear things down” part is always executed, even if the code that does the
# work doesn’t finish. Perhaps the most common (and important) use of context
# managers is to properly manage resources. The act of opening a file consumes
# a resource (called a file descriptor), and this resource is limited by your
# OS – there are a maximum number of files a process can have open at one time.
# Using a context manager ensures these resources are released.

with open('filename.txt', 'w') as fileobject:
    print('do something')

# So the general translation is that there is a try and finally block running
# behind the scenes. The example below demonstrates this method in amother way.
# It says try: __enter__() the block and when completed, finally: __exit__().

class controlled_execution:
    def __enter__(self):
        thing = 'set things up'
        print(thing)
        return thing
    def __exit__(self, type, value, traceback):
        print('tear things down')

with controlled_execution() as thing:
    print('do something')

# This is considered a context manager. A context manager is an object that
# defines the runtime context to be established when executing a with statement.
# The context manager handles the entry into, and the exit from, the desired
# runtime context for the execution of the block of code. Context managers are
# normally invoked using the with statement. Typical uses of context managers
# include saving and restoring various kinds of global state, locking and
# unlocking resources, closing opened files, etc.

# As above, you can implement a context manager as a class. At the very least a
# context manager has __enter__ and __exit__ methods defined. Here's an example
# of a file opening context manager:

class File():

    def __init__(self, filename, method):
        self.file_obj = open(filename, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()
        return True   # if you want exceptions to be ignored
        return False  # if you want to pass the exception up the line

# Just by defining __enter__ and __exit__ methods we can use it in a with
# statement:

with File('test.txt', 'w') as opened_file:
    opened_file.write('Hola!')

# You can also construct your own context managers using the contextmanager
# decorator from contextlib.

# -----------------------------------------------------------------------------
# example 1
# -----------------------------------------------------------------------------

from contextlib import contextmanager

@contextmanager
def tag(name):
    print("<{}>".format(name), end='')
    yield
    print("</{}>".format(name))

with tag("h1"):
    print("Heading", end='')  # <h1>Heading</h1>

# -----------------------------------------------------------------------------
# example 2
# -----------------------------------------------------------------------------
# This could be used when you have to change the current directory temporarily
# and then return to where you were:

from contextlib import contextmanager
import os

@contextmanager
def working_directory(path):
    current_dir = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(current_dir)

with working_directory("data/stuff"):
    pass # do something within data/stuff

# Then here you are back again in the original working directory

# -----------------------------------------------------------------------------
# example 3
# -----------------------------------------------------------------------------
# This example  creates a temporary folder and cleans it up when leaving
# the context:

from tempfile import mkdtemp
from shutil import rmtree

@contextmanager
def temporary_dir(*args, **kwargs):
    name = mkdtemp(*args, **kwargs)
    try:
        yield name
    finally:
        shutil.rmtree(name)

with temporary_dir() as dirname:
    pass # do whatever
