'''Systems (Files, Directories, Programs and Processes)'''


# Python provides many operating system functions through a module named os.
# Like many other languages, Python patterned its file operations after Unix.
# Some functions, such as chown() and chmod(), have the same names, but there
# are a few new ones.


# Files
# -----------------------------------------------------------------------------
# Create a file with open()
# open() function is used to open a file or create one if it doesn't exist:

with open('data/practice.txt', 'w') as fob:
    print('File created.', file=fob)

# Check Existence with exists()
# you can provide exists(), with a relative or absolute pathname:

import os

print(os.path.exists('data/practice.txt'))    # True
print(os.path.exists('./data/practice.txt'))  # True
print(os.path.exists('.'))                    # True

# Check Type with isfile(), isdir(), isabs()
# These functions check whether a name refers to a file, directory, or path

name = 'data/practice.txt'

print(os.path.isfile(name))                   # True
print(os.path.isdir(name))                    # False
print(os.path.isabs('/templates/home.html'))  # True

# Copy with copy()
# The copy() function comes from another module, shutil:
# The shutil.move() function copies a file and then removes the original.

import shutil

shutil.copy('data/practice.txt', 'data/practice_copy.txt')
shutil.move('data/practice.txt', 'data/practice1.txt')

# Change Name with rename()

os.rename('data/practice_copy.txt', 'data/practice2.txt')

# Create a hard link with link() or a soft link with symlink()

# Soft Links (symbolic links) are shortcuts (aliases) to files or directories.
# These shortcuts can lead to different a partition with a different "inode"
# number from original. If the original copy is deleted, the link will no
# longer work.

# Hard Links are for files only; you cannot link to a file on different
# partition with a different "inode" number. If the original copy is deleted
# the link will still work, because it accesses the underlying data that the
# real copy was accessing.

# Make a hard link to practice1.txt from the new file p_link:

os.link('data/practice1.txt', 'data/p_link')

# Make a symbolic link (alias, shortcut) to practice1.txt from the new file:

os.symlink('data/practice1.txt', 'data/p_slink')

# Check if a file is a symbolic link (alias, shortcut):

print(os.path.islink('data/p_slink'))  # True

# Get a Pathname with abspath()
# This function expands a relative name to an absolute one.

print(os.path.abspath('data/practice1.txt'))
# /Users/jessicarush/Documents/Coding/Python/github_python/data/practice1.txt

# Get a symlink Pathname with realpath()

print(os.path.realpath('data/p_slink'))
# /Users/jessicarush/Documents/Coding/Python/github_python/data/data/practice1.txt

# NOTE: I have no idea why the output says data/data/

# Delete a File with remove()

os.remove('data/p_link')
os.remove('data/p_slink')

# Change Permissions with chmod()

# On a Unix system, chmod() changes file permissions. There are read, write,
# and execute permissions for the user, the main group that the user is in,
# and the rest of the world. The command takes a compressed octal (base 8)
# value that combines user, group, and other permissions.

os.chmod('data/practice1.txt', 0o4644)

# There's a great octal calculator: http://permissions-calculator.org

# Change Ownership with chown()

# This function is Unix/Linux/Mac–specific. You can change the owner and/or
# group ownership of a file by specifying the numeric user ID (uid) and group
# ID (gid). I can't get this to work but in theory:

uid = 501
gid = 20
os.chown('data/practice1.txt', uid, gid)


# Directories
# -----------------------------------------------------------------------------
# Create with mkdir()

os.mkdir('data/practice')

# Check that it's there:

print(os.path.exists('data/practice'))  # True

# Delete with rmdir() - remember this only works on empty directories

os.rmdir('data/practice')

# List Contents with listdir()

os.mkdir('data/practice')
os.mkdir('data/practice/stuff')

print(os.listdir('data/practice'))  # ['stuff']

os.rmdir('data/practice/stuff')
os.rmdir('data/practice')

# Change Current Directory with chdir()

os.chdir('../')         # go up one directory
print(os.listdir('.'))  # list contents of current directory
# ['.DS_Store', 'resources', 'programs', 'courses', 'templates', 'github_python']

os.chdir('github_python/')

# copy a directory and all of it's contents recursively
# - this WILL NOT overwrite directories that already exist:

import shutil

os.mkdir('data/my_files')
with open('data/my_files/test.txt', 'w') as fob:
    print('File created.', file=fob)

src = 'data/my_files'
dst ='data/backups'
shutil.copytree(src, dst)

# copy a directory and all of it's contents recursively
# - this WILL overwrite directories that already exist:

import distutils.dir_util

src = 'data/my_files'
dst ='data/backups'
distutils.dir_util.copy_tree(src, dst)


# List Matching Files with glob()
# -----------------------------------------------------------------------------
# The glob() function matches file or directory names by using Unix shell
# rules rather than regular expression syntax. Here are those rules:

# * matches everything (in RE would be .*)
# ? matches a single character
# [abc] matches character a, b, or c
# [!abc] matches any character except a, b, or c

# Get all files or directories that begin with 'T' upper or lower case:

import glob

print(glob.glob('[Tt]*'))

# begins with 'n' or 'N' and ends in py:

os.chdir('data')

print(glob.glob('[nN]*csv'))


# Programs and Processes
# -----------------------------------------------------------------------------
# The Python os module provides some ways to access some system
# information similar to what you would see in Activity Monitor.

import os

# Get Process ID for the running Python interpreter:

print(os.getpid())  # 6047

# Get current working directory:

print(os.getcwd())  # /Users/jessicarush/Documents/Coding/Python/github_python

# Get user and group IDs:

print(os.getuid())  # 501
print(os.getgid())  # 20

# Create a Process with subprocess:

# All of the programs here so far have been individual processes. Individual
# processes are isolated from other processes. You can start and stop other
# existing programs from Python by using the subprocess module.

# Example: run another program in a shell and grab the output it creates using
# the getoutput() function.

import subprocess

r = subprocess.getoutput('python3 date_time_examples.py')
print(r)

# You won't get anything back until the process ends. If you need to call
# something that might take a long time, look into concurrency.py.

# Here, we'll get the output of the Unix date program:

r = subprocess.getoutput('date')
print(r)
# Tue 21 Nov 2017 11:09:31 PST

# Because the argument to getoutput() is a string representing a complete
# shell command, you can include arguments, pipes, < and > so on:

r = subprocess.getoutput('date -u')
print(r)
# Tue 21 Nov 2017 19:10:40 UTC

# Piping to this wc command does a count of lines, words, and characters.
# I have no idea why it formats like it does:

r = subprocess.getoutput('date -u | wc')
print(r)
#        1       6      29

# A variant method called check_output() takes a list of the command and
# arguments. By default it only returns standard output as type bytes rather
# than a string and does not use the shell:

r = subprocess.check_output(['date', '-u'])
print(r)
# b'Tue 21 Nov 2017 19:15:25 UTC\n'

# To show the exit status of the other program, getstatusoutput() returns a
# tuple with the status code and output:

r = subprocess.getstatusoutput('date')
print(r)
# (0, 'Tue 21 Nov 2017 11:16:11 PST')

# (In Unix-like systems, 0 is usually the exit status for success.)

# If you only want the status and no output use call():

r = subprocess.call('date')
print(r)
# 0

# Create a Process with Multiprocessing:

# You can run a Python function as a separate process or run multiple
# independent processes in a single program with the multiprocessing module:

import multiprocessing as mp
import os

def do_this(arg):
     name(arg)

def name(arg):
    print("Process {} is: {}".format(os.getpid(), arg))

if __name__ == "__main__":
    name("the main program")
    for n in range(4):
        # NOTE: args=(must be a tuple,)
        p = mp.Process(target=do_this, args=("function {}".format(n+1),))
        p.start()

# Process 6236 is: the main program
# Process 6246 is: function 1
# Process 6247 is: function 2
# Process 6248 is: function 3
# Process 6249 is: function 4

# The Process() function spawned a new process and ran the do_this() function
# in it. Because we did this in a loop, we generated four new processes that
# executed do_this() and then exited.

# The intention is that you can spread out some task to multiple processes to
# save overall time; for example, downloading web pages for scraping, resizing
# images... It includes ways to queue tasks, enable intercommunication among
# processes, and wait for all the processes to finish.

# Kill a Process with terminate()

# If you created one or more processes and want to terminate one for some
# reason (perhaps it's stuck in a loop), use terminate().

# In this example, the process would count to a thousand, sleeping at each
# step for a second, and printing a message. However, our main program will
# terminate it at 5 seconds:

import multiprocessing as mp
import time
import os

def whoami(name):
    print('{} in process {}'.format(name, os.getpid()))

def counter(name):
    whoami(name)
    start = 1
    stop = 1000
    for num in range(start, stop):
        print('{} of {}'.format(num, stop))
        time.sleep(1)

if __name__ == "__main__":
    whoami("main")
    p = mp.Process(target=counter, args=("counter",))
    p.start()
    time.sleep(5)
    p.terminate()

# see also concurrency.py
