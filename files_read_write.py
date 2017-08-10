# Persistence

# In the context of storing data in a computer system, this means that the data
# survives after the process with which it was created has ended. In other words,
# for data to be considered persistent, it must write to non-volatile storage
# such as a disk (as opposed to memory).

# The simplest kind of persistence is a plain old file, sometimes called a flat
# file. This is just a sequence of bytes stored under a filename. You read from
# a file into memory and write from memory to a file.

# Before reading or writing a file, you need to open it:

fileobject = open('filename', 'r')

# The arg after the filename is the mode. The first letter indicates the operation:

# r    read - default mode if not specified
# w    write - if file doesn't exist, it's created. If file does exist, is overwritten
# x    write - but only if the file does not already exist
# a    append - write after the end if the file exists

# The second letter of mode indicates the file type:

# t   text  - default type if not specified
# b   binary

# After opening a file, you call functions to read or write data, then you need to close the file:

fileobject.close()

# Testing: 

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

"""

# This writes the contents of text to the file testfile1:

fout = open('testfile1', 'w')
fout.write(text1)
fout.close()

# You can also print to a text file:

fout = open('testfile2', 'w')
print(text1, file=fout)
fout.close()

# When printing additional data to a file you'll get a space between each
# argument and a newline at the end. These are due to the following arguments:

# sep (separator, which default to a space ' ')
# end (end string, which defaults to a newline '\n')

# If you want print() to write like write() do this:

fout = open('testfile2', 'w')
print(text1, file=fout, sep='', end='')
fout.close()

# If you have a very large source string, you can write it in chunks:

fout = open('testfile1', 'w')
size = len(text2)
offset = 0
chunk = 100

while True:
    if offset > size:
        break
    fout.write(text2[offset:offset+chunk])
    offset += chunk

fout.close()

# Test 'x' with our own exception handler:

try:
    fout = open('testfile1', 'x')
    fout.write('stuff')
except FileExistsError:
    print('testfile1 file already exists!')

# read()

fin = open('testfile1', 'r')
poem = fin.read()
fin.close()

# You can provide a max character count for how much is read in at a time.
# The following will read 100 characters at a time and append each chunk to a string:

poem = ''
fin = open('testfile1', 'r')
chunk = 100

while True:
    fragment = fin.read(chunk)
    # As you read and write, Python keeps track of where you are in the file.
    if not fragment:
        break
    poem += fragment

fin.close()

# After you’ve read all the way to the end, further calls to read() will
# return an empty string (''), which is treated as False in if not fragment.
# This breaks out of the while True loop.

# readline() - this example does the same as above but feeds one line at a
# time instead of chunks of 100 characters:

poem = ''
fin = open('testfile1', 'r')

while True:
    line = fin.readline()
    if not line:
        break
    poem += line

fin.close()

# The easiest way to read a text file is by using an iterator. This returns 
# one line at a time... similar to previous example but less code:

poem = ''
fin = open('testfile1', 'r')

for line in fin:
    poem += line

fin.close()

# readlines() - the previous examples read and built up a single string.
# This call reads a line t a time and returns a list of one-line strings:

fin = open('testfile1', 'r')
lines = fin.readlines()
fin.close()

# Testing:

print('Lines read: ', len(lines))
for line in lines:
    print(line, end='')

# Write a Binary file:

bdata = bytes(range(0, 256))

fout = open('testbinary', 'wb')
fout.write(bdata)
fout.close()

# as with text you can write binary in chunks:

fout = open('testbinary', 'wb')
size = len(bdata)
offset = 0
chunk = 100

while True:
    if offset > size:
        break
    fout.write(bdata[offset:offset+chunk])
    offset += chunk

fout.close()

# read() a Binary file:

fin = open('testbinary', 'rb')
bdata = fin.read()
fin.close()

# Close files automatically using: with expression as variable

# If you forget to close a file that you’ve opened, you can end up wasting
# system resources or accidentally overwriting a file. Python has 'context
# managers' to clean up things such as open files:

with open('testfile2', 'w') as fout:
    fout.write(text1)

# After the block of code completes (normally or by a raised exception), the 
# file is closed automatically.

# seek(), tell()

# Reminder: As you read and write, Python keeps track of where you are in
# the file. The tell() function returns your current offset position in
# bytes. The seek() function lets you jump to another offset in the file.
# This means you don’t have to read every byte in a file to read the last one.
# Note: seek() also returns the current offset.

fin = open('testbinary', 'rb')
fin.tell()          # returns 0
fin.seek(255)       # moves to one byte before the end of the file
bdata = fin.read()  # reads the last byte
len(bdata)          # returns 1
fin.close()

# You can call seek() with a second argument: seek(offset, origin)
# If origin is 0 (the default), move offset bytes from the start
# If origin is 1, move offset bytes from the current position
# If origin is 2, move offset bytes relative to the end

# So to get to the last byte we could also do:

fin = open('testbinary', 'rb')
fin.seek(-1, 2)
fin.close()

# These functions are most useful for binary files. Though you can use them
# with text files, you would have a hard time calculating offsets as the
# most popular encoding (UTF-8) uses varying numbers of bytes per character.

# filename.truncate() - Empties the file.
