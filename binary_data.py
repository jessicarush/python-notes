# Binary data

# bytes() and bytearray() are sequences of eight-bit integers, with possible values of 0 to 255:

blist = [1, 2, 3, 255]
the_bytes = bytes(blist)            # returns b'\x01\x02\x03\xff'
the_byte_array = bytearray(blist)   # returns bytearray(b'\x01\x02\x03\xff')

the_byte_array[1] = 127      # this works because bytearray is mutable (like a list of bytes)
the_bytes[1] = 127           # this doesn't work because is immutable (like a tuple of bytes)

# The representation of a bytes value begins with a b and a quote character, followed by hex 
# sequences such as \x02 or ASCII characters, and ends with a matching quote character. 
# When printing bytes or bytearray data, Python uses \x xx for non-printable bytes and their 
# ASCII equivalents for printable ones (plus some common escape characters, such as \n instead of \x0a).

# Convert Binary Data with struct

# The standard library contains the struct module. With it you can convert binary data to and from 
# Python data structures.

# The following program will extract the width and height of an image from some PNG file data:

import struct

# valid_png_header contains the 8-byte sequence that marks the start of a valid PNG:

valid_png_header = b'\x89PNG\r\n\x1a\n'

# data contains the first 30 bytes from the PNG file:

data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR' + \
    b'\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'

if data[:8] == valid_png_header:
    # width is extracted from bytes 16-20, height from bytes 21-24:
    width, height = struct.unpack('>LL', data[16:24])
    print('Valid PNG, width', width, 'height', height)
else:
    print('Not a valid PNG')

# The >LL is the format string that instructs unpack() how to interpret its input byte sequences and
# assemble them into Python data types. The > means that integers are stored in big-endian format. 
# Each L specifies a 4-byte unsigned long integer.

# You can examine each 4-byte value directly:

print(data[16:20])
print(data[20:24])

# When you want to go in the other direction and convert Python data to bytes, use the struct pack() function:

import struct

struct.pack('>L', 154)
struct.pack('>L', 141)

# Format specifiers fot pack() and unpack()

# <     little endian
# >     big endian

# x     skip a byte                 1 bytes
# b     signed byte                 1 bytes
# B     unsigned byte               1 bytes
# h     signed short integer        2 bytes
# H     unsigned short integer      2 bytes
# i     signed integer              4 bytes
# I     unsigned integer            4 bytes
# l     signed long integer         4 bytes
# L     unsigned long integer       4 bytes
# Q     unsigned long long integer  8 bytes
# f     single precision float      4 bytes
# d     double precision float      8 bytes
# p     count and characters        1 + count
# s     characters                  count

# The type specifiers follow the endian character. Any specifier may be preceded by a number 
# that indicates the count. 2L is the same as LL:

testing = struct.unpack('>2L', data[16:24])
print(testing)

# We used the slice data[16:24] to grab the interesting bytes directly. We could also use the 
# x specifier to skip the uninteresting parts:

testing = struct.unpack('>16x2L6x', data)
print(testing)

# Use big-endian integer format (>)
# Skip 16 bytes (16x)
# Read 8 bytes—two unsigned long integers (2L)
# Skip the final 6 bytes (6x)

# To read and write binary files see files_read_write.py
