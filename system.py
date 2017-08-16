# Systems (Files, Directories, Programs and Processes)

# Python provides many operating system functions through a module named os
# Like many other languages, Python patterned its file operations after Unix.
# Some functions, such as chown() and chmod(), have the same names, but there
# are a few new ones.

# Create a file with open()
# open() function is used to open a file or create one if it doesn’t exist:

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

# Directories

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

# List Matching Files with glob()

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
