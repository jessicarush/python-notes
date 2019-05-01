'''Binary data and Unicode Strings'''


# Unicode
# -----------------------------------------------------------------------------
# Note: in Python 3 strings (str) are Unicode strings and bytes are raw 8-bit
# values. In Python 2, strings are raw 8-bit values and instances of unicode
# contain Unicode characters.

# Therefor in Python 3 you can use unicode IDs or names in a string:

print('Caf\u00E9')               # use \u for four hex numbers
print('Ghost: \U0001F47B')       # use \U for eight hex numbers
print('Infinity: \N{INFINITY}')  # use \N{name} for unicode names

# The python unicodedata module has functions that translate in both directions
# lookup() takes a case-insensitive name and returns the unicode character
# name() takes a unicode character and returns the upper case name

# This function will take a unicode character, look up its name, then look up
# the character again (it should match the original character)

import unicodedata


def unicode_test(value):
    '''Unicode character name lookup function.'''
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print(value, '–', name, '–', value2)


unicode_test('A')       # A – LATIN CAPITAL LETTER A – A
unicode_test('\u00E9')  # é – LATIN SMALL LETTER E WITH ACUTE – é
unicode_test('∞')       # ∞ – INFINITY – ∞


# Encoding
# -----------------------------------------------------------------------------
# Using a string's encode() method, you can convert unicoded strings into any
# encodings supported by Python. By default, Python uses utf-8 encoding and
# it's best to stick with UTF-8.

# Be careful when copying & pasting from other sources (such as web pages)
# into python strings as they may be encoded in Latin-1 or Windows 1252.
# This will cause exceptions later.

# The encode() functions first arg is the encoding name such as:

string = 'hello'
string.encode('ascii')               # seven-bit ASCII
string.encode('latin-1')             # also known as ISO 8859-1
string.encode('unicode-escape')      # Python unicode literal format
string.encode('utf-8')               # eight bit variable length

print(type(string.encode('utf-8')))  # <class 'bytes'>

# encode() takes a second arg that avoids encoding exceptions where the
# character doesn't exist in that set.

string = 'hello \u00E9'

# throw away anything that won't encode:
print(string.encode('ascii', 'ignore'))
# b'hello '

# replace anything that won't encode with '?'
print(string.encode('ascii', 'replace'))
# b'hello ?'

# replace anything that won't encode with its name
print(string.encode('ascii', 'namereplace'))
# b'hello \N{LATIN SMALL LETTER E WITH ACUTE}'

# produce character entity for HTML:
print(string.encode('ascii', 'xmlcharrefreplace'))
# b'hello &#233;'

# produce python unicode character string:
test = string.encode('ascii', 'backslashreplace')
print(test)
# b'hello \\xe9'

print('hello \xe9')
# hello é


# Decoding
# -----------------------------------------------------------------------------
# We decode byte strings to Unicode strings. Whenever we get text from some
# external source (files, databases, websites), it's encoded as byte strings.
# The tricky part is knowing which encoding was actually used, so we can run
# it backward and get Unicode strings.

place = 'caf\u00e9'                   # a unicode string
print(type(place))                    # <class 'str'>

place_bytes = place.encode('utf-8')   # encoded to UTF-8
print(type(place_bytes))              # <class 'bytes'>

place2 = place_bytes.decode('utf-8')  # decode back to unicode
print(type(place2))                   # <class 'str'>

# This worked because we knew the original coding. If you decode with the wrong
# arg like ascii, you may get exceptions from illegal characters. In addition,
# there are some characters that aren't illegal... but aren't the same:

place3 = place_bytes.decode('latin-1')
print(place3)  # cafÃ©

# The bottom line: whenever possible use UTF-8


# Example: helper functions
# -----------------------------------------------------------------------------
# You'll often need two helper functions that ensure the type of input values
# matches your codes expectations.

def to_str(bytes_or_str):
    '''Takes a str or bytes and always returns a str.'''
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value


def to_bytes(bytes_or_str):
    '''Takes a str or bytes and always returns a bytes.'''
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value


# Formatting as binary, hex, octal
# -----------------------------------------------------------------------------
# {:b} will format numbers as binary (base 2):

for i in range(17):
    print("{0:>2} in binary is {0:>08b}".format(i))

# {:x} will format numbers as hex (base 16):

for i in range(17):
    print("{0:>2} in hex is {0:>02x}".format(i))

# {:o} as octal (base 8):

for i in range(17):
    print("{0:>2} in octal is {0:>4o}".format(i))


# Integers from binary, hex, octal format
# -----------------------------------------------------------------------------

n = 32             # normal number (base 10)
h = 0x20           # hexadecimal (base 16) starts with 0x
b = 0b100000       # binary (base 2) starts with 0b
o = 0o40           # octal (base 8) starts with 0o

print(n, type(n))  # 32 <class 'int'>
print(h, type(h))  # 32 <class 'int'>
print(b, type(b))  # 32 <class 'int'>
print(o, type(o))  # 32 <class 'int'>


# Converting integers to binary, hex, octal strings
# -----------------------------------------------------------------------------

h = hex(32)        # hexadecimal (base 16)
b = bin(32)        # binary (base 2)
o = oct(32)        # octal (base 8)

print(h, type(h))  # 0x20 <class 'str'>
print(b, type(b))  # 0b100000 <class 'str'>
print(o, type(o))  # 0o40 <class 'str'>


# to_bytes() and from_bytes()
# -----------------------------------------------------------------------------
# These two are methods that can be used with integer objects.
# to_bytes() will return an array of bytes representing an integer.
# The first arg is the length, the second declares the byteorder (see below).

x = (1024).to_bytes(2, byteorder='big')
y = (1024).to_bytes(2, byteorder='little')

print("to_bytes:", x, y)
# to_bytes: b'\x04\x00' b'\x00\x04'

x = (1024).to_bytes(10, byteorder='big')
y = (1024).to_bytes(10, byteorder='little')

print("big endian bytes:", x)
print("little endian bytes:", y)
# big endian bytes:    b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00'
# little endian bytes: b'\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00'

print(type(x))
# class 'bytes'

# Note that if you don't specify a length large enough to accomade the number,
# you'll get a OverflowError: int too big to convert

# from_bytes() - return the integer represented by the given array of bytes.

x = int.from_bytes(b'\x04\x00', byteorder='big')
y = int.from_bytes(b'\x00\x04', byteorder='little')

print("from_bytes:", x, y)
# from_bytes: 1024 1024

x = int.from_bytes(b'\x04\x00', byteorder='little')
y = int.from_bytes(b'\x00\x04', byteorder='big')

print("from_bytes:", x, y)
# from_bytes: 4 4


# big endian and little endian
# -----------------------------------------------------------------------------
# Big Endian Byte Order: The most significant byte (the "big end") of the data
# is placed at the byte with the lowest address. The rest of the data is placed
# in order in the next three bytes in memory.

# Little Endian Byte Order: The least significant byte (the "little end") of
# the data is placed at the byte with the lowest address. The rest of the data
# is placed in order in the next three bytes in memory.

# https://en.wikipedia.org/wiki/Endianness


# bytes() and bytearray()
# -----------------------------------------------------------------------------
# These two objects are sequences of eight-bit integers, with possible values
# of 0 to 255. The main difference between them is that bytearray() is mutable
# while bytes() is not.

a_list = [1, 2, 3, 255]
string = 'Sample Text'

list_bytes = bytes(a_list)                     # b'\x01\x02\x03\xff'
string_bytes = bytes(string, 'utf-8')          # b'Sample Text'

list_bytearray = bytearray(a_list)             # bytearray(b'\x01\x02\x03\xff')
string_bytearray = bytearray(string, 'utf-8')  # bytearray(b'Sample Text')

print(type(list_bytes))                        # class 'bytes'
print(type(list_bytearray))                    # class 'bytearray'

list_bytearray[1] = 127  # works because bytearray is mutable
# list_bytes[1] = 127    # doesn't work because bytes is immutable

# The representation of a bytes value begins with a b' and a quote character,
# followed by hex sequences such as \x02 or ASCII characters, and ends with a
# matching quote character. When printing bytes or bytearray data, Python uses
# \x xx for non-printable bytes and their ASCII equivalents for printable ones
# (plus some common escape characters, such as \n).

# See also:
# https://en.wikiversity.org/wiki/Python_Concepts/Bytes_objects_and_Bytearrays


# Convert Binary Data with struct
# -----------------------------------------------------------------------------
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


# struct.pack()
# -----------------------------------------------------------------------------
# When you want to go the other way and convert Python data to bytes:

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


# Summary
# -----------------------------------------------------------------------------

some_string = 'hello'      # <class 'str'>
some_bytes = b'hello'      # <class 'bytes'>
some_num = 31              # <class 'int'>
some_binary_num = b'\x1f'  # <class 'bytes'>

# encode() and decode()
encoded = some_string.encode('utf-8')  # <class 'bytes'>
decoded = some_bytes.decode('utf-8')   # <class 'str'>

# bytes() and bytearray()
bytes_instance = bytes(some_string, 'utf-8')          # <class 'bytes'>
bytearray_instance = bytearray(some_string, 'utf-8')  # <class 'bytearray'>

# to_bytes() and from_bytes()
x = some_num.to_bytes(1, byteorder='big')             # <class 'bytes'>
y = int.from_bytes(some_binary_num, byteorder='big')  # <class 'int'>

# struct.pack() and struct.unpack()
packed = struct.pack('>L', some_num)
unpacked = struct.unpack('>5s', some_bytes)

print(packed, type(packed))      # b'\x00\x00\x00\x1f' <class 'bytes'>
print(unpacked, type(unpacked))  # (b'hello',) <class 'tuple'>


# Next review: clarify the differences between these.


# To read and write binary files see files_read_write.py
