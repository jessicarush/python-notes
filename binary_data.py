'''Binary data'''

# Formatting as binary, hex, octal -------------------------------------------

# {:b) will format numbers as binary (base 2):

for i in range(17):
    print("{0:>2} in binary is {0:>08b}".format(i))

# {:x} will format numbers as hex (base 16):

for i in range(17):
    print("{0:>2} in hex is {0:>02x}".format(i))

# {:o} as octal (base 8):

for i in range(17):
    print("{0:>2} in octal is {0:>4o}".format(i))

# Inputing binary, hex, octal ------------------------------------------------

w = 32        # normal number (base 10)
x = 0x20      # hexadecimal (base 16) starts with 0x
y = 0b100000  # binary number (base 2) starts with 0b
z = 0o40      # octal number (base 8) starts with 0o

print (w, x, y, z)  # 32 32 32 32

# Converting integers to binary, hex, octal ----------------------------------

x = hex(32)   # hexadecimal (base 16)
y = bin(32)   # binary number (base 2)
z = oct(32)   # octal number (base 8)

print (x, y, z)  # 0x20 0b100000 0o40

# bytes() and bytearray() ----------------------------------------------------

# These two objects are sequences of eight-bit integers, with possible values
# of 0 to 255:

a_list = [1, 2, 3, 255]
string = 'Sample Text'

list_bytes = bytes(a_list)  # returns b'\x01\x02\x03\xff'
string_bytes = bytes(string, 'utf-8')  # b'Sample Text'

list_array = bytearray(a_list)  # returns bytearray(b'\x01\x02\x03\xff')
string_array = bytearray(string, 'utf-8')  # bytearray(b'Sample Text')
print(string_array)

print(type(list_bytes))  # class 'bytes'
print(type(list_array))  # class 'bytearray'

list_array[1] = 127 # works because bytearray is mutable
# list_bytes[1] = 127    # doesn't work because bytes is immutable

# The representation of a bytes value begins with a b'' and a quote character,
# followed by hex sequences such as \x02 or ASCII characters, and ends with a
# matching quote character. When printing bytes or bytearray data, Python uses
# \x xx for non-printable bytes and their ASCII equivalents for printable ones
# (plus some common escape characters, such as \n).

# to_bytes() and from_bytes() ------------------------------------------------

# These two are methods that can be applied to integer objects

# to_bytes() - return an array of bytes representing an integer.

x = (1024).to_bytes(2, byteorder='big')
y = (1024).to_bytes(2, byteorder='little')

print("Using to_bytes:", x, y)  # Using to_bytes: b'\x04\x00' b'\x00\x04'
print(type(x)) # class 'bytes'

# from_bytes() - return the integer represented by the given array of bytes.

x = int.from_bytes(b'\x00\x10', byteorder='big')
y = int.from_bytes(b'\x00\x10', byteorder='little')

print("Using from_bytes:", x, y)  # Using from_bytes: 16 4096

# Convert Binary Data with struct --------------------------------------------

# The standard library contains the struct module. With it you can convert
# binary data to and from Python data structures.

# The following program will extract the width and height of an image from some
# PNG file data:

import struct

# valid_png contains the 8-byte sequence that marks the start of a valid PNG:

valid_png = b'\x89PNG\r\n\x1a\n'

# data contains the first 30 bytes from the PNG file:

data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR' + \
    b'\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'

if data[:8] == valid_png:
    # width is extracted from bytes 16-20, height from bytes 21-24:
    width, height = struct.unpack('>LL', data[16:24])
    print('Valid PNG, width', width, 'height', height)
else:
    print('Not a valid PNG')

# The >LL is the format string that instructs unpack() how to interpret its
# input byte sequences and assemble them into Python data types. The > means
# that integers are stored in big-endian format. Each L specifies a 4-byte
# unsigned long integer.

# You can examine each 4-byte value directly:

print(data[16:20])  # b'\x00\x00\x00\x9a'
print(data[20:24])  # b'\x00\x00\x00\x8d'

# struct.pack() --------------------------------------------------------------

# When you want to go the other way and convert Python data to bytes:

import struct

struct.pack('>L', 154)
struct.pack('>L', 141)

# Format specifiers for pack() and unpack()

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

# The type specifiers follow the endian character. Any specifier may be
# preceded by a number that indicates the count. 2L is the same as LL:

testing = struct.unpack('>2L', data[16:24])
print(testing)  # (154, 141)

# We used the slice data[16:24] to grab the interesting bytes directly.
# We could also use the x specifier to skip the uninteresting parts:

testing = struct.unpack('>16x2L6x', data)
print(testing)  # (154, 141)

# Use big endian integer format (>)
# Skip 16 bytes (16x)
# Read 8 bytes-two unsigned long integers (2L)
# Skip the final 6 bytes (6x)

# big endian and little endian -----------------------------------------------

# Big Endian Byte Order: The most significant byte (the "big end") of the data
# is placed at the byte with the lowest address. The rest of the data is placed
# in order in the next three bytes in memory.

# Little Endian Byte Order: The least significant byte (the "little end") of
# the data is placed at the byte with the lowest address. The rest of the data
# is placed in order in the next three bytes in memory

# https://en.wikipedia.org/wiki/Endianness

# To read and write binary files see files_read_write.py
