'''Systems (Files, Directories, Programs and Processes)'''

# Python provides many operating system functions through a module named os
# Like many other languages, Python patterned its file operations after Unix.
# Some functions, such as chown() and chmod(), have the same names, but there
# are a few new ones.

# -----------------------------------------------------------------------------
# Files
# -----------------------------------------------------------------------------
# Create a file with open()
# open() function is used to open a file or create one if it doesn't exist:

fout = open('practice.txt', 'w')
print('File created.', file=fout)
fout.close()

# Check Existence with exists()
# you can provide exists(), with a relative or absolute pathname:

import os

os.path.exists('practice.txt')
os.path.exists('./practice.txt')
os.path.exists('.')

# Check Type with isfile(), isdir(), isabs()
# These functions check whether a name refers to a file, directory, or link

name = 'practice.txt'

os.path.isfile(name)
os.path.isdir(name)
os.path.isabs('/templates/home.html')

# Copy with copy()
# The copy() function comes from another module, shutil:
# The shutil.move() function copies a file and then removes the original.

import shutil
shutil.copy('practice.txt', 'practice_copy.txt')

# Change Name with rename()

os.rename('practice_copy.txt', 'practice2.txt')

# Link with link() or symlink()
# Make a hard link to practice.txt from the new file p_link.txt:

os.link('practice.txt', 'p_link')

# Make a symbolic link (aka alias, shortcut) to practice.txt from the new file:

os.symlink('practice.txt', 'p_slink')

# Check if a file is a symbolic link (alias, shortcut):

os.path.islink('p_slink')

# Change Permissions with chmod()

# On a Unix system, chmod() changes file permissions. There are read, write,
# and execute permissions for the user, the main group that the user is in,
# and the rest of the world. The command takes a compressed octal (base 8)
# value that combines user, group, and other permissions.

os.chmod('practice.txt', 0o4644)

# There's a great octal calculator: http://permissions-calculator.org

# Change Ownership with chown()

# This function is Unix/Linux/Mac–specific. You can change the owner and/or
# group ownership of a file by specifying the numeric user ID (uid) and group
# ID (gid). I can't get this to work but in theory:

uid = 501
gid = 20
os.chown('practice.txt', uid, gid)

# Get a Pathname with abspath()
# This function expands a relative name to an absolute one.

print(os.path.abspath('practice.txt'))

# Get a symlink Pathname with realpath()

print(os.path.realpath('p_slink'))

# Delete a File with remove()

os.remove('p_link')
os.remove('p_slink')

# -----------------------------------------------------------------------------
# Directories
# -----------------------------------------------------------------------------

# Create with mkdir()

os.mkdir('practice')

# Check that it's there:

os.path.exists('practice')

# Delete with rmdir() - remember this only works on empty directories

os.rmdir('practice')

# List Contents with listdir()

os.mkdir('practice')
os.mkdir('practice/stuff')
print(os.listdir('practice'))

# Change Current Directory with chdir()
# go from one directory to another:

os.chdir('../')         # go up one directory
print(os.listdir('.'))  # list content of current directory

# copy a directory and all of it's contents recursively
# - this WILL NOT overwrite directories that already exist:

import shutil
src = 'my_files/'
dst ='/Users/username/Documents/Backups/'
shutil.copytree(src, dst)

# copy a directory and all of it's contents recursively
# - this WILL overwrite directories that already exist:

import distutils.dir_util
src = 'my_files/'
dst ='/Users/username/Documents/Backups/'
distutils.dir_util.copy_tree(src, dst)

# -----------------------------------------------------------------------------
# List Matching Files with glob()
# -----------------------------------------------------------------------------
# The glob() function matches file or directory names by using Unix shell
# rules rather than regular expression syntax. Here are those rules:

# * matches everything (in RE would be .*)
# ? matches a single character
# [abc] matches character a, b, or c
# [!abc] matches any character except a, b, or c

# Get all files or directories that begin with 'T':

import glob

print(glob.glob('T*'))

# begins with 'f' or 'g' and ends in py:

os.chdir('Introducing Python')
print(glob.glob('[fg]*py'))

# -----------------------------------------------------------------------------
# Programs and Processes
# -----------------------------------------------------------------------------
# The Python os module provides some ways to access some system
# information similar to what you would see in Activity Monitor.

import os

# Get Process ID for the running Python interpreter:

print(os.getpid())

# Get current working directory:

print(os.getcwd())

# Get user and group IDs:

print(os.getuid())
print(os.getgid())

# Create a Process with subprocess:

# All of the programs here so far have been individual processes. Individual
# processes are isolated from other processes. You can start and stop other
# existing programs from Python by using the subprocess module.

# Example: run another program in a shell and grab the output it creates using
# the getoutput() function. Here, we'll get the output of the Unix date program:

import subprocess
ret = subprocess.getoutput('date')
print(ret)

# You won't get anything back until the process ends. If you need to call
# something that might take a long time, look into "concurrency".

# Because the argument to getoutput() is a string representing a complete
# shell command, you can include arguments, pipes, < and > so on:

ret = subprocess.getoutput('date -u')
print(ret)

# Piping to this wc command does a count of lines, words, and characters.
# I have no idea why it formats like it does:

ret = subprocess.getoutput('date -u | wc')
print(ret)

# A variant method called check_output() takes a list of the command and
# arguments. By default it only returns standard output as type bytes rather
# than a string and does not use the shell:

ret = subprocess.check_output(['date', '-u'])
print(ret)

# To show the exit status of the other program, getstatusoutput() returns a
# tuple with the status code and output:

ret = subprocess.getstatusoutput('date')
print(ret)

# (In Unix-like systems, 0 is usually the exit status for success.)

# If you only want the status and no output use call():

ret = subprocess.call('date')
print(ret)

# Create a Process with Multiprocessing:

# You can run a Python function as a separate process or run multiple
# independent processes in a single program with the multiprocessing module:

import multiprocessing
import os

def do_this(what):
     name(what)

def name(what):
    print("Process %s is: %s" % (os.getpid(), what))

if __name__ == "__main__":
    name("the main program")
    for n in range(4):
        p = multiprocessing.Process(target=do_this,
            args=("function %s" % n,))
        p.start()

# The Process() function spawned a new process and ran the do_this() function
# in it. Because we did this in a loop, we generated four new processes that
# executed do_this() and then exited.

# The intention is that you can spread out some task to multiple processes to
# save overall time; for example, downloading web pages for scraping, resizing
# images... It includes ways to queue tasks, enable intercommunication among
# processes, and wait for all the processes to finish.

# Kill a Process with Terminate()

# If you created one or more processes and want to terminate one for some reason
# (perhaps it's stuck in a loop), use terminate().

# In this example, the process would count to a thousand, sleeping at each
# step for a second, and printing a message. However, our main program will
# terminate it at 5 seconds:

import multiprocessing
import time
import os

def whoami(name):
    print('%s, in process %s' % (name, os.getpid()))

def counter(name):
    whoami(name)
    start = 1
    stop = 1000
    for num in range(start, stop):
        print('%s of %s' % (num, stop))
        time.sleep(1)

if __name__ == "__main__":
    whoami("main")
    p = multiprocessing.Process(target=counter, args=("counter",))
    p.start()
    time.sleep(5)
    p.terminate()
