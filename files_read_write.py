# Persistence ----------------------------------------------------------------

# In the context of storing data in a computer system, this means that the data
# survives after the process with which it was created has ended. In other
# words, for data to be considered persistent, it must write to non-volatile
# storage such as a disk (as opposed to memory).

# The simplest kind of persistence is a plain old file, sometimes called a flat
# file. This is just a sequence of bytes stored under a filename. You read from
# a file into memory and write from memory to a file.

# File Handling Basics -------------------------------------------------------

# Before reading or writing a file, you need to open it:

fileobject = open('filename.txt', 'w')

# The arg after the filename is the mode. The first letter indicates the operation:

# r  read - default mode if not specified
# w  write - if file doesn't exist, it's created. If exists, it's overwritten
# x  write - but only if the file does not already exist
# a  append - write after the end if the file exists

# The second letter of mode indicates the file type:

# t   text  - default type if not specified
# b   binary

# After opening a file, you call functions to read or write data, then you need
# to close the file:

fileobject.close()

# Close files automatically --------------------------------------------------

# using: with expression as variable

# If you forget to close a file that you've opened, you can end up wasting
# system resources or accidentally overwriting a file. Python has 'context
# managers' to clean up things such as open files:

with open('filename.txt', 'r') as fileobject:
    pass

# After the block of code completes (normally or by a raised exception),
# the file is closed automatically.

# write() --------------------------------------------------------------------

text1 = '...Some content...'
text2 = """
The Gashlycrumb Tinies - by Edward Gorey
A is for Amy who fell down the stairs.
B is for Basil assaulted by bears.
C is for Clair who wasted away.
D is for Desmond thrown out of the sleigh.
E is for Ernest who choked on a peach.
F is for Fanny, sucked dry by a leech.
G is for George, smothered under a rug.
H is for Hector, done in by a thug.
I is for Ida who drowned in the lake.
J is for James who took lye, by mistake.
K is for Kate who was struck with an axe.
L is for Leo who swallowed some tacks.
M is for Maud who was swept out to sea.
N is for Nevil who died of ennui.
O is for Olive, run through with an awl.
P is for Prue, trampled flat in a brawl.
Q is for Quinton who sank in a mire.
R is for Rhoda, consumed by a fire.
S is for Susan who perished of fits.
T is for Titas who blew into bits.
U is for Una who slipped down a drain.
V is for Victor, squashed under a train.
W is for Winie, embedded in ice.
X is for Xerxes, devoured by mice.
Y is for Yoric whose head was bashed in.
Z is for Zilla who drank too much gin.
The end
"""

# This writes the contents of text to the file testfile1:

with open('testfile1.txt', 'w') as fout:
    fout.write(text1)

# If you have a very large source string, you can write it in chunks:

with open('testfile1.txt', 'w') as fout:
    size = len(text2)
    offset = 0
    chunk = 100
    while True:
        if offset > size:
            break
        fout.write(text2[offset:offset+chunk])
        offset += chunk

# Test 'x' with our own exception handler:

try:
    fout = open('testfile1.txt', 'x')
    fout.write('stuff')
except FileExistsError:
    print('testfile1 file already exists!')


# print() to a file ----------------------------------------------------------

# You can also print to a text file. NOTE: when typing out file=fileoject, its
# actually the convention to NOT have spaces around the equals sign because
# these are named arguments as opposed to variable assignemnts. Same goes for
# sep='' and end='' coming up.

with open('testfile2.txt', 'w') as fout:
    print(text1, file=fout)

# When printing additional data to a file you'll get a space between each
# argument and a newline at the end. These are due to the following arguments:

# sep (separator, which defaults to a space ' ')
# end (end string, which defaults to a newline '\n')

# If you want to change these print() defaults:

with open('testfile2.txt', 'w') as fout:
    print(text1, file=fout, sep='', end='')

# read() ---------------------------------------------------------------------

# read() reads all contents of the file and returns a single string

with open('testfile1.txt', 'r') as fin:
    poem = fin.read()

# You can provide a max character count for how much is read in at a time.
# The following will read 100 characters at a time and append each chunk to
# the string:

poem = ''
with open('testfile1.txt', 'r') as fin:
    chunk = 100
    while True:
        fragment = fin.read(chunk)
        # As you read, write, Python keeps track of where you are in the file.
        if not fragment:
            break
        poem += fragment

# After you've read all the way to the end, further calls to read() will
# return an empty string (''), which is treated as False in 'if not fragment'.
# This breaks out of the while True loop.

# readline() -----------------------------------------------------------------

# this example does the same as above but feeds one line at a time instead of
# chunks of 100 characters:

poem = ''
with open('testfile1.txt', 'r') as fin:
    while True:
        line = fin.readline()
        if not line:
            break
        poem += line

# Another approach:

with open("testfile1.txt", 'r') as fin:
    line = fin.readline()
    while line:
        print(line, end='')
        line = fin.readline()

# Read a file by iterating ---------------------------------------------------

# The easiest way to read a text file is by using an iterator. This returns
# one line at a time... similar to previous examples but less code:

poem = ''
with open('testfile1.txt', 'r') as fin:
    for line in fin:
        poem += line

# a variation:

with open("testfile1.txt", 'r') as fin:
    for line in fin:
        if "by" in line.lower():
            print(line, end='')

# readlines() ----------------------------------------------------------------

# readlines() - the previous examples read and built up a single string.
# This call reads a line at a time and returns a list of one-line strings:

with open('testfile1.txt', 'r') as fin:
    lines = fin.readlines()
    print('Lines read: ', len(lines))
    for line in lines:
        print(line, end='')

# with readlines() you can go from the last line to the first:

with open("testfile1.txt", 'r') as fin:
    lines  = fin.readlines()
    for line in lines[::-1]:
        print(line, end='')

# NOTE: If you tried using fin.read() or fin.readline() in the above, all the
# letters would be printed in reverse, not just the lines.

# Binary Files ---------------------------------------------------------------

# Write a Binary file:

bdata = bytes(range(0, 256))

with open('testbinary', 'wb') as fout:
    fout.write(bdata)

# as with text you can write binary in chunks:

with open('testbinary', 'wb') as fout:
    size = len(bdata)
    offset = 0
    chunk = 100
    while True:
        if offset > size:
            break
        fout.write(bdata[offset:offset+chunk])
        offset += chunk

# read() a Binary file:

with open('testbinary', 'rb') as fin:
    bdata = fin.read()

# seek(), tell() -------------------------------------------------------------

# Reminder: As you read and write, Python keeps track of where you are in
# the file. The tell() function returns your current offset position in
# bytes. The seek() function lets you jump to another offset in the file.
# This means you don't have to read every byte in a file to read the last one.
# Note: seek() also returns the current offset.

with open('testbinary', 'rb') as fin:
    fin.tell()          # returns 0
    fin.seek(255)       # moves to one byte before the end of the file
    bdata = fin.read()  # reads the last byte
    len(bdata)          # returns 1

# You can call seek() with a second argument: seek(offset, origin)
# If origin is 0 (the default), move offset bytes from the start
# If origin is 1, move offset bytes from the current position
# If origin is 2, move offset bytes relative to the end

# So to get to the last byte we could also do:

with open('testbinary', 'rb') as fin:
    fin.seek(-1, 2)

# These functions are most useful for binary files. Though you can use them
# with text files, you would have a hard time calculating offsets as the
# most popular encoding (UTF-8) uses varying numbers of bytes per character.

# eval() ---------------------------------------------------------------------

# Problems can arise when trying to read data structure from files. Example:

unkle = ('The Road, Pt. 1', 'UNKLE', '2017', (
         (1, 'Inter 1'),
         (2, 'Farewell'),
         (3, 'Looking for the Rain'),
         (4, 'Cowboys or Indians')))

with open('music.txt', 'w') as music_file:
    print(unkle, file=music_file)

# the problem here is that there's no easy way to read the data in the file
# back in as a tuple because it's now just a string with brackets. That's when
# eval() can help:

with open ('music.txt', 'r') as music_file:
    music_contents = music_file.readline()

unkle = eval(music_contents)
album, artist, year, tracks = unkle # tuple unpacking
print(album)
print(tracks[3])

# truncate() -----------------------------------------------------------------

# filename.truncate() - Empties the file
