'''Unicode'''

# Note: Python 3 strings are Unicode strings not byte arrays.
# Therefor you can use unicode IDs or names in a string:

print('Caf\u00E9') # use \u for four hex numbers
print('Ghost: \U0001F47B') # use \U for eight hex numbers
print('Infinity: \N{INFINITY}') # use \N{name} for unicode names

# The python unicodedata module has functions that translate in both directions
# lookup() takes a case-insensitive name and returns the unicode character
# name() takes a unicode character and returns the upper case name

# This function will take a unicode character, look up its name, then look up
# the character again (it should match the original character)

def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value:', value, 'name:', name, 'value2:', value2)

unicode_test('A')
unicode_test('\u00E9')
unicode_test('∞')

# -----------------------------------------------------------------------------
# Encoding
# -----------------------------------------------------------------------------
# It's best to stick with UTF-8. Be careful when copying & pasting from other
# sources (such as web pages) into python strings as they ma be encoded in
# Latin-1 or Windows 1252. This will cause exceptions later.

# encode()
# The functions first arg is the encoding name such as:

character = '\u00E9'
#character.encode('ascii')          # seven-bit ASCII
character.encode('utf-8')           # eight bit variable length
character.encode('latin-1')         # also known as ISO 8859-1
character.encode('unicode-escape')  # Python unicode literal format

# encode() takes a second arg that avoids encoding exceptions
# (where the character doesn't exist in that set)

# throw away anything that won't encode:
character.encode('ascii', 'ignore')
# replace anything that won't encode with '?'
character.encode('ascii', 'replace')
# produce python unicode character string:
character.encode('ascii', 'backslashreplace')
# produce character entity for HTML:
character.encode('ascii', 'xmlcharrefreplace')

# -----------------------------------------------------------------------------
# Decoding
# -----------------------------------------------------------------------------
# We decode byte strings to Unicode strings. Whenever we get text from some
# external source (files, databases, websites), it's encoded as byte strings.
# The tricky part is knowing which encoding was actually used, so we can run it
# backward and get Unicode strings.

place = 'caf\u00e9' # a unicode string
print(type(place))

place_bytes = place.encode('utf-8')   # encoded to UTF-8
print(type(place_bytes))

# decode()

place2 = place_bytes.decode('utf-8')  # decode back to unicode
print(type(place2))

# This worked because we knew the original coding. If you decode with the wrong
# arg like ascii, you may get exceptions from illegal characters. In addition,
# there are some characters that aren't illegal... but aren't the same:

place3 = place_bytes.decode('latin-1')
print(place3)

# The bottom line: whenever possible use UTF-8
